# -*- coding: utf-8 -*-
import unittest
from mock import patch, Mock
from six import u
from twilio.rest.http import HttpClient


class HttpClientUnicodeTest(unittest.TestCase):

    @patch("httplib2.Http")
    @patch("twilio.rest.http.Response")
    def test_ascii_encode(self, resp_mock, mock):
        http = mock.return_value
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'

        data = {
            "body": "HeyHey".encode('utf-8')
        }

        HttpClient().make_request("GET", "http://www.example.com", data=data)

        http.request.assert_called_with("http://www.example.com", "GET",
                                        headers=None, body="body=HeyHey")


    @patch("httplib2.Http")
    @patch("twilio.rest.http.Response")
    def test_ascii(self, resp_mock, mock):
        http = mock.return_value
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'

        data = {
            "body": "HeyHey"
        }

        HttpClient().make_request("GET", "http://www.example.com", data=data)

        http.request.assert_called_with("http://www.example.com", "GET",
                                        headers=None, body="body=HeyHey")


    @patch("httplib2.Http")
    @patch("twilio.rest.http.Response")
    def test_double_encoding(self, resp_mock, mock):
        http = mock.return_value
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'

        body = u('Chlo\xe9\xf1')

        data = {
            "body": body.encode('utf-8'),
        }

        HttpClient().make_request("GET", "http://www.example.com", data=data)

        http.request.assert_called_with("http://www.example.com", "GET",
                                        headers=None, body="body=Chlo%C3%A9%C3%B1")


    @patch("httplib2.Http")
    @patch("twilio.rest.http.Response")
    def test_paging(self, resp_mock, mock):
        http = mock.return_value
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'

        data = {
            "body": u('Chlo\xe9\xf1'),
        }

        HttpClient().make_request("GET", "http://www.example.com", data=data)

        http.request.assert_called_with("http://www.example.com", "GET",
                                        headers=None, body="body=Chlo%C3%A9%C3%B1")


    @patch("httplib2.Http")
    @patch("twilio.rest.http.Response")
    def test_unicode_sequence_form_value(self, resp_mock, mock):
        http = mock.return_value
        http.request.return_value = (Mock(), Mock())
        http.request.return_value[0].status = '200'

        data = {
            "body": [u('\xe5'), u('\xe7')],
        }

        HttpClient().make_request("POST", "http://www.example.com", data=data)

        http.request.assert_called_with(
            "http://www.example.com",
            "POST",
            headers=None,
            body="body=%C3%A5&body=%C3%A7",
        )
