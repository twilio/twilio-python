import datetime
import jwt

from twilio.http.orgs_token_manager import OrgTokenManager
from twilio.twilio_bearer_token_auth import TwilioBearerTokenAuth


class BearerTokenHTTPClient:
    def __init__(self, orgs_token_manager: OrgTokenManager):
        self.orgs_token_manager = orgs_token_manager

    def get_headers(self):
        headers = {}
        if TwilioBearerTokenAuth.get_access_token() is None:
            access_token = OrgTokenManager.fetch_access_token()
            TwilioBearerTokenAuth.init(access_token)
        elif TwilioBearerTokenAuth.get_access_token() is not None and self.is_token_expired(TwilioBearerTokenAuth.get_access_token()):
            access_token = OrgTokenManager.fetch_access_token()
            TwilioBearerTokenAuth.init(access_token)
        else:
            access_token = TwilioBearerTokenAuth.get_access_token()

        headers.update({
            'Authorization': 'Bearer {}'.format(access_token)
        })

        return headers

    def is_token_expired(self, token):
        decoded_jwt = jwt.decode(token, options={"verify_signature": False})
        expires_at = decoded_jwt.get('exp')
        # Add a buffer of 30 seconds
        buffer_seconds = 30
        buffer_expires_at = expires_at - buffer_seconds
        return buffer_expires_at < datetime.datetime.now().timestamp()
