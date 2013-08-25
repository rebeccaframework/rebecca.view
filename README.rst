.. contents::

rebecca.view
==============

``rebecca.view`` is helper classes for pyramid views.

BasicView methods and properties
------------------------------------------

properties

- ``context`` view context passed to constructor
- ``request`` request passed to constructor
- ``response`` response attribute of ``request``
- ``body`` body attribute of ``request``

methods

- ``redirect(url)`` create HTTPFound object from url
- ``redirect_route(route_name, **values)`` create HTTPFound object with route_url
- ``action_dispatch`` call method named ``*_action`` with request param.


Softification
-------------------------

``Softification`` is context manager to replace Exceptions to the other Exceptions.

::

   with Softification(NoResultFound, HTTPNotFound):
       item = DBSession.query(Item).filter(Item.id==id).one()

If ``one()`` method raises ``NoResultFound`` exception, the context manager catch that 
and raises the HTTPNotFound exception.
You can use tuple for target Exception classes.


USAGE
--------------

BasicView
++++++++++++++++++

To use ``BasicView``, inherit that simply.::

    class Greeting(BasicView):
        def __call__(self):
            return self.redirect_route('top', v=1)
