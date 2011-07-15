import unittest
from mock import Mock
from twilio import TwilioException
from twilio.rest.resources import AvailablePhoneNumber
from twilio.rest.resources import AvailablePhoneNumbers
from twilio.rest.resources import PhoneNumbers


class AvailablePhoneNumberTest(unittest.TestCase):

    def setUp(self):
        self.parent = Mock()
        self.instance = AvailablePhoneNumber(self.parent)

    def test_init(self):
        self.assertEquals(self.instance.name, "")

    def test_purchase(self):
        self.instance.phone_number = "+123"
        self.instance.purchase(voice_url="http://www.google.com")

        self.parent.purchase.assert_called_with(
            voice_url="http://www.google.com",
            phone_number="+123")


class AvailabePhoneNumbersTest(unittest.TestCase):

    def setUp(self):
        self.resource = AvailablePhoneNumbers("http://api.twilio.com",
                                              ("user", "pass"), Mock())

    def test_get(self):
        with self.assertRaises(TwilioException):
            self.resource.get("PN123")

    def test_list(self):
        request = Mock()
        request.return_value = (Mock(), {"available_phone_numbers": []})
        self.resource.request = request

        self.resource.list()

        uri = "http://api.twilio.com/AvailablePhoneNumbers/US/Local"
        request.assert_called_with("GET", uri, params={})

    def test_load_instance(self):
        instance = self.resource.load_instance({"hey": "you"})
        self.assertIsInstance(instance.parent, Mock)
        self.assertEquals(instance.hey, "you")


class PhoneNumbersTest(unittest.TestCase):

    def test_reference(self):
        base = "http://api.twilio.com"
        phone_numbers = PhoneNumbers(base, Mock())

        self.assertEquals(phone_numbers.available_phone_numbers.phone_numbers,
                          phone_numbers)





