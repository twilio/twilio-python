import unittest

from mock import Mock, patch

from tests.tools import create_mock_json
from twilio.rest.resources import Account


class AccountTest(unittest.TestCase):

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_usage_records_subresource(self, request):
        resp = create_mock_json("tests/resources/usage_records_list.json")
        request.return_value = resp

        mock = Mock()
        mock.uri = "/base"
        account = Account(mock, 'AC123')
        account.load_subresources()
        records = account.usage_records.list()
        self.assertEquals(len(records), 2)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_usage_triggers_subresource(self, request):
        resp = create_mock_json("tests/resources/usage_triggers_list.json")
        request.return_value = resp

        mock = Mock()
        mock.uri = "/base"
        account = Account(mock, 'AC123')
        account.load_subresources()
        triggers = account.usage_triggers.list()
        self.assertEquals(len(triggers), 2)
