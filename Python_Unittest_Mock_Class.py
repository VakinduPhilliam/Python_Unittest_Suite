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
# The Mock Class
# Mock is a flexible mock object intended to replace the use of stubs and test doubles throughout your code. Mocks are callable and create attributes as new
# mocks when you access them. 
# Accessing the same attribute will always return the same mock. Mocks record how you use them, allowing you to make assertions about what your code has done
# to them.
#

#
# assert_called(*args, **kwargs). 
# Assert that the mock was called at least once.
# 

mock = Mock()
mock.method()

# OUTPUT: '<Mock name='mock.method()' id='...'>'

mock.method.assert_called()
 

#
# assert_called_once(*args, **kwargs). 
# Assert that the mock was called exactly once.
# 

mock = Mock()
mock.method()

# OUTPUT: '<Mock name='mock.method()' id='...'>'

mock.method.assert_called_once()
mock.method()

# OUTPUT: '<Mock name='mock.method()' id='...'>'

mock.method.assert_called_once()

#
# assert_called_with(*args, **kwargs). 
# This method is a convenient way of asserting that calls are made in a particular way:
# 

mock = Mock()
mock.method(1, 2, 3, test='wow')

# OUTPUT: '<Mock name='mock.method()' id='...'>'

mock.method.assert_called_with(1, 2, 3, test='wow')

#
# assert_called_once_with(*args, **kwargs). 
# Assert that the mock was called exactly once and that that call was with the specified arguments.
# 

mock = Mock(return_value=None)
mock('foo', bar='baz')

mock.assert_called_once_with('foo', bar='baz')
mock('other', bar='values')

mock.assert_called_once_with('other', bar='values')
