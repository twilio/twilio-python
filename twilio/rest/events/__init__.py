from twilio.rest.events import EventsBase
from warnings import warn


class Events(EventsBase):

    @property
    def event_types(self):
        warn('event_types is deprecated. Use v1.event_types instead.', DeprecationWarning, stacklevel=2)
        return self.v1.event_types

    @property
    def schemas(self):
        warn('schemas is deprecated. Use v1.schemas instead.', DeprecationWarning, stacklevel=2)
        return self.v1.schemas

    @property
    def sinks(self):
        warn('sinks is deprecated. Use v1.sinks instead.', DeprecationWarning, stacklevel=2)
        return self.v1.sinks

    @property
    def subscriptions(self):
        warn('subscriptions is deprecated. Use v1.subscriptions instead.', DeprecationWarning, stacklevel=2)
        return self.v1.subscriptions
