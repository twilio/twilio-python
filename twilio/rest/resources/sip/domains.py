from twilio.rest.resources import InstanceResource, ListResource


class IpAccessControlListMapping(InstanceResource):
    def delete(self):
        """
        Remove this mapping (disassociate the ACL from the Domain).
        """
        return self.parent.delete_instance(self.name)


class IpAccessControlListMappings(ListResource):
    name = "IpAccessControlListMappings"
    key = "ip_access_control_list_mappings"
    instance = IpAccessControlListMapping

    def create(self, ip_access_control_list_sid, **kwargs):
        """Add a :class:`CredentialListMapping` to this domain.

        :param sid: String identifier for an existing
                                    :class:`CredentialList`.
        """
        kwargs.update(ip_access_control_list_sid=ip_access_control_list_sid)
        return self.create_instance(kwargs)

    def delete(self, sid):
        """Remove a :class:`CredentialListMapping` from this domain.

        :param sid: String identifier for a CredentialList resource
        """
        return self.delete_instance(sid)


class CredentialListMapping(InstanceResource):
    def delete(self):
        """
        Remove this mapping (disassociate the CredentialList from the Domain).
        """
        return self.parent.delete_instance(self.name)


class CredentialListMappings(ListResource):
    name = "CredentialListMappings"
    key = "credential_list_mappings"
    instance = CredentialListMapping

    def create(self, credential_list_sid, **kwargs):
        """Add a :class:`CredentialListMapping` to this domain.

        :param sid: String identifier for an existing
                                    :class:`CredentialList`.
        """
        kwargs.update(credential_list_sid=credential_list_sid)
        return self.create_instance(kwargs)

    def delete(self, sid):
        """Remove a :class:`CredentialListMapping` from this domain.

        :param sid: String identifier for a CredentialList resource
        """
        return self.delete_instance(sid)


class SipDomain(InstanceResource):
    """An inbound SIP Domain.

    .. attribute:: sid

        A 34 character string that uniquely identifies this resource.

    .. attribute:: account_sid

        The unique id of the Account responsible for this domain.

    .. attribute:: domain_name

        A unique domain name for this inbound SIP endpoint. Must end in
        .sip.twilio.com.

    .. attribute:: friendly_name

        A human-readable name for this SIP domain. (restrictions?)

    .. attribute:: auth_type

        ???

    .. attribute:: voice_url

        The URL Twilio will request when this domain receives a call.

    .. attribute:: voice_method

        The HTTP method Twilio will use when requesting the above voice_url.
        Either GET or POST.

    .. attribute:: voice_fallback_url

        The URL that Twilio will request if an error occurs retrieving or
        executing the TwiML requested by voice_url.

    .. attribute:: voice_fallback_method

        The HTTP method Twilio will use when requesting the voice_fallback_url.
        Either GET or POST.

    .. attribute:: voice_status_callback_url

        The URL that Twilio will request to pass status parameters (such as
        call ended) to your application.

    .. attribute:: voice_status_callback_method

        The HTTP method Twilio will use to make requests to the status_callback
        URL. Either GET or POST.

    .. attribute:: date_created

        The date that this resource was created.

    .. attribute:: date_updated

        The date that this resource was last updated.

    """
    subresources = [IpAccessControlListMappings, CredentialListMappings]

    def update(self, **kwargs):
        """
        Update this :class:`SipDomain`
        """
        return self.parent.update_instance(self.name, kwargs)

    def delete(self):
        """
        Delete this domain.
        """
        return self.parent.delete_instance(self.name)


class SipDomains(ListResource):
    name = "Domains"
    key = "sip_domains"
    instance = SipDomain

    def create(self, domain_name, **kwargs):
        """ Create a :class:`SipDomain`.

        :param domain_name: A unique domain name ending in '.sip.twilio.com'
        """
        kwargs['domain_name'] = domain_name
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """
        Update a :class:`SipDomain`

        :param sid: String identifier for a SipDomain resource
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete a :class:`SipDomain`.

        :param sid: String identifier for a SipDomain resource
        """
        return self.delete_instance(sid)
