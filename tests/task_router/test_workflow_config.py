import unittest
import json

from mock import patch, Mock




from tests.tools import create_mock_json
from twilio.rest.resources.task_router.workflow_config import WorkflowConfig
from twilio.rest.resources.task_router.workflow_rule import WorkflowRule
from twilio.rest.resources.task_router.workflow_ruletarget import WorkflowRuleTarget

class WorkflowConfigTest(unittest.TestCase):
      def test_to_json(self):
          rules =[]
          ruleTargets=[]
          ruleTargets1=[]
          ruleTarget = WorkflowRuleTarget("WQeae4fc2f4db7f377c5d3758fb08b79b7","1==1",1,20)
          ruleTarget1 = WorkflowRuleTarget("WQ19ebe92fb33522f018b5a31d805d94da","1==1",1,210)
          ruleTargets.append(ruleTarget);
          ruleTargets1.append(ruleTarget1);
          rule = WorkflowRule("1==1",ruleTargets,"SomeQ")
          rules.append(rule)
          rule1 =  WorkflowRule("1==1",ruleTargets1,"SomeOtherQ")
          rules.append(rule1)
          deftarget = WorkflowRuleTarget("WQ9963154bf3122d0a0558f3763951d916","1==1",None,None)


          config = WorkflowConfig(rules,deftarget)
          self.assertEqual(self.is_json(config.toJson()),True)




      def test_from_Json(self):

          data="{\"task_routing\": {        \"filters\": [            {                \"targets\": [                    {                        \"queue\": \"WQec62de0e1148b8477f2e24579779c8b1\",                        \"expression\": \"task.language IN worker.languages\"                    }                ],                \"friendly_name\": \"Sales\",                \"expression\": \"type == \\\"sales\\\"\"            },            {                \"targets\": [                    {                        \"queue\": \"WQ2acd4c1a41ffadce5d1bac9e1ce2fa9f\",                        \"expression\": \"task.language IN worker.languages\"                    }                ],                \"friendly_name\": \"Marketing\",                \"expression\": \"type == \\\"marketing\\\"\"            },            {                \"targets\": [                    {                        \"queue\": \"WQe5eb317eb23500ade45087ea6522896c\",                        \"expression\": \"task.language IN worker.languages\"                    }                ],                \"friendly_name\": \"Support\",                \"expression\": \"type == \\\"support\\\"\"            }        ],        \"default_filter\": {            \"queue\": \"WQ05f810d2d130344fd56e3c91ece2e594\"        }    }}"
          config = WorkflowConfig.json2obj(data)
          self.assertEqual(len(config.task_routing.filters),3)
          self.assertEqual(len(config.task_routing.default_filter),1)

          
          
      def test_from_json2(self):
          data ="{    \"task_routing\": {        \"default_filter\": {            \"expression\": null,            \"priority\": null,            \"queue\": \"WQYYYYY\",            \"timeout\": null        },        \"filters\": [            {                \"expression\": \"1==1\",                \"friendly_name\": \"SomeQ\",                \"targets\": [                    {                        \"expression\": \"1==1\",                        \"priority\": 1,                        \"queue\": \"WQXXXX\",                        \"timeout\": 20                    }                ]            },            {                \"expression\": \"1==1\",                \"friendly_name\": \"SomeOtherQ\",                \"targets\": [                    {                        \"expression\": \"1==1\",                        \"priority\": 1,                        \"queue\": \"WQXXXX\",                        \"timeout\": 20                    }                ]            }        ]    }}"
          config = WorkflowConfig.json2obj(data)
          self.assertEqual(len(config.task_routing.filters),2)
          self.assertEqual(len(config.task_routing.default_filter),4)



      def is_json(self,myjson):
         try:
            json_object = json.loads(myjson)
         except ValueError, e:
            return False
         return True

