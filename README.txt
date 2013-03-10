.. contents::

rebecca.view
==============

``rebecca.view`` is helper classes for pyramid views.

BasicView methods and properties
------------------------------------------

properties::

- ``context`` view context passed to constructor
- ``request`` request passed to constructor
- ``response`` response attribute of ``request``
- ``body`` body attribute of ``request``

methods::

- ``redirect(url)`` create HTTPFound object from url
- ``redirect_route(route_name, **values)`` create HTTPFound object with route_url
- ``action_dispatch`` call method named *_action with request param.


USAGE
--------------

To use ``BasicView``, inherit that simply.::

    class Greeting(BasicView):
        def __call__(self):
            return self.redirect_route('top', v=1)
