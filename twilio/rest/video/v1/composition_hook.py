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


class CompositionHookList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CompositionHookList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.video.v1.composition_hook.CompositionHookList
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/CompositionHooks'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the CompositionHookInstance

        :returns: The fetched CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return CompositionHookInstance(self._version, payload)
    
    
    def update(self, friendly_name, enabled=values.unset, video_layout=values.unset, audio_sources=values.unset, audio_sources_excluded=values.unset, trim=values.unset, format=values.unset, resolution=values.unset, status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the CompositionHookInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to  100 characters long and it must be unique within the account.
        :param bool enabled: Whether the composition hook is active. When `true`, the composition hook will be triggered for every completed Group Room in the account. When `false`, the composition hook never triggers.
        :param object video_layout: A JSON object that describes the video layout of the composition hook in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param list[str] audio_sources: An array of track names from the same group room to merge into the compositions created by the composition hook. Can include zero or more track names. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` includes tracks named `student` as well as `studentTeam`.
        :param list[str] audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :param bool trim: Whether to clip the intervals where there is no active media in the compositions triggered by the composition hook. The default is `true`. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param Format format: 
        :param str resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to `640x480`.  The string's format is `{width}x{height}` where:   * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 * `{width}` * `{height}` <= 921,600  Typical values are:   * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF = `320x240`  Note that the `resolution` imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
        
        :returns: The created CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Enabled': enabled,
            'VideoLayout': serialize.object(video_layout),
            'AudioSources': serialize.map(audio_sources, lambda e: e),
            'AudioSourcesExcluded': serialize.map(audio_sources_excluded, lambda e: e),
            'Trim': trim,
            'Format': format,
            'Resolution': resolution,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })
        
        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return CompositionHookInstance(self._version, payload)
    
    
    def create(self, friendly_name, enabled=values.unset, video_layout=values.unset, audio_sources=values.unset, audio_sources_excluded=values.unset, resolution=values.unset, format=values.unset, status_callback=values.unset, status_callback_method=values.unset, trim=values.unset):
        """
        Create the CompositionHookInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to  100 characters long and it must be unique within the account.
        :param bool enabled: Whether the composition hook is active. When `true`, the composition hook will be triggered for every completed Group Room in the account. When `false`, the composition hook will never be triggered.
        :param object video_layout: An object that describes the video layout of the composition hook in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param list[str] audio_sources: An array of track names from the same group room to merge into the compositions created by the composition hook. Can include zero or more track names. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` includes tracks named `student` as well as `studentTeam`.
        :param list[str] audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :param str resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to `640x480`.  The string's format is `{width}x{height}` where:   * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 * `{width}` * `{height}` <= 921,600  Typical values are:   * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF = `320x240`  Note that the `resolution` imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :param Format format: 
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
        :param bool trim: Whether to clip the intervals where there is no active media in the Compositions triggered by the composition hook. The default is `true`. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        
        :returns: The created CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Enabled': enabled,
            'VideoLayout': serialize.object(video_layout),
            'AudioSources': serialize.map(audio_sources, lambda e: e),
            'AudioSourcesExcluded': serialize.map(audio_sources_excluded, lambda e: e),
            'Resolution': resolution,
            'Format': format,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'Trim': trim,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return CompositionHookInstance(self._version, payload)
    
    
    def stream(self, enabled=values.unset, date_created_after=values.unset, date_created_before=values.unset, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams CompositionHookInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param bool enabled: Read only CompositionHook resources with an `enabled` value that matches this parameter.
        :param datetime date_created_after: Read only CompositionHook resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only CompositionHook resources created before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param str friendly_name: Read only CompositionHook resources with friendly names that match this string. The match is not case sensitive and can include asterisk `*` characters as wildcard match.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition_hook.CompositionHookInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            enabled=enabled,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, enabled=values.unset, date_created_after=values.unset, date_created_before=values.unset, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists CompositionHookInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param bool enabled: Read only CompositionHook resources with an `enabled` value that matches this parameter.
        :param datetime date_created_after: Read only CompositionHook resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only CompositionHook resources created before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param str friendly_name: Read only CompositionHook resources with friendly names that match this string. The match is not case sensitive and can include asterisk `*` characters as wildcard match.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition_hook.CompositionHookInstance]
        """
        return list(self.stream(
            enabled=enabled,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, enabled=values.unset, date_created_after=values.unset, date_created_before=values.unset, friendly_name=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CompositionHookInstance records from the API.
        Request is executed immediately
        
        :param bool enabled: Read only CompositionHook resources with an `enabled` value that matches this parameter.
        :param datetime date_created_after: Read only CompositionHook resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param datetime date_created_before: Read only CompositionHook resources created before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
        :param str friendly_name: Read only CompositionHook resources with friendly names that match this string. The match is not case sensitive and can include asterisk `*` characters as wildcard match.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookPage
        """
        data = values.of({ 
            'Enabled': enabled,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CompositionHookPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CompositionHookInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CompositionHookPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a CompositionHookContext
        
        :param sid: The SID of the CompositionHook resource to update.
        
        :returns: twilio.rest.video.v1.composition_hook.CompositionHookContext
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookContext
        """
        return CompositionHookContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a CompositionHookContext
        
        :param sid: The SID of the CompositionHook resource to update.
        
        :returns: twilio.rest.video.v1.composition_hook.CompositionHookContext
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookContext
        """
        return CompositionHookContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionHookList>'










class CompositionHookPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CompositionHookPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookPage
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CompositionHookInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        return CompositionHookInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionHookPage>'




class CompositionHookInstance(InstanceResource):

    class Format(object):
        MP4 = "mp4"
        WEBM = "webm"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the CompositionHookInstance
        :returns: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'enabled': payload.get('enabled'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'sid': payload.get('sid'),
            'audio_sources': payload.get('audio_sources'),
            'audio_sources_excluded': payload.get('audio_sources_excluded'),
            'video_layout': payload.get('video_layout'),
            'resolution': payload.get('resolution'),
            'trim': payload.get('trim'),
            'format': payload.get('format'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CompositionHookContext for this CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookContext
        """
        if self._context is None:
            self._context = CompositionHookContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CompositionHook resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource. Can be up to 100 characters long and must be unique within the account.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def enabled(self):
        """
        :returns: Whether the CompositionHook is active. When `true`, the CompositionHook is triggered for every completed Group Room on the account. When `false`, the CompositionHook is never triggered.
        :rtype: bool
        """
        return self._properties['enabled']
    
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
    def sid(self):
        """
        :returns: The unique string that we created to identify the CompositionHook resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def audio_sources(self):
        """
        :returns: The array of track names to include in the compositions created by the composition hook. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except those specified in `audio_sources_excluded`. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` includes tracks named `student` as well as `studentTeam`. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :rtype: list[str]
        """
        return self._properties['audio_sources']
    
    @property
    def audio_sources_excluded(self):
        """
        :returns: The array of track names to exclude from the compositions created by the composition hook. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this property can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :rtype: list[str]
        """
        return self._properties['audio_sources_excluded']
    
    @property
    def video_layout(self):
        """
        :returns: A JSON object that describes the video layout of the composition in terms of regions as specified in the HTTP POST request that created the CompositionHook resource. See [POST Parameters](https://www.twilio.com/docs/video/api/compositions-resource#http-post-parameters) for more information. Please, be aware that either video_layout or audio_sources have to be provided to get a valid creation request
        :rtype: dict
        """
        return self._properties['video_layout']
    
    @property
    def resolution(self):
        """
        :returns: The dimensions of the video image in pixels expressed as columns (width) and rows (height). The string's format is `{width}x{height}`, such as `640x480`.
        :rtype: str
        """
        return self._properties['resolution']
    
    @property
    def trim(self):
        """
        :returns: Whether intervals with no media are clipped, as specified in the POST request that created the CompositionHook resource. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :rtype: bool
        """
        return self._properties['trim']
    
    @property
    def format(self):
        """
        :returns: 
        :rtype: Format
        """
        return self._properties['format']
    
    @property
    def status_callback(self):
        """
        :returns: The URL we call using the `status_callback_method` to send status information to your application.
        :rtype: str
        """
        return self._properties['status_callback']
    
    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we should use to call `status_callback`. Can be `POST` or `GET` and defaults to `POST`.
        :rtype: str
        """
        return self._properties['status_callback_method']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the CompositionHookInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the CompositionHookInstance
        

        :returns: The fetched CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name, enabled=values.unset, video_layout=values.unset, audio_sources=values.unset, audio_sources_excluded=values.unset, trim=values.unset, format=values.unset, resolution=values.unset, status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the CompositionHookInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to  100 characters long and it must be unique within the account.
        :params bool enabled: Whether the composition hook is active. When `true`, the composition hook will be triggered for every completed Group Room in the account. When `false`, the composition hook never triggers.
        :params object video_layout: A JSON object that describes the video layout of the composition hook in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :params list[str] audio_sources: An array of track names from the same group room to merge into the compositions created by the composition hook. Can include zero or more track names. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` includes tracks named `student` as well as `studentTeam`.
        :params list[str] audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :params bool trim: Whether to clip the intervals where there is no active media in the compositions triggered by the composition hook. The default is `true`. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :params Format format: 
        :params str resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to `640x480`.  The string's format is `{width}x{height}` where:   * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 * `{width}` * `{height}` <= 921,600  Typical values are:   * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF = `320x240`  Note that the `resolution` imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :params str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
        :params str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.

        :returns: The updated CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        return self._proxy.update(friendly_name=friendly_name, enabled=enabled, video_layout=video_layout, audio_sources=audio_sources, audio_sources_excluded=audio_sources_excluded, trim=trim, format=format, resolution=resolution, status_callback=status_callback, status_callback_method=status_callback_method, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.CompositionHookInstance {}>'.format(context)

class CompositionHookContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CompositionHookContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the CompositionHook resource to update.

        :returns: twilio.rest.video.v1.composition_hook.CompositionHookContext
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/CompositionHooks/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the CompositionHookInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the CompositionHookInstance
        

        :returns: The fetched CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CompositionHookInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name, enabled=values.unset, video_layout=values.unset, audio_sources=values.unset, audio_sources_excluded=values.unset, trim=values.unset, format=values.unset, resolution=values.unset, status_callback=values.unset, status_callback_method=values.unset):
        """
        Update the CompositionHookInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to  100 characters long and it must be unique within the account.
        :params bool enabled: Whether the composition hook is active. When `true`, the composition hook will be triggered for every completed Group Room in the account. When `false`, the composition hook never triggers.
        :params object video_layout: A JSON object that describes the video layout of the composition hook in terms of regions. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :params list[str] audio_sources: An array of track names from the same group room to merge into the compositions created by the composition hook. Can include zero or more track names. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` includes tracks named `student` as well as `studentTeam`.
        :params list[str] audio_sources_excluded: An array of track names to exclude. A composition triggered by the composition hook includes all audio sources specified in `audio_sources` except for those specified in `audio_sources_excluded`. The track names in this parameter can include an asterisk as a wild card character, which matches zero or more characters in a track name. For example, `student*` excludes `student` as well as `studentTeam`. This parameter can also be empty.
        :params bool trim: Whether to clip the intervals where there is no active media in the compositions triggered by the composition hook. The default is `true`. Compositions with `trim` enabled are shorter when the Room is created and no Participant joins for a while as well as if all the Participants leave the room and join later, because those gaps will be removed. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :params Format format: 
        :params str resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels. Defaults to `640x480`.  The string's format is `{width}x{height}` where:   * 16 <= `{width}` <= 1280 * 16 <= `{height}` <= 1280 * `{width}` * `{height}` <= 921,600  Typical values are:   * HD = `1280x720` * PAL = `1024x576` * VGA = `640x480` * CIF = `320x240`  Note that the `resolution` imposes an aspect ratio to the resulting composition. When the original video tracks are constrained by the aspect ratio, they are scaled to fit. See [Specifying Video Layouts](https://www.twilio.com/docs/video/api/compositions-resource#specifying-video-layouts) for more info.
        :params str status_callback: The URL we should call using the `status_callback_method` to send status information to your application on every composition event. If not provided, status callback events will not be dispatched.
        :params str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.

        :returns: The updated CompositionHookInstance
        :rtype: twilio.rest.video.v1.composition_hook.CompositionHookInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Enabled': enabled,
            'VideoLayout': serialize.object(video_layout),
            'AudioSources': serialize.map(audio_sources, lambda e: e),
            'AudioSourcesExcluded': serialize.map(audio_sources_excluded, lambda e: e),
            'Trim': trim,
            'Format': format,
            'Resolution': resolution,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return CompositionHookInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.CompositionHookContext {}>'.format(context)


