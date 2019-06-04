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
# Mock for Method Calls on an Object
#

# 
# In the last example we patched a method directly on an object to check that it was called correctly.
# Another common use case is to pass an object into a method (or some part of the system under test) and then check that it is used in the correct way.
#
 
#
# The simple ProductionClass below has a closer method. If it is called with an object then it calls close on it.
# 

class ProductionClass:
        def closer(self, something):

            something.close()

# 
# So to test it we need to pass in an object with a close method and check that it was called correctly.
# 

real = ProductionClass()
mock = Mock()

real.closer(mock)

mock.close.assert_called_with()
