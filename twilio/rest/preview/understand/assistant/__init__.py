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


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.understand.assistant.assistant_fallback_actions import (
    AssistantFallbackActionsList,
)
from twilio.rest.preview.understand.assistant.assistant_initiation_actions import (
    AssistantInitiationActionsList,
)
from twilio.rest.preview.understand.assistant.dialogue import DialogueList
from twilio.rest.preview.understand.assistant.field_type import FieldTypeList
from twilio.rest.preview.understand.assistant.model_build import ModelBuildList
from twilio.rest.preview.understand.assistant.query import QueryList
from twilio.rest.preview.understand.assistant.style_sheet import StyleSheetList
from twilio.rest.preview.understand.assistant.task import TaskList


class AssistantInstance(InstanceResource):

    """
    :ivar account_sid: The unique ID of the Account that created this Assistant.
    :ivar date_created: The date that this resource was created
    :ivar date_updated: The date that this resource was last updated
    :ivar friendly_name: A text description for the Assistant. It is non-unique and can up to 255 characters long.
    :ivar latest_model_build_sid: The unique ID (Sid) of the latest model build. Null if no model has been built.
    :ivar links:
    :ivar log_queries: A boolean that specifies whether queries should be logged for 30 days further training. If false, no queries will be stored, if true, queries will be stored for 30 days and deleted thereafter.
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. You can use the unique name in the URL path. Unique up to 64 characters long.
    :ivar url:
    :ivar callback_url: A user-provided URL to send event callbacks to.
    :ivar callback_events: Space-separated list of callback events that will trigger callbacks.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.latest_model_build_sid: Optional[str] = payload.get(
            "latest_model_build_sid"
        )
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.log_queries: Optional[bool] = payload.get("log_queries")
        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.url: Optional[str] = payload.get("url")
        self.callback_url: Optional[str] = payload.get("callback_url")
        self.callback_events: Optional[str] = payload.get("callback_events")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[AssistantContext] = None

    @property
    def _proxy(self) -> "AssistantContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssistantContext for this AssistantInstance
        """
        if self._context is None:
            self._context = AssistantContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the AssistantInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AssistantInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AssistantInstance":
        """
        Fetch the AssistantInstance


        :returns: The fetched AssistantInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AssistantInstance":
        """
        Asynchronous coroutine to fetch the AssistantInstance


        :returns: The fetched AssistantInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        log_queries: Union[bool, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_events: Union[str, object] = values.unset,
        fallback_actions: Union[object, object] = values.unset,
        initiation_actions: Union[object, object] = values.unset,
        style_sheet: Union[object, object] = values.unset,
    ) -> "AssistantInstance":
        """
        Update the AssistantInstance

        :param friendly_name: A text description for the Assistant. It is non-unique and can up to 255 characters long.
        :param log_queries: A boolean that specifies whether queries should be logged for 30 days further training. If false, no queries will be stored, if true, queries will be stored for 30 days and deleted thereafter. Defaults to true if no value is provided.
        :param unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param callback_url: A user-provided URL to send event callbacks to.
        :param callback_events: Space-separated list of callback events that will trigger callbacks.
        :param fallback_actions: The JSON actions to be executed when the user's input is not recognized as matching any Task.
        :param initiation_actions: The JSON actions to be executed on inbound phone calls when the Assistant has to say something first.
        :param style_sheet: The JSON object that holds the style sheet for the assistant

        :returns: The updated AssistantInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            log_queries=log_queries,
            unique_name=unique_name,
            callback_url=callback_url,
            callback_events=callback_events,
            fallback_actions=fallback_actions,
            initiation_actions=initiation_actions,
            style_sheet=style_sheet,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        log_queries: Union[bool, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_events: Union[str, object] = values.unset,
        fallback_actions: Union[object, object] = values.unset,
        initiation_actions: Union[object, object] = values.unset,
        style_sheet: Union[object, object] = values.unset,
    ) -> "AssistantInstance":
        """
        Asynchronous coroutine to update the AssistantInstance

        :param friendly_name: A text description for the Assistant. It is non-unique and can up to 255 characters long.
        :param log_queries: A boolean that specifies whether queries should be logged for 30 days further training. If false, no queries will be stored, if true, queries will be stored for 30 days and deleted thereafter. Defaults to true if no value is provided.
        :param unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param callback_url: A user-provided URL to send event callbacks to.
        :param callback_events: Space-separated list of callback events that will trigger callbacks.
        :param fallback_actions: The JSON actions to be executed when the user's input is not recognized as matching any Task.
        :param initiation_actions: The JSON actions to be executed on inbound phone calls when the Assistant has to say something first.
        :param style_sheet: The JSON object that holds the style sheet for the assistant

        :returns: The updated AssistantInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            log_queries=log_queries,
            unique_name=unique_name,
            callback_url=callback_url,
            callback_events=callback_events,
            fallback_actions=fallback_actions,
            initiation_actions=initiation_actions,
            style_sheet=style_sheet,
        )

    @property
    def assistant_fallback_actions(self) -> AssistantFallbackActionsList:
        """
        Access the assistant_fallback_actions
        """
        return self._proxy.assistant_fallback_actions

    @property
    def assistant_initiation_actions(self) -> AssistantInitiationActionsList:
        """
        Access the assistant_initiation_actions
        """
        return self._proxy.assistant_initiation_actions

    @property
    def dialogues(self) -> DialogueList:
        """
        Access the dialogues
        """
        return self._proxy.dialogues

    @property
    def field_types(self) -> FieldTypeList:
        """
        Access the field_types
        """
        return self._proxy.field_types

    @property
    def model_builds(self) -> ModelBuildList:
        """
        Access the model_builds
        """
        return self._proxy.model_builds

    @property
    def queries(self) -> QueryList:
        """
        Access the queries
        """
        return self._proxy.queries

    @property
    def style_sheet(self) -> StyleSheetList:
        """
        Access the style_sheet
        """
        return self._proxy.style_sheet

    @property
    def tasks(self) -> TaskList:
        """
        Access the tasks
        """
        return self._proxy.tasks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.AssistantInstance {}>".format(context)


class AssistantContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the AssistantContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Assistants/{sid}".format(**self._solution)

        self._assistant_fallback_actions: Optional[AssistantFallbackActionsList] = None
        self._assistant_initiation_actions: Optional[
            AssistantInitiationActionsList
        ] = None
        self._dialogues: Optional[DialogueList] = None
        self._field_types: Optional[FieldTypeList] = None
        self._model_builds: Optional[ModelBuildList] = None
        self._queries: Optional[QueryList] = None
        self._style_sheet: Optional[StyleSheetList] = None
        self._tasks: Optional[TaskList] = None

    def delete(self) -> bool:
        """
        Deletes the AssistantInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AssistantInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AssistantInstance:
        """
        Fetch the AssistantInstance


        :returns: The fetched AssistantInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AssistantInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AssistantInstance:
        """
        Asynchronous coroutine to fetch the AssistantInstance


        :returns: The fetched AssistantInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AssistantInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        log_queries: Union[bool, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_events: Union[str, object] = values.unset,
        fallback_actions: Union[object, object] = values.unset,
        initiation_actions: Union[object, object] = values.unset,
        style_sheet: Union[object, object] = values.unset,
    ) -> AssistantInstance:
        """
        Update the AssistantInstance

        :param friendly_name: A text description for the Assistant. It is non-unique and can up to 255 characters long.
        :param log_queries: A boolean that specifies whether queries should be logged for 30 days further training. If false, no queries will be stored, if true, queries will be stored for 30 days and deleted thereafter. Defaults to true if no value is provided.
        :param unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param callback_url: A user-provided URL to send event callbacks to.
        :param callback_events: Space-separated list of callback events that will trigger callbacks.
        :param fallback_actions: The JSON actions to be executed when the user's input is not recognized as matching any Task.
        :param initiation_actions: The JSON actions to be executed on inbound phone calls when the Assistant has to say something first.
        :param style_sheet: The JSON object that holds the style sheet for the assistant

        :returns: The updated AssistantInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "LogQueries": log_queries,
                "UniqueName": unique_name,
                "CallbackUrl": callback_url,
                "CallbackEvents": callback_events,
                "FallbackActions": serialize.object(fallback_actions),
                "InitiationActions": serialize.object(initiation_actions),
                "StyleSheet": serialize.object(style_sheet),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssistantInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        log_queries: Union[bool, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_events: Union[str, object] = values.unset,
        fallback_actions: Union[object, object] = values.unset,
        initiation_actions: Union[object, object] = values.unset,
        style_sheet: Union[object, object] = values.unset,
    ) -> AssistantInstance:
        """
        Asynchronous coroutine to update the AssistantInstance

        :param friendly_name: A text description for the Assistant. It is non-unique and can up to 255 characters long.
        :param log_queries: A boolean that specifies whether queries should be logged for 30 days further training. If false, no queries will be stored, if true, queries will be stored for 30 days and deleted thereafter. Defaults to true if no value is provided.
        :param unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param callback_url: A user-provided URL to send event callbacks to.
        :param callback_events: Space-separated list of callback events that will trigger callbacks.
        :param fallback_actions: The JSON actions to be executed when the user's input is not recognized as matching any Task.
        :param initiation_actions: The JSON actions to be executed on inbound phone calls when the Assistant has to say something first.
        :param style_sheet: The JSON object that holds the style sheet for the assistant

        :returns: The updated AssistantInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "LogQueries": log_queries,
                "UniqueName": unique_name,
                "CallbackUrl": callback_url,
                "CallbackEvents": callback_events,
                "FallbackActions": serialize.object(fallback_actions),
                "InitiationActions": serialize.object(initiation_actions),
                "StyleSheet": serialize.object(style_sheet),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssistantInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def assistant_fallback_actions(self) -> AssistantFallbackActionsList:
        """
        Access the assistant_fallback_actions
        """
        if self._assistant_fallback_actions is None:
            self._assistant_fallback_actions = AssistantFallbackActionsList(
                self._version,
                self._solution["sid"],
            )
        return self._assistant_fallback_actions

    @property
    def assistant_initiation_actions(self) -> AssistantInitiationActionsList:
        """
        Access the assistant_initiation_actions
        """
        if self._assistant_initiation_actions is None:
            self._assistant_initiation_actions = AssistantInitiationActionsList(
                self._version,
                self._solution["sid"],
            )
        return self._assistant_initiation_actions

    @property
    def dialogues(self) -> DialogueList:
        """
        Access the dialogues
        """
        if self._dialogues is None:
            self._dialogues = DialogueList(
                self._version,
                self._solution["sid"],
            )
        return self._dialogues

    @property
    def field_types(self) -> FieldTypeList:
        """
        Access the field_types
        """
        if self._field_types is None:
            self._field_types = FieldTypeList(
                self._version,
                self._solution["sid"],
            )
        return self._field_types

    @property
    def model_builds(self) -> ModelBuildList:
        """
        Access the model_builds
        """
        if self._model_builds is None:
            self._model_builds = ModelBuildList(
                self._version,
                self._solution["sid"],
            )
        return self._model_builds

    @property
    def queries(self) -> QueryList:
        """
        Access the queries
        """
        if self._queries is None:
            self._queries = QueryList(
                self._version,
                self._solution["sid"],
            )
        return self._queries

    @property
    def style_sheet(self) -> StyleSheetList:
        """
        Access the style_sheet
        """
        if self._style_sheet is None:
            self._style_sheet = StyleSheetList(
                self._version,
                self._solution["sid"],
            )
        return self._style_sheet

    @property
    def tasks(self) -> TaskList:
        """
        Access the tasks
        """
        if self._tasks is None:
            self._tasks = TaskList(
                self._version,
                self._solution["sid"],
            )
        return self._tasks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.AssistantContext {}>".format(context)


class AssistantPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AssistantInstance:
        """
        Build an instance of AssistantInstance

        :param payload: Payload response from the API
        """
        return AssistantInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Understand.AssistantPage>"


class AssistantList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AssistantList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Assistants"

    def create(
        self,
        friendly_name: Union[str, object] = values.unset,
        log_queries: Union[bool, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_events: Union[str, object] = values.unset,
        fallback_actions: Union[object, object] = values.unset,
        initiation_actions: Union[object, object] = values.unset,
        style_sheet: Union[object, object] = values.unset,
    ) -> AssistantInstance:
        """
        Create the AssistantInstance

        :param friendly_name: A text description for the Assistant. It is non-unique and can up to 255 characters long.
        :param log_queries: A boolean that specifies whether queries should be logged for 30 days further training. If false, no queries will be stored, if true, queries will be stored for 30 days and deleted thereafter. Defaults to true if no value is provided.
        :param unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param callback_url: A user-provided URL to send event callbacks to.
        :param callback_events: Space-separated list of callback events that will trigger callbacks.
        :param fallback_actions: The JSON actions to be executed when the user's input is not recognized as matching any Task.
        :param initiation_actions: The JSON actions to be executed on inbound phone calls when the Assistant has to say something first.
        :param style_sheet: The JSON object that holds the style sheet for the assistant

        :returns: The created AssistantInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "LogQueries": log_queries,
                "UniqueName": unique_name,
                "CallbackUrl": callback_url,
                "CallbackEvents": callback_events,
                "FallbackActions": serialize.object(fallback_actions),
                "InitiationActions": serialize.object(initiation_actions),
                "StyleSheet": serialize.object(style_sheet),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssistantInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        log_queries: Union[bool, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        callback_events: Union[str, object] = values.unset,
        fallback_actions: Union[object, object] = values.unset,
        initiation_actions: Union[object, object] = values.unset,
        style_sheet: Union[object, object] = values.unset,
    ) -> AssistantInstance:
        """
        Asynchronously create the AssistantInstance

        :param friendly_name: A text description for the Assistant. It is non-unique and can up to 255 characters long.
        :param log_queries: A boolean that specifies whether queries should be logged for 30 days further training. If false, no queries will be stored, if true, queries will be stored for 30 days and deleted thereafter. Defaults to true if no value is provided.
        :param unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param callback_url: A user-provided URL to send event callbacks to.
        :param callback_events: Space-separated list of callback events that will trigger callbacks.
        :param fallback_actions: The JSON actions to be executed when the user's input is not recognized as matching any Task.
        :param initiation_actions: The JSON actions to be executed on inbound phone calls when the Assistant has to say something first.
        :param style_sheet: The JSON object that holds the style sheet for the assistant

        :returns: The created AssistantInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "LogQueries": log_queries,
                "UniqueName": unique_name,
                "CallbackUrl": callback_url,
                "CallbackEvents": callback_events,
                "FallbackActions": serialize.object(fallback_actions),
                "InitiationActions": serialize.object(initiation_actions),
                "StyleSheet": serialize.object(style_sheet),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssistantInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssistantInstance]:
        """
        Streams AssistantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssistantInstance]:
        """
        Asynchronously streams AssistantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssistantInstance]:
        """
        Lists AssistantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssistantInstance]:
        """
        Asynchronously lists AssistantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> AssistantPage:
        """
        Retrieve a single page of AssistantInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssistantInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AssistantPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> AssistantPage:
        """
        Asynchronously retrieve a single page of AssistantInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssistantInstance
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
        return AssistantPage(self._version, response)

    def get_page(self, target_url: str) -> AssistantPage:
        """
        Retrieve a specific page of AssistantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssistantInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AssistantPage(self._version, response)

    async def get_page_async(self, target_url: str) -> AssistantPage:
        """
        Asynchronously retrieve a specific page of AssistantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssistantInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AssistantPage(self._version, response)

    def get(self, sid: str) -> AssistantContext:
        """
        Constructs a AssistantContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return AssistantContext(self._version, sid=sid)

    def __call__(self, sid: str) -> AssistantContext:
        """
        Constructs a AssistantContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return AssistantContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Understand.AssistantList>"
