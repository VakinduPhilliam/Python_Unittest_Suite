# Python Test Mock
# unittest.mock — mock object library
# unittest.mock is a library for testing in Python.
# It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.
# unittest.mock provides a core Mock class removing the need to create a host of stubs throughout your test suite.
# After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with.
# You can also specify return values and set needed attributes in the normal way.
# 
# Additionally, mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test, along with sentinel
# for creating unique objects.
# 
# Mock is very easy to use and is designed for use with unittest. Mock is based on the ‘action -> assertion’ pattern instead of ‘record -> replay’ used by
# many mocking frameworks.
#

#
# Partial mocking:
# In some tests I wanted to mock out a call to datetime.date.today() to return a known date, but I didn’t want to prevent the code under test from creating
# new date objects.
# Unfortunately datetime.date is written in C, and so I couldn’t just monkey-patch out the static date.today() method.
# The patch decorator is used here to mock out the date class in the module under test.
# The side_effect attribute on the mock date class is then set to a lambda function that returns a real date.
# When the mock date class is called a real date will be constructed and returned by side_effect.
# 

from datetime import date

    with patch('mymodule.date') as mock_date:
        mock_date.today.return_value = date(2010, 10, 8)

        mock_date.side_effect = lambda *args, **kw: date(*args, **kw)

        assert mymodule.date.today() == date(2010, 10, 8)

        assert mymodule.date(2009, 6, 8) == date(2009, 6, 8)
