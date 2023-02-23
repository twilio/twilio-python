"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SampleList(ListResource):

    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the SampleList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resources to read.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resources to read.
        
        :returns: twilio.rest.autopilot.v1.assistant.task.sample.SampleList
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid,  }
        self._uri = '/Assistants/${assistant_sid}/Tasks/${task_sid}/Samples'.format(**self._solution)
        
        
    
    
    
    
    def create(self, language, tagged_text, source_channel=values.unset):
        """
        Create the SampleInstance
        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the new sample. For example: `en-US`.
        :param str tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :param str source_channel: The communication channel from which the new sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.
        
        :returns: The created SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        """
        data = values.of({ 
            'Language': language,
            'TaggedText': tagged_text,
            'SourceChannel': source_channel,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return SampleInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'])
    
    
    def stream(self, language=values.unset, limit=None, page_size=None):
        """
        Streams SampleInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            language=language,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, language=values.unset, limit=None, page_size=None):
        """
        Lists SampleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance]
        """
        return list(self.stream(
            language=language,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, language=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SampleInstance records from the API.
        Request is executed immediately
        
        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SamplePage
        """
        data = values.of({ 
            'Language': language,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SamplePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SampleInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SamplePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SamplePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SampleContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Sample resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.task.sample.SampleContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleContext
        """
        return SampleContext(self._version, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a SampleContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Sample resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.task.sample.SampleContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleContext
        """
        return SampleContext(self._version, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.SampleList>'










class SamplePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SamplePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.autopilot.v1.assistant.task.sample.SamplePage
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SamplePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SampleInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        """
        return SampleInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.SamplePage>'




class SampleContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str, task_sid: str, sid: str):
        """
        Initialize the SampleContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource to update.:param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the Sample resource to update.:param sid: The Twilio-provided string that uniquely identifies the Sample resource to update.

        :returns: twilio.rest.autopilot.v1.assistant.task.sample.SampleContext
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
            'task_sid': task_sid,
            'sid': sid,
        }
        self._uri = '/Assistants/${assistant_sid}/Tasks/${task_sid}/Samples/${sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the SampleInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri)
        
    def fetch(self):
        """
        Fetch the SampleInstance

        :returns: The fetched SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            task_sid=self._solution['task_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, language=values.unset, tagged_text=values.unset, source_channel=values.unset):
        """
        Update the SampleInstance
        
        :params str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :params str tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :params str source_channel: The communication channel from which the sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.

        :returns: The updated SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        """
        data = values.of({ 
            'Language': language,
            'TaggedText': tagged_text,
            'SourceChannel': source_channel,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data)

        return SampleInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            task_sid=self._solution['task_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.SampleContext {}>'.format(context)

class SampleInstance(InstanceResource):

    def __init__(self, version, payload, assistant_sid: str, task_sid: str, sid: str=None):
        """
        Initialize the SampleInstance
        :returns: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'task_sid': payload.get('task_sid'),
            'language': payload.get('language'),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'tagged_text': payload.get('tagged_text'),
            'url': payload.get('url'),
            'source_channel': payload.get('source_channel'),
        }

        self._context = None
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SampleContext for this SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleContext
        """
        if self._context is None:
            self._context = SampleContext(self._version, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sample resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def task_sid(self):
        """
        :returns: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) associated with the resource.
        :rtype: str
        """
        return self._properties['task_sid']
    
    @property
    def language(self):
        """
        :returns: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :rtype: str
        """
        return self._properties['language']
    
    @property
    def assistant_sid(self):
        """
        :returns: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task associated with the resource.
        :rtype: str
        """
        return self._properties['assistant_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Sample resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def tagged_text(self):
        """
        :returns: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :rtype: str
        """
        return self._properties['tagged_text']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Sample resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def source_channel(self):
        """
        :returns: The communication channel from which the sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.
        :rtype: str
        """
        return self._properties['source_channel']
    
    def delete(self):
        """
        Deletes the SampleInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the SampleInstance

        :returns: The fetched SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        """
        return self._proxy.fetch()
    
    def update(self, language=values.unset, tagged_text=values.unset, source_channel=values.unset):
        """
        Update the SampleInstance
        
        :params str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) string that specifies the language used for the sample. For example: `en-US`.
        :params str tagged_text: The text example of how end users might express the task. The sample can contain [Field tag blocks](https://www.twilio.com/docs/autopilot/api/task-sample#field-tagging).
        :params str source_channel: The communication channel from which the sample was captured. Can be: `voice`, `sms`, `chat`, `alexa`, `google-assistant`, `slack`, or null if not included.

        :returns: The updated SampleInstance
        :rtype: twilio.rest.autopilot.v1.assistant.task.sample.SampleInstance
        """
        return self._proxy.update(language=language, tagged_text=tagged_text, source_channel=source_channel, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.SampleInstance {}>'.format(context)


