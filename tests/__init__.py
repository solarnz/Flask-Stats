# -*- coding: utf-8 -*-

import unittest
import time

from flask import Flask
from flask.ext.stats import Stats
from mock import Mock


class TestStats(unittest.TestCase):
    def _create_app(self, name):
        app = Flask(name)

        @app.route('/')
        def index():
            time.sleep(0.03)
            return ''

        @app.route('/other')
        def other():
            time.sleep(0.08)
            return ''

        return app

    def test_setup(self):
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

    def test_setup_single_application(self):
        app = self._create_app('hello')
        stats = Stats(app).client

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

    def _setup_mocks(self, stats_extension):
        pipeline_mock = Mock()
        pipeline_contextmanager_mock = Mock()
        pipeline_contextmanager_mock.__enter__ = Mock(
            return_value=pipeline_mock
        )
        pipeline_contextmanager_mock.__exit__ = Mock(return_value=False)

        stats_extension.pipeline = Mock()
        stats_extension.pipeline.return_value = pipeline_contextmanager_mock

        return pipeline_mock


class TimingValue(object):
    def __init__(self, expected_value, acceptable_variance):
        self.expected_value = expected_value
        self.acceptable_variance = acceptable_variance

    def __eq__(self, other):
        return (
            self.expected_value - self.acceptable_variance < other and
            self.expected_value + self.acceptable_variance > other
        )

    def __ne__(self, other):
        return not self.__eq__(other)
