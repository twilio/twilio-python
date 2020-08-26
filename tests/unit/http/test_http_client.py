# -*- coding: utf-8 -*-
import unittest

from mock import patch, Mock
from requests import Session

from twilio.base.version import Version
from twilio.base.exceptions import TwilioRestException
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

    def test_request_with_timeout(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}

        response = self.client.request(
            'doesnt matter', 'doesnt matter', None, None, None, None, 30, None)

        self.assertEqual('other.twilio.com', self.request_mock.headers['Host'])
        self.assertEqual(200, response.status_code)
        self.assertEqual('testing-unicode: Ω≈ç√, 💩', response.content)

    def test_request_where_method_timeout_equals_zero(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}

        try:
            self.client.request(
                'doesnt matter', 'doesnt matter', None, None, None, None, 0, None)
        except Exception as e:
            self.assertEqual(ValueError, type(e))

    def test_request_where_class_timeout_manually_set(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}
        self.client.timeout = 30

        response = self.client.request(
            'doesnt matter', 'doesnt matter')
        self.assertEqual('other.twilio.com', self.request_mock.headers['Host'])
        self.assertEqual(200, response.status_code)
        self.assertEqual('testing-unicode: Ω≈ç√, 💩', response.content)

    def test_request_where_class_timeout_equals_zero(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}
        self.client.timeout = 0

        try:
            self.client.request(
                'doesnt matter', 'doesnt matter')
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_request_where_class_timeout_and_method_timeout_set(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}
        self.client.timeout = 30

        response = self.client.request(
            'doesnt matter', 'doesnt matter', None, None, None, None, 15, None)

        self.assertEqual('other.twilio.com', self.request_mock.headers['Host'])
        self.assertEqual(200, response.status_code)
        self.assertEqual('testing-unicode: Ω≈ç√, 💩', response.content)

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

    def test_request_behind_proxy(self):
        proxies = {
            'http': 'http://proxy.twilio.com',
            'https': 'https://proxy.twilio.com',
        }
        self.client = TwilioHttpClient(proxy=proxies)
        self.client.request('doesnt matter', 'doesnt matter')
        self.assertEqual(proxies, self.session_mock.proxies)

    def test_exception_with_details(self):
        v1 = MyVersion(self.client)
        error_text = """{   
            "code": 20001,
            "message": "Bad request",
            "more_info": "https://www.twilio.com/docs/errors/20001",
            "status": 400,
            "details": {
                "foo":"bar"
            }
        }"""
        self.session_mock.send.return_value = Response(400, error_text)
        try:
            v1.fetch("get", "none", None, None, None, None, None)
            self.fail('should not happen')
        except TwilioRestException as err:
            self.assertEqual(400, err.status)
            self.assertEqual(20001, err.code)
            self.assertEqual("get", err.method)
            self.assertEqual("Unable to fetch record: Bad request", err.msg)
            self.assertEqual({"foo": "bar"}, err.details)


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


class MyVersion(Version):
    def __init__(self, domain):
        super(MyVersion, self).__init__(domain)
        self.version = 'v1'
        self._credentials = None
