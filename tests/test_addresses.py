import unittest

from mock import Mock
from nose.tools import raises

from twilio.exceptions import TwilioException
from twilio.rest.resources import Addresses


class AddressesTest(unittest.TestCase):
    def setUp(self):
        self.parent = Mock()
        self.resource = Addresses("http://api.twilio.com", ("user", "pass"))

    def test_update(self):
        request = Mock()
        request.return_value = (Mock(), {"sid": "123"})
        self.resource.request = request

        self.resource.update("123", friendly_name="hi")

        uri = "http://api.twilio.com/Addresses/123"
        request.assert_called_with("POST", uri, data={"FriendlyName": "hi"})

    @raises(TwilioException)
    def test_update_rejects_iso_country(self):
        self.resource.update("123", iso_country="CA")
