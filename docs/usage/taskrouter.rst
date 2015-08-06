.. module:: twilio.rest.resources.task_router

==========
TaskRouter
==========

Twilio TaskRouter is a system for distributing tasks such as phone calls,
leads, support tickets, and other work items to the people and processes that
can best handle them.

For more information, see the `TaskRouter documentation
<https://www.twilio.com/docs/taskrouter>_`.


Creating a Workspace
--------------------

A Workspace is a container for your Tasks, Workers, TaskQueues, Workflows and
Activities. Each of these items exists within a single Workspace and will not
be shared across Workspaces.

The following code will create a new :class:`Workspace` resource and print
its unique ID.

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    workspace = client.workspaces.create(
        friendly_name="Customer Support",
        template="FIFO",  # Sets up default activities and a FIFO TaskQueue
    )
    print workspace.sid

..

The following code will get an instance of an existing :class:`workspace` resource

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    workspace = client.workspaces.get(WORKSPACE_SID)
    print workspace.friendly_name
..

The following code will get the list of all existing :class:`workspace` resources

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    for workspace in  client.workspaces.list()
        print workspace.friendly_name
..

The following code will create a update an existing :class:`Workspace` resource

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    workspace = client.workspaces.update(
        WORKSPACE_SID,
        friendly_name='Test Workspace',
        event_callback_uri="http://www.example.com",
        template='FIFO')

..
The following code will delete an existing :class:`workspace` resource

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    client.workspaces.delete(WORKSPACE_SID)
..



Workflows
---------

Workflows control how tasks will be prioritized and routed into TaskQueues, and
how Tasks should escalate in priority or move across queues over time.
Workflows are described in a simple JSON format and can be modified through the
REST API or through the account portal.

The following code will create a new :class:`Workflow` resource and print its
unique ID:

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    # Some JSON to configure the Workflow. See the documentation at
    # http://www.twilio.com/docs/taskrouter for more details.
    CONFIG = """
    {
       "task_routing":{
          "filters":[
             {
                "friendly_name":"Gold Tickets",
                "expression":"customer_value == 'Gold' AND type == 'ticket'",
                "targets":[
                   {
                      "task_queue_sid":"WQ0123456789abcdef0123456789abcdef",
                      "priority":"2"
                   }
                ]
             }
          ],
          "default_filter":{
             "task_queue_sid":"WQabcdef01234567890123456789abcdef"
          }
       }
    }
    """

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    workflow = client.workflows(WORKSPACE_SID).create(
        friendly_name="Incoming Call Flow",
        assignment_callback_url="https://example.com/callback",
        fallback_assignment_callback_url="https://example.com/callback2",
        configuration=CONFIG
    )
    print workflow.sid

..

The following code will get a instance of an existing :class:`workflow` resource

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    workflow = client.workflows(WORKSPACE_SID).get(WORKFLOW_SID)
    print workflow.friendly_name

..



The following code will get a list of all existing :class:`workflow` resources

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    for workflow in client.workflows(WORKSPACE_SID).list()
        print workflow.friendly_name

..

The following code will update an existing :class:`workflow` resource

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    # Some JSON to configure the Workflow. See the documentation at
    # http://www.twilio.com/docs/taskrouter for more details.
    CONFIG = """
    {
       "task_routing":{
          "filters":[
             {
                "friendly_name":"Gold Tickets",
                "expression":"customer_value == 'Gold' AND type == 'ticket'",
                "targets":[
                   {
                      "task_queue_sid":"WQ0123456789abcdef0123456789abcdef",
                      "priority":"2"
                   }
                ]
             },
             {
                "targets": [
                    {
                        "queue": "WQ2acd4c1a41ffadce5d1bac9e1ce2fa9f",
                        "priority": "1"
                    }
                ],
                "friendly_name": "Marketing",
                "expression": "type == 'marketing'"
            }
          ],
          "default_filter":{
             "task_queue_sid":"WQabcdef01234567890123456789abcdef"
          }
       }
    }
    """

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    workflow = client.workflows(WORKSPACE_SID).update(
        WORKFLOW_SID,
        friendly_name="Incoming Call Flow",
        assignment_callback_url="https://example.com/callback",
        fallback_assignment_callback_url="https://example.com/callback2",
        configuration=CONFIG
    )
    print workflow.sid

