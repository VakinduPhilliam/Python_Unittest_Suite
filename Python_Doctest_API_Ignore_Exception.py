# Python Doctest API
# The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work
# exactly as shown.
#
#  There are several common ways to use doctest:
# > To check that a module’s docstrings are up-to-date by verifying that all interactive examples still work as documented.
# > To perform regression testing by verifying that interactive examples from a test file or a test object work as expected.
# > To write tutorial documentation for a package, liberally illustrated with input-output examples.
#   Depending on whether the examples or the expository text are emphasized, this has the flavor of “literate testing” or “executable documentation”.
#

#
# doctest.IGNORE_EXCEPTION_DETAIL: 
# When specified, an example that expects an exception passes if an exception of the expected type is raised, even if the exception detail does not match.
#

#
# For example, an example expecting ValueError: 42 will pass if the actual exception raised is ValueError: 3*14, but will fail, e.g., if TypeError is raised.
#

# 
# It will also ignore the module name used in Python 3 doctest reports.
# Hence both of these variations will work with the flag specified, regardless of whether the test is run under Python 2.7 or Python 3.2 (or later versions):
# 

raise CustomError('message')

raise CustomError('message')

#
# Note that ELLIPSIS can also be used to ignore the details of the exception message, but such a test may still fail based on whether or not the module
# details are printed as part of the exception name.
#
# Using IGNORE_EXCEPTION_DETAIL and the details from Python 2.3 is also the only clear way to write a doctest that doesn’t care about the exception detail
# yet continues to pass under Python 2.3 or earlier (those releases do not support doctest directives and ignore them as irrelevant comments).
#
# For example:
# 

(1, 2)[3] = 'moo'
 