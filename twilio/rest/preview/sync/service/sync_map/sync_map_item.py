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


class SyncMapItemList(ListResource):

    def __init__(self, version: Version, service_sid: str, map_sid: str):
        """
        Initialize the SyncMapItemList

        :param Version version: Version that contains the resource
        :param service_sid: 
        :param map_sid: 
        
        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemList
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'map_sid': map_sid,  }
        self._uri = '/Services/{service_sid}/Maps/{map_sid}/Items'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the SyncMapItemInstance

        :returns: The fetched SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return SyncMapItemInstance(self._version, payload, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'])
    
    
    def update(self, data, if_match=values.unset):
        """
        Update the SyncMapItemInstance

        :param object data: 
        :param str if_match: The If-Match HTTP request header
        
        :returns: The created SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        data = values.of({ 
            'Data': serialize.object(data),
        })
        headers = values.of({'If-Match': if_match, })
        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return SyncMapItemInstance(self._version, payload, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'])
    
    
    def create(self, key, data):
        """
        Create the SyncMapItemInstance

        :param str key: 
        :param object data: 
        
        :returns: The created SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        data = values.of({ 
            'Key': key,
            'Data': serialize.object(data),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SyncMapItemInstance(self._version, payload, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'])
    
    
    def stream(self, order=values.unset, from_=values.unset, bounds=values.unset, limit=None, page_size=None):
        """
        Streams SyncMapItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param QueryResultOrder order: 
        :param str from_: 
        :param QueryFromBoundType bounds: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            order=order,
            from_=from_,
            bounds=bounds,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, order=values.unset, from_=values.unset, bounds=values.unset, limit=None, page_size=None):
        """
        Lists SyncMapItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param QueryResultOrder order: 
        :param str from_: 
        :param QueryFromBoundType bounds: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance]
        """
        return list(self.stream(
            order=order,
            from_=from_,
            bounds=bounds,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, order=values.unset, from_=values.unset, bounds=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SyncMapItemInstance records from the API.
        Request is executed immediately
        
        :param QueryResultOrder order: 
        :param str from_: 
        :param QueryFromBoundType bounds: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemPage
        """
        data = values.of({ 
            'Order': order,
            'From': from_,
            'Bounds': bounds,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SyncMapItemPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SyncMapItemPage(self._version, response, self._solution)


    def get(self, key):
        """
        Constructs a SyncMapItemContext
        
        :param key: 
        
        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        """
        return SyncMapItemContext(self._version, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], key=key)

    def __call__(self, key):
        """
        Constructs a SyncMapItemContext
        
        :param key: 
        
        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        """
        return SyncMapItemContext(self._version, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], key=key)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncMapItemList>'










class SyncMapItemPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SyncMapItemPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemPage
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncMapItemInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        return SyncMapItemInstance(self._version, payload, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Sync.SyncMapItemPage>'




class SyncMapItemInstance(InstanceResource):

    class QueryFromBoundType(object):
        INCLUSIVE = "inclusive"
        EXCLUSIVE = "exclusive"

    class QueryResultOrder(object):
        ASC = "asc"
        DESC = "desc"

    def __init__(self, version, payload, service_sid: str, map_sid: str, key: str=None):
        """
        Initialize the SyncMapItemInstance
        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        super().__init__(version)

        self._properties = { 
            'key': payload.get('key'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'map_sid': payload.get('map_sid'),
            'url': payload.get('url'),
            'revision': payload.get('revision'),
            'data': payload.get('data'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'created_by': payload.get('created_by'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'map_sid': map_sid, 'key': key or self._properties['key'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncMapItemContext for this SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        """
        if self._context is None:
            self._context = SyncMapItemContext(self._version, service_sid=self._solution['service_sid'], map_sid=self._solution['map_sid'], key=self._solution['key'],)
        return self._context
    
    @property
    def key(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['key']
    
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
    def map_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['map_sid']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
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
    
    def delete(self, if_match=values.unset):
        """
        Deletes the SyncMapItemInstance
        
        :params str if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(if_match=if_match, )
    
    def fetch(self):
        """
        Fetch the SyncMapItemInstance
        

        :returns: The fetched SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        return self._proxy.fetch()
    
    def update(self, data, if_match=values.unset):
        """
        Update the SyncMapItemInstance
        
        :params object data: 
        :params str if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        return self._proxy.update(data=data, if_match=if_match, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncMapItemInstance {}>'.format(context)

class SyncMapItemContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, map_sid: str, key: str):
        """
        Initialize the SyncMapItemContext

        :param Version version: Version that contains the resource
        :param service_sid: :param map_sid: :param key: 

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'map_sid': map_sid,
            'key': key,
        }
        self._uri = '/Services/{service_sid}/Maps/{map_sid}/Items/{key}'.format(**self._solution)
        
    
    def delete(self, if_match=values.unset):
        """
        Deletes the SyncMapItemInstance

        :param str if_match: The If-Match HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'If-Match': if_match, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)
        
    def fetch(self):
        """
        Fetch the SyncMapItemInstance
        

        :returns: The fetched SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
            key=self._solution['key'],
            
        )
        
    def update(self, data, if_match=values.unset):
        """
        Update the SyncMapItemInstance
        
        :params object data: 
        :params str if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_item.SyncMapItemInstance
        """
        data = values.of({ 
            'Data': serialize.object(data),
        })
        headers = values.of({'If-Match': if_match, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            map_sid=self._solution['map_sid'],
            key=self._solution['key']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Sync.SyncMapItemContext {}>'.format(context)


