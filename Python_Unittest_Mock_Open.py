# Python Unittest
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
# mock_open:
# unittest.mock.mock_open(mock=None, read_data=None). 
# A helper function to create a mock to replace the use of open().
# It works for open() called directly or used as a context manager.
# The mock argument is the mock object to configure. If None (the default) then a MagicMock will be created for you, with the API limited to methods or
# attributes available on standard file handles.
# 

#
# read_data is a string for the read(), readline(), and readlines() methods of the file handle to return.
# Calls to those methods will take data from read_data until it is depleted. The mock of these methods is pretty simplistic: every time the mock is called,
# the read_data is rewound to the start. If you need more control over the data that you are feeding to the tested code you will need to customize this
# mock for yourself. When that is insufficient, one of the in-memory filesystem packages on PyPI can offer a realistic filesystem for testing.
#

#
# Using open() as a context manager is a great way to ensure your file handles are closed properly and is becoming common:
# 

with open('/some/path', 'w') as f:
         f.write('something')

# 
# The issue is that even if you mock out the call to open() it is the returned object that is used as a context manager (and has __enter__() and __exit__()
# called).
#

# 
# Mocking context managers with a MagicMock is common enough and fiddly enough that a helper function is useful.
# 

m = mock_open()


with patch('__main__.open', m):
        with open('foo', 'w') as h:

            h.write('some stuff')


m.mock_calls
m.assert_called_once_with('foo', 'w')

handle = m()
handle.write.assert_called_once_with('some stuff')

# 
# And for reading files:
# 

with patch('__main__.open', mock_open(read_data='bibble')) as m:
         with open('foo') as h:
              result = h.read()

m.assert_called_once_with('foo')

assert result == 'bibble'
