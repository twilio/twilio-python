from twilio.rest.monitor import MonitorBase
from warnings import warn


class Monitor(MonitorBase):

    @property
    def alerts(self):
        warn('alerts is deprecated. Use v1.alerts instead.', DeprecationWarning, stacklevel=2)
        return self.v1.alerts

    @property
    def events(self):
        warn('events is deprecated. Use v1.events instead.', DeprecationWarning, stacklevel=2)
        return self.v1.events
