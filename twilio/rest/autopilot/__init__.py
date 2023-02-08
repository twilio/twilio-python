from twilio.rest.autopilot import AutopilotBase
from warnings import warn


class Autopilot(AutopilotBase):

    @property
    def assistants(self):
        warn('assistants is deprecated. Use v1.assistants instead.', DeprecationWarning, stacklevel=2)
        return self.v1.assistants

    @property
    def restore_assistant(self):
        warn('restore_assistant is deprecated. Use v1.restore_assistant instead.', DeprecationWarning, stacklevel=2)
        return self.v1.restore_assistant
