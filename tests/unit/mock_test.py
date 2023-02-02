import unittest
import requests
from unittest import mock
from unittest.mock import MagicMock
from twilio.rest import Client
from twilio.http.response import Response


# I think I need to mock TwilioHttpClient (or maybe its parent, HttpClient) under http.httpClient
class TestAccount(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_account(self):
        response = Response(status_code=200, text="Some text")
        self.client = Client('username', 'password')
        self.client.request = MagicMock(return_value=response)
        self.client.api.v2010.accounts.create("SomeName")
        self.client.request.assert_called_with("POST", "/Accounts.json", params=None, data={"FriendlyName": "SomeName"}, headers=None, auth=None, timeout=None, allow_redirects=False)

    @mock.patch('twilio.rest.Client')
    def test2(self):
        pass


if __name__ == "__main__":
    unittest.main()
