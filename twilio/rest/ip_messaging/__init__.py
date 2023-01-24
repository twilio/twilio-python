from twilio.rest.ip_messaging import IpMessagingBase
from warnings import warn


class IpMessaging(IpMessagingBase):

    @property
    def credentials(self):
        warn('credentials() is deprecated. Use v2.credentials() instead.', DeprecationWarning, stacklevel=2)
        return self.v2.credentials

    @property
    def services(self):
        warn('services() is deprecated. Use v2.services() instead.', DeprecationWarning, stacklevel=2)
        return self.v2.services



