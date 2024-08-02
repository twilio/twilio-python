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
from twilio.rest.preview.hosted_numbers.authorization_document.dependent_hosted_number_order import DependentHostedNumberOrderList


class AuthorizationDocumentInstance(InstanceResource):

    class Status(object):
        OPENED = "opened"
        SIGNING = "signing"
        SIGNED = "signed"
        CANCELED = "canceled"
        FAILED = "failed"

    """
    :ivar sid: A 34 character string that uniquely identifies this AuthorizationDocument.
    :ivar address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
    :ivar status: 
    :ivar email: Email that this AuthorizationDocument will be sent to for signing.
    :ivar cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
    :ivar date_created: The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: 
    :ivar links: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.address_sid: Optional[str] = payload.get("address_sid")
        self.status: Optional["AuthorizationDocumentInstance.Status"] = payload.get("status")
        self.email: Optional[str] = payload.get("email")
        self.cc_emails: Optional[List[str]] = payload.get("cc_emails")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_created"))
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_updated"))
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        
        self._solution = { 
            "sid": sid or self.sid,
        }
        self._context: Optional[AuthorizationDocumentContext] = None

    @property
    def _proxy(self) -> "AuthorizationDocumentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AuthorizationDocumentContext for this AuthorizationDocumentInstance
        """
        if self._context is None:
            self._context = AuthorizationDocumentContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    
    def fetch(self) -> "AuthorizationDocumentInstance":
        """
        Fetch the AuthorizationDocumentInstance
        

        :returns: The fetched AuthorizationDocumentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AuthorizationDocumentInstance":
        """
        Asynchronous coroutine to fetch the AuthorizationDocumentInstance
        

        :returns: The fetched AuthorizationDocumentInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, hosted_number_order_sids: Union[List[str], object]=values.unset, address_sid: Union[str, object]=values.unset, email: Union[str, object]=values.unset, cc_emails: Union[List[str], object]=values.unset, status: Union["AuthorizationDocumentInstance.Status", object]=values.unset, contact_title: Union[str, object]=values.unset, contact_phone_number: Union[str, object]=values.unset) -> "AuthorizationDocumentInstance":
        """
        Update the AuthorizationDocumentInstance
        
        :param hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param email: Email that this AuthorizationDocument will be sent to for signing.
        :param cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
        :param status: 
        :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.

        :returns: The updated AuthorizationDocumentInstance
        """
        return self._proxy.update(hosted_number_order_sids=hosted_number_order_sids, address_sid=address_sid, email=email, cc_emails=cc_emails, status=status, contact_title=contact_title, contact_phone_number=contact_phone_number, )

    async def update_async(self, hosted_number_order_sids: Union[List[str], object]=values.unset, address_sid: Union[str, object]=values.unset, email: Union[str, object]=values.unset, cc_emails: Union[List[str], object]=values.unset, status: Union["AuthorizationDocumentInstance.Status", object]=values.unset, contact_title: Union[str, object]=values.unset, contact_phone_number: Union[str, object]=values.unset) -> "AuthorizationDocumentInstance":
        """
        Asynchronous coroutine to update the AuthorizationDocumentInstance
        
        :param hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param email: Email that this AuthorizationDocument will be sent to for signing.
        :param cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
        :param status: 
        :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.

        :returns: The updated AuthorizationDocumentInstance
        """
        return await self._proxy.update_async(hosted_number_order_sids=hosted_number_order_sids, address_sid=address_sid, email=email, cc_emails=cc_emails, status=status, contact_title=contact_title, contact_phone_number=contact_phone_number, )
    
    @property
    def dependent_hosted_number_orders(self) -> DependentHostedNumberOrderList:
        """
        Access the dependent_hosted_number_orders
        """
        return self._proxy.dependent_hosted_number_orders
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.HostedNumbers.AuthorizationDocumentInstance {}>'.format(context)

class AuthorizationDocumentContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the AuthorizationDocumentContext

        :param version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this AuthorizationDocument.
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/AuthorizationDocuments/{sid}'.format(**self._solution)
        
        self._dependent_hosted_number_orders: Optional[DependentHostedNumberOrderList] = None
    
    
    def fetch(self) -> AuthorizationDocumentInstance:
        """
        Fetch the AuthorizationDocumentInstance
        

        :returns: The fetched AuthorizationDocumentInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AuthorizationDocumentInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> AuthorizationDocumentInstance:
        """
        Asynchronous coroutine to fetch the AuthorizationDocumentInstance
        

        :returns: The fetched AuthorizationDocumentInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return AuthorizationDocumentInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, hosted_number_order_sids: Union[List[str], object]=values.unset, address_sid: Union[str, object]=values.unset, email: Union[str, object]=values.unset, cc_emails: Union[List[str], object]=values.unset, status: Union["AuthorizationDocumentInstance.Status", object]=values.unset, contact_title: Union[str, object]=values.unset, contact_phone_number: Union[str, object]=values.unset) -> AuthorizationDocumentInstance:
        """
        Update the AuthorizationDocumentInstance
        
        :param hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param email: Email that this AuthorizationDocument will be sent to for signing.
        :param cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
        :param status: 
        :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.

        :returns: The updated AuthorizationDocumentInstance
        """
        data = values.of({ 
            'HostedNumberOrderSids': serialize.map(hosted_number_order_sids, lambda e: e),
            'AddressSid': address_sid,
            'Email': email,
            'CcEmails': serialize.map(cc_emails, lambda e: e),
            'Status': status,
            'ContactTitle': contact_title,
            'ContactPhoneNumber': contact_phone_number,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return AuthorizationDocumentInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )

    async def update_async(self, hosted_number_order_sids: Union[List[str], object]=values.unset, address_sid: Union[str, object]=values.unset, email: Union[str, object]=values.unset, cc_emails: Union[List[str], object]=values.unset, status: Union["AuthorizationDocumentInstance.Status", object]=values.unset, contact_title: Union[str, object]=values.unset, contact_phone_number: Union[str, object]=values.unset) -> AuthorizationDocumentInstance:
        """
        Asynchronous coroutine to update the AuthorizationDocumentInstance
        
        :param hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param email: Email that this AuthorizationDocument will be sent to for signing.
        :param cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed
        :param status: 
        :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.

        :returns: The updated AuthorizationDocumentInstance
        """
        data = values.of({ 
            'HostedNumberOrderSids': serialize.map(hosted_number_order_sids, lambda e: e),
            'AddressSid': address_sid,
            'Email': email,
            'CcEmails': serialize.map(cc_emails, lambda e: e),
            'Status': status,
            'ContactTitle': contact_title,
            'ContactPhoneNumber': contact_phone_number,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return AuthorizationDocumentInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
    
    
    @property
    def dependent_hosted_number_orders(self) -> DependentHostedNumberOrderList:
        """
        Access the dependent_hosted_number_orders
        """
        if self._dependent_hosted_number_orders is None:
            self._dependent_hosted_number_orders = DependentHostedNumberOrderList(
                self._version, 
                self._solution['sid'],
            )
        return self._dependent_hosted_number_orders
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.HostedNumbers.AuthorizationDocumentContext {}>'.format(context)









class AuthorizationDocumentPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> AuthorizationDocumentInstance:
        """
        Build an instance of AuthorizationDocumentInstance

        :param payload: Payload response from the API
        """
        return AuthorizationDocumentInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.HostedNumbers.AuthorizationDocumentPage>"





class AuthorizationDocumentList(ListResource):
    
    def __init__(self, version: Version):
        """
        Initialize the AuthorizationDocumentList

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/AuthorizationDocuments'
        
        
    
    
    
    def create(self, hosted_number_order_sids: List[str], address_sid: str, email: str, contact_title: str, contact_phone_number: str, cc_emails: Union[List[str], object]=values.unset) -> AuthorizationDocumentInstance:
        """
        Create the AuthorizationDocumentInstance

        :param hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param email: Email that this AuthorizationDocument will be sent to for signing.
        :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
        :param cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
        
        :returns: The created AuthorizationDocumentInstance
        """
        
        data = values.of({ 
            'HostedNumberOrderSids': serialize.map(hosted_number_order_sids, lambda e: e),
            'AddressSid': address_sid,
            'Email': email,
            'ContactTitle': contact_title,
            'ContactPhoneNumber': contact_phone_number,
            'CcEmails': serialize.map(cc_emails, lambda e: e),
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return AuthorizationDocumentInstance(self._version, payload)

    async def create_async(self, hosted_number_order_sids: List[str], address_sid: str, email: str, contact_title: str, contact_phone_number: str, cc_emails: Union[List[str], object]=values.unset) -> AuthorizationDocumentInstance:
        """
        Asynchronously create the AuthorizationDocumentInstance

        :param hosted_number_order_sids: A list of HostedNumberOrder sids that this AuthorizationDocument will authorize for hosting phone number capabilities on Twilio's platform.
        :param address_sid: A 34 character string that uniquely identifies the Address resource that is associated with this AuthorizationDocument.
        :param email: Email that this AuthorizationDocument will be sent to for signing.
        :param contact_title: The title of the person authorized to sign the Authorization Document for this phone number.
        :param contact_phone_number: The contact phone number of the person authorized to sign the Authorization Document.
        :param cc_emails: Email recipients who will be informed when an Authorization Document has been sent and signed.
        
        :returns: The created AuthorizationDocumentInstance
        """
        
        data = values.of({ 
            'HostedNumberOrderSids': serialize.map(hosted_number_order_sids, lambda e: e),
            'AddressSid': address_sid,
            'Email': email,
            'ContactTitle': contact_title,
            'ContactPhoneNumber': contact_phone_number,
            'CcEmails': serialize.map(cc_emails, lambda e: e),
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return AuthorizationDocumentInstance(self._version, payload)
    
    
    def stream(self, 
        email: Union[str, object] = values.unset,
        status: Union["AuthorizationDocumentInstance.Status", object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AuthorizationDocumentInstance]:
        """
        Streams AuthorizationDocumentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param &quot;AuthorizationDocumentInstance.Status&quot; status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
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
            email=email,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        email: Union[str, object] = values.unset,
        status: Union["AuthorizationDocumentInstance.Status", object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[AuthorizationDocumentInstance]:
        """
        Asynchronously streams AuthorizationDocumentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param &quot;AuthorizationDocumentInstance.Status&quot; status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
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
            email=email,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        email: Union[str, object] = values.unset,
        status: Union["AuthorizationDocumentInstance.Status", object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AuthorizationDocumentInstance]:
        """
        Lists AuthorizationDocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param &quot;AuthorizationDocumentInstance.Status&quot; status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            email=email,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        email: Union[str, object] = values.unset,
        status: Union["AuthorizationDocumentInstance.Status", object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AuthorizationDocumentInstance]:
        """
        Asynchronously lists AuthorizationDocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str email: Email that this AuthorizationDocument will be sent to for signing.
        :param &quot;AuthorizationDocumentInstance.Status&quot; status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            email=email,
            status=status,
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        email: Union[str, object] = values.unset,
        status: Union["AuthorizationDocumentInstance.Status", object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AuthorizationDocumentPage:
        """
        Retrieve a single page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately
        
        :param email: Email that this AuthorizationDocument will be sent to for signing.
        :param status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AuthorizationDocumentInstance
        """
        data = values.of({ 
            'Email': email,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AuthorizationDocumentPage(self._version, response)

    async def page_async(self, 
        email: Union[str, object] = values.unset,
        status: Union["AuthorizationDocumentInstance.Status", object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AuthorizationDocumentPage:
        """
        Asynchronously retrieve a single page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately
        
        :param email: Email that this AuthorizationDocument will be sent to for signing.
        :param status: Status of an instance resource. It can hold one of the values: 1. opened 2. signing, 3. signed LOA, 4. canceled, 5. failed. See the section entitled [Status Values](https://www.twilio.com/docs/phone-numbers/hosted-numbers/hosted-numbers-api/authorization-document-resource#status-values) for more information on each of these statuses.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AuthorizationDocumentInstance
        """
        data = values.of({ 
            'Email': email,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return AuthorizationDocumentPage(self._version, response)

    def get_page(self, target_url: str) -> AuthorizationDocumentPage:
        """
        Retrieve a specific page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AuthorizationDocumentInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AuthorizationDocumentPage(self._version, response)

    async def get_page_async(self, target_url: str) -> AuthorizationDocumentPage:
        """
        Asynchronously retrieve a specific page of AuthorizationDocumentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AuthorizationDocumentInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return AuthorizationDocumentPage(self._version, response)





    def get(self, sid: str) -> AuthorizationDocumentContext:
        """
        Constructs a AuthorizationDocumentContext
        
        :param sid: A 34 character string that uniquely identifies this AuthorizationDocument.
        """
        return AuthorizationDocumentContext(self._version, sid=sid)

    def __call__(self, sid: str) -> AuthorizationDocumentContext:
        """
        Constructs a AuthorizationDocumentContext
        
        :param sid: A 34 character string that uniquely identifies this AuthorizationDocument.
        """
        return AuthorizationDocumentContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Preview.HostedNumbers.AuthorizationDocumentList>'

