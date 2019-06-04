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
# For ensuring that the mock objects in your tests have the same api as the objects they are replacing, you can use auto-speccing. Auto-speccing can be done
# through the autospec argument to patch, or the create_autospec() function. Auto-speccing creates mock objects that have the same attributes and methods as
# the objects they are replacing, and any functions and methods (including constructors) have the same call signature as the real object.
# 
# This ensures that your mocks will fail in the same way as your production code if they are used incorrectly:
# 

from unittest.mock import create_autospec

def function(a, b, c):
        pass

mock_function = create_autospec(function, return_value='fishy')

mock_function(1, 2, 3)

# OUTPUT: 'fishy'

mock_function.assert_called_once_with(1, 2, 3)

mock_function('wrong arguments')
