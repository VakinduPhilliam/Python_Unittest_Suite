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
# Side effect functions and iterables:
# side_effect can also be set to a function or an iterable.
# The use case for side_effect as an iterable is where your mock is going to be called several times, and you want each call to return a different value.
# When you set side_effect to an iterable every call to the mock returns the next value from the iterable:
# 

mock = MagicMock(side_effect=[4, 5, 6])
mock()

# OUTPUT: '4'

mock()

# OUTPUT: '5'

mock()

# OUTPUT: '6'

# 
# For more advanced use cases, like dynamically varying the return values depending on what the mock is called with, side_effect can be a function.
# The function will be called with the same arguments as the mock.
# Whatever the function returns is what the call returns:
# 

vals = {(1, 2): 1, (2, 3): 2}

def side_effect(*args):
        return vals[args]
   
mock = MagicMock(side_effect=side_effect)
mock(1, 2)

# OUTPUT: '1'

mock(2, 3)

# OUTPUT: '2'
