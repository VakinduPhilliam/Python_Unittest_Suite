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
# A callable mock which was created with a spec (or a spec_set) will introspect the specification object’s signature when matching calls to the mock.
# Therefore, it can match the actual call’s arguments regardless of whether they were passed positionally or by name:
#
 
#
# This applies to assert_called_with(), assert_called_once_with(), assert_has_calls() and assert_any_call().
# When Autospeccing, it will also apply to method calls on the mock object.
#

def f(a, b, c): pass

mock = Mock(spec=f)
mock(1, 2, c=3)

# OUTPUT: '<Mock name='mock()' id='140161580456576'>'

mock.assert_called_with(1, 2, 3)

mock.assert_called_with(a=1, b=2, c=3)
