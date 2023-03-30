import time
import unittest
from datetime import datetime

from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (
    SyncGrant,
    VoiceGrant,
    VideoGrant,
    TaskRouterGrant,
    ChatGrant,
    PlaybackGrant,
)

ACCOUNT_SID = "AC123"
SIGNING_KEY_SID = "SK123"


# python2.6 support
def assert_is_not_none(obj):
    assert obj is not None, "%r is None" % obj


def assert_in(obj1, obj2):
    assert obj1 in obj2, "%r is not in %r" % (obj1, obj2)


def assert_greater_equal(obj1, obj2):
    assert obj1 > obj2, "%r is not greater than or equal to %r" % (obj1, obj2)


class AccessTokenTest(unittest.TestCase):
    def _validate_claims(self, payload):
        assert SIGNING_KEY_SID == payload["iss"]
        assert ACCOUNT_SID == payload["sub"]

        assert payload["exp"] is not None
        assert payload["jti"] is not None
        assert payload["grants"] is not None

        assert payload["exp"] >= int(time.time())

        assert payload["iss"] in payload["jti"]

    def test_empty_grants(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        token = scat.to_jwt()

        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert {} == decoded_token.payload["grants"]

    def test_region(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret", region="foo")
        token = scat.to_jwt()
        decoded_token = AccessToken.from_jwt(token, "secret")
        assert decoded_token.headers["twr"] == "foo"

    def test_empty_region(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        token = scat.to_jwt()
        decoded_token = AccessToken.from_jwt(token, "secret")
        self.assertRaises(KeyError, lambda: decoded_token.headers["twr"])

    def test_nbf(self):
        now = int(time.mktime(datetime.now().timetuple()))
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret", nbf=now)
        token = scat.to_jwt()

        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert now == decoded_token.nbf

    def test_headers(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self.assertEqual(decoded_token.headers["cty"], "twilio-fpa;v=1")

    def test_identity(self):
        scat = AccessToken(
            ACCOUNT_SID, SIGNING_KEY_SID, "secret", identity="test@twilio.com"
        )
        token = scat.to_jwt()

        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert {"identity": "test@twilio.com"} == decoded_token.payload["grants"]

    def test_conversations_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(VoiceGrant(outgoing_application_sid="CP123"))

        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 1 == len(decoded_token.payload["grants"])
        assert {"outgoing": {"application_sid": "CP123"}} == decoded_token.payload[
            "grants"
        ]["voice"]

    def test_video_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(VideoGrant(room="RM123"))

        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 1 == len(decoded_token.payload["grants"])
        assert {"room": "RM123"} == decoded_token.payload["grants"]["video"]

    def test_chat_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(ChatGrant(service_sid="IS123", push_credential_sid="CR123"))

        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 1 == len(decoded_token.payload["grants"])
        assert {
            "service_sid": "IS123",
            "push_credential_sid": "CR123",
        } == decoded_token.payload["grants"]["chat"]

    def test_sync_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.identity = "bender"
        scat.add_grant(SyncGrant(service_sid="IS123", endpoint_id="blahblahendpoint"))

        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 2 == len(decoded_token.payload["grants"])
        assert "bender" == decoded_token.payload["grants"]["identity"]
        assert {
            "service_sid": "IS123",
            "endpoint_id": "blahblahendpoint",
        } == decoded_token.payload["grants"]["data_sync"]

    def test_grants(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(VideoGrant())
        scat.add_grant(ChatGrant())

        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 2 == len(decoded_token.payload["grants"])
        assert {} == decoded_token.payload["grants"]["video"]
        assert {} == decoded_token.payload["grants"]["chat"]

    def test_programmable_voice_grant(self):
        grant = VoiceGrant(
            outgoing_application_sid="AP123", outgoing_application_params={"foo": "bar"}
        )

        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(grant)

        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 1 == len(decoded_token.payload["grants"])
        assert {
            "outgoing": {"application_sid": "AP123", "params": {"foo": "bar"}}
        } == decoded_token.payload["grants"]["voice"]

    def test_programmable_voice_grant_incoming(self):
        grant = VoiceGrant(incoming_allow=True)

        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(grant)

        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 1 == len(decoded_token.payload["grants"])
        assert {"incoming": {"allow": True}} == decoded_token.payload["grants"]["voice"]

    def test_task_router_grant(self):
        grant = TaskRouterGrant(
            workspace_sid="WS123", worker_sid="WK123", role="worker"
        )

        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(grant)

        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 1 == len(decoded_token.payload["grants"])
        assert {
            "workspace_sid": "WS123",
            "worker_sid": "WK123",
            "role": "worker",
        } == decoded_token.payload["grants"]["task_router"]

    def test_playback_grant(self):
        """Test that PlaybackGrants are created and decoded correctly."""
        grant = {
            "requestCredentials": None,
            "playbackUrl": "https://000.us-east-1.playback.live-video.net/api/video/v1/us-east-000.channel.000?token=xxxxx",
            "playerStreamerSid": "VJXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        }
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(PlaybackGrant(grant=grant))
        token = scat.to_jwt()
        assert token is not None
        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 1 == len(decoded_token.payload["grants"])
        assert grant == decoded_token.payload["grants"]["player"]

    def test_pass_grants_in_constructor(self):
        grants = [VideoGrant(), ChatGrant()]
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret", grants=grants)

        token = scat.to_jwt()
        assert token is not None

        decoded_token = AccessToken.from_jwt(token, "secret")
        self._validate_claims(decoded_token.payload)
        assert 2 == len(decoded_token.payload["grants"])
        assert {} == decoded_token.payload["grants"]["video"]
        assert {} == decoded_token.payload["grants"]["chat"]

    def test_constructor_validates_grants(self):
        grants = [VideoGrant, "GrantMeAccessToEverything"]
        self.assertRaises(
            ValueError,
            AccessToken,
            ACCOUNT_SID,
            SIGNING_KEY_SID,
            "secret",
            grants=grants,
        )

    def test_add_grant_validates_grant(self):
        scat = AccessToken(ACCOUNT_SID, SIGNING_KEY_SID, "secret")
        scat.add_grant(VideoGrant())
        self.assertRaises(ValueError, scat.add_grant, "GrantRootAccess")
