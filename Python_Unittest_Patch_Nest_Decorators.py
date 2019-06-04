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
# Nesting Patch Decorators:
# If you want to perform multiple patches then you can simply stack up the decorators.
#

# 
# You can stack up multiple patch decorators using this pattern:
# 

@patch.object(SomeClass, 'class_method')
@patch.object(SomeClass, 'static_method')

def test(mock1, mock2):
        assert SomeClass.static_method is mock1
        assert SomeClass.class_method is mock2

        SomeClass.static_method('foo')
        SomeClass.class_method('bar')

        return mock1, mock2

mock1, mock2 = test()
mock1.assert_called_once_with('foo')

mock2.assert_called_once_with('bar')

# 
# Note that the decorators are applied from the bottom upwards.
# This is the standard way that Python applies decorators.
# The order of the created mocks passed into your test function matches this order.
#