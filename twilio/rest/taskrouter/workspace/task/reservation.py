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
from twilio.rest.resources.base import NextGenInstanceResource
from twilio.rest.resources.base import NextGenListResource


class Reservation(NextGenInstanceResource):
    """
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: reservation_status
    
        The reservation_status
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: task_sid
    
        The task_sid
    
    .. attribute:: worker_name
    
        The worker_name
    
    .. attribute:: worker_sid
    
        The worker_sid
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    """
    id_key = "sid"

    def load(self, *args, **kwargs):
        super(Reservation, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str reservation_status: The reservation_status
        :param str worker_activity_sid: The worker_activity_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Reservation`
        """
        return self.update_instance(kwargs)


class Reservations(NextGenListResource):
    name = "Reservations"
    mount_name = "reservations"
    key = "reservations"
    instance = Reservation

    def __init__(self, *args, **kwargs):
        super(Reservations, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Reservation`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Reservation`
        """
        return self.get_instances(kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Reservation`
        :returns: A placeholder for a :class:`Reservation` resource
        """
        return self.get_instance(sid)

    def update(self, sid, reservation_status, **kwargs):
        """
        Update a :class:`Reservation`
        
        :param str reservation_status: The reservation_status
        :param str sid: The sid
        :param str worker_activity_sid: The worker_activity_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Reservation`
        """
        kwargs["ReservationStatus"] = reservation_status
        return self.update_instance(sid, kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Reservation` using an iterator
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Reservation`
        """
        return super(Reservations, self).iter(**kwargs)
