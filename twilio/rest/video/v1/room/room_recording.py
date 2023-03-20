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


from typing import Optional
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class RoomRecordingList(ListResource):
    def __init__(self, version: Version, room_sid: str):
        """
        Initialize the RoomRecordingList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the room with the RoomRecording resources to read.

        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingList
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
        }
        self._uri = "/Rooms/{room_sid}/Recordings".format(**self._solution)

    def stream(
        self,
        status=values.unset,
        source_sid=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Streams RoomRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param RoomRecordingInstance.Status status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_recording.RoomRecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            source_sid=source_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status=values.unset,
        source_sid=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously streams RoomRecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param RoomRecordingInstance.Status status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_recording.RoomRecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            status=status,
            source_sid=source_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status=values.unset,
        source_sid=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Lists RoomRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param RoomRecordingInstance.Status status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_recording.RoomRecordingInstance]
        """
        return list(
            self.stream(
                status=status,
                source_sid=source_sid,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status=values.unset,
        source_sid=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        limit=None,
        page_size=None,
    ):
        """
        Asynchronously lists RoomRecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param RoomRecordingInstance.Status status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.room_recording.RoomRecordingInstance]
        """
        return list(
            await self.stream_async(
                status=status,
                source_sid=source_sid,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        status=values.unset,
        source_sid=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Retrieve a single page of RoomRecordingInstance records from the API.
        Request is executed immediately

        :param RoomRecordingInstance.Status status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingPage
        """
        data = values.of(
            {
                "Status": status,
                "SourceSid": source_sid,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RoomRecordingPage(self._version, response, self._solution)

    async def page_async(
        self,
        status=values.unset,
        source_sid=values.unset,
        date_created_after=values.unset,
        date_created_before=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ):
        """
        Asynchronously retrieve a single page of RoomRecordingInstance records from the API.
        Request is executed immediately

        :param RoomRecordingInstance.Status status: Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingPage
        """
        data = values.of(
            {
                "Status": status,
                "SourceSid": source_sid,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return RoomRecordingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RoomRecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RoomRecordingPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of RoomRecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RoomRecordingPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a RoomRecordingContext

        :param sid: The SID of the RoomRecording resource to fetch.

        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        """
        return RoomRecordingContext(
            self._version, room_sid=self._solution["room_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a RoomRecordingContext

        :param sid: The SID of the RoomRecording resource to fetch.

        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        """
        return RoomRecordingContext(
            self._version, room_sid=self._solution["room_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Video.V1.RoomRecordingList>"


class RoomRecordingPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of RoomRecordingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        """
        return RoomRecordingInstance(
            self._version, payload, room_sid=self._solution["room_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.RoomRecordingPage>"


class RoomRecordingInstance(InstanceResource):
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

    def __init__(self, version, payload, room_sid: str, sid: Optional[str] = None):
        """
        Initialize the RoomRecordingInstance

        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "status": payload.get("status"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "sid": payload.get("sid"),
            "source_sid": payload.get("source_sid"),
            "size": payload.get("size"),
            "url": payload.get("url"),
            "type": payload.get("type"),
            "duration": deserialize.integer(payload.get("duration")),
            "container_format": payload.get("container_format"),
            "codec": payload.get("codec"),
            "grouping_sids": payload.get("grouping_sids"),
            "track_name": payload.get("track_name"),
            "offset": payload.get("offset"),
            "media_external_location": payload.get("media_external_location"),
            "room_sid": payload.get("room_sid"),
            "links": payload.get("links"),
        }

        self._solution = {
            "room_sid": room_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[RoomRecordingContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoomRecordingContext for this RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        """
        if self._context is None:
            self._context = RoomRecordingContext(
                self._version,
                room_sid=self._solution["room_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RoomRecording resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def status(self):
        """
        :returns:
        :rtype: RoomRecordingInstance.Status
        """
        return self._properties["status"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the RoomRecording resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def source_sid(self):
        """
        :returns: The SID of the recording source. For a Room Recording, this value is a `track_sid`.
        :rtype: str
        """
        return self._properties["source_sid"]

    @property
    def size(self):
        """
        :returns: The size of the recorded track in bytes.
        :rtype: int
        """
        return self._properties["size"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def type(self):
        """
        :returns:
        :rtype: RoomRecordingInstance.Type
        """
        return self._properties["type"]

    @property
    def duration(self):
        """
        :returns: The duration of the recording rounded to the nearest second. Sub-second duration tracks have a `duration` of 1 second
        :rtype: int
        """
        return self._properties["duration"]

    @property
    def container_format(self):
        """
        :returns:
        :rtype: RoomRecordingInstance.Format
        """
        return self._properties["container_format"]

    @property
    def codec(self):
        """
        :returns:
        :rtype: RoomRecordingInstance.Codec
        """
        return self._properties["codec"]

    @property
    def grouping_sids(self):
        """
        :returns: A list of SIDs related to the Recording. Includes the `room_sid` and `participant_sid`.
        :rtype: dict
        """
        return self._properties["grouping_sids"]

    @property
    def track_name(self):
        """
        :returns: The name that was given to the source track of the recording. If no name is given, the `source_sid` is used.
        :rtype: str
        """
        return self._properties["track_name"]

    @property
    def offset(self):
        """
        :returns: The time in milliseconds elapsed between an arbitrary point in time, common to all group rooms, and the moment when the source room of this track started. This information provides a synchronization mechanism for recordings belonging to the same room.
        :rtype: int
        """
        return self._properties["offset"]

    @property
    def media_external_location(self):
        """
        :returns: The URL of the media file associated with the recording when stored externally. See [External S3 Recordings](/docs/video/api/external-s3-recordings) for more details.
        :rtype: str
        """
        return self._properties["media_external_location"]

    @property
    def room_sid(self):
        """
        :returns: The SID of the Room resource the recording is associated with.
        :rtype: str
        """
        return self._properties["room_sid"]

    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties["links"]

    def delete(self):
        """
        Deletes the RoomRecordingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the RoomRecordingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the RoomRecordingInstance


        :returns: The fetched RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the RoomRecordingInstance


        :returns: The fetched RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.RoomRecordingInstance {}>".format(context)


class RoomRecordingContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str, sid: str):
        """
        Initialize the RoomRecordingContext

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the Room resource with the recording to fetch.
        :param sid: The SID of the RoomRecording resource to fetch.

        :returns: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "room_sid": room_sid,
            "sid": sid,
        }
        self._uri = "/Rooms/{room_sid}/Recordings/{sid}".format(**self._solution)

    def delete(self):
        """
        Deletes the RoomRecordingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the RoomRecordingInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the RoomRecordingInstance


        :returns: The fetched RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RoomRecordingInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the RoomRecordingInstance


        :returns: The fetched RoomRecordingInstance
        :rtype: twilio.rest.video.v1.room.room_recording.RoomRecordingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RoomRecordingInstance(
            self._version,
            payload,
            room_sid=self._solution["room_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Video.V1.RoomRecordingContext {}>".format(context)
