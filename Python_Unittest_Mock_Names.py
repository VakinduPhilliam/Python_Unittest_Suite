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
# Mock names and the name attribute.
# Since “name” is an argument to the Mock constructor, if you want your mock object to have a “name” attribute you can’t just pass it in at creation time.
# There are two alternatives.
# One option is to use configure_mock():
# 

mock = MagicMock()
mock.configure_mock(name='my_name')

mock.name

# OUTPUT: 'my_name'
 
#
# A simpler option is to simply set the “name” attribute after mock creation:
# 

mock = MagicMock()
mock.name = "foo"
