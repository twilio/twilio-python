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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AvailableAddOnExtensionList(ListResource):

    def __init__(self, version: Version, available_add_on_sid: str):
        """
        Initialize the AvailableAddOnExtensionList

        :param Version version: Version that contains the resource
        :param available_add_on_sid: The SID of the AvailableAddOn resource with the extensions to read.
        
        :returns: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionList
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'available_add_on_sid': available_add_on_sid,  }
        self._uri = '/AvailableAddOns/{available_add_on_sid}/Extensions'.format(**self._solution)
        
        
    
    def fetch(self):
        """
        Fetch the AvailableAddOnExtensionInstance

        :returns: The fetched AvailableAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return AvailableAddOnExtensionInstance(self._version, payload, available_add_on_sid=self._solution['available_add_on_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AvailableAddOnExtensionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AvailableAddOnExtensionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AvailableAddOnExtensionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AvailableAddOnExtensionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AvailableAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AvailableAddOnExtensionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AvailableAddOnExtensionContext
        
        :param sid: The SID of the AvailableAddOn Extension resource to fetch.
        
        :returns: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionContext
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionContext
        """
        return AvailableAddOnExtensionContext(self._version, available_add_on_sid=self._solution['available_add_on_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a AvailableAddOnExtensionContext
        
        :param sid: The SID of the AvailableAddOn Extension resource to fetch.
        
        :returns: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionContext
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionContext
        """
        return AvailableAddOnExtensionContext(self._version, available_add_on_sid=self._solution['available_add_on_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.AvailableAddOnExtensionList>'




class AvailableAddOnExtensionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AvailableAddOnExtensionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionPage
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AvailableAddOnExtensionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance
        """
        return AvailableAddOnExtensionInstance(self._version, payload, available_add_on_sid=self._solution['available_add_on_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.AvailableAddOnExtensionPage>'




class AvailableAddOnExtensionInstance(InstanceResource):

    def __init__(self, version, payload, available_add_on_sid: str, sid: str=None):
        """
        Initialize the AvailableAddOnExtensionInstance
        :returns: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'available_add_on_sid': payload.get('available_add_on_sid'),
            'friendly_name': payload.get('friendly_name'),
            'product_name': payload.get('product_name'),
            'unique_name': payload.get('unique_name'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'available_add_on_sid': available_add_on_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AvailableAddOnExtensionContext for this AvailableAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionContext
        """
        if self._context is None:
            self._context = AvailableAddOnExtensionContext(self._version, available_add_on_sid=self._solution['available_add_on_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the AvailableAddOnExtension resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def available_add_on_sid(self):
        """
        :returns: The SID of the AvailableAddOn resource to which this extension applies.
        :rtype: str
        """
        return self._properties['available_add_on_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def product_name(self):
        """
        :returns: The name of the Product this Extension is used within.
        :rtype: str
        """
        return self._properties['product_name']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the AvailableAddOnExtensionInstance
        

        :returns: The fetched AvailableAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.AvailableAddOnExtensionInstance {}>'.format(context)

class AvailableAddOnExtensionContext(InstanceContext):

    def __init__(self, version: Version, available_add_on_sid: str, sid: str):
        """
        Initialize the AvailableAddOnExtensionContext

        :param Version version: Version that contains the resource
        :param available_add_on_sid: The SID of the AvailableAddOn resource with the extension to fetch.:param sid: The SID of the AvailableAddOn Extension resource to fetch.

        :returns: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionContext
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'available_add_on_sid': available_add_on_sid,
            'sid': sid,
        }
        self._uri = '/AvailableAddOns/{available_add_on_sid}/Extensions/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the AvailableAddOnExtensionInstance
        

        :returns: The fetched AvailableAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.available_add_on.available_add_on_extension.AvailableAddOnExtensionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AvailableAddOnExtensionInstance(
            self._version,
            payload,
            available_add_on_sid=self._solution['available_add_on_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.AvailableAddOnExtensionContext {}>'.format(context)


