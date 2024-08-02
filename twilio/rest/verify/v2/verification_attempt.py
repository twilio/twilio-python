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


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class VerificationAttemptInstance(InstanceResource):

    class Channels(object):
        SMS = "sms"
        CALL = "call"
        EMAIL = "email"
        WHATSAPP = "whatsapp"

    class ConversionStatus(object):
        CONVERTED = "converted"
        UNCONVERTED = "unconverted"

    """
    :ivar sid: The SID that uniquely identifies the verification attempt resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Verification resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) used to generate the attempt.
    :ivar verification_sid: The SID of the [Verification](https://www.twilio.com/docs/verify/api/verification) that generated the attempt.
    :ivar date_created: The date that this Attempt was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date that this Attempt was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar conversion_status: 
    :ivar channel: 
    :ivar price: An object containing the charge for this verification attempt related to the channel costs and the currency used. The costs related to the succeeded verifications are not included. May not be immediately available. More information on pricing is available [here](https://www.twilio.com/en-us/verify/pricing).
    :ivar channel_data: An object containing the channel specific information for an attempt.
    :ivar url: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.verification_sid: Optional[str] = payload.get("verification_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_created"))
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_updated"))
        self.conversion_status: Optional["VerificationAttemptInstance.ConversionStatus"] = payload.get("conversion_status")
        self.channel: Optional["VerificationAttemptInstance.Channels"] = payload.get("channel")
        self.price: Optional[Dict[str, object]] = payload.get("price")
        self.channel_data: Optional[Dict[str, object]] = payload.get("channel_data")
        self.url: Optional[str] = payload.get("url")

        
        self._solution = { 
            "sid": sid or self.sid,
        }
        self._context: Optional[VerificationAttemptContext] = None

    @property
    def _proxy(self) -> "VerificationAttemptContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: VerificationAttemptContext for this VerificationAttemptInstance
        """
        if self._context is None:
            self._context = VerificationAttemptContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    
    def fetch(self) -> "VerificationAttemptInstance":
        """
        Fetch the VerificationAttemptInstance
        

        :returns: The fetched VerificationAttemptInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "VerificationAttemptInstance":
        """
        Asynchronous coroutine to fetch the VerificationAttemptInstance
        

        :returns: The fetched VerificationAttemptInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationAttemptInstance {}>'.format(context)

class VerificationAttemptContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the VerificationAttemptContext

        :param version: Version that contains the resource
        :param sid: The unique SID identifier of a Verification Attempt
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Attempts/{sid}'.format(**self._solution)
        
    
    
    def fetch(self) -> VerificationAttemptInstance:
        """
        Fetch the VerificationAttemptInstance
        

        :returns: The fetched VerificationAttemptInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return VerificationAttemptInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> VerificationAttemptInstance:
        """
        Asynchronous coroutine to fetch the VerificationAttemptInstance
        

        :returns: The fetched VerificationAttemptInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return VerificationAttemptInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationAttemptContext {}>'.format(context)





class VerificationAttemptPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> VerificationAttemptInstance:
        """
        Build an instance of VerificationAttemptInstance

        :param payload: Payload response from the API
        """
        return VerificationAttemptInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.VerificationAttemptPage>"





