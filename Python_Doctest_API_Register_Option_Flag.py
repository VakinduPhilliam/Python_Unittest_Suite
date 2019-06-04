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
# doctest.register_optionflag(name) 
# Create a new option flag with a given name, and return the new flag’s integer value.
# register_optionflag() can be used when subclassing OutputChecker or DocTestRunner to create new options that are supported by your subclasses.
# register_optionflag() should always be called using the following idiom:
# 

MY_FLAG = register_optionflag('MY_FLAG')
