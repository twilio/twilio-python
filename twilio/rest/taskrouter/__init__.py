from twilio.rest.taskrouter import TaskrouterBase
from warnings import warn


class Taskrouter(TaskrouterBase):

    @property
    def workspaces(self):
        warn('workspaces() is deprecated. Use v1.workspaces() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.workspaces
