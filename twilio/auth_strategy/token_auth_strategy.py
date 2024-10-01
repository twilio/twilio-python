import jwt
import threading
import logging
from datetime import datetime, timedelta

from twilio.auth_strategy.auth_type import AuthType
from twilio.auth_strategy.auth_strategy import AuthStrategy
from twilio.http.token_manager import TokenManager


class TokenAuthStrategy(AuthStrategy):
    def __init__(self, token_manager: TokenManager):
        super().__init__(AuthType.ORGS_TOKEN)
        self.token_manager = token_manager
        self.token = None
        self.lock = threading.Lock()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_auth_string(self) -> str:
        if self.token is None:
            self.fetch_token()
        return f"Bearer {self.token}"

    def requires_authentication(self) -> bool:
        return True

    def fetch_token(self):
        self.logger.info("New token fetched for accessing organization API")
        if self.token is None or self.token == "" or self.is_token_expired(self.token):
            with self.lock:
                if self.token is None or self.token == "" or self.is_token_expired(self.token):
                    self.token = self.token_manager.fetch_access_token()

    def is_token_expired(self, token):
        print(f'token is {token}')
        decoded_jwt = jwt.decode(token, options={"verify_signature": True}, algorithms=["RS256"])
        expires_at = decoded_jwt.get("exp")
        # Add a buffer of 30 seconds
        buffer_seconds = 30
        buffer_expires_at = expires_at - buffer_seconds
        return buffer_expires_at < datetime.datetime.now().timestamp()