from twilio.rest.proxy import ProxyBase
from warnings import warn


class Proxy(ProxyBase):

    @property
    def services(self):
        warn('services() is deprecated. Use v1.services() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.services
