import unittest

from mock import patch, Mock, sentinel, ANY
from nose.tools import assert_equal, assert_true
from twilio.rest.http import HttpClient

from twilio.rest.resources.imports import json
from twilio.rest import TwilioRestClient, resources, TwilioTaskRouterClient
from tests.tools import create_mock_json

AUTH = ("ACCOUNT_SID", "AUTH_TOKEN")


class RestClientTest(unittest.TestCase):
    def setUp(self):
        self.http_client = HttpClient()
        self.http_client.make_request = Mock()

        self.client = TwilioRestClient("ACCOUNT_SID", "AUTH_TOKEN",
                                       client=self.http_client)
        self.task_router_client = TwilioTaskRouterClient(
            "ACCOUNT_SID", "AUTH_TOKEN", client=self.http_client)

    def test_connect_apps(self):
        assert_true(isinstance(self.client.connect_apps,
                               resources.ConnectApps))

    def test_authorized_apps(self):
        assert_true(isinstance(self.client.authorized_connect_apps,
                               resources.AuthorizedConnectApps))

    def test_conferences(self):
        self.http_client.make_request = Mock()
        mock = self.http_client.make_request
        mock.return_value = Mock()
        mock.return_value.ok = True
        mock.return_value.content = '{"conferences": []}'
        self.client.conferences.list().execute()

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_members(self, mock):
        resp = create_mock_json("tests/resources/members_list.json")
        mock.return_value = resp
        self.client.members("QU123").list().execute()
        uri = "https://api.twilio.com/2010-04-01/Accounts/ACCOUNT_SID" \
              "/Queues/QU123/Members"
        mock.assert_called_with("GET", uri, auth=AUTH,
                                use_json_extension=True,
                                client=self.http_client)

    def test_workflows(self):
        resp = create_mock_json(
            "tests/resources/task_router/workflows_list.json"
        )
        request = self.http_client.make_request
        request.return_value = resp
        workflows = self.task_router_client.workflows("WS123")
        workflows = workflows.list().execute()
        assert_true(workflows[0].sid is not None)
        uri = "https://taskrouter.twilio.com/v1/Workspaces/WS123/Workflows"
        request.assert_called_with("GET", uri, headers=ANY,
                                   auth=AUTH)


class RestClientTimeoutTest(unittest.TestCase):
    def setUp(self):
        self.http_client = HttpClient()
        self.client = TwilioRestClient("ACCOUNT_SID", "AUTH_TOKEN",
                                       timeout=sentinel.timeout,
                                       client=self.http_client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_members(self, mock_request):
        resp = create_mock_json("tests/resources/members_list.json")
        mock_request.return_value = resp
        self.client.members("QU123").list().execute()
        mock_request.assert_called_with("GET", ANY, auth=AUTH,
                                        timeout=sentinel.timeout,
                                        use_json_extension=True,
                                        client=self.http_client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_arbitrary_member(self, mock_request):
        mock_response = Mock()
        mock_response.ok = True
        mock_response.content = json.dumps({"short_codes": []})
        mock_request.return_value = mock_response
        assert_equal([], self.client.sms.short_codes.list().execute())
        mock_request.assert_called_once_with("GET", ANY, auth=AUTH,
                                             timeout=sentinel.timeout,
                                             use_json_extension=True,
                                             client=self.http_client)