..

The following code will delete an existing :class:`Workflow`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    client.workflows(WORKSPACE_SID).delete(
        WORKFLOW_SID
    )


..


Activities
----------

Activities describe the current status of your Workers, which determines
whether they are eligible to receive task assignments. Workers are always set
to a single Activity.

To create a new :class:`Activity`:

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    activity = client.activities(WORKSPACE_SID).create(
        friendly_name="Coffee Break",
        available=False,  # Whether workers are available to handle tasks during this activity
    )

..

To get an existing :class:`activity` resource

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    activity = client.activities(WORKSPACE_SID).get(ACTIVITY_SID)
    print activity.friendly_name

..

To get a list of existing :class:`activity` resources

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    for activity in client.activities(WORKSPACE_SID).list()
        print activity.friendly_name

..

To update an existing :class:`Activity`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    activity = client.activities(WORKSPACE_SID).update(
        ACTIVITY_SID,
        friendly_name="Coffee Break",
        available=True,
    )

..

To delete an existing :class:`Activity`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    activity = client.activities(WORKSPACE_SID).delete(
        ACTIVITY_SID
    )

..

Workers
-------

Workers represent an entity that is able to perform tasks, such as an agent
working in a call center, or a salesperson handling leads.

To create a new :class:`Worker`:

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    worker = client.workers(WORKSPACE_SID).create(
        friendly_name="Jamie",
        attributes="""{
        "phone": "+14155551234",
        "languages": ["EN", "ES"]
    }
    """
    )
    print worker.sid

..

To get an existing :class:`worker` instance

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    worker = client.workers(WORKSPACE_SID).get(WORKER_SID)
    print worker_friendly_name;
..


To get an existing :class:`worker` list

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    for worker in client.workers(WORKSPACE_SID).list()
        print worker_friendly_name;
..


To update an existing :class:`Worker`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    worker = client.workers(WORKSPACE_SID).update(
        WORKER_SID,
        friendly_name="Jamie Howe",
        attributes="""{
        "phone": "+14155551234",
        "languages": ["EN", "ES","DE"]
    }
    """
    )
    print worker.sid

..

To delete an existing :class:`Worker`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    client.workers(WORKSPACE_SID).delete(
        WORKER_SID
    )

..

TaskQueues
----------

TaskQueues are the resource you use to categorize Tasks and describe which
Workers are eligible to handle those Tasks. As your Workflows process Tasks,
those Tasks will pass through one or more TaskQueues until the Task is assigned
and accepted by an eligible Worker.

To create a new :class:`TaskQueue`:

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    queue = client.task_queues(WORKSPACE_SID).create(
        friendly_name="Sales",
        # The Activity to assign workers when a task is reserved for them
        reservation_activity_sid="WA11111111111",
        # The Activity to assign workers when a task is assigned to them
        assignment_activity_sid="WA222222222222",
    )
    print queue.sid

..

To get an existing :class`TaskQueue` instance

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    queue = client.task_queues(WORKSPACE_SID).get(TASKQUEUE_SID)
    print queue.sid

..



To get an existing :class`TaskQueue` list

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    for queue in client.task_queues(WORKSPACE_SID).list()
        print queue.sid

..


To update an existing :class:`TaskQueue`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    queue = client.task_queues(WORKSPACE_SID).update(
        TASKQUEUE_SID,
        friendly_name="Sales+Pre-Sales",
        # The Activity to assign workers when a task is reserved for them
        reservation_activity_sid="WA11111111111",
        # The Activity to assign workers when a task is assigned to them
        assignment_activity_sid="WA222222222222",
    )
    print queue.sid

..

To delete an existing :class:`TaskQueue`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    queue = client.task_queues(WORKSPACE_SID).delete(
        TASKQUEUE_SID
    )
    print queue.sid

..


