import pytest
from pyramid import testing

class TestBaseView(object):
    @pytest.fixture
    def target(self):
        from rebecca.view import BaseView
        return BaseView

    def test_it(self, target):
        request = testing.DummyRequest()
        context = testing.DummyResource()
        result = target(context, request)

        assert result.context == context
        assert result.request == request

class TestViewSupport(object):
    @pytest.fixture
    def target(self):
        from rebecca.view import ViewSupport
        return ViewSupport

    @pytest.fixture
    def config(self, request):
        config = testing.setUp()
        def fin():
            testing.tearDown()
        request.addfinalizer(fin)
        return config

    def test_response(self, target):
        request = testing.DummyRequest()
        view_support = target()
        view_support.request = request

        assert view_support.response == request.response

    def test_redirect(self, target):
        view_support = target()
        result = view_support.redirect('http://testing.example.com')

        assert result.location == 'http://testing.example.com'

    def test_redirect_route(self, target, config):
        config.add_route('testing', 'testing/{value1}/{value2}')
        request = testing.DummyRequest()
        view_support = target()
        view_support.request = request
        result = view_support.redirect_route('testing',
                                             value1=100,
                                             value2='test')
        
        assert result.location == 'http://example.com/testing/100/test'


    def test_body(self, target):
        request = testing.DummyRequest(body='this is body')
        view_support = target()
        view_support.request = request

        assert view_support.body == 'this is body'


    def test_action_dispatch(self, target):
        request = testing.DummyRequest(
            params=dict(action='test'),
            )
        view_support = target()
        view_support.request = request
        view_support.test_action = lambda: 'OK'

        result = view_support.action_dispatch('default')
        assert result == 'OK'

    def test_action_dispatch_default(self, target):
        request = testing.DummyRequest(
            )
        view_support = target()
        view_support.request = request
        view_support.default_action = lambda: 'OK'

        result = view_support.action_dispatch('default')
        assert result == 'OK'

    def test_action_dispatch_invalid(self, target):
        request = testing.DummyRequest(
            )
        view_support = target()
        view_support.request = request

        result = view_support.action_dispatch('default')
        assert result.status_int == 400
