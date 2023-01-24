from twilio.rest.wireless import WirelessBase
from warnings import warn


class Wireless(WirelessBase):

    @property
    def usage_records(self):
        warn('usage_records() is deprecated. Use v1.usage_records() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.usage_records

    @property
    def commands(self):
        warn('commands() is deprecated. Use v1.commands() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.commands

    @property
    def rate_plans(self):
        warn('rate_plans() is deprecated. Use v1.rate_plans() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.rate_plans

    @property
    def sims(self):
        warn('sims() is deprecated. Use v1.sims() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.sims
