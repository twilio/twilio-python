r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TaskActionsList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskActionsList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param task_sid: The unique ID of the Task.

        :returns: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsList
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }

    def get(self):
        """
        Constructs a TaskActionsContext


        :returns: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsContext
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsContext
        """
        return TaskActionsContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __call__(self):
        """
        Constructs a TaskActionsContext


        :returns: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsContext
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsContext
        """
        return TaskActionsContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Preview.Understand.TaskActionsList>"


class TaskActionsInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskActionsInstance

        :returns: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "assistant_sid": payload.get("assistant_sid"),
            "task_sid": payload.get("task_sid"),
            "url": payload.get("url"),
            "data": payload.get("data"),
        }

        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._context: Optional[TaskActionsContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskActionsContext for this TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsContext
        """
        if self._context is None:
            self._context = TaskActionsContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                task_sid=self._solution["task_sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Field.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the parent Assistant.
        :rtype: str
        """
        return self._properties["assistant_sid"]

    @property
    def task_sid(self):
        """
        :returns: The unique ID of the Task.
        :rtype: str
        """
        return self._properties["task_sid"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    @property
    def data(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["data"]

    def fetch(self):
        """
        Fetch the TaskActionsInstance


        :returns: The fetched TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TaskActionsInstance


        :returns: The fetched TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """
        return await self._proxy.fetch_async()

    def update(self, actions=values.unset):
        """
        Update the TaskActionsInstance

        :param object actions: The JSON actions that instruct the Assistant how to perform this task.

        :returns: The updated TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """
        return self._proxy.update(
            actions=actions,
        )

    async def update_async(self, actions=values.unset):
        """
        Asynchronous coroutine to update the TaskActionsInstance

        :param object actions: The JSON actions that instruct the Assistant how to perform this task.

        :returns: The updated TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """
        return await self._proxy.update_async(
            actions=actions,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.TaskActionsInstance {}>".format(context)


class TaskActionsContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskActionsContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.
        :param task_sid: The unique ID of the Task.

        :returns: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsContext
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "task_sid": task_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{task_sid}/Actions".format(
            **self._solution
        )

    def fetch(self):
        """
        Fetch the TaskActionsInstance


        :returns: The fetched TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TaskActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TaskActionsInstance


        :returns: The fetched TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TaskActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def update(self, actions=values.unset):
        """
        Update the TaskActionsInstance

        :param object actions: The JSON actions that instruct the Assistant how to perform this task.

        :returns: The updated TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """
        data = values.of(
            {
                "Actions": serialize.object(actions),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    async def update_async(self, actions=values.unset):
        """
        Asynchronous coroutine to update the TaskActionsInstance

        :param object actions: The JSON actions that instruct the Assistant how to perform this task.

        :returns: The updated TaskActionsInstance
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsInstance
        """
        data = values.of(
            {
                "Actions": serialize.object(actions),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            task_sid=self._solution["task_sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.TaskActionsContext {}>".format(context)
