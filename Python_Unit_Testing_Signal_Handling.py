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
# Signal Handling:
# 

#
# The -c/--catch command-line option to unittest, along with the catchbreak parameter to unittest.main(), provide more friendly handling of control-C during
# a test run.
# With catch break behavior enabled control-C will allow the currently running test to complete, and the test run will then end and report all the results 
# so far.
# A second control-c will raise a KeyboardInterrupt in the usual way.
# 
# The control-c handling signal handler attempts to remain compatible with code or tests that install their own signal.SIGINT handler.
# If the unittest handler is called but isn’t the installed signal.SIGINT handler, i.e. it has been replaced by the system under test and delegated to, then
# it calls the default handler.
# This will normally be the expected behavior by code that replaces an installed handler and delegates to it.
# For individual tests that need unittest control-c handling disabled the removeHandler() decorator can be used.
#
# There are a few utility functions for framework authors to enable control-c handling functionality within test frameworks.
#
# unittest.installHandler() 
# Install the control-c handler. When a signal.SIGINT is received (usually in response to the user pressing control-c) all registered results have stop()
# called.
#
# unittest.registerResult(result) 
# Register a TestResult object for control-c handling.
# Registering a result stores a weak reference to it, so it doesn’t prevent the result from being garbage collected.
# 
# Registering a TestResult object has no side-effects if control-c handling is not enabled, so test frameworks can unconditionally register all results they
# create independently of whether or not handling is enabled.
#
# unittest.removeResult(result) 
# Remove a registered result. Once a result has been removed then stop() will no longer be called on that result object in response to a control-c.
#
# unittest.removeHandler(function=None) 
# When called without arguments this function removes the control-c handler if it has been installed. This function can also be used as a test decorator to
# temporarily remove the handler while the test is being executed:
 

@unittest.removeHandler

def test_signal_handling(self):

#    ...
