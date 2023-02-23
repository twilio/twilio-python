"""
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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class FieldValueList(ListResource):

    def __init__(self, version: Version, assistant_sid: str, field_type_sid: str):
        """
        Initialize the FieldValueList

        :param Version version: Version that contains the resource
        :param assistant_sid: 
        :param field_type_sid: 
        
        :returns: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueList
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'field_type_sid': field_type_sid,  }
        self._uri = '/Assistants/${assistant_sid}/FieldTypes/${field_type_sid}/FieldValues'.format(**self._solution)
        
        
    
    
    
    def create(self, language, value, synonym_of=values.unset):
        """
        Create the FieldValueInstance
        :param str language: An ISO language-country string of the value.
        :param str value: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param str synonym_of: A value that indicates this field value is a synonym of. Empty if the value is not a synonym.
        
        :returns: The created FieldValueInstance
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance
        """
        data = values.of({ 
            'Language': language,
            'Value': value,
            'SynonymOf': synonym_of,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return FieldValueInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], field_type_sid=self._solution['field_type_sid'])
    
    
    def stream(self, language=values.unset, limit=None, page_size=None):
        """
        Streams FieldValueInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str language: An ISO language-country string of the value. For example: *en-US*
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            language=language,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, language=values.unset, limit=None, page_size=None):
        """
        Lists FieldValueInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str language: An ISO language-country string of the value. For example: *en-US*
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance]
        """
        return list(self.stream(
            language=language,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, language=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FieldValueInstance records from the API.
        Request is executed immediately
        
        :param str language: An ISO language-country string of the value. For example: *en-US*
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FieldValueInstance
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValuePage
        """
        data = values.of({ 
            'Language': language,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return FieldValuePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FieldValueInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FieldValueInstance
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValuePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return FieldValuePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a FieldValueContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueContext
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueContext
        """
        return FieldValueContext(self._version, assistant_sid=self._solution['assistant_sid'], field_type_sid=self._solution['field_type_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a FieldValueContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueContext
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueContext
        """
        return FieldValueContext(self._version, assistant_sid=self._solution['assistant_sid'], field_type_sid=self._solution['field_type_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.FieldValueList>'








class FieldValuePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FieldValuePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValuePage
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValuePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FieldValueInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance
        """
        return FieldValueInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], field_type_sid=self._solution['field_type_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.FieldValuePage>'




class FieldValueContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str, field_type_sid: str, sid: str):
        """
        Initialize the FieldValueContext

        :param Version version: Version that contains the resource
        :param assistant_sid: :param field_type_sid: :param sid: 

        :returns: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueContext
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
            'field_type_sid': field_type_sid,
            'sid': sid,
        }
        self._uri = '/Assistants/${assistant_sid}/FieldTypes/${field_type_sid}/FieldValues/${sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the FieldValueInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri)
        
    def fetch(self):
        """
        Fetch the FieldValueInstance

        :returns: The fetched FieldValueInstance
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return FieldValueInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            field_type_sid=self._solution['field_type_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.FieldValueContext {}>'.format(context)

class FieldValueInstance(InstanceResource):

    def __init__(self, version, payload, assistant_sid: str, field_type_sid: str, sid: str=None):
        """
        Initialize the FieldValueInstance
        :returns: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'field_type_sid': payload.get('field_type_sid'),
            'language': payload.get('language'),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'value': payload.get('value'),
            'url': payload.get('url'),
            'synonym_of': payload.get('synonym_of'),
        }

        self._context = None
        self._solution = { 'assistant_sid': assistant_sid, 'field_type_sid': field_type_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FieldValueContext for this FieldValueInstance
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueContext
        """
        if self._context is None:
            self._context = FieldValueContext(self._version, assistant_sid=self._solution['assistant_sid'], field_type_sid=self._solution['field_type_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Field Value.
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
    def field_type_sid(self):
        """
        :returns: The unique ID of the Field Type associated with this Field Value.
        :rtype: str
        """
        return self._properties['field_type_sid']
    
    @property
    def language(self):
        """
        :returns: An ISO language-country string of the value.
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
    def value(self):
        """
        :returns: The Field Value itself.
        :rtype: str
        """
        return self._properties['value']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def synonym_of(self):
        """
        :returns: A value that indicates this field value is a synonym of. Empty if the value is not a synonym.
        :rtype: str
        """
        return self._properties['synonym_of']
    
    def delete(self):
        """
        Deletes the FieldValueInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the FieldValueInstance

        :returns: The fetched FieldValueInstance
        :rtype: twilio.rest.preview.understand.assistant.field_type.field_value.FieldValueInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.FieldValueInstance {}>'.format(context)


