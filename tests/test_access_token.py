import unittest

from nose.tools import assert_equal
from twilio.jwt import decode
from twilio.access_token import AccessToken

ACCOUNT_SID = 'AC123'
SIGNING_KEY_SID = 'SK123'


# python2.6 support
def assert_is_not_none(obj):
    assert obj is not None, '%r is None' % obj


class AccessTokenTest(unittest.TestCase):
    def _validate_claims(self, payload):
        assert_equal(SIGNING_KEY_SID, payload['iss'])
        assert_equal(ACCOUNT_SID, payload['sub'])
        assert_is_not_none(payload['nbf'])
        assert_is_not_none(payload['exp'])
        assert_equal(payload['nbf'] + 3600, payload['exp'])
        assert_is_not_none(payload['jti'])
        assert_equal('{0}-{1}'.format(payload['iss'], payload['nbf']),
                     payload['jti'])
        assert_is_not_none(payload['grants'])

    def test_empty_grants(self):
        scat = AccessToken(SIGNING_KEY_SID, ACCOUNT_SID, 'secret')
        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal([], payload['grants'])

    def test_single_grant(self):
        scat = AccessToken(SIGNING_KEY_SID, ACCOUNT_SID, 'secret')
        scat.add_grant('https://api.twilio.com/**')
        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(1, len(payload['grants']))
        assert_equal('https://api.twilio.com/**', payload['grants'][0]['res'])
        assert_equal(['*'], payload['grants'][0]['act'])

    def test_endpoint_grant(self):
        scat = AccessToken(SIGNING_KEY_SID, ACCOUNT_SID, 'secret')
        scat.add_endpoint_grant('bob')
        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(1, len(payload['grants']))
        assert_equal('sip:bob@AC123.endpoint.twilio.com',
                     payload['grants'][0]['res'])
        assert_equal(['listen', 'invite'], payload['grants'][0]['act'])

    def test_rest_grant(self):
        scat = AccessToken(SIGNING_KEY_SID, ACCOUNT_SID, 'secret')
        scat.add_rest_grant('/Apps')
        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(1, len(payload['grants']))
        assert_equal('https://api.twilio.com/2010-04-01/Accounts/AC123/Apps',
                     payload['grants'][0]['res'])
        assert_equal(['*'], payload['grants'][0]['act'])

    def test_enable_nts(self):
        scat = AccessToken(SIGNING_KEY_SID, ACCOUNT_SID, 'secret')
        scat.enable_nts()
        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(1, len(payload['grants']))
        assert_equal('https://api.twilio.com/2010-04-01/Accounts/AC123/Tokens.json',
                     payload['grants'][0]['res'])
        assert_equal(['POST'], payload['grants'][0]['act'])
