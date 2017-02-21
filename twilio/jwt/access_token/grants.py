from twilio.jwt.access_token import AccessTokenGrant


class IpMessagingGrant(AccessTokenGrant):
    """Grant to access Twilio IP Messaging"""
    def __init__(self, service_sid=None, endpoint_id=None,
                 deployment_role_sid=None, push_credential_sid=None):
        self.service_sid = service_sid
        self.endpoint_id = endpoint_id
        self.deployment_role_sid = deployment_role_sid
        self.push_credential_sid = push_credential_sid

    @property
    def key(self):
        return "ip_messaging"

    def to_payload(self):
        grant = {}
        if self.service_sid:
            grant['service_sid'] = self.service_sid
        if self.endpoint_id:
            grant['endpoint_id'] = self.endpoint_id
        if self.deployment_role_sid:
            grant['deployment_role_sid'] = self.deployment_role_sid
        if self.push_credential_sid:
            grant['push_credential_sid'] = self.push_credential_sid

        return grant


class SyncGrant(AccessTokenGrant):
    """Grant to access Twilio Sync"""
    def __init__(self, service_sid=None, endpoint_id=None):
        self.service_sid = service_sid
        self.endpoint_id = endpoint_id

    @property
    def key(self):
        return "data_sync"

    def to_payload(self):
        grant = {}
        if self.service_sid:
            grant['service_sid'] = self.service_sid
        if self.endpoint_id:
            grant['endpoint_id'] = self.endpoint_id

        return grant


class ConversationsGrant(AccessTokenGrant):
    """Grant to access Twilio Conversations"""
    def __init__(self, configuration_profile_sid=None):
        self.configuration_profile_sid = configuration_profile_sid

    @property
    def key(self):
        return "rtc"

    def to_payload(self):
        grant = {}
        if self.configuration_profile_sid:
            grant['configuration_profile_sid'] = self.configuration_profile_sid

        return grant


class VoiceGrant(AccessTokenGrant):
    """Grant to access Twilio Programmable Voice"""
    def __init__(self,
                 outgoing_application_sid=None,
                 outgoing_application_params=None,
                 push_credential_sid=None,
                 endpoint_id=None):
        self.outgoing_application_sid = outgoing_application_sid
        """ :type : str """
        self.outgoing_application_params = outgoing_application_params
        """ :type : dict """
        self.push_credential_sid = push_credential_sid
        """ :type : str """
        self.endpoint_id = endpoint_id
        """ :type : str """

    @property
    def key(self):
        return "voice"

    def to_payload(self):
        grant = {}
        if self.outgoing_application_sid:
            grant['outgoing'] = {}
            grant['outgoing']['application_sid'] = self.outgoing_application_sid

            if self.outgoing_application_params:
                grant['outgoing']['params'] = self.outgoing_application_params

        if self.push_credential_sid:
            grant['push_credential_sid'] = self.push_credential_sid

        if self.endpoint_id:
            grant['endpoint_id'] = self.endpoint_id

        return grant


class VideoGrant(AccessTokenGrant):
    """Grant to access Twilio Video"""
    def __init__(self, configuration_profile_sid=None):
        self.configuration_profile_sid = configuration_profile_sid

    @property
    def key(self):
        return "video"

    def to_payload(self):
        grant = {}
        if self.configuration_profile_sid:
            grant['configuration_profile_sid'] = self.configuration_profile_sid

        return grant
