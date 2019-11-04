# -*- coding: utf-8 -*-

import unittest

from mock import patch, Mock
from requests import Request
from requests import Session

from twilio.base.exceptions import TwilioRestException
from twilio.http.validation_client import ValidationClient
from twilio.http.response import Response


class TestValidationClientHelpers(unittest.TestCase):
    def setUp(self):
        self.request = Request(
            'GET',
            'https://api.twilio.com/2010-04-01/Accounts/AC123/Messages',
            auth=('Username', 'Password'),
        )
        self.request = self.request.prepare()
        self.client = ValidationClient('AC123', 'SK123', 'CR123', 'private_key')

    def test_build_validation_payload_basic(self):
        validation_payload = self.client._build_validation_payload(self.request)
        self.assertEqual('GET', validation_payload.method)
        self.assertEqual('/2010-04-01/Accounts/AC123/Messages', validation_payload.path)
        self.assertEqual('', validation_payload.query_string)
        self.assertEqual(['authorization', 'host'], validation_payload.signed_headers)
        self.assertEqual('', validation_payload.body)

    def test_build_validation_payload_query_string_parsed(self):
        self.request.url = self.request.url + '?QueryParam=1&Other=true'

        validation_payload = self.client._build_validation_payload(self.request)

        self.assertEqual('GET', validation_payload.method)
        self.assertEqual('/2010-04-01/Accounts/AC123/Messages', validation_payload.path)
        self.assertEqual('QueryParam=1&Other=true', validation_payload.query_string)
        self.assertEqual(['authorization', 'host'], validation_payload.signed_headers)
        self.assertEqual('', validation_payload.body)

    def test_build_validation_payload_body_parsed(self):
        self.request.body = 'foobar'

        validation_payload = self.client._build_validation_payload(self.request)

        self.assertEqual('GET', validation_payload.method)
        self.assertEqual('/2010-04-01/Accounts/AC123/Messages', validation_payload.path)
        self.assertEqual('', validation_payload.query_string)
        self.assertEqual(['authorization', 'host'], validation_payload.signed_headers)
        self.assertEqual('foobar', validation_payload.body)

    def test_build_validation_payload_complex(self):
        self.request.body = 'foobar'
        self.request.url = self.request.url + '?QueryParam=Value&OtherQueryParam=OtherValue'

        validation_payload = self.client._build_validation_payload(self.request)

        self.assertEqual('GET', validation_payload.method)
        self.assertEqual('/2010-04-01/Accounts/AC123/Messages', validation_payload.path)
        self.assertEqual(['authorization', 'host'], validation_payload.signed_headers)
        self.assertEqual('foobar', validation_payload.body)
        self.assertEqual('QueryParam=Value&OtherQueryParam=OtherValue',
                         validation_payload.query_string)

    def test_get_host(self):
        self.assertEqual('api.twilio.com', self.client._get_host(self.request))


class TestValidationClientRequest(unittest.TestCase):

    def setUp(self):
        self.session_patcher = patch('twilio.http.validation_client.Session')
        self.jwt_patcher = patch('twilio.http.validation_client.ClientValidationJwt')

        self.session_mock = Mock(wraps=Session())
        self.validation_token = self.jwt_patcher.start()
        self.request_mock = Mock()

        self.session_mock.prepare_request.return_value = self.request_mock
        self.session_mock.send.return_value = Response(200, 'test, omega: Ω, pile of poop: 💩')
        self.validation_token.return_value.to_jwt.return_value = 'test-token'
        self.request_mock.headers = {}

        session_constructor_mock = self.session_patcher.start()
        session_constructor_mock.return_value = self.session_mock

        self.client = ValidationClient('AC123', 'SK123', 'CR123', 'private_key')

    def tearDown(self):
        self.session_patcher.stop()
        self.jwt_patcher.stop()

    def test_request_does_not_overwrite_host_header(self):
        self.request_mock.url = 'https://api.twilio.com/'

        self.client.request('doesnt matter', 'doesnt matter')

        self.assertEqual('api.twilio.com', self.request_mock.headers['Host'])
        self.assertEqual('test-token', self.request_mock.headers['Twilio-Client-Validation'])

    def test_request_sets_host_header_if_missing(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}

        self.client.request('doesnt matter', 'doesnt matter')

        self.assertEqual('other.twilio.com', self.request_mock.headers['Host'])
        self.assertEqual('test-token', self.request_mock.headers['Twilio-Client-Validation'])

    def test_request_with_unicode_response(self):
        self.request_mock.url = 'https://api.twilio.com/'
        self.request_mock.headers = {'Host': 'other.twilio.com'}

        response = self.client.request('doesnt matter', 'doesnt matter')

        self.assertEqual('other.twilio.com', self.request_mock.headers['Host'])
        self.assertEqual('test-token', self.request_mock.headers['Twilio-Client-Validation'])
        self.assertEqual(200, response.status_code)
        self.assertEqual('test, omega: Ω, pile of poop: 💩', response.content)

    @patch('twilio.http.validation_client')
    def test_validate_ssl_certificate_success(self, http_client):
        http_client.request.return_value = Response(200, 'success')
        self.client.validate_ssl_certificate(http_client)

    @patch('twilio.http.validation_client')
    def test_validate_ssl_certificate_error(self, http_client):
        http_client.request.return_value = Response(504, 'error')

        with self.assertRaises(TwilioRestException):
            self.client.validate_ssl_certificate(http_client)
