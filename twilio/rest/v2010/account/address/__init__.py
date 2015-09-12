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
from twilio.rest.v2010.account.address.dependent_phone_number import (
    DependentPhoneNumber,
    DependentPhoneNumbers,
)
from twilio.rest.resources.base import ListResource


class Address(InstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: city
    
        The city
    
    .. attribute:: customer_name
    
        The customer_name
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: iso_country
    
        The iso_country
    
    .. attribute:: postal_code
    
        The postal_code
    
    .. attribute:: region
    
        The region
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: street
    
        The street
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"
    subresources = [
        DependentPhoneNumbers
    ]

    def load(self, *args, **kwargs):
        super(Address, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def delete(self):
        """
        Delete the instance
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance()

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str city: The city
        :param str customer_name: The customer_name
        :param str friendly_name: The friendly_name
        :param str postal_code: The postal_code
        :param str region: The region
        :param str street: The street
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Address`
        """
        return self.update_instance(kwargs)


class Addresses(ListResource):
    name = "Addresses"
    mount_name = "addresses"
    key = "addresses"
    instance = Address

    def __init__(self, *args, **kwargs):
        super(Addresses, self).__init__(*args, **kwargs)

    def create(self, customer_name, street, city, region, postal_code, iso_country,
               **kwargs):
        """
        Create a new :class:`Address`
        
        :param str city: The city
        :param str customer_name: The customer_name
        :param str friendly_name: The friendly_name
        :param str iso_country: The iso_country
        :param str postal_code: The postal_code
        :param str region: The region
        :param str street: The street
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Address`
        """
        kwargs["CustomerName"] = customer_name
        kwargs["Street"] = street
        kwargs["City"] = city
        kwargs["Region"] = region
        kwargs["PostalCode"] = postal_code
        kwargs["IsoCountry"] = iso_country
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Address`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Address`
        :returns: A placeholder for a :class:`Address` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Address`
        
        :param str city: The city
        :param str customer_name: The customer_name
        :param str friendly_name: The friendly_name
        :param str postal_code: The postal_code
        :param str region: The region
        :param str sid: The sid
        :param str street: The street
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Address`
        """
        return self.update_instance(sid, kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Address`
        
        :param str customer_name: The customer_name
        :param str friendly_name: The friendly_name
        :param str iso_country: The iso_country
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Address`
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Address` using an iterator
        
        :param str customer_name: The customer_name
        :param str friendly_name: The friendly_name
        :param str iso_country: The iso_country
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Address`
        """
        return super(Addresses, self).iter(**kwargs)
