from twilio.rest.taskrouter.workspace.worker import (
    Worker as BaseWorker,
    Workers as BaseWorkers,
)
from twilio.rest.taskrouter.workspace.worker.worker_statistics import (
    WorkerStatistics,
    WorkerStatisticsList
)


class Worker(BaseWorker):

    def load_subresources(self):
        super(Worker, self).load_subresources()
        self.statistics = WorkerStatisticsList(
            self.uri,
            self.parent.auth,
            self.parent.timeout
        )


class Workers(BaseWorkers):
    instance = Worker
