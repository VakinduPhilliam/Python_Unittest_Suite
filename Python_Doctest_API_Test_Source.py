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
 
# doctest.testsource(module, name): 
# Convert the doctest for an object to a script.
#

# 
# Argument module is a module object, or dotted name of a module, containing the object whose doctests are of interest.
# Argument name is the name (within the module) of the object with the doctests of interest.
# The result is a string, containing the object’s docstring converted to a Python script, as described for script_from_examples() above.
#
# For example, if module a.py contains a top-level function f(), then
# 

import a, doctest

print(doctest.testsource(a, "a.f"))
 
#
# prints a script version of function f()’s docstring, with doctests converted to code, and the rest placed in comments.
#