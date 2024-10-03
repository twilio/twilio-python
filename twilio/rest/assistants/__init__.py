from warnings import warn

from twilio.rest.assistants import AssistantsBase
from twilio.rest.assistants.v1.assistant import AssistantList
from twilio.rest.assistants.v1.knowledge import KnowledgeList
from twilio.rest.assistants.v1.policy import PolicyList
from twilio.rest.assistants.v1.session import SessionList
from twilio.rest.assistants.v1.tool import ToolList


class Assistants(AssistantsBase):

    @property
    def assistants(self) -> AssistantList:
        warn(
            "assistants is deprecated. Use v1.assistants instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.assistants

    @property
    def knowledge(self) -> KnowledgeList:
        warn(
            "knowledge is deprecated. Use v1.knowledge instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.knowledge

    @property
    def policies(self) -> PolicyList:
        warn(
            "policies is deprecated. Use v1.policies instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.policies

    @property
    def sessions(self) -> SessionList:
        warn(
            "sessions is deprecated. Use v1.sessions instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.sessions

    @property
    def tools(self) -> ToolList:
        warn(
            "tools is deprecated. Use v1.tools instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.tools
