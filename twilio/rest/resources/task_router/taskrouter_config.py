from .workflow_rule import WorkflowRule
from .workflow_ruletarget import WorkflowRuleTarget
class TaskRouterConfig:

   """
    TaskRouterConfig represents the filter and default_filter
    of a workflow configuration of taskrouter
   """

   def __init__(self, rules, defaultTarget):
        self.filters = rules
        self.default_filter = defaultTarget

   @property
   def filters(self):
        return self.filters

   @property
   def defaultFilter(self):
        return self.default_filter

   def __repr__(self):
        out = self.__dict__
        return out
