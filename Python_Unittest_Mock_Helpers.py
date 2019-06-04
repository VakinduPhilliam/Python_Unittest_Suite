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
# Helpers:
# sentinel
# unittest.mock.sentinel 

#
# The sentinel object provides a convenient way of providing unique objects for your tests.
# 
# Attributes are created on demand when you access them by name.
# Accessing the same attribute will always return the same object. The objects returned have a sensible repr so that test failure messages are readable.
# The sentinel attributes now preserve their identity when they are copied or pickled.

# 
# Sometimes when testing you need to test that a specific object is passed as an argument to another method, or returned. It can be common to create named
# sentinel objects to test this. sentinel provides a convenient way of creating and testing the identity of objects like this.

#
# In this example we monkey patch method to return sentinel.some_object:
# 

real = ProductionClass()
real.method = Mock(name="method")

real.method.return_value = sentinel.some_object

result = real.method()

assert result is sentinel.some_object

sentinel.some_object

# OUTPUT: 'sentinel.some_object'
 
#
# DEFAULT:
# unittest.mock.DEFAULT: 
# The DEFAULT object is a pre-created sentinel (actually sentinel.DEFAULT). It can be used by side_effect functions to indicate that the normal return value
# should be used.
# 

#
# call:
# unittest.mock.call(*args, **kwargs). 
# call() is a helper object for making simpler assertions, for comparing with call_args, call_args_list, mock_calls and method_calls.
# call() can also be used with assert_has_calls().
# 

m = MagicMock(return_value=None)
m(1, 2, a='foo', b='bar')

m()

m.call_args_list == [call(1, 2, a='foo', b='bar'), call()]

# OUTPUT: 'True'

#
# call.call_list(): 
# For a call object that represents multiple calls, call_list() returns a list of all the intermediate calls as well as the final call.
# call_list is particularly useful for making assertions on “chained calls”. A chained call is multiple calls on a single line of code.
# This results in multiple entries in mock_calls on a mock. Manually constructing the sequence of calls can be tedious.
# call_list() can construct the sequence of calls from the same chained call:
# 

m = MagicMock()
m(1).method(arg='foo').other('bar')(2.0)

# OUTPUT: '<MagicMock name='mock().method().other()()' id='...'>'

kall = call(1).method(arg='foo').other('bar')(2.0)

kall.call_list()

m.mock_calls == kall.call_list()

# OUTPUT: 'True'
 
#
# A call object is either a tuple of (positional args, keyword args) or (name, positional args, keyword args) depending on how it was constructed.
# When you construct them yourself this isn’t particularly interesting, but the call objects that are in the Mock.call_args, Mock.call_args_list and
# Mock.mock_calls attributes can be introspected to get at the individual arguments they contain.
# 
# The call objects in Mock.call_args and Mock.call_args_list are two-tuples of (positional args, keyword args) whereas the call objects in Mock.mock_calls, 
# along with ones you construct yourself, are three-tuples of (name, positional args, keyword args).
# 
# You can use their “tupleness” to pull out the individual arguments for more complex introspection and assertions.
# The positional arguments are a tuple (an empty tuple if there are no positional arguments) and the keyword arguments are a dictionary:
# 

m = MagicMock(return_value=None)
m(1, 2, 3, arg='one', arg2='two')

kall = m.call_args

args, kwargs = kall

args

# OUTPUT: '(1, 2, 3)'

kwargs

# OUTPUT: '{'arg2': 'two', 'arg': 'one'}'

args is kall[0]

# OUTPUT: 'True'

kwargs is kall[1]

# OUTPUT: 'True'
 
m = MagicMock()
m.foo(4, 5, 6, arg='two', arg2='three')

# OUTPUT: '<MagicMock name='mock.foo()' id='...'>'

kall = m.mock_calls[0]

name, args, kwargs = kall
name

# OUTPUT: 'foo'

args

# OUTPUT: '(4, 5, 6)'

kwargs

# OUTPUT: '{'arg2': 'three', 'arg': 'two'}'

name is m.mock_calls[0][0]

# OUTPUT: 'True'
 
#
# create_autospec:
# unittest.mock.create_autospec(spec, spec_set=False, instance=False, **kwargs) 
# Create a mock object using another object as a spec. Attributes on the mock will use the corresponding attribute on the spec object as their spec.
#
 
#
# Functions or methods being mocked will have their arguments checked to ensure that they are called with the correct signature.
# If spec_set is True then attempting to set attributes that don’t exist on the spec object will raise an AttributeError.
# 
# If a class is used as a spec then the return value of the mock (the instance of the class) will have the same spec.
# You can use a class as the spec for an instance object by passing instance=True.
# The returned mock will only be callable if instances of the mock are callable.
# create_autospec() also takes arbitrary keyword arguments that are passed to the constructor of the created mock.
#

#
# ANY
# unittest.mock.ANY 
# Sometimes you may need to make assertions about some of the arguments in a call to mock, but either not care about some of the arguments or want to pull
# them individually out of call_args and make more complex assertions on them.
# 
# To ignore certain arguments you can pass in objects that compare equal to everything. Calls to assert_called_with() and assert_called_once_with() will
# then succeed no matter what was passed in.
# 

mock = Mock(return_value=None)
mock('foo', bar=object())

mock.assert_called_once_with('foo', bar=ANY)

# 
# ANY can also be used in comparisons with call lists like mock_calls:
# 

m = MagicMock(return_value=None)
m(1)

m(1, 2)
m(object())

m.mock_calls == [call(1), call(1, 2), ANY]

# OUTPUT: 'True'
