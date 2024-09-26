import base64
from enum import Enum


class BasicAuthStrategy(AuthStrategy):
    def __init__(self, username: str, password: str):
        super().__init__(AuthType.BASIC)
        self.username = username
        self.password = password

    def get_auth_string(self) -> str:
        credentials = f"{self.username}:{self.password}"
        encoded = base64.b64encode(credentials.encode('ascii')).decode('ascii')
        return f"Basic {encoded}"

    def requires_authentication(self) -> bool:
        return True