from twilio.rest.resources.base import InstanceResource, ListResource


class SigningKey(InstanceResource):
    """
    A signing key resource.
    See https://www.twilio.com/docs/api/rest/signing-keys

    .. attribute:: sid

        The unique ID for this signing key.

    .. attribute:: friendly_name

        A human-readable description of this signing key.

    .. attribute:: secret

        This signing key's secret.

    .. attribute:: date_created

        The date this signing key was created, given as UTC in ISO 8601 format.

    .. attribute:: date_updated

        The date this singing key was last updated, given as UTC in ISO 8601
        format.
    """

    def update(self, **kwargs):
        """
        Update this signing key
        """
        return self.parent.update(self.name, **kwargs)

    def delete(self):
        """
        Delete this signing key
        """
        return self.parent.delete(self.name)


class SigningKeys(ListResource):
    name = "SigningKeys"
    key = "signing_keys"
    instance = SigningKey

    def create(self, **kwargs):
        """
        Create a :class:`SigningKey` with any of these optional parameters.

        :param friendly_name: A human readable description of the signing key.
        """
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """
        Update a :class:`SigningKey` with the given parameters.

        All the parameters are describe above in :meth:`create`
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete a :class:`SigningKey`
        """
        return self.delete_instance(sid)

    def list(self, **kw):
        """
        List is not supported, hence raises an Error
        """
        raise AttributeError("SigningKeys do not support lists()")
