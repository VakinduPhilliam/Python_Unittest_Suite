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
# test.support.load_package_tests(pkg_dir, loader, standard_tests, pattern): 
# Generic implementation of the unittest load_tests protocol for use in test packages. pkg_dir is the root directory of the package; loader, standard_tests,
# and pattern are the arguments expected by load_tests.
#
# In simple cases, the test package’s __init__.py can be the following:
# 

import os

from test.support import load_package_tests

def load_tests(*args):

          return load_package_tests(os.path.dirname(__file__), *args)
