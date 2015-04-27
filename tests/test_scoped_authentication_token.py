import unittest
from decimal import Decimal

from nose.tools import assert_equal, assert_is_not_none, assert_true

from twilio.jwt import decode

from twilio.scoped_authentication_token import ScopedAuthenticationToken, Grant


class ScopedAuthenticationTokenTest(unittest.TestCase):
    def test_add_grant(self):
        scoped_authentication_token = ScopedAuthenticationToken(
            'SK123',
            'AC123',
            None,
            3600,
            [Grant('https://api.twilio.com/**')]
        )
        scoped_authentication_token.add_grant(Grant('https://taskrouter.twilio.com/**'))
        assert_equal(2, len(scoped_authentication_token.grants))

    def test_generate_token(self):
        scoped_authentication_token = ScopedAuthenticationToken(
            'SK123',
            'AC123',
            'Token1',
            3600,
            [Grant('https://api.twilio.com/**')]
        )
        token = scoped_authentication_token.generate_token('secret')
        assert_is_not_none(token)
        decoded_token = decode(token, 'secret')
        assert_is_not_none(decoded_token)
        assert_equal('Token1', decoded_token['jti'])
        assert_equal('SK123', decoded_token['iss'])
        assert_equal('AC123', decoded_token['sub'])
        assert_is_not_none(decoded_token['nbf'])
        assert_is_not_none(decoded_token['exp'])
        assert_true(Decimal(decoded_token['nbf']) < Decimal(decoded_token['exp']))
        assert_is_not_none(decoded_token['grants'])
        assert_equal('https://api.twilio.com/**', decoded_token['grants'][0]['res'])
        assert_equal('*', decoded_token['grants'][0]['act'][0])

    def test_generate_token_without_grant(self):
        scoped_authentication_token = ScopedAuthenticationToken('SK123', 'AC123', 'Token1', 3600)
        token = scoped_authentication_token.generate_token('secret')
        assert_is_not_none(token)
        decoded_token = decode(token, 'secret')
        assert_is_not_none(decoded_token)
        assert_equal('Token1', decoded_token['jti'])
        assert_equal('SK123', decoded_token['iss'])
        assert_equal('AC123', decoded_token['sub'])
        assert_is_not_none(decoded_token['nbf'])
        assert_is_not_none(decoded_token['exp'])
        assert_true(Decimal(decoded_token['nbf']) < Decimal(decoded_token['exp']))
        assert_is_not_none(decoded_token['grants'])
        assert_equal(0, len(decoded_token['grants']))

    def test_generate_token_without_token_id(self):
        scoped_authentication_token = ScopedAuthenticationToken(
            'SK123',
            'AC123',
            None,
            3600,
            [Grant('https://api.twilio.com/**')]
        )
        token = scoped_authentication_token.generate_token('secret')
        assert_is_not_none(token)
        decoded_token = decode(token, 'secret')
        assert_is_not_none(decoded_token)
        assert_is_not_none(decoded_token['jti'])
        assert_equal('SK123', decoded_token['iss'])
        assert_equal('AC123', decoded_token['sub'])
        assert_is_not_none(decoded_token['nbf'])
        assert_is_not_none(decoded_token['exp'])
        assert_true(Decimal(decoded_token['nbf']) < Decimal(decoded_token['exp']))
        assert_is_not_none(decoded_token['grants'])
        assert_equal('https://api.twilio.com/**', decoded_token['grants'][0]['res'])
        assert_equal('*', decoded_token['grants'][0]['act'][0])
