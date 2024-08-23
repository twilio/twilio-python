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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CommandInstance(InstanceResource):
    """
    :ivar sid:
    :ivar account_sid:
    :ivar device_sid:
    :ivar sim_sid:
    :ivar command:
    :ivar command_mode:
    :ivar status:
    :ivar direction:
    :ivar date_created:
    :ivar date_updated:
    :ivar url:
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.device_sid: Optional[str] = payload.get("device_sid")
        self.sim_sid: Optional[str] = payload.get("sim_sid")
        self.command: Optional[str] = payload.get("command")
        self.command_mode: Optional[str] = payload.get("command_mode")
        self.status: Optional[str] = payload.get("status")
        self.direction: Optional[str] = payload.get("direction")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[CommandContext] = None

    @property
    def _proxy(self) -> "CommandContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CommandContext for this CommandInstance
        """
        if self._context is None:
            self._context = CommandContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "CommandInstance":
        """
        Fetch the CommandInstance


        :returns: The fetched CommandInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CommandInstance":
        """
        Asynchronous coroutine to fetch the CommandInstance


        :returns: The fetched CommandInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Preview.Wireless.CommandInstance {context}>"


class CommandContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CommandContext

        :param version: Version that contains the resource
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Commands/{sid}".format(**self._solution)

    def fetch(self) -> CommandInstance:
        """
        Fetch the CommandInstance


        :returns: The fetched CommandInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CommandInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CommandInstance:
        """
        Asynchronous coroutine to fetch the CommandInstance


        :returns: The fetched CommandInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CommandInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Preview.Wireless.CommandContext {context}>"


class CommandPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> CommandInstance:
        """
        Build an instance of CommandInstance

        :param payload: Payload response from the API
        """
        return CommandInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Wireless.CommandPage>"


class CommandList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CommandList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Commands"

    def create(
        self,
        command: str,
        device: Union[str, object] = values.unset,
        sim: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        command_mode: Union[str, object] = values.unset,
        include_sid: Union[str, object] = values.unset,
    ) -> CommandInstance:
        """
        Create the CommandInstance

        :param command:
        :param device:
        :param sim:
        :param callback_method:
        :param callback_url:
        :param command_mode:
        :param include_sid:

        :returns: The created CommandInstance
        """

        data = values.of(
            {
                "Command": command,
                "Device": device,
                "Sim": sim,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
                "CommandMode": command_mode,
                "IncludeSid": include_sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CommandInstance(self._version, payload)

    async def create_async(
        self,
        command: str,
        device: Union[str, object] = values.unset,
        sim: Union[str, object] = values.unset,
        callback_method: Union[str, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        command_mode: Union[str, object] = values.unset,
        include_sid: Union[str, object] = values.unset,
    ) -> CommandInstance:
        """
        Asynchronously create the CommandInstance

        :param command:
        :param device:
        :param sim:
        :param callback_method:
        :param callback_url:
        :param command_mode:
        :param include_sid:

        :returns: The created CommandInstance
        """

        data = values.of(
            {
                "Command": command,
                "Device": device,
                "Sim": sim,
                "CallbackMethod": callback_method,
                "CallbackUrl": callback_url,
                "CommandMode": command_mode,
                "IncludeSid": include_sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CommandInstance(self._version, payload)

    def stream(
        self,
        device: Union[str, object] = values.unset,
        sim: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        direction: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[CommandInstance]:
        """
        Streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str device:
        :param str sim:
        :param str status:
        :param str direction:
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
            device=device,
            sim=sim,
            status=status,
            direction=direction,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        device: Union[str, object] = values.unset,
        sim: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        direction: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[CommandInstance]:
        """
        Asynchronously streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str device:
        :param str sim:
        :param str status:
        :param str direction:
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
            device=device,
            sim=sim,
            status=status,
            direction=direction,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        device: Union[str, object] = values.unset,
        sim: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        direction: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CommandInstance]:
        """
        Lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str device:
        :param str sim:
        :param str status:
        :param str direction:
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
                device=device,
                sim=sim,
                status=status,
                direction=direction,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        device: Union[str, object] = values.unset,
        sim: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        direction: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CommandInstance]:
        """
        Asynchronously lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str device:
        :param str sim:
        :param str status:
        :param str direction:
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
                device=device,
                sim=sim,
                status=status,
                direction=direction,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        device: Union[str, object] = values.unset,
        sim: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        direction: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CommandPage:
        """
        Retrieve a single page of CommandInstance records from the API.
        Request is executed immediately

        :param device:
        :param sim:
        :param status:
        :param direction:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        """
        data = values.of(
            {
                "Device": device,
                "Sim": sim,
                "Status": status,
                "Direction": direction,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CommandPage(self._version, response)

    async def page_async(
        self,
        device: Union[str, object] = values.unset,
        sim: Union[str, object] = values.unset,
        status: Union[str, object] = values.unset,
        direction: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CommandPage:
        """
        Asynchronously retrieve a single page of CommandInstance records from the API.
        Request is executed immediately

        :param device:
        :param sim:
        :param status:
        :param direction:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        """
        data = values.of(
            {
                "Device": device,
                "Sim": sim,
                "Status": status,
                "Direction": direction,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return CommandPage(self._version, response)

    def get_page(self, target_url: str) -> CommandPage:
        """
        Retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CommandPage(self._version, response)

    async def get_page_async(self, target_url: str) -> CommandPage:
        """
        Asynchronously retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CommandPage(self._version, response)

    def get(self, sid: str) -> CommandContext:
        """
        Constructs a CommandContext

        :param sid:
        """
        return CommandContext(self._version, sid=sid)

    def __call__(self, sid: str) -> CommandContext:
        """
        Constructs a CommandContext

        :param sid:
        """
        return CommandContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Wireless.CommandList>"
