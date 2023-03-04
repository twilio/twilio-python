"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
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
from twilio.rest.messaging.v1.service.alpha_sender import AlphaSenderList
from twilio.rest.messaging.v1.service.phone_number import PhoneNumberList
from twilio.rest.messaging.v1.service.short_code import ShortCodeList
from twilio.rest.messaging.v1.service.us_app_to_person import UsAppToPersonList
from twilio.rest.messaging.v1.service.us_app_to_person_usecase import UsAppToPersonUsecaseList


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.messaging.v1.service.ServiceList
        :rtype: twilio.rest.messaging.v1.service.ServiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, inbound_request_url=values.unset, inbound_method=values.unset, fallback_url=values.unset, fallback_method=values.unset, status_callback=values.unset, sticky_sender=values.unset, mms_converter=values.unset, smart_encoding=values.unset, scan_message_content=values.unset, fallback_to_long_code=values.unset, area_code_geomatch=values.unset, validity_period=values.unset, synchronous_validation=values.unset, usecase=values.unset, use_inbound_webhook_on_number=values.unset):
        """
        Create the ServiceInstance

        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str inbound_request_url: The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
        :param str inbound_method: The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.
        :param str fallback_url: The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
        :param str fallback_method: The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.
        :param str status_callback: The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
        :param bool sticky_sender: Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.
        :param bool mms_converter: Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.
        :param bool smart_encoding: Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.
        :param ServiceScanMessageContent scan_message_content: 
        :param bool fallback_to_long_code: Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.
        :param bool area_code_geomatch: Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.
        :param int validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
        :param bool synchronous_validation: Reserved.
        :param str usecase: A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..].
        :param bool use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.
        
        :returns: The created ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'InboundRequestUrl': inbound_request_url,
            'InboundMethod': inbound_method,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'StatusCallback': status_callback,
            'StickySender': sticky_sender,
            'MmsConverter': mms_converter,
            'SmartEncoding': smart_encoding,
            'ScanMessageContent': scan_message_content,
            'FallbackToLongCode': fallback_to_long_code,
            'AreaCodeGeomatch': area_code_geomatch,
            'ValidityPeriod': validity_period,
            'SynchronousValidation': synchronous_validation,
            'Usecase': usecase,
            'UseInboundWebhookOnNumber': use_inbound_webhook_on_number,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.messaging.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.ServiceInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServicePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ServicePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: The SID of the Service resource to update.
        
        :returns: twilio.rest.messaging.v1.service.ServiceContext
        :rtype: twilio.rest.messaging.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: The SID of the Service resource to update.
        
        :returns: twilio.rest.messaging.v1.service.ServiceContext
        :rtype: twilio.rest.messaging.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ServiceList>'










class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.service.ServicePage
        :rtype: twilio.rest.messaging.v1.service.ServicePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.service.ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ServicePage>'




class ServiceInstance(InstanceResource):

    class ServiceScanMessageContent(object):
        INHERIT = "inherit"
        ENABLE = "enable"
        DISABLE = "disable"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the ServiceInstance
        :returns: twilio.rest.messaging.v1.service.ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'inbound_request_url': payload.get('inbound_request_url'),
            'inbound_method': payload.get('inbound_method'),
            'fallback_url': payload.get('fallback_url'),
            'fallback_method': payload.get('fallback_method'),
            'status_callback': payload.get('status_callback'),
            'sticky_sender': payload.get('sticky_sender'),
            'mms_converter': payload.get('mms_converter'),
            'smart_encoding': payload.get('smart_encoding'),
            'scan_message_content': payload.get('scan_message_content'),
            'fallback_to_long_code': payload.get('fallback_to_long_code'),
            'area_code_geomatch': payload.get('area_code_geomatch'),
            'synchronous_validation': payload.get('synchronous_validation'),
            'validity_period': deserialize.integer(payload.get('validity_period')),
            'url': payload.get('url'),
            'links': payload.get('links'),
            'usecase': payload.get('usecase'),
            'us_app_to_person_registered': payload.get('us_app_to_person_registered'),
            'use_inbound_webhook_on_number': payload.get('use_inbound_webhook_on_number'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Service resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def inbound_request_url(self):
        """
        :returns: The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
        :rtype: str
        """
        return self._properties['inbound_request_url']
    
    @property
    def inbound_method(self):
        """
        :returns: The HTTP method we use to call `inbound_request_url`. Can be `GET` or `POST`.
        :rtype: str
        """
        return self._properties['inbound_method']
    
    @property
    def fallback_url(self):
        """
        :returns: The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
        :rtype: str
        """
        return self._properties['fallback_url']
    
    @property
    def fallback_method(self):
        """
        :returns: The HTTP method we use to call `fallback_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['fallback_method']
    
    @property
    def status_callback(self):
        """
        :returns: The URL we call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
        :rtype: str
        """
        return self._properties['status_callback']
    
    @property
    def sticky_sender(self):
        """
        :returns: Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.
        :rtype: bool
        """
        return self._properties['sticky_sender']
    
    @property
    def mms_converter(self):
        """
        :returns: Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.
        :rtype: bool
        """
        return self._properties['mms_converter']
    
    @property
    def smart_encoding(self):
        """
        :returns: Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.
        :rtype: bool
        """
        return self._properties['smart_encoding']
    
    @property
    def scan_message_content(self):
        """
        :returns: 
        :rtype: ServiceScanMessageContent
        """
        return self._properties['scan_message_content']
    
    @property
    def fallback_to_long_code(self):
        """
        :returns: Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.
        :rtype: bool
        """
        return self._properties['fallback_to_long_code']
    
    @property
    def area_code_geomatch(self):
        """
        :returns: Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.
        :rtype: bool
        """
        return self._properties['area_code_geomatch']
    
    @property
    def synchronous_validation(self):
        """
        :returns: Reserved.
        :rtype: bool
        """
        return self._properties['synchronous_validation']
    
    @property
    def validity_period(self):
        """
        :returns: How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
        :rtype: int
        """
        return self._properties['validity_period']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Service resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The absolute URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    @property
    def usecase(self):
        """
        :returns: A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..]
        :rtype: str
        """
        return self._properties['usecase']
    
    @property
    def us_app_to_person_registered(self):
        """
        :returns: Whether US A2P campaign is registered for this Service.
        :rtype: bool
        """
        return self._properties['us_app_to_person_registered']
    
    @property
    def use_inbound_webhook_on_number(self):
        """
        :returns: A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.
        :rtype: bool
        """
        return self._properties['use_inbound_webhook_on_number']
    
    def delete(self):
        """
        Deletes the ServiceInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, inbound_request_url=values.unset, inbound_method=values.unset, fallback_url=values.unset, fallback_method=values.unset, status_callback=values.unset, sticky_sender=values.unset, mms_converter=values.unset, smart_encoding=values.unset, scan_message_content=values.unset, fallback_to_long_code=values.unset, area_code_geomatch=values.unset, validity_period=values.unset, synchronous_validation=values.unset, usecase=values.unset, use_inbound_webhook_on_number=values.unset):
        """
        Update the ServiceInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str inbound_request_url: The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
        :params str inbound_method: The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.
        :params str fallback_url: The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
        :params str fallback_method: The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.
        :params str status_callback: The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
        :params bool sticky_sender: Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.
        :params bool mms_converter: Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.
        :params bool smart_encoding: Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.
        :params ServiceScanMessageContent scan_message_content: 
        :params bool fallback_to_long_code: Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.
        :params bool area_code_geomatch: Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.
        :params int validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
        :params bool synchronous_validation: Reserved.
        :params str usecase: A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..]
        :params bool use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        return self._proxy.update(friendly_name=friendly_name, inbound_request_url=inbound_request_url, inbound_method=inbound_method, fallback_url=fallback_url, fallback_method=fallback_method, status_callback=status_callback, sticky_sender=sticky_sender, mms_converter=mms_converter, smart_encoding=smart_encoding, scan_message_content=scan_message_content, fallback_to_long_code=fallback_to_long_code, area_code_geomatch=area_code_geomatch, validity_period=validity_period, synchronous_validation=synchronous_validation, usecase=usecase, use_inbound_webhook_on_number=use_inbound_webhook_on_number, )
    
    @property
    def alpha_senders(self):
        """
        Access the alpha_senders

        :returns: twilio.rest.messaging.v1.service.AlphaSenderList
        :rtype: twilio.rest.messaging.v1.service.AlphaSenderList
        """
        return self._proxy.alpha_senders
    
    @property
    def phone_numbers(self):
        """
        Access the phone_numbers

        :returns: twilio.rest.messaging.v1.service.PhoneNumberList
        :rtype: twilio.rest.messaging.v1.service.PhoneNumberList
        """
        return self._proxy.phone_numbers
    
    @property
    def short_codes(self):
        """
        Access the short_codes

        :returns: twilio.rest.messaging.v1.service.ShortCodeList
        :rtype: twilio.rest.messaging.v1.service.ShortCodeList
        """
        return self._proxy.short_codes
    
    @property
    def us_app_to_person(self):
        """
        Access the us_app_to_person

        :returns: twilio.rest.messaging.v1.service.UsAppToPersonList
        :rtype: twilio.rest.messaging.v1.service.UsAppToPersonList
        """
        return self._proxy.us_app_to_person
    
    @property
    def us_app_to_person_usecases(self):
        """
        Access the us_app_to_person_usecases

        :returns: twilio.rest.messaging.v1.service.UsAppToPersonUsecaseList
        :rtype: twilio.rest.messaging.v1.service.UsAppToPersonUsecaseList
        """
        return self._proxy.us_app_to_person_usecases
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.ServiceInstance {}>'.format(context)

class ServiceContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Service resource to update.

        :returns: twilio.rest.messaging.v1.service.ServiceContext
        :rtype: twilio.rest.messaging.v1.service.ServiceContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Services/{sid}'.format(**self._solution)
        
        self._alpha_senders = None
        self._phone_numbers = None
        self._short_codes = None
        self._us_app_to_person = None
        self._us_app_to_person_usecases = None
    
    def delete(self):
        """
        Deletes the ServiceInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, inbound_request_url=values.unset, inbound_method=values.unset, fallback_url=values.unset, fallback_method=values.unset, status_callback=values.unset, sticky_sender=values.unset, mms_converter=values.unset, smart_encoding=values.unset, scan_message_content=values.unset, fallback_to_long_code=values.unset, area_code_geomatch=values.unset, validity_period=values.unset, synchronous_validation=values.unset, usecase=values.unset, use_inbound_webhook_on_number=values.unset):
        """
        Update the ServiceInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str inbound_request_url: The URL we call using `inbound_method` when a message is received by any phone number or short code in the Service. When this property is `null`, receiving inbound messages is disabled. All messages sent to the Twilio phone number or short code will not be logged and received on the Account. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `inbound_request_url` defined for the Messaging Service.
        :params str inbound_method: The HTTP method we should use to call `inbound_request_url`. Can be `GET` or `POST` and the default is `POST`.
        :params str fallback_url: The URL that we call using `fallback_method` if an error occurs while retrieving or executing the TwiML from the Inbound Request URL. If the `use_inbound_webhook_on_number` field is enabled then the webhook url defined on the phone number will override the `fallback_url` defined for the Messaging Service.
        :params str fallback_method: The HTTP method we should use to call `fallback_url`. Can be: `GET` or `POST`.
        :params str status_callback: The URL we should call to [pass status updates](https://www.twilio.com/docs/sms/api/message-resource#message-status-values) about message delivery.
        :params bool sticky_sender: Whether to enable [Sticky Sender](https://www.twilio.com/docs/sms/services#sticky-sender) on the Service instance.
        :params bool mms_converter: Whether to enable the [MMS Converter](https://www.twilio.com/docs/sms/services#mms-converter) for messages sent through the Service instance.
        :params bool smart_encoding: Whether to enable [Smart Encoding](https://www.twilio.com/docs/sms/services#smart-encoding) for messages sent through the Service instance.
        :params ServiceScanMessageContent scan_message_content: 
        :params bool fallback_to_long_code: Whether to enable [Fallback to Long Code](https://www.twilio.com/docs/sms/services#fallback-to-long-code) for messages sent through the Service instance.
        :params bool area_code_geomatch: Whether to enable [Area Code Geomatch](https://www.twilio.com/docs/sms/services#area-code-geomatch) on the Service Instance.
        :params int validity_period: How long, in seconds, messages sent from the Service are valid. Can be an integer from `1` to `14,400`.
        :params bool synchronous_validation: Reserved.
        :params str usecase: A string that describes the scenario in which the Messaging Service will be used. Examples: [notification, marketing, verification, poll ..]
        :params bool use_inbound_webhook_on_number: A boolean value that indicates either the webhook url configured on the phone number will be used or `inbound_request_url`/`fallback_url` url will be called when a message is received from the phone number. If this field is enabled then the webhook url defined on the phone number will override the `inbound_request_url`/`fallback_url` defined for the Messaging Service.

        :returns: The updated ServiceInstance
        :rtype: twilio.rest.messaging.v1.service.ServiceInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'InboundRequestUrl': inbound_request_url,
            'InboundMethod': inbound_method,
            'FallbackUrl': fallback_url,
            'FallbackMethod': fallback_method,
            'StatusCallback': status_callback,
            'StickySender': sticky_sender,
            'MmsConverter': mms_converter,
            'SmartEncoding': smart_encoding,
            'ScanMessageContent': scan_message_content,
            'FallbackToLongCode': fallback_to_long_code,
            'AreaCodeGeomatch': area_code_geomatch,
            'ValidityPeriod': validity_period,
            'SynchronousValidation': synchronous_validation,
            'Usecase': usecase,
            'UseInboundWebhookOnNumber': use_inbound_webhook_on_number,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def alpha_senders(self):
        """
        Access the alpha_senders

        :returns: twilio.rest.messaging.v1.service.AlphaSenderList
        :rtype: twilio.rest.messaging.v1.service.AlphaSenderList
        """
        if self._alpha_senders is None:
            self._alpha_senders = AlphaSenderList(self._version, self._solution['sid'],
            )
        return self._alpha_senders
    
    @property
    def phone_numbers(self):
        """
        Access the phone_numbers

        :returns: twilio.rest.messaging.v1.service.PhoneNumberList
        :rtype: twilio.rest.messaging.v1.service.PhoneNumberList
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(self._version, self._solution['sid'],
            )
        return self._phone_numbers
    
    @property
    def short_codes(self):
        """
        Access the short_codes

        :returns: twilio.rest.messaging.v1.service.ShortCodeList
        :rtype: twilio.rest.messaging.v1.service.ShortCodeList
        """
        if self._short_codes is None:
            self._short_codes = ShortCodeList(self._version, self._solution['sid'],
            )
        return self._short_codes
    
    @property
    def us_app_to_person(self):
        """
        Access the us_app_to_person

        :returns: twilio.rest.messaging.v1.service.UsAppToPersonList
        :rtype: twilio.rest.messaging.v1.service.UsAppToPersonList
        """
        if self._us_app_to_person is None:
            self._us_app_to_person = UsAppToPersonList(self._version, self._solution['sid'],
            )
        return self._us_app_to_person
    
    @property
    def us_app_to_person_usecases(self):
        """
        Access the us_app_to_person_usecases

        :returns: twilio.rest.messaging.v1.service.UsAppToPersonUsecaseList
        :rtype: twilio.rest.messaging.v1.service.UsAppToPersonUsecaseList
        """
        if self._us_app_to_person_usecases is None:
            self._us_app_to_person_usecases = UsAppToPersonUsecaseList(self._version, self._solution['sid'],
            )
        return self._us_app_to_person_usecases
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.ServiceContext {}>'.format(context)


