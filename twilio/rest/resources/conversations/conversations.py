from twilio.rest.resources import NextGenInstanceResource, NextGenListResource


class ConversationsRoot(object):

    def __init__(self, base_uri, *args, **kwargs):
        self.uri = "%s/Conversations" % base_uri
        self._instance_base = Conversations(self.uri, *args, **kwargs)
        self.in_progress = Conversations("%s/InProgress" % self.uri, *args,
                                         **kwargs)
        self.completed = Conversations("%s/Completed" % self.uri, *args,
                                       **kwargs)

    def get(self, sid):
        return self._instance_base.get(sid)

    def delete_instance(self, sid):
        return self._instance_base.delete_instance(sid)


class Conversation(NextGenInstanceResource):
    """A Conversation instance representing a call
       between two or more participants.

    .. attribute:: sid

    .. attribute:: account_sid

    .. attribute:: status

    .. attribute:: date_created

    .. attribute:: start_time

    .. attribute:: end_time

    .. attribute:: duration

    .. attribute:: url
    """
    pass


class Conversations(NextGenListResource):

    name = "Conversations"
    instance = Conversation

    def __init__(self, uri, *args, **kwargs):
        super(Conversations, self).__init__(uri, *args, **kwargs)
        # This list is exposed at two different locations: /InProgress
        # and /Completed. The parent Root object will hand us the full URL
        # to set up at.
        self._uri = uri

    @property
    def uri(self):
        return self._uri
