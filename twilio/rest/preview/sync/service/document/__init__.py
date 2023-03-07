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
from twilio.rest.preview.sync.service.document.document_permission import DocumentPermissionList


class DocumentList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the DocumentList

        :param Version version: Version that contains the resource
        :param service_sid: 
        
        :returns: twilio.rest.preview.sync.service.document.DocumentList
        :rtype: twilio.rest.preview.sync.service.document.DocumentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Documents'.format(**self._solution)
        
        
    
    
    
    
    def create(self, unique_name=values.unset, data=values.unset):
        """
        Create the DocumentInstance

        :param str unique_name: 
        :param object data: 
        
        :returns: The created DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'Data': serialize.object(data),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return DocumentInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams DocumentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.sync.service.document.DocumentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.document.DocumentInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DocumentInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return DocumentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DocumentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return DocumentPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a DocumentContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.sync.service.document.DocumentContext
        :rtype: twilio.rest.preview.sync.service.document.DocumentContext
        """
        return DocumentContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a DocumentContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.sync.service.document.DocumentContext
        :rtype: twilio.rest.preview.sync.service.document.DocumentContext
        """
        return DocumentContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.DocumentList>'










class DocumentPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DocumentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.sync.service.document.DocumentPage
        :rtype: twilio.rest.preview.sync.service.document.DocumentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DocumentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.sync.service.document.DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentInstance
        """
        return DocumentInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.DocumentPage>'




class DocumentInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the DocumentInstance
        :returns: twilio.rest.preview.sync.service.document.DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
            'revision': payload.get('revision'),
            'data': payload.get('data'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'created_by': payload.get('created_by'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DocumentContext for this DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentContext
        """
        if self._context is None:
            self._context = DocumentContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def unique_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    @property
    def revision(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['revision']
    
    @property
    def data(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['data']
    
    @property
    def date_created(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def created_by(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['created_by']
    
    def delete(self):
        """
        Deletes the DocumentInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the DocumentInstance
        

        :returns: The fetched DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentInstance
        """
        return self._proxy.fetch()
    
    def update(self, data, if_match=values.unset):
        """
        Update the DocumentInstance
        
        :params object data: 
        :params str if_match: The If-Match HTTP request header

        :returns: The updated DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentInstance
        """
        return self._proxy.update(data=data, if_match=if_match, )
    
    @property
    def document_permissions(self):
        """
        Access the document_permissions

        :returns: twilio.rest.preview.sync.service.document.DocumentPermissionList
        :rtype: twilio.rest.preview.sync.service.document.DocumentPermissionList
        """
        return self._proxy.document_permissions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.DocumentInstance {}>'.format(context)

class DocumentContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the DocumentContext

        :param Version version: Version that contains the resource
        :param service_sid: 
        :param sid: 

        :returns: twilio.rest.preview.sync.service.document.DocumentContext
        :rtype: twilio.rest.preview.sync.service.document.DocumentContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Documents/{sid}'.format(**self._solution)
        
        self._document_permissions = None
    
    def delete(self):
        """
        Deletes the DocumentInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the DocumentInstance
        

        :returns: The fetched DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DocumentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, data, if_match=values.unset):
        """
        Update the DocumentInstance
        
        :params object data: 
        :params str if_match: The If-Match HTTP request header

        :returns: The updated DocumentInstance
        :rtype: twilio.rest.preview.sync.service.document.DocumentInstance
        """
        data = values.of({ 
            'Data': serialize.object(data),
        })
        headers = values.of({'If-Match': if_match, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return DocumentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def document_permissions(self):
        """
        Access the document_permissions

        :returns: twilio.rest.preview.sync.service.document.DocumentPermissionList
        :rtype: twilio.rest.preview.sync.service.document.DocumentPermissionList
        """
        if self._document_permissions is None:
            self._document_permissions = DocumentPermissionList(
                self._version, 
                self._solution['service_sid'],
                self._solution['sid'],
            )
        return self._document_permissions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.DocumentContext {}>'.format(context)


