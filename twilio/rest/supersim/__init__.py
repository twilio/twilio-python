from twilio.rest.supersim import SupersimBase
from warnings import warn


class Supersim(SupersimBase):

    @property
    def esim_profiles(self):
        warn('esim_profiles is deprecated. Use v1.esim_profiles instead.', DeprecationWarning, stacklevel=2)
        return self.v1.esim_profiles

    @property
    def fleets(self):
        warn('fleets is deprecated. Use v1.fleets instead.', DeprecationWarning, stacklevel=2)
        return self.v1.fleets

    @property
    def ip_commands(self):
        warn('ip_commands is deprecated. Use v1.ip_commands instead.', DeprecationWarning, stacklevel=2)
        return self.v1.ip_commands

    @property
    def networks(self):
        warn('networks is deprecated. Use v1.networks instead.', DeprecationWarning, stacklevel=2)
        return self.v1.networks

    @property
    def network_access_profiles(self):
        warn('network_access_profiles is deprecated. Use v1.network_access_profiles instead.', DeprecationWarning, stacklevel=2)
        return self.v1.network_access_profiles

    @property
    def settings_updates(self):
        warn('settings_updates is deprecated. Use v1.settings_updates instead.', DeprecationWarning, stacklevel=2)
        return self.v1.settings_updates

    @property
    def sims(self):
        warn('sims is deprecated. Use v1.sims instead.', DeprecationWarning, stacklevel=2)
        return self.v1.sims

    @property
    def sms_commands(self):
        warn('sms_commands is deprecated. Use v1.sms_commands instead.', DeprecationWarning, stacklevel=2)
        return self.v1.sms_commands

    @property
    def usage_records(self):
        warn('usage_records is deprecated. Use v1.usage_records instead.', DeprecationWarning, stacklevel=2)
        return self.v1.usage_records
