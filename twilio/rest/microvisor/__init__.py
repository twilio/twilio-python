from twilio.rest.microvisor import MicrovisorBase
from warnings import warn


class Microvisor(MicrovisorBase):

    @property
    def apps(self):
        warn('apps is deprecated. Use v1.apps instead.', DeprecationWarning, stacklevel=2)
        return self.v1.apps

    @property
    def devices(self):
        warn('devices is deprecated. Use v1.devices instead.', DeprecationWarning, stacklevel=2)
        return self.v1.devices
