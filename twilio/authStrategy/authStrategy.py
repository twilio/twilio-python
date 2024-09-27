from twilio.authStrategy.authType import AuthType
from enum import Enum
from abc import abstractmethod


class AuthStrategy(object):
    def __init__(self, auth_type: AuthType):
        self._auth_type = auth_type

    @property
    def auth_type(self) -> AuthType:
        return self._auth_type

    @abstractmethod
    def get_auth_string(self) -> str:
        """Return the authentication string."""
        pass

    @abstractmethod
    def requires_authentication(self) -> bool:
        """Return True if authentication is required, else False."""
        pass