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
# Mock subclasses and their attributes:
# There are various reasons why you might want to subclass Mock. One reason might be to add helper methods.
#

#
# Here’s a silly example:
# 

class MyMock(MagicMock):
        def has_been_called(self):

            return self.called

mymock = MyMock(return_value=None)

mymock

# OUTPUT: '<MyMock id='...'>'

mymock.has_been_called()

# OUTPUT: 'False'

mymock()
mymock.has_been_called()

# OUTPUT: 'True'
 
#
# The standard behaviour for Mock instances is that attributes and the return value mocks are of the same type as the mock they are accessed on.
# This ensures that Mock attributes are Mocks and MagicMock attributes are MagicMocks.
# So if you’re subclassing to add helper methods then they’ll also be available on the attributes and return value mock of instances of your subclass.
# 

mymock.foo

# OUTPUT: '<MyMock name='mock.foo' id='...'>'

mymock.foo.has_been_called()

# OUTPUT: 'False'

mymock.foo()

# OUTPUT: '<MyMock name='mock.foo()' id='...'>'

mymock.foo.has_been_called()

# OUTPUT: 'True'

# 
# Sometimes this is inconvenient.
# For example, one user is subclassing mock to created a Twisted adaptor.
# Having this applied to attributes too actually causes errors.
#

# 
# Mock (in all its flavours) uses a method called _get_child_mock to create these “sub-mocks” for attributes and return values.
# You can prevent your subclass being used for attributes by overriding this method.
# The signature is that it takes arbitrary keyword arguments (**kwargs) which are then passed onto the mock constructor:
# 

class Subclass(MagicMock):
        def _get_child_mock(self, **kwargs):

            return MagicMock(**kwargs)

mymock = Subclass()

mymock.foo

# OUTPUT: '<MagicMock name='mock.foo' id='...'>'

assert isinstance(mymock, Subclass)
assert not isinstance(mymock.foo, Subclass)

assert not isinstance(mymock(), Subclass)
