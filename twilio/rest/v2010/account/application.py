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


class Application(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account that created this application.
    
    .. attribute:: api_version
    
        Requests to this application will start a new TwiML session with this
        API version.
    
    .. attribute:: date_created
    
        The date that this resource was created, given as GMT RFC 2822 format.
    
    .. attribute:: date_updated
    
        The date that this resource was last updated, given as GMT RFC 2822
        format.
    
    .. attribute:: friendly_name
    
        A human readable descriptive text for this resource, up to 64 characters
        long.
    
    .. attribute:: message_status_callback
    
        Twilio will make a `POST` request to this URL to pass status parameters
        (such as sent or failed) to your application if you use the `/Messages`
        endpoint to send the message and specify this application's `Sid` as the
        `ApplicationSid` on an outgoing SMS request.
    
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
    
    .. attribute:: sms_status_callback
    
        The URL that Twilio will `POST` to when a message is sent via the
        `/SMS/Messages` endpoint if you specify the `Sid` of this application on
        an outgoing SMS request.
    
    .. attribute:: sms_url
    
        The URL Twilio will request when a phone number assigned to this
        application receives an incoming SMS message.
    
    .. attribute:: status_callback
    
        The URL that Twilio will request to pass status parameters (such as call
        ended) to your application.
    
    .. attribute:: status_callback_method
    
        The HTTP method Twilio will use to make requests to the `StatusCallback`
        URL. Either `GET` or `POST`.
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`.
    
    .. attribute:: voice_caller_id_lookup
    
        Look up the caller's caller-ID name from the CNAM database (additional
        charges apply). Either `true` or `false`.
    
    .. attribute:: voice_fallback_method
    
        The HTTP method Twilio will use when requesting the `VoiceFallbackUrl`.
        Either `GET` or `POST`.
    
    .. attribute:: voice_fallback_url
    
        The URL that Twilio will request if an error occurs retrieving or
        executing the TwiML requested by `Url`.
    
    .. attribute:: voice_method
    
        The HTTP method Twilio will use when requesting the above `Url`. Either
        `GET` or `POST`.
    
    .. attribute:: voice_url
    
        The URL Twilio will request when a phone number assigned to this
        application receives a call.
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Application, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def delete(self):
        """
        Delete the application by the specified application sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()

    def update(self, **kwargs):
        """
        Updates the application's properties
        
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID name from the
            CNAM database (additional charges apply). Either `true` or `false`.
        :param str api_version: Requests to this application will start a new TwiML
            session with this API version.
        :param str friendly_name: A human readable descriptive text for this resource,
            up to 64 characters long.
        :param str message_status_callback: Twilio will make a `POST` request to this
            URL to pass status parameters (such as sent or failed) to your application if
            you use the `/Messages` endpoint to send the message and specify this
            application's `Sid` as the `ApplicationSid` on an outgoing SMS request.
        :param str sms_fallback_method: The HTTP method Twilio will use when requesting
            the above URL. Either `GET` or `POST`.
        :param str sms_fallback_url: The URL that Twilio will request if an error occurs
            retrieving or executing the TwiML from `SmsUrl`.
        :param str sms_method: The HTTP method Twilio will use when making requests to
            the `SmsUrl`. Either `GET` or `POST`.
        :param str sms_status_callback: The URL that Twilio will `POST` to when a
            message is sent via the `/SMS/Messages` endpoint if you specify the `Sid` of
            this application on an outgoing SMS request.
        :param str sms_url: The URL Twilio will request when a phone number assigned to
            this application receives an incoming SMS message.
        :param str status_callback: The URL that Twilio will request to pass status
            parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method Twilio will use to make
            requests to the `StatusCallback` URL. Either `GET` or `POST`.
        :param str voice_fallback_method: The HTTP method Twilio will use when
            requesting the `VoiceFallbackUrl`. Either `GET` or `POST`.
        :param str voice_fallback_url: The URL that Twilio will request if an error
            occurs retrieving or executing the TwiML requested by `Url`.
        :param str voice_method: The HTTP method Twilio will use when requesting the
            above `Url`. Either `GET` or `POST`.
        :param str voice_url: The URL Twilio will request when a phone number assigned
            to this application receives a call.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Application`
        """
        return self.update_instance(kwargs)


class Applications(ListResource):
    name = "Applications"
    mount_name = "applications"
    key = "applications"
    instance = Application

    def __init__(self, *args, **kwargs):
        super(Applications, self).__init__(*args, **kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Create a new application within your account
        
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID name from the
            CNAM database (additional charges apply). Either `true` or `false`.
        :param str api_version: Requests to this application will start a new TwiML
            session with this API version.
        :param str friendly_name: A human readable descriptive text for this resource,
            up to 64 characters long.
        :param str message_status_callback: Twilio will make a `POST` request to this
            URL to pass status parameters (such as sent or failed) to your application if
            you use the `/Messages` endpoint to send the message and specify this
            application's `Sid` as the `ApplicationSid` on an outgoing SMS request.
        :param str sms_fallback_method: The HTTP method Twilio will use when requesting
            the above URL. Either `GET` or `POST`.
        :param str sms_fallback_url: The URL that Twilio will request if an error occurs
            retrieving or executing the TwiML from `SmsUrl`.
        :param str sms_method: The HTTP method Twilio will use when making requests to
            the `SmsUrl`. Either `GET` or `POST`.
        :param str sms_status_callback: The URL that Twilio will `POST` to when a
            message is sent via the `/SMS/Messages` endpoint if you specify the `Sid` of
            this application on an outgoing SMS request.
        :param str sms_url: The URL Twilio will request when a phone number assigned to
            this application receives an incoming SMS message.
        :param str status_callback: The URL that Twilio will request to pass status
            parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method Twilio will use to make
            requests to the `StatusCallback` URL. Either `GET` or `POST`.
        :param str voice_fallback_method: The HTTP method Twilio will use when
            requesting the `VoiceFallbackUrl`. Either `GET` or `POST`.
        :param str voice_fallback_url: The URL that Twilio will request if an error
            occurs retrieving or executing the TwiML requested by `Url`.
        :param str voice_method: The HTTP method Twilio will use when requesting the
            above `Url`. Either `GET` or `POST`.
        :param str voice_url: The URL Twilio will request when a phone number assigned
            to this application receives a call.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Application`
        """
        kwargs["FriendlyName"] = friendly_name
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the application by the specified application sid
        
        :param str sid: The application sid the uniquely identifies this application
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def get(self, sid):
        """
        Fetch the application specified by the provided sid
        
        :param str sid: The application Sid that that uniquely identifies this resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Application`
        :returns: A placeholder for a :class:`Application` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a list of applications representing an application within the requesting account
        
        :param str friendly_name: Only return application resources with friendly names
            that match exactly with this name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Application`
        """
        return self.get_instances(kwargs)

    def update(self, sid, **kwargs):
        """
        Updates the application's properties
        
        :param bool voice_caller_id_lookup: Look up the caller's caller-ID name from the
            CNAM database (additional charges apply). Either `true` or `false`.
        :param str api_version: Requests to this application will start a new TwiML
            session with this API version.
        :param str friendly_name: A human readable descriptive text for this resource,
            up to 64 characters long.
        :param str message_status_callback: Twilio will make a `POST` request to this
            URL to pass status parameters (such as sent or failed) to your application if
            you use the `/Messages` endpoint to send the message and specify this
            application's `Sid` as the `ApplicationSid` on an outgoing SMS request.
        :param str sid: The sid
        :param str sms_fallback_method: The HTTP method Twilio will use when requesting
            the above URL. Either `GET` or `POST`.
        :param str sms_fallback_url: The URL that Twilio will request if an error occurs
            retrieving or executing the TwiML from `SmsUrl`.
        :param str sms_method: The HTTP method Twilio will use when making requests to
            the `SmsUrl`. Either `GET` or `POST`.
        :param str sms_status_callback: The URL that Twilio will `POST` to when a
            message is sent via the `/SMS/Messages` endpoint if you specify the `Sid` of
            this application on an outgoing SMS request.
        :param str sms_url: The URL Twilio will request when a phone number assigned to
            this application receives an incoming SMS message.
        :param str status_callback: The URL that Twilio will request to pass status
            parameters (such as call ended) to your application.
        :param str status_callback_method: The HTTP method Twilio will use to make
            requests to the `StatusCallback` URL. Either `GET` or `POST`.
        :param str voice_fallback_method: The HTTP method Twilio will use when
            requesting the `VoiceFallbackUrl`. Either `GET` or `POST`.
        :param str voice_fallback_url: The URL that Twilio will request if an error
            occurs retrieving or executing the TwiML requested by `Url`.
        :param str voice_method: The HTTP method Twilio will use when requesting the
            above `Url`. Either `GET` or `POST`.
        :param str voice_url: The URL Twilio will request when a phone number assigned
            to this application receives a call.
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Application`
        """
        return self.update_instance(sid, kwargs)

    def iter(self, **kwargs):
        """
        Retrieve a list of applications representing an application within the requesting account
        
        :param str friendly_name: Only return application resources with friendly names
            that match exactly with this name
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Application`
        """
        return super(Applications, self).iter(**kwargs)
