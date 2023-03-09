r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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
from twilio.rest.verify.v2.service.entity.challenge import ChallengeList
from twilio.rest.verify.v2.service.entity.factor import FactorList
from twilio.rest.verify.v2.service.entity.new_factor import NewFactorList


class EntityList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the EntityList

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        
        :returns: twilio.rest.verify.v2.service.entity.EntityList
        :rtype: twilio.rest.verify.v2.service.entity.EntityList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Entities'.format(**self._solution)
        
        
    
    
    
    def create(self, identity):
        """
        Create the EntityInstance

        :param str identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        
        :returns: The created EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityInstance
        """
        data = values.of({ 
            'Identity': identity,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return EntityInstance(self._version, payload, service_sid=self._solution['service_sid'])

    async def create_async(self, identity):
        """
        Asynchronous coroutine to create the EntityInstance

        :param str identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        
        :returns: The created EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityInstance
        """
        data = values.of({ 
            'Identity': identity,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return EntityInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams EntityInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v2.service.entity.EntityInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams EntityInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v2.service.entity.EntityInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EntityInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.entity.EntityInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists EntityInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.entity.EntityInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of EntityInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return EntityPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of EntityInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return EntityPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EntityInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return EntityPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of EntityInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return EntityPage(self._version, response, self._solution)


    def get(self, identity):
        """
        Constructs a EntityContext
        
        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        
        :returns: twilio.rest.verify.v2.service.entity.EntityContext
        :rtype: twilio.rest.verify.v2.service.entity.EntityContext
        """
        return EntityContext(self._version, service_sid=self._solution['service_sid'], identity=identity)

    def __call__(self, identity):
        """
        Constructs a EntityContext
        
        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        
        :returns: twilio.rest.verify.v2.service.entity.EntityContext
        :rtype: twilio.rest.verify.v2.service.entity.EntityContext
        """
        return EntityContext(self._version, service_sid=self._solution['service_sid'], identity=identity)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.EntityList>'








class EntityPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the EntityPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.service.entity.EntityPage
        :rtype: twilio.rest.verify.v2.service.entity.EntityPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EntityInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.entity.EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityInstance
        """
        return EntityInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.EntityPage>'




class EntityInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, identity: str=None):
        """
        Initialize the EntityInstance
        :returns: twilio.rest.verify.v2.service.entity.EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'identity': payload.get('identity'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'identity': identity or self._properties['identity'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EntityContext for this EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityContext
        """
        if self._context is None:
            self._context = EntityContext(self._version, service_sid=self._solution['service_sid'], identity=self._solution['identity'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this Entity.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def identity(self):
        """
        :returns: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The unique SID identifier of the Service.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this Entity was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this Entity was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Contains a dictionary of URL links to nested resources of this Entity.
        :rtype: dict
        """
        return self._properties['links']
    
    
    def delete(self):
        """
        Deletes the EntityInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the EntityInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the EntityInstance
        

        :returns: The fetched EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the EntityInstance
        

        :returns: The fetched EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityInstance
        """
        return await self._proxy.fetch_async()
    
    @property
    def challenges(self):
        """
        Access the challenges

        :returns: twilio.rest.verify.v2.service.entity.ChallengeList
        :rtype: twilio.rest.verify.v2.service.entity.ChallengeList
        """
        return self._proxy.challenges
    
    @property
    def factors(self):
        """
        Access the factors

        :returns: twilio.rest.verify.v2.service.entity.FactorList
        :rtype: twilio.rest.verify.v2.service.entity.FactorList
        """
        return self._proxy.factors
    
    @property
    def new_factors(self):
        """
        Access the new_factors

        :returns: twilio.rest.verify.v2.service.entity.NewFactorList
        :rtype: twilio.rest.verify.v2.service.entity.NewFactorList
        """
        return self._proxy.new_factors
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.EntityInstance {}>'.format(context)

class EntityContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, identity: str):
        """
        Initialize the EntityContext

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.

        :returns: twilio.rest.verify.v2.service.entity.EntityContext
        :rtype: twilio.rest.verify.v2.service.entity.EntityContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'identity': identity,
        }
        self._uri = '/Services/{service_sid}/Entities/{identity}'.format(**self._solution)
        
        self._challenges = None
        self._factors = None
        self._new_factors = None
    
    def delete(self):
        """
        Deletes the EntityInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the EntityInstance
        

        :returns: The fetched EntityInstance
        :rtype: twilio.rest.verify.v2.service.entity.EntityInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return EntityInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            
        )
        
    
    @property
    def challenges(self):
        """
        Access the challenges

        :returns: twilio.rest.verify.v2.service.entity.ChallengeList
        :rtype: twilio.rest.verify.v2.service.entity.ChallengeList
        """
        if self._challenges is None:
            self._challenges = ChallengeList(
                self._version, 
                self._solution['service_sid'],
                self._solution['identity'],
            )
        return self._challenges
    
    @property
    def factors(self):
        """
        Access the factors

        :returns: twilio.rest.verify.v2.service.entity.FactorList
        :rtype: twilio.rest.verify.v2.service.entity.FactorList
        """
        if self._factors is None:
            self._factors = FactorList(
                self._version, 
                self._solution['service_sid'],
                self._solution['identity'],
            )
        return self._factors
    
    @property
    def new_factors(self):
        """
        Access the new_factors

        :returns: twilio.rest.verify.v2.service.entity.NewFactorList
        :rtype: twilio.rest.verify.v2.service.entity.NewFactorList
        """
        if self._new_factors is None:
            self._new_factors = NewFactorList(
                self._version, 
                self._solution['service_sid'],
                self._solution['identity'],
            )
        return self._new_factors
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.EntityContext {}>'.format(context)


