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
# Nesting Patches:
# Using patch as a context manager is nice, but if you do multiple patches you can end up with nested with statements indenting further and further to the
# right:
# 

class MyTest(TestCase):

        def test_foo(self):

            with patch('mymodule.Foo') as mock_foo:

                with patch('mymodule.Bar') as mock_bar:

                    with patch('mymodule.Spam') as mock_spam:

                        assert mymodule.Foo is mock_foo

                        assert mymodule.Bar is mock_bar

                       assert mymodule.Spam is mock_spam

original = mymodule.Foo

MyTest('test_foo').test_foo()

assert mymodule.Foo is original

# 
# With unittest cleanup functions and the patch methods: start and stop we can achieve the same effect without the nested indentation.
#
# A simple helper method, create_patch, puts the patch in place and returns the created mock for us:
# 

class MyTest(TestCase):

       def create_patch(self, name):
            patcher = patch(name)

            thing = patcher.start()

            self.addCleanup(patcher.stop)

            return thing

        def test_foo(self):
            mock_foo = self.create_patch('mymodule.Foo')

            mock_bar = self.create_patch('mymodule.Bar')
            mock_spam = self.create_patch('mymodule.Spam')

            assert mymodule.Foo is mock_foo

            assert mymodule.Bar is mock_bar
            assert mymodule.Spam is mock_spam

original = mymodule.Foo

MyTest('test_foo').run()

assert mymodule.Foo is original
