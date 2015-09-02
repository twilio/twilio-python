from .credential_lists import Credentials, SipCredentialLists
from .domains import (
    CredentialListMappings,
    IpAccessControlListMappings,
    Domains
)
from .ip_access_control_lists import IpAddresses, SipIpAccessControlLists

from twilio.rest.v2010.account.sip import (
    Sip as BaseSip
)


class Sip(BaseSip):

    """Holds all the SIP resources."""
    def __init__(self, client, base_uri, auth, timeout):
        super(Sip, self).__init__(client, base_uri, auth, timeout)
        self.uri = "%s/SIP" % base_uri
        self.auth = auth

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
