import six
if six.PY3:
    import unittest
else:
    import unittest2 as unittest

from twilio.rest import TwilioRestClient, resources
from mock import patch, Mock
from tools import create_mock_json

AUTH = ("ACCOUNT_SID", "AUTH_TOKEN")


class RestClientTest(unittest.TestCase):

    def setUp(self):
        self.client = TwilioRestClient("ACCOUNT_SID", "AUTH_TOKEN")

    @patch("twilio.rest.make_request")
    def test_request(self, mock):
        self.client.request("2010-04-01", method="GET")
        mock.assert_called_with("GET", "https://api.twilio.com/2010-04-01",
                                headers={"User-Agent": 'twilio-python',
                                         'Accept-Charset': 'utf-8'},
                                params={}, auth=AUTH, data=None)

    def test_connect_apps(self):
        self.assertIsInstance(self.client.connect_apps,
            resources.ConnectApps)

    def test_authorized_apps(self):
        self.assertIsInstance(self.client.authorized_connect_apps,
            resources.AuthorizedConnectApps)

    @patch("twilio.rest.resources.base.make_request")
    def test_conferences(self, mock):
        mock.return_value = Mock()
        mock.return_value.ok = True
        mock.return_value.content = '{"conferences": []}'
        self.client.conferences.list()

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_members(self, mock):
        resp = create_mock_json("tests/resources/members_list.json")
        mock.return_value = resp
        self.client.members("QU123").list()
        uri = "https://api.twilio.com/2010-04-01/Accounts/ACCOUNT_SID/Queues/QU123/Members"
        mock.assert_called_with("GET", uri, params={}, auth=AUTH)
