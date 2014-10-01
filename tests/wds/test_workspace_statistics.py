import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.resources.wds.workspaces_statistics import WorkspaceStatisticsFactory, WorkspaceStatistics


AUTH = ("AC123", "token")
BASE_URI = "https://wds.twilio.com/v1/Accounts/AC123/Workspaces"
WORKSPACE_SID = "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class WorkspaceStatisticsTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/wds/workspaces_statistics_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/{}/Statistics".format(BASE_URI, WORKSPACE_SID)
        list_resource = WorkspaceStatisticsFactory(BASE_URI, AUTH)
        worker_statistics = WorkspaceStatistics(list_resource)
        worker_statistics.get(WORKSPACE_SID)
        request.assert_called_with("GET", uri, params={}, auth=AUTH)
