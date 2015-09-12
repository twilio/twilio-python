# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.base import InstanceResource
from twilio.rest.v2010.account.available_phone_number.local import (
    Local,
    Locals,
)
from twilio.rest.v2010.account.available_phone_number.toll_free import (
    TollFree,
    TollFrees,
)
from twilio.rest.v2010.account.available_phone_number.mobile import (
    Mobile,
    Mobiles,
)
from twilio.rest.resources.base import ListResource


class AvailablePhoneNumberCountry(InstanceResource):
    """
    .. attribute:: country_code
    
        The country_code
    
    .. attribute:: country
    
        The country
    
    .. attribute:: uri
    
        The uri
    
    .. attribute:: beta
    
        The beta
    
    .. attribute:: subresource_uris
    
        The subresource_uris
    """
    id_key = "country_code"
    subresources = [
        Locals,
        TollFrees,
        Mobiles
    ]


class AvailablePhoneNumberCountries(ListResource):
    name = "AvailablePhoneNumbers"
    mount_name = "available_phone_numbers"
    key = "countries"
    instance = AvailablePhoneNumberCountry

    def __init__(self, *args, **kwargs):
        super(AvailablePhoneNumberCountries, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`AvailablePhoneNumberCountry`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`AvailablePhoneNumberCountry`
        """
        return self.get_instances(kwargs)

    def get(self, country_code):
        """
        Get a placeholder for an instance resource.
        
        :param str country_code: The country_code
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`AvailablePhoneNumberCountry`
        :returns: A placeholder for a :class:`AvailablePhoneNumberCountry` resource
        """
        return self.get_instance(country_code)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`AvailablePhoneNumberCountry` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`AvailablePhoneNumberCountry`
        """
        return super(AvailablePhoneNumberCountries, self).iter(**kwargs)
