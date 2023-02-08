from twilio.rest.oauth import OauthBase
from warnings import warn


class Oauth(OauthBase):

    @property
    def oauth(self):
        warn('oauth is deprecated. Use v1.oauth instead.', DeprecationWarning, stacklevel=2)
        return self.v1.oauth

    @property
    def device_code(self):
        warn('device_code is deprecated. Use v1.device_code instead.', DeprecationWarning, stacklevel=2)
        return self.v1.device_code

    @property
    def openid_discovery(self):
        warn('openid_discovery is deprecated. Use v1.openid_discovery instead.', DeprecationWarning, stacklevel=2)
        return self.v1.openid_discovery

    @property
    def token(self):
        warn('token is deprecated. Use v1.token instead.', DeprecationWarning, stacklevel=2)
        return self.v1.token

    @property
    def user_info(self):
        warn('user_info is deprecated. Use v1.user_info instead.', DeprecationWarning, stacklevel=2)
        return self.v1.user_info
