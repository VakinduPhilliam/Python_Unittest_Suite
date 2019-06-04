# Python Regression Testing
# test — Regression tests package for Python
# 
##########################################################################################################################################################
#
# NOTE:
#
# The test package is meant for internal use by Python only. It is documented for the benefit of the core developers of Python.
# Any use of this package outside of Python’s standard library is discouraged as code mentioned here can change or be removed without notice between
# releases of Python.
#
########################################################################################################################################################## 
#
# The test package contains all regression tests for Python as well as the modules test.support and test.regrtest.
# test.support is used to enhance your tests while test.regrtest drives the testing suite.
# 
# Each module in the test package whose name starts with test_ is a testing suite for a specific module or feature.
# All new tests should be written using the unittest or doctest module. Some older tests are written using a “traditional” testing style that compares
# output printed to sys.stdout; this style of test is considered deprecated.
#

#
# test.support.check__all__(test_case, module, name_of_module=None, extra=(), blacklist=()):
# Assert that the __all__ variable of module contains all public names.
#
# The module’s public names (its API) are detected automatically based on whether they match the public name convention and were defined in module.
# The 'name_of_module' argument can specify (as a string or tuple thereof) what module(s) an API could be defined in order to be detected as a public API.
# One case for this is when module imports part of its public API from other modules, possibly a C backend (like csv and its _csv).
#
# The 'extra' argument can be a set of names that wouldn’t otherwise be automatically detected as “public”, like objects without a proper __module__ attribute.
# If provided, it will be added to the automatically detected ones.
#
# The 'blacklist' argument can be a set of names that must not be treated as part of the public API even though their names indicate otherwise.
#
 
#
# Example use:
# 

import bar
import foo
import unittest

from test import support

class MiscTestCase(unittest.TestCase):

    def test__all__(self):
        support.check__all__(self, foo)

class OtherTestCase(unittest.TestCase):

    def test__all__(self):
        extra = {'BAR_CONST', 'FOO_CONST'}

        blacklist = {'baz'}  # Undocumented name.

        # bar imports part of its API from _bar.

        support.check__all__(self, bar, ('bar', '_bar'),
                             extra=extra, blacklist=blacklist)
