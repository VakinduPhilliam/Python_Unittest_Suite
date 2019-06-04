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
# mock_calls: 
# mock_calls records all calls to the mock object, its methods, magic methods and return value mocks.
# 
# Members of mock_calls are call objects. These can be unpacked as tuples to get at the individual arguments. 
#

mock = MagicMock()
result = mock(1, 2, 3)

mock.first(a=3)

# OUTPUT: '<MagicMock name='mock.first()' id='...'>'

mock.second()

# OUTPUT: '<MagicMock name='mock.second()' id='...'>'

int(mock)

# OUTPUT: '1'

result(1)

# OUTPUT: '<MagicMock name='mock()()' id='...'>'

expected = [call(1, 2, 3), call.first(a=3), call.second(),
           call.__int__(), call()(1)]

mock.mock_calls == expected

# OUTPUT: 'True'

#
# The way mock_calls are recorded means that where nested calls are made, the parameters of ancestor calls are not recorded and so will always compare
# equal:
# 

mock = MagicMock()
mock.top(a=3).bottom()

# OUTPUT: '<MagicMock name='mock.top().bottom()' id='...'>'

mock.mock_calls

# OUTPUT: '[call.top(a=3), call.top().bottom()]'

mock.mock_calls[-1] == call.top(a=-1).bottom()

# OUTPUT: 'True'
