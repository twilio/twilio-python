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


class RecordingList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the RecordingList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.video.v1.recording.RecordingList
        :rtype: twilio.rest.video.v1.recording.RecordingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Recordings'.format(**self._solution)
        
        
    
    
    
    def stream(self, status=values.unset, source_sid=values.unset, grouping_sid=values.unset, date_created_after=values.unset, date_created_before=values.unset, media_type=values.unset, limit=None, page_size=None):
        """
        Streams RecordingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param RecordingInstance.Status status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param list[str] grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param RecordingInstance.Type media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.recording.RecordingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            source_sid=source_sid,
            grouping_sid=grouping_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            media_type=media_type,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, source_sid=values.unset, grouping_sid=values.unset, date_created_after=values.unset, date_created_before=values.unset, media_type=values.unset, limit=None, page_size=None):
        """
        Lists RecordingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param RecordingInstance.Status status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param list[str] grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param RecordingInstance.Type media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.recording.RecordingInstance]
        """
        return list(self.stream(
            status=status,
            source_sid=source_sid,
            grouping_sid=grouping_sid,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            media_type=media_type,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, source_sid=values.unset, grouping_sid=values.unset, date_created_after=values.unset, date_created_before=values.unset, media_type=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RecordingInstance records from the API.
        Request is executed immediately
        
        :param RecordingInstance.Status status: Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
        :param str source_sid: Read only the recordings that have this `source_sid`.
        :param list[str] grouping_sid: Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
        :param datetime date_created_after: Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
        :param datetime date_created_before: Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
        :param RecordingInstance.Type media_type: Read only recordings that have this media type. Can be either `audio` or `video`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RecordingInstance
        :rtype: twilio.rest.video.v1.recording.RecordingPage
        """
        data = values.of({ 
            'Status': status,
            'SourceSid': source_sid,
            'GroupingSid': serialize.map(grouping_sid, lambda e: e),
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'MediaType': media_type,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RecordingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RecordingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RecordingInstance
        :rtype: twilio.rest.video.v1.recording.RecordingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RecordingPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a RecordingContext
        
        :param sid: The SID of the Recording resource to fetch.
        
        :returns: twilio.rest.video.v1.recording.RecordingContext
        :rtype: twilio.rest.video.v1.recording.RecordingContext
        """
        return RecordingContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a RecordingContext
        
        :param sid: The SID of the Recording resource to fetch.
        
        :returns: twilio.rest.video.v1.recording.RecordingContext
        :rtype: twilio.rest.video.v1.recording.RecordingContext
        """
        return RecordingContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RecordingList>'






class RecordingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RecordingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.recording.RecordingPage
        :rtype: twilio.rest.video.v1.recording.RecordingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RecordingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.recording.RecordingInstance
        :rtype: twilio.rest.video.v1.recording.RecordingInstance
        """
        return RecordingInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.RecordingPage>'




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

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the RecordingInstance
        :returns: twilio.rest.video.v1.recording.RecordingInstance
        :rtype: twilio.rest.video.v1.recording.RecordingInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'status': payload.get('status'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'sid': payload.get('sid'),
            'source_sid': payload.get('source_sid'),
            'size': payload.get('size'),
            'url': payload.get('url'),
            'type': payload.get('type'),
            'duration': deserialize.integer(payload.get('duration')),
            'container_format': payload.get('container_format'),
            'codec': payload.get('codec'),
            'grouping_sids': payload.get('grouping_sids'),
            'track_name': payload.get('track_name'),
            'offset': payload.get('offset'),
            'media_external_location': payload.get('media_external_location'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RecordingContext for this RecordingInstance
        :rtype: twilio.rest.video.v1.recording.RecordingContext
        """
        if self._context is None:
            self._context = RecordingContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: RecordingInstance.Status
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
    def sid(self):
        """
        :returns: The unique string that we created to identify the Recording resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def source_sid(self):
        """
        :returns: The SID of the recording source. For a Room Recording, this value is a `track_sid`.
        :rtype: str
        """
        return self._properties['source_sid']
    
    @property
    def size(self):
        """
        :returns: The size of the recorded track, in bytes.
        :rtype: int
        """
        return self._properties['size']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def type(self):
        """
        :returns: 
        :rtype: RecordingInstance.Type
        """
        return self._properties['type']
    
    @property
    def duration(self):
        """
        :returns: The duration of the recording in seconds rounded to the nearest second. Sub-second tracks have a `Duration` property of 1 second
        :rtype: int
        """
        return self._properties['duration']
    
    @property
    def container_format(self):
        """
        :returns: 
        :rtype: RecordingInstance.Format
        """
        return self._properties['container_format']
    
    @property
    def codec(self):
        """
        :returns: 
        :rtype: RecordingInstance.Codec
        """
        return self._properties['codec']
    
    @property
    def grouping_sids(self):
        """
        :returns: A list of SIDs related to the recording. Includes the `room_sid` and `participant_sid`.
        :rtype: dict
        """
        return self._properties['grouping_sids']
    
    @property
    def track_name(self):
        """
        :returns: The name that was given to the source track of the recording. If no name is given, the `source_sid` is used.
        :rtype: str
        """
        return self._properties['track_name']
    
    @property
    def offset(self):
        """
        :returns: The time in milliseconds elapsed between an arbitrary point in time, common to all group rooms, and the moment when the source room of this track started. This information provides a synchronization mechanism for recordings belonging to the same room.
        :rtype: int
        """
        return self._properties['offset']
    
    @property
    def media_external_location(self):
        """
        :returns: The URL of the media file associated with the recording when stored externally. See [External S3 Recordings](/docs/video/api/external-s3-recordings) for more details.
        :rtype: str
        """
        return self._properties['media_external_location']
    
    @property
    def status_callback(self):
        """
        :returns: The URL called using the `status_callback_method` to send status information on every recording event.
        :rtype: str
        """
        return self._properties['status_callback']
    
    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method used to call `status_callback`. Can be: `POST` or `GET`, defaults to `POST`.
        :rtype: str
        """
        return self._properties['status_callback_method']
    
    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the RecordingInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the RecordingInstance
        

        :returns: The fetched RecordingInstance
        :rtype: twilio.rest.video.v1.recording.RecordingInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RecordingInstance {}>'.format(context)

class RecordingContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the RecordingContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Recording resource to fetch.

        :returns: twilio.rest.video.v1.recording.RecordingContext
        :rtype: twilio.rest.video.v1.recording.RecordingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Recordings/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the RecordingInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the RecordingInstance
        

        :returns: The fetched RecordingInstance
        :rtype: twilio.rest.video.v1.recording.RecordingInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RecordingInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.RecordingContext {}>'.format(context)


