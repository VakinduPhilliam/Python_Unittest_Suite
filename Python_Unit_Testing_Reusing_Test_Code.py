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
# Re-using old test code
#
 
#
# Some users will find that they have existing test code that they would like to run from unittest, without converting every old test function to a TestCase
# subclass.
#

# 
# For this reason, unittest provides a FunctionTestCase class. This subclass of TestCase can be used to wrap an existing test function.
# Set-up and tear-down functions can also be provided.
#

# 
# Given the following test function:
# 

def testSomething():
    something = makeSomething()

    assert something.name is not None

    # ...

# 
# one can create an equivalent test case instance as follows, with optional set-up and tear-down methods:
# 

testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=makeSomethingDB,
                                     tearDown=deleteSomethingDB) 

#
# Note:
# Even though FunctionTestCase can be used to quickly convert an existing test base over to a unittest-based system, this approach is not recommended.
# Taking the time to set up proper TestCase subclasses will make future test refactorings infinitely easier.
#
 
#
# In some cases, the existing tests may have been written using the doctest module.
# If so, doctest provides a DocTestSuite class that can automatically build unittest.TestSuite instances from the existing doctest-based tests.
#
