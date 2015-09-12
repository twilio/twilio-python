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
from twilio.rest.v2010.account.conference.participant import (
    Participant,
    Participants,
)
from twilio.rest.resources.base import ListResource


class Conference(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account] responsible for creating this conference.
    
    .. attribute:: date_created
    
        The date that this conference was created, given as GMT in RFC 2822
        format.
    
    .. attribute:: date_updated
    
        The date that this conference was last updated, given as GMT in RFC 2822
        format.
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: friendly_name
    
        A user provided string that identifies this conference room.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this conference.
    
    .. attribute:: status
    
        A string representing the status of the conference. May be `init`,
        `in-progress`, or `completed`.
    
    .. attribute:: uri
    
        he URI for this resource, relative to `https://api.twilio.com`.
    """
    id_key = "sid"
    COMPLETED = "completed"
    IN_PROGRESS = "in-progress"
    INIT = "init"
    subresources = [
        Participants
    ]

    def load(self, *args, **kwargs):
        super(Conference, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)


class Conferences(ListResource):
    name = "Conferences"
    mount_name = "conferences"
    key = "conferences"
    instance = Conference

    def __init__(self, *args, **kwargs):
        super(Conferences, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch an instance of a conference
        
        :param str sid: The conference Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Conference`
        :returns: A placeholder for a :class:`Conference` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of conferences belonging to the account used to make the request
        
        :param conference.status status: A string representing the status of the
            conference. May be `init`, `in-progress`, or `completed`.
        :param date date_created: Only show conferences that started on this date, given
            as YYYY-MM-DD. You can also specify inequality such as DateCreated<=YYYY-MM-DD
        :param date date_created_after: The date_created>
        :param date date_created_before: The date_created<
        :param date date_updated: Only show conferences that were last updated on this
            date, given as YYYY-MM-DD. You can also specify inequality such as
            DateUpdated>=YYYY-MM-DD
        :param date date_updated_after: The date_updated>
        :param date date_updated_before: The date_updated<
        :param str friendly_name: Only show results who's friendly name exactly matches
            the string
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Conference`
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
        if "date_updated_before" in kwargs:
            kwargs["DateUpdated<"] = parse_date(kwargs["date_updated_before"])
            del kwargs["date_updated_before"]
        if "date_updated_after" in kwargs:
            kwargs["DateUpdated>"] = parse_date(kwargs["date_updated_after"])
            del kwargs["date_updated_after"]
        if "date_updated" in kwargs:
            kwargs["DateUpdated"] = parse_date(kwargs["date_updated"])
            del kwargs["date_updated"]
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of conferences belonging to the account used to make the request
        
        :param conference.status status: A string representing the status of the
            conference. May be `init`, `in-progress`, or `completed`.
        :param date date_created: Only show conferences that started on this date, given
            as YYYY-MM-DD. You can also specify inequality such as DateCreated<=YYYY-MM-DD
        :param date date_created_after: The date_created>
        :param date date_created_before: The date_created<
        :param date date_updated: Only show conferences that were last updated on this
            date, given as YYYY-MM-DD. You can also specify inequality such as
            DateUpdated>=YYYY-MM-DD
        :param date date_updated_after: The date_updated>
        :param date date_updated_before: The date_updated<
        :param str friendly_name: Only show results who's friendly name exactly matches
            the string
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Conference`
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
        if "date_updated_before" in kwargs:
            kwargs["DateUpdated<"] = parse_date(kwargs["date_updated_before"])
            del kwargs["date_updated_before"]
        if "date_updated_after" in kwargs:
            kwargs["DateUpdated>"] = parse_date(kwargs["date_updated_after"])
            del kwargs["date_updated_after"]
        if "date_updated" in kwargs:
            kwargs["DateUpdated"] = parse_date(kwargs["date_updated"])
            del kwargs["date_updated"]
        return super(Conferences, self).iter(**kwargs)
