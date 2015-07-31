from twilio.rest.resources import NextGenInstanceResource
from twilio.rest.resources import NextGenListResource


class TaskrouterActivity(NextGenInstanceResource):
    """
    
    .. attribute:: account_sid
    
        The account_sid
    
    .. attribute:: available
    
        The available
    
    .. attribute:: date_created
    
        The date_created
    
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


class TaskrouterActivities(NextGenListResource):
    name = "Activities"
    key = "taskrouter_activities"
    instance = TaskrouterActivity

    def __init__(self, *args, **kwargs):
        super(TaskrouterActivities, self).__init__(*args, **kwargs)

    def update(self, sid, friendly_name, **kwargs):
        """
        Update the :class:`TaskrouterActivity`
        
        :param str friendly_name: The friendly_name
        """
        kwargs["FriendlyName"] = friendly_name
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """ Delete the :class:`TaskrouterActivity` """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`TaskrouterActivity`
        
        :param str available: The available
        :param str friendly_name: The friendly_name
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Create a new :class:`TaskrouterActivity`
        
        :param bool available: The available
        :param str friendly_name: The friendly_name
        """
        kwargs["FriendlyName"] = friendly_name
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`TaskrouterActivity` using an iterator
        
        :param str available: The available
        :param str friendly_name: The friendly_name
        """
        return super(TaskrouterActivities, self).iter(**kwargs)
