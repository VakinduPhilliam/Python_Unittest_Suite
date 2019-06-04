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
# method_calls: 
# As well as tracking calls to themselves, mocks also track calls to methods and attributes, and their methods and attributes:
#

# 
# Members of method_calls are call objects. These can be unpacked as tuples to get at the individual arguments.
#

mock = Mock()
mock.method()

# OUTPUT: '<Mock name='mock.method()' id='...'>'

mock.property.method.attribute()

# OUTPUT: '<Mock name='mock.property.method.attribute()' id='...'>'

mock.method_calls

# OUTPUT: '[call.method(), call.property.method.attribute()]'
