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
# assertRaises(exception, callable, *args, **kwds) assertRaises(exception, *, msg=None):
# Test that an exception is raised when callable is called with any positional or keyword arguments that are also passed to assertRaises().
# The test passes if exception is raised, is an error if another exception is raised, or fails if no exception is raised.
# To catch any of a group of exceptions, a tuple containing the exception classes may be passed as exception.
#
 
#
# If only the exception and possibly the msg arguments are given, return a context manager so that the code under test can be written inline rather than as
# a function:
# 

with self.assertRaises(SomeException):
    do_something()

# 
# When used as a context manager, assertRaises() accepts the additional keyword argument msg.
#

# 
# The context manager will store the caught exception object in its exception attribute.
# This can be useful if the intention is to perform additional checks on the exception raised:
# 

with self.assertRaises(SomeException) as cm:
    do_something()

the_exception = cm.exception

self.assertEqual(the_exception.error_code, 3)

#
# assertRaisesRegex(exception, regex, callable, *args, **kwds) assertRaisesRegex(exception, regex, *, msg=None):
# Like assertRaises() but also tests that regex matches on the string representation of the raised exception. regex may be a regular expression object or a
# string containing a regular expression suitable for use by re.search().
#
# Examples:
# 

self.assertRaisesRegex(ValueError, "invalid literal for.*XYZ'$",
                       int, 'XYZ')

# 
# or:
# 

with self.assertRaisesRegex(ValueError, 'literal'):
   int('XYZ')

#
# assertWarns(warning, callable, *args, **kwds) assertWarns(warning, *, msg=None):
# Test that a warning is triggered when callable is called with any positional or keyword arguments that are also passed to assertWarns().
# The test passes if warning is triggered and fails if it isn’t. Any exception is an error. To catch any of a group of warnings, a tuple containing the
# warning classes may be passed as warnings.
#

# 
# If only the warning and possibly the msg arguments are given, return a context manager so that the code under test can be written inline rather than as a
# function:
# 

with self.assertWarns(SomeWarning):
           do_something()
 
#
# When used as a context manager, assertWarns() accepts the additional keyword argument msg.
# The context manager will store the caught warning object in its warning attribute, and the source line which triggered the warnings in the filename and
# lineno attributes.
# This can be useful if the intention is to perform additional checks on the warning caught:
# 

with self.assertWarns(SomeWarning) as cm:
    do_something()

self.assertIn('myfile.py', cm.filename)

self.assertEqual(320, cm.lineno)

# 
# This method works regardless of the warning filters in place when it is called.
# 

#
# assertWarnsRegex(warning, regex, callable, *args, **kwds) assertWarnsRegex(warning, regex, *, msg=None):
# Like assertWarns() but also tests that regex matches on the message of the triggered warning. regex may be a regular expression object or a string
# containing a regular expression suitable for use by re.search().
#
# Example:
# 

self.assertWarnsRegex(DeprecationWarning,
                      r'legacy_function\(\) is deprecated',
                      legacy_function, 'XYZ')

# 
# or:
# 

with self.assertWarnsRegex(RuntimeWarning, 'unsafe frobnicating'):
         frobnicate('/etc/passwd')

#
# assertLogs(logger=None, level=None): 
# A context manager to test that at least one message is logged on the logger or one of its children, with at least the given level.
#
 
#
# If given, logger should be a logging.Logger object or a str giving the name of a logger. The default is the root logger, which will catch all messages.
# If given, level should be either a numeric logging level or its string equivalent (for example either "ERROR" or logging.ERROR).
# The default is logging.INFO.
# The test passes if at least one message emitted inside the with block matches the logger and level conditions, otherwise it fails.
# The object returned by the context manager is a recording helper which keeps tracks of the matching log messages.
# It has two attributes:
#

# records: 
# A list of logging.LogRecord objects of the matching log messages.
# output: 
# A list of str objects with the formatted output of matching messages.

# 
# Example:
# 

with self.assertLogs('foo', level='INFO') as cm:
   logging.getLogger('foo').info('first message')

   logging.getLogger('foo.bar').error('second message')

self.assertEqual(cm.output, ['INFO:foo:first message',
                             'ERROR:foo.bar:second message'])

#
# assertGreater(first, second, msg=None)
# assertGreaterEqual(first, second, msg=None)
# assertLess(first, second, msg=None)
# assertLessEqual(first, second, msg=None)
#
#  Test that first is respectively >, >=, < or <= than second depending on the method name.
#
# If not, the test will fail:
 
self.assertGreaterEqual(3, 4)

# OUTPUT: 'AssertionError: "3" unexpectedly not greater than or equal to "4"'
