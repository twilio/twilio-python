from twilio.rest.resources import NextGenInstanceResource, NextGenListResource


class User(NextGenInstanceResource):

    def update(self, sid, **kwargs):
        return self.update_instance(sid, kwargs)

    def delete(self):
        """
        Delete this user
        """
        return self.delete_instance()


class Users(NextGenListResource):

    name = "Users"
    instance = User

    def list(self, **kwargs):
        """
        Returns a page of :class:`User` resources as a list.
        For paging information see :class:`ListResource`.

        **NOTE**: Due to the potentially voluminous amount of data in an
        alert, the full HTTP request and response data is only returned
        in the User instance resource representation.

        """
        return self.get_instances(kwargs)

    def create(self, id, **kwargs):
        """
        Make a phone call to a number.

        :param str id: The identity of the user.
        :param str role: The role to assign the user.

        :return: A :class:`User` object
        """
        kwargs["id"] = id
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete a given User
        """
        return self.delete_instance(sid)
