from pyramid.httpexceptions import HTTPFound, HTTPBadRequest
from six import reraise

class Softification(object):
    def __init__(self, targets, replacer):
        self.targets = targets
        self.replacer = replacer

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is None:
            return

        if isinstance(exc_val, self.targets):
            raise self.replacer()

        reraise(exc_type, exc_val, exc_tb)


class BaseView(object):
    def __init__(self, context, request):
        self.context = context
        self.request = request


class ViewSupport(object):
    @property
    def response(self):
        return self.request.response

    def redirect(self, url):
        return HTTPFound(location=url)

    def redirect_route(self, route_name, **values):
        return self.redirect(self.request.route_url(route_name, **values))

    def redirect_resource(self, model, *values, **kw):
        return self.redirect(self.request.resource_url(model, *values, **kw))

    @property
    def body(self):
        return self.request.body

    def action_dispatch(self, default):
        action = self.request.params.get('action', default)
        mname = action + '_action'
        if not hasattr(self, mname):
            return HTTPBadRequest()
        return getattr(self, mname)()


class BasicView(BaseView, ViewSupport):
    pass

class ActionView(BasicView):
    def __call__(self):
        return self.action_dispatch()
