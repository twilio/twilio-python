"""
Test that make+request is making correct HTTP requests

Uses the awesome httpbin.org to validate responses
"""
import platform
import unittest

import twilio
from nose.tools import assert_equal, raises
from mock import patch, Mock, ANY
from twilio.rest.exceptions import TwilioRestException
from twilio.rest.http import HttpClient
from twilio.rest.resources.base import make_twilio_request
from twilio.rest.resources.connection import Connection
from twilio.rest.resources.connection import PROXY_TYPE_SOCKS5

get_headers = {
    "User-Agent": "twilio-python/{version} (Python {python_version})".format(
        version=twilio.__version__,
        python_version=platform.python_version(),
    ),
    "Accept-Charset": "utf-8",
    "Accept": "application/json",
}

post_headers = get_headers.copy()
post_headers["Content-Type"] = "application/x-www-form-urlencoded"


class HttpClientTest(unittest.TestCase):

    def setUp(self):
        self.client = HttpClient()

    @patch('twilio.rest.http.Response')
    @patch('httplib2.Http')
    def test_get_params(self, http_mock, response_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'
        http_mock.return_value = http
        self.client.make_request("GET", "http://httpbin.org/get", params={"hey": "you"})
        http.request.assert_called_with("http://httpbin.org/get?hey=you", "GET",
                                        body=None, headers=None)

    @patch('twilio.rest.http.Response')
    @patch('httplib2.Http')
    def test_get_extra_params(self, http_mock, response_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'
        http_mock.return_value = http
        self.client.make_request("GET", "http://httpbin.org/get?foo=bar", params={"hey": "you"})
        http.request.assert_called_with("http://httpbin.org/get?foo=bar&hey=you", "GET",
                                        body=None, headers=None)

    @patch('twilio.rest.http.Response')
    @patch('httplib2.Http')
    def test_resp_uri(self, http_mock, response_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'
        http_mock.return_value = http
        self.client.make_request("GET", "http://httpbin.org/get")
        http.request.assert_called_with("http://httpbin.org/get", "GET",
                                        body=None, headers=None)


    @patch('twilio.rest.http.Response')
    @patch('httplib2.Http')
    def test_sequence_data(self, http_mock, response_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'
        http_mock.return_value = http
        self.client.make_request(
            "POST",
            "http://httpbin.org/post",
            data={"a_list": ["here", "is", "some", "stuff"]},
        )
        http.request.assert_called_with(
            "http://httpbin.org/post",
            "POST",
            body="a_list=here&a_list=is&a_list=some&a_list=stuff",
            headers=None,
        )

    def test_make_twilio_request_headers(self):
        self.client.make_request = Mock()
        mock = self.client.make_request

        url = "http://random/url"
        make_twilio_request("POST", url, use_json_extension=True,
                            client=self.client)

        mock.assert_called_with("POST", "http://random/url.json",
                                headers=post_headers)

    @raises(TwilioRestException)
    def test_make_twilio_request_bad_data(self):
        self.client.make_request = Mock()
        mock = self.client.make_request

        resp = Mock()
        resp.ok = False
        resp.return_value = "error"
        mock.return_value = resp

        url = "http://random/url"
        make_twilio_request("POST", url, client=self.client)
        mock.assert_called_with("POST", "http://random/url.json",
                                headers=post_headers)

    @patch('twilio.rest.http.Response')
    @patch('httplib2.Http')
    def test_proxy_info(self, http_mock, resp_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'
        http_mock.return_value = http
        Connection.set_proxy_info(
            'example.com',
            8080,
            proxy_type=PROXY_TYPE_SOCKS5,
        )
        self.client.make_request("GET", "http://httpbin.org/get")
        http_mock.assert_called_with(timeout=None, ca_certs=ANY, proxy_info=ANY)
        http.request.assert_called_with("http://httpbin.org/get", "GET",
                                        body=None, headers=None)
        proxy_info = http_mock.call_args[1]['proxy_info']
        assert_equal(proxy_info.proxy_host, 'example.com')
        assert_equal(proxy_info.proxy_port, 8080)
        assert_equal(proxy_info.proxy_type, PROXY_TYPE_SOCKS5)
