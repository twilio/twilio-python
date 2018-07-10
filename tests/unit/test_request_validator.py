# -*- coding: utf-8 -*-
import unittest

from nose.tools import assert_equal, assert_true
from six import b, u

from twilio.request_validator import RequestValidator


class ValidationTest(unittest.TestCase):

    def setUp(self):
        token = "12345"
        self.validator = RequestValidator(token)

        self.uri = "https://mycompany.com/myapp.php?foo=1&bar=2"
        self.params = {
            "CallSid": "CA1234567890ABCDE",
            "Digits": "1234",
            "From": "+14158675309",
            "To": "+18005551212",
            "Caller": "+14158675309",
        }
        self.expected = "RSOYDt4T1cUTdK1PDd93/VVr8B8="
        self.body = "{\"property\": \"value\", \"boolean\": true}"
        self.bodyHash = "Ch/3Y02as7ldtcmi3+lBbkFQKyg6gMfPGWMmMvluZiA="
        self.encodedBodyHash = self.bodyHash.replace("+", "%2B").replace("=", "%3D")
        self.uriWithBody = self.uri + "&bodySHA256=" + self.encodedBodyHash

    def test_compute_signature_bytecode(self):
        expected = b(self.expected)
        signature = self.validator.compute_signature(self.uri,
                                                     self.params,
                                                     utf=False)
        assert_equal(signature, expected)

    def test_compute_signature_unicode(self):
        expected = u(self.expected)
        signature = self.validator.compute_signature(self.uri,
                                                     self.params,
                                                     utf=True)
        assert_equal(signature, expected)

    def test_compute_hash_bytecode(self):
        expected = b(self.bodyHash)
        body_hash = self.validator.compute_hash(self.body, utf=False)

        assert_equal(expected, body_hash)

    def test_compute_hash_unicode(self):
        expected = u(self.bodyHash)
        body_hash = self.validator.compute_hash(self.body, utf=True)

        assert_equal(expected, body_hash)

    def test_validation(self):
        assert_true(self.validator.validate(self.uri, self.params, self.expected))

    def test_validation_removes_port_on_https(self):
        uri = self.uri.replace(".com", ".com:1234")
        assert_true(self.validator.validate(uri, self.params, self.expected))

    def test_validation_of_body_succeeds(self):
        uri = self.uriWithBody
        is_valid = self.validator.validate(uri, self.body, "afcFvPLPYT8mg/JyIVkdnqQKa2s=")
        assert_true(is_valid)
