r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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


class OriginationUrlList(ListResource):

    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the OriginationUrlList

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the OriginationUrl.
        
        :returns: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlList
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'trunk_sid': trunk_sid,  }
        self._uri = '/Trunks/{trunk_sid}/OriginationUrls'.format(**self._solution)
        
        
    
    
    
    
    def create(self, weight, priority, enabled, friendly_name, sip_url):
        """
        Create the OriginationUrlInstance

        :param int weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :param int priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :param bool enabled: Whether the URL is enabled. The default is `true`.
        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema.
        
        :returns: The created OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        data = values.of({ 
            'Weight': weight,
            'Priority': priority,
            'Enabled': enabled,
            'FriendlyName': friendly_name,
            'SipUrl': sip_url,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return OriginationUrlInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'])

    async def create_async(self, weight, priority, enabled, friendly_name, sip_url):
        """
        Asynchronous coroutine to create the OriginationUrlInstance

        :param int weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :param int priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :param bool enabled: Whether the URL is enabled. The default is `true`.
        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema.
        
        :returns: The created OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        data = values.of({ 
            'Weight': weight,
            'Priority': priority,
            'Enabled': enabled,
            'FriendlyName': friendly_name,
            'SipUrl': sip_url,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return OriginationUrlInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams OriginationUrlInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams OriginationUrlInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists OriginationUrlInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists OriginationUrlInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of OriginationUrlInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return OriginationUrlPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of OriginationUrlInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return OriginationUrlPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of OriginationUrlInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return OriginationUrlPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of OriginationUrlInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return OriginationUrlPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a OriginationUrlContext
        
        :param sid: The unique string that we created to identify the OriginationUrl resource to update.
        
        :returns: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlContext
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlContext
        """
        return OriginationUrlContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a OriginationUrlContext
        
        :param sid: The unique string that we created to identify the OriginationUrl resource to update.
        
        :returns: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlContext
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlContext
        """
        return OriginationUrlContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.OriginationUrlList>'










class OriginationUrlPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the OriginationUrlPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlPage
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of OriginationUrlInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        return OriginationUrlInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.OriginationUrlPage>'




class OriginationUrlInstance(InstanceResource):

    def __init__(self, version, payload, trunk_sid: str, sid: str=None):
        """
        Initialize the OriginationUrlInstance
        :returns: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'sid': payload.get('sid'),
            'trunk_sid': payload.get('trunk_sid'),
            'weight': deserialize.integer(payload.get('weight')),
            'enabled': payload.get('enabled'),
            'sip_url': payload.get('sip_url'),
            'friendly_name': payload.get('friendly_name'),
            'priority': deserialize.integer(payload.get('priority')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'trunk_sid': trunk_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: OriginationUrlContext for this OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlContext
        """
        if self._context is None:
            self._context = OriginationUrlContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OriginationUrl resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the OriginationUrl resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def trunk_sid(self):
        """
        :returns: The SID of the Trunk that owns the Origination URL.
        :rtype: str
        """
        return self._properties['trunk_sid']
    
    @property
    def weight(self):
        """
        :returns: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :rtype: int
        """
        return self._properties['weight']
    
    @property
    def enabled(self):
        """
        :returns: Whether the URL is enabled. The default is `true`.
        :rtype: bool
        """
        return self._properties['enabled']
    
    @property
    def sip_url(self):
        """
        :returns: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema.
        :rtype: str
        """
        return self._properties['sip_url']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def priority(self):
        """
        :returns: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :rtype: int
        """
        return self._properties['priority']
    
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
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def delete(self):
        """
        Deletes the OriginationUrlInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the OriginationUrlInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the OriginationUrlInstance
        

        :returns: The fetched OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the OriginationUrlInstance
        

        :returns: The fetched OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, weight=values.unset, priority=values.unset, enabled=values.unset, friendly_name=values.unset, sip_url=values.unset):
        """
        Update the OriginationUrlInstance
        
        :params int weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :params int priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :params bool enabled: Whether the URL is enabled. The default is `true`.
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.

        :returns: The updated OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        return self._proxy.update(weight=weight, priority=priority, enabled=enabled, friendly_name=friendly_name, sip_url=sip_url, )

    async def update_async(self, weight=values.unset, priority=values.unset, enabled=values.unset, friendly_name=values.unset, sip_url=values.unset):
        """
        Asynchronous coroutine to update the OriginationUrlInstance
        
        :params int weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :params int priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :params bool enabled: Whether the URL is enabled. The default is `true`.
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.

        :returns: The updated OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        return await self._proxy.update_async(weight=weight, priority=priority, enabled=enabled, friendly_name=friendly_name, sip_url=sip_url, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.OriginationUrlInstance {}>'.format(context)

class OriginationUrlContext(InstanceContext):

    def __init__(self, version: Version, trunk_sid: str, sid: str):
        """
        Initialize the OriginationUrlContext

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to update the OriginationUrl.
        :param sid: The unique string that we created to identify the OriginationUrl resource to update.

        :returns: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlContext
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'trunk_sid': trunk_sid,
            'sid': sid,
        }
        self._uri = '/Trunks/{trunk_sid}/OriginationUrls/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the OriginationUrlInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the OriginationUrlInstance
        

        :returns: The fetched OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, weight=values.unset, priority=values.unset, enabled=values.unset, friendly_name=values.unset, sip_url=values.unset):
        """
        Update the OriginationUrlInstance
        
        :params int weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :params int priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :params bool enabled: Whether the URL is enabled. The default is `true`.
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.

        :returns: The updated OriginationUrlInstance
        :rtype: twilio.rest.trunking.v1.trunk.origination_url.OriginationUrlInstance
        """
        data = values.of({ 
            'Weight': weight,
            'Priority': priority,
            'Enabled': enabled,
            'FriendlyName': friendly_name,
            'SipUrl': sip_url,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.OriginationUrlContext {}>'.format(context)


