from twilio.rest.resources import NextGenInstanceResource
from twilio.rest.resources import NextGenListResource


class TaskrouterWorker(NextGenInstanceResource):
    """
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: activity_name
    
        The activity_name
    
    .. attribute:: activity_sid
    
        The activity_sid
    
    .. attribute:: attributes
    
        The attributes
    
    .. attribute:: available
    
        The available
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_status_changed
    
        The date_status_changed
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    """
    id_key = "sid"

    def update(self, **kwargs):
        """ Update the instance """
        return self.update_instance(**kwargs)

    def delete(self):
        """ Delete the instance """
        return self.delete_instance()


class TaskrouterWorkers(NextGenListResource):
    name = "Workers"
    key = "taskrouter_workers"
    instance = TaskrouterWorker

    def __init__(self, *args, **kwargs):
        super(TaskrouterWorkers, self).__init__(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`TaskrouterWorker`
        
        :param str activity_name: The activity_name
        :param str activity_sid: The activity_sid
        :param str available: The available
        :param str friendly_name: The friendly_name
        :param str target_workers_expression: The target_workers_expression
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Create a new :class:`TaskrouterWorker`
        
        :param str activity_sid: The activity_sid
        :param str attributes: The attributes
        :param str friendly_name: The friendly_name
        """
        kwargs["FriendlyName"] = friendly_name
        return self.create_instance(kwargs)

    def update(self, sid, **kwargs):
        """
        Update the :class:`TaskrouterWorker`
        
        :param str activity_sid: The activity_sid
        :param str attributes: The attributes
        :param str friendly_name: The friendly_name
        :param str sid: The sid
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`TaskrouterWorker`
        
        :param str sid: The sid
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`TaskrouterWorker` using an iterator
        
        :param str activity_name: The activity_name
        :param str activity_sid: The activity_sid
        :param str available: The available
        :param str friendly_name: The friendly_name
        :param str target_workers_expression: The target_workers_expression
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        """
        return super(TaskrouterWorkers, self).iter(**kwargs)
