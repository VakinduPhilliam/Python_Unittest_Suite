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
# call_args_list: 
# This is a list of all the calls made to the mock object in sequence (so the length of the list is the number of times it has been called).
# Before any calls have been made it is an empty list. The call object can be used for conveniently constructing lists of calls to compare with
# call_args_list.
# 

mock = Mock(return_value=None)
mock()

mock(3, 4)
mock(key='fish', next='w00t!')

mock.call_args_list

# OUTPUT: '[call(), call(3, 4), call(key='fish', next='w00t!')]'

expected = [(), ((3, 4),), ({'key': 'fish', 'next': 'w00t!'},)]

mock.call_args_list == expected

# OUTPUT: 'True'
