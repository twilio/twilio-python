"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
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


class SupportingDocumentTypeList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SupportingDocumentTypeList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeList
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/SupportingDocumentTypes'.format(**self._solution)
        
        
    
    def fetch(self):
        """
        Fetch the SupportingDocumentTypeInstance

        :returns: The fetched SupportingDocumentTypeInstance
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return SupportingDocumentTypeInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams SupportingDocumentTypeInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SupportingDocumentTypeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SupportingDocumentTypeInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SupportingDocumentTypeInstance
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SupportingDocumentTypePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SupportingDocumentTypeInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SupportingDocumentTypeInstance
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SupportingDocumentTypePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SupportingDocumentTypeContext
        
        :param sid: The unique string that identifies the Supporting Document Type resource.
        
        :returns: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeContext
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeContext
        """
        return SupportingDocumentTypeContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a SupportingDocumentTypeContext
        
        :param sid: The unique string that identifies the Supporting Document Type resource.
        
        :returns: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeContext
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeContext
        """
        return SupportingDocumentTypeContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.SupportingDocumentTypeList>'




class SupportingDocumentTypePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SupportingDocumentTypePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypePage
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SupportingDocumentTypeInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance
        """
        return SupportingDocumentTypeInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.SupportingDocumentTypePage>'




class SupportingDocumentTypeInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the SupportingDocumentTypeInstance
        :returns: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'machine_name': payload.get('machine_name'),
            'fields': payload.get('fields'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SupportingDocumentTypeContext for this SupportingDocumentTypeInstance
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeContext
        """
        if self._context is None:
            self._context = SupportingDocumentTypeContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Supporting Document Type resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def friendly_name(self):
        """
        :returns: A human-readable description of the Supporting Document Type resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def machine_name(self):
        """
        :returns: The machine-readable description of the Supporting Document Type resource.
        :rtype: str
        """
        return self._properties['machine_name']
    
    @property
    def fields(self):
        """
        :returns: The required information for creating a Supporting Document. The required fields will change as regulatory needs change and will differ for businesses and individuals.
        :rtype: list[object]
        """
        return self._properties['fields']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Supporting Document Type resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the SupportingDocumentTypeInstance
        

        :returns: The fetched SupportingDocumentTypeInstance
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.SupportingDocumentTypeInstance {}>'.format(context)

class SupportingDocumentTypeContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the SupportingDocumentTypeContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that identifies the Supporting Document Type resource.

        :returns: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeContext
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/SupportingDocumentTypes/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the SupportingDocumentTypeInstance
        

        :returns: The fetched SupportingDocumentTypeInstance
        :rtype: twilio.rest.trusthub.v1.supporting_document_type.SupportingDocumentTypeInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SupportingDocumentTypeInstance(
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
        return '<Twilio.Trusthub.V1.SupportingDocumentTypeContext {}>'.format(context)


