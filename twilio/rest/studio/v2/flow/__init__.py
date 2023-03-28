r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
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
from twilio.rest.studio.v2.flow.execution import ExecutionList
from twilio.rest.studio.v2.flow.flow_revision import FlowRevisionList
from twilio.rest.studio.v2.flow.flow_test_user import FlowTestUserList


class FlowInstance(InstanceResource):
    class Status(object):
        DRAFT = "draft"
        PUBLISHED = "published"

    """
    :ivar sid: The unique string that we created to identify the Flow resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flow resource.
    :ivar friendly_name: The string that you assigned to describe the Flow.
    :ivar definition: JSON representation of flow definition.
    :ivar status: 
    :ivar revision: The latest revision number of the Flow's definition.
    :ivar commit_message: Description of change made in the revision.
    :ivar valid: Boolean if the flow definition is valid.
    :ivar errors: List of error in the flow definition.
    :ivar warnings: List of warnings in the flow definition.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar webhook_url: 
    :ivar url: The absolute URL of the resource.
    :ivar links: The URLs of the Flow's nested resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.definition: Optional[Dict[str, object]] = payload.get("definition")
        self.status: Optional["FlowInstance.Status"] = payload.get("status")
        self.revision: Optional[int] = deserialize.integer(payload.get("revision"))
        self.commit_message: Optional[str] = payload.get("commit_message")
        self.valid: Optional[bool] = payload.get("valid")
        self.errors: Optional[List[object]] = payload.get("errors")
        self.warnings: Optional[List[object]] = payload.get("warnings")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.webhook_url: Optional[str] = payload.get("webhook_url")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[FlowContext] = None

    @property
    def _proxy(self) -> "FlowContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FlowContext for this FlowInstance
        """
        if self._context is None:
            self._context = FlowContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the FlowInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FlowInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "FlowInstance":
        """
        Fetch the FlowInstance


        :returns: The fetched FlowInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FlowInstance":
        """
        Asynchronous coroutine to fetch the FlowInstance


        :returns: The fetched FlowInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        status: "FlowInstance.Status",
        friendly_name: Union[str, object] = values.unset,
        definition: Union[object, object] = values.unset,
        commit_message: Union[str, object] = values.unset,
    ) -> "FlowInstance":
        """
        Update the FlowInstance

        :param status:
        :param friendly_name: The string that you assigned to describe the Flow.
        :param definition: JSON representation of flow definition.
        :param commit_message: Description of change made in the revision.

        :returns: The updated FlowInstance
        """
        return self._proxy.update(
            status=status,
            friendly_name=friendly_name,
            definition=definition,
            commit_message=commit_message,
        )

    async def update_async(
        self,
        status: "FlowInstance.Status",
        friendly_name: Union[str, object] = values.unset,
        definition: Union[object, object] = values.unset,
        commit_message: Union[str, object] = values.unset,
    ) -> "FlowInstance":
        """
        Asynchronous coroutine to update the FlowInstance

        :param status:
        :param friendly_name: The string that you assigned to describe the Flow.
        :param definition: JSON representation of flow definition.
        :param commit_message: Description of change made in the revision.

        :returns: The updated FlowInstance
        """
        return await self._proxy.update_async(
            status=status,
            friendly_name=friendly_name,
            definition=definition,
            commit_message=commit_message,
        )

    @property
    def executions(self) -> ExecutionList:
        """
        Access the executions
        """
        return self._proxy.executions

    @property
    def revisions(self) -> FlowRevisionList:
        """
        Access the revisions
        """
        return self._proxy.revisions

    @property
    def test_users(self) -> FlowTestUserList:
        """
        Access the test_users
        """
        return self._proxy.test_users

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V2.FlowInstance {}>".format(context)


class FlowContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the FlowContext

        :param version: Version that contains the resource
        :param sid: The SID of the Flow resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Flows/{sid}".format(**self._solution)

        self._executions: Optional[ExecutionList] = None
        self._revisions: Optional[FlowRevisionList] = None
        self._test_users: Optional[FlowTestUserList] = None

    def delete(self) -> bool:
        """
        Deletes the FlowInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FlowInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> FlowInstance:
        """
        Fetch the FlowInstance


        :returns: The fetched FlowInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FlowInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> FlowInstance:
        """
        Asynchronous coroutine to fetch the FlowInstance


        :returns: The fetched FlowInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FlowInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        status: "FlowInstance.Status",
        friendly_name: Union[str, object] = values.unset,
        definition: Union[object, object] = values.unset,
        commit_message: Union[str, object] = values.unset,
    ) -> FlowInstance:
        """
        Update the FlowInstance

        :param status:
        :param friendly_name: The string that you assigned to describe the Flow.
        :param definition: JSON representation of flow definition.
        :param commit_message: Description of change made in the revision.

        :returns: The updated FlowInstance
        """
        data = values.of(
            {
                "Status": status,
                "FriendlyName": friendly_name,
                "Definition": serialize.object(definition),
                "CommitMessage": commit_message,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FlowInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        status: "FlowInstance.Status",
        friendly_name: Union[str, object] = values.unset,
        definition: Union[object, object] = values.unset,
        commit_message: Union[str, object] = values.unset,
    ) -> FlowInstance:
        """
        Asynchronous coroutine to update the FlowInstance

        :param status:
        :param friendly_name: The string that you assigned to describe the Flow.
        :param definition: JSON representation of flow definition.
        :param commit_message: Description of change made in the revision.

        :returns: The updated FlowInstance
        """
        data = values.of(
            {
                "Status": status,
                "FriendlyName": friendly_name,
                "Definition": serialize.object(definition),
                "CommitMessage": commit_message,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FlowInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def executions(self) -> ExecutionList:
        """
        Access the executions
        """
        if self._executions is None:
            self._executions = ExecutionList(
                self._version,
                self._solution["sid"],
            )
        return self._executions

    @property
    def revisions(self) -> FlowRevisionList:
        """
        Access the revisions
        """
        if self._revisions is None:
            self._revisions = FlowRevisionList(
                self._version,
                self._solution["sid"],
            )
        return self._revisions

    @property
    def test_users(self) -> FlowTestUserList:
        """
        Access the test_users
        """
        if self._test_users is None:
            self._test_users = FlowTestUserList(
                self._version,
                self._solution["sid"],
            )
        return self._test_users

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Studio.V2.FlowContext {}>".format(context)


class FlowPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> FlowInstance:
        """
        Build an instance of FlowInstance

        :param payload: Payload response from the API
        """
        return FlowInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V2.FlowPage>"


class FlowList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the FlowList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Flows"

    def create(
        self,
        friendly_name: str,
        status: "FlowInstance.Status",
        definition: object,
        commit_message: Union[str, object] = values.unset,
    ) -> FlowInstance:
        """
        Create the FlowInstance

        :param friendly_name: The string that you assigned to describe the Flow.
        :param status:
        :param definition: JSON representation of flow definition.
        :param commit_message: Description of change made in the revision.

        :returns: The created FlowInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Status": status,
                "Definition": serialize.object(definition),
                "CommitMessage": commit_message,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FlowInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name: str,
        status: "FlowInstance.Status",
        definition: object,
        commit_message: Union[str, object] = values.unset,
    ) -> FlowInstance:
        """
        Asynchronously create the FlowInstance

        :param friendly_name: The string that you assigned to describe the Flow.
        :param status:
        :param definition: JSON representation of flow definition.
        :param commit_message: Description of change made in the revision.

        :returns: The created FlowInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Status": status,
                "Definition": serialize.object(definition),
                "CommitMessage": commit_message,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FlowInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FlowInstance]:
        """
        Streams FlowInstance records from the API as a generator stream.
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
    ) -> List[FlowInstance]:
        """
        Asynchronously streams FlowInstance records from the API as a generator stream.
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
    ) -> List[FlowInstance]:
        """
        Lists FlowInstance records from the API as a list.
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
    ) -> List[FlowInstance]:
        """
        Asynchronously lists FlowInstance records from the API as a list.
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
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> FlowPage:
        """
        Retrieve a single page of FlowInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FlowInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FlowPage(self._version, response)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> FlowPage:
        """
        Asynchronously retrieve a single page of FlowInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FlowInstance
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
        return FlowPage(self._version, response)

    def get_page(self, target_url: str) -> FlowPage:
        """
        Retrieve a specific page of FlowInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FlowInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FlowPage(self._version, response)

    async def get_page_async(self, target_url: str) -> FlowPage:
        """
        Asynchronously retrieve a specific page of FlowInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FlowInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FlowPage(self._version, response)

    def get(self, sid: str) -> FlowContext:
        """
        Constructs a FlowContext

        :param sid: The SID of the Flow resource to fetch.
        """
        return FlowContext(self._version, sid=sid)

    def __call__(self, sid: str) -> FlowContext:
        """
        Constructs a FlowContext

        :param sid: The SID of the Flow resource to fetch.
        """
        return FlowContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V2.FlowList>"
