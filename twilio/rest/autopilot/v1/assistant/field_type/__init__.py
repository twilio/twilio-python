r"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.autopilot.v1.assistant.field_type.field_value import FieldValueList


class FieldTypeList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the FieldTypeList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
        
        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeList
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        self._uri = '/Assistants/{assistant_sid}/FieldTypes'.format(**self._solution)
        
        
    
    
    
    
    def create(self, unique_name, friendly_name=values.unset):
        """
        Create the FieldTypeInstance

        :param str unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.
        :param str friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
        
        :returns: The created FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return FieldTypeInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])

    async def create_async(self, unique_name, friendly_name=values.unset):
        """
        Asynchronous coroutine to create the FieldTypeInstance

        :param str unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.
        :param str friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
        
        :returns: The created FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return FieldTypeInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams FieldTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams FieldTypeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FieldTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists FieldTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FieldTypeInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return FieldTypePage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of FieldTypeInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return FieldTypePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FieldTypeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return FieldTypePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of FieldTypeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return FieldTypePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a FieldTypeContext
        
        :param sid: The Twilio-provided string that uniquely identifies the FieldType resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        """
        return FieldTypeContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a FieldTypeContext
        
        :param sid: The Twilio-provided string that uniquely identifies the FieldType resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        """
        return FieldTypeContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.FieldTypeList>'










class FieldTypePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FieldTypePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FieldTypeInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        return FieldTypeInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.FieldTypePage>'




class FieldTypeInstance(InstanceResource):

    def __init__(self, version, payload, assistant_sid: str, sid: str=None):
        """
        Initialize the FieldTypeInstance
        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'links': payload.get('links'),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FieldTypeContext for this FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        """
        if self._context is None:
            self._context = FieldTypeContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the FieldType resource.
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
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource. It is not unique and can be up to 255 characters long.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def links(self):
        """
        :returns: A list of the URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    @property
    def assistant_sid(self):
        """
        :returns: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource.
        :rtype: str
        """
        return self._properties['assistant_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the FieldType resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the FieldType resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def delete(self):
        """
        Deletes the FieldTypeInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the FieldTypeInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the FieldTypeInstance
        

        :returns: The fetched FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FieldTypeInstance
        

        :returns: The fetched FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, friendly_name=values.unset, unique_name=values.unset):
        """
        Update the FieldTypeInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params str unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.

        :returns: The updated FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        return self._proxy.update(friendly_name=friendly_name, unique_name=unique_name, )

    async def update_async(self, friendly_name=values.unset, unique_name=values.unset):
        """
        Asynchronous coroutine to update the FieldTypeInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params str unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.

        :returns: The updated FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        return await self._proxy.update_async(friendly_name=friendly_name, unique_name=unique_name, )
    
    @property
    def field_values(self):
        """
        Access the field_values

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldValueList
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldValueList
        """
        return self._proxy.field_values
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.FieldTypeInstance {}>'.format(context)

class FieldTypeContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str, sid: str):
        """
        Initialize the FieldTypeContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the to update.
        :param sid: The Twilio-provided string that uniquely identifies the FieldType resource to update.

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
            'sid': sid,
        }
        self._uri = '/Assistants/{assistant_sid}/FieldTypes/{sid}'.format(**self._solution)
        
        self._field_values = None
    
    def delete(self):
        """
        Deletes the FieldTypeInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the FieldTypeInstance
        

        :returns: The fetched FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FieldTypeInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, unique_name=values.unset):
        """
        Update the FieldTypeInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :params str unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource. The first 64 characters must be unique.

        :returns: The updated FieldTypeInstance
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldTypeInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return FieldTypeInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def field_values(self):
        """
        Access the field_values

        :returns: twilio.rest.autopilot.v1.assistant.field_type.FieldValueList
        :rtype: twilio.rest.autopilot.v1.assistant.field_type.FieldValueList
        """
        if self._field_values is None:
            self._field_values = FieldValueList(
                self._version, 
                self._solution['assistant_sid'],
                self._solution['sid'],
            )
        return self._field_values
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.FieldTypeContext {}>'.format(context)


