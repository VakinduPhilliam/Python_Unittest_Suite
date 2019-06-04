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
# test.support.import_fresh_module(name, fresh=(), blocked=(), deprecated=False): 
# This function imports and returns a fresh copy of the named Python module by removing the named module from sys.modules before doing the import.
# Note that unlike reload(), the original module is not affected by this operation.
# 
# 'fresh' is an iterable of additional module names that are also removed from the sys.modules cache before doing the import.
# 'blocked' is an iterable of module names that are replaced with None in the module cache during the import to ensure that attempts to import them raise
# ImportError.
#

#
# Example use:
# 

# Get copies of the warnings module for testing without affecting the
# version being used by the rest of the test suite. One copy uses the
# C implementation, the other is forced to use the pure Python fallback
# implementation

py_warnings = import_fresh_module('warnings', blocked=['_warnings'])

c_warnings = import_fresh_module('warnings', fresh=['_warnings'])
