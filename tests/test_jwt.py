import time
import unittest

from nose.tools import assert_true, assert_equal

from twilio import jwt
from twilio.util import TwilioCapability


class JwtTest(unittest.TestCase):

    def assertIn(self, foo, bar, msg=None):
        """backport for 2.6"""
        return assert_true(foo in bar, msg=(msg or "%s not found in %s"
            % (foo, bar)))

    def test_no_permissions(self):
        token = TwilioCapability("AC123", "XXXXX")
        payload = token.payload()
        assert_equal(len(payload), 1)
        assert_equal(payload["scope"], '')

    def test_inbound_permissions(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_client_incoming("andy")
        payload = token.payload()

        eurl = "scope:client:incoming?clientName=andy"
        assert_equal(len(payload), 1)
        assert_equal(payload['scope'], eurl)

    def test_outbound_permissions(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_client_outgoing("AP123")
        payload = token.payload()

        eurl = "scope:client:outgoing?appSid=AP123"

        assert_equal(len(payload), 1)
        self.assertIn(eurl, payload['scope'])

    def test_outbound_permissions_params(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_client_outgoing("AP123", foobar=3)
        payload = token.payload()

        eurl = "scope:client:outgoing?appParams=foobar%3D3&appSid=AP123"
        assert_equal(payload["scope"], eurl)

    def test_events(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_event_stream()
        payload = token.payload()

        event_uri = "scope:stream:subscribe?path=%2F2010-04-01%2FEvents"
        assert_equal(payload["scope"], event_uri)

    def test_events_with_filters(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_event_stream(foobar="hey")
        payload = token.payload()

        event_uri = "scope:stream:subscribe?params=foobar%3Dhey&path=%2F2010-04-01%2FEvents"
        assert_equal(payload["scope"], event_uri)

    def test_decode(self):
        token = TwilioCapability("AC123", "XXXXX")
        token.allow_client_outgoing("AP123", foobar=3)
        token.allow_client_incoming("andy")
        token.allow_event_stream()

        outgoing_uri = "scope:client:outgoing?appParams=foobar%3D3&appSid=AP123&clientName=andy"
        incoming_uri = "scope:client:incoming?clientName=andy"
        event_uri = "scope:stream:subscribe?path=%2F2010-04-01%2FEvents"

        result = jwt.decode(token.generate(), "XXXXX")
        scope = result["scope"].split(" ")

        self.assertIn(outgoing_uri, scope)
        self.assertIn(incoming_uri, scope)
        self.assertIn(event_uri, scope)

    def setUp(self):
        self.payload = {"iss": "jeff", "exp": int(time.time()), "claim": "insanity"}

    def test_encode_decode(self):
        secret = 'secret'
        jwt_message = jwt.encode(self.payload, secret)
        decoded_payload = jwt.decode(jwt_message, secret)
        self.assertEqual(decoded_payload, self.payload)

    def test_bad_secret(self):
        right_secret = 'foo'
        bad_secret = 'bar'
        jwt_message = jwt.encode(self.payload, right_secret)
        self.assertRaises(jwt.DecodeError, jwt.decode, jwt_message, bad_secret)

    def test_decodes_valid_jwt(self):
        example_payload = {"hello": "world"}
        example_secret = "secret"
        example_jwt = "eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJoZWxsbyI6ICJ3b3JsZCJ9.tvagLDLoaiJKxOKqpBXSEGy7SYSifZhjntgm9ctpyj8"
        decoded_payload = jwt.decode(example_jwt, example_secret)
        self.assertEqual(decoded_payload, example_payload)

    def test_allow_skip_verification(self):
        right_secret = 'foo'
        jwt_message = jwt.encode(self.payload, right_secret)
        decoded_payload = jwt.decode(jwt_message, verify=False)
        self.assertEqual(decoded_payload, self.payload)

    def test_no_secret(self):
        right_secret = 'foo'
        jwt_message = jwt.encode(self.payload, right_secret)
        self.assertRaises(jwt.DecodeError, jwt.decode, jwt_message)

    def test_invalid_crypto_alg(self):
        self.assertRaises(NotImplementedError, jwt.encode, self.payload, "secret", "HS1024")
