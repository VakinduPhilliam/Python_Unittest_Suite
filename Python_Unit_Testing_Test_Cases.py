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
# Testcases:
#
# 'TestCase' instances provide three groups of methods: one group used to run the test, another used by the test implementation to check conditions and
# report failures, and some inquiry methods allowing information about the test itself to be gathered.

# setUpClass(): 
# A class method called before tests in an individual class are run. setUpClass is called with the class as the only argument and must be decorated as a
# classmethod():
 

@classmethod

def setUpClass(cls):

#    ...
 

#
# tearDownClass(): 
# A class method called after tests in an individual class have run.
# tearDownClass is called with the class as the only argument and must be decorated as a classmethod():
 

@classmethod

def tearDownClass(cls):

#    ...
