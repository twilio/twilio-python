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
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InviteInstance(InstanceResource):

    """
    :ivar sid:
    :ivar account_sid:
    :ivar channel_sid:
    :ivar service_sid:
    :ivar identity:
    :ivar date_created:
    :ivar date_updated:
    :ivar role_sid:
    :ivar created_by:
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
        self.created_by: Optional[str] = payload.get("created_by")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "channel_sid": channel_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[InviteContext] = None

    @property
    def _proxy(self) -> "InviteContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InviteContext for this InviteInstance
        """
        if self._context is None:
            self._context = InviteContext(
                self._version,
                service_sid=self._solution["service_sid"],
                channel_sid=self._solution["channel_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the InviteInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the InviteInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "InviteInstance":
        """
        Fetch the InviteInstance


        :returns: The fetched InviteInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "InviteInstance":
        """
        Asynchronous coroutine to fetch the InviteInstance


        :returns: The fetched InviteInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V1.InviteInstance {}>".format(context)


class InviteContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        """
        Initialize the InviteContext

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
            "/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the InviteInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the InviteInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> InviteInstance:
        """
        Fetch the InviteInstance


        :returns: The fetched InviteInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return InviteInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> InviteInstance:
        """
        Asynchronous coroutine to fetch the InviteInstance


        :returns: The fetched InviteInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return InviteInstance(
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
        return "<Twilio.IpMessaging.V1.InviteContext {}>".format(context)


class InvitePage(Page):
    def get_instance(self, payload) -> InviteInstance:
        """
        Build an instance of InviteInstance

        :param dict payload: Payload response from the API
        """
        return InviteInstance(
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
        return "<Twilio.IpMessaging.V1.InvitePage>"


class InviteList(ListResource):
    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        """
        Initialize the InviteList

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
        self._uri = "/Services/{service_sid}/Channels/{channel_sid}/Invites".format(
            **self._solution
        )

    def create(self, identity, role_sid=values.unset) -> InviteInstance:
        """
        Create the InviteInstance

        :param str identity:
        :param str role_sid:

        :returns: The created InviteInstance
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

        return InviteInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    async def create_async(self, identity, role_sid=values.unset) -> InviteInstance:
        """
        Asynchronously create the InviteInstance

        :param str identity:
        :param str role_sid:

        :returns: The created InviteInstance
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

        return InviteInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
        )

    def stream(
        self, identity=values.unset, limit=None, page_size=None
    ) -> List[InviteInstance]:
        """
        Streams InviteInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[str] identity:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(identity=identity, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self, identity=values.unset, limit=None, page_size=None
    ) -> List[InviteInstance]:
        """
        Asynchronously streams InviteInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[str] identity:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(identity=identity, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self, identity=values.unset, limit=None, page_size=None
    ) -> List[InviteInstance]:
        """
        Lists InviteInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[str] identity:
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
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
        self, identity=values.unset, limit=None, page_size=None
    ) -> List[InviteInstance]:
        """
        Asynchronously lists InviteInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[str] identity:
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
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
        identity=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> InvitePage:
        """
        Retrieve a single page of InviteInstance records from the API.
        Request is executed immediately

        :param List[str] identity:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InviteInstance
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
        return InvitePage(self._version, response, self._solution)

    async def page_async(
        self,
        identity=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> InvitePage:
        """
        Asynchronously retrieve a single page of InviteInstance records from the API.
        Request is executed immediately

        :param List[str] identity:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InviteInstance
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
        return InvitePage(self._version, response, self._solution)

    def get_page(self, target_url) -> InvitePage:
        """
        Retrieve a specific page of InviteInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InviteInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InvitePage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> InvitePage:
        """
        Asynchronously retrieve a specific page of InviteInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InviteInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InvitePage(self._version, response, self._solution)

    def get(self, sid) -> InviteContext:
        """
        Constructs a InviteContext

        :param sid:
        """
        return InviteContext(
            self._version,
            service_sid=self._solution["service_sid"],
            channel_sid=self._solution["channel_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> InviteContext:
        """
        Constructs a InviteContext

        :param sid:
        """
        return InviteContext(
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
        return "<Twilio.IpMessaging.V1.InviteList>"
