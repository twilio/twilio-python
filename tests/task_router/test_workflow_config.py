import unittest
import json

from twilio.task_router.workflow_config import WorkflowConfig
from twilio.task_router.workflow_rule import WorkflowRule
from twilio.task_router.workflow_ruletarget import WorkflowRuleTarget


class WorkflowConfigTest(unittest.TestCase):
        def test_to_json(self):
            rules = [
                WorkflowRule("1==1", [WorkflowRuleTarget("WQeae4fc2f4db7f377c5d3758fb08b79b7", "1==1", 1, 20)], "SomeQ"),
                WorkflowRule("1==1", [WorkflowRuleTarget("WQ19ebe92fb33522f018b5a31d805d94da", "1==1", 1, 210)], "SomeOtherQ")
            ]
            def_target = WorkflowRuleTarget("WQ9963154bf3122d0a0558f3763951d916", "1==1", None, None)
            config = WorkflowConfig(rules, def_target)
            self.assertEqual(True, self.is_json(config.to_json()))

        def test_from_json(self):

            data = {
                       'task_routing':
                       {
                           'filters': [
                               {
                                   'expression': 'type == "sales"',
                                   'friendly_name': 'Sales',
                                   'targets': [
                                       {
                                           'queue': 'WQec62de0e1148b8477f2e24579779c8b1',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               },
                               {
                                   'expression': 'type == "marketing"',
                                   'friendly_name': 'Marketing',
                                   'targets': [
                                       {
                                           'queue': 'WQ2acd4c1a41ffadce5d1bac9e1ce2fa9f',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               },
                               {
                                   'expression': 'type == "support"',
                                   'friendly_name': 'Support',
                                   'targets': [
                                       {
                                           'queue': 'WQe5eb317eb23500ade45087ea6522896c',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               }
                           ],
                           'default_filter':
                           {
                               'queue': 'WQ05f810d2d130344fd56e3c91ece2e594'
                           }
                       }
                   }

            config = WorkflowConfig.json2obj(json.dumps(data))
            self.assertEqual(3, len(config.task_routing.filters))
            self.assertEqual(1, len(config.task_routing.default_filter))

        def test_from_json2(self):

            data = {'task_routing': {'filters': [{'friendly_name': 'SomeQ', 'expression': '1==1', 'targets': [
                {'priority': 1, 'queue': 'WQXXXX', 'expression': '1==1', 'timeout': 20}]},
                                                  {'friendly_name': 'SomeOtherQ', 'expression': '1==1',
                                                   'targets': [
                                                       {'priority': 1, 'queue': 'WQXXXX', 'expression': '1==1',
                                                        'timeout': 20}]}],
                                      'default_filter': {'priority': None, 'queue': 'WQYYYYY', 'expression': None,
                                                         'timeout': None}}}
            config = WorkflowConfig.json2obj(json.dumps(data))
            self.assertEqual(2, len(config.task_routing.filters))
            self.assertEqual(4, len(config.task_routing.default_filter))

        def test_from_json_with_filter_friendly_name(self):
            data = {
                       'task_routing':
                       {
                           'filters': [
                               {
                                   'expression': 'type == "sales"',
                                   'filter_friendly_name': 'Sales',
                                   'targets': [
                                       {

                                           'queue': 'WQec62de0e1148b8477f2e24579779c8b1',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               },
                               {
                                   'expression': 'type == "marketing"',
                                   'filter_friendly_name': 'Marketing',
                                   'targets': [
                                       {
                                           'queue': 'WQ2acd4c1a41ffadce5d1bac9e1ce2fa9f',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               },
                               {
                                   'expression': 'type == "support"',
                                   'filter_friendly_name': 'Support',
                                   'targets': [
                                       {
                                           'queue': 'WQe5eb317eb23500ade45087ea6522896c',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               }
                           ],
                           'default_filter':
                           {
                               'queue': 'WQ05f810d2d130344fd56e3c91ece2e594'
                           }
                       }
                   }
            # marshal object
            config = WorkflowConfig.json2obj(json.dumps(data))
            self.assertEqual(3, len(config.task_routing.filters))
            self.assertEqual(1, len(config.task_routing.default_filter))

            # check that the configuration was marshaled to "friendly_name" and not "filter_friendly_name"
            expected_config_data = {
                                      "task_routing":
                                      {
                                          "default_filter":
                                          {
                                              "queue": "WQ05f810d2d130344fd56e3c91ece2e594"
                                          },
                                          "filters": [
                                              {
                                                  "expression": "type == \"sales\"",
                                                  "friendly_name": "Sales",
                                                  "targets": [
                                                      {
                                                          "expression": "task.language IN worker.languages",
                                                          "queue": "WQec62de0e1148b8477f2e24579779c8b1"
                                                      }
                                                  ]
                                              },
                                              {
                                                  "expression": "type == \"marketing\"",
                                                  "friendly_name": "Marketing",
                                                  "targets": [
                                                      {
                                                          "expression": "task.language IN worker.languages",
                                                          "queue": "WQ2acd4c1a41ffadce5d1bac9e1ce2fa9f"
                                                      }
                                                  ]
                                              },
                                              {
                                                  "expression": "type == \"support\"",
                                                  "friendly_name": "Support",
                                                  "targets": [
                                                      {
                                                          "expression": "task.language IN worker.languages",
                                                          "queue": "WQe5eb317eb23500ade45087ea6522896c"
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                   }

            expected_config_json = json.dumps(expected_config_data,
                          sort_keys=True,
                          indent=4)
            # check that marshaling back stays as "friendly_name"
            self.assertEqual(config.to_json(), expected_config_json)

        def test_from_json_with_both_filter_and_friendly_name(self):
            data = {
                       'task_routing':
                       {
                           'filters': [
                               {
                                   'expression': 'type == "sales"',
                                   'filter_friendly_name': "Sales",
                                   'friendly_name': 'Sales2',
                                   'targets': [
                                       {

                                           'queue': 'WQec62de0e1148b8477f2e24579779c8b1',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               },
                               {
                                   'expression': 'type == "marketing"',
                                   'filter_friendly_name': 'Marketing',
                                   'friendly_name': 'Marketing2',
                                   'targets': [
                                       {
                                           'queue': 'WQ2acd4c1a41ffadce5d1bac9e1ce2fa9f',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               },
                               {
                                   'expression': 'type == "support"',
                                   'filter_friendly_name': 'Support',
                                   'friendly_name': 'Support2',
                                   'targets': [
                                       {
                                           'queue': 'WQe5eb317eb23500ade45087ea6522896c',
                                           'expression': 'task.language IN worker.languages'
                                       }
                                   ]
                               }
                           ],
                           'default_filter':
                           {
                               'queue': 'WQ05f810d2d130344fd56e3c91ece2e594'
                           }
                       }
                   }
            # marshal object
            config = WorkflowConfig.json2obj(json.dumps(data))
            self.assertEqual(3, len(config.task_routing.filters))
            self.assertEqual(1, len(config.task_routing.default_filter))

            # check that the configuration was marshaled to "friendly_name" and not "filter_friendly_name"
            expected_config_data = {
                                      "task_routing":
                                      {
                                          "default_filter":
                                          {
                                              "queue": "WQ05f810d2d130344fd56e3c91ece2e594"
                                          },
                                          "filters": [
                                              {
                                                  "expression": "type == \"sales\"",
                                                  "friendly_name": "Sales",
                                                  "targets": [
                                                      {
                                                          "expression": "task.language IN worker.languages",
                                                          "queue": "WQec62de0e1148b8477f2e24579779c8b1"
                                                      }
                                                  ]
                                              },
                                              {
                                                  "expression": "type == \"marketing\"",
                                                  "friendly_name": "Marketing",
                                                  "targets": [
                                                      {
                                                          "expression": "task.language IN worker.languages",
                                                          "queue": "WQ2acd4c1a41ffadce5d1bac9e1ce2fa9f"
                                                      }
                                                  ]
                                              },
                                              {
                                                  "expression": "type == \"support\"",
                                                  "friendly_name": "Support",
                                                  "targets": [
                                                      {
                                                          "expression": "task.language IN worker.languages",
                                                          "queue": "WQe5eb317eb23500ade45087ea6522896c"
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                   }

            expected_config_json = json.dumps(expected_config_data,
                          sort_keys=True,
                          indent=4)
            # check that marshaling back stays as "friendly_name"
            self.assertEqual(config.to_json(), expected_config_json)

        def is_json(self, myjson):
            try:
                json.loads(myjson)
            except ValueError as e:
                print(e)
                return False
            return True
