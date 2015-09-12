# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.conversations.conversation.participant import (
    Participant,
    Participants,
)
from twilio.rest.resources.base import NextGenListResource


class InProgress(NextGenInstanceResource):
    """
    .. attribute:: sid
    
        The sid
    
    .. attribute:: status
    
        The status
    
    .. attribute:: duration
    
        The duration
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: start_time
    
        The start_time
    
    .. attribute:: end_time
    
        The end_time
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: url
    
        The url
    """
    id_key = "sid"
    CREATED = "created"
    ENDED = "ended"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"
    subresources = [
        Participants
    ]

    def load(self, *args, **kwargs):
        super(InProgress, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "start_time") and self.start_time:
            self.start_time = parse_iso_date(self.start_time)
        
        if hasattr(self, "end_time") and self.end_time:
            self.end_time = parse_iso_date(self.end_time)


class InProgresses(NextGenListResource):
    name = "Conversations/InProgress"
    mount_name = "in_progress"
    key = "conversations"
    instance = InProgress

    def __init__(self, *args, **kwargs):
        super(InProgresses, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`InProgress`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`InProgress`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`InProgress` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`InProgress`
        """
        return super(InProgresses, self).iter(**kwargs)
