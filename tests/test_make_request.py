"""
Test that make+request is making correct HTTP requests

Uses the awesome httpbin.org to validate responses
"""

import json
from nose.tools import assert_equals
from nose.tools import raises
from mock import patch
from mock import Mock
from twilio import TwilioRestException
from twilio.rest.resources import make_request
from twilio.rest.resources import make_twilio_request

get_headers = {
    "User-Agent": "twilio-python",
    "Accept": "application/json",
    }

post_headers = get_headers.copy()
post_headers["Content-Type"] = "application/x-www-form-urlencoded"

def test_get_params():
    tests = [
        ("http://httpbin.org/get", {"hey":"you", "foo":"bar"}),
        ("http://httpbin.org/get?hey=you", {"foo":"bar"}),
        ("http://httpbin.org/get?hey=you&foo=bar", {}),
        ]

    for test in tests:
        yield check_get_params, test[0], test[1]

def check_get_params(url, params):
    resp = make_request("GET", url, params=params)
    body = json.loads(resp.content)

    assert_equals(body["args"]["hey"], "you")
    assert_equals(body["args"]["foo"], "bar")

def test_resp_uri():
    resp = make_request("GET", "http://httpbin.org/get")
    assert_equals(resp.url, "http://httpbin.org/get")

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
