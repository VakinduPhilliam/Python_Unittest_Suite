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
# Loader:
# 'loader' is the instance of TestLoader doing the loading.
# standard_tests are the tests that would be loaded by default from the module.
# It is common for test modules to only want to add or remove tests from the standard set of tests.
# The third argument is used when loading packages as part of test discovery.
#

# 
# A typical load_tests function that loads tests from a specific set of TestCase classes may look like:
# 

test_cases = (TestCase1, TestCase2, TestCase3)

def load_tests(loader, tests, pattern):
    suite = TestSuite()

    for test_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_class)

        suite.addTests(tests)

    return suite

# 
# If discovery is started in a directory containing a package, either from the command line or by calling TestLoader.discover(), then
# the package __init__.py will be checked for load_tests.
# If that function does not exist, discovery will recurse into the package as though it were just another directory.
# Otherwise, discovery of the package’s tests will be left up to load_tests which is called with the following arguments:
# 

# load_tests(loader, standard_tests, pattern)

#
# This should return a TestSuite representing all the tests from the package.
# (standard_tests will only contain tests collected from __init__.py.)
#

# 
# Because the pattern is passed into load_tests the package is free to continue (and potentially modify) test discovery.
# A ‘do nothing’ load_tests function for a test package would look like:
# 

def load_tests(loader, standard_tests, pattern):

    # top level directory cached on loader instance

    this_dir = os.path.dirname(__file__)

    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)

    standard_tests.addTests(package_tests)

    return standard_tests

