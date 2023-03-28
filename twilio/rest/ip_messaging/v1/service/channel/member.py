r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
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


class MemberInstance(InstanceResource):

    """
    :ivar sid:
    :ivar account_sid:
    :ivar channel_sid:
    :ivar service_sid:
    :ivar identity:
    :ivar date_created:
    :ivar date_updated:
    :ivar role_sid:
    :ivar last_consumed_message_index:
    :ivar last_consumption_timestamp:
    :ivar url:
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        channel_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.channel_sid: Optional[str] = payload.get("channel_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.role_sid: Optional[str] = payload.get("role_sid")
        self.last_consumed_message_index: Optional[int] = deserialize.integer(
            payload.get("last_consumed_message_index")
        )
        self.last_consumption_timestamp: Optional[
            datetime
        ] = deserialize.iso8601_datetime(payload.get("last_consumption_timestamp"))
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "channel_sid": channel_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[MemberContext] = None

    @property
    def _proxy(self) -> "MemberContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MemberContext for this MemberInstance
        """
        if self._context is None:
            self._context = MemberContext(
                self._version,
                service_sid=self._solution["service_sid"],
                channel_sid=self._solution["channel_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the MemberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the MemberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "MemberInstance":
        """
        Fetch the MemberInstance


        :returns: The fetched MemberInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "MemberInstance":
        """
        Asynchronous coroutine to fetch the MemberInstance


        :returns: The fetched MemberInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        role_sid: Union[str, object] = values.unset,
        last_consumed_message_index: Union[int, object] = values.unset,
    ) -> "MemberInstance":
        """
        Update the MemberInstance

        :param role_sid:
        :param last_consumed_message_index:

        :returns: The updated MemberInstance
        """
        return self._proxy.update(
            role_sid=role_sid,
            last_consumed_message_index=last_consumed_message_index,
        )

    async def update_async(
        self,
        role_sid: Union[str, object] = values.unset,
        last_consumed_message_index: Union[int, object] = values.unset,
    ) -> "MemberInstance":
        """
        Asynchronous coroutine to update the MemberInstance

        :param role_sid:
        :param last_consumed_message_index:

        :returns: The updated MemberInstance
        """
        return await self._proxy.update_async(
            role_sid=role_sid,
            last_consumed_message_index=last_consumed_message_index,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V1.MemberInstance {}>".format(context)


class MemberContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        """
        Initialize the MemberContext

        :param version: Version that contains the resource
        :param service_sid:
        :param channel_sid:
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "channel_sid": channel_sid,
            "sid": sid,
        }
        self._uri = (
            "/Services/{service_sid}/Channels/{channel_sid}/Members/{sid}".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the MemberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the MemberInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> MemberInstance:
        """
        Fetch the MemberInstance


        :returns: The fetched MemberInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> MemberInstance:
        """
        Asynchronous coroutine to fetch the MemberInstance


        :returns: The fetched MemberInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        role_sid: Union[str, object] = values.unset,
        last_consumed_message_index: Union[int, object] = values.unset,
    ) -> MemberInstance:
        """
        Update the MemberInstance

        :param role_sid:
        :param last_consumed_message_index:

        :returns: The updated MemberInstance
        """
        data = values.of(
            {
                "RoleSid": role_sid,
                "LastConsumedMessageIndex": last_consumed_message_index,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        role_sid: Union[str, object] = values.unset,
        last_consumed_message_index: Union[int, object] = values.unset,
    ) -> MemberInstance:
        """
        Asynchronous coroutine to update the MemberInstance

        :param role_sid:
        :param last_consumed_message_index:

        :returns: The updated MemberInstance
        """
        data = values.of(
            {
                "RoleSid": role_sid,
                "LastConsumedMessageIndex": last_consumed_message_index,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V1.MemberContext {}>".format(context)


class MemberPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> MemberInstance:
        """
        Build an instance of MemberInstance

        :param payload: Payload response from the API
        """
        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V1.MemberPage>"


class MemberList(ListResource):
    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        """
        Initialize the MemberList

        :param version: Version that contains the resource
        :param service_sid:
        :param channel_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "channel_sid": channel_sid,
        }
        self._uri = "/Services/{service_sid}/Channels/{channel_sid}/Members".format(
            **self._solution
        )

    def create(
        self, identity: str, role_sid: Union[str, object] = values.unset
    ) -> MemberInstance:
        """
        Create the MemberInstance

        :param identity:
        :param role_sid:

        :returns: The created MemberInstance
        """
        data = values.of(
            {
                "Identity": identity,
                "RoleSid": role_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def create_async(
        self, identity: str, role_sid: Union[str, object] = values.unset
    ) -> MemberInstance:
        """
        Asynchronously create the MemberInstance

        :param identity:
        :param role_sid:

        :returns: The created MemberInstance
        """
        data = values.of(
            {
                "Identity": identity,
                "RoleSid": role_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return MemberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def stream(
        self,
        identity: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MemberInstance]:
        """
        Streams MemberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[str] identity:
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(identity=identity, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        identity: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MemberInstance]:
        """
        Asynchronously streams MemberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[str] identity:
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(identity=identity, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        identity: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MemberInstance]:
        """
        Lists MemberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[str] identity:
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
                identity=identity,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        identity: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MemberInstance]:
        """
        Asynchronously lists MemberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[str] identity:
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
                identity=identity,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        identity: Union[List[str], object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> MemberPage:
        """
        Retrieve a single page of MemberInstance records from the API.
        Request is executed immediately

        :param identity:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MemberInstance
        """
        data = values.of(
            {
                "Identity": serialize.map(identity, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MemberPage(self._version, response, self._solution)

    async def page_async(
        self,
        identity: Union[List[str], object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> MemberPage:
        """
        Asynchronously retrieve a single page of MemberInstance records from the API.
        Request is executed immediately

        :param identity:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MemberInstance
        """
        data = values.of(
            {
                "Identity": serialize.map(identity, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return MemberPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> MemberPage:
        """
        Retrieve a specific page of MemberInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MemberInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MemberPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> MemberPage:
        """
        Asynchronously retrieve a specific page of MemberInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MemberInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MemberPage(self._version, response, self._solution)

    def get(self, sid: str) -> MemberContext:
        """
        Constructs a MemberContext

        :param sid:
        """
        return MemberContext(
            self._version,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> MemberContext:
        """
        Constructs a MemberContext

        :param sid:
        """
        return MemberContext(
            self._version,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V1.MemberList>"
