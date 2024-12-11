from enum import Enum


class AuthType(Enum):
    ORGS_TOKEN = "orgs_stoken"
    NO_AUTH = "noauth"
    BASIC = "basic"
    API_KEY = "api_key"
    CLIENT_CREDENTIALS = "client_credentials"

    def __str__(self):
        return self.value
