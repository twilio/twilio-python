import unittest

from mock import patch, Mock, sentinel, ANY
from nose.tools import assert_equal, assert_true

from twilio.rest.resources.imports import json
from twilio.rest import TwilioRestClient, resources, TwilioTaskRouterClient
from tests.tools import create_mock_json

AUTH = ("ACCOUNT_SID", "AUTH_TOKEN")


class RestClientTest(unittest.TestCase):
    def setUp(self):
        self.client = TwilioRestClient("ACCOUNT_SID", "AUTH_TOKEN")
        self.task_router_client = TwilioTaskRouterClient("ACCOUNT_SID",
                                                         "AUTH_TOKEN")

    @patch("twilio.rest.base.make_request")
    def test_request(self, mock):
        self.client.request("2010-04-01", method="GET")
        mock.assert_called_with("GET", "https://api.twilio.com/2010-04-01",
                                headers={"User-Agent": ANY,
                                         'Accept-Charset': 'utf-8'},
                                params={}, auth=AUTH, data=None)
        called_kwargs = mock.mock_calls[0][2]
        self.assertTrue(
            'twilio-python' in called_kwargs['headers']['User-Agent']
        )

    def test_connect_apps(self):
        assert_true(isinstance(self.client.connect_apps,
                               resources.ConnectApps))

    def test_authorized_apps(self):
        assert_true(isinstance(self.client.authorized_connect_apps,
                               resources.AuthorizedConnectApps))

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
        uri = "https://api.twilio.com/2010-04-01/Accounts/ACCOUNT_SID" \
              "/Queues/QU123/Members"
        mock.assert_called_with("GET", uri, params={}, auth=AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_request")
    def test_workflows(self, request):
        resp = create_mock_json(
            "tests/resources/task_router/workflows_list.json"
        )
        request.return_value = resp
        workflows = self.task_router_client.workflows("WS123")
        workflows = workflows.list()
        assert_true(workflows[0].sid is not None)
        uri = "https://taskrouter.twilio.com/v1/Workspaces/WS123/Workflows"
        request.assert_called_with("GET", uri, headers=ANY, params={},
                                   auth=AUTH)


class RestClientTimeoutTest(unittest.TestCase):
    def setUp(self):
        self.client = TwilioRestClient("ACCOUNT_SID", "AUTH_TOKEN",
                                       timeout=sentinel.timeout)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_members(self, mock_request):
        resp = create_mock_json("tests/resources/members_list.json")
        mock_request.return_value = resp
        self.client.members("QU123").list()
        mock_request.assert_called_with("GET", ANY, params=ANY, auth=AUTH,
                                        timeout=sentinel.timeout,
                                        use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_arbitrary_member(self, mock_request):
        mock_response = Mock()
        mock_response.ok = True
        mock_response.content = json.dumps({"short_codes": []})
        mock_request.return_value = mock_response
        assert_equal([], self.client.sms.short_codes.list())
        mock_request.assert_called_once_with("GET", ANY, params=ANY, auth=AUTH,
                                             timeout=sentinel.timeout,
                                             use_json_extension=True)
