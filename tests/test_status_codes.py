from flask.ext.stats import Stats

from . import TestStats


class TestAppRoutes(TestStats):
    def test_200(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/')

        pipeline.incr.assert_called_once_with(
            'index.http_200'
        )

    def test_302(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/redirect')

        pipeline.incr.assert_called_once_with(
            'redir.http_302'
        )

    def test_401(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/fail')

        pipeline.incr.assert_called_once_with(
            'fail.http_401'
        )


class TestAppNonExistentRoute(TestStats):
    def test_404(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/hello')

        pipeline.incr.assert_called_once_with(
            'None.http_404'
        )

    def test_301_to_route_with_slash(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/slash')

        pipeline.incr.assert_called_once_with(
            'None.http_301'
        )


class TestBlueprintRoutes(TestStats):
    def test_200(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/blue/')

        pipeline.incr.assert_called_once_with(
            'balls.blueprint_index.http_200'
        )

    def test_302(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/blue/redirect')

        pipeline.incr.assert_called_once_with(
            'balls.blueprint_redir.http_302'
        )

    def test_401(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/blue/fail')

        pipeline.incr.assert_called_once_with(
            'balls.blueprint_fail.http_401'
        )


class TestBlueprintNonExistentRoute(TestStats):
    def test_404(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/blue/hello')

        pipeline.incr.assert_called_once_with(
            'None.http_404'
        )

    def test_301_to_route_with_slash(self):
        app = self._create_app('hello')

        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/blue/slash')

        pipeline.incr.assert_called_once_with(
            'None.http_301'
        )
