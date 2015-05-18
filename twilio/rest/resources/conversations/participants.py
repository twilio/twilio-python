from twilio.rest.resources import NextGenInstanceResource, NextGenListResource


class Participant(NextGenInstanceResource):
    """A participant in a Conversation.

    .. attribute:: sid

    .. attribute:: conversation_sid

    .. attribute:: account_sid

    .. attribute:: status

    .. attribute:: address

    .. attribute:: date_created

    .. attribute:: start_time

    .. attribute:: end_time

    .. attribute:: duration

    .. attribute:: url
    """
    pass


class Participants(NextGenListResource):
    """A list of :class:`Participant` objects."""

    name = "Participants"
    instance = Participant
