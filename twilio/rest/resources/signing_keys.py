from twilio.rest.resources.base import InstanceResource, ListResource


class SigningKey(InstanceResource):
    """ A signing key resource """

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
