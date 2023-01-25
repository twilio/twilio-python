from rest.frontline_api import FrontlineApiBase
from warnings import warn


class FrontlineApi(FrontlineApiBase):

    @property
    def users(self):
        warn('users() is deprecated. Use v1.users() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.users
