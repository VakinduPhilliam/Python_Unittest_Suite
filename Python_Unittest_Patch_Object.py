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
# patch.object:
# patch.object(target, attribute, new=DEFAULT, spec=None, create=False, spec_set=None, autospec=None, new_callable=None, **kwargs).
# patch the named member (attribute) on an object (target) with a mock object.
# 
# patch.object() can be used as a decorator, class decorator or a context manager. Arguments new, spec, create, spec_set, autospec and new_callable have the
# same meaning as for patch(). Like patch(), patch.object() takes arbitrary keyword arguments for configuring the mock object it creates.
# When used as a class decorator patch.object() honours patch.TEST_PREFIX for choosing which methods to wrap.
# 
# You can either call patch.object() with three arguments or two arguments. The three argument form takes the object to be patched, the attribute name and
# the object to replace the attribute with.
# When calling with the two argument form you omit the replacement object, and a mock is created for you and passed in as an extra argument to the decorated
# function:
# 

@patch.object(SomeClass, 'class_method')

def test(mock_method):
        SomeClass.class_method(3)

        mock_method.assert_called_with(3)

test()
