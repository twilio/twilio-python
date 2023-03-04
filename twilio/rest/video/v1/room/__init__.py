"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.video.v1.room.participant import ParticipantList
from twilio.rest.video.v1.room.recording_rules import RecordingRulesList
from twilio.rest.video.v1.room.room_recording import RoomRecordingList


class RoomList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the RoomList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.video.v1.room.RoomList
        :rtype: twilio.rest.video.v1.room.RoomList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Rooms'.format(**self._solution)
        
        
    
    
    
    def create(self, enable_turn=values.unset, type=values.unset, unique_name=values.unset, status_callback=values.unset, status_callback_method=values.unset, max_participants=values.unset, record_participants_on_connect=values.unset, video_codecs=values.unset, media_region=values.unset, recording_rules=values.unset, audio_only=values.unset, max_participant_duration=values.unset, empty_room_timeout=values.unset, unused_room_timeout=values.unset, large_room=values.unset):
        """
        Create the RoomInstance

        :param bool enable_turn: Deprecated, now always considered to be true.
        :param RoomRoomType type: 
        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be `POST` or `GET`.
        :param int max_participants: The maximum number of concurrent Participants allowed in the room. Peer-to-peer rooms can have up to 10 Participants. Small Group rooms can have up to 4 Participants. Group rooms can have up to 50 Participants.
        :param bool record_participants_on_connect: Whether to start recording when Participants connect. ***This feature is not available in `peer-to-peer` rooms.***
        :param list[RoomVideoCodec] video_codecs: An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.  ***This feature is not available in `peer-to-peer` rooms***
        :param str media_region: The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-address-whitelisting#group-rooms-media-servers). ***This feature is not available in `peer-to-peer` rooms.***
        :param object recording_rules: A collection of Recording Rules that describe how to include or exclude matching tracks for recording
        :param bool audio_only: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only.
        :param int max_participant_duration: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
        :param int empty_room_timeout: Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions).
        :param int unused_room_timeout: Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions).
        :param bool large_room: When set to true, indicated that this is the large room.
        
        :returns: The created RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomInstance
        """
        data = values.of({ 
            'EnableTurn': enable_turn,
            'Type': type,
            'UniqueName': unique_name,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'MaxParticipants': max_participants,
            'RecordParticipantsOnConnect': record_participants_on_connect,
            'VideoCodecs': serialize.map(video_codecs, lambda e: e),
            'MediaRegion': media_region,
            'RecordingRules': serialize.object(recording_rules),
            'AudioOnly': audio_only,
            'MaxParticipantDuration': max_participant_duration,
            'EmptyRoomTimeout': empty_room_timeout,
            'UnusedRoomTimeout': unused_room_timeout,
            'LargeRoom': large_room,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return RoomInstance(self._version, payload)
    
    
    def stream(self, status=values.unset, unique_name=values.unset, date_created_after=values.unset, date_created_before=values.unset, limit=None, page_size=None):
        """
        Streams RoomInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param RoomRoomStatus status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.RoomInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            unique_name=unique_name,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, unique_name=values.unset, date_created_after=values.unset, date_created_before=values.unset, limit=None, page_size=None):
        """
        Lists RoomInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param RoomRoomStatus status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.room.RoomInstance]
        """
        return list(self.stream(
            status=status,
            unique_name=unique_name,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, unique_name=values.unset, date_created_after=values.unset, date_created_before=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RoomInstance records from the API.
        Request is executed immediately
        
        :param RoomRoomStatus status: Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
        :param str unique_name: Read only rooms with the this `unique_name`.
        :param datetime date_created_after: Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
        :param datetime date_created_before: Read only rooms that started before this date, given as `YYYY-MM-DD`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomPage
        """
        data = values.of({ 
            'Status': status,
            'UniqueName': unique_name,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RoomPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RoomInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RoomPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a RoomContext
        
        :param sid: The SID of the Room resource to update.
        
        :returns: twilio.rest.video.v1.room.RoomContext
        :rtype: twilio.rest.video.v1.room.RoomContext
        """
        return RoomContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a RoomContext
        
        :param sid: The SID of the Room resource to update.
        
        :returns: twilio.rest.video.v1.room.RoomContext
        :rtype: twilio.rest.video.v1.room.RoomContext
        """
        return RoomContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RoomList>'








class RoomPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RoomPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.room.RoomPage
        :rtype: twilio.rest.video.v1.room.RoomPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RoomInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.room.RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomInstance
        """
        return RoomInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RoomPage>'




class RoomInstance(InstanceResource):

    class RoomRoomStatus(object):
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        FAILED = "failed"

    class RoomRoomType(object):
        GO = "go"
        PEER_TO_PEER = "peer-to-peer"
        GROUP = "group"
        GROUP_SMALL = "group-small"

    class RoomVideoCodec(object):
        VP8 = "VP8"
        H264 = "H264"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the RoomInstance
        :returns: twilio.rest.video.v1.room.RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'status': payload.get('status'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'account_sid': payload.get('account_sid'),
            'enable_turn': payload.get('enable_turn'),
            'unique_name': payload.get('unique_name'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'end_time': deserialize.iso8601_datetime(payload.get('end_time')),
            'duration': deserialize.integer(payload.get('duration')),
            'type': payload.get('type'),
            'max_participants': deserialize.integer(payload.get('max_participants')),
            'max_participant_duration': deserialize.integer(payload.get('max_participant_duration')),
            'max_concurrent_published_tracks': deserialize.integer(payload.get('max_concurrent_published_tracks')),
            'record_participants_on_connect': payload.get('record_participants_on_connect'),
            'video_codecs': payload.get('video_codecs'),
            'media_region': payload.get('media_region'),
            'audio_only': payload.get('audio_only'),
            'empty_room_timeout': deserialize.integer(payload.get('empty_room_timeout')),
            'unused_room_timeout': deserialize.integer(payload.get('unused_room_timeout')),
            'large_room': payload.get('large_room'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoomContext for this RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomContext
        """
        if self._context is None:
            self._context = RoomContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Room resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: RoomRoomStatus
        """
        return self._properties['status']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Room resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def enable_turn(self):
        """
        :returns: Deprecated, now always considered to be true.
        :rtype: bool
        """
        return self._properties['enable_turn']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def status_callback(self):
        """
        :returns: The URL we call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
        :rtype: str
        """
        return self._properties['status_callback']
    
    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we use to call `status_callback`. Can be `POST` or `GET` and defaults to `POST`.
        :rtype: str
        """
        return self._properties['status_callback_method']
    
    @property
    def end_time(self):
        """
        :returns: The UTC end time of the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :rtype: datetime
        """
        return self._properties['end_time']
    
    @property
    def duration(self):
        """
        :returns: The duration of the room in seconds.
        :rtype: int
        """
        return self._properties['duration']
    
    @property
    def type(self):
        """
        :returns: 
        :rtype: RoomRoomType
        """
        return self._properties['type']
    
    @property
    def max_participants(self):
        """
        :returns: The maximum number of concurrent Participants allowed in the room. 
        :rtype: int
        """
        return self._properties['max_participants']
    
    @property
    def max_participant_duration(self):
        """
        :returns: The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
        :rtype: int
        """
        return self._properties['max_participant_duration']
    
    @property
    def max_concurrent_published_tracks(self):
        """
        :returns: The maximum number of published audio, video, and data tracks all participants combined are allowed to publish in the room at the same time. Check [Programmable Video Limits](https://www.twilio.com/docs/video/programmable-video-limits) for more details. If it is set to 0 it means unconstrained.
        :rtype: int
        """
        return self._properties['max_concurrent_published_tracks']
    
    @property
    def record_participants_on_connect(self):
        """
        :returns: Whether to start recording when Participants connect. ***This feature is not available in `peer-to-peer` rooms.***
        :rtype: bool
        """
        return self._properties['record_participants_on_connect']
    
    @property
    def video_codecs(self):
        """
        :returns: An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.  ***This feature is not available in `peer-to-peer` rooms***
        :rtype: list[RoomVideoCodec]
        """
        return self._properties['video_codecs']
    
    @property
    def media_region(self):
        """
        :returns: The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-address-whitelisting#media-servers). ***This feature is not available in `peer-to-peer` rooms.***
        :rtype: str
        """
        return self._properties['media_region']
    
    @property
    def audio_only(self):
        """
        :returns: When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only.
        :rtype: bool
        """
        return self._properties['audio_only']
    
    @property
    def empty_room_timeout(self):
        """
        :returns: Specifies how long (in minutes) a room will remain active after last participant leaves. Can be configured when creating a room via REST API. For Ad-Hoc rooms this value cannot be changed.
        :rtype: int
        """
        return self._properties['empty_room_timeout']
    
    @property
    def unused_room_timeout(self):
        """
        :returns: Specifies how long (in minutes) a room will remain active if no one joins. Can be configured when creating a room via REST API. For Ad-Hoc rooms this value cannot be changed.
        :rtype: int
        """
        return self._properties['unused_room_timeout']
    
    @property
    def large_room(self):
        """
        :returns: Indicates if this is a large room.
        :rtype: bool
        """
        return self._properties['large_room']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    def fetch(self):
        """
        Fetch the RoomInstance
        

        :returns: The fetched RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomInstance
        """
        return self._proxy.fetch()
    
    def update(self, status):
        """
        Update the RoomInstance
        
        :params RoomRoomStatus status: 

        :returns: The updated RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomInstance
        """
        return self._proxy.update(status=status, )
    
    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.video.v1.room.ParticipantList
        :rtype: twilio.rest.video.v1.room.ParticipantList
        """
        return self._proxy.participants
    
    @property
    def recording_rules(self):
        """
        Access the recording_rules

        :returns: twilio.rest.video.v1.room.RecordingRulesList
        :rtype: twilio.rest.video.v1.room.RecordingRulesList
        """
        return self._proxy.recording_rules
    
    @property
    def recordings(self):
        """
        Access the recordings

        :returns: twilio.rest.video.v1.room.RoomRecordingList
        :rtype: twilio.rest.video.v1.room.RoomRecordingList
        """
        return self._proxy.recordings
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RoomInstance {}>'.format(context)

class RoomContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the RoomContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Room resource to update.

        :returns: twilio.rest.video.v1.room.RoomContext
        :rtype: twilio.rest.video.v1.room.RoomContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Rooms/{sid}'.format(**self._solution)
        
        self._participants = None
        self._recording_rules = None
        self._recordings = None
    
    def fetch(self):
        """
        Fetch the RoomInstance
        

        :returns: The fetched RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RoomInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, status):
        """
        Update the RoomInstance
        
        :params RoomRoomStatus status: 

        :returns: The updated RoomInstance
        :rtype: twilio.rest.video.v1.room.RoomInstance
        """
        data = values.of({ 
            'Status': status,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return RoomInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.video.v1.room.ParticipantList
        :rtype: twilio.rest.video.v1.room.ParticipantList
        """
        if self._participants is None:
            self._participants = ParticipantList(self._version, self._solution['sid'],
            )
        return self._participants
    
    @property
    def recording_rules(self):
        """
        Access the recording_rules

        :returns: twilio.rest.video.v1.room.RecordingRulesList
        :rtype: twilio.rest.video.v1.room.RecordingRulesList
        """
        if self._recording_rules is None:
            self._recording_rules = RecordingRulesList(self._version, self._solution['sid'],
            )
        return self._recording_rules
    
    @property
    def recordings(self):
        """
        Access the recordings

        :returns: twilio.rest.video.v1.room.RoomRecordingList
        :rtype: twilio.rest.video.v1.room.RoomRecordingList
        """
        if self._recordings is None:
            self._recordings = RoomRecordingList(self._version, self._solution['sid'],
            )
        return self._recordings
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RoomContext {}>'.format(context)


