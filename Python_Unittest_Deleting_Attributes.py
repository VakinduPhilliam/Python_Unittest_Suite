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
# Deleting Attributes:
# 
# Mock objects create attributes on demand. This allows them to pretend to be objects of any type.
# You may want a mock object to return False to a hasattr() call, or raise an AttributeError when an attribute is fetched.
# You can do this by providing an object as a spec for a mock, but that isn’t always convenient.
# 
# You “block” attributes by deleting them. Once deleted, accessing an attribute will raise an AttributeError.
# 

mock = MagicMock()

hasattr(mock, 'm')

# OUTPUT: 'True'

del mock.m

hasattr(mock, 'm')

# OUTPUT: 'False'

del mock.f

mock.f
