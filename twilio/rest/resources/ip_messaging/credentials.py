from twilio.rest.resources import NextGenInstanceResource, NextGenListResource


class Credential(NextGenInstanceResource):

    def update(self, sid, **kwargs):
        return self.update_instance(sid, kwargs)

    def delete(self):
        """
        Delete this credential
        """
        return self.delete_instance()


class Credentials(NextGenListResource):

    name = "Credentials"
    instance = Credential

    def list(self, **kwargs):
        """
        Returns a page of :class:`Credential` resources as a list.
        For paging information see :class:`ListResource`.

        **NOTE**: Due to the potentially voluminous amount of data in an
        alert, the full HTTP request and response data is only returned
        in the Credential instance resource representation.

        :param date after: Only list alerts logged after this datetime
        :param date before: Only list alerts logger before this datetime
        :param log_level: If 'error', only shows errors. If 'warning',
         only show warnings
        """
        return self.get_instances(kwargs)

    def create(self, type, **kwargs):
        """
        Make a phone call to a number.

        :param str type: The type of credential
        :param str friendly_name: The friendly name of the credential.

        :return: A :class:`Credential` object
        """
        kwargs["type"] = type
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete a given Credential
        """
        return self.delete_instance(sid)
