# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.resources.base import NextGenListResource
from twilio.rest.resources.base import GetQuery


class PhoneNumber(NextGenInstanceResource):
    """
    .. attribute:: country_code
    
        The country_code
    
    .. attribute:: phone_number
    
        The phone_number
    
    .. attribute:: national_format
    
        The national_format
    
    .. attribute:: mobile_country_code
    
        The mobile_country_code
    
    .. attribute:: mobile_network_code
    
        The mobile_network_code
    
    .. attribute:: name
    
        The name
    
    .. attribute:: type
    
        The type
    
    .. attribute:: carrier
    
        The carrier
    """
    id_key = "phone_number"

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        super(PhoneNumber, self).__init__(parent, None)


class PhoneNumbers(NextGenListResource):
    name = "PhoneNumbers"
    mount_name = "phone_numbers"
    key = "phone_numbers"
    instance = PhoneNumber

    def __init__(self, *args, **kwargs):
        super(PhoneNumbers, self).__init__(*args, **kwargs)

    def get(self, phone_number, **kwargs):
        """
        Get the PhoneNumber
        
        :param str country_code: The country_code
        :param str phone_number: The phone_number
        :param str type: The type
        
        :raises TwilioRestException: when the request fails on execute
        """
        uri = "%s/%s" % (self.uri, phone_number)
        return GetQuery(self, uri, self.use_json_extension,
                        params=kwargs)

    def load_instance(self, data):
        """ Override because PhoneNumber does not have a sid """
        instance = self.instance(self)
        instance.load(data)
        instance.load_subresources()
        return instance
