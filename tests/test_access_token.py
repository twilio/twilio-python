import time
import unittest

from datetime import datetime
from nose.tools import assert_equal
from twilio.jwt import decode
from twilio.access_token import AccessToken, ConversationsGrant, IpMessagingGrant

ACCOUNT_SID = 'AC123'
SIGNING_KEY_SID = 'SK123'


# python2.6 support
def assert_is_not_none(obj):
    assert obj is not None, '%r is None' % obj


def assert_in(obj1, obj2):
    assert obj1 in obj2, '%r is not in %r' % (obj1, obj2)


def assert_greater_equal(obj1, obj2):
    assert obj1 > obj2, '%r is not greater than or equal to %r' % (obj1, obj2)


class AccessTokenTest(unittest.TestCase):
    def _validate_claims(self, payload):
        assert_equal(SIGNING_KEY_SID, payload['iss'])
        assert_equal(ACCOUNT_SID, payload['sub'])

        assert_is_not_none(payload['exp'])
        assert_is_not_none(payload['jti'])
        assert_is_not_none(payload['grants'])

        assert_greater_equal(payload['exp'], int(time.time()))

        assert_in(payload['iss'], payload['jti'])

    def test_empty_grants(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        token = str(scat)

        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal({}, payload['grants'])

    def test_nbf(self):
        now = int(time.mktime(datetime.now().timetuple()))
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret', nbf=now)
        token = str(scat)

        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(now, payload['nbf'])

    def test_identity(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret', identity='test@twilio.com')
        token = str(scat)

        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal({
            'identity': 'test@twilio.com'
        }, payload['grants'])

    def test_conversations_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(ConversationsGrant(configuration_profile_sid='CP123'))

        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(1, len(payload['grants']))
        assert_equal({
            'configuration_profile_sid': 'CP123'
        }, payload['grants']['rtc'])

    def test_ip_messaging_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(IpMessagingGrant(service_sid='IS123', push_credential_sid='CR123'))

        token = str(scat)
        assert_is_not_none(token)
        payload = decode(token, 'secret')
        self._validate_claims(payload)
        assert_equal(1, len(payload['grants']))
        assert_equal({
            'service_sid': 'IS123',
            'push_credential_sid': 'CR123'
        }, payload['grants']['ip_messaging'])

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
