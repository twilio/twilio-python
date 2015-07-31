from twilio.rest.resources import NextGenInstanceResource
from twilio.rest.resources import NextGenListResource


class TaskrouterWorkspace(NextGenInstanceResource):
    """
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: date_created
    
        The date_created
    
    .. attribute:: date_updated
    
        The date_updated
    
    .. attribute:: default_activity_name
    
        The default_activity_name
    
    .. attribute:: default_activity_sid
    
        The default_activity_sid
    
    .. attribute:: event_callback_url
    
        The event_callback_url
    
    .. attribute:: friendly_name
    
        The friendly_name
    
    .. attribute:: sid
    
        The sid
    
    .. attribute:: timeout_activity_name
    
        The timeout_activity_name
    
    .. attribute:: timeout_activity_sid
    
        The timeout_activity_sid
    """
    id_key = "sid"

    def update(self, **kwargs):
        """ Update the instance """
        return self.update_instance(**kwargs)


class TaskrouterWorkspaces(NextGenListResource):
    name = "Workspaces"
    key = "taskrouter_workspaces"
    instance = TaskrouterWorkspace

    def __init__(self, *args, **kwargs):
        super(TaskrouterWorkspaces, self).__init__(*args, **kwargs)

    def update(self, sid, **kwargs):
        """
        Update the :class:`TaskrouterWorkspace`
        
        :param str default_activity_sid: The default_activity_sid
        :param str event_callback_url: The event_callback_url
        :param str friendly_name: The friendly_name
        :param str timeout_activity_sid: The timeout_activity_sid
        """
        return self.update_instance(sid, kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`TaskrouterWorkspace`
        
        :param str friendly_name: The friendly_name
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Create a new :class:`TaskrouterWorkspace`
        
        :param str event_callback_url: The event_callback_url
        :param str friendly_name: The friendly_name
        :param str template: The template
        """
        kwargs["FriendlyName"] = friendly_name
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`TaskrouterWorkspace` using an iterator
        
        :param str friendly_name: The friendly_name
        """
        return super(TaskrouterWorkspaces, self).iter(**kwargs)
