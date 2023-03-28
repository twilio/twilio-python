r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ParticipantInstance(InstanceResource):
    class Codec(object):
        VP8 = "VP8"
        H264 = "H264"
        VP9 = "VP9"

    class EdgeLocation(object):
        ASHBURN = "ashburn"
        DUBLIN = "dublin"
        FRANKFURT = "frankfurt"
        SINGAPORE = "singapore"
        SYDNEY = "sydney"
        SAO_PAULO = "sao_paulo"
        ROAMING = "roaming"
        UMATILLA = "umatilla"
        TOKYO = "tokyo"

    class RoomStatus(object):
        IN_PROGRESS = "in_progress"
        COMPLETED = "completed"

    class TwilioRealm(object):
        US1 = "us1"
        US2 = "us2"
        AU1 = "au1"
        BR1 = "br1"
        IE1 = "ie1"
        JP1 = "jp1"
        SG1 = "sg1"
        IN1 = "in1"
        DE1 = "de1"
        GLL = "gll"

    """
    :ivar participant_sid: Unique identifier for the participant.
    :ivar participant_identity: The application-defined string that uniquely identifies the participant within a Room.
    :ivar join_time: When the participant joined the room.
    :ivar leave_time: When the participant left the room.
    :ivar duration_sec: Amount of time in seconds the participant was in the room.
    :ivar account_sid: Account SID associated with the room.
    :ivar room_sid: Unique identifier for the room.
    :ivar status: 
    :ivar codecs: Codecs detected from the participant. Can be `VP8`, `H264`, or `VP9`.
    :ivar end_reason: Reason the participant left the room. See [the list of possible values here](https://www.twilio.com/docs/video/video-log-analyzer/video-log-analyzer-api#end_reason).
    :ivar error_code: Errors encountered by the participant.
    :ivar error_code_url: Twilio error code dictionary link.
    :ivar media_region: 
    :ivar properties: Object containing information about the participant's data from the room. See [below](https://www.twilio.com/docs/video/video-log-analyzer/video-log-analyzer-api#properties) for more information.
    :ivar edge_location: 
    :ivar publisher_info: Object containing information about the SDK name and version. See [below](https://www.twilio.com/docs/video/video-log-analyzer/video-log-analyzer-api#publisher_info) for more information.
    :ivar url: URL of the participant resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        room_sid: str,
        participant_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.participant_sid: Optional[str] = payload.get("participant_sid")
        self.participant_identity: Optional[str] = payload.get("participant_identity")
        self.join_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("join_time")
        )
        self.leave_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("leave_time")
        )
        self.duration_sec: Optional[int] = payload.get("duration_sec")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.room_sid: Optional[str] = payload.get("room_sid")
        self.status: Optional["ParticipantInstance.RoomStatus"] = payload.get("status")
        self.codecs: Optional[List["ParticipantInstance.Codec"]] = payload.get("codecs")
        self.end_reason: Optional[str] = payload.get("end_reason")
        self.error_code: Optional[int] = deserialize.integer(payload.get("error_code"))
        self.error_code_url: Optional[str] = payload.get("error_code_url")
        self.media_region: Optional["ParticipantInstance.TwilioRealm"] = payload.get(
            "media_region"
        )
        self.properties: Optional[Dict[str, object]] = payload.get("properties")
        self.edge_location: Optional["ParticipantInstance.EdgeLocation"] = payload.get(
            "edge_location"
        )
        self.publisher_info: Optional[Dict[str, object]] = payload.get("publisher_info")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid or self.participant_sid,
        }
        self._context: Optional[ParticipantContext] = None

    @property
    def _proxy(self) -> "ParticipantContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ParticipantContext for this ParticipantInstance
        """
        if self._context is None:
            self._context = ParticipantContext(
                self._version,
                room_sid=self._solution["room_sid"],
                participant_sid=self._solution["participant_sid"],
            )
        return self._context

    def fetch(self) -> "ParticipantInstance":
        """
        Fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ParticipantInstance":
        """
        Asynchronous coroutine to fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.ParticipantInstance {}>".format(context)


class ParticipantContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str, participant_sid: str):
        """
        Initialize the ParticipantContext

        :param version: Version that contains the resource
        :param room_sid: The SID of the Room resource.
        :param participant_sid: The SID of the Participant resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "participant_sid": participant_sid,
        }
        self._uri = "/Video/Rooms/{room_sid}/Participants/{participant_sid}".format(
            **self._solution
        )

    def fetch(self) -> ParticipantInstance:
        """
        Fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    async def fetch_async(self) -> ParticipantInstance:
        """
        Asynchronous coroutine to fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ParticipantInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.ParticipantContext {}>".format(context)


class ParticipantPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ParticipantInstance:
        """
        Build an instance of ParticipantInstance

        :param payload: Payload response from the API
        """
        return ParticipantInstance(
            self._version, payload, room_sid=self._solution["room_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.ParticipantPage>"


class ParticipantList(ListResource):
    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the ParticipantList

        :param version: Version that contains the resource
        :param room_sid: The SID of the Room resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
        }
        self._uri = "/Video/Rooms/{room_sid}/Participants".format(**self._solution)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ParticipantInstance]:
        """
        Streams ParticipantInstance records from the API as a generator stream.
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
    ) -> List[ParticipantInstance]:
        """
        Asynchronously streams ParticipantInstance records from the API as a generator stream.
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
    ) -> List[ParticipantInstance]:
        """
        Lists ParticipantInstance records from the API as a list.
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
    ) -> List[ParticipantInstance]:
        """
        Asynchronously lists ParticipantInstance records from the API as a list.
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
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ParticipantPage:
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ParticipantPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ParticipantPage:
        """
        Asynchronously retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
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
        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ParticipantPage:
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ParticipantPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ParticipantPage:
        """
        Asynchronously retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ParticipantPage(self._version, response, self._solution)

    def get(self, participant_sid: str) -> ParticipantContext:
        """
        Constructs a ParticipantContext

        :param participant_sid: The SID of the Participant resource.
        """
        return ParticipantContext(
            self._version,
            room_sid=self._solution["room_sid"],
            participant_sid=participant_sid,
        )

    def __call__(self, participant_sid: str) -> ParticipantContext:
        """
        Constructs a ParticipantContext

        :param participant_sid: The SID of the Participant resource.
        """
        return ParticipantContext(
            self._version,
            room_sid=self._solution["room_sid"],
            participant_sid=participant_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.ParticipantList>"
