from .. import NextGenInstanceResource, NextGenListResource
from .statistics import Statistics


class TaskQueue(NextGenInstanceResource):
    """
    A TaskQueue resource
    """
    subresources = [
        Statistics,
    ]

    def delete(self):
        """
        Delete a task queue.
        """
        return self.parent.delete_instance(self.name)

    def update(self, **kwargs):
        """
        Update a task queue.
        """
        return self.parent.update_instance(self.name, kwargs)


class TaskQueues(NextGenListResource):
    """ A list of TaskQueue resources """

    name = "TaskQueues"
    instance = TaskQueue
    key = "task_queues"

    def __init__(self, base_uri, auth, timeout, **kwargs):
        super(TaskQueues, self).__init__(base_uri, auth, timeout, **kwargs)
        self.statistics = Statistics(self.uri, auth, **kwargs)

    def create(self, friendly_name, assignment_activity_sid,
               reservation_activity_sid, **kwargs):
        """
        Create a TaskQueue.

        :param friendly_name: Human readable description of this TaskQueue (for
            example "Support - Tier 1", "Sales" or "Escalation")
        :param assignment_activity_sid: ActivitySID to assign workers once a
            task is assigned for them.
        :param reservation_activity_sid: ActivitySID to assign workers once a
            task is reserved for them.
        """
        kwargs['friendly_name'] = friendly_name
        kwargs['assignment_activity_sid'] = assignment_activity_sid
        kwargs['reservation_activity_sid'] = reservation_activity_sid
        return self.create_instance(kwargs)

    def delete(self, sid):
        """
        Delete the given task queue
        """
        return self.delete_instance(sid)

    def update(self, sid, **kwargs):
        """
        Update a :class:`TaskQueue` with the given parameters.

        All the parameters are describe above in :meth:`create`
        """
        return self.update_instance(sid, kwargs)
