from twilio.rest.resources import NextGenInstanceResource
from twilio.rest.resources import NextGenListResource


class TaskrouterReservation(NextGenInstanceResource):
    """
    
    .. attribute:: account_sid
    
        The account_sid
    
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

    def update(self, **kwargs):
        """ Update the instance """
        return self.update_instance(**kwargs)


class TaskrouterReservations(NextGenListResource):
    name = "Reservations"
    key = "taskrouter_reservation"
    instance = TaskrouterReservation

    def __init__(self, *args, **kwargs):
        super(TaskrouterReservations, self).__init__(*args, **kwargs)

    def update(self, sid, reservation_status, **kwargs):
        """
        Update the :class:`TaskrouterReservation`
        
        :param str reservation_status: The reservation_status
        :param str sid: The sid
        :param str worker_activity_sid: The worker_activity_sid
        """
        kwargs["ReservationStatus"] = reservation_status
        return self.update_instance(sid, kwargs)
