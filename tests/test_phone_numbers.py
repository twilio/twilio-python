from __future__ import with_statement
import json
import unittest

from mock import Mock

from twilio.rest.resources import PhoneNumbers
from twilio.rest.resources import PhoneNumber


class PhoneNumberTest(unittest.TestCase):

    def setUp(self):
        self.parent = Mock()
        self.uri = "/base"
        self.auth = ("AC123", "token")

    def test_update_rename_status_callback_url(self):
        mock = Mock()
        mock.uri = "/base"
        instance = PhoneNumber(mock, "SID")
        instance.update(status_callback_url="http://www.example.com")
        mock.update.assert_called_with("SID", status_callback="http://www.example.com")

    def test_update_instance_rename_status_callback_url(self):
        resource = PhoneNumbers(self.uri, self.auth)
        resource.update_instance = Mock()
        resource.update("SID", status_callback_url="http://www.example.com")
        resource.update_instance.assert_called_with("SID", {"status_callback": "http://www.example.com"})

    def test_application_sid(self):
        resource = PhoneNumbers(self.uri, self.auth)
        resource.update_instance = Mock()
        resource.update("SID", application_sid="foo")
        resource.update_instance.assert_called_with(
                "SID", {"voice_application_sid": "foo", "sms_application_sid": "foo"})

    def test_voice_application_sid(self):
        resource = PhoneNumbers(self.uri, self.auth)
        resource.update_instance = Mock()
        resource.update("SID", voice_application_sid="foo")
        resource.update_instance.assert_called_with(
                "SID", {"voice_application_sid": "foo"})

    def test_sms_application_sid(self):
        resource = PhoneNumbers(self.uri, self.auth)
        resource.update_instance = Mock()
        resource.update("SID", sms_application_sid="foo")
        resource.update_instance.assert_called_with(
                "SID", {"sms_application_sid": "foo"})

    def test_status_callback_url(self):
        resource = PhoneNumbers(self.uri, self.auth)
        resource.update_instance = Mock()
        resource.update("SID", status_callback="foo")
        resource.update_instance.assert_called_with(
                "SID", {"status_callback": "foo"})

    def test_transfer(self):
        resource = PhoneNumbers(self.uri, self.auth)
        resource.update = Mock()
        resource.transfer("SID", "AC123")
        resource.update.assert_called_with("SID", account_sid="AC123")

    def test_instance_transfer(self):
        mock = Mock()
        mock.uri = "/base"
        instance = PhoneNumber(mock, "SID")
        instance.transfer("AC123")
        mock.transfer.assert_called_with("SID", "AC123")

    def test_base_uri(self):
        parent = Mock()
        parent.base_uri = ("https://api.twilio.com/2010-04-01/Accounts/"
            "AC123")
        resource = PhoneNumber(parent, "PNd2ae06cced59a5733d2c1c1c69a83a28")

        with open("tests/resources/incoming_phone_numbers_instance.json") as f:
            entry = json.load(f)
            resource.load(entry)

        self.assertEquals(resource.parent.base_uri,
            ("https://api.twilio.com/2010-04-01/Accounts/AC4bf2dafbed59a573"
             "3d2c1c1c69a83a28"))

    def test_purchase_type(self):

        types = {'local': 'Local', 'mobile': 'Mobile', 'tollfree': 'TollFree'}
        for type in ('local', 'mobile', 'tollfree'):
            resource = PhoneNumbers(self.uri, self.auth)
            resource.request = Mock()
            resource.request.return_value = (None, None)
            resource.load_instance = Mock()
            resource.purchase(type=type, phone_number='888')
            resource.request.assert_called_with('POST', self.uri + '/IncomingPhoneNumbers/' + types[type],
                                                data={'PhoneNumber': '888'})


class IncomingPhoneNumbersTest(unittest.TestCase):

    def setUp(self):
        self.resource = PhoneNumbers("http://api.twilio.com",
                                     ("user", "pass"))

    def test_mobile(self):
        request = Mock()
        request.return_value = (Mock(), {"incoming_phone_numbers": []})
        self.resource.request = request
        self.resource.list(type='mobile')

        uri = "http://api.twilio.com/IncomingPhoneNumbers/Mobile"
        request.assert_called_with("GET", uri, params={})

    def test_local(self):
        request = Mock()
        request.return_value = (Mock(), {"incoming_phone_numbers": []})
        self.resource.request = request
        self.resource.list(type='local')

        uri = "http://api.twilio.com/IncomingPhoneNumbers/Local"
        request.assert_called_with("GET", uri, params={})

    def test_toll_free(self):
        request = Mock()
        request.return_value = (Mock(), {"incoming_phone_numbers": []})
        self.resource.request = request
        self.resource.list(type='tollfree')

        uri = "http://api.twilio.com/IncomingPhoneNumbers/TollFree"
        request.assert_called_with("GET", uri, params={})
