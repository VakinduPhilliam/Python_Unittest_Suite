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
# The patchers:
# The patch decorators are used for patching objects only within the scope of the function they decorate.
# They automatically handle the unpatching for you, even if exceptions are raised.
# All of these functions can also be used in with statements or as class decorators.
#
# unittest.mock.patch(target, new=DEFAULT, spec=None, create=False, spec_set=None, autospec=None, new_callable=None, **kwargs).
# patch() acts as a function decorator, class decorator or a context manager.
# Inside the body of the function or with statement, the target is patched with a new object.
# When the function/with statement exits the patch is undone.

#
# patch() as function decorator, creating the mock for you and passing it into the decorated function:
# 

@patch('__main__.SomeClass')

 def function(normal_argument, mock_class):
        print(mock_class is SomeClass)

function(None)

# OUTPUT: 'True'
 
#
# Patching a class replaces the class with a MagicMock instance. If the class is instantiated in the code under test then it will be the return_value of the
# mock that will be used.
# If the class is instantiated multiple times you could use side_effect to return a new mock each time. Alternatively you can set the return_value to be
# anything you want.
#
# To configure return values on methods of instances on the patched class you must do this on the return_value.

#
# For example:
# 

class Class:
        def method(self):
            pass

with patch('__main__.Class') as MockClass:
        instance = MockClass.return_value
        instance.method.return_value = 'foo'

        assert Class() is instance

     assert Class().method() == 'foo'

# 
# If you use spec or spec_set and patch() is replacing a class, then the return value of the created mock will have the same spec.
# 

Original = Class
patcher = patch('__main__.Class', spec=True)

MockClass = patcher.start()

instance = MockClass()

assert isinstance(instance, Original)

patcher.stop()

# 
# The new_callable argument is useful where you want to use an alternative class to the default MagicMock for the created mock.
#
# For example, if you wanted a NonCallableMock to be used:
# 

thing = object()

with patch('__main__.thing', new_callable=NonCallableMock) as mock_thing:
        assert thing is mock_thing

        thing()

#
# Another use case might be to replace an object with an io.StringIO instance:
# 

from io import StringIO

    def foo():
        print('Something')

@patch('sys.stdout', new_callable=StringIO)

    def test(mock_stdout):

       foo()

       assert mock_stdout.getvalue() == 'Something\n'

test()

# 
# When patch() is creating a mock for you, it is common that the first thing you need to do is to configure the mock.
# Some of that configuration can be done in the call to patch.
# Any arbitrary keywords you pass into the call will be used to set attributes on the created mock:
# 

patcher = patch('__main__.thing', first='one', second='two')

mock_thing = patcher.start()
mock_thing.first

# OUTPUT: 'one'

mock_thing.second

# OUTPUT: 'two'

# 
# As well as attributes on the created mock attributes, like the return_value and side_effect, of child mocks can also be configured.
# These aren’t syntactically valid to pass in directly as keyword arguments, but a dictionary with these as keys can still be expanded into a patch() call
# using **:
# 

config = {'method.return_value': 3, 'other.side_effect': KeyError}

patcher = patch('__main__.thing', **config)

mock_thing = patcher.start()
mock_thing.method()

# OUTPUT: '3'

mock_thing.other()
