import time
import unittest

from datetime import datetime
from nose.tools import assert_equal

from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (
    IpMessagingGrant,
    SyncGrant,
    VoiceGrant,
    VideoGrant,
    TaskRouterGrant
)

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
        token = scat.to_jwt()

        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal({}, decoded_token.payload['grants'])

    def test_nbf(self):
        now = int(time.mktime(datetime.now().timetuple()))
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret', nbf=now)
        token = scat.to_jwt()

        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal(now, decoded_token.nbf)

    def test_headers(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        token = scat.to_jwt()
        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self.assertEqual(decoded_token.headers['cty'], 'twilio-fpa;v=1')

    def test_identity(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret', identity='test@twilio.com')
        token = scat.to_jwt()

        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal({
            'identity': 'test@twilio.com'
        }, decoded_token.payload['grants'])

    def test_video_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(VideoGrant(room='CP123'))

        token = scat.to_jwt()
        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal(1, len(decoded_token.payload['grants']))
        assert_equal({
            'room': 'CP123'
        }, decoded_token.payload['grants']['video'])

    def test_ip_messaging_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(IpMessagingGrant(service_sid='IS123', push_credential_sid='CR123'))

        token = scat.to_jwt()
        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal(1, len(decoded_token.payload['grants']))
        assert_equal({
            'service_sid': 'IS123',
            'push_credential_sid': 'CR123'
        }, decoded_token.payload['grants']['ip_messaging'])

    def test_sync_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.identity = "bender"
        scat.add_grant(SyncGrant(service_sid='IS123', endpoint_id='blahblahendpoint'))

        token = scat.to_jwt()
        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal(2, len(decoded_token.payload['grants']))
        assert_equal("bender", decoded_token.payload['grants']['identity'])
        assert_equal({
            'service_sid': 'IS123',
            'endpoint_id': 'blahblahendpoint'
        }, decoded_token.payload['grants']['data_sync'])

    def test_grants(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(VideoGrant())
        scat.add_grant(IpMessagingGrant())

        token = scat.to_jwt()
        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal(2, len(decoded_token.payload['grants']))
        assert_equal({}, decoded_token.payload['grants']['video'])
        assert_equal({}, decoded_token.payload['grants']['ip_messaging'])

    def test_programmable_voice_grant(self):
        grant = VoiceGrant(
            outgoing_application_sid='AP123',
            outgoing_application_params={
                'foo': 'bar'
            }
        )

        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(grant)

        token = scat.to_jwt()
        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal(1, len(decoded_token.payload['grants']))
        assert_equal({
            'outgoing': {
                'application_sid': 'AP123',
                'params': {
                    'foo': 'bar'
                }
            }
        }, decoded_token.payload['grants']['voice'])

    def test_task_router_grant(self):
        grant = TaskRouterGrant(
            workspace_sid='WS123',
            worker_sid='WK123',
            role='worker'
        )

        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(grant)

        token = scat.to_jwt()
        assert_is_not_none(token)
        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal(1, len(decoded_token.payload['grants']))
        assert_equal({
            'workspace_sid': 'WS123',
            'worker_sid': 'WK123',
            'role': 'worker'
        }, decoded_token.payload['grants']['task_router'])

    def test_pass_grants_in_constructor(self):
        grants = [
            VideoGrant(),
            IpMessagingGrant()
        ]
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret', grants=grants)

        token = scat.to_jwt()
        assert_is_not_none(token)

        decoded_token = AccessToken.from_jwt(token, 'secret')
        self._validate_claims(decoded_token.payload)
        assert_equal(2, len(decoded_token.payload['grants']))
        assert_equal({}, decoded_token.payload['grants']['video'])
        assert_equal({}, decoded_token.payload['grants']['ip_messaging'])

    def test_constructor_validates_grants(self):
        grants = [VideoGrant, 'GrantMeAccessToEverything']
        self.assertRaises(ValueError, AccessToken, ACCOUNT_SID, SIGNING_KEY_SID, 'secret',
                          grants=grants)

    def test_add_grant_validates_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, 'secret')
        scat.add_grant(VideoGrant())
        self.assertRaises(ValueError, scat.add_grant, 'GrantRootAccess')
