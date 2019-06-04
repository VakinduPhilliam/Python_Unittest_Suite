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
# Mocking chained calls:
# Mocking chained calls is actually straightforward with mock once you understand the return_value attribute. When a mock is called for the first time, or 
# you fetch its return_value before it has been called, a new Mock is created.
# This means that you can see how the object returned from a call to a mocked object has been used by interrogating the return_value mock:
# 

mock = Mock()
mock().foo(a=2, b=3)

# OUTPUT: '<Mock name='mock().foo()' id='...'>'

mock.return_value.foo.assert_called_with(a=2, b=3)

# 
# From here it is a simple step to configure and then make assertions about chained calls.
# Of course another alternative is writing your code in a more testable way in the first place…
#

# 
# So, suppose we have some code that looks a little bit like this:
# 

class Something:

        def __init__(self):
            self.backend = BackendProvider()

        def method(self):
            response = self.backend.get_endpoint('foobar').create_call('spam', 'eggs').start_call()

            # more code

# 
# Assuming that BackendProvider is already well tested, how do we test method()? Specifically, we want to test that the code section # more code uses the
# response object in the correct way.
# As this chain of calls is made from an instance attribute we can monkey patch the backend attribute on a Something instance.
# In this particular case we are only interested in the return value from the final call to start_call so we don’t have much configuration to do.
# Let’s assume the object it returns is ‘file-like’, so we’ll ensure that our response object uses the builtin open() as its spec.
# To do this we create a mock instance as our mock backend and create a mock response object for it. To set the response as the return value for that final
# start_call we could do this:
# 

#
# mock_backend.get_endpoint.return_value.create_call.return_value.start_call.return_value = mock_response
# We can do that in a slightly nicer way using the configure_mock() method to directly set the return value for us:
# 

something = Something()

mock_response = Mock(spec=open)
mock_backend = Mock()

config = {'get_endpoint.return_value.create_call.return_value.start_call.return_value': mock_response}

mock_backend.configure_mock(**config)

# 
# With these we monkey patch the “mock backend” in place and can make the real call:
# 

something.backend = mock_backend

something.method()

# 
# Using mock_calls we can check the chained call with a single assert.
# A chained call is several calls in one line of code, so there will be several entries in mock_calls.
# We can use call.call_list() to create this list of calls for us:
# 

chained = call.get_endpoint('foobar').create_call('spam', 'eggs').start_call()
call_list = chained.call_list()

assert mock_backend.mock_calls == call_list
