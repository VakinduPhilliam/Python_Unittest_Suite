# Python Unit Testing
# unittest — Unit testing framework.
# Unittest supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from
# the reporting framework.
# 
# To achieve this, unittest supports some important concepts in an object-oriented way:
#
# 'test fixture': A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions.
# This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
#
# 'test case': A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs.
# unittest provides a base class, TestCase, which may be used to create new test cases.
#
# 'test suite': A test suite is a collection of test cases, test suites, or both.
# It is used to aggregate tests that should be executed together.
#
# 'test runner': A test runner is a component which orchestrates the execution of tests and provides the outcome to the user.
# The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.
#

#
# Basic example:
# The unittest module provides a rich set of tools for constructing and running tests.
# This section demonstrates that a small subset of the tools suffice to meet the needs of most users.
#
 
#
# Here is a short script to test three string methods:
# 

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):

        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
 
        self.assertEqual(s.split(), ['hello', 'world'])

        # check that s.split fails when the separator is not a string

        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':

    unittest.main()

#
# A testcase is created by subclassing unittest.TestCase.
# The three individual tests are defined with methods whose names start with the letters test.
# This naming convention informs the test runner about which methods represent tests.
#

#
# The crux of each test is a call to assertEqual() to check for an expected result; assertTrue() or assertFalse() to verify a condition; or assertRaises()
# to verify that a specific exception gets raised.
#

#
# These methods are used instead of the assert statement so the test runner can accumulate all test results and produce a report.
# The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method.
# They are covered in more detail in the section Organizing test code.
#
