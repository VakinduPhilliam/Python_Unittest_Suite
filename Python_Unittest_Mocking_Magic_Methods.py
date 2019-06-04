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
# Mocking Magic Methods:
# Mock supports mocking the Python protocol methods, also known as “magic methods”.
# This allows mock objects to replace containers or other objects that implement Python protocols.
# Because magic methods are looked up differently from normal methods, this support has been specially implemented. This means that only specific magic
# methods are supported.
#
# The supported list includes almost all of them. If there are any missing that you need please let us know.
# 

#
# You mock magic methods by setting the method you are interested in to a function or a mock instance.
# If you are using a function then it must take self as the first argument.
# 

def __str__(self):
        return 'fooble'

mock = Mock()
mock.__str__ = __str__

str(mock)

# OUTPUT: 'fooble'
 

mock = Mock()
mock.__str__ = Mock()

mock.__str__.return_value = 'fooble'

str(mock)

# OUTPUT: 'fooble'
 

mock = Mock()
mock.__iter__ = Mock(return_value=iter([]))

list(mock)

# OUTPUT: '[]'

# 
# One use case for this is for mocking objects used as context managers in a with statement:
# 

mock = Mock()
mock.__enter__ = Mock(return_value='foo')

mock.__exit__ = Mock(return_value=False)

with mock as m:
        assert m == 'foo'

mock.__enter__.assert_called_with()

mock.__exit__.assert_called_with(None, None, None)
