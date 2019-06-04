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

# patch.dict.
# patch.dict(in_dict, values=(), clear=False, **kwargs). 
# Patch a dictionary, or dictionary like object, and restore the dictionary to its original state after the test.
# 
# in_dict can be a dictionary or a mapping like container. If it is a mapping then it must at least support getting, setting and deleting items plus
# iterating over keys.
# in_dict can also be a string specifying the name of the dictionary, which will then be fetched by importing it.
# values can be a dictionary of values to set in the dictionary. values can also be an iterable of (key, value) pairs.
#
# If clear is true then the dictionary will be cleared before the new values are set.
# 
# patch.dict() can also be called with arbitrary keyword arguments to set values in the dictionary.
# 
# patch.dict() can be used as a context manager, decorator or class decorator. When used as a class decorator patch.dict() honours patch.TEST_PREFIX for
# choosing which methods to wrap.
# 
# patch.dict() can be used to add members to a dictionary, or simply let a test change a dictionary, and ensure the dictionary is restored when the test
# ends.
# 

foo = {}

with patch.dict(foo, {'newkey': 'newvalue'}):
        assert foo == {'newkey': 'newvalue'}

assert foo == {}
 

import os

with patch.dict('os.environ', {'newkey': 'newvalue'}):
        print(os.environ['newkey'])


# OUTPUT: 'newvalue'

assert 'newkey' not in os.environ

# 
# Keywords can be used in the patch.dict() call to set values in the dictionary:
# 

mymodule = MagicMock()
mymodule.function.return_value = 'fish'

with patch.dict('sys.modules', mymodule=mymodule):
        import mymodule
 
       mymodule.function('some', 'args')

# OUTPUT: 'fish'
 
#
# patch.dict() can be used with dictionary like objects that aren’t actually dictionaries.
# At the very minimum they must support item getting, setting, deleting and either iteration or membership test.
# This corresponds to the magic methods __getitem__(), __setitem__(), __delitem__() and either __iter__() or __contains__().
# 

class Container:
        def __init__(self):
            self.values = {}

        def __getitem__(self, name):
            return self.values[name]

        def __setitem__(self, name, value):
            self.values[name] = value

        def __delitem__(self, name):
            del self.values[name]

        def __iter__(self):
            return iter(self.values)

thing = Container()
thing['one'] = 1

with patch.dict(thing, one=2, two=3):
        assert thing['one'] == 2

       assert thing['two'] == 3

assert thing['one'] == 1
assert list(thing) == ['one']
