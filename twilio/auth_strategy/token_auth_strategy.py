import jwt
import threading
import logging
from datetime import datetime, timezone

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
        self.fetch_token()
        return f"Bearer {self.token}"

    def requires_authentication(self) -> bool:
        return True

    def fetch_token(self):
        if self.token is None or self.token == "" or self.is_token_expired(self.token):
            with self.lock:
                if (
                    self.token is None
                    or self.token == ""
                    or self.is_token_expired(self.token)
                ):
                    self.logger.info("New token fetched for accessing organization API")
                    self.token = self.token_manager.fetch_access_token()

    def is_token_expired(self, token):
        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            exp = decoded.get("exp")

            if exp is None:
                return True  # No expiration time present, consider it expired

            # Check if the expiration time has passed by using time-zone
            return datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(
                timezone.utc
            )

        except jwt.DecodeError:
            return True  # Token is invalid
        except Exception as e:
            print(f"An error occurred: {e}")
            return True
