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
# Mock allows you to assign functions (or other Mock instances) to magic methods and they will be called appropriately.
# The MagicMock class is just a Mock variant that has all of the magic methods pre-created for you (well, all the useful ones anyway).
# 
# The following is an example of using magic methods with the ordinary Mock class:
# 

mock = Mock()
mock.__str__ = Mock(return_value='wheeeeee')

str(mock)

# OUTPUT: 'wheeeeee'
