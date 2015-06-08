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

    workspace = client.workflows(WORKSPACE_SID).create(
        friendly_name="Incoming Call Flow",
        assignment_callback_url="https://example.com/callback",
        fallback_assignment_callback_url="https://example.com/callback2",
        configuration=CONFIG
    )
    print workspace.sid


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
