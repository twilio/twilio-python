from twilio.rest.voice import VoiceBase
from warnings import warn


class Voice(VoiceBase):

    @property
    def archived_calls(self):
        warn('archived_calls is deprecated. Use v1.archived_calls instead.', DeprecationWarning, stacklevel=2)
        return self.v1.archived_calls

    @property
    def byoc_trunks(self):
        warn('byoc_trunks is deprecated. Use v1.byoc_trunks instead.', DeprecationWarning, stacklevel=2)
        return self.v1.byoc_trunks

    @property
    def connection_policies(self):
        warn('connection_policies is deprecated. Use v1.connection_policies instead.', DeprecationWarning, stacklevel=2)
        return self.v1.connection_policies

    @property
    def dialing_permissions(self):
        warn('dialing_permissions is deprecated. Use v1.dialing_permissions instead.', DeprecationWarning, stacklevel=2)
        return self.v1.dialing_permissions

    @property
    def ip_records(self):
        warn('ip_records is deprecated. Use v1.ip_records instead.', DeprecationWarning, stacklevel=2)
        return self.v1.ip_records

    @property
    def source_ip_mappings(self):
        warn('source_ip_mappings is deprecated. Use v1.source_ip_mappings instead.', DeprecationWarning, stacklevel=2)
        return self.v1.source_ip_mappings
