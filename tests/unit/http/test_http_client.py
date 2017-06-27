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

    def test_request_with_unicode_response(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}

        response = self.client.request('doesnt matter', 'doesnt matter')

        self.assertEqual('other.twilio.com', self.request_mock.headers['Host'])
        self.assertEqual(200, response.status_code)
        self.assertEqual('testing-unicode: Ω≈ç√, 💩', response.content)
