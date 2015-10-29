"""
Test that make+request is making correct HTTP requests

Uses the awesome httpbin.org to validate responses
"""
import base64
import platform
import unittest

from httplib2 import Response
from nose.tools import assert_equal, raises
from mock import patch, Mock, ANY

import twilio
from twilio.rest.exceptions import TwilioRestException
from twilio.rest.resources.base import make_request, make_twilio_request
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


class MakeRequestTest(unittest.TestCase):

    @patch('twilio.rest.resources.base.Response')
    @patch('httplib2.Http')
    def test_get_params(self, http_mock, response_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http_mock.return_value = http
        make_request("GET", "http://httpbin.org/get", params={"hey": "you"})
        http.request.assert_called_with("http://httpbin.org/get?hey=you", "GET",
                                        body=None, headers=None)

    @patch('twilio.rest.resources.base.Response')
    @patch('httplib2.Http')
    def test_get_extra_params(self, http_mock, response_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http_mock.return_value = http
        make_request("GET", "http://httpbin.org/get?foo=bar", params={"hey": "you"})
        http.request.assert_called_with("http://httpbin.org/get?foo=bar&hey=you", "GET",
                                        body=None, headers=None)

    @patch('twilio.rest.resources.base.Response')
    @patch('httplib2.Http')
    def test_resp_uri(self, http_mock, response_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http_mock.return_value = http
        make_request("GET", "http://httpbin.org/get")
        http.request.assert_called_with("http://httpbin.org/get", "GET",
                                        body=None, headers=None)

    @patch('twilio.rest.resources.base.Response')
    @patch('httplib2.Http')
    def test_sequence_data(self, http_mock, response_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http_mock.return_value = http
        make_request(
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

    @patch('twilio.rest.resources.base.Response')
    @patch('httplib2.Http._conn_request')
    def test_make_request_basic_auth(self, mock_request, mock_response):
        response = Response({
            'status': '401',
            'WWW-Authenticate': 'Basic realm="Twilio API"'
        })
        mock_request.side_effect = [(response, Mock()), (Mock(), Mock())]
        make_request('GET', 'http://httpbin.org/get', auth=('AC123', 'AuthToken'))

        auth = "{0}:{1}".format('AC123', 'AuthToken')
        encoded_auth = auth.encode('utf-8')
        b64_auth = base64.b64encode(encoded_auth)

        mock_request.assert_called_with(
            ANY,
            '/get',
            'GET',
            None,
            {
                'accept-encoding': 'gzip, deflate',
                'authorization': 'Basic {0}'.format(b64_auth.decode('utf-8')),
                'user-agent': ANY,
            }
        )

    @patch('twilio.rest.resources.base.make_request')
    def test_make_twilio_request_headers(self, mock):
        url = "http://random/url"
        make_twilio_request("POST", url, use_json_extension=True)
        mock.assert_called_with("POST", "http://random/url.json",
                                headers=post_headers)

    @raises(TwilioRestException)
    @patch('twilio.rest.resources.base.make_request')
    def test_make_twilio_request_bad_data(self, mock):
        resp = Mock()
        resp.ok = False
        resp.return_value = "error"
        mock.return_value = resp

        url = "http://random/url"
        make_twilio_request("POST", url)
        mock.assert_called_with("POST", "http://random/url.json",
                                headers=post_headers)

    @patch('twilio.rest.resources.base.Response')
    @patch('httplib2.Http')
    def test_proxy_info(self, http_mock, resp_mock):
        http = Mock()
        http.request.return_value = (Mock(), Mock())
        http_mock.return_value = http
        Connection.set_proxy_info(
            'example.com',
            8080,
            proxy_type=PROXY_TYPE_SOCKS5,
        )
        make_request("GET", "http://httpbin.org/get")
        http_mock.assert_called_with(timeout=None, ca_certs=ANY, proxy_info=ANY)
        http.request.assert_called_with("http://httpbin.org/get", "GET",
                                        body=None, headers=None)
        proxy_info = http_mock.call_args[1]['proxy_info']
        assert_equal(proxy_info.proxy_host, 'example.com')
        assert_equal(proxy_info.proxy_port, 8080)
        assert_equal(proxy_info.proxy_type, PROXY_TYPE_SOCKS5)
