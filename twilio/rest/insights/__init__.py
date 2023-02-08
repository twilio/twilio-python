from twilio.rest.insights import InsightsBase
from warnings import warn


class Insights(InsightsBase):

    @property
    def settings(self):
        warn('settings is deprecated. Use v1.settings instead.', DeprecationWarning, stacklevel=2)
        return self.v1.settings

    @property
    def calls(self):
        warn('calls is deprecated. Use v1.calls instead.', DeprecationWarning, stacklevel=2)
        return self.v1.calls

    @property
    def call_summaries(self):
        warn('call_summaries is deprecated. Use v1.call_summaries instead.', DeprecationWarning, stacklevel=2)
        return self.v1.call_summaries

    @property
    def conferences(self):
        warn('conferences is deprecated. Use v1.conferences instead.', DeprecationWarning, stacklevel=2)
        return self.v1.conferences

    @property
    def rooms(self):
        warn('rooms is deprecated. Use v1.rooms instead.', DeprecationWarning, stacklevel=2)
        return self.v1.rooms
