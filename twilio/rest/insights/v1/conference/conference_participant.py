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


class ConferenceParticipantInstance(InstanceResource):
    class CallDirection(object):
        INBOUND = "inbound"
        OUTBOUND = "outbound"

    class CallStatus(object):
        ANSWERED = "answered"
        COMPLETED = "completed"
        BUSY = "busy"
        FAIL = "fail"
        NOANSWER = "noanswer"
        RINGING = "ringing"
        CANCELED = "canceled"

    class CallType(object):
        CARRIER = "carrier"
        CLIENT = "client"
        SIP = "sip"

    class JitterBufferSize(object):
        LARGE = "large"
        SMALL = "small"
        MEDIUM = "medium"
        OFF = "off"

    class ProcessingState(object):
        COMPLETE = "complete"
        IN_PROGRESS = "in_progress"
        TIMEOUT = "timeout"

    class Region(object):
        US1 = "us1"
        US2 = "us2"
        AU1 = "au1"
        BR1 = "br1"
        IE1 = "ie1"
        JP1 = "jp1"
        SG1 = "sg1"
        DE1 = "de1"

    """
    :ivar participant_sid: SID for this participant.
    :ivar label: The user-specified label of this participant.
    :ivar conference_sid: The unique SID identifier of the Conference.
    :ivar call_sid: Unique SID identifier of the call that generated the Participant resource.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar call_direction: 
    :ivar _from: Caller ID of the calling party.
    :ivar to: Called party.
    :ivar call_status: 
    :ivar country_code: ISO alpha-2 country code of the participant based on caller ID or called number.
    :ivar is_moderator: Boolean. Indicates whether participant had startConferenceOnEnter=true or endConferenceOnExit=true.
    :ivar join_time: ISO 8601 timestamp of participant join event.
    :ivar leave_time: ISO 8601 timestamp of participant leave event.
    :ivar duration_seconds: Participant durations in seconds.
    :ivar outbound_queue_length: Add Participant API only. Estimated time in queue at call creation.
    :ivar outbound_time_in_queue: Add Participant API only. Actual time in queue in seconds.
    :ivar jitter_buffer_size: 
    :ivar is_coach: Boolean. Indicated whether participant was a coach.
    :ivar coached_participants: Call SIDs coached by this participant.
    :ivar participant_region: 
    :ivar conference_region: 
    :ivar call_type: 
    :ivar processing_state: 
    :ivar properties: Participant properties and metadata.
    :ivar events: Object containing information of actions taken by participants. Contains a dictionary of URL links to nested resources of this Conference Participant.
    :ivar metrics: Object. Contains participant call quality metrics.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        conference_sid: str,
        participant_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.participant_sid: Optional[str] = payload.get("participant_sid")
        self.label: Optional[str] = payload.get("label")
        self.conference_sid: Optional[str] = payload.get("conference_sid")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.call_direction: Optional[
            "ConferenceParticipantInstance.CallDirection"
        ] = payload.get("call_direction")
        self._from: Optional[str] = payload.get("from")
        self.to: Optional[str] = payload.get("to")
        self.call_status: Optional[
            "ConferenceParticipantInstance.CallStatus"
        ] = payload.get("call_status")
        self.country_code: Optional[str] = payload.get("country_code")
        self.is_moderator: Optional[bool] = payload.get("is_moderator")
        self.join_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("join_time")
        )
        self.leave_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("leave_time")
        )
        self.duration_seconds: Optional[int] = deserialize.integer(
            payload.get("duration_seconds")
        )
        self.outbound_queue_length: Optional[int] = deserialize.integer(
            payload.get("outbound_queue_length")
        )
        self.outbound_time_in_queue: Optional[int] = deserialize.integer(
            payload.get("outbound_time_in_queue")
        )
        self.jitter_buffer_size: Optional[
            "ConferenceParticipantInstance.JitterBufferSize"
        ] = payload.get("jitter_buffer_size")
        self.is_coach: Optional[bool] = payload.get("is_coach")
        self.coached_participants: Optional[List[str]] = payload.get(
            "coached_participants"
        )
        self.participant_region: Optional[
            "ConferenceParticipantInstance.Region"
        ] = payload.get("participant_region")
        self.conference_region: Optional[
            "ConferenceParticipantInstance.Region"
        ] = payload.get("conference_region")
        self.call_type: Optional[
            "ConferenceParticipantInstance.CallType"
        ] = payload.get("call_type")
        self.processing_state: Optional[
            "ConferenceParticipantInstance.ProcessingState"
        ] = payload.get("processing_state")
        self.properties: Optional[Dict[str, object]] = payload.get("properties")
        self.events: Optional[Dict[str, object]] = payload.get("events")
        self.metrics: Optional[Dict[str, object]] = payload.get("metrics")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "conference_sid": conference_sid,
            "participant_sid": participant_sid or self.participant_sid,
        }
        self._context: Optional[ConferenceParticipantContext] = None

    @property
    def _proxy(self) -> "ConferenceParticipantContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConferenceParticipantContext for this ConferenceParticipantInstance
        """
        if self._context is None:
            self._context = ConferenceParticipantContext(
                self._version,
                conference_sid=self._solution["conference_sid"],
                participant_sid=self._solution["participant_sid"],
            )
        return self._context

    def fetch(
        self,
        events: Union[str, object] = values.unset,
        metrics: Union[str, object] = values.unset,
    ) -> "ConferenceParticipantInstance":
        """
        Fetch the ConferenceParticipantInstance

        :param events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
        :param metrics: Object. Contains participant call quality metrics.

        :returns: The fetched ConferenceParticipantInstance
        """
        return self._proxy.fetch(
            events=events,
            metrics=metrics,
        )

    async def fetch_async(
        self,
        events: Union[str, object] = values.unset,
        metrics: Union[str, object] = values.unset,
    ) -> "ConferenceParticipantInstance":
        """
        Asynchronous coroutine to fetch the ConferenceParticipantInstance

        :param events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
        :param metrics: Object. Contains participant call quality metrics.

        :returns: The fetched ConferenceParticipantInstance
        """
        return await self._proxy.fetch_async(
            events=events,
            metrics=metrics,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.ConferenceParticipantInstance {}>".format(context)


class ConferenceParticipantContext(InstanceContext):
    def __init__(self, version: Version, conference_sid: str, participant_sid: str):
        """
        Initialize the ConferenceParticipantContext

        :param version: Version that contains the resource
        :param conference_sid: The unique SID identifier of the Conference.
        :param participant_sid: The unique SID identifier of the Participant.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "conference_sid": conference_sid,
            "participant_sid": participant_sid,
        }
        self._uri = (
            "/Conferences/{conference_sid}/Participants/{participant_sid}".format(
                **self._solution
            )
        )

    def fetch(
        self,
        events: Union[str, object] = values.unset,
        metrics: Union[str, object] = values.unset,
    ) -> ConferenceParticipantInstance:
        """
        Fetch the ConferenceParticipantInstance

        :param events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
        :param metrics: Object. Contains participant call quality metrics.

        :returns: The fetched ConferenceParticipantInstance
        """

        data = values.of(
            {
                "Events": events,
                "Metrics": metrics,
            }
        )

        payload = self._version.fetch(method="GET", uri=self._uri, params=data)

        return ConferenceParticipantInstance(
            self._version,
            payload,
            conference_sid=self._solution["conference_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    async def fetch_async(
        self,
        events: Union[str, object] = values.unset,
        metrics: Union[str, object] = values.unset,
    ) -> ConferenceParticipantInstance:
        """
        Asynchronous coroutine to fetch the ConferenceParticipantInstance

        :param events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
        :param metrics: Object. Contains participant call quality metrics.

        :returns: The fetched ConferenceParticipantInstance
        """

        data = values.of(
            {
                "Events": events,
                "Metrics": metrics,
            }
        )

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data
        )

        return ConferenceParticipantInstance(
            self._version,
            payload,
            conference_sid=self._solution["conference_sid"],
            participant_sid=self._solution["participant_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Insights.V1.ConferenceParticipantContext {}>".format(context)


class ConferenceParticipantPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ConferenceParticipantInstance:
        """
        Build an instance of ConferenceParticipantInstance

        :param payload: Payload response from the API
        """
        return ConferenceParticipantInstance(
            self._version, payload, conference_sid=self._solution["conference_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.ConferenceParticipantPage>"


class ConferenceParticipantList(ListResource):
    def __init__(self, version: Version, conference_sid: str):
        """
        Initialize the ConferenceParticipantList

        :param version: Version that contains the resource
        :param conference_sid: The unique SID identifier of the Conference.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "conference_sid": conference_sid,
        }
        self._uri = "/Conferences/{conference_sid}/Participants".format(
            **self._solution
        )

    def stream(
        self,
        participant_sid: Union[str, object] = values.unset,
        label: Union[str, object] = values.unset,
        events: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ConferenceParticipantInstance]:
        """
        Streams ConferenceParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str participant_sid: The unique SID identifier of the Participant.
        :param str label: User-specified label for a participant.
        :param str events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
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
            participant_sid=participant_sid,
            label=label,
            events=events,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        participant_sid: Union[str, object] = values.unset,
        label: Union[str, object] = values.unset,
        events: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ConferenceParticipantInstance]:
        """
        Asynchronously streams ConferenceParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str participant_sid: The unique SID identifier of the Participant.
        :param str label: User-specified label for a participant.
        :param str events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
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
            participant_sid=participant_sid,
            label=label,
            events=events,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        participant_sid: Union[str, object] = values.unset,
        label: Union[str, object] = values.unset,
        events: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ConferenceParticipantInstance]:
        """
        Lists ConferenceParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str participant_sid: The unique SID identifier of the Participant.
        :param str label: User-specified label for a participant.
        :param str events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
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
                participant_sid=participant_sid,
                label=label,
                events=events,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        participant_sid: Union[str, object] = values.unset,
        label: Union[str, object] = values.unset,
        events: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ConferenceParticipantInstance]:
        """
        Asynchronously lists ConferenceParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str participant_sid: The unique SID identifier of the Participant.
        :param str label: User-specified label for a participant.
        :param str events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
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
                participant_sid=participant_sid,
                label=label,
                events=events,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        participant_sid: Union[str, object] = values.unset,
        label: Union[str, object] = values.unset,
        events: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ConferenceParticipantPage:
        """
        Retrieve a single page of ConferenceParticipantInstance records from the API.
        Request is executed immediately

        :param participant_sid: The unique SID identifier of the Participant.
        :param label: User-specified label for a participant.
        :param events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ConferenceParticipantInstance
        """
        data = values.of(
            {
                "ParticipantSid": participant_sid,
                "Label": label,
                "Events": events,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ConferenceParticipantPage(self._version, response, self._solution)

    async def page_async(
        self,
        participant_sid: Union[str, object] = values.unset,
        label: Union[str, object] = values.unset,
        events: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ConferenceParticipantPage:
        """
        Asynchronously retrieve a single page of ConferenceParticipantInstance records from the API.
        Request is executed immediately

        :param participant_sid: The unique SID identifier of the Participant.
        :param label: User-specified label for a participant.
        :param events: Conference events generated by application or participant activity; e.g. `hold`, `mute`, etc.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ConferenceParticipantInstance
        """
        data = values.of(
            {
                "ParticipantSid": participant_sid,
                "Label": label,
                "Events": events,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ConferenceParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ConferenceParticipantPage:
        """
        Retrieve a specific page of ConferenceParticipantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ConferenceParticipantInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ConferenceParticipantPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ConferenceParticipantPage:
        """
        Asynchronously retrieve a specific page of ConferenceParticipantInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ConferenceParticipantInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ConferenceParticipantPage(self._version, response, self._solution)

    def get(self, participant_sid: str) -> ConferenceParticipantContext:
        """
        Constructs a ConferenceParticipantContext

        :param participant_sid: The unique SID identifier of the Participant.
        """
        return ConferenceParticipantContext(
            self._version,
            conference_sid=self._solution["conference_sid"],
            participant_sid=participant_sid,
        )

    def __call__(self, participant_sid: str) -> ConferenceParticipantContext:
        """
        Constructs a ConferenceParticipantContext

        :param participant_sid: The unique SID identifier of the Participant.
        """
        return ConferenceParticipantContext(
            self._version,
            conference_sid=self._solution["conference_sid"],
            participant_sid=participant_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.ConferenceParticipantList>"
