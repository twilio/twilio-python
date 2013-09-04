from twilio.rest.resources import InstanceResource, ListResource


class IpAddress(InstanceResource):
    def update(self, **kwargs):
        """Update this address."""
        return self.parent.update_instance(self.name, **kwargs)

    def delete(self):
        """
        Delete this address.
        """
        return self.parent.delete_instance(self.name)


class IpAddresses(ListResource):
    name = "Addresses"
    key = "addresses"
    instance = IpAddress

    def create(self, friendly_name, ip_address, **kwargs):
        """Add an IP address to a SipIpAccessControlList.

        :param friendly_name: A human-readable name for this address.
        :param ip_address: A dotted-decimal IPv4 address
        """
        kwargs['friendly_name'] = friendly_name
        kwargs['ip_address'] = ip_address
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """Update a :class:`Address`.

        :param sid: String identifier for an address
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """Remove an IP address entry from an ACL.

        :param sid: String identifier for an address
        """
        return self.delete_instance(sid)


class SipIpAccessControlList(InstanceResource):
    subresources = [IpAddresses]

    def update(self, **kwargs):
        """Update this address."""
        return self.parent.update_instance(self.name, **kwargs)

    def delete(self):
        """
        Delete this address.
        """
        return self.parent.delete_instance(self.name)


class SipIpAccessControlLists(ListResource):
    name = "IpAccessControlLists"
    key = "ip_access_control_lists"
    instance = SipIpAccessControlList

    def create(self, friendly_name, **kwargs):
        """ Create a :class:`SipIpAccessControlList`.

        :param domain_name: A human-readable name for this ACL.
        """
        kwargs['friendly_name'] = friendly_name
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """
        Update a :class:`SipIpAccessControlList`

        :param sid: String identifier for a SipIpAccessControlList resource
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete a :class:`SipIpAccessControlList`.

        :param sid: String identifier for a SipIpAccessControlList resource
        """
        return self.delete_instance(sid)