class VerificationAttemptList(ListResource):
    
    def __init__(self, version: Version):
        """
        Initialize the VerificationAttemptList

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/Attempts'
        
        
    
    
    def stream(self, 
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        channel_data_to: Union[str, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union["VerificationAttemptInstance.Channels", object] = values.unset,
        verify_service_sid: Union[str, object] = values.unset,
        verification_sid: Union[str, object] = values.unset,
        status: Union["VerificationAttemptInstance.ConversionStatus", object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[VerificationAttemptInstance]:
        """
        Streams VerificationAttemptInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param datetime date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param datetime date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param &quot;VerificationAttemptInstance.Channels&quot; channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param &quot;VerificationAttemptInstance.ConversionStatus&quot; status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
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
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            channel_data_to=channel_data_to,
            country=country,
            channel=channel,
            verify_service_sid=verify_service_sid,
            verification_sid=verification_sid,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        channel_data_to: Union[str, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union["VerificationAttemptInstance.Channels", object] = values.unset,
        verify_service_sid: Union[str, object] = values.unset,
        verification_sid: Union[str, object] = values.unset,
        status: Union["VerificationAttemptInstance.ConversionStatus", object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[VerificationAttemptInstance]:
        """
        Asynchronously streams VerificationAttemptInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param datetime date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param datetime date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param &quot;VerificationAttemptInstance.Channels&quot; channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param &quot;VerificationAttemptInstance.ConversionStatus&quot; status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
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
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            channel_data_to=channel_data_to,
            country=country,
            channel=channel,
            verify_service_sid=verify_service_sid,
            verification_sid=verification_sid,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        channel_data_to: Union[str, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union["VerificationAttemptInstance.Channels", object] = values.unset,
        verify_service_sid: Union[str, object] = values.unset,
        verification_sid: Union[str, object] = values.unset,
        status: Union["VerificationAttemptInstance.ConversionStatus", object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[VerificationAttemptInstance]:
        """
        Lists VerificationAttemptInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param datetime date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param datetime date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param &quot;VerificationAttemptInstance.Channels&quot; channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param &quot;VerificationAttemptInstance.ConversionStatus&quot; status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            channel_data_to=channel_data_to,
            country=country,
            channel=channel,
            verify_service_sid=verify_service_sid,
            verification_sid=verification_sid,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        channel_data_to: Union[str, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union["VerificationAttemptInstance.Channels", object] = values.unset,
        verify_service_sid: Union[str, object] = values.unset,
        verification_sid: Union[str, object] = values.unset,
        status: Union["VerificationAttemptInstance.ConversionStatus", object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[VerificationAttemptInstance]:
        """
        Asynchronously lists VerificationAttemptInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param datetime date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param datetime date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param str channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param str country: Filter used to query Verification Attempts sent to the specified destination country.
        :param &quot;VerificationAttemptInstance.Channels&quot; channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param str verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param str verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param &quot;VerificationAttemptInstance.ConversionStatus&quot; status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            channel_data_to=channel_data_to,
            country=country,
            channel=channel,
            verify_service_sid=verify_service_sid,
            verification_sid=verification_sid,
            status=status,
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        channel_data_to: Union[str, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union["VerificationAttemptInstance.Channels", object] = values.unset,
        verify_service_sid: Union[str, object] = values.unset,
        verification_sid: Union[str, object] = values.unset,
        status: Union["VerificationAttemptInstance.ConversionStatus", object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> VerificationAttemptPage:
        """
        Retrieve a single page of VerificationAttemptInstance records from the API.
        Request is executed immediately
        
        :param date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param country: Filter used to query Verification Attempts sent to the specified destination country.
        :param channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of VerificationAttemptInstance
        """
        data = values.of({ 
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'ChannelData.To': channel_data_to,
            'Country': country,
            'Channel': channel,
            'VerifyServiceSid': verify_service_sid,
            'VerificationSid': verification_sid,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return VerificationAttemptPage(self._version, response)

    async def page_async(self, 
        date_created_after: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        channel_data_to: Union[str, object] = values.unset,
        country: Union[str, object] = values.unset,
        channel: Union["VerificationAttemptInstance.Channels", object] = values.unset,
        verify_service_sid: Union[str, object] = values.unset,
        verification_sid: Union[str, object] = values.unset,
        status: Union["VerificationAttemptInstance.ConversionStatus", object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> VerificationAttemptPage:
        """
        Asynchronously retrieve a single page of VerificationAttemptInstance records from the API.
        Request is executed immediately
        
        :param date_created_after: Datetime filter used to consider only Verification Attempts created after this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param date_created_before: Datetime filter used to consider only Verification Attempts created before this datetime on the summary aggregation. Given as GMT in ISO 8601 formatted datetime string: yyyy-MM-dd'T'HH:mm:ss'Z.
        :param channel_data_to: Destination of a verification. It is phone number in E.164 format.
        :param country: Filter used to query Verification Attempts sent to the specified destination country.
        :param channel: Filter used to query Verification Attempts by communication channel. Valid values are `SMS` and `CALL`
        :param verify_service_sid: Filter used to query Verification Attempts by verify service. Only attempts of the provided SID will be returned.
        :param verification_sid: Filter used to return all the Verification Attempts of a single verification. Only attempts of the provided verification SID will be returned.
        :param status: Filter used to query Verification Attempts by conversion status. Valid values are `UNCONVERTED`, for attempts that were not converted, and `CONVERTED`, for attempts that were confirmed.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of VerificationAttemptInstance
        """
        data = values.of({ 
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'ChannelData.To': channel_data_to,
            'Country': country,
            'Channel': channel,
            'VerifyServiceSid': verify_service_sid,
            'VerificationSid': verification_sid,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return VerificationAttemptPage(self._version, response)

    def get_page(self, target_url: str) -> VerificationAttemptPage:
        """
        Retrieve a specific page of VerificationAttemptInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of VerificationAttemptInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return VerificationAttemptPage(self._version, response)

    async def get_page_async(self, target_url: str) -> VerificationAttemptPage:
        """
        Asynchronously retrieve a specific page of VerificationAttemptInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of VerificationAttemptInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return VerificationAttemptPage(self._version, response)



    def get(self, sid: str) -> VerificationAttemptContext:
        """
        Constructs a VerificationAttemptContext
        
        :param sid: The unique SID identifier of a Verification Attempt
        """
        return VerificationAttemptContext(self._version, sid=sid)

    def __call__(self, sid: str) -> VerificationAttemptContext:
        """
        Constructs a VerificationAttemptContext
        
        :param sid: The unique SID identifier of a Verification Attempt
        """
        return VerificationAttemptContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Verify.V2.VerificationAttemptList>'

