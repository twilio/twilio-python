"""
Test that make+request is making correct HTTP requests

Uses the awesome httpbin.org to validate responses
"""
import json
import twilio
from nose.tools import assert_equals
from nose.tools import raises
from mock import patch
from mock import Mock
from twilio import TwilioRestException
from twilio.rest.resources import make_request
from twilio.rest.resources import make_twilio_request

get_headers = {
    "User-Agent": "twilio-python/{}".format(twilio.__version__),
    "Accept": "application/json",
    }

post_headers = get_headers.copy()
post_headers["Content-Type"] = "application/x-www-form-urlencoded"


@patch('twilio.rest.resources.Response')
@patch('httplib2.Http')
def test_get_params(http_mock, response_mock):
    http = Mock()
    http.request.return_value = (Mock(), Mock())
    http_mock.return_value = http
    make_request("GET", "http://httpbin.org/get", params={"hey": "you"})
    http.request.assert_called_with("http://httpbin.org/get?hey=you", "GET",
            body=None, headers=None)


@patch('twilio.rest.resources.Response')
@patch('httplib2.Http')
def test_get_extra_paranms(http_mock, response_mock):
    http = Mock()
    http.request.return_value = (Mock(), Mock())
    http_mock.return_value = http
    make_request("GET", "http://httpbin.org/get?foo=bar", params={"hey": "you"})
    http.request.assert_called_with("http://httpbin.org/get?foo=bar&hey=you", "GET",
            body=None, headers=None)


@patch('twilio.rest.resources.Response')
@patch('httplib2.Http')
def test_resp_uri(http_mock, response_mock):
    http = Mock()
    http.request.return_value = (Mock(), Mock())
    http_mock.return_value = http
    make_request("GET", "http://httpbin.org/get")
    http.request.assert_called_with("http://httpbin.org/get", "GET",
            body=None, headers=None)


@patch('twilio.rest.resources.make_request')
def test_make_twilio_request_headers(mock):
    url = "http://random/url"
    make_twilio_request("POST", url)
    mock.assert_called_with("POST", "http://random/url.json",
                            headers=post_headers)

@raises(TwilioRestException)
@patch('twilio.rest.resources.make_request')
def test_make_twilio_request_bad_data(mock):
    resp = Mock()
    resp.ok = False
    mock.return_value = resp

    url = "http://random/url"
    make_twilio_request("POST", url)
    mock.assert_called_with("POST", "http://random/url.json",
                            headers=post_headers)
