# Python Unittest
# unittest.mock — mock object library
# unittest.mock is a library for testing in Python.
# It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
# unittest.mock provides a core Mock class removing the need to create a host of stubs throughout your test suite.
# After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with.
# You can also specify return values and set needed attributes in the normal way.
# 
# Additionally, mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test, along with sentinel
# for creating unique objects.
# 
# Mock is very easy to use and is designed for use with unittest. Mock is based on the ‘action -> assertion’ pattern instead of ‘record -> replay’ used by
# many mocking frameworks.
#

#
# patch methods: start and stop.
# All the patchers have start() and stop() methods.
# These make it simpler to do patching in setUp methods or where you want to do multiple patches without nesting decorators or with statements.
# To use them call patch(), patch.object() or patch.dict() as normal and keep a reference to the returned patcher object.
# You can then call start() to put the patch in place and stop() to undo it.
# If you are using patch() to create a mock for you then it will be returned by the call to patcher.start.
# 

patcher = patch('package.module.ClassName')

from package import module

original = module.ClassName

new_mock = patcher.start()

assert module.ClassName is not original
assert module.ClassName is new_mock

patcher.stop()

assert module.ClassName is original
assert module.ClassName is not new_mock

# 
# A typical use case for this might be for doing multiple patches in the setUp method of a TestCase:
# 

class MyTest(TestCase):

        def setUp(self):
            self.patcher1 = patch('package.module.Class1')
            self.patcher2 = patch('package.module.Class2')

            self.MockClass1 = self.patcher1.start()
            self.MockClass2 = self.patcher2.start()

        def tearDown(self):
            self.patcher1.stop()
            self.patcher2.stop()

        def test_something(self):
            assert package.module.Class1 is self.MockClass1
            assert package.module.Class2 is self.MockClass2

MyTest('test_something').run()
 
#
# Caution:
# If you use this technique you must ensure that the patching is “undone” by calling stop.
# This can be fiddlier than you might think, because if an exception is raised in the setUp then tearDown is not called.
# unittest.TestCase.addCleanup() makes this easier:
# 

class MyTest(TestCase):
        def setUp(self):
            patcher = patch('package.module.Class')

            self.MockClass = patcher.start()
            self.addCleanup(patcher.stop)

        def test_something(self):
            assert package.module.Class is self.MockClass
