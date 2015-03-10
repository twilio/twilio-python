.. module:: twilio.rest.resources.task_router

========================================
:mod:`twilio.rest.resources.task_router`
========================================


Workspaces
>>>>>>>>>>

.. autoclass:: Workspaces
   :members:
   :exclude-members: instance

.. autoclass:: Workspace

Workflows
>>>>>>>>>

.. autoclass:: Workflows
   :members:
   :exclude-members: instance

.. autoclass:: Workflow

Activities
>>>>>>>>>>

.. autoclass:: Activities
   :members:
   :exclude-members: instance

.. autoclass:: Activity
    .. attribute:: sid

        The unique ID for this Activity.

    .. attribute:: account_sid

        The unique ID of the Account that owns this Activity.

    .. attribute:: workspace_sid

        The unique ID of the :class:`Workspace` that owns this Activity.

    .. attribute:: friendly_name

        A human-readable name for the Activity, such as 'on-call', 'break',
        'email', etc. These names will be used to calculate and expose
        statistics about workers, and give you visibility into the state of
        each of your workers.

    .. attribute:: available

        Boolean value indicating whether the worker should be eligible to
        receive a Task when they occupy this Activity. For example, in an
        activity called 'On Call', the worker would be unavailable to receive
        additional Task assignments.

    .. attribute:: date_created

        The date this Activity was created, given as UTC in ISO 8601 format.

    .. attribute:: date_updated

        The date this Activity was last updated, given as UTC in ISO 8601
        format.

Workers
>>>>>>>>>>

.. autoclass:: Workers
   :members:
   :exclude-members: instance

.. autoclass:: Worker

TaskQueues
>>>>>>>>>>

.. autoclass:: TaskQueues
   :members:
   :exclude-members: instance

.. autoclass:: TaskQueue

Tasks
>>>>>>>>>>

.. autoclass:: Tasks
   :members:
   :exclude-members: instance

.. autoclass:: Task

Events
>>>>>>>>>>

.. autoclass:: Events
   :members:
   :exclude-members: instance

.. autoclass:: Event
