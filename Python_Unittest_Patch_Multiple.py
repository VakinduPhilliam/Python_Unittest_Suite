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
# If you want patch.multiple() to create mocks for you, then you can use DEFAULT as the value.
# If you use patch.multiple() as a decorator then the created mocks are passed into the decorated function by keyword.
# 

thing = object()
other = object()
 

@patch.multiple('__main__', thing=DEFAULT, other=DEFAULT)

    def test_function(thing, other):
        assert isinstance(thing, MagicMock)
        assert isinstance(other, MagicMock)

test_function()
 
#
# patch.multiple() can be nested with other patch decorators, but put arguments passed by keyword after any of the standard arguments created by patch():
# 

@patch('sys.exit')
@patch.multiple('__main__', thing=DEFAULT, other=DEFAULT)

def test_function(mock_exit, other, thing):
        assert 'other' in repr(other)
        assert 'thing' in repr(thing)

        assert 'exit' in repr(mock_exit)

test_function()

# 
# If patch.multiple() is used as a context manager, the value returned by the context manger is a dictionary where created mocks are keyed by name:
# 

with patch.multiple('__main__', thing=DEFAULT, other=DEFAULT) as values:
        assert 'other' in repr(values['other'])
        assert 'thing' in repr(values['thing'])

        assert values['thing'] is thing
        assert values['other'] is other
