# -*- coding: utf-8 -*-
import os
import unittest
from twilio.util import RequestValidator


class ValidationTest(unittest.TestCase):

    def test_validation(self):
        token = "1c892n40nd03kdnc0112slzkl3091j20"
        validator = RequestValidator(token)

        uri = "http://www.postbin.org/1ed898x"
        params = {
            "AccountSid": "AC9a9f9392lad99kla0sklakjs90j092j3",
            "ApiVersion": "2010-04-01",
            "CallSid": "CAd800bb12c0426a7ea4230e492fef2a4f",
            "CallStatus": "ringing",
            "Called": "+15306384866",
            "CalledCity": "OAKLAND",
            "CalledCountry": "US",
            "CalledState": "CA",
            "CalledZip": "94612",
            "Caller": "+15306666666",
            "CallerCity": "SOUTH LAKE TAHOE",
            "CallerCountry": "US",
            "CallerName": "CA Wireless Call",
            "CallerState": "CA",
            "CallerZip": "89449",
            "Direction": "inbound",
            "From": "+15306666666",
            "FromCity": "SOUTH LAKE TAHOE",
            "FromCountry": "US",
            "FromState": "CA",
            "FromZip": "89449",
            "To": "+15306384866",
            "ToCity": "OAKLAND",
            "ToCountry": "US",
            "ToState": "CA",
            "ToZip": "94612",
            }

        expected = "fF+xx6dTinOaCdZ0aIeNkHr/ZAA="

        self.assertEquals(validator.compute_signature(uri, params), expected)
        self.assertTrue(validator.validate(uri, params, expected))

    @unittest.skip("utf 8 support still a work in progress")
    def test_international_sms(self):

        token = os.environ["TWILIO_AUTH_TOKEN"]
        validator = RequestValidator(token)

        uri = "http://www.postbin.org/1c2pdoc"
        params = {
            "AccountSid": "AC4bf2dafb92341f7caf8650403e422d23",
            "ApiVersion": "2010-04-01",
            "Body": "Chloéñ",
            "From": "+15305451766",
            "FromCity": "SOUTH LAKE TAHOE",
            "FromCountry": "US",
            "FromState": "CA",
            "FromZip": "89449",
            "SmsMessageSid": "SM51d6d055f53f1072543872c601aae89b",
            "SmsStatus": "SM51d6d055f53f1072543872c601aae89b",
            "SmsStatus": "received",
            "To": "+15304194304",
            "ToCity": "WOODLAND",
            "ToCountry": "US",
            "ToState": "CA",
            "ToZip": "95695",
            }

        expected = "UHkWu+6WLOzPunzb8PuCGPeW1Uw="

        self.assertEquals(validator.compute_signature(uri, params), expected)
        self.assertTrue(validator.validate(uri, params, expected))
