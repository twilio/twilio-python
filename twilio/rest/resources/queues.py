from twilio.rest.resources import InstanceResource, ListResource


class Member(InstanceResource):
    id_key = "call_sid"


class Members(ListResource):
    name = "Members"
    instance = Member
    key = "queue_members"

    def list(self, **kwargs):
        """
        Returns a list of :class:`Member` resources in the given queue

        :param queue_sid: Queue this participant is part of
        """
        return self.get_instances(kwargs)

    def dequeue(self, url, call_sid='Front', **kwargs):
        """
        Dequeues a member from the queue and have the member's call
        begin executing the TwiML document at the url.

        :param call_sid: Call sid specifying the member, if not given,
                         the member at the front of the queue will be used
        :param url: url of the TwiML document to be executed.
        """
        kwargs['url'] = url
        return self.update_instance(call_sid, kwargs)


class Queue(InstanceResource):

    subresources = [
        Members
    ]

    def update(self, **kwargs):
        """
        Update this queue

        :param friendly_name: A new friendly name for this queue
        :param max_size: A new max size. Changing a max size to less than the
                         current size results in the queue rejecting incoming
                         requests until it shrinks below the new max size
        """
        return self.parent.update_instance(self.name, kwargs)

    def delete(self):
        """
        Delete this queue.  Can only be run on empty queues.
        """
        return self.parent.delete_instance(self.name)


class Queues(ListResource):
    name = "Queues"
    instance = Queue

    def list(self, **kwargs):
        """
        Returns a page of :class:`Queue` resources as a list sorted by DateUpdated.
        For paging informtion see :class:`ListResource`
        """
        return self.get_instances(kwargs)

    def create(self, name, **kwargs):
        """ Create an :class:`Queue` with any of these optional parameters.

        :param name: A human readable description of the application,
                              with maximum length 64 characters.
        :param max_size: The limit on calls allowed into the queue (optional)
        """
        kwargs['friendly_name'] = name
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Queue`

        :param sid: String identifier for a Queue resource
        :param friendly_name: A new friendly name for this queue
        :param max_size: A new max size. Changing a max size to less than the
                         current size results in the queue rejecting incoming
                         requests until it shrinks below the new max size
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete a :class:`Queue`. Can only be run on empty queues.

        :param sid: String identifier for a Queue resource
        """
        return self.delete_instance(sid)
