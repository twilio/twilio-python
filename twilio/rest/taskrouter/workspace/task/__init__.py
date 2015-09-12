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
from twilio.rest.taskrouter.workspace.task.reservation import (
    Reservation,
    Reservations,
)
from twilio.rest.resources.base import NextGenListResource


class Task(NextGenInstanceResource):
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
    subresources = [
        Reservations
    ]

    def load(self, *args, **kwargs):
        super(Task, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Update the instance
        
        :param str attributes: The attributes
        :param str priority: The priority
        :param str reason: The reason
        :param task.status assignment_status: The assignment_status
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Task`
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


class Tasks(NextGenListResource):
    name = "Tasks"
    mount_name = "tasks"
    key = "tasks"
    instance = Task

    def __init__(self, *args, **kwargs):
        super(Tasks, self).__init__(*args, **kwargs)

    def get(self, sid):
        """
        Get a placeholder for an instance resource.
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Task`
        :returns: A placeholder for a :class:`Task` resource
        """
        return self.get_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`Task`
        
        :param str attributes: The attributes
        :param str priority: The priority
        :param str reason: The reason
        :param str sid: The sid
        :param task.status assignment_status: The assignment_status
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Task`
        """
        return self.update_instance(sid, kwargs)

    def delete(self, sid):
        """
        Delete the :class:`Task`
        
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`DeleteQuery`
        :returns: A DeleteQuery when executed returns True iff the deletion is successful
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        Retrieve a collection of :class:`Task`
        
        :param str priority: The priority
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        :param str workflow_name: The workflow_name
        :param str workflow_sid: The workflow_sid
        :param task.status assignment_status: The assignment_status
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Task`
        """
        return self.get_instances(kwargs)

    def create(self, attributes, workflow_sid, **kwargs):
        """
        Create a new :class:`Task`
        
        :param str attributes: The attributes
        :param str priority: The priority
        :param str timeout: The timeout
        :param str workflow_sid: The workflow_sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Task`
        """
        kwargs["Attributes"] = attributes
        kwargs["WorkflowSid"] = workflow_sid
        return self.create_instance(kwargs)

    def iter(self, **kwargs):
        """
        Return all instances of :class:`Task` using an iterator
        
        :param str priority: The priority
        :param str task_queue_name: The task_queue_name
        :param str task_queue_sid: The task_queue_sid
        :param str workflow_name: The workflow_name
        :param str workflow_sid: The workflow_sid
        :param task.status assignment_status: The assignment_status
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Task`
        """
        return super(Tasks, self).iter(**kwargs)
