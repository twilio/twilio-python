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


class Local(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: address_requirements
    
        The address_requirements
    
    .. attribute:: api_version
    
        The api_version
    
    .. attribute:: beta
    
        The beta
    
    .. attribute:: capabilities
    
        The capabilities
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: phone_number
    
        The phone_number
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: sms_application_sid
    
        The sms_application_sid
    
    .. attribute:: sms_fallback_method
    
        The sms_fallback_method
    
    .. attribute:: sms_fallback_url
    
        The sms_fallback_url
    
    .. attribute:: sms_method
    
        The sms_method
    
    .. attribute:: sms_url
    
        The sms_url
    
    .. attribute:: status_callback
    
        The status_callback
    
    .. attribute:: status_callback_method
    
        The status_callback_method
    
    .. attribute:: uri
    
        The uri
    
    .. attribute:: voice_application_sid
    
        The voice_application_sid
    
    .. attribute:: voice_caller_id_lookup
    
        The voice_caller_id_lookup
    
    .. attribute:: voice_fallback_method
    
        The voice_fallback_method
    
    .. attribute:: voice_fallback_url
    
        The voice_fallback_url
    
    .. attribute:: voice_method
    
        The voice_method
    
    .. attribute:: voice_url
    
        The voice_url
    """
    id_key = "sid"
    ANY = "any"
    FOREIGN = "foreign"
    LOCAL = "local"
    NONE = "none"

    def load(self, *args, **kwargs):
        super(Local, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)


class Locals(ListResource):
    name = "IncomingPhoneNumbers/Local"
    mount_name = "local"
    key = "incoming_phone_numbers"
    instance = Local

    def __init__(self, *args, **kwargs):
        super(Locals, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Local`
        
        :param bool beta: The beta
        :param str friendly_name: The friendly_name
        :param str phone_number: The phone_number
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Local`
        """
        return self.get_instances(kwargs)

    def create(self, area_code, phone_number, **kwargs):
        """
        Create a new :class:`Local`
        
        :param bool voice_caller_id_lookup: The voice_caller_id_lookup
        :param str api_version: The api_version
        :param str area_code: The area_code
        :param str friendly_name: The friendly_name
        :param str phone_number: The phone_number
        :param str sms_application_sid: The sms_application_sid
        :param str sms_fallback_method: The sms_fallback_method
        :param str sms_fallback_url: The sms_fallback_url
        :param str sms_method: The sms_method
        :param str sms_url: The sms_url
        :param str status_callback: The status_callback
        :param str status_callback_method: The status_callback_method
        :param str voice_application_sid: The voice_application_sid
        :param str voice_fallback_method: The voice_fallback_method
        :param str voice_fallback_url: The voice_fallback_url
        :param str voice_method: The voice_method
        :param str voice_url: The voice_url
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Local`
        """
        kwargs["AreaCode"] = area_code
        kwargs["PhoneNumber"] = phone_number
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Local` using an iterator
        
        :param bool beta: The beta
        :param str friendly_name: The friendly_name
        :param str phone_number: The phone_number
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Local`
        """
        return super(Locals, self).iter(**kwargs)
