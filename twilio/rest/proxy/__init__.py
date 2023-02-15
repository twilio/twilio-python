from warnings import warn

from twilio.rest.proxy import ProxyBase
from twilio.rest.proxy.v1.service import ServiceList


class Proxy(ProxyBase):

    @property
    def services(self) -> ServiceList:
        warn('services is deprecated. Use v1.services instead.', DeprecationWarning, stacklevel=2)
        return self.v1.services
