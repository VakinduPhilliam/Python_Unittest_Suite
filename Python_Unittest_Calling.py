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
# Calling
# Mock objects are callable. The call will return the value set as the return_value attribute. The default return value is a new Mock object; it is created
# the first time the return value is accessed (either explicitly or by calling the Mock) - but it is stored and the same one returned each time.
# Calls made to the object will be recorded in the attributes like call_args and call_args_list.
# If side_effect is set then it will be called after the call has been recorded, so if side_effect raises an exception the call is still recorded.

# 
# The simplest way to make a mock raise an exception when called is to make side_effect an exception class or instance:
# 

m = MagicMock(side_effect=IndexError)
m(1, 2, 3)

m.mock_calls

# OUTPUT: '[call(1, 2, 3)]'

m.side_effect = KeyError('Bang!')
m('two', 'three', 'four')

m.mock_calls

# OUTPUT: '[call(1, 2, 3), call('two', 'three', 'four')]'
