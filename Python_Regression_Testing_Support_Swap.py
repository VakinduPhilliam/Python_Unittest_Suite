# Python Regression Testing
# test — Regression tests package for Python
# 
##########################################################################################################################################################
#
# NOTE:
#
# The test package is meant for internal use by Python only. It is documented for the benefit of the core developers of Python.
# Any use of this package outside of Python’s standard library is discouraged as code mentioned here can change or be removed without notice between
# releases of Python.
#
########################################################################################################################################################## 
#
# The test package contains all regression tests for Python as well as the modules test.support and test.regrtest.
# test.support is used to enhance your tests while test.regrtest drives the testing suite.
# 
# Each module in the test package whose name starts with test_ is a testing suite for a specific module or feature.
# All new tests should be written using the unittest or doctest module. Some older tests are written using a “traditional” testing style that compares
# output printed to sys.stdout; this style of test is considered deprecated.
#

#
# test.support.swap_attr(obj, attr, new_val): 
# Context manager to swap out an attribute with a new object.
#

# 
# Usage:
# 

with swap_attr(obj, "attr", 5):

#    ...
 
#
# This will set obj.attr to 5 for the duration of the with block, restoring the old value at the end of the block.
# If attr doesn’t exist on obj, it will be created and then deleted at the end of the block.
#

#
# test.support.swap_item(obj, attr, new_val): 
# Context manager to swap out an item with a new object.

# 
# Usage:
# 

with swap_item(obj, "item", 5):

#    ...
