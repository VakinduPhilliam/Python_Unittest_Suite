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
# Autospeccing:
# 
# Autospeccing is based on the existing spec feature of mock. It limits the api of mocks to the api of an original object (the spec), but it is recursive
# (implemented lazily) so that attributes of mocks only have the same api as the attributes of the spec.
# In addition mocked functions / methods have the same call signature as the original so they raise a TypeError if they are called incorrectly.
# Mock is a very powerful and flexible object, but it suffers from two flaws when used to mock out objects from a system under test. One of these flaws is
# specific to the Mock api and the other is a more general problem with using mock objects.
#

#
# Mock has two assert methods that are extremely handy: assert_called_with() and assert_called_once_with().
# 

mock = Mock(name='Thing', return_value=None)
mock(1, 2, 3)

mock.assert_called_once_with(1, 2, 3)
mock(1, 2, 3)

mock.assert_called_once_with(1, 2, 3)

# 
# Because mocks auto-create attributes on demand, and allow you to call them with arbitrary arguments, if you misspell one of these assert methods then your
# assertion is gone:
# 

mock = Mock(name='Thing', return_value=None)
mock(1, 2, 3)

mock.assret_called_once_with(4, 5, 6)

# 
# Your tests can pass silently and incorrectly because of the typo.
# The second issue is more general to mocking. If you refactor some of your code, rename members and so on, any tests for code that is still using the old
# api but uses mocks instead of the real objects will still pass. This means your tests can all pass even though your code is broken.
#
 
#
# Note that this is another reason why you need integration tests as well as unit tests. Testing everything in isolation is all fine and dandy, but if you
# don’t test how your units are “wired together” there is still lots of room for bugs that tests might have caught.
# mock already provides a feature to help with this, called speccing. If you use a class or instance as the spec for a mock then you can only access
# attributes on the mock that exist on the real class:
# 

from urllib import request

mock = Mock(spec=request.Request)
mock.assret_called_with

#
# The spec only applies to the mock itself, so we still have the same issue with any methods on the mock:
# 

mock.has_data()

# OUTPUT: '<mock.Mock object at 0x...>'

mock.has_data.assret_called_with()

# 
# Auto-speccing solves this problem. You can either pass autospec=True to patch() / patch.object() or use the create_autospec() function to create a mock 
# with a spec. If you use the autospec=True argument to patch() then the object that is being replaced will be used as the spec object.
# Because the speccing is done “lazily” (the spec is created as attributes on the mock are accessed) you can use it with very complex or deeply nested
# objects (like modules that import modules that import modules) without a big performance hit.
# 

#
# Here’s an example of it in use:
# 

from urllib import request

patcher = patch('__main__.request', autospec=True)
mock_request = patcher.start()

request is mock_request

# OUTPUT: 'True'

mock_request.Request

# OUTPUT: '<MagicMock name='request.Request' spec='Request' id='...'>'
 
#
# You can see that request.Request has a spec. request.Request takes two arguments in the constructor (one of which is self).
#

#
# Here’s what happens if we try to call it incorrectly:
# 

req = request.Request()

#
# The spec also applies to instantiated classes (i.e. the return value of specced mocks):
# 

req = request.Request('foo')
req

# OUTPUT: '<NonCallableMagicMock name='request.Request()' spec='Request' id='...'>'

# 
# Request objects are not callable, so the return value of instantiating our mocked out request.Request is a non-callable mock.
# With the spec in place any typos in our asserts will raise the correct error:
# 

req.add_header('spam', 'eggs')

# OUTPUT: '<MagicMock name='request.Request().add_header()' id='...'>'

req.add_header.assret_called_with

req.add_header.assert_called_with('spam', 'eggs')

# 
# In many cases you will just be able to add autospec=True to your existing patch() calls and then be protected against bugs due to typos and api changes.
#
 
#
# As well as using autospec through patch() there is a create_autospec() for creating autospecced mocks directly:
# 

from urllib import request

mock_request = create_autospec(request)
mock_request.Request('foo', 'bar')

# OUTPUT: '<NonCallableMagicMock name='mock.Request()' spec='Request' id='...'>'

# 
# This isn’t without caveats and limitations however, which is why it is not the default behaviour.
# In order to know what attributes are available on the spec object, autospec has to introspect (access attributes) the spec.
# As you traverse attributes on the mock a corresponding traversal of the original object is happening under the hood.
# If any of your specced objects have properties or descriptors that can trigger code execution then you may not be able to use autospec.
# On the other hand it is much better to design your objects so that introspection is safe.
# 

#
# A more serious problem is that it is common for instance attributes to be created in the __init__() method and not to exist on the class at all.
# autospec can’t know about any dynamically created attributes and restricts the api to visible attributes.
# 

class Something:
      def __init__(self):

        self.a = 33

      with patch('__main__.Something', autospec=True):
      thing = Something()

      thing.a

#
# There are a few different ways of resolving this problem.
# The easiest, but not necessarily the least annoying, way is to simply set the required attributes on the mock after creation.
# Just because autospec doesn’t allow you to fetch attributes that don’t exist on the spec it doesn’t prevent you setting them:
# 

with patch('__main__.Something', autospec=True):
      thing = Something()

      thing.a = 33

# 
# There is a more aggressive version of both spec and autospec that does prevent you setting non-existent attributes.
# This is useful if you want to ensure your code only sets valid attributes too, but obviously it prevents this particular scenario:
# 

with patch('__main__.Something', autospec=True, spec_set=True):
      thing = Something()

      thing.a = 33

#
# Probably the best way of solving the problem is to add class attributes as default values for instance members initialised in __init__().
# Note that if you are only setting default attributes in __init__() then providing them via class attributes (shared between instances of course) is faster
# too. e.g.
# 

class Something:
       a = 33

# 
# This brings up another issue.
# It is relatively common to provide a default value of None for members that will later be an object of a different type.
# None would be useless as a spec because it wouldn’t let you access any attributes or methods on it.
# As None is never going to be useful as a spec, and probably indicates a member that will normally of some other type, autospec doesn’t use a spec for
# members that are set to None. These will just be ordinary mocks (well - MagicMocks):
# 

class Something:
        member = None

mock = create_autospec(Something)

mock.member.foo.bar.baz()

# OUTPUT: '<MagicMock name='mock.member.foo.bar.baz()' id='...'>'
 
#
# If modifying your production classes to add defaults isn’t to your liking then there are more options.
# One of these is simply to use an instance as the spec rather than the class.
# The other is to create a subclass of the production class and add the defaults to the subclass without affecting the production class.
# Both of these require you to use an alternative object as the spec.
# Thankfully patch() supports this - you can simply pass the alternative object as the autospec argument:
# 

class Something:
      def __init__(self):

      self.a = 33

class SomethingForTest(Something):
      a = 33

p = patch('__main__.Something', autospec=SomethingForTest)
mock = p.start()

mock.a

# OUTPUT: '<NonCallableMagicMock name='Something.a' spec='int' id='...'>'
