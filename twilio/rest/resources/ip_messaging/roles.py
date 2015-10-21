from twilio.rest.resources import NextGenInstanceResource, NextGenListResource


class Role(NextGenInstanceResource):

    def update(self, sid, **kwargs):
        return self.update_instance(sid, kwargs)

    def delete(self):
        """
        Delete this role
        """
        return self.delete_instance()


class Roles(NextGenListResource):

    name = "Roles"
    instance = Role

    def list(self, **kwargs):
        """
        Returns a page of :class:`Role` resources as a list.
        For paging information see :class:`ListResource`.

        **NOTE**: Due to the potentially voluminous amount of data in an
        alert, the full HTTP request and response data is only returned
        in the Role instance resource representation.

        """
        return self.get_instances(kwargs)

    def delete(self, sid):
        """
        Delete a given Role
        """
        return self.delete_instance(sid)
