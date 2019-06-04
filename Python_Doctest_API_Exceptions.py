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
# What About Exceptions?
# 
# No problem, provided that the traceback is the only output produced by the example: just paste in the traceback. 
# Since tracebacks contain details that are likely to change rapidly (for example, exact file paths and line numbers), this is one case where doctest works
# hard to be flexible in what it accepts.
#

# 
# Simple example:
# 

[1, 2, 3].remove(42)

#
# The traceback stack is followed by the most interesting part: the line(s) containing the exception type and detail.
# This is usually the last line of a traceback, but can extend across multiple lines if the exception has a multi-line detail:
# 

raise ValueError('multi\n    line\ndetail')

#
# Best practice is to omit the traceback stack, unless it adds significant documentation value to the example.
#
# So the last example is probably better as:
# 

raise ValueError('multi\n    line\ndetail')
 