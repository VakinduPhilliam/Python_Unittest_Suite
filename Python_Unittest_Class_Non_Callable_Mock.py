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
# class unittest.mock.NonCallableMock(spec=None, wraps=None, name=None, spec_set=None, **kwargs).
# A non-callable version of Mock.
# The constructor parameters have the same meaning of Mock, with the exception of return_value and side_effect which have no meaning on a non-callable mock.
 
#
# Mock objects that use a class or an instance as a spec or spec_set are able to pass isinstance() tests:
# 

mock = Mock(spec=SomeClass)

isinstance(mock, SomeClass)

# OUTPUT: 'True'

mock = Mock(spec_set=SomeClass())

isinstance(mock, SomeClass)

# OUTPUT: 'True'

#
# The Mock classes have support for mocking magic methods.
# The mock classes and the patch() decorators all take arbitrary keyword arguments for configuration.
# For the patch() decorators the keywords are passed to the constructor of the mock being created. The keyword arguments are for configuring attributes of
# the mock:
# 

m = MagicMock(attribute=3, other='fish')

m.attribute

# OUTPUT: '3'

m.other

# OUTPUT: 'fish'
 
#
# The return value and side effect of child mocks can be set in the same way, using dotted notation.
# As you can’t use dotted names directly in a call you have to create a dictionary and unpack it using **:
# 

attrs = {'method.return_value': 3, 'other.side_effect': KeyError}

mock = Mock(some_attribute='eggs', **attrs)

mock.some_attribute

# OUTPUT: 'eggs'

mock.method()

# OUTPUT: '3'

mock.other()
