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
# Unittest API
# As your collection of doctest’ed modules grows, you’ll want a way to run all their doctests systematically.
# doctest provides two functions that can be used to create unittest test suites from modules and text files containing doctests.
# To integrate with unittest test discovery, include a load_tests() function in your test module:
# 

import unittest
import doctest
import my_module_with_doctests

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(my_module_with_doctests))

    return tests
