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
# Mocking a Generator Method:
# A Python generator is a function or method that uses the yield statement to return a series of values when iterated over.
# A generator method / function is called to return the generator object.
#
# It is the generator object that is then iterated over.
# The protocol method for iteration is __iter__(), so we can mock this using a MagicMock.
#

# 
# Here’s an example class with an “iter” method implemented as a generator:
# 

class Foo:

     def iter(self):
            for i in [1, 2, 3]:

                yield i

foo = Foo()

list(foo.iter())

# OUTPUT: '[1, 2, 3]'

#
# How would we mock this class, and in particular its “iter” method?
#

# 
# To configure the values returned from the iteration (implicit in the call to list), we need to configure the object returned by the call to foo.iter().
# 

mock_foo = MagicMock()
mock_foo.iter.return_value = iter([1, 2, 3])

list(mock_foo.iter())

# OUTPUT: '[1, 2, 3]'
