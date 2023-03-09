r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
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


class SampleList(ListResource):

    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the SampleList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant.
        :param task_sid: The unique ID of the Task associated with this Sample.
        
        :returns: twilio.rest.preview.understand.assistant.task.sample.SampleList
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid,  }
        self._uri = '/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples'.format(**self._solution)
        
        
    
    
    
    
    def create(self, language, tagged_text, source_channel=values.unset):
        """
        Create the SampleInstance

        :param str language: An ISO language-country string of the sample.
        :param str tagged_text: The text example of how end-users may express this task. The sample may contain Field tag blocks.
        :param str source_channel: The communication channel the sample was captured. It can be: *voice*, *sms*, *chat*, *alexa*, *google-assistant*, or *slack*. If not included the value will be null
        
        :returns: The created SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        data = values.of({ 
            'Language': language,
            'TaggedText': tagged_text,
            'SourceChannel': source_channel,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SampleInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'])

    async def create_async(self, language, tagged_text, source_channel=values.unset):
        """
        Asynchronous coroutine to create the SampleInstance

        :param str language: An ISO language-country string of the sample.
        :param str tagged_text: The text example of how end-users may express this task. The sample may contain Field tag blocks.
        :param str source_channel: The communication channel the sample was captured. It can be: *voice*, *sms*, *chat*, *alexa*, *google-assistant*, or *slack*. If not included the value will be null
        
        :returns: The created SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        data = values.of({ 
            'Language': language,
            'TaggedText': tagged_text,
            'SourceChannel': source_channel,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return SampleInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'])
    
    
    def stream(self, language=values.unset, limit=None, page_size=None):
        """
        Streams SampleInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str language: An ISO language-country string of the sample.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.sample.SampleInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            language=language,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, language=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams SampleInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str language: An ISO language-country string of the sample.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.sample.SampleInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            language=language,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, language=values.unset, limit=None, page_size=None):
        """
        Lists SampleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str language: An ISO language-country string of the sample.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.sample.SampleInstance]
        """
        return list(self.stream(
            language=language,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, language=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists SampleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str language: An ISO language-country string of the sample.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.sample.SampleInstance]
        """
        return list(await self.stream_async(
            language=language,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, language=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SampleInstance records from the API.
        Request is executed immediately
        
        :param str language: An ISO language-country string of the sample.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SamplePage
        """
        data = values.of({ 
            'Language': language,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SamplePage(self._version, response, self._solution)

    async def page_async(self, language=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of SampleInstance records from the API.
        Request is executed immediately
        
        :param str language: An ISO language-country string of the sample.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SamplePage
        """
        data = values.of({ 
            'Language': language,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return SamplePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SampleInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SamplePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SamplePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of SampleInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SamplePage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return SamplePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SampleContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.preview.understand.assistant.task.sample.SampleContext
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleContext
        """
        return SampleContext(self._version, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a SampleContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.preview.understand.assistant.task.sample.SampleContext
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleContext
        """
        return SampleContext(self._version, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.SampleList>'










class SamplePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SamplePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.understand.assistant.task.sample.SamplePage
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SamplePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SampleInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        return SampleInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.SamplePage>'




class SampleInstance(InstanceResource):

    def __init__(self, version, payload, assistant_sid: str, task_sid: str, sid: str=None):
        """
        Initialize the SampleInstance
        :returns: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
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
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleContext
        """
        if self._context is None:
            self._context = SampleContext(self._version, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Sample.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def task_sid(self):
        """
        :returns: The unique ID of the Task associated with this Sample.
        :rtype: str
        """
        return self._properties['task_sid']
    
    @property
    def language(self):
        """
        :returns: An ISO language-country string of the sample.
        :rtype: str
        """
        return self._properties['language']
    
    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the Assistant.
        :rtype: str
        """
        return self._properties['assistant_sid']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def tagged_text(self):
        """
        :returns: The text example of how end-users may express this task. The sample may contain Field tag blocks.
        :rtype: str
        """
        return self._properties['tagged_text']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def source_channel(self):
        """
        :returns: The communication channel the sample was captured. It can be: *voice*, *sms*, *chat*, *alexa*, *google-assistant*, or *slack*. If not included the value will be null
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
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the SampleInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the SampleInstance
        

        :returns: The fetched SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SampleInstance
        

        :returns: The fetched SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, language=values.unset, tagged_text=values.unset, source_channel=values.unset):
        """
        Update the SampleInstance
        
        :params str language: An ISO language-country string of the sample.
        :params str tagged_text: The text example of how end-users may express this task. The sample may contain Field tag blocks.
        :params str source_channel: The communication channel the sample was captured. It can be: *voice*, *sms*, *chat*, *alexa*, *google-assistant*, or *slack*. If not included the value will be null

        :returns: The updated SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        return self._proxy.update(language=language, tagged_text=tagged_text, source_channel=source_channel, )

    async def update_async(self, language=values.unset, tagged_text=values.unset, source_channel=values.unset):
        """
        Asynchronous coroutine to update the SampleInstance
        
        :params str language: An ISO language-country string of the sample.
        :params str tagged_text: The text example of how end-users may express this task. The sample may contain Field tag blocks.
        :params str source_channel: The communication channel the sample was captured. It can be: *voice*, *sms*, *chat*, *alexa*, *google-assistant*, or *slack*. If not included the value will be null

        :returns: The updated SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        return await self._proxy.update_async(language=language, tagged_text=tagged_text, source_channel=source_channel, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.SampleInstance {}>'.format(context)

class SampleContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str, task_sid: str, sid: str):
        """
        Initialize the SampleContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant.
        :param task_sid: The unique ID of the Task associated with this Sample.
        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.preview.understand.assistant.task.sample.SampleContext
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
            'task_sid': task_sid,
            'sid': sid,
        }
        self._uri = '/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the SampleInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SampleInstance
        

        :returns: The fetched SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

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
        
        :params str language: An ISO language-country string of the sample.
        :params str tagged_text: The text example of how end-users may express this task. The sample may contain Field tag blocks.
        :params str source_channel: The communication channel the sample was captured. It can be: *voice*, *sms*, *chat*, *alexa*, *google-assistant*, or *slack*. If not included the value will be null

        :returns: The updated SampleInstance
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleInstance
        """
        data = values.of({ 
            'Language': language,
            'TaggedText': tagged_text,
            'SourceChannel': source_channel,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

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
        return '<Twilio.Preview.Understand.SampleContext {}>'.format(context)


