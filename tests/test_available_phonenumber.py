import json
import unittest

from mock import Mock, patch
from nose.tools import assert_equal, assert_true, assert_false

from twilio.rest.exceptions import TwilioException
from twilio.rest.resources import AvailablePhoneNumber
from twilio.rest.resources import AvailablePhoneNumbers
from twilio.rest.resources import PhoneNumbers
from twilio.rest.resources import UNSET_TIMEOUT


class AvailablePhoneNumberTest(unittest.TestCase):

    def setUp(self):
        self.parent = Mock()
        self.instance = AvailablePhoneNumber(self.parent)

    def test_init(self):
        assert_false(self.instance.name)

    def test_purchase(self):
        self.instance.phone_number = "+123"
        self.instance.purchase(voice_url="http://www.google.com").execute()

        self.parent.purchase.assert_called_with(
            voice_url="http://www.google.com",
            phone_number="+123")


class AvailablePhoneNumbersTest(unittest.TestCase):

    def setUp(self):
        self.auth = ("user", "pass")
        self.resource = AvailablePhoneNumbers("http://api.twilio.com",
                                              self.auth, UNSET_TIMEOUT, Mock())

    def test_get(self):
        self.assertRaises(TwilioException, self.resource.get, "PN123")

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_list(self, mock):
        response = Mock()
        response.status_code = 201
        response.content = json.dumps({"available_phone_numbers": []})
        mock.return_value = response

        self.resource.list().execute()

        uri = "http://api.twilio.com/AvailablePhoneNumbers/US/Local"
        mock.assert_called_with("GET", uri, params={},
                                auth=self.auth, use_json_extension=True)

    def test_load_instance(self):
        instance = self.resource.load_instance({"hey": "you"})
        assert_true(isinstance(instance.parent, Mock))
        assert_equal(instance.hey, "you")

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_mobile(self, mock):
        response = Mock()
        response.status_code = 201
        response.content = json.dumps({"available_phone_numbers": []})
        mock.return_value = response

        self.resource.list(type='mobile', country='GB').execute()
        uri = "http://api.twilio.com/AvailablePhoneNumbers/GB/Mobile"
        mock.assert_called_with("GET", uri, params={},
                                auth=self.auth, use_json_extension=True)


class PhoneNumbersTest(unittest.TestCase):

    def setUp(self):
        self.resource = PhoneNumbers("http://api.twilio.com",
                                     ("user", "pass"))

    def test_reference(self):
        assert_equal(self.resource.available_phone_numbers.phone_numbers,
                     self.resource)

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_purchase_status_callback(self, mock):
        response = Mock()
        response.status_code = 201
        response.content = json.dumps({"sid": ""})
        mock.return_value = response

        self.resource.purchase(area_code="530", status_callback_url="http://",
                               status_callback_method="POST").execute()

        uri = "http://api.twilio.com/IncomingPhoneNumbers"

        data = {
            "AreaCode": "530",
            "StatusCallback": "http://",
            "StatusCallbackMethod": "POST",
        }

        mock.assert_called_with("POST", uri, data=data,
                                auth=("user", "pass"),
                                use_json_extension=True)
