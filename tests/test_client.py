import unittest
from twilio.rest import TwilioRestClient
from twilio.rest import resources


class RestClientTest(unittest.TestCase):

    def setUp(self):
        self.client = TwilioRestClient("ACCOUNT_SID", "AUTH_TOKEN")

    def test_connect_apps(self):
        self.assertIsInstance(self.client.connect_apps, 
            resources.ConnectApps)

    def test_authorized_apps(self):
        self.assertIsInstance(self.client.authorized_connect_apps, 
            resources.AuthorizedConnectApps)
