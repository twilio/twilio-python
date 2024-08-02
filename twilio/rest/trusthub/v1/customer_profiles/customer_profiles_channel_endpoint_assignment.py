r"""
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


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CustomerProfilesChannelEndpointAssignmentInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Item Assignment resource.
    :ivar customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Item Assignment resource.
    :ivar channel_endpoint_type: The type of channel endpoint. eg: phone-number
    :ivar channel_endpoint_sid: The SID of an channel endpoint
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Identity resource.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], customer_profile_sid: str, sid: Optional[str] = None):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.customer_profile_sid: Optional[str] = payload.get("customer_profile_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.channel_endpoint_type: Optional[str] = payload.get("channel_endpoint_type")
        self.channel_endpoint_sid: Optional[str] = payload.get("channel_endpoint_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_created"))
        self.url: Optional[str] = payload.get("url")

        
        self._solution = { 
            "customer_profile_sid": customer_profile_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[CustomerProfilesChannelEndpointAssignmentContext] = None

    @property
    def _proxy(self) -> "CustomerProfilesChannelEndpointAssignmentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CustomerProfilesChannelEndpointAssignmentContext for this CustomerProfilesChannelEndpointAssignmentInstance
        """
        if self._context is None:
            self._context = CustomerProfilesChannelEndpointAssignmentContext(self._version, customer_profile_sid=self._solution['customer_profile_sid'], sid=self._solution['sid'],)
        return self._context
    
    
    def delete(self) -> bool:
        """
        Deletes the CustomerProfilesChannelEndpointAssignmentInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()
    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CustomerProfilesChannelEndpointAssignmentInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self) -> "CustomerProfilesChannelEndpointAssignmentInstance":
        """
        Fetch the CustomerProfilesChannelEndpointAssignmentInstance
        

        :returns: The fetched CustomerProfilesChannelEndpointAssignmentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CustomerProfilesChannelEndpointAssignmentInstance":
        """
        Asynchronous coroutine to fetch the CustomerProfilesChannelEndpointAssignmentInstance
        

        :returns: The fetched CustomerProfilesChannelEndpointAssignmentInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesChannelEndpointAssignmentInstance {}>'.format(context)

class CustomerProfilesChannelEndpointAssignmentContext(InstanceContext):

    def __init__(self, version: Version, customer_profile_sid: str, sid: str):
        """
        Initialize the CustomerProfilesChannelEndpointAssignmentContext

        :param version: Version that contains the resource
        :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
        :param sid: The unique string that we created to identify the resource.
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'customer_profile_sid': customer_profile_sid,
            'sid': sid,
        }
        self._uri = '/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments/{sid}'.format(**self._solution)
        
    
    
    def delete(self) -> bool:
        """
        Deletes the CustomerProfilesChannelEndpointAssignmentInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CustomerProfilesChannelEndpointAssignmentInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self) -> CustomerProfilesChannelEndpointAssignmentInstance:
        """
        Fetch the CustomerProfilesChannelEndpointAssignmentInstance
        

        :returns: The fetched CustomerProfilesChannelEndpointAssignmentInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CustomerProfilesChannelEndpointAssignmentInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution['customer_profile_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> CustomerProfilesChannelEndpointAssignmentInstance:
        """
        Asynchronous coroutine to fetch the CustomerProfilesChannelEndpointAssignmentInstance
        

        :returns: The fetched CustomerProfilesChannelEndpointAssignmentInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return CustomerProfilesChannelEndpointAssignmentInstance(
            self._version,
            payload,
            customer_profile_sid=self._solution['customer_profile_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.CustomerProfilesChannelEndpointAssignmentContext {}>'.format(context)









class CustomerProfilesChannelEndpointAssignmentPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> CustomerProfilesChannelEndpointAssignmentInstance:
        """
        Build an instance of CustomerProfilesChannelEndpointAssignmentInstance

        :param payload: Payload response from the API
        """
        return CustomerProfilesChannelEndpointAssignmentInstance(self._version, payload, customer_profile_sid=self._solution["customer_profile_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.CustomerProfilesChannelEndpointAssignmentPage>"





class CustomerProfilesChannelEndpointAssignmentList(ListResource):
    
    def __init__(self, version: Version, customer_profile_sid: str):
        """
        Initialize the CustomerProfilesChannelEndpointAssignmentList

        :param version: Version that contains the resource
        :param customer_profile_sid: The unique string that we created to identify the CustomerProfile resource.
        
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 'customer_profile_sid': customer_profile_sid,  }
        self._uri = '/CustomerProfiles/{customer_profile_sid}/ChannelEndpointAssignments'.format(**self._solution)
        
        
    
    
    
    def create(self, channel_endpoint_type: str, channel_endpoint_sid: str) -> CustomerProfilesChannelEndpointAssignmentInstance:
        """
        Create the CustomerProfilesChannelEndpointAssignmentInstance

        :param channel_endpoint_type: The type of channel endpoint. eg: phone-number
        :param channel_endpoint_sid: The SID of an channel endpoint
        
        :returns: The created CustomerProfilesChannelEndpointAssignmentInstance
        """
        
        data = values.of({ 
            'ChannelEndpointType': channel_endpoint_type,
            'ChannelEndpointSid': channel_endpoint_sid,
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return CustomerProfilesChannelEndpointAssignmentInstance(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'])

    async def create_async(self, channel_endpoint_type: str, channel_endpoint_sid: str) -> CustomerProfilesChannelEndpointAssignmentInstance:
        """
        Asynchronously create the CustomerProfilesChannelEndpointAssignmentInstance

        :param channel_endpoint_type: The type of channel endpoint. eg: phone-number
        :param channel_endpoint_sid: The SID of an channel endpoint
        
        :returns: The created CustomerProfilesChannelEndpointAssignmentInstance
        """
        
        data = values.of({ 
            'ChannelEndpointType': channel_endpoint_type,
            'ChannelEndpointSid': channel_endpoint_sid,
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return CustomerProfilesChannelEndpointAssignmentInstance(self._version, payload, customer_profile_sid=self._solution['customer_profile_sid'])
    
    
    def stream(self, 
        channel_endpoint_sid: Union[str, object] = values.unset,
        channel_endpoint_sids: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[CustomerProfilesChannelEndpointAssignmentInstance]:
        """
        Streams CustomerProfilesChannelEndpointAssignmentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        channel_endpoint_sid: Union[str, object] = values.unset,
        channel_endpoint_sids: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[CustomerProfilesChannelEndpointAssignmentInstance]:
        """
        Asynchronously streams CustomerProfilesChannelEndpointAssignmentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        channel_endpoint_sid: Union[str, object] = values.unset,
        channel_endpoint_sids: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CustomerProfilesChannelEndpointAssignmentInstance]:
        """
        Lists CustomerProfilesChannelEndpointAssignmentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        channel_endpoint_sid: Union[str, object] = values.unset,
        channel_endpoint_sids: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CustomerProfilesChannelEndpointAssignmentInstance]:
        """
        Asynchronously lists CustomerProfilesChannelEndpointAssignmentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str channel_endpoint_sid: The SID of an channel endpoint
        :param str channel_endpoint_sids: comma separated list of channel endpoint sids
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            channel_endpoint_sid=channel_endpoint_sid,
            channel_endpoint_sids=channel_endpoint_sids,
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        channel_endpoint_sid: Union[str, object] = values.unset,
        channel_endpoint_sids: Union[str, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CustomerProfilesChannelEndpointAssignmentPage:
        """
        Retrieve a single page of CustomerProfilesChannelEndpointAssignmentInstance records from the API.
        Request is executed immediately
        
        :param channel_endpoint_sid: The SID of an channel endpoint
        :param channel_endpoint_sids: comma separated list of channel endpoint sids
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CustomerProfilesChannelEndpointAssignmentInstance
        """
        data = values.of({ 
            'ChannelEndpointSid': channel_endpoint_sid,
            'ChannelEndpointSids': channel_endpoint_sids,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CustomerProfilesChannelEndpointAssignmentPage(self._version, response, self._solution)

    async def page_async(self, 
        channel_endpoint_sid: Union[str, object] = values.unset,
        channel_endpoint_sids: Union[str, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CustomerProfilesChannelEndpointAssignmentPage:
        """
        Asynchronously retrieve a single page of CustomerProfilesChannelEndpointAssignmentInstance records from the API.
        Request is executed immediately
        
        :param channel_endpoint_sid: The SID of an channel endpoint
        :param channel_endpoint_sids: comma separated list of channel endpoint sids
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CustomerProfilesChannelEndpointAssignmentInstance
        """
        data = values.of({ 
            'ChannelEndpointSid': channel_endpoint_sid,
            'ChannelEndpointSids': channel_endpoint_sids,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return CustomerProfilesChannelEndpointAssignmentPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> CustomerProfilesChannelEndpointAssignmentPage:
        """
        Retrieve a specific page of CustomerProfilesChannelEndpointAssignmentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CustomerProfilesChannelEndpointAssignmentInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CustomerProfilesChannelEndpointAssignmentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> CustomerProfilesChannelEndpointAssignmentPage:
        """
        Asynchronously retrieve a specific page of CustomerProfilesChannelEndpointAssignmentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CustomerProfilesChannelEndpointAssignmentInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return CustomerProfilesChannelEndpointAssignmentPage(self._version, response, self._solution)



    def get(self, sid: str) -> CustomerProfilesChannelEndpointAssignmentContext:
        """
        Constructs a CustomerProfilesChannelEndpointAssignmentContext
        
        :param sid: The unique string that we created to identify the resource.
        """
        return CustomerProfilesChannelEndpointAssignmentContext(self._version, customer_profile_sid=self._solution['customer_profile_sid'], sid=sid)

    def __call__(self, sid: str) -> CustomerProfilesChannelEndpointAssignmentContext:
        """
        Constructs a CustomerProfilesChannelEndpointAssignmentContext
        
        :param sid: The unique string that we created to identify the resource.
        """
        return CustomerProfilesChannelEndpointAssignmentContext(self._version, customer_profile_sid=self._solution['customer_profile_sid'], sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Trusthub.V1.CustomerProfilesChannelEndpointAssignmentList>'

