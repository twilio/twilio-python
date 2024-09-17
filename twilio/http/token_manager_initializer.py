from twilio.http.token_manager import TokenManager


class TokenManagerInitializer:

    org_token_manager = None

    @classmethod
    def set_token_manager(cls, token_manager: TokenManager):
        cls.org_token_manager = token_manager

    @classmethod
    def get_token_manager(cls):
        if cls.org_token_manager is None:
            raise Exception("Token Manager not initialized")
        return cls.org_token_manager
