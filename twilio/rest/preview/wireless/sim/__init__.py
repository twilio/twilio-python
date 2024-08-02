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
from twilio.rest.preview.wireless.sim.usage import UsageList


class SimInstance(InstanceResource):

    """
    :ivar sid: 
    :ivar unique_name: 
    :ivar account_sid: 
    :ivar rate_plan_sid: 
    :ivar friendly_name: 
    :ivar iccid: 
    :ivar e_id: 
    :ivar status: 
    :ivar commands_callback_url: 
    :ivar commands_callback_method: 
    :ivar sms_fallback_method: 
    :ivar sms_fallback_url: 
    :ivar sms_method: 
    :ivar sms_url: 
    :ivar voice_fallback_method: 
    :ivar voice_fallback_url: 
    :ivar voice_method: 
    :ivar voice_url: 
    :ivar date_created: 
    :ivar date_updated: 
    :ivar url: 
    :ivar links: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.rate_plan_sid: Optional[str] = payload.get("rate_plan_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.iccid: Optional[str] = payload.get("iccid")
        self.e_id: Optional[str] = payload.get("e_id")
        self.status: Optional[str] = payload.get("status")
        self.commands_callback_url: Optional[str] = payload.get("commands_callback_url")
        self.commands_callback_method: Optional[str] = payload.get("commands_callback_method")
        self.sms_fallback_method: Optional[str] = payload.get("sms_fallback_method")
        self.sms_fallback_url: Optional[str] = payload.get("sms_fallback_url")
        self.sms_method: Optional[str] = payload.get("sms_method")
        self.sms_url: Optional[str] = payload.get("sms_url")
        self.voice_fallback_method: Optional[str] = payload.get("voice_fallback_method")
        self.voice_fallback_url: Optional[str] = payload.get("voice_fallback_url")
        self.voice_method: Optional[str] = payload.get("voice_method")
        self.voice_url: Optional[str] = payload.get("voice_url")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_created"))
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_updated"))
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        
        self._solution = { 
            "sid": sid or self.sid,
        }
        self._context: Optional[SimContext] = None

    @property
    def _proxy(self) -> "SimContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SimContext for this SimInstance
        """
        if self._context is None:
            self._context = SimContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    
    def fetch(self) -> "SimInstance":
        """
        Fetch the SimInstance
        

        :returns: The fetched SimInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SimInstance":
        """
        Asynchronous coroutine to fetch the SimInstance
        

        :returns: The fetched SimInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, unique_name: Union[str, object]=values.unset, callback_method: Union[str, object]=values.unset, callback_url: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset, rate_plan: Union[str, object]=values.unset, status: Union[str, object]=values.unset, commands_callback_method: Union[str, object]=values.unset, commands_callback_url: Union[str, object]=values.unset, sms_fallback_method: Union[str, object]=values.unset, sms_fallback_url: Union[str, object]=values.unset, sms_method: Union[str, object]=values.unset, sms_url: Union[str, object]=values.unset, voice_fallback_method: Union[str, object]=values.unset, voice_fallback_url: Union[str, object]=values.unset, voice_method: Union[str, object]=values.unset, voice_url: Union[str, object]=values.unset) -> "SimInstance":
        """
        Update the SimInstance
        
        :param unique_name: 
        :param callback_method: 
        :param callback_url: 
        :param friendly_name: 
        :param rate_plan: 
        :param status: 
        :param commands_callback_method: 
        :param commands_callback_url: 
        :param sms_fallback_method: 
        :param sms_fallback_url: 
        :param sms_method: 
        :param sms_url: 
        :param voice_fallback_method: 
        :param voice_fallback_url: 
        :param voice_method: 
        :param voice_url: 

        :returns: The updated SimInstance
        """
        return self._proxy.update(unique_name=unique_name, callback_method=callback_method, callback_url=callback_url, friendly_name=friendly_name, rate_plan=rate_plan, status=status, commands_callback_method=commands_callback_method, commands_callback_url=commands_callback_url, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_url=sms_url, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_url=voice_url, )

    async def update_async(self, unique_name: Union[str, object]=values.unset, callback_method: Union[str, object]=values.unset, callback_url: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset, rate_plan: Union[str, object]=values.unset, status: Union[str, object]=values.unset, commands_callback_method: Union[str, object]=values.unset, commands_callback_url: Union[str, object]=values.unset, sms_fallback_method: Union[str, object]=values.unset, sms_fallback_url: Union[str, object]=values.unset, sms_method: Union[str, object]=values.unset, sms_url: Union[str, object]=values.unset, voice_fallback_method: Union[str, object]=values.unset, voice_fallback_url: Union[str, object]=values.unset, voice_method: Union[str, object]=values.unset, voice_url: Union[str, object]=values.unset) -> "SimInstance":
        """
        Asynchronous coroutine to update the SimInstance
        
        :param unique_name: 
        :param callback_method: 
        :param callback_url: 
        :param friendly_name: 
        :param rate_plan: 
        :param status: 
        :param commands_callback_method: 
        :param commands_callback_url: 
        :param sms_fallback_method: 
        :param sms_fallback_url: 
        :param sms_method: 
        :param sms_url: 
        :param voice_fallback_method: 
        :param voice_fallback_url: 
        :param voice_method: 
        :param voice_url: 

        :returns: The updated SimInstance
        """
        return await self._proxy.update_async(unique_name=unique_name, callback_method=callback_method, callback_url=callback_url, friendly_name=friendly_name, rate_plan=rate_plan, status=status, commands_callback_method=commands_callback_method, commands_callback_url=commands_callback_url, sms_fallback_method=sms_fallback_method, sms_fallback_url=sms_fallback_url, sms_method=sms_method, sms_url=sms_url, voice_fallback_method=voice_fallback_method, voice_fallback_url=voice_fallback_url, voice_method=voice_method, voice_url=voice_url, )
    
    @property
    def usage(self) -> UsageList:
        """
        Access the usage
        """
        return self._proxy.usage
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.SimInstance {}>'.format(context)

class SimContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the SimContext

        :param version: Version that contains the resource
        :param sid: 
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Sims/{sid}'.format(**self._solution)
        
        self._usage: Optional[UsageList] = None
    
    
    def fetch(self) -> SimInstance:
        """
        Fetch the SimInstance
        

        :returns: The fetched SimInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> SimInstance:
        """
        Asynchronous coroutine to fetch the SimInstance
        

        :returns: The fetched SimInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return SimInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, unique_name: Union[str, object]=values.unset, callback_method: Union[str, object]=values.unset, callback_url: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset, rate_plan: Union[str, object]=values.unset, status: Union[str, object]=values.unset, commands_callback_method: Union[str, object]=values.unset, commands_callback_url: Union[str, object]=values.unset, sms_fallback_method: Union[str, object]=values.unset, sms_fallback_url: Union[str, object]=values.unset, sms_method: Union[str, object]=values.unset, sms_url: Union[str, object]=values.unset, voice_fallback_method: Union[str, object]=values.unset, voice_fallback_url: Union[str, object]=values.unset, voice_method: Union[str, object]=values.unset, voice_url: Union[str, object]=values.unset) -> SimInstance:
        """
        Update the SimInstance
        
        :param unique_name: 
        :param callback_method: 
        :param callback_url: 
        :param friendly_name: 
        :param rate_plan: 
        :param status: 
        :param commands_callback_method: 
        :param commands_callback_url: 
        :param sms_fallback_method: 
        :param sms_fallback_url: 
        :param sms_method: 
        :param sms_url: 
        :param voice_fallback_method: 
        :param voice_fallback_url: 
        :param voice_method: 
        :param voice_url: 

        :returns: The updated SimInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'FriendlyName': friendly_name,
            'RatePlan': rate_plan,
            'Status': status,
            'CommandsCallbackMethod': commands_callback_method,
            'CommandsCallbackUrl': commands_callback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SimInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )

    async def update_async(self, unique_name: Union[str, object]=values.unset, callback_method: Union[str, object]=values.unset, callback_url: Union[str, object]=values.unset, friendly_name: Union[str, object]=values.unset, rate_plan: Union[str, object]=values.unset, status: Union[str, object]=values.unset, commands_callback_method: Union[str, object]=values.unset, commands_callback_url: Union[str, object]=values.unset, sms_fallback_method: Union[str, object]=values.unset, sms_fallback_url: Union[str, object]=values.unset, sms_method: Union[str, object]=values.unset, sms_url: Union[str, object]=values.unset, voice_fallback_method: Union[str, object]=values.unset, voice_fallback_url: Union[str, object]=values.unset, voice_method: Union[str, object]=values.unset, voice_url: Union[str, object]=values.unset) -> SimInstance:
        """
        Asynchronous coroutine to update the SimInstance
        
        :param unique_name: 
        :param callback_method: 
        :param callback_url: 
        :param friendly_name: 
        :param rate_plan: 
        :param status: 
        :param commands_callback_method: 
        :param commands_callback_url: 
        :param sms_fallback_method: 
        :param sms_fallback_url: 
        :param sms_method: 
        :param sms_url: 
        :param voice_fallback_method: 
        :param voice_fallback_url: 
        :param voice_method: 
        :param voice_url: 

        :returns: The updated SimInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'FriendlyName': friendly_name,
            'RatePlan': rate_plan,
            'Status': status,
            'CommandsCallbackMethod': commands_callback_method,
            'CommandsCallbackUrl': commands_callback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return SimInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
    
    
    @property
    def usage(self) -> UsageList:
        """
        Access the usage
        """
        if self._usage is None:
            self._usage = UsageList(
                self._version, 
                self._solution['sid'],
            )
        return self._usage
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Wireless.SimContext {}>'.format(context)







class SimPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> SimInstance:
        """
        Build an instance of SimInstance

        :param payload: Payload response from the API
        """
        return SimInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Wireless.SimPage>"





class SimList(ListResource):
    
    def __init__(self, version: Version):
        """
        Initialize the SimList

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/Sims'
        
        
    
    
    
    def stream(self, 
        status: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        rate_plan: Union[str, object] = values.unset,
        e_id: Union[str, object] = values.unset,
        sim_registration_code: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SimInstance]:
        """
        Streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str status: 
        :param str iccid: 
        :param str rate_plan: 
        :param str e_id: 
        :param str sim_registration_code: 
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
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        status: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        rate_plan: Union[str, object] = values.unset,
        e_id: Union[str, object] = values.unset,
        sim_registration_code: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SimInstance]:
        """
        Asynchronously streams SimInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str status: 
        :param str iccid: 
        :param str rate_plan: 
        :param str e_id: 
        :param str sim_registration_code: 
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
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        status: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        rate_plan: Union[str, object] = values.unset,
        e_id: Union[str, object] = values.unset,
        sim_registration_code: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SimInstance]:
        """
        Lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str status: 
        :param str iccid: 
        :param str rate_plan: 
        :param str e_id: 
        :param str sim_registration_code: 
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        status: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        rate_plan: Union[str, object] = values.unset,
        e_id: Union[str, object] = values.unset,
        sim_registration_code: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SimInstance]:
        """
        Asynchronously lists SimInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str status: 
        :param str iccid: 
        :param str rate_plan: 
        :param str e_id: 
        :param str sim_registration_code: 
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            status=status,
            iccid=iccid,
            rate_plan=rate_plan,
            e_id=e_id,
            sim_registration_code=sim_registration_code,
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        status: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        rate_plan: Union[str, object] = values.unset,
        e_id: Union[str, object] = values.unset,
        sim_registration_code: Union[str, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SimPage:
        """
        Retrieve a single page of SimInstance records from the API.
        Request is executed immediately
        
        :param status: 
        :param iccid: 
        :param rate_plan: 
        :param e_id: 
        :param sim_registration_code: 
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        """
        data = values.of({ 
            'Status': status,
            'Iccid': iccid,
            'RatePlan': rate_plan,
            'EId': e_id,
            'SimRegistrationCode': sim_registration_code,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SimPage(self._version, response)

    async def page_async(self, 
        status: Union[str, object] = values.unset,
        iccid: Union[str, object] = values.unset,
        rate_plan: Union[str, object] = values.unset,
        e_id: Union[str, object] = values.unset,
        sim_registration_code: Union[str, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SimPage:
        """
        Asynchronously retrieve a single page of SimInstance records from the API.
        Request is executed immediately
        
        :param status: 
        :param iccid: 
        :param rate_plan: 
        :param e_id: 
        :param sim_registration_code: 
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SimInstance
        """
        data = values.of({ 
            'Status': status,
            'Iccid': iccid,
            'RatePlan': rate_plan,
            'EId': e_id,
            'SimRegistrationCode': sim_registration_code,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return SimPage(self._version, response)

    def get_page(self, target_url: str) -> SimPage:
        """
        Retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SimPage(self._version, response)

    async def get_page_async(self, target_url: str) -> SimPage:
        """
        Asynchronously retrieve a specific page of SimInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SimInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return SimPage(self._version, response)





    def get(self, sid: str) -> SimContext:
        """
        Constructs a SimContext
        
        :param sid: 
        """
        return SimContext(self._version, sid=sid)

    def __call__(self, sid: str) -> SimContext:
        """
        Constructs a SimContext
        
        :param sid: 
        """
        return SimContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Preview.Wireless.SimList>'

