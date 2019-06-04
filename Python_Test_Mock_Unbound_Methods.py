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
# Mocking Unbound Methods:
# Whilst writing tests today I needed to patch an unbound method (patching the method on the class rather than on the instance).
# I needed self to be passed in as the first argument because I want to make asserts about which objects were calling this particular method.
# The issue is that you can’t patch with a mock for this, because if you replace an unbound method with a mock it doesn’t become a bound method when fetched
# from the instance, and so it doesn’t get self passed in.
# The workaround is to patch the unbound method with a real function instead.
# The patch() decorator makes it so simple to patch out methods with a mock that having to create a real function becomes a nuisance.
#

# 
# If you pass autospec=True to patch then it does the patching with a real function object.
# This function object has the same signature as the one it is replacing, but delegates to a mock under the hood.
# You still get your mock auto-created in exactly the same way as before.
# What it means though, is that if you use it to patch out an unbound method on a class the mocked function will be turned into a bound method if it is
# fetched from an instance.
# It will have self passed in as the first argument, which is exactly what I wanted:
# 

class Foo:
      def foo(self):
          pass

with patch.object(Foo, 'foo', autospec=True) as mock_foo:
      mock_foo.return_value = 'foo'

      foo = Foo()

      foo.foo()

# OUTPUT: 'foo'

mock_foo.assert_called_once_with(foo)
