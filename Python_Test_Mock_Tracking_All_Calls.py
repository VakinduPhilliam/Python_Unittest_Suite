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
# Tracking all Calls:
# Often you want to track more than a single call to a method. The mock_calls attribute records all calls to child attributes of the mock - and also to
# their children.
# 

mock = MagicMock()
mock.method()

# OUTPUT: '<MagicMock name='mock.method()' id='...'>'

mock.attribute.method(10, x=53)

# OUTPUT: '<MagicMock name='mock.attribute.method()' id='...'>'

mock.mock_calls

# OUTPUT: '[call.method(), call.attribute.method(10, x=53)]'
 
#
# If you make an assertion about mock_calls and any unexpected methods have been called, then the assertion will fail.
# This is useful because as well as asserting that the calls you expected have been made, you are also checking that they were made in the right order and
# with no additional calls:
#

# 
# You use the call object to construct lists for comparing with mock_calls:
# 

expected = [call.method(), call.attribute.method(10, x=53)]
mock.mock_calls == expected

# OUTPUT: 'True'
 
#
# However, parameters to calls that return mocks are not recorded, which means it is not possible to track nested calls where the parameters used to create
# ancestors are important:
# 

m = Mock()
m.factory(important=True).deliver()

# OUTPUT: '<Mock name='mock.factory().deliver()' id='...'>'

m.mock_calls[-1] == call.factory(important=False).deliver()

# OUTPUT: 'True'
