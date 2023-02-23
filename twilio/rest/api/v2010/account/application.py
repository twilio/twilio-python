"""
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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ApplicationList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the ApplicationList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to read.
        
        :returns: twilio.rest.api.v2010.account.application.ApplicationList
        :rtype: twilio.rest.api.v2010.account.application.ApplicationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/Applications.json'.format(**self._solution)
        
        
    
    
    
    
    def create(self, api_version=values.unset, voice_url=values.unset, voice_method=values.unset, voice_fallback_url=values.unset, voice_fallback_method=values.unset, status_callback=values.unset, status_callback_method=values.unset, voice_caller_id_lookup=values.unset, sms_url=values.unset, sms_method=values.unset, sms_fallback_url=values.unset, sms_fallback_method=values.unset, sms_status_callback=values.unset, message_status_callback=values.unset, friendly_name=values.unset, public_application_connect_enabled=values.unset):
        """
        Create the ApplicationInstance

        :param str api_version: The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is the account's default API version.
        :param str voice_url: The URL we should call when the phone number assigned to this application receives a call.
        :param str voice_method: The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
        :param str voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
        :param str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application.
        :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.
        :param bool voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.
        :param str sms_url: The URL we should call when the phone number receives an incoming SMS message.
        :param str sms_method: The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.
        :param str sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.
        :param str sms_fallback_method: The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.
        :param str sms_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application.
        :param str message_status_callback: The URL we should call using a POST method to send message status information to your application.
        :param str friendly_name: A descriptive string that you create to describe the new application. It can be up to 64 characters long.
        :param bool public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.
        
        :returns: The created ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationInstance
        """
        data = values.of({ 
            'ApiVersion': api_version,
            'VoiceUrl': voice_url,
            'VoiceMethod': voice_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'SmsUrl': sms_url,
            'SmsMethod': sms_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsStatusCallback': sms_status_callback,
            'MessageStatusCallback': message_status_callback,
            'FriendlyName': friendly_name,
            'PublicApplicationConnectEnabled': public_application_connect_enabled,
        })
        )
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ApplicationInstance(self._version, payload, account_sid=self._solution['account_sid'])
    
    
    def stream(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Streams ApplicationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str friendly_name: The string that identifies the Application resources to read.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.application.ApplicationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, friendly_name=values.unset, limit=None, page_size=None):
        """
        Lists ApplicationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str friendly_name: The string that identifies the Application resources to read.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.application.ApplicationInstance]
        """
        return list(self.stream(
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, friendly_name=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ApplicationInstance records from the API.
        Request is executed immediately
        
        :param str friendly_name: The string that identifies the Application resources to read.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationPage
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ApplicationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ApplicationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ApplicationPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ApplicationContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Application resource to update.
        
        :returns: twilio.rest.api.v2010.account.application.ApplicationContext
        :rtype: twilio.rest.api.v2010.account.application.ApplicationContext
        """
        return ApplicationContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ApplicationContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Application resource to update.
        
        :returns: twilio.rest.api.v2010.account.application.ApplicationContext
        :rtype: twilio.rest.api.v2010.account.application.ApplicationContext
        """
        return ApplicationContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ApplicationList>'










class ApplicationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ApplicationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.application.ApplicationPage
        :rtype: twilio.rest.api.v2010.account.application.ApplicationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ApplicationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.application.ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationInstance
        """
        return ApplicationInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ApplicationPage>'




class ApplicationContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the ApplicationContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to update.:param sid: The Twilio-provided string that uniquely identifies the Application resource to update.

        :returns: twilio.rest.api.v2010.account.application.ApplicationContext
        :rtype: twilio.rest.api.v2010.account.application.ApplicationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Applications/{sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the ApplicationInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ApplicationInstance
        

        :returns: The fetched ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ApplicationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, api_version=values.unset, voice_url=values.unset, voice_method=values.unset, voice_fallback_url=values.unset, voice_fallback_method=values.unset, status_callback=values.unset, status_callback_method=values.unset, voice_caller_id_lookup=values.unset, sms_url=values.unset, sms_method=values.unset, sms_fallback_url=values.unset, sms_fallback_method=values.unset, sms_status_callback=values.unset, message_status_callback=values.unset, public_application_connect_enabled=values.unset):
        """
        Update the ApplicationInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str api_version: The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is your account's default API version.
        :params str voice_url: The URL we should call when the phone number assigned to this application receives a call.
        :params str voice_method: The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
        :params str voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
        :params str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :params str status_callback: The URL we should call using the `status_callback_method` to send status information to your application.
        :params str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.
        :params bool voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.
        :params str sms_url: The URL we should call when the phone number receives an incoming SMS message.
        :params str sms_method: The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.
        :params str sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.
        :params str sms_fallback_method: The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.
        :params str sms_status_callback: Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility.
        :params str message_status_callback: The URL we should call using a POST method to send message status information to your application.
        :params bool public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.

        :returns: The updated ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'ApiVersion': api_version,
            'VoiceUrl': voice_url,
            'VoiceMethod': voice_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceFallbackMethod': voice_fallback_method,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'SmsUrl': sms_url,
            'SmsMethod': sms_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsStatusCallback': sms_status_callback,
            'MessageStatusCallback': message_status_callback,
            'PublicApplicationConnectEnabled': public_application_connect_enabled,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ApplicationInstance(
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
        return '<Twilio.Api.V2010.ApplicationContext {}>'.format(context)

class ApplicationInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the ApplicationInstance
        :returns: twilio.rest.api.v2010.account.application.ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'message_status_callback': payload.get('message_status_callback'),
            'sid': payload.get('sid'),
            'sms_fallback_method': payload.get('sms_fallback_method'),
            'sms_fallback_url': payload.get('sms_fallback_url'),
            'sms_method': payload.get('sms_method'),
            'sms_status_callback': payload.get('sms_status_callback'),
            'sms_url': payload.get('sms_url'),
            'status_callback': payload.get('status_callback'),
            'status_callback_method': payload.get('status_callback_method'),
            'uri': payload.get('uri'),
            'voice_caller_id_lookup': payload.get('voice_caller_id_lookup'),
            'voice_fallback_method': payload.get('voice_fallback_method'),
            'voice_fallback_url': payload.get('voice_fallback_url'),
            'voice_method': payload.get('voice_method'),
            'voice_url': payload.get('voice_url'),
            'public_application_connect_enabled': payload.get('public_application_connect_enabled'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ApplicationContext for this ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationContext
        """
        if self._context is None:
            self._context = ApplicationContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def api_version(self):
        """
        :returns: The API version used to start a new TwiML session.
        :rtype: str
        """
        return self._properties['api_version']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def message_status_callback(self):
        """
        :returns: The URL we call using a POST method to send message status information to your application.
        :rtype: str
        """
        return self._properties['message_status_callback']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Application resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def sms_fallback_method(self):
        """
        :returns: The HTTP method we use to call `sms_fallback_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['sms_fallback_method']
    
    @property
    def sms_fallback_url(self):
        """
        :returns: The URL that we call when an error occurs while retrieving or executing the TwiML from `sms_url`.
        :rtype: str
        """
        return self._properties['sms_fallback_url']
    
    @property
    def sms_method(self):
        """
        :returns: The HTTP method we use to call `sms_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['sms_method']
    
    @property
    def sms_status_callback(self):
        """
        :returns: The URL we call using a POST method to send status information to your application about SMS messages that refer to the application.
        :rtype: str
        """
        return self._properties['sms_status_callback']
    
    @property
    def sms_url(self):
        """
        :returns: The URL we call when the phone number receives an incoming SMS message.
        :rtype: str
        """
        return self._properties['sms_url']
    
    @property
    def status_callback(self):
        """
        :returns: The URL we call using the `status_callback_method` to send status information to your application.
        :rtype: str
        """
        return self._properties['status_callback']
    
    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we use to call `status_callback`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['status_callback_method']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    @property
    def voice_caller_id_lookup(self):
        """
        :returns: Whether we look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']
    
    @property
    def voice_fallback_method(self):
        """
        :returns: The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['voice_fallback_method']
    
    @property
    def voice_fallback_url(self):
        """
        :returns: The URL that we call when an error occurs retrieving or executing the TwiML requested by `url`.
        :rtype: str
        """
        return self._properties['voice_fallback_url']
    
    @property
    def voice_method(self):
        """
        :returns: The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['voice_method']
    
    @property
    def voice_url(self):
        """
        :returns: The URL we call when the phone number assigned to this application receives a call.
        :rtype: str
        """
        return self._properties['voice_url']
    
    @property
    def public_application_connect_enabled(self):
        """
        :returns: Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.
        :rtype: bool
        """
        return self._properties['public_application_connect_enabled']
    
    def delete(self):
        """
        Deletes the ApplicationInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ApplicationInstance
        

        :returns: The fetched ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, api_version=values.unset, voice_url=values.unset, voice_method=values.unset, voice_fallback_url=values.unset, voice_fallback_method=values.unset, status_callback=values.unset, status_callback_method=values.unset, voice_caller_id_lookup=values.unset, sms_url=values.unset, sms_method=values.unset, sms_fallback_url=values.unset, sms_fallback_method=values.unset, sms_status_callback=values.unset, message_status_callback=values.unset, public_application_connect_enabled=values.unset):
        """
        Update the ApplicationInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str api_version: The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is your account's default API version.
        :params str voice_url: The URL we should call when the phone number assigned to this application receives a call.
        :params str voice_method: The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
        :params str voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
        :params str voice_fallback_method: The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
        :params str status_callback: The URL we should call using the `status_callback_method` to send status information to your application.
        :params str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.
        :params bool voice_caller_id_lookup: Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.
        :params str sms_url: The URL we should call when the phone number receives an incoming SMS message.
        :params str sms_method: The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.
        :params str sms_fallback_url: The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.
        :params str sms_fallback_method: The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.
        :params str sms_status_callback: Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility.
        :params str message_status_callback: The URL we should call using a POST method to send message status information to your application.
        :params bool public_application_connect_enabled: Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.

        :returns: The updated ApplicationInstance
        :rtype: twilio.rest.api.v2010.account.application.ApplicationInstance
        """
        return self._proxy.update(friendly_name=friendly_name, api_version=api_version, voice_url=voice_url, voice_method=voice_method, voice_fallback_url=voice_fallback_url, voice_fallback_method=voice_fallback_method, status_callback=status_callback, status_callback_method=status_callback_method, voice_caller_id_lookup=voice_caller_id_lookup, sms_url=sms_url, sms_method=sms_method, sms_fallback_url=sms_fallback_url, sms_fallback_method=sms_fallback_method, sms_status_callback=sms_status_callback, message_status_callback=message_status_callback, public_application_connect_enabled=public_application_connect_enabled, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ApplicationInstance {}>'.format(context)


