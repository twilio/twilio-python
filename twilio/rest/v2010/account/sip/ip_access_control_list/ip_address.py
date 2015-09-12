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


class IpAddress(InstanceResource):
    """
    .. attribute:: sid
    
        The sid
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: ip_address
    
        The ip_address
    
    .. attribute:: ip_access_control_list_sid
    
        The ip_access_control_list_sid
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: uri
    
        The uri
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(IpAddress, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str friendly_name: The friendly_name
        :param str ip_address: The ip_address
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`IpAddress`
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


class IpAddresses(ListResource):
    name = "IpAddresses"
    mount_name = "ip_addresses"
    key = "ip_addresses"
    instance = IpAddress

    def __init__(self, *args, **kwargs):
        super(IpAddresses, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`IpAddress`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`IpAddress`
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, ip_address, **kwargs):
        """
        Create a new :class:`IpAddress`
        
        :param str friendly_name: The friendly_name
        :param str ip_address: The ip_address
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`IpAddress`
        """
        kwargs["FriendlyName"] = friendly_name
        kwargs["IpAddress"] = ip_address
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`IpAddress`
        :returns: A placeholder for a :class:`IpAddress` resource
        """
        return self.get_instance(sid)

    def update(self, sid, ip_address, friendly_name, **kwargs):
        """
        Update a :class:`IpAddress`
        
        :param str friendly_name: The friendly_name
        :param str ip_address: The ip_address
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`IpAddress`
        """
        kwargs["IpAddress"] = ip_address
        kwargs["FriendlyName"] = friendly_name
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`IpAddress`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`IpAddress` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`IpAddress`
        """
        return super(IpAddresses, self).iter(**kwargs)
