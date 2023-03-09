r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class SigningKeyList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the SigningKeyList

        :param Version version: Version that contains the resource
        :param account_sid: 
        
        :returns: twilio.rest.api.v2010.account.signing_key.SigningKeyList
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/SigningKeys.json'.format(**self._solution)
        
        
    
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams SigningKeyInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.signing_key.SigningKeyInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams SigningKeyInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.signing_key.SigningKeyInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SigningKeyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.signing_key.SigningKeyInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists SigningKeyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.signing_key.SigningKeyInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SigningKeyInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SigningKeyPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of SigningKeyInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return SigningKeyPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SigningKeyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SigningKeyPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of SigningKeyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return SigningKeyPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SigningKeyContext
        
        :param sid: 
        
        :returns: twilio.rest.api.v2010.account.signing_key.SigningKeyContext
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyContext
        """
        return SigningKeyContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a SigningKeyContext
        
        :param sid: 
        
        :returns: twilio.rest.api.v2010.account.signing_key.SigningKeyContext
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyContext
        """
        return SigningKeyContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SigningKeyList>'








class SigningKeyPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SigningKeyPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.signing_key.SigningKeyPage
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SigningKeyInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        """
        return SigningKeyInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.SigningKeyPage>'




class SigningKeyInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the SigningKeyInstance
        :returns: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SigningKeyContext for this SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyContext
        """
        if self._context is None:
            self._context = SigningKeyContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
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
    
    
    def delete(self):
        """
        Deletes the SigningKeyInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the SigningKeyInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the SigningKeyInstance
        

        :returns: The fetched SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SigningKeyInstance
        

        :returns: The fetched SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, friendly_name=values.unset):
        """
        Update the SigningKeyInstance
        
        :params str friendly_name: 

        :returns: The updated SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        """
        return self._proxy.update(friendly_name=friendly_name, )

    async def update_async(self, friendly_name=values.unset):
        """
        Asynchronous coroutine to update the SigningKeyInstance
        
        :params str friendly_name: 

        :returns: The updated SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        """
        return await self._proxy.update_async(friendly_name=friendly_name, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.SigningKeyInstance {}>'.format(context)

class SigningKeyContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the SigningKeyContext

        :param Version version: Version that contains the resource
        :param account_sid: 
        :param sid: 

        :returns: twilio.rest.api.v2010.account.signing_key.SigningKeyContext
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SigningKeys/{sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the SigningKeyInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SigningKeyInstance
        

        :returns: The fetched SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset):
        """
        Update the SigningKeyInstance
        
        :params str friendly_name: 

        :returns: The updated SigningKeyInstance
        :rtype: twilio.rest.api.v2010.account.signing_key.SigningKeyInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SigningKeyInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.SigningKeyContext {}>'.format(context)


