r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Assistants
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AssistantsToolInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Tool resource.
    :ivar description: The description of the tool.
    :ivar enabled: True if the tool is enabled.
    :ivar id: The tool ID.
    :ivar meta: The metadata related to method, url, input_schema to used with the Tool.
    :ivar name: The name of the tool.
    :ivar requires_auth: The authentication requirement for the tool.
    :ivar type: The type of the tool. ('WEBHOOK')
    :ivar url: The url of the tool resource.
    :ivar date_created: The date and time in GMT when the Tool was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Tool was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        assistant_id: str,
        id: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.description: Optional[str] = payload.get("description")
        self.enabled: Optional[bool] = payload.get("enabled")
        self.id: Optional[str] = payload.get("id")
        self.meta: Optional[Dict[str, object]] = payload.get("meta")
        self.name: Optional[str] = payload.get("name")
        self.requires_auth: Optional[bool] = payload.get("requires_auth")
        self.type: Optional[str] = payload.get("type")
        self.url: Optional[str] = payload.get("url")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "assistant_id": assistant_id,
            "id": id or self.id,
        }
        self._context: Optional[AssistantsToolContext] = None

    @property
    def _proxy(self) -> "AssistantsToolContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssistantsToolContext for this AssistantsToolInstance
        """
        if self._context is None:
            self._context = AssistantsToolContext(
                self._version,
                assistant_id=self._solution["assistant_id"],
                id=self._solution["id"],
            )
        return self._context

    def create(self) -> "AssistantsToolInstance":
        """
        Create the AssistantsToolInstance


        :returns: The created AssistantsToolInstance
        """
        return self._proxy.create()

    async def create_async(self) -> "AssistantsToolInstance":
        """
        Asynchronous coroutine to create the AssistantsToolInstance


        :returns: The created AssistantsToolInstance
        """
        return await self._proxy.create_async()

    def delete(self) -> bool:
        """
        Deletes the AssistantsToolInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AssistantsToolInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Assistants.V1.AssistantsToolInstance {}>".format(context)


class AssistantsToolContext(InstanceContext):

    def __init__(self, version: Version, assistant_id: str, id: str):
        """
        Initialize the AssistantsToolContext

        :param version: Version that contains the resource
        :param assistant_id: The assistant ID.
        :param id: The tool ID.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_id": assistant_id,
            "id": id,
        }
        self._uri = "/Assistants/{assistant_id}/Tools/{id}".format(**self._solution)

    def create(self) -> AssistantsToolInstance:
        """
        Create the AssistantsToolInstance


        :returns: The created AssistantsToolInstance
        """
        data = values.of({})

        payload = self._version.create(method="POST", uri=self._uri, data=data)

        return AssistantsToolInstance(
            self._version,
            payload,
            assistant_id=self._solution["assistant_id"],
            id=self._solution["id"],
        )

    async def create_async(self) -> AssistantsToolInstance:
        """
        Asynchronous coroutine to create the AssistantsToolInstance


        :returns: The created AssistantsToolInstance
        """
        data = values.of({})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data
        )

        return AssistantsToolInstance(
            self._version,
            payload,
            assistant_id=self._solution["assistant_id"],
            id=self._solution["id"],
        )

    def delete(self) -> bool:
        """
        Deletes the AssistantsToolInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AssistantsToolInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Assistants.V1.AssistantsToolContext {}>".format(context)


class AssistantsToolPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> AssistantsToolInstance:
        """
        Build an instance of AssistantsToolInstance

        :param payload: Payload response from the API
        """
        return AssistantsToolInstance(
            self._version, payload, assistant_id=self._solution["assistant_id"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Assistants.V1.AssistantsToolPage>"


class AssistantsToolList(ListResource):

    def __init__(self, version: Version, assistant_id: str):
        """
        Initialize the AssistantsToolList

        :param version: Version that contains the resource
        :param assistant_id: The assistant ID.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_id": assistant_id,
        }
        self._uri = "/Assistants/{assistant_id}/Tools".format(**self._solution)

    def create(self) -> AssistantsToolInstance:
        """
        Create the AssistantsToolInstance


        :returns: The created AssistantsToolInstance
        """

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(method="POST", uri=self._uri, headers=headers)

        return AssistantsToolInstance(
            self._version, payload, assistant_id=self._solution["assistant_id"]
        )

    async def create_async(self) -> AssistantsToolInstance:
        """
        Asynchronously create the AssistantsToolInstance


        :returns: The created AssistantsToolInstance
        """

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, headers=headers
        )

        return AssistantsToolInstance(
            self._version, payload, assistant_id=self._solution["assistant_id"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AssistantsToolInstance]:
        """
        Streams AssistantsToolInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[AssistantsToolInstance]:
        """
        Asynchronously streams AssistantsToolInstance records from the API as a generator stream.
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

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssistantsToolInstance]:
        """
        Lists AssistantsToolInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssistantsToolInstance]:
        """
        Asynchronously lists AssistantsToolInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssistantsToolPage:
        """
        Retrieve a single page of AssistantsToolInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssistantsToolInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AssistantsToolPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssistantsToolPage:
        """
        Asynchronously retrieve a single page of AssistantsToolInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssistantsToolInstance
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
        return AssistantsToolPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AssistantsToolPage:
        """
        Retrieve a specific page of AssistantsToolInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssistantsToolInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AssistantsToolPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AssistantsToolPage:
        """
        Asynchronously retrieve a specific page of AssistantsToolInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssistantsToolInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AssistantsToolPage(self._version, response, self._solution)

    def get(self, id: str) -> AssistantsToolContext:
        """
        Constructs a AssistantsToolContext

        :param id: The tool ID.
        """
        return AssistantsToolContext(
            self._version, assistant_id=self._solution["assistant_id"], id=id
        )

    def __call__(self, id: str) -> AssistantsToolContext:
        """
        Constructs a AssistantsToolContext

        :param id: The tool ID.
        """
        return AssistantsToolContext(
            self._version, assistant_id=self._solution["assistant_id"], id=id
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Assistants.V1.AssistantsToolList>"