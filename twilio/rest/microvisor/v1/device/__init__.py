"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
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
from twilio.rest.microvisor.v1.device.device_config import DeviceConfigList
from twilio.rest.microvisor.v1.device.device_secret import DeviceSecretList


class DeviceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the DeviceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.microvisor.v1.device.DeviceList
        :rtype: twilio.rest.microvisor.v1.device.DeviceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Devices'.format(**self._solution)
        
        
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams DeviceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.microvisor.v1.device.DeviceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DeviceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.microvisor.v1.device.DeviceInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DeviceInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DevicePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return DevicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeviceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DevicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return DevicePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a DeviceContext
        
        :param sid: A 34-character string that uniquely identifies this Device.
        
        :returns: twilio.rest.microvisor.v1.device.DeviceContext
        :rtype: twilio.rest.microvisor.v1.device.DeviceContext
        """
        return DeviceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a DeviceContext
        
        :param sid: A 34-character string that uniquely identifies this Device.
        
        :returns: twilio.rest.microvisor.v1.device.DeviceContext
        :rtype: twilio.rest.microvisor.v1.device.DeviceContext
        """
        return DeviceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.DeviceList>'






class DevicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DevicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.microvisor.v1.device.DevicePage
        :rtype: twilio.rest.microvisor.v1.device.DevicePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeviceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.microvisor.v1.device.DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DeviceInstance
        """
        return DeviceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.DevicePage>'




class DeviceInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the DeviceInstance
        :returns: twilio.rest.microvisor.v1.device.DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DeviceInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'account_sid': payload.get('account_sid'),
            'app': payload.get('app'),
            'logging': payload.get('logging'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DeviceContext for this DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DeviceContext
        """
        if self._context is None:
            self._context = DeviceContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34-character string that uniquely identifies this Device.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def unique_name(self):
        """
        :returns: A developer-defined string that uniquely identifies the Device. This value must be unique for all Devices on this Account. The `unique_name` value may be used as an alternative to the `sid` in the URL path to address the resource.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def app(self):
        """
        :returns: Information about the target App and the App reported by this Device. Contains the properties `target_sid`, `date_targeted`, `update_status` (one of `up-to-date`, `pending` and `error`), `update_error_code`, `reported_sid` and `date_reported`.
        :rtype: dict
        """
        return self._properties['app']
    
    @property
    def logging(self):
        """
        :returns: Object specifying whether application logging is enabled for this Device. Contains the properties `enabled` and `date_expires`.
        :rtype: dict
        """
        return self._properties['logging']
    
    @property
    def date_created(self):
        """
        :returns: The date that this Device was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this Device was last updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
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
    
    def fetch(self):
        """
        Fetch the DeviceInstance
        

        :returns: The fetched DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DeviceInstance
        """
        return self._proxy.fetch()
    
    def update(self, unique_name=values.unset, target_app=values.unset, logging_enabled=values.unset):
        """
        Update the DeviceInstance
        
        :params str unique_name: A unique and addressable name to be assigned to this Device by the developer. It may be used in place of the Device SID.
        :params str target_app: The SID or unique name of the App to be targeted to the Device.
        :params bool logging_enabled: A Boolean flag specifying whether to enable application logging. Logs will be enabled or extended for 24 hours.

        :returns: The updated DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DeviceInstance
        """
        return self._proxy.update(unique_name=unique_name, target_app=target_app, logging_enabled=logging_enabled, )
    
    @property
    def device_configs(self):
        """
        Access the device_configs

        :returns: twilio.rest.microvisor.v1.device.DeviceConfigList
        :rtype: twilio.rest.microvisor.v1.device.DeviceConfigList
        """
        return self._proxy.device_configs
    
    @property
    def device_secrets(self):
        """
        Access the device_secrets

        :returns: twilio.rest.microvisor.v1.device.DeviceSecretList
        :rtype: twilio.rest.microvisor.v1.device.DeviceSecretList
        """
        return self._proxy.device_secrets
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.DeviceInstance {}>'.format(context)

class DeviceContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the DeviceContext

        :param Version version: Version that contains the resource
        :param sid: A 34-character string that uniquely identifies this Device.

        :returns: twilio.rest.microvisor.v1.device.DeviceContext
        :rtype: twilio.rest.microvisor.v1.device.DeviceContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Devices/{sid}'.format(**self._solution)
        
        self._device_configs = None
        self._device_secrets = None
    
    def fetch(self):
        """
        Fetch the DeviceInstance
        

        :returns: The fetched DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DeviceInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DeviceInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, unique_name=values.unset, target_app=values.unset, logging_enabled=values.unset):
        """
        Update the DeviceInstance
        
        :params str unique_name: A unique and addressable name to be assigned to this Device by the developer. It may be used in place of the Device SID.
        :params str target_app: The SID or unique name of the App to be targeted to the Device.
        :params bool logging_enabled: A Boolean flag specifying whether to enable application logging. Logs will be enabled or extended for 24 hours.

        :returns: The updated DeviceInstance
        :rtype: twilio.rest.microvisor.v1.device.DeviceInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'TargetApp': target_app,
            'LoggingEnabled': logging_enabled,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return DeviceInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def device_configs(self):
        """
        Access the device_configs

        :returns: twilio.rest.microvisor.v1.device.DeviceConfigList
        :rtype: twilio.rest.microvisor.v1.device.DeviceConfigList
        """
        if self._device_configs is None:
            self._device_configs = DeviceConfigList(self._version, self._solution['sid'],
            )
        return self._device_configs
    
    @property
    def device_secrets(self):
        """
        Access the device_secrets

        :returns: twilio.rest.microvisor.v1.device.DeviceSecretList
        :rtype: twilio.rest.microvisor.v1.device.DeviceSecretList
        """
        if self._device_secrets is None:
            self._device_secrets = DeviceSecretList(self._version, self._solution['sid'],
            )
        return self._device_secrets
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.DeviceContext {}>'.format(context)


