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
# Writing Unit Tests for the test package:
# It is preferred that tests that use the unittest module follow a few guidelines.
# One is to name the test module by starting it with test_ and end it with the name of the module being tested.
# The test methods in the test module should start with test_ and end with a description of what the method is testing.
# This is needed so that the methods are recognized by the test driver as test methods.
# Also, no documentation string for the method should be included.
# A comment (such as # Tests function returns only True or False) should be used to provide documentation for test methods.
# This is done because documentation strings get printed out if they exist and thus what test is being run is not stated.
#

# 
# A basic boilerplate is often used:
# 

import unittest
from test import support

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):

    # ... code to execute in preparation for tests ...

    def tearDown(self):

    #  ... code to execute to clean up after tests ...

    def test_feature_one(self):

        # Test feature one.

        # ... testing code ...

    def test_feature_two(self):

        # Test feature two.

        #... testing code ...

    # ... more test methods ...

class MyTestCase2(unittest.TestCase):

    # ... same structure as MyTestCase1 ...

# ... more test classes ...

if __name__ == '__main__':
    unittest.main()
