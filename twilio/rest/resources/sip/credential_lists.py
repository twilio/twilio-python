from twilio.rest.resources import InstanceResource, ListResource


class Credential(InstanceResource):
    def update(self, **kwargs):
        """Update this credential."""
        return self.parent.update_instance(self.name, **kwargs)

    def delete(self):
        """
        Delete this credential.
        """
        return self.parent.delete_instance(self.name)


class Credentials(ListResource):
    name = "Credentials"
    key = "credential_lists"
    instance = Credential

    def create(self, username, password, **kwargs):
        """Add a Credential to a SipCredentialList.

        :param username: The username to add
        :param password: The password for the user
        """
        kwargs.update(username=username, password=password)
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """Update a :class:`Credential`.

        :param sid: String identifier for a credential
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """Remove a username/password

        :param sid: String identifier for a credential
        """
        return self.delete_instance(sid)


class SipCredentialList(InstanceResource):
    subresources = [Credentials]

    def update(self, **kwargs):
        """Update this credential list."""
        return self.parent.update_instance(self.name, **kwargs)

    def delete(self):
        """
        Delete this credential list.
        """
        return self.parent.delete_instance(self.name)


class SipCredentialLists(ListResource):
    name = "CredentialLists"
    key = "credential_lists"
    instance = SipCredentialList

    def create(self, friendly_name, **kwargs):
        """ Create a :class:`SipCredentialList`.

        :param friendly_name: A human-readable name for this credential list.
        """
        kwargs['friendly_name'] = friendly_name
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """
        Update a :class:`SipCredentialList`

        :param sid: String identifier for a SipCredentialList resource
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete a :class:`SipCredentialList`.

        :param sid: String identifier for a SipCredentialList resource
        """
        return self.delete_instance(sid)
