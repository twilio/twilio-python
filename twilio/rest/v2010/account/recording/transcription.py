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
from twilio.rest.resources.base import InstanceResource
from twilio.rest.resources.base import ListResource


class Transcription(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: duration
    
        The duration
    
    .. attribute:: owner_account_sid
    
        The owner_account_sid
    
    .. attribute:: price
    
        The price
    
    .. attribute:: price_unit
    
        The price_unit
    
    .. attribute:: recording_sid
    
        The recording_sid
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: status
    
        The status
    
    .. attribute:: transcription_text
    
        The transcription_text
    
    .. attribute:: type
    
        The type
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"
    COMPLETED = "completed"
    FAILED = "failed"
    IN_PROGRESS = "in-progress"

    def load(self, *args, **kwargs):
        super(Transcription, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Transcriptions(ListResource):
    name = "Transcriptions"
    mount_name = "transcriptions"
    key = "transcriptions"
    instance = Transcription

    def __init__(self, *args, **kwargs):
        super(Transcriptions, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Transcription`
        :returns: A placeholder for a :class:`Transcription` resource
        """
        return self.get_instance(sid)

    def delete(self, sid):
        """
        Delete the :class:`Transcription`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Transcription`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Transcription`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Transcription` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Transcription`
        """
        return super(Transcriptions, self).iter(**kwargs)
