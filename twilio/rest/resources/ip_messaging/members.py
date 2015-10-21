from twilio.rest.resources import NextGenInstanceResource, NextGenListResource


class Member(NextGenInstanceResource):

    def update(self, sid, **kwargs):
        return self.update_instance(sid, kwargs)

    def delete(self):
        """
        Delete this member
        """
        return self.delete_instance()


class Members(NextGenListResource):

    name = "Members"
    instance = Member

    def list(self, **kwargs):
        """
        Returns a page of :class:`Member` resources as a list.
        For paging information see :class:`ListResource`.

        **NOTE**: Due to the potentially voluminous amount of data in an
        alert, the full HTTP request and response data is only returned
        in the Member instance resource representation.

        """
        return self.get_instances(kwargs)

    def create(self, identity, **kwargs):
        """
        Create a Member.

        :param str identity: The identity of the user.
        :param str role: The role to assign the member.

        :return: A :class:`Member` object
        """
        kwargs["identity"] = identity
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete a given Member
        """
        return self.delete_instance(sid)
