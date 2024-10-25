from warnings import warn

from twilio.rest.oauth.OauthBase import OauthBase
from twilio.rest.oauth.v1.token import TokenList


class Oauth(OauthBase):

    @property
    def token(self) -> TokenList:
        warn(
            "token is deprecated. Use v1.token instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.token
