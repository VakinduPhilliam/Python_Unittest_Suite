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
# Creating a Mock from an Existing Object:
# One problem with over use of mocking is that it couples your tests to the implementation of your mocks rather than your real code.
# Suppose you have a class that implements some_method.
# In a test for another class, you provide a mock of this object that also provides some_method.
# If later you refactor the first class, so that it no longer has some_method - then your tests will continue to pass even though your code is now broken!
#

# 
# Mock allows you to provide an object as a specification for the mock, using the spec keyword argument. Accessing methods / attributes on the mock that
# don’t exist on your specification object will immediately raise an attribute error.
# If you change the implementation of your specification, then tests that use that class will start failing immediately without you having to instantiate
# the class in those tests.
# 

mock = Mock(spec=SomeClass)
mock.old_method()

#
# Using a specification also enables a smarter matching of calls made to the mock, regardless of whether some parameters were passed as positional or named
# arguments:
# 

def f(a, b, c): pass

mock = Mock(spec=f)
mock(1, 2, 3)

# OUTPUT: '<Mock name='mock()' id='140161580456576'>'

mock.assert_called_with(a=1, b=2, c=3)
