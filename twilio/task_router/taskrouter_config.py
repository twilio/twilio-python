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
        self.workflow_rules = []

        for rule in rules:
            if isinstance(rule, WorkflowRule):
                self.workflow_rules.append(rule)
            else:
                try:
                    name = rule['friendly_name']
                except KeyError:
                    name = rule['filter_friendly_name']
                self.workflow_rules.append(
                    WorkflowRule(rule['expression'], rule['targets'], name))

    def __repr__(self):

        return str({
            'workflow_rules': self.workflow_rules,
            'default': self.default_filter,
            'rules': self.rules
        })
