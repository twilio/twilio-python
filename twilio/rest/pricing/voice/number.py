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


class Number(NextGenInstanceResource):
    """
    .. attribute:: number
    
        The number
    
    .. attribute:: country
    
        The country
    
    .. attribute:: iso_country
    
        The iso_country
    
    .. attribute:: outbound_call_price
    
        The outbound_call_price
    
    .. attribute:: inbound_call_price
    
        The inbound_call_price
    
    .. attribute:: price_unit
    
        The price_unit
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "number"


class Numbers(NextGenListResource):
    name = "Voice/Numbers"
    mount_name = "numbers"
    key = "numbers"
    instance = Number

    def __init__(self, *args, **kwargs):
        super(Numbers, self).__init__(*args, **kwargs)

    def get(self, number):
        """
        Get a placeholder for an instance resource.
        
        :param str number: The number
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Number`
        :returns: A placeholder for a :class:`Number` resource
        """
        return self.get_instance(number)
