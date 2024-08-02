r"""
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


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class RatePlanInstance(InstanceResource):

    """
    :ivar sid: 
    :ivar unique_name: 
    :ivar account_sid: 
    :ivar friendly_name: 
    :ivar data_enabled: 
    :ivar data_metering: 
    :ivar data_limit: 
    :ivar messaging_enabled: 
    :ivar voice_enabled: 
    :ivar national_roaming_enabled: 
    :ivar international_roaming: 
    :ivar date_created: 
    :ivar date_updated: 
    :ivar url: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.data_enabled: Optional[bool] = payload.get("data_enabled")
        self.data_metering: Optional[str] = payload.get("data_metering")
        self.data_limit: Optional[int] = deserialize.integer(payload.get("data_limit"))
        self.messaging_enabled: Optional[bool] = payload.get("messaging_enabled")
        self.voice_enabled: Optional[bool] = payload.get("voice_enabled")
        self.national_roaming_enabled: Optional[bool] = payload.get("national_roaming_enabled")
        self.international_roaming: Optional[List[str]] = payload.get("international_roaming")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_created"))
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_updated"))
        self.url: Optional[str] = payload.get("url")

        
        self._solution = { 
            "sid": sid or self.sid,
        }
        self._context: Optional[RatePlanContext] = None

    @property
    def _proxy(self) -> "RatePlanContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RatePlanContext for this RatePlanInstance
        """
        if self._context is None:
            self._context = RatePlanContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    
    def delete(self) -> bool:
        """
        Deletes the RatePlanInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()
    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RatePlanInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self) -> "RatePlanInstance":
        """
        Fetch the RatePlanInstance
        

        :returns: The fetched RatePlanInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RatePlanInstance":
        """
        Asynchronous coroutine to fetch the RatePlanInstance
        

        :returns: The fetched RatePlanInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, unique_name: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset) -> "RatePlanInstance":
        """
        Update the RatePlanInstance
        
        :param unique_name: 
        :param friendly_name: 

        :returns: The updated RatePlanInstance
        """
        return self._proxy.update(unique_name=unique_name, friendly_name=friendly_name, )

    async def update_async(self, unique_name: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset) -> "RatePlanInstance":
        """
        Asynchronous coroutine to update the RatePlanInstance
        
        :param unique_name: 
        :param friendly_name: 

        :returns: The updated RatePlanInstance
        """
        return await self._proxy.update_async(unique_name=unique_name, friendly_name=friendly_name, )
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.RatePlanInstance {}>'.format(context)

class RatePlanContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the RatePlanContext

        :param version: Version that contains the resource
        :param sid: 
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/RatePlans/{sid}'.format(**self._solution)
        
    
    
    def delete(self) -> bool:
        """
        Deletes the RatePlanInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RatePlanInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self) -> RatePlanInstance:
        """
        Fetch the RatePlanInstance
        

        :returns: The fetched RatePlanInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> RatePlanInstance:
        """
        Asynchronous coroutine to fetch the RatePlanInstance
        

        :returns: The fetched RatePlanInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, unique_name: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset) -> RatePlanInstance:
        """
        Update the RatePlanInstance
        
        :param unique_name: 
        :param friendly_name: 

        :returns: The updated RatePlanInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )

    async def update_async(self, unique_name: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset) -> RatePlanInstance:
        """
        Asynchronous coroutine to update the RatePlanInstance
        
        :param unique_name: 
        :param friendly_name: 

        :returns: The updated RatePlanInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return RatePlanInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.RatePlanContext {}>'.format(context)











class RatePlanPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> RatePlanInstance:
        """
        Build an instance of RatePlanInstance

        :param payload: Payload response from the API
        """
        return RatePlanInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Wireless.RatePlanPage>"





class RatePlanList(ListResource):
    
    def __init__(self, version: Version):
        """
        Initialize the RatePlanList

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/RatePlans'
        
        
    
    
    
    
    def create(self, unique_name: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset, data_enabled: Union[bool, object]=values.unset, data_limit: Union[int, object]=values.unset, data_metering: Union[str, object]=values.unset, messaging_enabled: Union[bool, object]=values.unset, voice_enabled: Union[bool, object]=values.unset, commands_enabled: Union[bool, object]=values.unset, national_roaming_enabled: Union[bool, object]=values.unset, international_roaming: Union[List[str], object]=values.unset) -> RatePlanInstance:
        """
        Create the RatePlanInstance

        :param unique_name: 
        :param friendly_name: 
        :param data_enabled: 
        :param data_limit: 
        :param data_metering: 
        :param messaging_enabled: 
        :param voice_enabled: 
        :param commands_enabled: 
        :param national_roaming_enabled: 
        :param international_roaming: 
        
        :returns: The created RatePlanInstance
        """
        
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'DataEnabled': serialize.boolean_to_string(data_enabled),
            'DataLimit': data_limit,
            'DataMetering': data_metering,
            'MessagingEnabled': serialize.boolean_to_string(messaging_enabled),
            'VoiceEnabled': serialize.boolean_to_string(voice_enabled),
            'CommandsEnabled': serialize.boolean_to_string(commands_enabled),
            'NationalRoamingEnabled': serialize.boolean_to_string(national_roaming_enabled),
            'InternationalRoaming': serialize.map(international_roaming, lambda e: e),
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return RatePlanInstance(self._version, payload)

    async def create_async(self, unique_name: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset, data_enabled: Union[bool, object]=values.unset, data_limit: Union[int, object]=values.unset, data_metering: Union[str, object]=values.unset, messaging_enabled: Union[bool, object]=values.unset, voice_enabled: Union[bool, object]=values.unset, commands_enabled: Union[bool, object]=values.unset, national_roaming_enabled: Union[bool, object]=values.unset, international_roaming: Union[List[str], object]=values.unset) -> RatePlanInstance:
        """
        Asynchronously create the RatePlanInstance

        :param unique_name: 
        :param friendly_name: 
        :param data_enabled: 
        :param data_limit: 
        :param data_metering: 
        :param messaging_enabled: 
        :param voice_enabled: 
        :param commands_enabled: 
        :param national_roaming_enabled: 
        :param international_roaming: 
        
        :returns: The created RatePlanInstance
        """
        
        data = values.of({ 
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'DataEnabled': serialize.boolean_to_string(data_enabled),
            'DataLimit': data_limit,
            'DataMetering': data_metering,
            'MessagingEnabled': serialize.boolean_to_string(messaging_enabled),
            'VoiceEnabled': serialize.boolean_to_string(voice_enabled),
            'CommandsEnabled': serialize.boolean_to_string(commands_enabled),
            'NationalRoamingEnabled': serialize.boolean_to_string(national_roaming_enabled),
            'InternationalRoaming': serialize.map(international_roaming, lambda e: e),
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return RatePlanInstance(self._version, payload)
    
    
    def stream(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[RatePlanInstance]:
        """
        Streams RatePlanInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
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
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[RatePlanInstance]:
        """
        Asynchronously streams RatePlanInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
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
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RatePlanInstance]:
        """
        Lists RatePlanInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RatePlanInstance]:
        """
        Asynchronously lists RatePlanInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RatePlanPage:
        """
        Retrieve a single page of RatePlanInstance records from the API.
        Request is executed immediately
        
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RatePlanInstance
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RatePlanPage(self._version, response)

    async def page_async(self, 
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RatePlanPage:
        """
        Asynchronously retrieve a single page of RatePlanInstance records from the API.
        Request is executed immediately
        
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RatePlanInstance
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return RatePlanPage(self._version, response)

    def get_page(self, target_url: str) -> RatePlanPage:
        """
        Retrieve a specific page of RatePlanInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RatePlanInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RatePlanPage(self._version, response)

    async def get_page_async(self, target_url: str) -> RatePlanPage:
        """
        Asynchronously retrieve a specific page of RatePlanInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RatePlanInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return RatePlanPage(self._version, response)



    def get(self, sid: str) -> RatePlanContext:
        """
        Constructs a RatePlanContext
        
        :param sid: 
        """
        return RatePlanContext(self._version, sid=sid)

    def __call__(self, sid: str) -> RatePlanContext:
        """
        Constructs a RatePlanContext
        
        :param sid: 
        """
        return RatePlanContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Preview.Wireless.RatePlanList>'

