from twilio.rest.taskrouter.task_queue import (
    TaskQueue as BaseTaskQueue,
    TaskQueues as BaseTaskQueues,
)
from twilio.rest.taskrouter.task_queue.task_queue_statistics import TaskQueueStatisticsList


class TaskQueue(BaseTaskQueue):

    def load_subresources(self):
        super(TaskQueue, self).load_subresources()
        self.statistics = TaskQueueStatisticsList(
            self.uri,
            self.parent.auth,
            self.parent.timeout
        )


class TaskQueues(BaseTaskQueues):
    instance = TaskQueue
