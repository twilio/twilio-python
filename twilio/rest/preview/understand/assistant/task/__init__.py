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
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.understand.assistant.task.field import FieldList
from twilio.rest.preview.understand.assistant.task.sample import SampleList
from twilio.rest.preview.understand.assistant.task.task_actions import TaskActionsList
from twilio.rest.preview.understand.assistant.task.task_statistics import (
    TaskStatisticsList,
)


class TaskList(ListResource):
    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the TaskList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant.

        :returns: twilio.rest.preview.understand.assistant.task.TaskList
        :rtype: twilio.rest.preview.understand.assistant.task.TaskList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks".format(**self._solution)

    def create(
        self,
        unique_name,
        friendly_name=values.unset,
        actions=values.unset,
        actions_url=values.unset,
    ):
        """
        Create the TaskInstance

        :param str unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param str friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param object actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param str actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: The created TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "Actions": serialize.object(actions),
                "ActionsUrl": actions_url,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    async def create_async(
        self,
        unique_name,
        friendly_name=values.unset,
        actions=values.unset,
        actions_url=values.unset,
    ):
        """
        Asynchronously create the TaskInstance

        :param str unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param str friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param object actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param str actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: The created TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "Actions": serialize.object(actions),
                "ActionsUrl": actions_url,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams TaskInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.TaskInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams TaskInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.TaskInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists TaskInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.TaskInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists TaskInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.TaskInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of TaskInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TaskPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of TaskInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return TaskPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TaskInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TaskPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of TaskInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return TaskPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a TaskContext

        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.preview.understand.assistant.task.TaskContext
        :rtype: twilio.rest.preview.understand.assistant.task.TaskContext
        """
        return TaskContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a TaskContext

        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.preview.understand.assistant.task.TaskContext
        :rtype: twilio.rest.preview.understand.assistant.task.TaskContext
        """
        return TaskContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Preview.Understand.TaskList>"


class TaskPage(Page):
    def __init__(self, version, response, solution):
        """
        Initialize the TaskPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.understand.assistant.task.TaskPage
        :rtype: twilio.rest.preview.understand.assistant.task.TaskPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.understand.assistant.task.TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        return TaskInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Preview.Understand.TaskPage>"


class TaskInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, sid: Optional[str] = None):
        """
        Initialize the TaskInstance

        :returns: twilio.rest.preview.understand.assistant.task.TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "friendly_name": payload.get("friendly_name"),
            "links": payload.get("links"),
            "assistant_sid": payload.get("assistant_sid"),
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "actions_url": payload.get("actions_url"),
            "url": payload.get("url"),
        }

        self._context = None
        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid or self._properties["sid"],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskContext for this TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskContext
        """
        if self._context is None:
            self._context = TaskContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Task.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def friendly_name(self):
        """
        :returns: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def links(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["links"]

    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the Assistant.
        :rtype: str
        """
        return self._properties["assistant_sid"]

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def unique_name(self):
        """
        :returns: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def actions_url(self):
        """
        :returns: User-provided HTTP endpoint where from the assistant fetches actions
        :rtype: str
        """
        return self._properties["actions_url"]

    @property
    def url(self):
        """
        :returns:
        :rtype: str
        """
        return self._properties["url"]

    def delete(self):
        """
        Deletes the TaskInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the TaskInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the TaskInstance


        :returns: The fetched TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TaskInstance


        :returns: The fetched TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        actions=values.unset,
        actions_url=values.unset,
    ):
        """
        Update the TaskInstance

        :param str friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param str unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param object actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param str actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: The updated TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            unique_name=unique_name,
            actions=actions,
            actions_url=actions_url,
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        actions=values.unset,
        actions_url=values.unset,
    ):
        """
        Asynchronous coroutine to update the TaskInstance

        :param str friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param str unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param object actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param str actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: The updated TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            unique_name=unique_name,
            actions=actions,
            actions_url=actions_url,
        )

    @property
    def fields(self):
        """
        Access the fields

        :returns: twilio.rest.preview.understand.assistant.task.FieldList
        :rtype: twilio.rest.preview.understand.assistant.task.FieldList
        """
        return self._proxy.fields

    @property
    def samples(self):
        """
        Access the samples

        :returns: twilio.rest.preview.understand.assistant.task.SampleList
        :rtype: twilio.rest.preview.understand.assistant.task.SampleList
        """
        return self._proxy.samples

    @property
    def task_actions(self):
        """
        Access the task_actions

        :returns: twilio.rest.preview.understand.assistant.task.TaskActionsList
        :rtype: twilio.rest.preview.understand.assistant.task.TaskActionsList
        """
        return self._proxy.task_actions

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.preview.understand.assistant.task.TaskStatisticsList
        :rtype: twilio.rest.preview.understand.assistant.task.TaskStatisticsList
        """
        return self._proxy.statistics

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.TaskInstance {}>".format(context)


class TaskContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, sid: str):
        """
        Initialize the TaskContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant.
        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.preview.understand.assistant.task.TaskContext
        :rtype: twilio.rest.preview.understand.assistant.task.TaskContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{sid}".format(**self._solution)

        self._fields = None
        self._samples = None
        self._task_actions = None
        self._statistics = None

    def delete(self):
        """
        Deletes the TaskInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the TaskInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the TaskInstance


        :returns: The fetched TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TaskInstance


        :returns: The fetched TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        actions=values.unset,
        actions_url=values.unset,
    ):
        """
        Update the TaskInstance

        :param str friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param str unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param object actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param str actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: The updated TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Actions": serialize.object(actions),
                "ActionsUrl": actions_url,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name=values.unset,
        unique_name=values.unset,
        actions=values.unset,
        actions_url=values.unset,
    ):
        """
        Asynchronous coroutine to update the TaskInstance

        :param str friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param str unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param object actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param str actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: The updated TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Actions": serialize.object(actions),
                "ActionsUrl": actions_url,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    @property
    def fields(self):
        """
        Access the fields

        :returns: twilio.rest.preview.understand.assistant.task.FieldList
        :rtype: twilio.rest.preview.understand.assistant.task.FieldList
        """
        if self._fields is None:
            self._fields = FieldList(
                self._version,
                self._solution["assistant_sid"],
                self._solution["sid"],
            )
        return self._fields

    @property
    def samples(self):
        """
        Access the samples

        :returns: twilio.rest.preview.understand.assistant.task.SampleList
        :rtype: twilio.rest.preview.understand.assistant.task.SampleList
        """
        if self._samples is None:
            self._samples = SampleList(
                self._version,
                self._solution["assistant_sid"],
                self._solution["sid"],
            )
        return self._samples

    @property
    def task_actions(self):
        """
        Access the task_actions

        :returns: twilio.rest.preview.understand.assistant.task.TaskActionsList
        :rtype: twilio.rest.preview.understand.assistant.task.TaskActionsList
        """
        if self._task_actions is None:
            self._task_actions = TaskActionsList(
                self._version,
                self._solution["assistant_sid"],
                self._solution["sid"],
            )
        return self._task_actions

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.preview.understand.assistant.task.TaskStatisticsList
        :rtype: twilio.rest.preview.understand.assistant.task.TaskStatisticsList
        """
        if self._statistics is None:
            self._statistics = TaskStatisticsList(
                self._version,
                self._solution["assistant_sid"],
                self._solution["sid"],
            )
        return self._statistics

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.TaskContext {}>".format(context)
