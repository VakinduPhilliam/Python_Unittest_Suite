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
# More complex argument matching:
# Using the same basic concept as ANY we can implement matchers to do more complex assertions on objects used as arguments to mocks.
#

# 
# Suppose we expect some object to be passed to a mock that by default compares equal based on object identity (which is the Python default for user defined
# classes).
# To use assert_called_with() we would need to pass in the exact same object.
# If we are only interested in some of the attributes of this object then we can create a matcher that will check these attributes for us.
#

#
# You can see in this example how a ‘standard’ call to assert_called_with isn’t sufficient:
# 

class Foo:
        def __init__(self, a, b):

            self.a, self.b = a, b

mock = Mock(return_value=None)
mock(Foo(1, 2))

mock.assert_called_with(Foo(1, 2))

#
# A comparison function for our Foo class might look something like this:
# 

def compare(self, other):
        if not type(self) == type(other):

            return False

        if self.a != other.a:
            return False

        if self.b != other.b:
            return False

      return True

# 
# And a matcher object that can use comparison functions like this for its equality operation would look something like this:
# 

class Matcher:
        def __init__(self, compare, some_obj):
            self.compare = compare
            self.some_obj = some_obj

        def __eq__(self, other):
            return self.compare(self.some_obj, other)

# 
# Putting all this together:
# 

match_foo = Matcher(compare, Foo(1, 2))
mock.assert_called_with(match_foo)

# 
# The Matcher is instantiated with our compare function and the Foo object we want to compare against.
# In assert_called_with the Matcher equality method will be called, which compares the object the mock was called with against the one we created our
# matcher with.
# If they match then assert_called_with passes, and if they don’t an AssertionError is raised:
# 

match_wrong = Matcher(compare, Foo(3, 4))

mock.assert_called_with(match_wrong)
