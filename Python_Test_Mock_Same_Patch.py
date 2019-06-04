# Python Test Mock
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
# Applying the same patch to every test method:
# 
# If you want several patches in place for multiple test methods the obvious way is to apply the patch decorators to every method.
# This can feel like unnecessary repetition. For Python 2.6 or more recent you can use patch() (in all its various forms) as a class decorator.
# This applies the patches to all test methods on the class.
# A test method is identified by methods whose names start with test:
# 

@patch('mymodule.SomeClass')

    class MyTest(TestCase):

        def test_one(self, MockSomeClass):
            self.assertIs(mymodule.SomeClass, MockSomeClass)

        def test_two(self, MockSomeClass):
            self.assertIs(mymodule.SomeClass, MockSomeClass)

        def not_a_test(self):
            return 'something'

MyTest('test_one').test_one()
MyTest('test_two').test_two()

MyTest('test_two').not_a_test()

# OUTPUT: 'something'
 
#
# An alternative way of managing patches is to use the patch methods: start and stop.
# These allow you to move the patching into your setUp and tearDown methods.
# 

class MyTest(TestCase):

        def setUp(self):
            self.patcher = patch('mymodule.foo')

            self.mock_foo = self.patcher.start()

        def test_foo(self):
            self.assertIs(mymodule.foo, self.mock_foo)

        def tearDown(self):
            self.patcher.stop()

MyTest('test_foo').run()

# 
# If you use this technique you must ensure that the patching is “undone” by calling stop.
# This can be fiddlier than you might think, because if an exception is raised in the setUp then tearDown is not called. unittest.TestCase.addCleanup()
# makes this easier:
# 

class MyTest(TestCase):

        def setUp(self):
            patcher = patch('mymodule.foo')

            self.addCleanup(patcher.stop)
            self.mock_foo = patcher.start()

        def test_foo(self):
            self.assertIs(mymodule.foo, self.mock_foo)

MyTest('test_foo').run()
