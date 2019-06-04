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
# Test Runner:
#
# When you have placed your tests in a module, the module can itself be the test runner.
# When a test fails, you can arrange for your test runner to re-run only the failing doctest while you debug the problem.
#
# Here is a minimal example of such a test runner:
# 

if __name__ == '__main__':
    import doctest

    flags = doctest.REPORT_NDIFF|doctest.FAIL_FAST

    if len(sys.argv) > 1:
        name = sys.argv[1]

        if name in globals():
            obj = globals()[name]

        else:
            obj = __test__[name]

        doctest.run_docstring_examples(obj, globals(), name=name,
                                       optionflags=flags)
    else:
        fail, total = doctest.testmod(optionflags=flags)

        print("{} failures out of {} tests".format(fail, total))
