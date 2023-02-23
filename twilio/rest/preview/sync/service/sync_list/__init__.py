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
from twilio.rest.preview.sync.service.sync_list.sync_list_item import SyncListItemList
from twilio.rest.preview.sync.service.sync_list.sync_list_permission import SyncListPermissionList


class SyncListList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the SyncListList

        :param Version version: Version that contains the resource
        :param service_sid: 
        
        :returns: twilio.rest.preview.sync.service.sync_list.SyncListList
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Lists'.format(**self._solution)
        
        
    
    
    
    def create(self, unique_name=values.unset):
        """
        Create the SyncListInstance

        :param str unique_name: 
        
        :returns: The created SyncListInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
        })
        )
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SyncListInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams SyncListInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.sync.service.sync_list.SyncListInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncListInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_list.SyncListInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SyncListInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncListInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SyncListPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncListInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SyncListPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SyncListContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.sync.service.sync_list.SyncListContext
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListContext
        """
        return SyncListContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a SyncListContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.sync.service.sync_list.SyncListContext
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListContext
        """
        return SyncListContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncListList>'








class SyncListPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SyncListPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.sync.service.sync_list.SyncListPage
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncListInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.sync.service.sync_list.SyncListInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListInstance
        """
        return SyncListInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncListPage>'




class SyncListContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the SyncListContext

        :param Version version: Version that contains the resource
        :param service_sid: :param sid: 

        :returns: twilio.rest.preview.sync.service.sync_list.SyncListContext
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Lists/{sid}'.format(**self._solution)
        
        self._sync_list_items = None
        self._sync_list_permissions = None
    
    def delete(self):
        """
        Deletes the SyncListInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SyncListInstance
        

        :returns: The fetched SyncListInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SyncListInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    @property
    def sync_list_items(self):
        """
        Access the sync_list_items

        :returns: twilio.rest.preview.sync.service.sync_list.SyncListItemList
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListItemList
        """
        if self._sync_list_items is None:
            self._sync_list_items = SyncListItemList(self._version, self._solution['service_sid'], self._solution['sid'],
            )
        return self._sync_list_items
    
    @property
    def sync_list_permissions(self):
        """
        Access the sync_list_permissions

        :returns: twilio.rest.preview.sync.service.sync_list.SyncListPermissionList
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListPermissionList
        """
        if self._sync_list_permissions is None:
            self._sync_list_permissions = SyncListPermissionList(self._version, self._solution['service_sid'], self._solution['sid'],
            )
        return self._sync_list_permissions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncListContext {}>'.format(context)

class SyncListInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the SyncListInstance
        :returns: twilio.rest.preview.sync.service.sync_list.SyncListInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListInstance
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

        :returns: SyncListContext for this SyncListInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListContext
        """
        if self._context is None:
            self._context = SyncListContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
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
        Deletes the SyncListInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the SyncListInstance
        

        :returns: The fetched SyncListInstance
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListInstance
        """
        return self._proxy.fetch()
    
    @property
    def sync_list_items(self):
        """
        Access the sync_list_items

        :returns: twilio.rest.preview.sync.service.sync_list.SyncListItemList
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListItemList
        """
        return self._proxy.sync_list_items
    
    @property
    def sync_list_permissions(self):
        """
        Access the sync_list_permissions

        :returns: twilio.rest.preview.sync.service.sync_list.SyncListPermissionList
        :rtype: twilio.rest.preview.sync.service.sync_list.SyncListPermissionList
        """
        return self._proxy.sync_list_permissions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncListInstance {}>'.format(context)


