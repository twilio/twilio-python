from .workflow_rule import WorkflowRule
from .workflow_ruletarget import WorkflowRuleTarget


class TaskRouterConfig:

    """
        TaskRouterConfig represents the filter and default_filter
        of a workflow configuration of taskrouter
    """

    def __init__(self, rules, default_target):
        self.filters = rules
        if default_target is not None:
            self.default_filter = default_target

        if self.filters is not None:
            for rule in self.filters:
                if not isinstance(rule, WorkflowRule):
                    filter_friendly_name = rule.pop('filter_friendly_name', None)
                    if filter_friendly_name is not None:
                        rule['friendly_name'] = filter_friendly_name

    def __repr__(self):
        return self.__dict__
