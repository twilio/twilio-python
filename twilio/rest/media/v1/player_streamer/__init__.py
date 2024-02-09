r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Media
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
from twilio.rest.media.v1.player_streamer.playback_grant import PlaybackGrantList


class PlayerStreamerInstance(InstanceResource):
    class EndedReason(object):
        ENDED_VIA_API = "ended-via-api"
        MAX_DURATION_EXCEEDED = "max-duration-exceeded"
        STREAM_DISCONNECTED_BY_SOURCE = "stream-disconnected-by-source"
        UNEXPECTED_FAILURE = "unexpected-failure"

    class Order(object):
        ASC = "asc"
        DESC = "desc"

    class Status(object):
        CREATED = "created"
        STARTED = "started"
        ENDED = "ended"
        FAILED = "failed"

    class UpdateStatus(object):
        ENDED = "ended"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the PlayerStreamer resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar video: Specifies whether the PlayerStreamer is configured to stream video. Defaults to `true`.
    :ivar links: The URLs of related resources.
    :ivar sid: The unique string generated to identify the PlayerStreamer resource.
    :ivar status: 
    :ivar url: The absolute URL of the resource.
    :ivar status_callback: The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details.
    :ivar status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
    :ivar ended_reason: 
    :ivar max_duration: The maximum time, in seconds, that the PlayerStreamer is active (`created` or `started`) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming.
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
        self.video: Optional[bool] = payload.get("video")
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.sid: Optional[str] = payload.get("sid")
        self.status: Optional["PlayerStreamerInstance.Status"] = payload.get("status")
        self.url: Optional[str] = payload.get("url")
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.ended_reason: Optional["PlayerStreamerInstance.EndedReason"] = payload.get(
            "ended_reason"
        )
        self.max_duration: Optional[int] = deserialize.integer(
            payload.get("max_duration")
        )

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[PlayerStreamerContext] = None

    @property
    def _proxy(self) -> "PlayerStreamerContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PlayerStreamerContext for this PlayerStreamerInstance
        """
        if self._context is None:
            self._context = PlayerStreamerContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "PlayerStreamerInstance":
        """
        Fetch the PlayerStreamerInstance


        :returns: The fetched PlayerStreamerInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "PlayerStreamerInstance":
        """
        Asynchronous coroutine to fetch the PlayerStreamerInstance


        :returns: The fetched PlayerStreamerInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, status: "PlayerStreamerInstance.UpdateStatus"
    ) -> "PlayerStreamerInstance":
        """
        Update the PlayerStreamerInstance

        :param status:

        :returns: The updated PlayerStreamerInstance
        """
        return self._proxy.update(
            status=status,
        )

    async def update_async(
        self, status: "PlayerStreamerInstance.UpdateStatus"
    ) -> "PlayerStreamerInstance":
        """
        Asynchronous coroutine to update the PlayerStreamerInstance

        :param status:

        :returns: The updated PlayerStreamerInstance
        """
        return await self._proxy.update_async(
            status=status,
        )

    @property
    def playback_grant(self) -> PlaybackGrantList:
        """
        Access the playback_grant
        """
        return self._proxy.playback_grant

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Media.V1.PlayerStreamerInstance {}>".format(context)


class PlayerStreamerContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the PlayerStreamerContext

        :param version: Version that contains the resource
        :param sid: The SID of the PlayerStreamer resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/PlayerStreamers/{sid}".format(**self._solution)

        self._playback_grant: Optional[PlaybackGrantList] = None

    def fetch(self) -> PlayerStreamerInstance:
        """
        Fetch the PlayerStreamerInstance


        :returns: The fetched PlayerStreamerInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PlayerStreamerInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> PlayerStreamerInstance:
        """
        Asynchronous coroutine to fetch the PlayerStreamerInstance


        :returns: The fetched PlayerStreamerInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PlayerStreamerInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self, status: "PlayerStreamerInstance.UpdateStatus"
    ) -> PlayerStreamerInstance:
        """
        Update the PlayerStreamerInstance

        :param status:

        :returns: The updated PlayerStreamerInstance
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

        return PlayerStreamerInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self, status: "PlayerStreamerInstance.UpdateStatus"
    ) -> PlayerStreamerInstance:
        """
        Asynchronous coroutine to update the PlayerStreamerInstance

        :param status:

        :returns: The updated PlayerStreamerInstance
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

        return PlayerStreamerInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def playback_grant(self) -> PlaybackGrantList:
        """
        Access the playback_grant
        """
        if self._playback_grant is None:
            self._playback_grant = PlaybackGrantList(
                self._version,
                self._solution["sid"],
            )
        return self._playback_grant

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Media.V1.PlayerStreamerContext {}>".format(context)


class PlayerStreamerPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> PlayerStreamerInstance:
        """
        Build an instance of PlayerStreamerInstance

        :param payload: Payload response from the API
        """
        return PlayerStreamerInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Media.V1.PlayerStreamerPage>"


class PlayerStreamerList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the PlayerStreamerList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/PlayerStreamers"

    def create(
        self,
        video: Union[bool, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        max_duration: Union[int, object] = values.unset,
    ) -> PlayerStreamerInstance:
        """
        Create the PlayerStreamerInstance

        :param video: Specifies whether the PlayerStreamer is configured to stream video. Defaults to `true`.
        :param status_callback: The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details.
        :param status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
        :param max_duration: The maximum time, in seconds, that the PlayerStreamer is active (`created` or `started`) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming.

        :returns: The created PlayerStreamerInstance
        """

        data = values.of(
            {
                "Video": video,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "MaxDuration": max_duration,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PlayerStreamerInstance(self._version, payload)

    async def create_async(
        self,
        video: Union[bool, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        max_duration: Union[int, object] = values.unset,
    ) -> PlayerStreamerInstance:
        """
        Asynchronously create the PlayerStreamerInstance

        :param video: Specifies whether the PlayerStreamer is configured to stream video. Defaults to `true`.
        :param status_callback: The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details.
        :param status_callback_method: The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
        :param max_duration: The maximum time, in seconds, that the PlayerStreamer is active (`created` or `started`) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming.

        :returns: The created PlayerStreamerInstance
        """

        data = values.of(
            {
                "Video": video,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "MaxDuration": max_duration,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PlayerStreamerInstance(self._version, payload)

    def stream(
        self,
        order: Union["PlayerStreamerInstance.Order", object] = values.unset,
        status: Union["PlayerStreamerInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[PlayerStreamerInstance]:
        """
        Streams PlayerStreamerInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;PlayerStreamerInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;PlayerStreamerInstance.Status&quot; status: Status to filter by, with possible values `created`, `started`, `ended`, or `failed`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(order=order, status=status, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        order: Union["PlayerStreamerInstance.Order", object] = values.unset,
        status: Union["PlayerStreamerInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[PlayerStreamerInstance]:
        """
        Asynchronously streams PlayerStreamerInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;PlayerStreamerInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;PlayerStreamerInstance.Status&quot; status: Status to filter by, with possible values `created`, `started`, `ended`, or `failed`.
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
            order=order, status=status, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        order: Union["PlayerStreamerInstance.Order", object] = values.unset,
        status: Union["PlayerStreamerInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[PlayerStreamerInstance]:
        """
        Lists PlayerStreamerInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;PlayerStreamerInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;PlayerStreamerInstance.Status&quot; status: Status to filter by, with possible values `created`, `started`, `ended`, or `failed`.
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
                order=order,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        order: Union["PlayerStreamerInstance.Order", object] = values.unset,
        status: Union["PlayerStreamerInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[PlayerStreamerInstance]:
        """
        Asynchronously lists PlayerStreamerInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;PlayerStreamerInstance.Order&quot; order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param &quot;PlayerStreamerInstance.Status&quot; status: Status to filter by, with possible values `created`, `started`, `ended`, or `failed`.
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
                order=order,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        order: Union["PlayerStreamerInstance.Order", object] = values.unset,
        status: Union["PlayerStreamerInstance.Status", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> PlayerStreamerPage:
        """
        Retrieve a single page of PlayerStreamerInstance records from the API.
        Request is executed immediately

        :param order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param status: Status to filter by, with possible values `created`, `started`, `ended`, or `failed`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of PlayerStreamerInstance
        """
        data = values.of(
            {
                "Order": order,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return PlayerStreamerPage(self._version, response)

    async def page_async(
        self,
        order: Union["PlayerStreamerInstance.Order", object] = values.unset,
        status: Union["PlayerStreamerInstance.Status", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> PlayerStreamerPage:
        """
        Asynchronously retrieve a single page of PlayerStreamerInstance records from the API.
        Request is executed immediately

        :param order: The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
        :param status: Status to filter by, with possible values `created`, `started`, `ended`, or `failed`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of PlayerStreamerInstance
        """
        data = values.of(
            {
                "Order": order,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return PlayerStreamerPage(self._version, response)

    def get_page(self, target_url: str) -> PlayerStreamerPage:
        """
        Retrieve a specific page of PlayerStreamerInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of PlayerStreamerInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return PlayerStreamerPage(self._version, response)

    async def get_page_async(self, target_url: str) -> PlayerStreamerPage:
        """
        Asynchronously retrieve a specific page of PlayerStreamerInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of PlayerStreamerInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return PlayerStreamerPage(self._version, response)

    def get(self, sid: str) -> PlayerStreamerContext:
        """
        Constructs a PlayerStreamerContext

        :param sid: The SID of the PlayerStreamer resource to update.
        """
        return PlayerStreamerContext(self._version, sid=sid)

    def __call__(self, sid: str) -> PlayerStreamerContext:
        """
        Constructs a PlayerStreamerContext

        :param sid: The SID of the PlayerStreamer resource to update.
        """
        return PlayerStreamerContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Media.V1.PlayerStreamerList>"
