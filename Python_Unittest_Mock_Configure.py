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
# configure_mock(**kwargs). 
# Set attributes on the mock through keyword arguments.
# 

#
# Attributes plus return values and side effects can be set on child mocks using standard dot notation and unpacking a dictionary in the method call:
# 

mock = Mock()

attrs = {'method.return_value': 3, 'other.side_effect': KeyError}

mock.configure_mock(**attrs)
mock.method()

# OUTPUT: '3'

mock.other()

#
# The same thing can be achieved in the constructor call to mocks:
# 

attrs = {'method.return_value': 3, 'other.side_effect': KeyError}
mock = Mock(some_attribute='eggs', **attrs)

mock.some_attribute

# OUTPUT: 'eggs'

mock.method()

# OUTPUT: '3'

mock.other()
