from twilio.rest.accounts import AccountsBase
from warnings import warn


class Accounts(AccountsBase):

    @property
    def auth_token_promotion(self):
        warn('auth_token_promotion() is deprecated. Use v1.auth_token_promotion() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.auth_token_promotion

    @property
    def credentials(self):
        warn('credentials() is deprecated. Use v1.credentials() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.credentials

    @property
    def secondary_auth_token(self):
        warn('secondary_auth_token() is deprecated. Use v1.secondary_auth_token() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.secondary_auth_token



