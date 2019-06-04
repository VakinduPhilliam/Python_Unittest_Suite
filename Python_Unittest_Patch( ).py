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
# Mock has many other ways you can configure it and control its behaviour. For example the spec argument configures the mock to take its specification from
# another object. Attempting to access attributes or methods on the mock that don’t exist on the spec will fail with an AttributeError.
# 
# The patch() decorator / context manager makes it easy to mock classes or objects in a module under test. The object you specify will be replaced with a
# mock (or other object) during the test and restored when the test ends:
# 

from unittest.mock import patch

@patch('module.ClassName2')
@patch('module.ClassName1')

def test(MockClass1, MockClass2):
        module.ClassName1()
        module.ClassName2()

        assert MockClass1 is module.ClassName1
        assert MockClass2 is module.ClassName2

        assert MockClass1.called

        assert MockClass2.called

test()
