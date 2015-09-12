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


class Media(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account responsible for this media.
    
    .. attribute:: content_type
    
        The default mime-type of the media, for example `image/jpeg`,
        `image/png`, or `image/gif`
    
    .. attribute:: date_created
    
        The date that this resource was created, given in RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given in RFC 2822 format.
    
    .. attribute:: parent_sid
    
        The unique id of the resource that created the media.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Media, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def delete(self):
        """
        Delete media from your account. Once delete, you will no longer be billed
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class MediaList(ListResource):
    name = "Media"
    mount_name = "media"
    key = "media_list"
    instance = Media

    def __init__(self, *args, **kwargs):
        super(MediaList, self).__init__(*args, **kwargs)

    def delete(self, sid):
        """
        Delete media from your account. Once delete, you will no longer be billed
        
        :param str sid: The media Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def get(self, sid):
        """
        Fetch a single media instance belonging to the account used to make the request
        
        :param str sid: The media Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Media`
        :returns: A placeholder for a :class:`Media` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of medias belonging to the account used to make the request
        
        :param date date_created: Only show media created on the given date, or
            before/after using date inequalities.
        :param date date_created_after: The date_created>
        :param date date_created_before: The date_created<
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Media`
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
        Retrieve a list of medias belonging to the account used to make the request
        
        :param date date_created: Only show media created on the given date, or
            before/after using date inequalities.
        :param date date_created_after: The date_created>
        :param date date_created_before: The date_created<
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Media`
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
        return super(MediaList, self).iter(**kwargs)
