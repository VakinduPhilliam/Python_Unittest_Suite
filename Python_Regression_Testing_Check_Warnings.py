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
# test.support.check_warnings(*filters, quiet=True): 
# A convenience wrapper for warnings.catch_warnings() that makes it easier to test that a warning was correctly raised.
# It is approximately equivalent to calling warnings.catch_warnings(record=True) with warnings.simplefilter() set to always and with the option to
# automatically validate the results that are recorded.
#

#
# If no arguments are specified, it defaults to:
# 

check_warnings(("", Warning), quiet=True)

#
# In this case all warnings are caught and no errors are raised.
# On entry to the context manager, a WarningRecorder instance is returned.
# The underlying warnings list from catch_warnings() is available via the recorder object’s warnings attribute.
# As a convenience, the attributes of the object representing the most recent warning can also be accessed directly through the recorder object.
# If no warning has been raised, then any of the attributes that would otherwise be expected on an object representing a warning will return None.
# The recorder object also has a reset() method, which clears the warnings list.
#
 
#
# The context manager is designed to be used like this:
# 

with check_warnings(("assertion is always true", SyntaxWarning),
                    ("", UserWarning)):

    exec('assert(False, "Hey!")')

    warnings.warn(UserWarning("Hide me!"))

# 
# In this case if either warning was not raised, or some other warning was raised, check_warnings() would raise an error.
# 
# When a test needs to look more deeply into the warnings, rather than just checking whether or not they occurred, code like this can be used:
# 

with check_warnings(quiet=True) as w:
    warnings.warn("foo")
    assert str(w.args[0]) == "foo"

    warnings.warn("bar")
    assert str(w.args[0]) == "bar"

    assert str(w.warnings[0].args[0]) == "foo"
    assert str(w.warnings[1].args[0]) == "bar"

    w.reset()
    assert len(w.warnings) == 0
