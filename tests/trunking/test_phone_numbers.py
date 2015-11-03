import unittest
from mock import Mock, patch
from nose.tools import assert_equal, assert_true
from tests.tools import create_mock_json
from twilio.rest.resources.trunking.phone_numbers import (
    PhoneNumbers
)

API_BASE_URI = "https://api.twilio.com/2010-04-01/Accounts"
ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
PHONE_NUMBERS_BASE_URI = "{0}/{1}/{2}".format(API_BASE_URI, ACCOUNT_SID,
                                              "IncomingPhoneNumbers")
AUTH = (ACCOUNT_SID, "auth_token")
BASE_URI = "https://trunking.twilio.com/v1/Trunks/TK11111111111111111111111111111111"


class PhoneNumbersTest(unittest.TestCase):
    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_phone_numbers_lists(self, request):
        resp = create_mock_json(
            'tests/resources/trunking/phone_numbers_list.json')
        resp.status_code = 200
        request.return_value = resp

        phone_numbers = PhoneNumbers(BASE_URI, AUTH)
        result = phone_numbers.list()

        assert_equal(len(result), 1)
        assert_equal(result[0].sid, 'PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].account_sid,
                     'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result[0].trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result[0].friendly_name, "Name")
        assert_equal(result[0].phone_number, "+14158675309")
        assert_equal(result[0].api_version, "2010-04-01")
        assert_equal(result[0].voice_caller_id_lookup, False)
        assert_equal(result[0].voice_fallback_method, "POST")
        assert_equal(result[0].status_callback_method, "POST")
        assert_equal(result[0].sms_url,
                     "https://demo.twilio.com/welcome/sms/reply/")
        assert_equal(result[0].sms_method, "POST")
        assert_equal(result[0].sms_fallback_method, "POST")
        assert_equal(result[0].address_requirements, "none")
        assert_equal(result[0].beta, False)
        assert_equal(result[0].url,
                     "{0}/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".
                     format(BASE_URI))
        assert_equal(result[0].links['phone_number'],
                     "{0}/{1}".format(PHONE_NUMBERS_BASE_URI,
                                      "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
        request.assert_called_with(
            "GET",
            "{0}/PhoneNumbers".format(BASE_URI),
            auth=AUTH,
            params={},
            use_json_extension=False,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_get_phone_numbers_instance(self, request):
        resp = create_mock_json(
            'tests/resources/trunking/phone_numbers_instance.json')
        resp.status_code = 200
        request.return_value = resp

        phone_numbers = PhoneNumbers(BASE_URI, AUTH)
        result = phone_numbers.get('PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_equal(result.sid, 'PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result.account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Name")
        assert_equal(result.phone_number, "+14158675309")
        assert_equal(result.api_version, "2010-04-01")
        assert_equal(result.voice_caller_id_lookup, False)
        assert_equal(result.voice_fallback_method, "POST")
        assert_equal(result.status_callback_method, "POST")
        assert_equal(result.sms_url,
                     "https://demo.twilio.com/welcome/sms/reply/")
        assert_equal(result.sms_method, "POST")
        assert_equal(result.sms_fallback_method, "POST")
        assert_equal(result.address_requirements, "none")
        assert_equal(result.beta, False)
        assert_equal(result.url,
                     "{0}/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(
                         BASE_URI))
        assert_equal(result.links['phone_number'],
                     "{0}/{1}".format(PHONE_NUMBERS_BASE_URI,
                                      "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

        request.assert_called_with(
            "GET",
            "{0}/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(
                BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_associate_phone_numbers_instance(self, request):
        resp = create_mock_json(
            'tests/resources/trunking/phone_numbers_instance.json')
        resp.status_code = 201
        request.return_value = resp

        phone_numbers = PhoneNumbers(BASE_URI, AUTH)
        result = phone_numbers.create('PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_equal(result.sid, 'PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result.account_sid, 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        assert_equal(result.trunk_sid, "TK11111111111111111111111111111111")
        assert_equal(result.friendly_name, "Name")
        assert_equal(result.phone_number, "+14158675309")
        assert_equal(result.api_version, "2010-04-01")
        assert_equal(result.voice_caller_id_lookup, False)
        assert_equal(result.voice_fallback_method, "POST")
        assert_equal(result.status_callback_method, "POST")
        assert_equal(result.sms_url,
                     "https://demo.twilio.com/welcome/sms/reply/")
        assert_equal(result.sms_method, "POST")
        assert_equal(result.sms_fallback_method, "POST")
        assert_equal(result.address_requirements, "none")
        assert_equal(result.beta, False)
        assert_equal(result.url,
                     "{0}/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(
                         BASE_URI))
        assert_equal(result.links['phone_number'],
                     "{0}/{1}".format(PHONE_NUMBERS_BASE_URI,
                                      "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))

        data_dict = dict()
        data_dict['PhoneNumberSid'] = 'PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        request.assert_called_with(
            "POST",
            "{0}/PhoneNumbers".format(BASE_URI),
            auth=AUTH,
            use_json_extension=False,
            data=data_dict,
        )

    @patch('twilio.rest.resources.base.make_twilio_request')
    def test_disassociate_phone_numbers_instance(self, request):
        resp = Mock()
        resp.status_code = 204
        request.return_value = resp

        phone_numbers = PhoneNumbers(BASE_URI, AUTH)
        result = phone_numbers.delete('PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        assert_true(result)

        request.assert_called_with(
            "DELETE",
            "{0}/PhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa".format(
                BASE_URI),
            auth=AUTH,
            use_json_extension=False
        )
