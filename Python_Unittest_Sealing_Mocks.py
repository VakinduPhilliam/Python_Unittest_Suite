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
# Sealing mocks:
# unittest.mock.seal(mock). 
# Seal will disable the automatic creation of mocks when accessing an attribute of the mock being sealed or any of its attributes that are already mocks
# recursively.
#

# 
# If a mock instance with a name or a spec is assigned to an attribute it won’t be considered in the sealing chain.
# This allows one to prevent seal from fixing part of the mock object.
# 

mock = Mock()
mock.submock.attribute1 = 2

mock.not_submock = mock.Mock(name="sample_name")

seal(mock)

mock.new_attribute  # This will raise AttributeError.
mock.submock.attribute2  # This will raise AttributeError.

mock.not_submock.attribute2  # This won't raise.
