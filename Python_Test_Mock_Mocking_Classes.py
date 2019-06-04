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
# Mocking Classes:
# A common use case is to mock out classes instantiated by your code under test.
# When you patch a class, then that class is replaced with a mock. Instances are created by calling the class.
# This means you access the “mock instance” by looking at the return value of the mocked class.
 
#
# In the example below we have a function some_function that instantiates Foo and calls a method on it.
# The call to patch() replaces the class Foo with a mock.
# The Foo instance is the result of calling the mock, so it is configured by modifying the mock return_value.
# 

def some_function():
        instance = module.Foo()

        return instance.method()

with patch('module.Foo') as mock:
        instance = mock.return_value
        instance.method.return_value = 'the result'

        result = some_function()

        assert result == 'the result'
