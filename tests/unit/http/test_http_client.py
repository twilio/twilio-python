# -*- coding: utf-8 -*-

import six

import unittest

import mock
from mock import patch, Mock
from requests import Request
from requests import Session

from twilio.http.http_client import TwilioHttpClient
from twilio.http.response import Response


class TestHttpClientRequest(unittest.TestCase):
    def setUp(self):
        self.session_patcher = patch('twilio.http.http_client.Session')

        self.session_mock = Mock(wraps=Session())
        self.request_mock = Mock()

        self.session_mock.prepare_request.return_value = self.request_mock
        self.session_mock.send.return_value = Response(200, 'testing-unicode: Ω≈ç√, 💩')
        self.request_mock.headers = {}

        session_constructor_mock = self.session_patcher.start()
        session_constructor_mock.return_value = self.session_mock

        self.client = TwilioHttpClient()

    def tearDown(self):
        self.session_patcher.stop()

    def test_request_sets_host_header_if_missing(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}

        self.client.request('doesnt matter', 'doesnt matter')

        self.assertEqual('other.twilio.com', self.request_mock.headers['Host'])
        self.assertIsNotNone(self.client.last_request)
        self.assertIsNotNone(self.client.last_response)

    def test_request_with_unicode_response(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}

        response = self.client.request('doesnt matter', 'doesnt matter')

        self.assertEqual('other.twilio.com', self.request_mock.headers['Host'])
        self.assertEqual(200, response.status_code)
        self.assertEqual('testing-unicode: Ω≈ç√, 💩', response.content)

    def test_last_request_last_response_exist(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}

        self.client.request('doesnt-matter-method',
                            'doesnt-matter-url',
                            {'params-value': 'params-key'},
                            {'data-value': 'data-key'},
                            {'headers-value': 'headers-key'},
                            ['a', 'b'])

        self.assertIsNotNone(self.client.last_request)
        self.assertEqual('doesnt-matter-url', self.client.last_request.url)
        self.assertEqual('DOESNT-MATTER-METHOD', self.client.last_request.method)
        self.assertEqual({'params-value': 'params-key'}, self.client.last_request.params)
        self.assertEqual({'data-value': 'data-key'}, self.client.last_request.data)
        self.assertEqual({'headers-value': 'headers-key'}, self.client.last_request.headers)
        self.assertEqual(['a', 'b'], self.client.last_request.auth)

        self.assertIsNotNone(self.client.last_response)
        self.assertEqual(200, self.client.last_response.status_code)
        self.assertEqual('testing-unicode: Ω≈ç√, 💩', self.client.last_response.text)

    def test_last_response_empty_on_error(self):
        self.session_mock.send.side_effect = Exception('voltron')

        with self.assertRaises(Exception):
            self.client.request('doesnt-matter', 'doesnt-matter')

            self.assertIsNotNone(self.client.last_request)
            self.assertIsNone(self.client.last_response)


class TestHttpClientSession(unittest.TestCase):

    def setUp(self):
        self.session_patcher = patch('twilio.http.http_client.Session')
        self.session_constructor_mock = self.session_patcher.start()

    def tearDown(self):
        self.session_patcher.stop()

    def _setup_session_response(self, value):
        session_mock = Mock(wraps=Session())
        request_mock = Mock()

        session_mock.prepare_request.return_value = request_mock
        session_mock.send.return_value = Response(200, value)
        self.session_constructor_mock.return_value = session_mock

    def test_session_preserved(self):
        self._setup_session_response('response_1')

        client = TwilioHttpClient()
        response_1 = client.request('GET', 'https://api.twilio.com')

        self._setup_session_response('response_2')
        response_2 = client.request('GET', 'https://api.twilio.com')

        # Used same session, response should be the same
        self.assertEqual(response_1.content, 'response_1')
        self.assertEqual(response_2.content, 'response_1')

    def test_session_not_preserved(self):
        self._setup_session_response('response_1')

        client = TwilioHttpClient(pool_connections=False)
        response_1 = client.request('GET', 'https://api.twilio.com')

        self._setup_session_response('response_2')
        response_2 = client.request('GET', 'https://api.twilio.com')

        # Used different session, responses should be different
        self.assertEqual(response_1.content, 'response_1')
        self.assertEqual(response_2.content, 'response_2')
