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


class ShortCode(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account that owns this short code.
    
    .. attribute:: api_version
    
        SMSs to this short code will start a new TwiML session with this API
        version.
    
    .. attribute:: date_created
    
        The date that this resource was created, given as GMT RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given as GMT RFC 2822
        format.
    
    .. attribute:: friendly_name
    
        A human readable descriptive text for this resource, up to 64 characters
        long. By default, the `FriendlyName` is just the short code.
    
    .. attribute:: short_code
    
        The short code. e.g., 894546.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: sms_fallback_method
    
        The HTTP method Twilio will use when requesting the above URL. Either
        `GET` or `POST`.
    
    .. attribute:: sms_fallback_url
    
        The URL that Twilio will request if an error occurs retrieving or
        executing the TwiML from `SmsUrl`.
    
    .. attribute:: sms_method
    
        The HTTP method Twilio will use when making requests to the `SmsUrl`.
        Either `GET` or `POST`.
    
    .. attribute:: sms_url
    
        The URL Twilio will request when receiving an incoming SMS message to
        this short code.
    
    .. attribute:: uri
    
        he URI for this resource, relative to `https://api.twilio.com`.
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(ShortCode, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update a short code with the following parameters
        
        :param str api_version: SMSs to this short code will start a new TwiML session
            with this API version.
        :param str friendly_name: A human readable descriptive text for this resource,
            up to 64 characters long. By default, the `FriendlyName` is just the short code.
        :param str sms_fallback_method: The HTTP method Twilio will use when requesting
            the above URL. Either `GET` or `POST`.
        :param str sms_fallback_url: The URL that Twilio will request if an error occurs
            retrieving or executing the TwiML from `SmsUrl`.
        :param str sms_method: The HTTP method Twilio will use when making requests to
            the `SmsUrl`. Either `GET` or `POST`.
        :param str sms_url: The URL Twilio will request when receiving an incoming SMS
            message to this short code.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`ShortCode`
        """
        return self.update_instance(kwargs)


class ShortCodes(ListResource):
    name = "SMS/ShortCodes"
    mount_name = "short_codes"
    key = "short_codes"
    instance = ShortCode

    def __init__(self, *args, **kwargs):
        super(ShortCodes, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Fetch an instance of a short code
        
        :param str sid: The short-code Sid that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ShortCode`
        :returns: A placeholder for a :class:`ShortCode` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a short code with the following parameters
        
        :param str api_version: SMSs to this short code will start a new TwiML session
            with this API version.
        :param str friendly_name: A human readable descriptive text for this resource,
            up to 64 characters long. By default, the `FriendlyName` is just the short code.
        :param str sid: The sid
        :param str sms_fallback_method: The HTTP method Twilio will use when requesting
            the above URL. Either `GET` or `POST`.
        :param str sms_fallback_url: The URL that Twilio will request if an error occurs
            retrieving or executing the TwiML from `SmsUrl`.
        :param str sms_method: The HTTP method Twilio will use when making requests to
            the `SmsUrl`. Either `GET` or `POST`.
        :param str sms_url: The URL Twilio will request when receiving an incoming SMS
            message to this short code.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`ShortCode`
        """
        return self.update_instance(sid, kwargs)

    def list(self, **kwargs):
        """
        Retrieve a list of short-codes belonging to the account used to make the request
        
        :param str friendly_name: Only show the ShortCode resources with friendly names
            that exactly match this name
        :param str short_code: Only show the ShortCode resources that match this
            pattern. You can specify partial numbers and use '*' as a wildcard for any digit
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`ShortCode`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of short-codes belonging to the account used to make the request
        
        :param str friendly_name: Only show the ShortCode resources with friendly names
            that exactly match this name
        :param str short_code: Only show the ShortCode resources that match this
            pattern. You can specify partial numbers and use '*' as a wildcard for any digit
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`ShortCode`
        """
        return super(ShortCodes, self).iter(**kwargs)
