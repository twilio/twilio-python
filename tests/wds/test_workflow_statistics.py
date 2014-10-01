import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.resources.wds.workflows_statistics import WorkflowStatisticsFactory, WorkflowStatistics


AUTH = ("AC123", "token")
BASE_URI = "https://wds.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics"
WORKFLOW_SID = "WFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class WorkflowStatisticsTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/wds/workflows_statistics_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/Workflows/{}".format(BASE_URI, WORKFLOW_SID)
        list_resource = WorkflowStatisticsFactory(BASE_URI, AUTH)
        worker_statistics = WorkflowStatistics(list_resource)
        worker_statistics.get(WORKFLOW_SID)
        request.assert_called_with("GET", uri, params={}, auth=AUTH)
