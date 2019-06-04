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
# unittest.main(module='__main__', defaultTest=None, argv=None, testRunner=None, testLoader=unittest.defaultTestLoader, exit=True, verbosity=1,
# failfast=None, catchbreak=None, buffer=None, warnings=None):
#

#
# A command-line program that loads a set of tests from module and runs them; this is primarily for making test modules conveniently executable.
# The simplest use for this function is to include the following line at the end of a test script:
# 

if __name__ == '__main__':
    unittest.main()

# 
# You can run tests with more detailed information by passing in the verbosity argument:
# 

if __name__ == '__main__':
    unittest.main(verbosity=2)

#
# main supports being used from the interactive interpreter by passing in the argument exit=False.
# This displays the result on standard output without calling sys.exit():
# 

from unittest import main

main(module='test_module', exit=False)
