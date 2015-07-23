from .taskrouter_config import TaskRouterConfig
import json
from collections import namedtuple, Iterable, OrderedDict
import numpy as np
from twilio.rest.resources.task_router.workflow_rule import WorkflowRule


class WorkflowConfig:

    """
    WorkflowConfig represents the whole workflow config json which contains
    filters and default_filter.
    """

    def __init__(self, workflowRules, defaultTarget):
        #filters and default_filters
        self.task_routing = TaskRouterConfig(workflowRules, defaultTarget)


    @property
    def taskrouterConfig(self):
        return self.task_routing

    def toJson(self):
          return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)


    @staticmethod
    def json2obj(data):
       m=json.loads(data)
       return WorkflowConfig(m['task_routing']['filters'],m['task_routing']['default_filter'])
