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


class Country(NextGenInstanceResource):
    """
    .. attribute:: country
    
        The country
    
    .. attribute:: iso_country
    
        The iso_country
    
    .. attribute:: url
    
        The url
    """
    id_key = "iso_country"


class Countries(NextGenListResource):
    name = "PhoneNumbers/Countries"
    mount_name = "countries"
    key = "countries"
    instance = Country

    def __init__(self, *args, **kwargs):
        super(Countries, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Country`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Country`
        """
        return self.get_instances(kwargs)

    def get(self, iso_country):
        """
        Get a placeholder for an instance resource.
        
        :param str iso_country: The iso_country
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Country`
        :returns: A placeholder for a :class:`Country` resource
        """
        return self.get_instance(iso_country)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Country` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Country`
        """
        return super(Countries, self).iter(**kwargs)
