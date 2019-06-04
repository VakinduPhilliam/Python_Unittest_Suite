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
# Where to patch:
# patch() works by (temporarily) changing the object that a name points to with another one.
# There can be many names pointing to any individual object, so for patching to work you must ensure that you patch the name used by the system under test.
# 
# The basic principle is that you patch where an object is looked up, which is not necessarily the same place as where it is defined.
# A couple of examples will help to clarify this.
# 
# Imagine we have a project that we want to test with the following structure:
# 

a.py
    -> Defines SomeClass

b.py
    -> from a import SomeClass
    -> some_function instantiates SomeClass

#
# The key is to patch out SomeClass where it is used (or where it is looked up).
# In this case some_function will actually look up SomeClass in module b, where we have imported it.
# The patching should look like:
# 

@patch('b.SomeClass')
 
#
# However, consider the alternative scenario where instead of from a import SomeClass module b does import a and some_function uses a.SomeClass.
# Both of these import forms are common.
# In this case the class we want to patch is being looked up in the module and so we have to patch a.SomeClass instead:
# 

@patch('a.SomeClass')
