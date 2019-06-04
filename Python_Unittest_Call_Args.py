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
# call_args: 
# This is either None (if the mock hasn’t been called), or the arguments that the mock was last called with.
# This will be in the form of a tuple: the first member is any ordered arguments the mock was called with (or an empty tuple) and the second member is any
# keyword arguments (or an empty dictionary).
# 
# 
# call_args, along with members of the lists call_args_list, method_calls and mock_calls are call objects.
# These are tuples, so they can be unpacked to get at the individual arguments and make more complex assertions. 
#

mock = Mock(return_value=None)

print(mock.call_args)

# OUTPUT: 'None'

mock()
mock.call_args

# OUTPUT: 'call()'

mock.call_args == ()

# OUTPUT: 'True'

mock(3, 4)
mock.call_args

# OUTPUT: 'call(3, 4)'

mock.call_args == ((3, 4),)

# OUTPUT: 'True'

mock(3, 4, 5, key='fish', next='w00t!')
mock.call_args

# OUTPUT: 'call(3, 4, 5, key='fish', next='w00t!')'

