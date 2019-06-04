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
# Mocking imports with patch.dict
# One situation where mocking can be hard is where you have a local import inside a function.
# These are harder to mock because they aren’t using an object from the module namespace that we can patch out.
# you can use patch.dict() to temporarily put a mock in place in sys.modules.
#
# Any imports whilst this patch is active will fetch the mock.
# When the patch is complete (the decorated function exits, the with statement body is complete or patcher.stop() is called) then whatever was there
# previously will be restored safely.
#

# 
# Here’s an example that mocks out the ‘fooble’ module.
# 

mock = Mock()

with patch.dict('sys.modules', {'fooble': mock}):
       import fooble

       fooble.blob()

# OUTPUT: '<Mock name='mock.blob()' id='...'>'

assert 'fooble' not in sys.modules

mock.blob.assert_called_once_with()

# 
# As you can see the import fooble succeeds, but on exit there is no ‘fooble’ left in sys.modules.
# 
# This also works for the from module import name form:
# 

mock = Mock()

with patch.dict('sys.modules', {'fooble': mock}):
       from fooble import blob

       blob.blip()

# OUTPUT: '<Mock name='mock.blob.blip()' id='...'>'

mock.blob.blip.assert_called_once_with()

# 
# With slightly more work you can also mock package imports:
# 

mock = Mock()
modules = {'package': mock, 'package.module': mock.module}

with patch.dict('sys.modules', modules):
        from package.module import fooble

        fooble()

# OUTPUT: '<Mock name='mock.module.fooble()' id='...'>'

mock.module.fooble.assert_called_once_with()
