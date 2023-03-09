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
from twilio.rest.preview.marketplace.available_add_on.available_add_on_extension import AvailableAddOnExtensionList


class AvailableAddOnList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AvailableAddOnList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnList
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/AvailableAddOns'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AvailableAddOnInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams AvailableAddOnInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return await self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AvailableAddOnInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists AvailableAddOnInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AvailableAddOnInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AvailableAddOnPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronously retrieve a single page of AvailableAddOnInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return AvailableAddOnPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AvailableAddOnPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return AvailableAddOnPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AvailableAddOnContext
        
        :param sid: The SID of the AvailableAddOn resource to fetch.
        
        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnContext
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnContext
        """
        return AvailableAddOnContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a AvailableAddOnContext
        
        :param sid: The SID of the AvailableAddOn resource to fetch.
        
        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnContext
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnContext
        """
        return AvailableAddOnContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.AvailableAddOnList>'




class AvailableAddOnPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AvailableAddOnPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnPage
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AvailableAddOnInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance
        """
        return AvailableAddOnInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.AvailableAddOnPage>'




class AvailableAddOnInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the AvailableAddOnInstance
        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'description': payload.get('description'),
            'pricing_type': payload.get('pricing_type'),
            'configuration_schema': payload.get('configuration_schema'),
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

        :returns: AvailableAddOnContext for this AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnContext
        """
        if self._context is None:
            self._context = AvailableAddOnContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the AvailableAddOn resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def description(self):
        """
        :returns: A short description of the Add-on's functionality.
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def pricing_type(self):
        """
        :returns: How customers are charged for using this Add-on.
        :rtype: str
        """
        return self._properties['pricing_type']
    
    @property
    def configuration_schema(self):
        """
        :returns: The JSON object with the configuration that must be provided when installing a given Add-on.
        :rtype: dict
        """
        return self._properties['configuration_schema']
    
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
        Fetch the AvailableAddOnInstance
        

        :returns: The fetched AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AvailableAddOnInstance
        

        :returns: The fetched AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance
        """
        return await self._proxy.fetch_async()
    
    @property
    def extensions(self):
        """
        Access the extensions

        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnExtensionList
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnExtensionList
        """
        return self._proxy.extensions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.AvailableAddOnInstance {}>'.format(context)

class AvailableAddOnContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the AvailableAddOnContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the AvailableAddOn resource to fetch.

        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnContext
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/AvailableAddOns/{sid}'.format(**self._solution)
        
        self._extensions = None
    
    
    def fetch(self):
        """
        Fetch the AvailableAddOnInstance
        

        :returns: The fetched AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AvailableAddOnInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AvailableAddOnInstance
        

        :returns: The fetched AvailableAddOnInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return AvailableAddOnInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    @property
    def extensions(self):
        """
        Access the extensions

        :returns: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnExtensionList
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnExtensionList
        """
        if self._extensions is None:
            self._extensions = AvailableAddOnExtensionList(
                self._version, 
                self._solution['sid'],
            )
        return self._extensions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.AvailableAddOnContext {}>'.format(context)


