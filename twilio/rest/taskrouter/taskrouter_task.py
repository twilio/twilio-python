from twilio.rest.resources import NextGenInstanceResource
from twilio.rest.resources import NextGenListResource


class TaskrouterTask(NextGenInstanceResource):
    """
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: age
    
        The age
    
    .. attribute:: assignment_status
    
        The assignment_status
    
    .. attribute:: attributes
    
        The attributes
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: priority
    
        The priority
    
    .. attribute:: reason
    
        The reason
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: task_queue_sid
    
        The task_queue_sid
    
    .. attribute:: timeout
    
        The timeout
    
    .. attribute:: workflow_sid
    
        The workflow_sid
    
    .. attribute:: workspace_sid
    
        The workspace_sid
    """
    id_key = "sid"
    ASSIGNED = "assigned"
    CANCELED = "canceled"
    PENDING = "pending"
    RESERVED = "reserved"

    def update(self, **kwargs):
        """ Update the instance """
        return self.update_instance(**kwargs)

    def delete(self):
        """ Delete the instance """
        return self.delete_instance()


class TaskrouterTasks(NextGenListResource):
    name = "Tasks"
    key = "taskrouter_tasks"
    instance = TaskrouterTask

    def __init__(self, *args, **kwargs):
        super(TaskrouterTasks, self).__init__(*args, **kwargs)

    def update(self, sid, **kwargs):
        """
        Update the :class:`TaskrouterTask`
        
        :param str attributes: The attributes
        :param str priority: The priority
        :param str reason: The reason
        :param str sid: The sid
        :param taskrouter_task.status assignment_status: The assignment_status
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`TaskrouterTask`
        
        :param str sid: The sid
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`TaskrouterTask`
        
        :param str priority: The priority
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        :param str workflow_name: The workflow_name
        :param str workflow_sid: The workflow_sid
        :param taskrouter_task.status assignment_status: The assignment_status
        """
        return self.get_instances(kwargs)

    def create(self, attributes, workflow_sid, **kwargs):
        """
        Create a new :class:`TaskrouterTask`
        
        :param str attributes: The attributes
        :param str priority: The priority
        :param str timeout: The timeout
        :param str workflow_sid: The workflow_sid
        """
        kwargs["Attributes"] = attributes
        kwargs["WorkflowSid"] = workflow_sid
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`TaskrouterTask` using an iterator
        
        :param str priority: The priority
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        :param str workflow_name: The workflow_name
        :param str workflow_sid: The workflow_sid
        :param taskrouter_task.status assignment_status: The assignment_status
        """
        return super(TaskrouterTasks, self).iter(**kwargs)
