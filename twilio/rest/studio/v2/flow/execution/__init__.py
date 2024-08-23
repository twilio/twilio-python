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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.studio.v2.flow.execution.execution_context import ExecutionContextList
from twilio.rest.studio.v2.flow.execution.execution_step import ExecutionStepList


class ExecutionInstance(InstanceResource):

    class Status:
        ACTIVE = "active"
        ENDED = "ended"

    """
    :ivar sid: The unique string that we created to identify the Execution resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Execution resource.
    :ivar flow_sid: The SID of the Flow.
    :ivar contact_channel_address: The phone number, SIP address or Client identifier that triggered the Execution. Phone numbers are in E.164 format (e.g. +16175551212). SIP addresses are formatted as `name@company.com`. Client identifiers are formatted `client:name`.
    :ivar context: The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data that your widgets can access as variables in configuration fields or in text areas as variable substitution.
    :ivar status: 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the resource.
    :ivar links: The URLs of nested resources.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        flow_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.flow_sid: Optional[str] = payload.get("flow_sid")
        self.contact_channel_address: Optional[str] = payload.get(
            "contact_channel_address"
        )
        self.context: Optional[Dict[str, object]] = payload.get("context")
        self.status: Optional["ExecutionInstance.Status"] = payload.get("status")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "flow_sid": flow_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ExecutionContext] = None

    @property
    def _proxy(self) -> "ExecutionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ExecutionContext for this ExecutionInstance
        """
        if self._context is None:
            self._context = ExecutionContext(
                self._version,
                flow_sid=self._solution["flow_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ExecutionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ExecutionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ExecutionInstance":
        """
        Fetch the ExecutionInstance


        :returns: The fetched ExecutionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ExecutionInstance":
        """
        Asynchronous coroutine to fetch the ExecutionInstance


        :returns: The fetched ExecutionInstance
        """
        return await self._proxy.fetch_async()

    def update(self, status: "ExecutionInstance.Status") -> "ExecutionInstance":
        """
        Update the ExecutionInstance

        :param status:

        :returns: The updated ExecutionInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(
        self, status: "ExecutionInstance.Status"
    ) -> "ExecutionInstance":
        """
        Asynchronous coroutine to update the ExecutionInstance

        :param status:

        :returns: The updated ExecutionInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    @property
    def execution_context(self) -> ExecutionContextList:
        """
        Access the execution_context
        """
        return self._proxy.execution_context

    @property
    def steps(self) -> ExecutionStepList:
        """
        Access the steps
        """
        return self._proxy.steps

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Studio.V2.ExecutionInstance {context}>"


class ExecutionContext(InstanceContext):

    def __init__(self, version: Version, flow_sid: str, sid: str):
        """
        Initialize the ExecutionContext

        :param version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Execution resources to update.
        :param sid: The SID of the Execution resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "flow_sid": flow_sid,
            "sid": sid,
        }
        self._uri = "/Flows/{flow_sid}/Executions/{sid}".format(**self._solution)

        self._execution_context: Optional[ExecutionContextList] = None
        self._steps: Optional[ExecutionStepList] = None

    def delete(self) -> bool:
        """
        Deletes the ExecutionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ExecutionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ExecutionInstance:
        """
        Fetch the ExecutionInstance


        :returns: The fetched ExecutionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ExecutionInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ExecutionInstance:
        """
        Asynchronous coroutine to fetch the ExecutionInstance


        :returns: The fetched ExecutionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ExecutionInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            sid=self._solution["sid"],
        )

    def update(self, status: "ExecutionInstance.Status") -> ExecutionInstance:
        """
        Update the ExecutionInstance

        :param status:

        :returns: The updated ExecutionInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExecutionInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, status: "ExecutionInstance.Status"
    ) -> ExecutionInstance:
        """
        Asynchronous coroutine to update the ExecutionInstance

        :param status:

        :returns: The updated ExecutionInstance
        """
        data = values.of(
            {
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ExecutionInstance(
            self._version,
            payload,
            flow_sid=self._solution["flow_sid"],
            sid=self._solution["sid"],
        )

    @property
    def execution_context(self) -> ExecutionContextList:
        """
        Access the execution_context
        """
        if self._execution_context is None:
            self._execution_context = ExecutionContextList(
                self._version,
                self._solution["flow_sid"],
                self._solution["sid"],
            )
        return self._execution_context

    @property
    def steps(self) -> ExecutionStepList:
        """
        Access the steps
        """
        if self._steps is None:
            self._steps = ExecutionStepList(
                self._version,
                self._solution["flow_sid"],
                self._solution["sid"],
            )
        return self._steps

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Studio.V2.ExecutionContext {context}>"


class ExecutionPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ExecutionInstance:
        """
        Build an instance of ExecutionInstance

        :param payload: Payload response from the API
        """
        return ExecutionInstance(
            self._version, payload, flow_sid=self._solution["flow_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V2.ExecutionPage>"


class ExecutionList(ListResource):

    def __init__(self, version: Version, flow_sid: str):
        """
        Initialize the ExecutionList

        :param version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Execution resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "flow_sid": flow_sid,
        }
        self._uri = "/Flows/{flow_sid}/Executions".format(**self._solution)

    def create(
        self, to: str, from_: str, parameters: Union[object, object] = values.unset
    ) -> ExecutionInstance:
        """
        Create the ExecutionInstance

        :param to: The Contact phone number to start a Studio Flow Execution, available as variable `{{contact.channel.address}}`.
        :param from_: The Twilio phone number to send messages or initiate calls from during the Flow's Execution. Available as variable `{{flow.channel.address}}`. For SMS, this can also be a Messaging Service SID.
        :param parameters: JSON data that will be added to the Flow's context and that can be accessed as variables inside your Flow. For example, if you pass in `Parameters={\\\"name\\\":\\\"Zeke\\\"}`, a widget in your Flow can reference the variable `{{flow.data.name}}`, which returns \\\"Zeke\\\". Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode the JSON string.

        :returns: The created ExecutionInstance
        """

        data = values.of(
            {
                "To": to,
                "From": from_,
                "Parameters": serialize.object(parameters),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ExecutionInstance(
            self._version, payload, flow_sid=self._solution["flow_sid"]
        )

    async def create_async(
        self, to: str, from_: str, parameters: Union[object, object] = values.unset
    ) -> ExecutionInstance:
        """
        Asynchronously create the ExecutionInstance

        :param to: The Contact phone number to start a Studio Flow Execution, available as variable `{{contact.channel.address}}`.
        :param from_: The Twilio phone number to send messages or initiate calls from during the Flow's Execution. Available as variable `{{flow.channel.address}}`. For SMS, this can also be a Messaging Service SID.
        :param parameters: JSON data that will be added to the Flow's context and that can be accessed as variables inside your Flow. For example, if you pass in `Parameters={\\\"name\\\":\\\"Zeke\\\"}`, a widget in your Flow can reference the variable `{{flow.data.name}}`, which returns \\\"Zeke\\\". Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode the JSON string.

        :returns: The created ExecutionInstance
        """

        data = values.of(
            {
                "To": to,
                "From": from_,
                "Parameters": serialize.object(parameters),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ExecutionInstance(
            self._version, payload, flow_sid=self._solution["flow_sid"]
        )

    def stream(
        self,
        date_created_from: Union[datetime, object] = values.unset,
        date_created_to: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ExecutionInstance]:
        """
        Streams ExecutionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param datetime date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        date_created_from: Union[datetime, object] = values.unset,
        date_created_to: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ExecutionInstance]:
        """
        Asynchronously streams ExecutionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param datetime date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        date_created_from: Union[datetime, object] = values.unset,
        date_created_to: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ExecutionInstance]:
        """
        Lists ExecutionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param datetime date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                date_created_from=date_created_from,
                date_created_to=date_created_to,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        date_created_from: Union[datetime, object] = values.unset,
        date_created_to: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ExecutionInstance]:
        """
        Asynchronously lists ExecutionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param datetime date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                date_created_from=date_created_from,
                date_created_to=date_created_to,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        date_created_from: Union[datetime, object] = values.unset,
        date_created_to: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ExecutionPage:
        """
        Retrieve a single page of ExecutionInstance records from the API.
        Request is executed immediately

        :param date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ExecutionInstance
        """
        data = values.of(
            {
                "DateCreatedFrom": serialize.iso8601_datetime(date_created_from),
                "DateCreatedTo": serialize.iso8601_datetime(date_created_to),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ExecutionPage(self._version, response, self._solution)

    async def page_async(
        self,
        date_created_from: Union[datetime, object] = values.unset,
        date_created_to: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ExecutionPage:
        """
        Asynchronously retrieve a single page of ExecutionInstance records from the API.
        Request is executed immediately

        :param date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ExecutionInstance
        """
        data = values.of(
            {
                "DateCreatedFrom": serialize.iso8601_datetime(date_created_from),
                "DateCreatedTo": serialize.iso8601_datetime(date_created_to),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ExecutionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ExecutionPage:
        """
        Retrieve a specific page of ExecutionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ExecutionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ExecutionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ExecutionPage:
        """
        Asynchronously retrieve a specific page of ExecutionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ExecutionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ExecutionPage(self._version, response, self._solution)

    def get(self, sid: str) -> ExecutionContext:
        """
        Constructs a ExecutionContext

        :param sid: The SID of the Execution resource to update.
        """
        return ExecutionContext(
            self._version, flow_sid=self._solution["flow_sid"], sid=sid
        )

    def __call__(self, sid: str) -> ExecutionContext:
        """
        Constructs a ExecutionContext

        :param sid: The SID of the Execution resource to update.
        """
        return ExecutionContext(
            self._version, flow_sid=self._solution["flow_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V2.ExecutionList>"
