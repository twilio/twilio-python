from datetime import date
import unittest

from mock import patch
from tests.tools import create_mock_json

from twilio.rest.resources import SmsMessages


class SmsTest(unittest.TestCase):

    def setUp(self):
        self.auth = ("sid", "token")
        self.resource = SmsMessages("foo", self.auth)
        self.params = {}

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_on(self, mock):
        resp = create_mock_json("tests/resources/sms_messages_list.json")
        resp.status_code = 201
        mock.return_value = resp

        self.resource.list(date_sent=date(2011, 1, 1))

        self.params['DateSent'] = '2011-01-01'
        mock.assert_called_with("GET", 'foo/SMS/Messages',
                                params=self.params,
                                auth=self.auth,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_after(self, mock):
        resp = create_mock_json("tests/resources/sms_messages_list.json")
        resp.status_code = 201
        mock.return_value = resp

        self.resource.list(after=date(2011, 1, 1))

        self.params['DateSent>'] = '2011-01-01'
        mock.assert_called_with("GET", 'foo/SMS/Messages',
                                params=self.params,
                                auth=self.auth,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_before(self, mock):
        resp = create_mock_json("tests/resources/sms_messages_list.json")
        resp.status_code = 201
        mock.return_value = resp

        self.resource.list(before=date(2011, 1, 1))

        self.params['DateSent<'] = '2011-01-01'
        mock.assert_called_with("GET", 'foo/SMS/Messages',
                                params=self.params,
                                auth=self.auth,
                                use_json_extension=True)
