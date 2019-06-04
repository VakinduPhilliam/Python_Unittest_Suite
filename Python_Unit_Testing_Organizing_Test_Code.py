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
# Organizing test code:
# The basic building blocks of unit testing are test cases — single scenarios that must be set up and checked for correctness.
# In unittest, test cases are represented by unittest.TestCase instances.
# To make your own test cases you must write subclasses of TestCase or use FunctionTestCase.
# The testing code of a TestCase instance should be entirely self contained, such that it can be run either in isolation or in arbitrary combination with
# any number of other test cases.
# The simplest TestCase subclass will simply implement a test method (i.e. a method whose name starts with test) in order to perform specific testing code:
# 

import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):

        widget = Widget('The widget')

        self.assertEqual(widget.size(), (50, 50))

#
# Note that in order to test something, we use one of the assert*() methods provided by the TestCase base class.
# If the test fails, an exception will be raised with an explanatory message, and unittest will identify the test case as a failure.
# Any other exceptions will be treated as errors.
# 
# Tests can be numerous, and their set-up can be repetitive.
# Luckily, we can factor out set-up code by implementing a method called setUp(), which the testing framework will automatically call for every single test
# we run:
# 

import unittest

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)

        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')
 

#
# Note:
# The order in which the various tests will be run is determined by sorting the test method names with respect to the built-in ordering for strings.
# If the setUp() method raises an exception while the test is running, the framework will consider the test to have suffered an error, and the test method
# will not be executed.
# 

#
# Similarly, we can provide a tearDown() method that tidies up after the test method has been run:
# 

import unittest

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

#
# If setUp() succeeded, tearDown() will be run whether the test method succeeded or not.
# Such a working environment for the testing code is called a test fixture.
#

#
# A new TestCase instance is created as a unique test fixture used to execute each individual test method.
# Thus setUp(), tearDown(), and __init__() will be called once per test.
# 

#
# It is recommended that you use TestCase implementations to group tests together according to the features they test.
# unittest provides a mechanism for this: the test suite, represented by unittest’s TestSuite class.
# In most cases, calling unittest.main() will do the right thing and collect all the module’s test cases for you and execute them.
# 

#
# However, should you want to customize the building of your test suite, you can do it yourself:
# 

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))

    suite.addTest(WidgetTestCase('test_widget_resize'))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    runner.run(suite())
