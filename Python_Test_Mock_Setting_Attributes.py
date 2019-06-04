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
# Setting Return Values and Attributes:
# Setting the return values on a mock object is trivially easy:
# 

mock = Mock()
mock.return_value = 3

mock()

# OUTPUT: '3'

# 
# Of course you can do the same for methods on the mock:
# 

mock = Mock()
mock.method.return_value = 3

mock.method()

# OUTPUT: '3'
 
#
# The return value can also be set in the constructor:
# 

mock = Mock(return_value=3)
mock()

# OUTPUT: '3'

# 
# If you need an attribute setting on your mock, just do it:
# 

mock = Mock()
mock.x = 3

mock.x

# OUTPUT: '3'

#
# Sometimes you want to mock up a more complex situation, like for example mock.connection.cursor().execute("SELECT 1").
# If we wanted this call to return a list, then we have to configure the result of the nested call.
#

# 
# We can use call to construct the set of calls in a “chained call” like this for easy assertion afterwards:
# 

mock = Mock()

cursor = mock.connection.cursor.return_value
cursor.execute.return_value = ['foo']

mock.connection.cursor().execute("SELECT 1")

# OUTPUT: '['foo']'

expected = call.connection.cursor().execute("SELECT 1").call_list()

mock.mock_calls

# OUTPUT: '[call.connection.cursor(), call.connection.cursor().execute('SELECT 1')]'

mock.mock_calls == expected

# OUTPUT: 'True'
