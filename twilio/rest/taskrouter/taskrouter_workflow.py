from twilio.rest.resources import NextGenInstanceResource
from twilio.rest.resources import NextGenListResource


class TaskrouterWorkflow(NextGenInstanceResource):
    """
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: assignment_callback_url
    
        The assignment_callback_url
    
    .. attribute:: configuration
    
        The configuration
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: fallback_assignment_callback_url
    
        The fallback_assignment_callback_url
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: task_reservation_timeout
    
        The task_reservation_timeout
    
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


class TaskrouterWorkflows(NextGenListResource):
    name = "Workflows"
    key = "taskrouter_workflows"
    instance = TaskrouterWorkflow

    def __init__(self, *args, **kwargs):
        super(TaskrouterWorkflows, self).__init__(*args, **kwargs)

    def update(self, sid, **kwargs):
        """
        Update the :class:`TaskrouterWorkflow`
        
        :param str assignment_callback_url: The assignment_callback_url
        :param str configuration: The configuration
        :param str fallback_assignment_callback_url: The
            fallback_assignment_callback_url
        :param str friendly_name: The friendly_name
        :param str sid: The sid
        :param str task_reservation_timeout: The task_reservation_timeout
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`TaskrouterWorkflow`
        
        :param str sid: The sid
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`TaskrouterWorkflow`
        
        :param str friendly_name: The friendly_name
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, configuration, assignment_callback_url,
               **kwargs):
        """
        Create a new :class:`TaskrouterWorkflow`
        
        :param str assignment_callback_url: The assignment_callback_url
        :param str configuration: The configuration
        :param str fallback_assignment_callback_url: The
            fallback_assignment_callback_url
        :param str friendly_name: The friendly_name
        :param str task_reservation_timeout: The task_reservation_timeout
        """
        kwargs["FriendlyName"] = friendly_name
        kwargs["Configuration"] = configuration
        kwargs["AssignmentCallbackUrl"] = assignment_callback_url
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`TaskrouterWorkflow` using an iterator
        
        :param str friendly_name: The friendly_name
        """
        return super(TaskrouterWorkflows, self).iter(**kwargs)