Tasks
-----

A Task instance resource represents a single item of work waiting to be
processed.

To create a new :class:`Task` via the REST API:

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"
    WORKFLOW_SID = "WWXXXXXXXXXXXXXX"
    # Some JSON containing attributes for this task. User-defined.
    TASK_ATTRIBUTES = """{
         "type": "call",
         "contact": "+15558675309",
         "customer-value": "gold",
         "task-reason": "support",
         "callSid": "CA42ed11..."
    }"""


    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    task = client.tasks(WORKSPACE_SID).create(
        attributes=TASK_ATTRIBUTES,
        assignment_status='pending',
        workflow_sid=WORKFLOW_SID
    )
    print task.sid
..

To get an existing :class:`Task` instance

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"
    WORKFLOW_SID = "WWXXXXXXXXXXXXXX"
    # Some JSON containing attributes for this task. User-defined.
    TASK_ATTRIBUTES = """{
         "type": "call",
         "contact": "+2014068777",
         "customer-value": "gold",
         "task-reason": "support",
         "callSid": "CA42ed11..."
    }"""


    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    task = client.tasks(WORKSPACE_SID).delete(TASK_SID)
    print task.attributes
..


To get an existing :class:`Task` list

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"
    WORKFLOW_SID = "WWXXXXXXXXXXXXXX"
    # Some JSON containing attributes for this task. User-defined.
    TASK_ATTRIBUTES = """{
         "type": "call",
         "contact": "+2014068777",
         "customer-value": "gold",
         "task-reason": "support",
         "callSid": "CA42ed11..."
    }"""


    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    for task in client.tasks(WORKSPACE_SID).list()
        print task.attributes
..

To update an existing  :class:`Task`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"
    WORKFLOW_SID = "WWXXXXXXXXXXXXXX"
    # Some JSON containing attributes for this task. User-defined.
    TASK_ATTRIBUTES = """{
         "type": "call",
         "contact": "+2014068777",
         "customer-value": "gold",
         "task-reason": "support",
         "callSid": "CA42ed11..."
    }"""


    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    task = client.tasks(WORKSPACE_SID).update(
        TASK_SID,
        attributes=TASK_ATTRIBUTES,
        assignment_status='pending',
        workflow_sid=WORKFLOW_SID
    )
    print task.sid
..

To delete an existing :class:`Task`

.. code-block:: python

    from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"
    WORKFLOW_SID = "WWXXXXXXXXXXXXXX"
    # Some JSON containing attributes for this task. User-defined.
    TASK_ATTRIBUTES = """{
         "type": "call",
         "contact": "+2014068777",
         "customer-value": "gold",
         "task-reason": "support",
         "callSid": "CA42ed11..."
    }"""


    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)
    client.tasks(WORKSPACE_SID).delete(
        TASK_SID
    )

..


Using Workflow builder helper classes to create a :class:`Workflow` resource.

.. code-block:: python

   from twilio.rest import TwilioTaskRouterClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    # See previous examples to create a Workspace
    WORKSPACE_SID = "WSZZZZZZZZZZZZZZ"

    rules = [
         WorkflowRule("1==1", [WorkflowRuleTarget("WQeae4fc2f4db7f377c5d3758fb08b79b7", "1==1", 1, 20)],"SomeQ"),
         WorkflowRule("1==1", [WorkflowRuleTarget("WQ19ebe92fb33522f018b5a31d805d94da", "1==1", 1, 210)], "SomeOtherQ")
    ]
    default_target = WorkflowRuleTarget("WQ9963154bf3122d0a0558f3763951d916", "1==1", None, None)
    config = WorkflowConfig(rules, default_target)
    print config.to_json()

    client = TwilioTaskRouterClient(ACCOUNT_SID, AUTH_TOKEN)

    workflow = client.workflows(WORKSPACE_SID).create(
        friendly_name= "Incoming Call Flow",
        assignment_callback_url= "https://example.com/callback",
        fallback_assignment_callback_url= "https://example.com/callback2",
        configuration= config.to_json()
    )

    print workflow.sid



..