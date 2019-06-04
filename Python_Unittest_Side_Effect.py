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

# side_effect: 
#
# This can either be a function to be called when the mock is called, an iterable or an exception (class or instance) to be raised.
# If you pass in a function it will be called with same arguments as the mock and unless the function returns the DEFAULT singleton the call to the mock
# will then return whatever the function returns. If the function returns DEFAULT then the mock will return its normal value (from the return_value).
# If you pass in an iterable, it is used to retrieve an iterator which must yield a value on every call. This value can either be an exception instance to
# be raised, or a value to be returned from the call to the mock (DEFAULT handling is identical to the function case).

# 
# An example of a mock that raises an exception (to test exception handling of an API):
# 

mock = Mock()
mock.side_effect = Exception('Boom!')

mock()

#
# Using side_effect to return a sequence of values:
# 

mock = Mock()
mock.side_effect = [3, 2, 1]

mock(), mock(), mock()

# OUTPUT: '(3, 2, 1)'

# 
# Using a callable:
# 

mock = Mock(return_value=3)

def side_effect(*args, **kwargs):
        return DEFAULT

mock.side_effect = side_effect
mock()

# OUTPUT: '3'
 
#
# side_effect can be set in the constructor.
#

#
# Here’s an example that adds one to the value the mock is called with and returns it:
# 

side_effect = lambda value: value + 1

mock = Mock(side_effect=side_effect)
mock(3)

# OUTPUT: '4'

mock(-8)

# OUTPUT: '-7'
 
#
# Setting side_effect to None clears it:
# 

m = Mock(side_effect=KeyError, return_value=3)
m()


m.side_effect = None
m()

# OUTPUT: '3'
