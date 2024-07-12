import datetime
import jwt

from twilio.base.version import Version
from twilio.http.token_manager import TokenManager
from twilio.twilio_bearer_token_auth import TwilioBearerTokenAuth


class BearerTokenHTTPClient:
    def __init__(self, orgs_token_manager: TokenManager):
        self.orgs_token_manager = orgs_token_manager

    def get_headers(self, version: Version):
        if TwilioBearerTokenAuth.get_access_token() is None or self.is_token_expired(
            TwilioBearerTokenAuth.get_access_token()
        ):
            access_token = self.orgs_token_manager.fetch_access_token(version)
            TwilioBearerTokenAuth.init(access_token)
        else:
            access_token = TwilioBearerTokenAuth.get_access_token()

        return access_token

    def is_token_expired(self, token):
        decoded_jwt = jwt.decode(token, options={"verify_signature": True})
        expires_at = decoded_jwt.get("exp")
        # Add a buffer of 30 seconds
        buffer_seconds = 30
        buffer_expires_at = expires_at - buffer_seconds
        return buffer_expires_at < datetime.datetime.now().timestamp()
