from twilio.http.client_token_manager import ClientTokenManager
from twilio.base.exceptions import TwilioException
from twilio.credential.credential_provider import CredentialProvider
from twilio.auth_strategy.auth_type import AuthType
from twilio.auth_strategy.token_auth_strategy import TokenAuthStrategy


class ClientCredentialProvider(CredentialProvider):
    def __init__(self, client_id: str, client_secret: str, token_manager=None):
        super().__init__(AuthType.CLIENT_CREDENTIALS)

        if client_id is None or client_secret is None:
            raise TwilioException("Client id and Client secret are mandatory")

        self.grant_type = "client_credentials"
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_manager = token_manager
        self.auth_strategy = None

    def to_auth_strategy(self):
        if self.token_manager is None:
            self.token_manager = ClientTokenManager(
                self.grant_type, self.client_id, self.client_secret
            )
        if self.auth_strategy is None:
            self.auth_strategy = TokenAuthStrategy(self.token_manager)
        return self.auth_strategy
