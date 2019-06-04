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
# FILTER_DIR:
# unittest.mock.FILTER_DIR: 
# FILTER_DIR is a module level variable that controls the way mock objects respond to dir() (only for Python 2.6 or more recent).
# The default is True, which uses the filtering described below, to only show useful members.
# If you dislike this filtering, or need to switch it off for diagnostic purposes, then set mock.FILTER_DIR = False.
#

# 
# With filtering on, dir(some_mock) shows only useful attributes and will include any dynamically created attributes that wouldn’t normally be shown. 
# If the mock was created with a spec (or autospec of course) then all the attributes from the original are shown, even if they haven’t been accessed yet:
# 

dir(Mock())

#  ...

from urllib import request

dir(Mock(spec=request))

#  ...
 
#
# Many of the not-very-useful (private to Mock rather than the thing being mocked) underscore and double underscore prefixed attributes have been filtered
# from the result of calling dir() on a Mock.
# If you dislike this behaviour you can switch it off by setting the module level switch FILTER_DIR:
# 

from unittest import mock

mock.FILTER_DIR = False
      dir(mock.Mock())

# ...
 
#
# Alternatively you can just use vars(my_mock) (instance members) and dir(type(my_mock)) (type members) to bypass the filtering irrespective of
# mock.FILTER_DIR.
#
