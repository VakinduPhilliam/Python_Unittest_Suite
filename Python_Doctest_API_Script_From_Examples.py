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
# doctest.script_from_examples(s): 
# Convert text with examples to a script.
#
# Argument s is a string containing doctest examples.
# The string is converted to a Python script, where doctest examples in s are converted to regular code, and everything else is converted to Python comments.
# The generated script is returned as a string.
#
# For example,
# 

import doctest

print(doctest.script_from_examples(r"""
    Set x and y to 1 and 2.
    >>> x, y = 1, 2

    Print their sum:
    >>> print(x+y)
    3
"""))
 
# 
# displays:
# 

# Set x and y to 1 and 2.

x, y = 1, 2

#
# Print their sum:

print(x+y)

# Expected:
## 3
