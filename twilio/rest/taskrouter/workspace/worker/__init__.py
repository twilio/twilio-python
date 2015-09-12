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
from twilio.rest.taskrouter.workspace.worker.worker_statistics import (
    Statistics,
    StatisticsList,
)
from twilio.rest.resources.base import NextGenListResource
from twilio.rest.taskrouter.workspace.worker.workers_statistics import (
    StatisticsList as WorkersStatistics_StatisticsList,
    Statistics as WorkersStatistics_Statistics,
)


class Worker(NextGenInstanceResource):
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
    subresources = [
        StatisticsList
    ]

    def load(self, *args, **kwargs):
        super(Worker, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_status_changed") and self.date_status_changed:
            self.date_status_changed = parse_iso_date(self.date_status_changed)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str activity_sid: The activity_sid
        :param str attributes: The attributes
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Worker`
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


class Workers(NextGenListResource):
    name = "Workers"
    mount_name = "workers"
    key = "workers"
    instance = Worker

    def __init__(self, *args, **kwargs):
        super(Workers, self).__init__(*args, **kwargs)
        self.statistics = WorkersStatistics_StatisticsList(*args, **kwargs)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Worker`
        
        :param str activity_name: The activity_name
        :param str activity_sid: The activity_sid
        :param str available: The available
        :param str friendly_name: The friendly_name
        :param str target_workers_expression: The target_workers_expression
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Worker`
        """
        return self.get_instances(kwargs)

    def create(self, friendly_name, **kwargs):
        """
        Create a new :class:`Worker`
        
        :param str activity_sid: The activity_sid
        :param str attributes: The attributes
        :param str friendly_name: The friendly_name
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Worker`
        """
        kwargs["FriendlyName"] = friendly_name
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Worker`
        :returns: A placeholder for a :class:`Worker` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Worker`
        
        :param str activity_sid: The activity_sid
        :param str attributes: The attributes
        :param str friendly_name: The friendly_name
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Worker`
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Worker`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Worker` using an iterator
        
        :param str activity_name: The activity_name
        :param str activity_sid: The activity_sid
        :param str available: The available
        :param str friendly_name: The friendly_name
        :param str target_workers_expression: The target_workers_expression
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Worker`
        """
        return super(Workers, self).iter(**kwargs)
