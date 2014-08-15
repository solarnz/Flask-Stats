from flask.ext.stats import Stats

from . import TestStats, TimingValue


class TestAppRoutes(TestStats):
    def test_timer(self):
        app = self._create_app('hello')
        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/')

        self.assertTrue(pipeline.incr.called)
        pipeline.incr.assert_called_once_with(
            'index.http_200'
        )
        pipeline.timing.assert_called_once_with(
            'index', TimingValue(0.03 * 1000, 10)
        )


class TestBlueprintRoutes(TestStats):
    def test_timer(self):
        app = self._create_app('hello')
        stats = Stats().init_app(app)

        pipeline = self._setup_mocks(stats)
        client = app.test_client()
        client.get('/')

        self.assertTrue(pipeline.incr.called)
        pipeline.incr.assert_called_once_with(
            'index.http_200'
        )
        pipeline.timing.assert_called_once_with(
            'index', TimingValue(0.03 * 1000, 10)
        )
