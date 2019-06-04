# Python Test Mock
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
# Coping with mutable arguments:
# Another situation is rare, but can bite you, is when your mock is called with mutable arguments.
# call_args and call_args_list store references to the arguments.
# If the arguments are mutated by the code under test then you can no longer make assertions about what the values were when the mock was called.
#

# 
# Here’s some example code that shows the problem.
#
# Imagine the following functions defined in ‘mymodule’:
# 

def frob(val):
    pass

def grob(val):
    "First frob and then clear val"

    frob(val)

    val.clear()

# 
# When we try to test that grob calls frob with the correct argument look what happens:
# 

with patch('mymodule.frob') as mock_frob:
        val = {6}

        mymodule.grob(val)

val

# OUTPUT: 'set()'

mock_frob.assert_called_with({6})

#
# One possibility would be for mock to copy the arguments you pass in.
# This could then cause problems if you do assertions that rely on object identity for equality.
#

# 
# Here’s one solution that uses the side_effect functionality.
# If you provide a side_effect function for a mock then side_effect will be called with the same args as the mock.
# This gives us an opportunity to copy the arguments and store them for later assertions.
#

#
# In this example I’m using another mock to store the arguments so that I can use the mock methods for doing the assertion.
# Again a helper function sets this up for me.
# 

from copy import deepcopy
from unittest.mock import Mock, patch, DEFAULT

def copy_call_args(mock):
        new_mock = Mock()

        def side_effect(*args, **kwargs):
            args = deepcopy(args)

            kwargs = deepcopy(kwargs)
            new_mock(*args, **kwargs)

            return DEFAULT

        mock.side_effect = side_effect

        return new_mock

with patch('mymodule.frob') as mock_frob:
        new_mock = copy_call_args(mock_frob)

        val = {6}

        mymodule.grob(val)

new_mock.assert_called_with({6})

new_mock.call_args

# OUTPUT: 'call({6})'
 
#
# copy_call_args is called with the mock that will be called.
# It returns a new mock that we do the assertion on.
# The side_effect function makes a copy of the args and calls our new_mock with the copy.
# 

#
# Note:
# If your mock is only going to be used once there is an easier way of checking arguments at the point they are called.
# You can simply do the checking inside a side_effect function.
# 

def side_effect(arg):
        assert arg == {6}

mock = Mock(side_effect=side_effect)

mock({6})
mock(set())

#
# An alternative approach is to create a subclass of Mock or MagicMock that copies (using copy.deepcopy()) the arguments.
#
# Here’s an example implementation:
# 

from copy import deepcopy

    class CopyingMock(MagicMock):
        def __call__(self, *args, **kwargs):

            args = deepcopy(args)

            kwargs = deepcopy(kwargs)

            return super(CopyingMock, self).__call__(*args, **kwargs)

c = CopyingMock(return_value=None)

arg = set()

c(arg)

arg.add(1)

c.assert_called_with(set())

c.assert_called_with(arg)

c.foo

# OUTPUT: '<CopyingMock name='mock.foo' id='...'>'
 
#
# When you subclass Mock or MagicMock all dynamically created attributes, and the return_value will use your subclass automatically.
# That means all children of a CopyingMock will also have the type CopyingMock.
#
