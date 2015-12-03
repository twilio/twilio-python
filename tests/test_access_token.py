import unittest

from nose.tools import assert_equal
from twilio.jwt import decode
from twilio.access_token import AccessToken, ConversationsGrant, IpMessagingGrant

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
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        token = str(scat)

        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal({}, payload['grants'])

    def test_conversations_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(ConversationsGrant())

        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(1, len(payload['grants']))
        assert_equal({}, payload['grants']['rtc'])

    def test_ip_messaging_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(IpMessagingGrant())

        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(1, len(payload['grants']))
        assert_equal({}, payload['grants']['ip_messaging'])

    def test_grants(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(ConversationsGrant())
        scat.add_grant(IpMessagingGrant())

        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(2, len(payload['grants']))
        assert_equal({}, payload['grants']['rtc'])
        assert_equal({}, payload['grants']['ip_messaging'])
