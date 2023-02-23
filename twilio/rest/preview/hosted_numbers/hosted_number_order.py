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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class HostedNumberOrderList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the HostedNumberOrderList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderList
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/HostedNumberOrders'.format(**self._solution)
        
        
    
    
    
    
    def create(self, phone_number, sms_capability, account_sid=values.unset, friendly_name=values.unset, unique_name=values.unset, cc_emails=values.unset, sms_url=values.unset, sms_method=values.unset, sms_fallback_url=values.unset, sms_fallback_method=values.unset, status_callback_url=values.unset, status_callback_method=values.unset, sms_application_sid=values.unset, address_sid=values.unset, email=values.unset, verification_type=values.unset, verification_document_sid=values.unset):
        """
        Create the HostedNumberOrderInstance

        :param str phone_number: The number to host in [+E.164](https://en.wikipedia.org/wiki/E.164) format
        :param bool sms_capability: Used to specify that the SMS capability will be hosted on Twilio's platform.
        :param str account_sid: This defaults to the AccountSid of the authorization the user is using. This can be provided to specify a subaccount to add the HostedNumberOrder to.
        :param str friendly_name: A 64 character string that is a human readable text that describes this resource.
        :param str unique_name: Optional. Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param list[str] cc_emails: Optional. A list of emails that the LOA document for this HostedNumberOrder will be carbon copied to.
        :param str sms_url: The URL that Twilio should request when somebody sends an SMS to the phone number. This will be copied onto the IncomingPhoneNumber resource.
        :param str sms_method: The HTTP method that should be used to request the SmsUrl. Must be either `GET` or `POST`.  This will be copied onto the IncomingPhoneNumber resource.
        :param str sms_fallback_url: A URL that Twilio will request if an error occurs requesting or executing the TwiML defined by SmsUrl. This will be copied onto the IncomingPhoneNumber resource.
        :param str sms_fallback_method: The HTTP method that should be used to request the SmsFallbackUrl. Must be either `GET` or `POST`. This will be copied onto the IncomingPhoneNumber resource.
        :param str status_callback_url: Optional. The Status Callback URL attached to the IncomingPhoneNumber resource.
        :param str status_callback_method: Optional. The Status Callback Method attached to the IncomingPhoneNumber resource.
        :param str sms_application_sid: Optional. The 34 character sid of the application Twilio should use to handle SMS messages sent to this number. If a `SmsApplicationSid` is present, Twilio will ignore all of the SMS urls above and use those set on the application.
        :param str address_sid: Optional. A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
        :param str email: Optional. Email of the owner of this phone number that is being hosted.
        :param HostedNumberOrderVerificationType verification_type: 
        :param str verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
        
        :returns: The created HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        data = values.of({ 
            'PhoneNumber': phone_number,
            'SmsCapability': sms_capability,
            'AccountSid': account_sid,
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'CcEmails': serialize.map(cc_emails, lambda e: e),
            'SmsUrl': sms_url,
            'SmsMethod': sms_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'StatusCallbackUrl': status_callback_url,
            'StatusCallbackMethod': status_callback_method,
            'SmsApplicationSid': sms_application_sid,
            'AddressSid': address_sid,
            'Email': email,
            'VerificationType': verification_type,
            'VerificationDocumentSid': verification_document_sid,
        })
        )
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return HostedNumberOrderInstance(self._version, payload)
    
    
    def stream(self, status=values.unset, phone_number=values.unset, incoming_phone_number_sid=values.unset, friendly_name=values.unset, unique_name=values.unset, limit=None, page_size=None):
        """
        Streams HostedNumberOrderInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param HostedNumberOrderStatus status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 64 characters.
        :param str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            unique_name=unique_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, phone_number=values.unset, incoming_phone_number_sid=values.unset, friendly_name=values.unset, unique_name=values.unset, limit=None, page_size=None):
        """
        Lists HostedNumberOrderInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param HostedNumberOrderStatus status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 64 characters.
        :param str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance]
        """
        return list(self.stream(
            status=status,
            phone_number=phone_number,
            incoming_phone_number_sid=incoming_phone_number_sid,
            friendly_name=friendly_name,
            unique_name=unique_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, phone_number=values.unset, incoming_phone_number_sid=values.unset, friendly_name=values.unset, unique_name=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of HostedNumberOrderInstance records from the API.
        Request is executed immediately
        
        :param HostedNumberOrderStatus status: The Status of this HostedNumberOrder. One of `received`, `pending-verification`, `verified`, `pending-loa`, `carrier-processing`, `testing`, `completed`, `failed`, or `action-required`.
        :param str phone_number: An E164 formatted phone number hosted by this HostedNumberOrder.
        :param str incoming_phone_number_sid: A 34 character string that uniquely identifies the IncomingPhoneNumber resource created by this HostedNumberOrder.
        :param str friendly_name: A human readable description of this resource, up to 64 characters.
        :param str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderPage
        """
        data = values.of({ 
            'Status': status,
            'PhoneNumber': phone_number,
            'IncomingPhoneNumberSid': incoming_phone_number_sid,
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return HostedNumberOrderPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of HostedNumberOrderInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return HostedNumberOrderPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a HostedNumberOrderContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        """
        return HostedNumberOrderContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a HostedNumberOrderContext
        
        :param sid: 
        
        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        """
        return HostedNumberOrderContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.HostedNumbers.HostedNumberOrderList>'










class HostedNumberOrderPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the HostedNumberOrderPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderPage
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of HostedNumberOrderInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        return HostedNumberOrderInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.HostedNumbers.HostedNumberOrderPage>'




class HostedNumberOrderContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the HostedNumberOrderContext

        :param Version version: Version that contains the resource
        :param sid: 

        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/HostedNumberOrders/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the HostedNumberOrderInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the HostedNumberOrderInstance
        

        :returns: The fetched HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return HostedNumberOrderInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, unique_name=values.unset, email=values.unset, cc_emails=values.unset, status=values.unset, verification_code=values.unset, verification_type=values.unset, verification_document_sid=values.unset, extension=values.unset, call_delay=values.unset):
        """
        Update the HostedNumberOrderInstance
        
        :params str friendly_name: A 64 character string that is a human readable text that describes this resource.
        :params str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :params str email: Email of the owner of this phone number that is being hosted.
        :params list[str] cc_emails: Optional. A list of emails that LOA document for this HostedNumberOrder will be carbon copied to.
        :params HostedNumberOrderStatus status: 
        :params str verification_code: A verification code that is given to the user via a phone call to the phone number that is being hosted.
        :params HostedNumberOrderVerificationType verification_type: 
        :params str verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
        :params str extension: Digits to dial after connecting the verification call.
        :params int call_delay: The number of seconds, between 0 and 60, to delay before initiating the verification call. Defaults to 0.

        :returns: The updated HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Email': email,
            'CcEmails': serialize.map(cc_emails, lambda e: e),
            'Status': status,
            'VerificationCode': verification_code,
            'VerificationType': verification_type,
            'VerificationDocumentSid': verification_document_sid,
            'Extension': extension,
            'CallDelay': call_delay,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return HostedNumberOrderInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.HostedNumbers.HostedNumberOrderContext {}>'.format(context)

class HostedNumberOrderInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the HostedNumberOrderInstance
        :returns: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'incoming_phone_number_sid': payload.get('incoming_phone_number_sid'),
            'address_sid': payload.get('address_sid'),
            'signing_document_sid': payload.get('signing_document_sid'),
            'phone_number': payload.get('phone_number'),
            'capabilities': payload.get('capabilities'),
            'friendly_name': payload.get('friendly_name'),
            'unique_name': payload.get('unique_name'),
            'status': payload.get('status'),
            'failure_reason': payload.get('failure_reason'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'verification_attempts': deserialize.integer(payload.get('verification_attempts')),
            'email': payload.get('email'),
            'cc_emails': payload.get('cc_emails'),
            'url': payload.get('url'),
            'verification_type': payload.get('verification_type'),
            'verification_document_sid': payload.get('verification_document_sid'),
            'extension': payload.get('extension'),
            'call_delay': deserialize.integer(payload.get('call_delay')),
            'verification_code': payload.get('verification_code'),
            'verification_call_sids': payload.get('verification_call_sids'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: HostedNumberOrderContext for this HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderContext
        """
        if self._context is None:
            self._context = HostedNumberOrderContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this HostedNumberOrder.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: A 34 character string that uniquely identifies the account.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def incoming_phone_number_sid(self):
        """
        :returns: A 34 character string that uniquely identifies the [IncomingPhoneNumber](https://www.twilio.com/docs/api/rest/incoming-phone-numbers) resource that represents the phone number being hosted.
        :rtype: str
        """
        return self._properties['incoming_phone_number_sid']
    
    @property
    def address_sid(self):
        """
        :returns: A 34 character string that uniquely identifies the Address resource that represents the address of the owner of this phone number.
        :rtype: str
        """
        return self._properties['address_sid']
    
    @property
    def signing_document_sid(self):
        """
        :returns: A 34 character string that uniquely identifies the [Authorization Document](https://www.twilio.com/docs/api/phone-numbers/hosted-number-authorization-documents) the user needs to sign.
        :rtype: str
        """
        return self._properties['signing_document_sid']
    
    @property
    def phone_number(self):
        """
        :returns: Phone number to be hosted. This must be in [E.164](https://en.wikipedia.org/wiki/E.164) format, e.g., +16175551212
        :rtype: str
        """
        return self._properties['phone_number']
    
    @property
    def capabilities(self):
        """
        :returns: 
        :rtype: PreviewHostedNumbersHostedNumberOrderCapabilities
        """
        return self._properties['capabilities']
    
    @property
    def friendly_name(self):
        """
        :returns: A 64 character string that is a human-readable text that describes this resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def unique_name(self):
        """
        :returns: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: HostedNumberOrderStatus
        """
        return self._properties['status']
    
    @property
    def failure_reason(self):
        """
        :returns: A message that explains why a hosted_number_order went to status \"action-required\"
        :rtype: str
        """
        return self._properties['failure_reason']
    
    @property
    def date_created(self):
        """
        :returns: The date this resource was created, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this resource was updated, given as [GMT RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def verification_attempts(self):
        """
        :returns: The number of attempts made to verify ownership of the phone number that is being hosted.
        :rtype: int
        """
        return self._properties['verification_attempts']
    
    @property
    def email(self):
        """
        :returns: Email of the owner of this phone number that is being hosted.
        :rtype: str
        """
        return self._properties['email']
    
    @property
    def cc_emails(self):
        """
        :returns: A list of emails that LOA document for this HostedNumberOrder will be carbon copied to.
        :rtype: list[str]
        """
        return self._properties['cc_emails']
    
    @property
    def url(self):
        """
        :returns: The URL of this HostedNumberOrder.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def verification_type(self):
        """
        :returns: 
        :rtype: HostedNumberOrderVerificationType
        """
        return self._properties['verification_type']
    
    @property
    def verification_document_sid(self):
        """
        :returns: A 34 character string that uniquely identifies the Identity Document resource that represents the document for verifying ownership of the number to be hosted.
        :rtype: str
        """
        return self._properties['verification_document_sid']
    
    @property
    def extension(self):
        """
        :returns: A numerical extension to be used when making the ownership verification call.
        :rtype: str
        """
        return self._properties['extension']
    
    @property
    def call_delay(self):
        """
        :returns: A value between 0-30 specifying the number of seconds to delay initiating the ownership verification call.
        :rtype: int
        """
        return self._properties['call_delay']
    
    @property
    def verification_code(self):
        """
        :returns: A verification code provided in the response for a user to enter when they pick up the phone call.
        :rtype: str
        """
        return self._properties['verification_code']
    
    @property
    def verification_call_sids(self):
        """
        :returns: A list of 34 character strings that are unique identifiers for the calls placed as part of ownership verification.
        :rtype: list[str]
        """
        return self._properties['verification_call_sids']
    
    def delete(self):
        """
        Deletes the HostedNumberOrderInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the HostedNumberOrderInstance
        

        :returns: The fetched HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, unique_name=values.unset, email=values.unset, cc_emails=values.unset, status=values.unset, verification_code=values.unset, verification_type=values.unset, verification_document_sid=values.unset, extension=values.unset, call_delay=values.unset):
        """
        Update the HostedNumberOrderInstance
        
        :params str friendly_name: A 64 character string that is a human readable text that describes this resource.
        :params str unique_name: Provides a unique and addressable name to be assigned to this HostedNumberOrder, assigned by the developer, to be optionally used in addition to SID.
        :params str email: Email of the owner of this phone number that is being hosted.
        :params list[str] cc_emails: Optional. A list of emails that LOA document for this HostedNumberOrder will be carbon copied to.
        :params HostedNumberOrderStatus status: 
        :params str verification_code: A verification code that is given to the user via a phone call to the phone number that is being hosted.
        :params HostedNumberOrderVerificationType verification_type: 
        :params str verification_document_sid: Optional. The unique sid identifier of the Identity Document that represents the document for verifying ownership of the number to be hosted. Required when VerificationType is phone-bill.
        :params str extension: Digits to dial after connecting the verification call.
        :params int call_delay: The number of seconds, between 0 and 60, to delay before initiating the verification call. Defaults to 0.

        :returns: The updated HostedNumberOrderInstance
        :rtype: twilio.rest.preview.hosted_numbers.hosted_number_order.HostedNumberOrderInstance
        """
        return self._proxy.update(friendly_name=friendly_name, unique_name=unique_name, email=email, cc_emails=cc_emails, status=status, verification_code=verification_code, verification_type=verification_type, verification_document_sid=verification_document_sid, extension=extension, call_delay=call_delay, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.HostedNumbers.HostedNumberOrderInstance {}>'.format(context)


