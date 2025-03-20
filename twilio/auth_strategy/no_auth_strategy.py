from auth_type import AuthType
from twilio.auth_strategy.auth_strategy import AuthStrategy


class NoAuthStrategy(AuthStrategy):
    def __init__(self):
        super().__init__(AuthType.NO_AUTH)

    def get_auth_string(self) -> str:
        return ""

    def requires_authentication(self) -> bool:
        return False
