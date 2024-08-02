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


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class OutgoingCallerIdInstance(InstanceResource):

    """
    :ivar sid: The unique string that that we created to identify the OutgoingCallerId resource.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resource.
    :ivar phone_number: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], account_sid: str, sid: Optional[str] = None):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(payload.get("date_created"))
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(payload.get("date_updated"))
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.phone_number: Optional[str] = payload.get("phone_number")
        self.uri: Optional[str] = payload.get("uri")

        
        self._solution = { 
            "account_sid": account_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[OutgoingCallerIdContext] = None

    @property
    def _proxy(self) -> "OutgoingCallerIdContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: OutgoingCallerIdContext for this OutgoingCallerIdInstance
        """
        if self._context is None:
            self._context = OutgoingCallerIdContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    
    def delete(self) -> bool:
        """
        Deletes the OutgoingCallerIdInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()
    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the OutgoingCallerIdInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self) -> "OutgoingCallerIdInstance":
        """
        Fetch the OutgoingCallerIdInstance
        

        :returns: The fetched OutgoingCallerIdInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "OutgoingCallerIdInstance":
        """
        Asynchronous coroutine to fetch the OutgoingCallerIdInstance
        

        :returns: The fetched OutgoingCallerIdInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, friendly_name: Union[str, object]=values.unset) -> "OutgoingCallerIdInstance":
        """
        Update the OutgoingCallerIdInstance
        
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The updated OutgoingCallerIdInstance
        """
        return self._proxy.update(friendly_name=friendly_name, )

    async def update_async(self, friendly_name: Union[str, object]=values.unset) -> "OutgoingCallerIdInstance":
        """
        Asynchronous coroutine to update the OutgoingCallerIdInstance
        
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The updated OutgoingCallerIdInstance
        """
        return await self._proxy.update_async(friendly_name=friendly_name, )
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.OutgoingCallerIdInstance {}>'.format(context)

class OutgoingCallerIdContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the OutgoingCallerIdContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to update.
        :param sid: The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update.
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json'.format(**self._solution)
        
    
    
    def delete(self) -> bool:
        """
        Deletes the OutgoingCallerIdInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the OutgoingCallerIdInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self) -> OutgoingCallerIdInstance:
        """
        Fetch the OutgoingCallerIdInstance
        

        :returns: The fetched OutgoingCallerIdInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return OutgoingCallerIdInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> OutgoingCallerIdInstance:
        """
        Asynchronous coroutine to fetch the OutgoingCallerIdInstance
        

        :returns: The fetched OutgoingCallerIdInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return OutgoingCallerIdInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, friendly_name: Union[str, object]=values.unset) -> OutgoingCallerIdInstance:
        """
        Update the OutgoingCallerIdInstance
        
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The updated OutgoingCallerIdInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return OutgoingCallerIdInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid']
        )

    async def update_async(self, friendly_name: Union[str, object]=values.unset) -> OutgoingCallerIdInstance:
        """
        Asynchronous coroutine to update the OutgoingCallerIdInstance
        
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The updated OutgoingCallerIdInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return OutgoingCallerIdInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid']
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.OutgoingCallerIdContext {}>'.format(context)









class OutgoingCallerIdPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> OutgoingCallerIdInstance:
        """
        Build an instance of OutgoingCallerIdInstance

        :param payload: Payload response from the API
        """
        return OutgoingCallerIdInstance(self._version, payload, account_sid=self._solution["account_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.OutgoingCallerIdPage>"





class OutgoingCallerIdList(ListResource):
    
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the OutgoingCallerIdList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OutgoingCallerId resources to read.
        
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/OutgoingCallerIds.json'.format(**self._solution)
        
        
    
    
    
    
    def stream(self, 
        phone_number: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[OutgoingCallerIdInstance]:
        """
        Streams OutgoingCallerIdInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str phone_number: The phone number of the OutgoingCallerId resources to read.
        :param str friendly_name: The string that identifies the OutgoingCallerId resources to read.
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
            phone_number=phone_number,
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        phone_number: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[OutgoingCallerIdInstance]:
        """
        Asynchronously streams OutgoingCallerIdInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str phone_number: The phone number of the OutgoingCallerId resources to read.
        :param str friendly_name: The string that identifies the OutgoingCallerId resources to read.
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
            phone_number=phone_number,
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        phone_number: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[OutgoingCallerIdInstance]:
        """
        Lists OutgoingCallerIdInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str phone_number: The phone number of the OutgoingCallerId resources to read.
        :param str friendly_name: The string that identifies the OutgoingCallerId resources to read.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            phone_number=phone_number,
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        phone_number: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[OutgoingCallerIdInstance]:
        """
        Asynchronously lists OutgoingCallerIdInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str phone_number: The phone number of the OutgoingCallerId resources to read.
        :param str friendly_name: The string that identifies the OutgoingCallerId resources to read.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            phone_number=phone_number,
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        phone_number: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> OutgoingCallerIdPage:
        """
        Retrieve a single page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately
        
        :param phone_number: The phone number of the OutgoingCallerId resources to read.
        :param friendly_name: The string that identifies the OutgoingCallerId resources to read.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of OutgoingCallerIdInstance
        """
        data = values.of({ 
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return OutgoingCallerIdPage(self._version, response, self._solution)

    async def page_async(self, 
        phone_number: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> OutgoingCallerIdPage:
        """
        Asynchronously retrieve a single page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately
        
        :param phone_number: The phone number of the OutgoingCallerId resources to read.
        :param friendly_name: The string that identifies the OutgoingCallerId resources to read.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of OutgoingCallerIdInstance
        """
        data = values.of({ 
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return OutgoingCallerIdPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> OutgoingCallerIdPage:
        """
        Retrieve a specific page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of OutgoingCallerIdInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return OutgoingCallerIdPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> OutgoingCallerIdPage:
        """
        Asynchronously retrieve a specific page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of OutgoingCallerIdInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return OutgoingCallerIdPage(self._version, response, self._solution)



    def get(self, sid: str) -> OutgoingCallerIdContext:
        """
        Constructs a OutgoingCallerIdContext
        
        :param sid: The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update.
        """
        return OutgoingCallerIdContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid: str) -> OutgoingCallerIdContext:
        """
        Constructs a OutgoingCallerIdContext
        
        :param sid: The Twilio-provided string that uniquely identifies the OutgoingCallerId resource to update.
        """
        return OutgoingCallerIdContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Api.V2010.OutgoingCallerIdList>'

