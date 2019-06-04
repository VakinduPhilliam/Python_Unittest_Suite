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
# Attaching Mocks as Attributes.
# When you attach a mock as an attribute of another mock (or as the return value) it becomes a “child” of that mock. Calls to the child are recorded in the
# method_calls and mock_calls attributes of the parent. This is useful for configuring child mocks and then attaching them to the parent, or for attaching
# mocks to a parent that records all calls to the children and allows you to make assertions about the order of calls between mocks:
# 

parent = MagicMock()
child1 = MagicMock(return_value=None)
child2 = MagicMock(return_value=None)

parent.child1 = child1
parent.child2 = child2

child1(1)
child2(2)

parent.mock_calls

# OUTPUT: '[call.child1(1), call.child2(2)]'
 
#
# The exception to this is if the mock has a name.
# This allows you to prevent the “parenting” if for some reason you don’t want it to happen.
# 

mock = MagicMock()

not_a_child = MagicMock(name='not-a-child')

mock.attribute = not_a_child
mock.attribute()

# OUTPUT: '<MagicMock name='not-a-child()' id='...'>'

mock.mock_calls

# OUTPUT: '[]'

# 
# Mocks created for you by patch() are automatically given names.
# To attach mocks that have names to a parent you use the attach_mock() method:
# 

thing1 = object()
thing2 = object()

parent = MagicMock()

with patch('__main__.thing1', return_value=None) as child1:
        with patch('__main__.thing2', return_value=None) as child2:

            parent.attach_mock(child1, 'child1')
            parent.attach_mock(child2, 'child2')

            child1('one')
            child2('two')

parent.mock_calls

# OUTPUT: '[call.child1('one'), call.child2('two')]'
 
#
# The only exceptions are magic methods and attributes (those that have leading and trailing double underscores).
# Mock doesn’t create these but instead raises an AttributeError.
# This is because the interpreter will often implicitly request these methods, and gets very confused to get a new Mock object when it expects a magic
# method.
# If you need magic method support see magic methods.
#
