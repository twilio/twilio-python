from .workflow_rule import WorkflowRule
import json


class TaskRouterConfig:

    """
        TaskRouterConfig represents the filter and default_filter
        of a workflow configuration of taskrouter
    """

    def __init__(self, rules, default_target):

        self.default_filter = default_target
        workflow_rules = []

        for rule in rules:
            if isinstance(rule, WorkflowRule):
                workflow_rules.append(rule)
            else:
                try:
                    name = rule['friendly_name']
                except KeyError:
                    name = rule['filter_friendly_name']
                workflow_rules.append(
                    WorkflowRule(rule['expression'], rule['targets'], name))
        self.filters = workflow_rules

    def to_json(self):

        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)

    @staticmethod
    def json2obj(data):

        m = json.loads(data)
        return TaskRouterConfig(m['filters'], m['default_filter'])
