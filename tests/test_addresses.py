import unittest

from mock import Mock
from nose.tools import assert_equal, raises

from twilio.exceptions import TwilioException
from twilio.rest.resources import Addresses, DependentPhoneNumbers


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

    def test_dependent_phone_numbers(self):
        pn_list = DependentPhoneNumbers(
            'http://api.twilio.com/mock',
            ('user', 'pass'),
        )
        request = Mock()
        request.return_value = (
            Mock(),
            {
                "dependent_phone_numbers": [{"sid": "PN123"}],
                "total": 1,
                "page": 0,
                "page_size": 50,
            },
        )
        pn_list.request = request

        result = pn_list.list()
        request.assert_called_with(
            "GET",
            "http://api.twilio.com/mock/DependentPhoneNumbers",
            params={},
        )
        assert_equal(result[0].sid, 'PN123')
