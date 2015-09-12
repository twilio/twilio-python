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
from twilio.rest.v2010.account.recording.transcription import (
    Transcription,
    Transcriptions,
)
from twilio.rest.resources.base import ListResource


class Recording(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account responsible for this recording.
    
    .. attribute:: api_version
    
        The version of the API in use during the recording.
    
    .. attribute:: call_sid
    
        The call during which the recording was made.
    
    .. attribute:: date_created
    
        The date that this resource was created, given in RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given in RFC 2822 format.
    
    .. attribute:: duration
    
        The length of the recording, in seconds.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`
    """
    id_key = "sid"
    subresources = [
        Transcriptions
    ]

    def load(self, *args, **kwargs):
        super(Recording, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def delete(self):
        """
        Delete a recording from your account
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Recordings(ListResource):
    name = "Recordings"
    mount_name = "recordings"
    key = "recordings"
    instance = Recording

    def __init__(self, *args, **kwargs):
        super(Recordings, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch an instance of a recording
        
        :param str sid: The recording Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Recording`
        :returns: A placeholder for a :class:`Recording` resource
        """
        return self.get_instance(sid)

    def delete(self, sid):
        """
        Delete a recording from your account
        
        :param str sid: The recording Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of recordings belonging to the account used to make the request
        
        :param date date_created: Only show recordings on the given date. Should be
            formatted as YYYY-MM-DD. You can also specify inequalities
        :param date date_created_after: The date_created>
        :param date date_created_before: The date_created<
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Recording`
        """
        if "date_created_before" in kwargs:
            kwargs["DateCreated<"] = parse_date(kwargs["date_created_before"])
            del kwargs["date_created_before"]
        if "date_created_after" in kwargs:
            kwargs["DateCreated>"] = parse_date(kwargs["date_created_after"])
            del kwargs["date_created_after"]
        if "date_created" in kwargs:
            kwargs["DateCreated"] = parse_date(kwargs["date_created"])
            del kwargs["date_created"]
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of recordings belonging to the account used to make the request
        
        :param date date_created: Only show recordings on the given date. Should be
            formatted as YYYY-MM-DD. You can also specify inequalities
        :param date date_created_after: The date_created>
        :param date date_created_before: The date_created<
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Recording`
        """
        if "date_created_before" in kwargs:
            kwargs["DateCreated<"] = parse_date(kwargs["date_created_before"])
            del kwargs["date_created_before"]
        if "date_created_after" in kwargs:
            kwargs["DateCreated>"] = parse_date(kwargs["date_created_after"])
            del kwargs["date_created_after"]
        if "date_created" in kwargs:
            kwargs["DateCreated"] = parse_date(kwargs["date_created"])
            del kwargs["date_created"]
        return super(Recordings, self).iter(**kwargs)
