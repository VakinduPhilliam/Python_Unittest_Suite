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
# __class__: 
# Normally the __class__ attribute of an object will return its type. For a mock object with a spec, __class__ returns the spec class instead.
# This allows mock objects to pass isinstance() tests for the object they are replacing / masquerading as:
# 

mock = Mock(spec=3)

isinstance(mock, int)

# OUTPUT: 'True'
 
#
# __class__ is assignable to, this allows a mock to pass an isinstance() check without forcing you to use a spec:
# 

mock = Mock()

mock.__class__ = dict

isinstance(mock, dict)

# OUTPUT: 'True'
