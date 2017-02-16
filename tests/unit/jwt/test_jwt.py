import unittest
import jwt as jwt_lib
import time

from nose.tools import assert_true
from mock import patch

from twilio.jwt import Jwt, JwtDecodeError


class DummyJwt(Jwt):
    """Jwt implementation that allows setting arbitrary payload and headers for testing."""
    def __init__(self, secret_key, issuer, subject=None, algorithm='HS256', nbf=None, ttl=3600,
                 valid_until=None, headers=None, payload=None):
        super(DummyJwt, self).__init__(
            secret_key=secret_key,
            issuer=issuer,
            subject=subject,
            algorithm=algorithm,
            nbf=nbf,
            ttl=ttl,
            valid_until=valid_until
        )
        self._payload = payload or {}
        self._headers = headers or {}

    def _generate_payload(self):
        return self._payload

    def _generate_headers(self):
        return self._headers


class JwtTest(unittest.TestCase):
    def assertIn(self, foo, bar, msg=None):
        """backport for 2.6"""
        return assert_true(foo in bar, msg=(msg or "%s not found in %s" % (foo, bar)))

    def now(self):
        return int(time.time())

    @patch('time.time')
    def test_basic_encode(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', headers={}, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 3600, 'nbf': 0},
            'secret_key',
            algorithm='HS256'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_with_subject(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', subject='subject', headers={}, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 3600, 'nbf': 0, 'sub': 'subject'},
            'secret_key',
            algorithm='HS256'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_custom_ttl(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', ttl=10, headers={}, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 10, 'nbf': 0},
            'secret_key',
            algorithm='HS256'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_ttl_added_to_current_time(self, time_mock):
        time_mock.return_value = 50.0

        jwt = DummyJwt('secret_key', 'issuer', ttl=10, headers={}, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 60, 'nbf': 50},
            'secret_key',
            algorithm='HS256'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_override_ttl(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', ttl=10, headers={}, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 20, 'nbf': 0},
            'secret_key',
            algorithm='HS256'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt(ttl=20))

    @patch('time.time')
    def test_encode_valid_until_overrides_ttl(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', ttl=10, valid_until=70, headers={}, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 70, 'nbf': 0},
            'secret_key',
            algorithm='HS256'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_custom_nbf(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', ttl=10, nbf=5, headers={}, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 10, 'nbf': 5},
            'secret_key',
            algorithm='HS256'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_custom_algorithm(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', algorithm='HS512', headers={}, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 3600, 'nbf': 0},
            'secret_key',
            algorithm='HS512'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_with_headers(self, time_mock):
        time_mock.return_value = 0.0
        headers = {'sooper': 'secret'}

        jwt = DummyJwt('secret_key', 'issuer', algorithm='HS512', headers=headers, payload={})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 3600, 'nbf': 0},
            'secret_key',
            algorithm='HS512',
            headers=headers
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_with_payload(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', algorithm='HS512', payload={'root': 'true'})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 3600, 'nbf': 0, 'root': 'true'},
            'secret_key',
            algorithm='HS512'
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    @patch('time.time')
    def test_encode_with_payload_and_headers(self, time_mock):
        time_mock.return_value = 0.0

        jwt = DummyJwt('secret_key', 'issuer', headers={'yes': 'oui'}, payload={'pay': 'me'})
        expected_jwt = jwt_lib.encode(
            {'iss': 'issuer', 'exp': 3600, 'nbf': 0, 'pay': 'me'},
            'secret_key',
            algorithm='HS256',
            headers={'yes': 'oui'}
        )

        self.assertEqual(expected_jwt, jwt.to_jwt())

    def test_encode_invalid_crypto_alg_fails(self):
        jwt = DummyJwt('secret_key', 'issuer', algorithm='PlzDontTouchAlgorithm')
        self.assertRaises(NotImplementedError, jwt.to_jwt)

    def test_encode_no_key_fails(self):
        jwt = DummyJwt(None, 'issuer')
        self.assertRaises(ValueError, jwt.to_jwt)

    def test_encode_decode(self):
        test_start = self.now()

        jwt = DummyJwt('secret_key', 'issuer', subject='hey', payload={'sick': 'sick'})
        decoded_jwt = Jwt.from_jwt(jwt.to_jwt(), 'secret_key')

        self.assertGreaterEqual(decoded_jwt.valid_until, self.now() + 3600)
        self.assertGreaterEqual(decoded_jwt.nbf, test_start)
        self.assertEqual(decoded_jwt.issuer, 'issuer')
        self.assertEqual(decoded_jwt.secret_key, 'secret_key')
        self.assertEqual(decoded_jwt.algorithm, 'HS256')
        self.assertEqual(decoded_jwt.subject, 'hey')

        self.assertEqual(decoded_jwt.headers, {'typ': 'JWT', 'alg': 'HS256'})
        self.assertDictContainsSubset({
            'iss': 'issuer',
            'sub': 'hey',
            'sick': 'sick',
        }, decoded_jwt.payload)

    def test_decode_bad_secret(self):
        jwt = DummyJwt('secret_key', 'issuer')
        self.assertRaises(JwtDecodeError, Jwt.from_jwt, jwt.to_jwt(), 'letmeinplz')

    def test_decodes_valid_jwt(self):
        expiry_time = self.now() + 1000
        example_jwt = jwt_lib.encode(
            {'hello': 'world', 'iss': 'me', 'sub': 'being awesome', 'exp': expiry_time},
            'secret'
        )

        decoded_jwt = Jwt.from_jwt(example_jwt, 'secret')
        self.assertEqual(decoded_jwt.issuer, 'me')
        self.assertEqual(decoded_jwt.subject, 'being awesome')
        self.assertEqual(decoded_jwt.valid_until, expiry_time)
        self.assertIn('hello', decoded_jwt.payload)
        self.assertEqual(decoded_jwt.payload['hello'], 'world')

    def test_decode_allows_skip_verification(self):
        jwt = DummyJwt('secret', 'issuer', payload={'get': 'rekt'})
        decoded_jwt = Jwt.from_jwt(jwt.to_jwt(), key=None)
        self.assertEqual(decoded_jwt.issuer, 'issuer')
        self.assertEqual(decoded_jwt.payload['get'], 'rekt')
        self.assertIsNone(decoded_jwt.secret_key)
