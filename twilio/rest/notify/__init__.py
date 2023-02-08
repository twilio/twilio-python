from twilio.rest.notify import NotifyBase
from warnings import warn


class Notify(NotifyBase):

    @property
    def credentials(self):
        warn('credentials is deprecated. Use v1.credentials instead.', DeprecationWarning, stacklevel=2)
        return self.v1.credentials

    @property
    def services(self):
        warn('services is deprecated. Use v1.services instead.', DeprecationWarning, stacklevel=2)
        return self.v1.services
