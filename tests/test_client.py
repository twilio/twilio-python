import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest
from twilio.rest import TwilioRestClient
from twilio.rest import resources
from mock import patch, Mock

class RestClientTest(unittest.TestCase):

    def setUp(self):
        self.client = TwilioRestClient("ACCOUNT_SID", "AUTH_TOKEN")


    @patch("twilio.rest.make_request")
    def test_request(self, mock):
        self.client.request("2010-04-01", method="GET")
        mock.assert_called_with("GET", "https://api.twilio.com/2010-04-01",
            headers={"User-Agent": 'twilio-python'}, params={},
            auth=("ACCOUNT_SID", "AUTH_TOKEN"), data=None)

    def test_connect_apps(self):
        self.assertIsInstance(self.client.connect_apps, 
            resources.ConnectApps)

    def test_authorized_apps(self):
        self.assertIsInstance(self.client.authorized_connect_apps, 
            resources.AuthorizedConnectApps)

    @patch("twilio.rest.resources.make_request")
    def test_conferences(self, mock):
        mock.return_value = Mock()
        mock.return_value.ok = True
        mock.return_value.content = '{"conferences": []}'
        self.client.conferences.list()
