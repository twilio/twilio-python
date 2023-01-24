from twilio.rest.sync import SyncBase
from warnings import warn


class Sync(SyncBase):

    @property
    def services(self):
        warn('services() is deprecated. Use v1.services() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.services



