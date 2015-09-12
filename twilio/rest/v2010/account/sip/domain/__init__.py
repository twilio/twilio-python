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
from twilio.rest.v2010.account.sip.domain.ip_access_control_list_mapping import (
    IpAccessControlListMapping,
    IpAccessControlListMappings,
)
from twilio.rest.v2010.account.sip.domain.credential_list_mapping import (
    CredentialListMapping,
    CredentialListMappings,
)
from twilio.rest.resources.base import ListResource


class Domain(InstanceResource):
    """
    .. attribute:: account_sid
    
        The unique id of the Account that sent this message
    
    .. attribute:: api_version
    
        The version of the Twilio API used to process the message
    
    .. attribute:: auth_type
    
        The types of authentication you have mapped to your domain
    
    .. attribute:: date_created
    
        The date that this resource was created
    
    .. attribute:: date_updated
    
        The date that this resource was last updated
    
    .. attribute:: domain_name
    
        The unique address you reserve on Twilio to which you route your SIP
        traffic
    
    .. attribute:: friendly_name
    
        A user-specified, human-readable name for the trigger.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies the SIP domain in Twilio
    
    .. attribute:: uri
    
        The URI for this resource relative to https://api.twilio.com
    
    .. attribute:: voice_fallback_method
    
        The HTTP method Twilio will use when requesting the VoiceFallbackUrl
    
    .. attribute:: voice_fallback_url
    
        The URL that Twilio will use if an error occurs retrieving or executing
        the TwiML requested by VoiceUrl
    
    .. attribute:: voice_method
    
        The HTTP method to use with the voice_url
    
    .. attribute:: voice_status_callback_method
    
        The voice_status_callback_method
    
    .. attribute:: voice_status_callback_url
    
        The URL that Twilio will request to pass status parameters
    
    .. attribute:: voice_url
    
        The URL Twilio will request when this domain receives a call
    """
    id_key = "sid"
    subresources = [
        IpAccessControlListMappings,
        CredentialListMappings
    ]

    def load(self, *args, **kwargs):
        super(Domain, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the attributes of a domain
        
        :param str api_version: The api_version
        :param str friendly_name: A user-specified, human-readable name for the trigger.
        :param str voice_fallback_method: The voice_fallback_method
        :param str voice_fallback_url: The voice_fallback_url
        :param str voice_method: The HTTP method to use with the voice_url
        :param str voice_status_callback_method: The voice_status_callback_method
        :param str voice_status_callback_url: The voice_status_callback_url
        :param str voice_url: The voice_url
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Domain`
        """
        return self.update_instance(kwargs)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()


class Domains(ListResource):
    name = "SIP/Domains"
    mount_name = "domains"
    key = "domains"
    instance = Domain

    def __init__(self, *args, **kwargs):
        super(Domains, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a list of domains belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Domain`
        """
        return self.get_instances(kwargs)

    def create(self, domain_name, **kwargs):
        """
        Create a new Domain
        
        :param str domain_name: The unique address you reserve on Twilio to which you
            route your SIP traffic
        :param str friendly_name: A user-specified, human-readable name for the trigger.
        :param str voice_fallback_method: The HTTP method Twilio will use when
            requesting the VoiceFallbackUrl
        :param str voice_fallback_url: The URL that Twilio will use if an error occurs
            retrieving or executing the TwiML requested by VoiceUrl
        :param str voice_method: The HTTP method to use with the voice_url
        :param str voice_status_callback_method: The voice_status_callback_method
        :param str voice_status_callback_url: The URL that Twilio will request to pass
            status parameters
        :param str voice_url: The URL Twilio will request when this domain receives a
            call
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Domain`
        """
        kwargs["DomainName"] = domain_name
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Fetch an instance of a Domain
        
        :param str sid: The domain sid that uniquely identifies the resource
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Domain`
        :returns: A placeholder for a :class:`Domain` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update the attributes of a domain
        
        :param str api_version: The api_version
        :param str friendly_name: A user-specified, human-readable name for the trigger.
        :param str sid: The sid
        :param str voice_fallback_method: The voice_fallback_method
        :param str voice_fallback_url: The voice_fallback_url
        :param str voice_method: The HTTP method to use with the voice_url
        :param str voice_status_callback_method: The voice_status_callback_method
        :param str voice_status_callback_url: The voice_status_callback_url
        :param str voice_url: The voice_url
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Domain`
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Domain`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Retrieve a list of domains belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Domain`
        """
        return super(Domains, self).iter(**kwargs)
