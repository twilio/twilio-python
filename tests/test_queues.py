import unittest
from mock import patch
from tests.tools import create_mock_json
from twilio.rest.http import HttpClient
from twilio.rest.resources import Queues, Queue

BASE_URI = "https://api.twilio.com/2010-04-01/Accounts/AC123"
ACCOUNT_SID = "AC123"
AUTH = (ACCOUNT_SID, "token")
QUEUE_SID = "QU1b9faddec3d54ec18488f86c83019bf0"
CALL_SID = "CAaaf2e9ded94aba3e57c42a3d55be6ff2"


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.client = HttpClient()
        self.list_resource = Queues(self.client, BASE_URI, AUTH)
        self.instance_resource = Queue(self.list_resource, QUEUE_SID)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_queues_list(self, mock):
        resp = create_mock_json("tests/resources/queues_list.json")
        mock.return_value = resp

        uri = "%s/Queues" % (BASE_URI)
        self.list_resource.list().execute()

        mock.assert_called_with("GET", uri, params={}, auth=AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_queues_create(self, mock):
        resp = create_mock_json("tests/resources/queues_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Queues" % (BASE_URI)
        self.list_resource.create('test', max_size=9001).execute()

        mock.assert_called_with("POST", uri,
                                data={'FriendlyName': 'test', 'MaxSize': 9001},
                                auth=AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_queues_get(self, mock):
        resp = create_mock_json("tests/resources/queues_instance.json")
        resp.status_code = 200
        mock.return_value = resp

        uri = "%s/Queues/%s" % (BASE_URI, QUEUE_SID)
        self.list_resource.get(QUEUE_SID).execute()
        mock.assert_called_with("GET", uri, auth=AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_queue_update(self, mock):
        resp = create_mock_json("tests/resources/queues_instance.json")
        resp.status_code = 201
        mock.return_value = resp

        uri = "%s/Queues/%s" % (BASE_URI, QUEUE_SID)
        self.instance_resource.update(friendly_name='QQ').execute()

        mock.assert_called_with("POST", uri,
                                data={'FriendlyName': 'QQ'}, auth=AUTH,
                                use_json_extension=True,
                                client=self.client)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_queue_delete(self, mock):
        resp = create_mock_json("tests/resources/queues_instance.json")
        mock.return_value = resp

        uri = "%s/Queues/%s" % (BASE_URI, QUEUE_SID)
        self.instance_resource.delete().execute()

        mock.assert_called_with("DELETE", uri, auth=AUTH, use_json_extension=True,
                                client=self.client)
