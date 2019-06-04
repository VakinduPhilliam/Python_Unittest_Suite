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
# How are Docstring Examples Recognized?
#

# 
# In most cases a copy-and-paste of an interactive console session works fine, but doctest isn’t trying to do an exact emulation of any specific Python
# shell.
# 

# comments are ignored

x = 12
x

# OUTPUT: '12'

if x == 13:
        print("yes")

    else:
        print("no")
        print("NO")

        print("NO!!!")

#
# If you continue a line via backslashing in an interactive session, or for any other reason use a backslash, you should use a raw docstring, which will
# preserve your backslashes exactly as you type them:
# 

def f(x):
        r'''Backslashes in a raw docstring: m\n'''

        print(f.__doc__)

#
# Backslashes in a raw docstring: m\n
# Otherwise, the backslash will be interpreted as part of the string.
#
# For example, the \n above would be interpreted as a newline character.
# Alternatively, you can double each backslash in the doctest version (and not use a raw string):
# 

def f(x):
        '''Backslashes in a raw docstring: m\\n'''

print(f.__doc__)

#
# Backslashes in a raw docstring: m\n
# 

#
# The starting column doesn’t matter:
# 

assert "Easy!"

import math

math.floor(1.9)
 