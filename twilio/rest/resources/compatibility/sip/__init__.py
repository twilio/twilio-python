from twilio.rest.resources.sip.credential_list_mapping import CredentialListMappings
from twilio.rest.resources.sip.credentials import Credentials
from twilio.rest.resources.sip.ip_access_control_list_mapping import IpAccessControlListMappings
from twilio.rest.resources.sip.ip_access_control_lists import IpAddresses


class Sip(object):
    """
    Backwards compatibility for sip
    """

    def __init__(self, base_uri, auth, timeout):
        self.uri = "%s/SIP" % base_uri
        self.auth = auth
        self.timeout = timeout

    def ip_access_control_list_mappings(self, domain_sid):
        """
        Return a :class:`IpAccessControlListMappings` instance for the
        :class:`Domain` with the given domain_sid
        """
        base_uri = "%s/Domains/%s" % (self.uri, domain_sid)
        return IpAccessControlListMappings(base_uri, self.auth, self.timeout)

    def credential_list_mappings(self, domain_sid):
        """
        Return a :class:`CredentialListMappings` instance for the
        :class:`Domain` with the given domain_sid
        """
        base_uri = "%s/Domains/%s" % (self.uri, domain_sid)
        return CredentialListMappings(base_uri, self.auth, self.timeout)

    def ip_addresses(self, ip_access_control_list_sid):
        """
        Return a :class:`IpAddresses` instance for the
        :class:`IpAccessControlList` with the given ip_access_control_list_sid
        """
        base_uri = "%s/IpAccessControlLists/%s" % (
            self.uri,
            ip_access_control_list_sid,
        )
        return IpAddresses(base_uri, self.auth, self.timeout)

    def credentials(self, credential_list_sid):
        """
        Return a :class:`Credentials` instance for the
        :class:`CredentialList` with the given credential_list_sid
        """
        base_uri = "%s/CredentialLists/%s" % (
            self.uri,
            credential_list_sid,
        )
        return Credentials(base_uri, self.auth, self.timeout)
