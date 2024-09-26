

from twilio.http.orgs_token_manager import OrgTokenManager
from twilio.base.exceptions import TwilioException
from twilio.credential.credentialProvider import CredentialProvider
from twilio.authStrategy.authType import AuthType
from twilio.authStrategy.tokenAuthStrategy import TokenAuthStrategy


class OrgsCredentialProvider(CredentialProvider):
    def __init__(self, client_id: str, client_secret: str, token_manager=None):
        super().__init__(AuthType.CLIENT_CREDENTIALS)

        if client_id is None or client_secret is None:
            raise TwilioException("Invalid credentials passed")

        self.grant_type = "client_credentials"
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_manager = token_manager

    def to_auth_strategy(self):
        if self.token_manager is None:
            self.token_manager = OrgTokenManager(self.grant_type, self.client_id, self.client_secret)

        return TokenAuthStrategy(self.token_manager)
