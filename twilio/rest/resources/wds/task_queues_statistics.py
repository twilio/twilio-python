from .. import InstanceResource, ListResource


class TaskQueueStatistics(InstanceResource):
    """
    A TaskQueueStatistics resource
    """
    id_key = "task_queue_sid"


class TaskQueuesStatistics(ListResource):
    """ A list of TaskQueuesStatistics resources """

    name = "TaskQueues"
    instance = TaskQueueStatistics
    key = "task_queues_statistics"
