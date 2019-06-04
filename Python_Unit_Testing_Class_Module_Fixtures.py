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
# Class and Module Fixtures:
# Class and module level fixtures are implemented in TestSuite. When the test suite encounters a test from a new class then tearDownClass() from the
# previous class (if there is one) is called, followed by setUpClass() from the new class.
#

#
# setUpClass and tearDownClass:
# These must be implemented as class methods.
# 

import unittest

class Test(unittest.TestCase):

    @classmethod

    def setUpClass(cls):
        cls._connection = createExpensiveConnectionObject()

    @classmethod

    def tearDownClass(cls):
        cls._connection.destroy()
 
#
# If you want the setUpClass and tearDownClass on base classes called then you must call up to them yourself.
# The implementations in TestCase are empty.
#

# 
# If an exception is raised during a setUpClass then the tests in the class are not run and the tearDownClass is not run.
# Skipped classes will not have setUpClass or tearDownClass run.
# If the exception is a SkipTest exception then the class will be reported as having been skipped instead of as an error.
#

#
# setUpModule and tearDownModuleK
# These should be implemented as functions:
# 

def setUpModule():
    createConnection()

def tearDownModule():
    closeConnection()

# 
# If an exception is raised in a setUpModule then none of the tests in the module will be run and the tearDownModule will not be run.
# If the exception is a SkipTest exception then the module will be reported as having been skipped instead of as an error.
#
