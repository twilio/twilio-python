# -*- coding: utf-8 -*-
from mock import patch, Mock
from twilio.rest import resources

@patch("httplib2.Http")
@patch("twilio.rest.resources.Response")
def test_paging(resp_mock, mock):
    http = mock.return_value
    http.request.return_value = (Mock(), Mock())

    data = {
        "body": u"Chloéñ",
        }
    
    resources.make_request("GET", "http://www.example.com", data=data)

    http.request.assert_called_with("http://www.example.com", "GET", 
            headers=None, body="body=Chlo%C3%A9%C3%B1")



