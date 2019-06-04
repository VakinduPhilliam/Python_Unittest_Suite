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
# class unittest.mock.PropertyMock(*args, **kwargs). 
# A mock intended to be used as a property, or other descriptor, on a class. PropertyMock provides __get__() and __set__() methods so you can specify a
# return value when it is fetched.
# 
# Fetching a PropertyMock instance from an object calls the mock, with no args. Setting it calls the mock with the value being set.
# 

class Foo:
        @property

        def foo(self):
            return 'something'

        @foo.setter

        def foo(self, value):
            pass

with patch('__main__.Foo.foo', new_callable=PropertyMock) as mock_foo:

        mock_foo.return_value = 'mockity-mock'

        this_foo = Foo()

        print(this_foo.foo)

        this_foo.foo = 6

# OUTPUT: 'mockity-mock'

mock_foo.mock_calls

# OUTPUT: '[call(), call(6)]'

# 
# Because of the way mock attributes are stored you can’t directly attach a PropertyMock to a mock object.
# Instead you can attach it to the mock type object:
# 

m = MagicMock()

p = PropertyMock(return_value=3)

type(m).foo = p

m.foo

# OUTPUT: '3'

p.assert_called_once_with()
