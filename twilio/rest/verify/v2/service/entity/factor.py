"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class FactorList(ListResource):

    def __init__(self, version: Version, service_sid: str, identity: str):
        """
        Initialize the FactorList

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Factors. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        
        :returns: twilio.rest.verify.v2.service.entity.factor.FactorList
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'identity': identity,  }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Factors'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the FactorInstance

        :returns: The fetched FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return FactorInstance(self._version, payload, service_sid=self._solution['service_sid'], identity=self._solution['identity'])
    
    
    def update(self, auth_payload=values.unset, friendly_name=values.unset, config_notification_token=values.unset, config_sdk_version=values.unset, config_time_step=values.unset, config_skew=values.unset, config_code_length=values.unset, config_alg=values.unset, config_notification_platform=values.unset):
        """
        Update the FactorInstance

        :param str auth_payload: The optional payload needed to verify the Factor for the first time. E.g. for a TOTP, the numeric code.
        :param str friendly_name: The new friendly name of this Factor. It can be up to 64 characters.
        :param str config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Required when `factor_type` is `push`. If specified, this value must be between 32 and 255 characters long.
        :param str config_sdk_version: The Verify Push SDK version used to configure the factor
        :param int config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive
        :param int config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive
        :param int config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive
        :param TotpAlgorithms config_alg: 
        :param str config_notification_platform: The transport technology used to generate the Notification Token. Can be `apn`, `fcm` or `none`.  Required when `factor_type` is `push`.
        
        :returns: The created FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        data = values.of({ 
            'AuthPayload': auth_payload,
            'FriendlyName': friendly_name,
            'Config.NotificationToken': config_notification_token,
            'Config.SdkVersion': config_sdk_version,
            'Config.TimeStep': config_time_step,
            'Config.Skew': config_skew,
            'Config.CodeLength': config_code_length,
            'Config.Alg': config_alg,
            'Config.NotificationPlatform': config_notification_platform,
        })
        
        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return FactorInstance(self._version, payload, service_sid=self._solution['service_sid'], identity=self._solution['identity'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams FactorInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v2.service.entity.factor.FactorInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FactorInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.entity.factor.FactorInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FactorInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return FactorPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FactorInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return FactorPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a FactorContext
        
        :param sid: A 34 character string that uniquely identifies this Factor.
        
        :returns: twilio.rest.verify.v2.service.entity.factor.FactorContext
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorContext
        """
        return FactorContext(self._version, service_sid=self._solution['service_sid'], identity=self._solution['identity'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a FactorContext
        
        :param sid: A 34 character string that uniquely identifies this Factor.
        
        :returns: twilio.rest.verify.v2.service.entity.factor.FactorContext
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorContext
        """
        return FactorContext(self._version, service_sid=self._solution['service_sid'], identity=self._solution['identity'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.FactorList>'








class FactorPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FactorPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorPage
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FactorInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        return FactorInstance(self._version, payload, service_sid=self._solution['service_sid'], identity=self._solution['identity'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.FactorPage>'




class FactorInstance(InstanceResource):

    class FactorStatuses(object):
        UNVERIFIED = "unverified"
        VERIFIED = "verified"

    class FactorTypes(object):
        PUSH = "push"
        TOTP = "totp"

    def __init__(self, version, payload, service_sid: str, identity: str, sid: str=None):
        """
        Initialize the FactorInstance
        :returns: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'entity_sid': payload.get('entity_sid'),
            'identity': payload.get('identity'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'status': payload.get('status'),
            'factor_type': payload.get('factor_type'),
            'config': payload.get('config'),
            'metadata': payload.get('metadata'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'identity': identity, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FactorContext for this FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorContext
        """
        if self._context is None:
            self._context = FactorContext(self._version, service_sid=self._solution['service_sid'], identity=self._solution['identity'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this Factor.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The unique SID identifier of the Service.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def entity_sid(self):
        """
        :returns: The unique SID identifier of the Entity.
        :rtype: str
        """
        return self._properties['entity_sid']
    
    @property
    def identity(self):
        """
        :returns: Customer unique identity for the Entity owner of the Factor. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def date_created(self):
        """
        :returns: The date that this Factor was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this Factor was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource, up to 64 characters. For a push factor, this can be the device's name.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: FactorStatuses
        """
        return self._properties['status']
    
    @property
    def factor_type(self):
        """
        :returns: 
        :rtype: FactorTypes
        """
        return self._properties['factor_type']
    
    @property
    def config(self):
        """
        :returns: An object that contains configurations specific to a `factor_type`.
        :rtype: dict
        """
        return self._properties['config']
    
    @property
    def metadata(self):
        """
        :returns: Custom metadata associated with the factor. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\"os\": \"Android\"}`. Can be up to 1024 characters in length.
        :rtype: dict
        """
        return self._properties['metadata']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the FactorInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the FactorInstance
        

        :returns: The fetched FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        return self._proxy.fetch()
    
    def update(self, auth_payload=values.unset, friendly_name=values.unset, config_notification_token=values.unset, config_sdk_version=values.unset, config_time_step=values.unset, config_skew=values.unset, config_code_length=values.unset, config_alg=values.unset, config_notification_platform=values.unset):
        """
        Update the FactorInstance
        
        :params str auth_payload: The optional payload needed to verify the Factor for the first time. E.g. for a TOTP, the numeric code.
        :params str friendly_name: The new friendly name of this Factor. It can be up to 64 characters.
        :params str config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Required when `factor_type` is `push`. If specified, this value must be between 32 and 255 characters long.
        :params str config_sdk_version: The Verify Push SDK version used to configure the factor
        :params int config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive
        :params int config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive
        :params int config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive
        :params TotpAlgorithms config_alg: 
        :params str config_notification_platform: The transport technology used to generate the Notification Token. Can be `apn`, `fcm` or `none`.  Required when `factor_type` is `push`.

        :returns: The updated FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        return self._proxy.update(auth_payload=auth_payload, friendly_name=friendly_name, config_notification_token=config_notification_token, config_sdk_version=config_sdk_version, config_time_step=config_time_step, config_skew=config_skew, config_code_length=config_code_length, config_alg=config_alg, config_notification_platform=config_notification_platform, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.FactorInstance {}>'.format(context)

class FactorContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, identity: str, sid: str):
        """
        Initialize the FactorContext

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.:param identity: Customer unique identity for the Entity owner of the Factor. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.:param sid: A 34 character string that uniquely identifies this Factor.

        :returns: twilio.rest.verify.v2.service.entity.factor.FactorContext
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'identity': identity,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Factors/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the FactorInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the FactorInstance
        

        :returns: The fetched FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, auth_payload=values.unset, friendly_name=values.unset, config_notification_token=values.unset, config_sdk_version=values.unset, config_time_step=values.unset, config_skew=values.unset, config_code_length=values.unset, config_alg=values.unset, config_notification_platform=values.unset):
        """
        Update the FactorInstance
        
        :params str auth_payload: The optional payload needed to verify the Factor for the first time. E.g. for a TOTP, the numeric code.
        :params str friendly_name: The new friendly name of this Factor. It can be up to 64 characters.
        :params str config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Required when `factor_type` is `push`. If specified, this value must be between 32 and 255 characters long.
        :params str config_sdk_version: The Verify Push SDK version used to configure the factor
        :params int config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive
        :params int config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive
        :params int config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive
        :params TotpAlgorithms config_alg: 
        :params str config_notification_platform: The transport technology used to generate the Notification Token. Can be `apn`, `fcm` or `none`.  Required when `factor_type` is `push`.

        :returns: The updated FactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.factor.FactorInstance
        """
        data = values.of({ 
            'AuthPayload': auth_payload,
            'FriendlyName': friendly_name,
            'Config.NotificationToken': config_notification_token,
            'Config.SdkVersion': config_sdk_version,
            'Config.TimeStep': config_time_step,
            'Config.Skew': config_skew,
            'Config.CodeLength': config_code_length,
            'Config.Alg': config_alg,
            'Config.NotificationPlatform': config_notification_platform,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.FactorContext {}>'.format(context)


