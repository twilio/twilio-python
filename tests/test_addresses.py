import json
import unittest

from mock import Mock, patch
from nose.tools import assert_equal

from twilio.rest.resources import Addresses, DependentPhoneNumbers


class AddressesTest(unittest.TestCase):
    def setUp(self):
        self.parent = Mock()
        self.auth = ("user", "pass")
        self.resource = Addresses("http://api.twilio.com", self.auth)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_update(self, mock):
        response = Mock()
        response.status_code = 200
        response.content = json.dumps({"sid": "123"})
        mock.return_value = response

        self.resource.update("123", friendly_name="hi").execute()

        uri = "http://api.twilio.com/Addresses/123"
        mock.assert_called_with("POST", uri, data={"FriendlyName": "hi"},
                                auth=self.auth, use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_dependent_phone_numbers(self, mock):
        pn_list = DependentPhoneNumbers(
            'http://api.twilio.com/mock',
            ('user', 'pass'),
        )

        response = Mock()
        response.status_code = 200
        response.content = json.dumps({
            "dependent_phone_numbers": [{"sid": "PN123"}],
            "total": 1,
            "page": 0,
            "page_size": 50,
        })
        mock.return_value = response

        result = pn_list.list().execute()
        mock.assert_called_with(
            "GET",
            "http://api.twilio.com/mock/DependentPhoneNumbers",
            params={},
            auth=self.auth,
            use_json_extension=True
        )
        assert_equal(result[0].sid, 'PN123')
