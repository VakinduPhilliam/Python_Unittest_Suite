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
# Checking Examples in a Text File:
# Another simple application of doctest is testing interactive examples in a text file.
#
# This can be done with the testfile() function:
# 

import doctest

doctest.testfile("example.txt")

# 
# That short script executes and verifies any interactive Python examples contained in the file example.txt.
# The file content is treated as if it were a single giant docstring; the file doesn’t need to contain a Python program!
#
 