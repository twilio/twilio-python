from twilio.rest.resources import NextGenInstanceResource
from twilio.rest.resources import NextGenListResource


class TaskrouterEvent(NextGenInstanceResource):
    """
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: description
    
        The description
    
    .. attribute:: event_data
    
        The event_data
    
    .. attribute:: event_date
    
        The event_date
    
    .. attribute:: event_type
    
        The event_type
    
    .. attribute:: resource_sid
    
        The resource_sid
    
    .. attribute:: resource_type
    
        The resource_type
    """
    id_key = "sid"


class TaskrouterEvents(NextGenListResource):
    name = "Events"
    key = "taskrouter_events"
    instance = TaskrouterEvent

    def __init__(self, *args, **kwargs):
        super(TaskrouterEvents, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`TaskrouterEvent`
        
        :param date end_date: The end_date
        :param date start_date: The start_date
        :param str event_type: The event_type
        :param str minutes: The minutes
        :param str reservation_sid: The reservation_sid
        :param str task_queue_sid: The task_queue_sid
        :param str task_sid: The task_sid
        :param str worker_sid: The worker_sid
        :param str workflow_sid: The workflow_sid
        """
        return self.get_instances(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`TaskrouterEvent` using an iterator
        
        :param date end_date: The end_date
        :param date start_date: The start_date
        :param str event_type: The event_type
        :param str minutes: The minutes
        :param str reservation_sid: The reservation_sid
        :param str task_queue_sid: The task_queue_sid
        :param str task_sid: The task_sid
        :param str worker_sid: The worker_sid
        :param str workflow_sid: The workflow_sid
        """
        return super(TaskrouterEvents, self).iter(**kwargs)
