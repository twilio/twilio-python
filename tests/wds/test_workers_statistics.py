import unittest

from mock import patch

from tests.tools import create_mock_json
from twilio.rest.resources.wds.workers_statistics import WorkerStatisticsFactory, \
    WorkersStatisticsFactory, WorkerStatistics


AUTH = ("AC123", "token")
BASE_URI = "https://wds.twilio.com/v1/Accounts/AC123/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Statistics"
WORKER_SID = "WKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class WorkerStatisticsTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get(self, request):
        resp = create_mock_json('tests/resources/wds/workers_statistics_instance.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/Workers/{}".format(BASE_URI, WORKER_SID)
        list_resource = WorkerStatisticsFactory(BASE_URI, AUTH)
        worker_statistics = WorkerStatistics(list_resource)
        worker_statistics.get(WORKER_SID)
        request.assert_called_with("GET", uri, params={}, auth=AUTH)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, request):
        resp = create_mock_json('tests/resources/wds/workers_statistics_list.json')
        resp.status_code = 200
        request.return_value = resp

        uri = "{}/Workers".format(BASE_URI)
        list_resource = WorkersStatisticsFactory(BASE_URI, AUTH)
        list_resource.get()
        request.assert_called_with("GET", uri, params={}, auth=AUTH)
