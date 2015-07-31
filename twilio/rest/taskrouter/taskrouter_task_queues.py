from twilio.rest.resources import NextGenInstanceResource
from twilio.rest.resources import NextGenListResource


class TaskrouterTaskQueues(NextGenInstanceResource):
    """
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: target_workers
    
        The target_workers
    
    .. attribute:: reservation_activity_sid
    
        The reservation_activity_sid
    
    .. attribute:: assignment_activity_sid
    
        The assignment_activity_sid
    
    .. attribute:: max_reserved_workers
    
        The max_reserved_workers
    """
    id_key = "sid"

    def update(self, **kwargs):
        """ Update the instance """
        return self.update_instance(**kwargs)

    def delete(self):
        """ Delete the instance """
        return self.delete_instance()


class TaskrouterTaskQueuesList(NextGenListResource):
    name = "TaskQueues"
    key = "taskrouter_task_queues"
    instance = TaskrouterTaskQueues

    def __init__(self, *args, **kwargs):
        super(TaskrouterTaskQueuesList, self).__init__(*args, **kwargs)

    def update(self, sid, **kwargs):
        """
        Update the :class:`TaskrouterTaskQueues`
        
        :param str assignment_activity_sid: The assignment_activity_sid
        :param str friendly_name: The friendly_name
        :param str max_reserved_workers: The max_reserved_workers
        :param str reservation_activity_sid: The reservation_activity_sid
        :param str sid: The sid
        :param str target_workers: The target_workers
        """
        return self.update_instance(sid, kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`TaskrouterTaskQueues`
        
        :param str evaluate_worker_attributes: The evaluate_worker_attributes
        :param str friendly_name: The friendly_name
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, reservation_activity_sid,
               assignment_activity_sid, **kwargs):
        """
        Create a new :class:`TaskrouterTaskQueues`
        
        :param str assignment_activity_sid: The assignment_activity_sid
        :param str friendly_name: The friendly_name
        :param str max_reserved_workers: The max_reserved_workers
        :param str reservation_activity_sid: The reservation_activity_sid
        :param str target_workers: The target_workers
        """
        kwargs["FriendlyName"] = friendly_name
        kwargs["ReservationActivitySid"] = reservation_activity_sid
        kwargs["AssignmentActivitySid"] = assignment_activity_sid
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the :class:`TaskrouterTaskQueues`
        
        :param str sid: The sid
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`TaskrouterTaskQueues` using an iterator
        
        :param str evaluate_worker_attributes: The evaluate_worker_attributes
        :param str friendly_name: The friendly_name
        """
        return super(TaskrouterTaskQueuesList, self).iter(**kwargs)
