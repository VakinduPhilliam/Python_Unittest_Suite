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
# return_value 
# Set this to configure the value returned by calling the mock:
# 

mock = Mock()
mock.return_value = 'fish'

mock()

# OUTPUT: 'fish'
 
#
# The default return value is a mock object and you can configure it in the normal way:
# 

mock = Mock()
mock.return_value.attribute = sentinel.Attribute

mock.return_value()

# OUTPUT: '<Mock name='mock()()' id='...'>'

mock.return_value.assert_called_with()

# 
# return_value can also be set in the constructor:
# 

mock = Mock(return_value=3)
mock.return_value

# OUTPUT: '3'

mock()

# OUTPUT: '3'
