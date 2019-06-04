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
# Tracking order of calls and less verbose call assertions
# The Mock class allows you to track the order of method calls on your mock objects through the method_calls attribute.
# This doesn’t allow you to track the order of calls between separate mock objects, however we can use mock_calls to achieve the same effect.
#
# Because mocks track calls to child mocks in mock_calls, and accessing an arbitrary attribute of a mock creates a child mock, we can create our separate
# mocks from a parent one. Calls to those child mock will then all be recorded, in order, in the mock_calls of the parent:
 
manager = Mock()

mock_foo = manager.foo
mock_bar = manager.bar
 

mock_foo.something()

# OUTPUT: '<Mock name='mock.foo.something()' id='...'>'

mock_bar.other.thing()

# OUTPUT: '<Mock name='mock.bar.other.thing()' id='...'>'
 
manager.mock_calls

# OUTPUT: '[call.foo.something(), call.bar.other.thing()]'
 
#
# We can then assert about the calls, including the order, by comparing with the mock_calls attribute on the manager mock:
# 

expected_calls = [call.foo.something(), call.bar.other.thing()]
manager.mock_calls == expected_calls

# OUTPUT: 'True'

# 
# If patch is creating, and putting in place, your mocks then you can attach them to a manager mock using the attach_mock() method.
# After attaching calls will be recorded in mock_calls of the manager.
# 

manager = MagicMock()

with patch('mymodule.Class1') as MockClass1:
        with patch('mymodule.Class2') as MockClass2:

            manager.attach_mock(MockClass1, 'MockClass1')
            manager.attach_mock(MockClass2, 'MockClass2')

            MockClass1().foo()
            MockClass2().bar()

# OUTPUT: '<MagicMock name='mock.MockClass1().foo()' id='...'>'
# OUTPUT: '<MagicMock name='mock.MockClass2().bar()' id='...'>'

manager.mock_calls

#
# If many calls have been made, but you’re only interested in a particular sequence of them then an alternative is to use the assert_has_calls() method.
# This takes a list of calls (constructed with the call object).
# If that sequence of calls are in mock_calls then the assert succeeds.
# 

m = MagicMock()
m().foo().bar().baz()

# OUTPUT: '<MagicMock name='mock().foo().bar().baz()' id='...'>'

m.one().two().three()

# OUTPUT: '<MagicMock name='mock.one().two().three()' id='...'>'

calls = call.one().two().three().call_list()

m.assert_has_calls(calls)

# 
# Even though the chained call m.one().two().three() aren’t the only calls that have been made to the mock, the assert still succeeds.
# Sometimes a mock may have several calls made to it, and you are only interested in asserting about some of those calls. You may not even care about the
# order.
# In this case you can pass any_order=True to assert_has_calls:
# 

m = MagicMock()

m(1), m.two(2, 3), m.seven(7), m.fifty('50')

# OUTPUT: '(...)'

calls = [call.fifty('50'), call(1), call.seven(7)]

m.assert_has_calls(calls, any_order=True)
