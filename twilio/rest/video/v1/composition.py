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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CompositionInstance(InstanceResource):

    class Format:
        MP4 = "mp4"
        WEBM = "webm"

    class Status:
        ENQUEUED = "enqueued"
        PROCESSING = "processing"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Composition resource.
    :ivar status: 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_completed: The date and time in GMT when the composition's media processing task finished, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_deleted: The date and time in GMT when the composition generated media was deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar sid: The unique string that we created to identify the Composition resource.
    :ivar room_sid: The SID of the Group Room that generated the audio and video tracks used in the composition. All media sources included in a composition must belong to the same Group Room.
    :ivar audio_sources: The array of track names to include in the composition. The composition includes all audio sources specified in `audio_sources` except those specified in `audio_sources_excluded`. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` includes tracks named `student` as well as `studentTeam`.
    :ivar audio_sources_excluded: The array of track names to exclude from the composition. The composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
    :ivar video_layout: An object that describes the video layout of the composition in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :ivar resolution: The dimensions of the video image in pixels expressed as columns (width) and rows (height). The string's format is `{width}x{height}`, such as `640x480`.
    :ivar trim: Whether to remove intervals with no media, as specified in the POST request that created the composition. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
    :ivar format: 
    :ivar bitrate: The average bit rate of the composition's media.
    :ivar size: The size of the composed media file in bytes.
    :ivar duration: The duration of the composition's media file in seconds.
    :ivar media_external_location: The URL of the media file associated with the composition when stored externally. See [External S3 Compositions](/docs/video/api/external-s3-compositions) for more details.
    :ivar status_callback: The URL called using the `status_callback_method` to send status information on every composition event.
    :ivar status_callback_method: The HTTP method used to call `status_callback`. Can be: `POST` or `GET`, defaults to `POST`.
    :ivar url: The absolute URL of the resource.
    :ivar links: The URL of the media file associated with the composition.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.status: Optional["CompositionInstance.Status"] = payload.get("status")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_completed: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_completed")
        )
        self.date_deleted: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_deleted")
        )
        self.sid: Optional[str] = payload.get("sid")
        self.room_sid: Optional[str] = payload.get("room_sid")
        self.audio_sources: Optional[List[str]] = payload.get("audio_sources")
        self.audio_sources_excluded: Optional[List[str]] = payload.get(
            "audio_sources_excluded"
        )
        self.video_layout: Optional[Dict[str, object]] = payload.get("video_layout")
        self.resolution: Optional[str] = payload.get("resolution")
        self.trim: Optional[bool] = payload.get("trim")
        self.format: Optional["CompositionInstance.Format"] = payload.get("format")
        self.bitrate: Optional[int] = deserialize.integer(payload.get("bitrate"))
        self.size: Optional[int] = payload.get("size")
        self.duration: Optional[int] = deserialize.integer(payload.get("duration"))
        self.media_external_location: Optional[str] = payload.get(
            "media_external_location"
        )
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[CompositionContext] = None

    @property
    def _proxy(self) -> "CompositionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CompositionContext for this CompositionInstance
        """
        if self._context is None:
            self._context = CompositionContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the CompositionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CompositionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "CompositionInstance":
        """
        Fetch the CompositionInstance


        :returns: The fetched CompositionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CompositionInstance":
        """
        Asynchronous coroutine to fetch the CompositionInstance


        :returns: The fetched CompositionInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Video.V1.CompositionInstance {context}>"


class CompositionContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CompositionContext

        :param version: Version that contains the resource
        :param sid: The SID of the Composition resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Compositions/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the CompositionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CompositionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> CompositionInstance:
        """
        Fetch the CompositionInstance


        :returns: The fetched CompositionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CompositionInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CompositionInstance:
        """
        Asynchronous coroutine to fetch the CompositionInstance


        :returns: The fetched CompositionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CompositionInstance(
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
        return f"<Twilio.Video.V1.CompositionContext {context}>"


class CompositionPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> CompositionInstance:
        """
        Build an instance of CompositionInstance

        :param payload: Payload response from the API
        """
        return CompositionInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.CompositionPage>"


class CompositionList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CompositionList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Compositions"

    def create(
        self,
        room_sid: str,
        video_layout: Union[object, object] = values.unset,
        audio_sources: Union[List[str], object] = values.unset,
        audio_sources_excluded: Union[List[str], object] = values.unset,
        resolution: Union[str, object] = values.unset,
        format: Union["CompositionInstance.Format", object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        trim: Union[bool, object] = values.unset,
    ) -> CompositionInstance:
        """
        Create the CompositionInstance

        :param room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
        :param video_layout: An object that describes the video layout of the composition in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :param audio_sources: An array of track names from the same group room to merge into the new composition. Can include zero or more track names. The new composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, `student*` includes `student` as well as `studentTeam`. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :param audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :param resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to `640x480`.  The string's format is `{width}x{height}` where:   * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 * `{width}` * `{height}` <= 921,600  Typical values are:   * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF = `320x240`  Note that the `resolution` imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param format:
        :param status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
        :param status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
        :param trim: Whether to clip the intervals where there is no active media in the composition. The default is `true`. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.

        :returns: The created CompositionInstance
        """

        data = values.of(
            {
                "RoomSid": room_sid,
                "VideoLayout": serialize.object(video_layout),
                "AudioSources": serialize.map(audio_sources, lambda e: e),
                "AudioSourcesExcluded": serialize.map(
                    audio_sources_excluded, lambda e: e
                ),
                "Resolution": resolution,
                "Format": format,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "Trim": serialize.boolean_to_string(trim),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CompositionInstance(self._version, payload)

    async def create_async(
        self,
        room_sid: str,
        video_layout: Union[object, object] = values.unset,
        audio_sources: Union[List[str], object] = values.unset,
        audio_sources_excluded: Union[List[str], object] = values.unset,
        resolution: Union[str, object] = values.unset,
        format: Union["CompositionInstance.Format", object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        trim: Union[bool, object] = values.unset,
    ) -> CompositionInstance:
        """
        Asynchronously create the CompositionInstance

        :param room_sid: The SID of the Group Room with the media tracks to be used as composition sources.
        :param video_layout: An object that describes the video layout of the composition in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :param audio_sources: An array of track names from the same group room to merge into the new composition. Can include zero or more track names. The new composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, `student*` includes `student` as well as `studentTeam`. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :param audio_sources_excluded: An array of track names to exclude. The new composition includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which will match zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :param resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to `640x480`.  The string's format is `{width}x{height}` where:   * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 * `{width}` * `{height}` <= 921,600  Typical values are:   * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF = `320x240`  Note that the `resolution` imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param format:
        :param status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
        :param status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
        :param trim: Whether to clip the intervals where there is no active media in the composition. The default is `true`. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.

        :returns: The created CompositionInstance
        """

        data = values.of(
            {
                "RoomSid": room_sid,
                "VideoLayout": serialize.object(video_layout),
                "AudioSources": serialize.map(audio_sources, lambda e: e),
                "AudioSourcesExcluded": serialize.map(
                    audio_sources_excluded, lambda e: e
                ),
                "Resolution": resolution,
                "Format": format,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "Trim": serialize.boolean_to_string(trim),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return CompositionInstance(self._version, payload)

    def stream(
        self,
        status: Union["CompositionInstance.Status", object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        room_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[CompositionInstance]:
        """
        Streams CompositionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;CompositionInstance.Status&quot; status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
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
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            room_sid=room_sid,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        status: Union["CompositionInstance.Status", object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        room_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[CompositionInstance]:
        """
        Asynchronously streams CompositionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;CompositionInstance.Status&quot; status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
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
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            room_sid=room_sid,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        status: Union["CompositionInstance.Status", object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        room_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CompositionInstance]:
        """
        Lists CompositionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;CompositionInstance.Status&quot; status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
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
                status=status,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                room_sid=room_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        status: Union["CompositionInstance.Status", object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        room_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CompositionInstance]:
        """
        Asynchronously lists CompositionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;CompositionInstance.Status&quot; status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param str room_sid: Read only Composition resources with this Room SID.
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
                status=status,
                date_created_after=date_created_after,
                date_created_before=date_created_before,
                room_sid=room_sid,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        status: Union["CompositionInstance.Status", object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        room_sid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CompositionPage:
        """
        Retrieve a single page of CompositionInstance records from the API.
        Request is executed immediately

        :param status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param room_sid: Read only Composition resources with this Room SID.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CompositionInstance
        """
        data = values.of(
            {
                "Status": status,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "RoomSid": room_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CompositionPage(self._version, response)

    async def page_async(
        self,
        status: Union["CompositionInstance.Status", object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        room_sid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CompositionPage:
        """
        Asynchronously retrieve a single page of CompositionInstance records from the API.
        Request is executed immediately

        :param status: Read only Composition resources with this status. Can be: `enqueued`, `processing`, `completed`, `deleted`, or `failed`.
        :param date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone.
        :param room_sid: Read only Composition resources with this Room SID.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CompositionInstance
        """
        data = values.of(
            {
                "Status": status,
                "DateCreatedAfter": serialize.iso8601_datetime(date_created_after),
                "DateCreatedBefore": serialize.iso8601_datetime(date_created_before),
                "RoomSid": room_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return CompositionPage(self._version, response)

    def get_page(self, target_url: str) -> CompositionPage:
        """
        Retrieve a specific page of CompositionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CompositionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CompositionPage(self._version, response)

    async def get_page_async(self, target_url: str) -> CompositionPage:
        """
        Asynchronously retrieve a specific page of CompositionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CompositionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CompositionPage(self._version, response)

    def get(self, sid: str) -> CompositionContext:
        """
        Constructs a CompositionContext

        :param sid: The SID of the Composition resource to fetch.
        """
        return CompositionContext(self._version, sid=sid)

    def __call__(self, sid: str) -> CompositionContext:
        """
        Constructs a CompositionContext

        :param sid: The SID of the Composition resource to fetch.
        """
        return CompositionContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Video.V1.CompositionList>"
