from twilio.rest.taskrouter.workspace.task_queue import (
    TaskQueue as BaseTaskQueue,
    TaskQueues as BaseTaskQueues,
)
from twilio.rest.taskrouter.workspace.task_queue.\
    instance_statistics import StatisticsList


class TaskQueue(BaseTaskQueue):

    def load_subresources(self):
        super(TaskQueue, self).load_subresources()
        self.statistics = StatisticsList(
            self.uri,
            self.parent.auth,
            self.parent.timeout
        )


class TaskQueues(BaseTaskQueues):
    instance = TaskQueue
