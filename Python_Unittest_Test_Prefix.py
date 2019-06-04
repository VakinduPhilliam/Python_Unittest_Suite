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
# TEST_PREFIX:
# All of the patchers can be used as class decorators.
# When used in this way they wrap every test method on the class.
# The patchers recognise methods that start with 'test' as being test methods.
# This is the same way that the unittest.TestLoader finds test methods by default.
# 
# It is possible that you want to use a different prefix for your tests.
# You can inform the patchers of the different prefix by setting patch.TEST_PREFIX:
# 

patch.TEST_PREFIX = 'foo'
value = 3

@patch('__main__.value', 'not three')

class Thing:

        def foo_one(self):
            print(value)

        def foo_two(self):
            print(value)

Thing().foo_one()

# OUTPUT: 'not three'

Thing().foo_two()

# OUTPUT: 'not three'

value

# OUTPUT: '3'
