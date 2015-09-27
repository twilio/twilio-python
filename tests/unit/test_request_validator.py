# -*- coding: utf-8 -*-
import unittest

from nose.tools import assert_equal, assert_true
from six import b, u

from twilio.request_validator import RequestValidator


class ValidationTest(unittest.TestCase):

    def setUp(self):
        token = "1c892n40nd03kdnc0112slzkl3091j20"
        self.validator = RequestValidator(token)

        self.uri = "http://www.postbin.org/1ed898x"
        self.params = {
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

    def test_compute_signature_bytecode(self):
        expected = b("fF+xx6dTinOaCdZ0aIeNkHr/ZAA=")
        signature = self.validator.compute_signature(self.uri,
                                                     self.params,
                                                     utf=False)
        assert_equal(signature, expected)

    def test_compute_signature_unicode(self):
        expected = u("fF+xx6dTinOaCdZ0aIeNkHr/ZAA=")
        signature = self.validator.compute_signature(self.uri,
                                                     self.params,
                                                     utf=True)
        assert_equal(signature, expected)

    def test_validation(self):
        expected = "fF+xx6dTinOaCdZ0aIeNkHr/ZAA="
        assert_true(self.validator.validate(self.uri, self.params, expected))
