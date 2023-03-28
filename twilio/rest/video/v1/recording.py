r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
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


class RecordingInstance(InstanceResource):
    class Codec(object):
        VP8 = "VP8"
        H264 = "H264"
        OPUS = "OPUS"
        PCMU = "PCMU"

    class Format(object):
        MKA = "mka"
        MKV = "mkv"

    class Status(object):
        PROCESSING = "processing"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"

    class Type(object):
        AUDIO = "audio"
        VIDEO = "video"
        DATA = "data"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource.
    :ivar status: 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar sid: The unique string that we created to identify the Recording resource.
    :ivar source_sid: The SID of the recording source. For a Room Recording, this value is a `track_sid`.
    :ivar size: The size of the recorded track, in bytes.
    :ivar url: The absolute URL of the resource.
    :ivar type: 
    :ivar duration: The duration of the recording in seconds rounded to the nearest second. Sub-second tracks have a `Duration` property of 1 second
    :ivar container_format: 
    :ivar codec: 
    :ivar grouping_sids: A list of SIDs related to the recording. Includes the `room_sid` and `participant_sid`.
    :ivar track_name: The name that was given to the source track of the recording. If no name is given, the `source_sid` is used.
    :ivar offset: The time in milliseconds elapsed between an arbitrary point in time, common to all group rooms, and the moment when the source room of this track started. This information provides a synchronization mechanism for recordings belonging to the same room.
    :ivar media_external_location: The URL of the media file associated with the recording when stored externally. See [External S3 Recordings](/docs/video/api/external-s3-recordings) for more details.
    :ivar status_callback: The URL called using the `status_callback_method` to send status information on every recording event.
    :ivar status_callback_method: The HTTP method used to call `status_callback`. Can be: `POST` or `GET`, defaults to `POST`.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.status: Optional["RecordingInstance.Status"] = payload.get("status")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.sid: Optional[str] = payload.get("sid")
        self.source_sid: Optional[str] = payload.get("source_sid")
        self.size: Optional[int] = payload.get("size")
        self.url: Optional[str] = payload.get("url")
        self.type: Optional["RecordingInstance.Type"] = payload.get("type")
        self.duration: Optional[int] = deserialize.integer(payload.get("duration"))
        self.container_format: Optional["RecordingInstance.Format"] = payload.get(
            "container_format"
        )
        self.codec: Optional["RecordingInstance.Codec"] = payload.get("codec")
        self.grouping_sids: Optional[Dict[str, object]] = payload.get("grouping_sids")
        self.track_name: Optional[str] = payload.get("track_name")
        self.offset: Optional[int] = payload.get("offset")
        self.media_external_location: Optional[str] = payload.get(
            "media_external_location"
        )
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[RecordingContext] = None

    @property
    def _proxy(self) -> "RecordingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RecordingContext for this RecordingInstance
        """
        if self._context is None:
            self._context = RecordingContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the RecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "RecordingInstance":
        """
        Fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RecordingInstance":
        """
        Asynchronous coroutine to fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.RecordingInstance {}>".format(context)


class RecordingContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the RecordingContext

        :param version: Version that contains the resource
        :param sid: The SID of the Recording resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Recordings/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the RecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RecordingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> RecordingInstance:
        """
        Fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RecordingInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RecordingInstance:
        """
        Asynchronous coroutine to fetch the RecordingInstance


        :returns: The fetched RecordingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RecordingInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.RecordingContext {}>".format(context)


class RecordingPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> RecordingInstance:
        """
        Build an instance of RecordingInstance

        :param payload: Payload response from the API
        """
        return RecordingInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.RecordingPage>"


class RecordingList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the RecordingList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Recordings"

    def stream(
        self,
        status: Union["RecordingInstance.Status", object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        grouping_sid: Union[List[str], object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        media_type: Union["RecordingInstance.Type", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RecordingInstance]:
        """
        Streams RecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;RecordingInstance.Status&quot; status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param List[str] grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param &quot;RecordingInstance.Type&quot; media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
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
            status=status,
            source_sid=source_sid,
            grouping_sid=grouping_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            media_type=media_type,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status: Union["RecordingInstance.Status", object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        grouping_sid: Union[List[str], object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        media_type: Union["RecordingInstance.Type", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RecordingInstance]:
        """
        Asynchronously streams RecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;RecordingInstance.Status&quot; status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param List[str] grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param &quot;RecordingInstance.Type&quot; media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
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
            status=status,
            source_sid=source_sid,
            grouping_sid=grouping_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            media_type=media_type,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status: Union["RecordingInstance.Status", object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        grouping_sid: Union[List[str], object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        media_type: Union["RecordingInstance.Type", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RecordingInstance]:
        """
        Lists RecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;RecordingInstance.Status&quot; status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param List[str] grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param &quot;RecordingInstance.Type&quot; media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
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
                status=status,
                source_sid=source_sid,
                grouping_sid=grouping_sid,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                media_type=media_type,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status: Union["RecordingInstance.Status", object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        grouping_sid: Union[List[str], object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        media_type: Union["RecordingInstance.Type", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RecordingInstance]:
        """
        Asynchronously lists RecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;RecordingInstance.Status&quot; status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param List[str] grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param &quot;RecordingInstance.Type&quot; media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
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
                status=status,
                source_sid=source_sid,
                grouping_sid=grouping_sid,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                media_type=media_type,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        status: Union["RecordingInstance.Status", object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        grouping_sid: Union[List[str], object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        media_type: Union["RecordingInstance.Type", object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> RecordingPage:
        """
        Retrieve a single page of RecordingInstance records from the API.
        Request is executed immediately

        :param status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param source_sid: Read only the recordings that have this `source_sid`.
        :param grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RecordingInstance
        """
        data = values.of(
            {
                "Status": status,
                "SourceSid": source_sid,
                "GroupingSid": serialize.map(grouping_sid, lambda e: e),
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "MediaType": media_type,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RecordingPage(self._version, response)

    async def page_async(
        self,
        status: Union["RecordingInstance.Status", object] = values.unset,
        source_sid: Union[str, object] = values.unset,
        grouping_sid: Union[List[str], object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        media_type: Union["RecordingInstance.Type", object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> RecordingPage:
        """
        Asynchronously retrieve a single page of RecordingInstance records from the API.
        Request is executed immediately

        :param status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param source_sid: Read only the recordings that have this `source_sid`.
        :param grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RecordingInstance
        """
        data = values.of(
            {
                "Status": status,
                "SourceSid": source_sid,
                "GroupingSid": serialize.map(grouping_sid, lambda e: e),
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "MediaType": media_type,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return RecordingPage(self._version, response)

    def get_page(self, target_url: str) -> RecordingPage:
        """
        Retrieve a specific page of RecordingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RecordingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RecordingPage(self._version, response)

    async def get_page_async(self, target_url: str) -> RecordingPage:
        """
        Asynchronously retrieve a specific page of RecordingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RecordingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RecordingPage(self._version, response)

    def get(self, sid: str) -> RecordingContext:
        """
        Constructs a RecordingContext

        :param sid: The SID of the Recording resource to fetch.
        """
        return RecordingContext(self._version, sid=sid)

    def __call__(self, sid: str) -> RecordingContext:
        """
        Constructs a RecordingContext

        :param sid: The SID of the Recording resource to fetch.
        """
        return RecordingContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.RecordingList>"
