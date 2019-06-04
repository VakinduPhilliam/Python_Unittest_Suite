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
# Checking multiple calls with mock:
# mock has a nice API for making assertions about how your mock objects are used.
# 

mock = Mock()

mock.foo_bar.return_value = None
mock.foo_bar('baz', spam='eggs')

mock.foo_bar.assert_called_with('baz', spam='eggs')
 
#
# If your mock is only being called once you can use the assert_called_once_with() method that also asserts that the call_count is one.
# 

mock.foo_bar.assert_called_once_with('baz', spam='eggs')

mock.foo_bar()
mock.foo_bar.assert_called_once_with('baz', spam='eggs')

#
# Both assert_called_with and assert_called_once_with make assertions about the most recent call.
# If your mock is going to be called several times, and you want to make assertions about all those calls you can use call_args_list:
# 

mock = Mock(return_value=None)

mock(1, 2, 3)
mock(4, 5, 6)

mock()

mock.call_args_list

# OUTPUT: '[call(1, 2, 3), call(4, 5, 6), call()]'
 
#
# The call helper makes it easy to make assertions about these calls.
# You can build up a list of expected calls and compare it to call_args_list.
# This looks remarkably similar to the repr of the call_args_list:
# 

expected = [call(1, 2, 3), call(4, 5, 6), call()]

mock.call_args_list == expected

# OUTPUT: 'True'
