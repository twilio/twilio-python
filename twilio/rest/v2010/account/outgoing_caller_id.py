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


class OutgoingCallerId(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account responsible for this Caller Id.
    
    .. attribute:: call_sid
    
        The call_sid
    
    .. attribute:: date_created
    
        The date that this resource was created, given in RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given in RFC 2822 format.
    
    .. attribute:: friendly_name
    
        A human readable descriptive text for this resource, up to 64 characters
        long. By default, the `FriendlyName` is a nicely formatted version of
        the phone number.
    
    .. attribute:: phone_number
    
        The incoming phone number. Formatted with a '+' and country code e.g.,
        +16175551212 (E.164 format).
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`.
    
    .. attribute:: validation_code
    
        The validation_code
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(OutgoingCallerId, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Updates the caller-id
        
        :param str friendly_name: A human readable description of the caller ID
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`OutgoingCallerId`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Delete the caller-id specified from the account
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class OutgoingCallerIds(ListResource):
    name = "OutgoingCallerIds"
    mount_name = "outgoing_caller_ids"
    key = "outgoing_caller_ids"
    instance = OutgoingCallerId

    def __init__(self, *args, **kwargs):
        super(OutgoingCallerIds, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch an outgoing-caller-id belonging to the account used to make the request
        
        :param str sid: The outgoing-caller-id Sid that uniquely identifies this
            resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`OutgoingCallerId`
        :returns: A placeholder for a :class:`OutgoingCallerId` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Updates the caller-id
        
        :param str friendly_name: A human readable description of the caller ID
        :param str sid: The outgoing-caller-id Sid that uniquely identifies this
            resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`OutgoingCallerId`
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the caller-id specified from the account
        
        :param str sid: The outgoing-caller-id Sid that uniquely identifies this
            resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of outgoing-caller-ids belonging to the account used to make the request
        
        :param str friendly_name: Only show the caller id resource that exactly matches
            this name
        :param str phone_number: Only show the caller id resource that exactly matches
            this phone number
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`OutgoingCallerId`
        """
        return self.get_instances(kwargs)

    def create(self, phone_number, **kwargs):
        """
        Add a new CallerID to your account
        
        :param str call_delay: The number of seconds between 0 and 64 to delay before
            initiating the verification call. Defaults to 0
        :param str extension: Digits to dial after connection the verification call
        :param str friendly_name: A human readable description of the new Caller ID
        :param str phone_number: The phone number to verify
        :param str status_callback: A URL that Twilio will request when the verification
            call ends to notify your app if the verification process was successful or not
        :param str status_callback_method: The HTTP method Twilio should use when
            requesting the above URL. Defaults to POST
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`OutgoingCallerId`
        """
        kwargs["PhoneNumber"] = phone_number
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of outgoing-caller-ids belonging to the account used to make the request
        
        :param str friendly_name: Only show the caller id resource that exactly matches
            this name
        :param str phone_number: Only show the caller id resource that exactly matches
            this phone number
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`OutgoingCallerId`
        """
        return super(OutgoingCallerIds, self).iter(**kwargs)

    def add(self, phone_number, **kwargs):
        """ An alias to create """
        return self.create(phone_number=phone_number, **kwargs)

    def verify(self, phone_number, **kwargs):
        """ An alias to create """
        return self.create(phone_number=phone_number, **kwargs)
