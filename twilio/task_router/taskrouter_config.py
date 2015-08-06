from .workflow_rule import WorkflowRule
from .workflow_ruletarget import WorkflowRuleTarget


class TaskRouterConfig:

    """
        TaskRouterConfig represents the filter and default_filter
        of a workflow configuration of taskrouter
    """

    def __init__(self, rules, default_target):
        self.filters = rules
        self.default_filter = default_target

    def __repr__(self):
        return self.__dict__
