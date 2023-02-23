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
from twilio.rest.preview.sync.service.document import DocumentList
from twilio.rest.preview.sync.service.sync_list import SyncListList
from twilio.rest.preview.sync.service.sync_map import SyncMapList


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.preview.sync.service.ServiceList
        :rtype: twilio.rest.preview.sync.service.ServiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name=values.unset, webhook_url=values.unset, reachability_webhooks_enabled=values.unset, acl_enabled=values.unset):
        """
        Create the ServiceInstance

        :param str friendly_name: 
        :param str webhook_url: 
        :param bool reachability_webhooks_enabled: 
        :param bool acl_enabled: 
        
        :returns: The created ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServiceInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'WebhookUrl': webhook_url,
            'ReachabilityWebhooksEnabled': reachability_webhooks_enabled,
            'AclEnabled': acl_enabled,
        })
        )
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.sync.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.ServiceInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServicePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ServicePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.sync.service.ServiceContext
        :rtype: twilio.rest.preview.sync.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.sync.service.ServiceContext
        :rtype: twilio.rest.preview.sync.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.ServiceList>'










class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.sync.service.ServicePage
        :rtype: twilio.rest.preview.sync.service.ServicePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.sync.service.ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.ServicePage>'




class ServiceContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: 

        :returns: twilio.rest.preview.sync.service.ServiceContext
        :rtype: twilio.rest.preview.sync.service.ServiceContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Services/{sid}'.format(**self._solution)
        
        self._documents = None
        self._sync_lists = None
        self._sync_maps = None
    
    def delete(self):
        """
        Deletes the ServiceInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServiceInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, webhook_url=values.unset, friendly_name=values.unset, reachability_webhooks_enabled=values.unset, acl_enabled=values.unset):
        """
        Update the ServiceInstance
        
        :params str webhook_url: 
        :params str friendly_name: 
        :params bool reachability_webhooks_enabled: 
        :params bool acl_enabled: 

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServiceInstance
        """
        data = values.of({ 
            'WebhookUrl': webhook_url,
            'FriendlyName': friendly_name,
            'ReachabilityWebhooksEnabled': reachability_webhooks_enabled,
            'AclEnabled': acl_enabled,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def documents(self):
        """
        Access the documents

        :returns: twilio.rest.preview.sync.service.DocumentList
        :rtype: twilio.rest.preview.sync.service.DocumentList
        """
        if self._documents is None:
            self._documents = DocumentList(self._version, self._solution['sid'],
            )
        return self._documents
    
    @property
    def sync_lists(self):
        """
        Access the sync_lists

        :returns: twilio.rest.preview.sync.service.SyncListList
        :rtype: twilio.rest.preview.sync.service.SyncListList
        """
        if self._sync_lists is None:
            self._sync_lists = SyncListList(self._version, self._solution['sid'],
            )
        return self._sync_lists
    
    @property
    def sync_maps(self):
        """
        Access the sync_maps

        :returns: twilio.rest.preview.sync.service.SyncMapList
        :rtype: twilio.rest.preview.sync.service.SyncMapList
        """
        if self._sync_maps is None:
            self._sync_maps = SyncMapList(self._version, self._solution['sid'],
            )
        return self._sync_maps
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.ServiceContext {}>'.format(context)

class ServiceInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the ServiceInstance
        :returns: twilio.rest.preview.sync.service.ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServiceInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'webhook_url': payload.get('webhook_url'),
            'reachability_webhooks_enabled': payload.get('reachability_webhooks_enabled'),
            'acl_enabled': payload.get('acl_enabled'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['friendly_name']
    
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
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def webhook_url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['webhook_url']
    
    @property
    def reachability_webhooks_enabled(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['reachability_webhooks_enabled']
    
    @property
    def acl_enabled(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['acl_enabled']
    
    @property
    def links(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the ServiceInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServiceInstance
        """
        return self._proxy.fetch()
    
    def update(self, webhook_url=values.unset, friendly_name=values.unset, reachability_webhooks_enabled=values.unset, acl_enabled=values.unset):
        """
        Update the ServiceInstance
        
        :params str webhook_url: 
        :params str friendly_name: 
        :params bool reachability_webhooks_enabled: 
        :params bool acl_enabled: 

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.preview.sync.service.ServiceInstance
        """
        return self._proxy.update(webhook_url=webhook_url, friendly_name=friendly_name, reachability_webhooks_enabled=reachability_webhooks_enabled, acl_enabled=acl_enabled, )
    
    @property
    def documents(self):
        """
        Access the documents

        :returns: twilio.rest.preview.sync.service.DocumentList
        :rtype: twilio.rest.preview.sync.service.DocumentList
        """
        return self._proxy.documents
    
    @property
    def sync_lists(self):
        """
        Access the sync_lists

        :returns: twilio.rest.preview.sync.service.SyncListList
        :rtype: twilio.rest.preview.sync.service.SyncListList
        """
        return self._proxy.sync_lists
    
    @property
    def sync_maps(self):
        """
        Access the sync_maps

        :returns: twilio.rest.preview.sync.service.SyncMapList
        :rtype: twilio.rest.preview.sync.service.SyncMapList
        """
        return self._proxy.sync_maps
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.ServiceInstance {}>'.format(context)


