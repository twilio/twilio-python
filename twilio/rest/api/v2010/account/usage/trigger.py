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


class TriggerList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the TriggerList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to read.
        
        :returns: twilio.rest.api.v2010.account.usage.trigger.TriggerList
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/Usage/Triggers.json'.format(**self._solution)
        
        
    
    
    
    
    def create(self, callback_url, trigger_value, usage_category, callback_method=values.unset, friendly_name=values.unset, recurring=values.unset, trigger_by=values.unset):
        """
        Create the TriggerInstance

        :param str callback_url: The URL we should call using `callback_method` when the trigger fires.
        :param str trigger_value: The usage value at which the trigger should fire.  For convenience, you can use an offset value such as `+30` to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a `+` as `%2B`.
        :param UsageTriggerUsageCategory usage_category: 
        :param str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.
        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param UsageTriggerRecurring recurring: 
        :param UsageTriggerTriggerField trigger_by: 
        
        :returns: The created TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        """
        data = values.of({ 
            'CallbackUrl': callback_url,
            'TriggerValue': trigger_value,
            'UsageCategory': usage_category,
            'CallbackMethod': callback_method,
            'FriendlyName': friendly_name,
            'Recurring': recurring,
            'TriggerBy': trigger_by,
        })
        )
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return TriggerInstance(self._version, payload, account_sid=self._solution['account_sid'])
    
    
    def stream(self, recurring=values.unset, trigger_by=values.unset, usage_category=values.unset, limit=None, page_size=None):
        """
        Streams TriggerInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param UsageTriggerRecurring recurring: The frequency of recurring UsageTriggers to read. Can be: `daily`, `monthly`, or `yearly` to read recurring UsageTriggers. An empty value or a value of `alltime` reads non-recurring UsageTriggers.
        :param UsageTriggerTriggerField trigger_by: The trigger field of the UsageTriggers to read.  Can be: `count`, `usage`, or `price` as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price).
        :param UsageTriggerUsageCategory usage_category: The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories).
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.trigger.TriggerInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            recurring=recurring,
            trigger_by=trigger_by,
            usage_category=usage_category,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, recurring=values.unset, trigger_by=values.unset, usage_category=values.unset, limit=None, page_size=None):
        """
        Lists TriggerInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param UsageTriggerRecurring recurring: The frequency of recurring UsageTriggers to read. Can be: `daily`, `monthly`, or `yearly` to read recurring UsageTriggers. An empty value or a value of `alltime` reads non-recurring UsageTriggers.
        :param UsageTriggerTriggerField trigger_by: The trigger field of the UsageTriggers to read.  Can be: `count`, `usage`, or `price` as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price).
        :param UsageTriggerUsageCategory usage_category: The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories).
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.usage.trigger.TriggerInstance]
        """
        return list(self.stream(
            recurring=recurring,
            trigger_by=trigger_by,
            usage_category=usage_category,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, recurring=values.unset, trigger_by=values.unset, usage_category=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TriggerInstance records from the API.
        Request is executed immediately
        
        :param UsageTriggerRecurring recurring: The frequency of recurring UsageTriggers to read. Can be: `daily`, `monthly`, or `yearly` to read recurring UsageTriggers. An empty value or a value of `alltime` reads non-recurring UsageTriggers.
        :param UsageTriggerTriggerField trigger_by: The trigger field of the UsageTriggers to read.  Can be: `count`, `usage`, or `price` as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price).
        :param UsageTriggerUsageCategory usage_category: The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories).
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerPage
        """
        data = values.of({ 
            'Recurring': recurring,
            'TriggerBy': trigger_by,
            'UsageCategory': usage_category,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return TriggerPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TriggerInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return TriggerPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a TriggerContext
        
        :param sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
        
        :returns: twilio.rest.api.v2010.account.usage.trigger.TriggerContext
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerContext
        """
        return TriggerContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a TriggerContext
        
        :param sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
        
        :returns: twilio.rest.api.v2010.account.usage.trigger.TriggerContext
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerContext
        """
        return TriggerContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TriggerList>'










class TriggerPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TriggerPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.usage.trigger.TriggerPage
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TriggerInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        """
        return TriggerInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TriggerPage>'




class TriggerContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the TriggerContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to update.:param sid: The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.

        :returns: twilio.rest.api.v2010.account.usage.trigger.TriggerContext
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Usage/Triggers/{sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the TriggerInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the TriggerInstance
        

        :returns: The fetched TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TriggerInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, callback_method=values.unset, callback_url=values.unset, friendly_name=values.unset):
        """
        Update the TriggerInstance
        
        :params str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.
        :params str callback_url: The URL we should call using `callback_method` when the trigger fires.
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The updated TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        """
        data = values.of({ 
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return TriggerInstance(
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
        return '<Twilio.Api.V2010.TriggerContext {}>'.format(context)

class TriggerInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the TriggerInstance
        :returns: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'callback_method': payload.get('callback_method'),
            'callback_url': payload.get('callback_url'),
            'current_value': payload.get('current_value'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_fired': deserialize.rfc2822_datetime(payload.get('date_fired')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'recurring': payload.get('recurring'),
            'sid': payload.get('sid'),
            'trigger_by': payload.get('trigger_by'),
            'trigger_value': payload.get('trigger_value'),
            'uri': payload.get('uri'),
            'usage_category': payload.get('usage_category'),
            'usage_record_uri': payload.get('usage_record_uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TriggerContext for this TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerContext
        """
        if self._context is None:
            self._context = TriggerContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the trigger monitors.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def api_version(self):
        """
        :returns: The API version used to create the resource.
        :rtype: str
        """
        return self._properties['api_version']
    
    @property
    def callback_method(self):
        """
        :returns: The HTTP method we use to call `callback_url`. Can be: `GET` or `POST`.
        :rtype: str
        """
        return self._properties['callback_method']
    
    @property
    def callback_url(self):
        """
        :returns: The URL we call using the `callback_method` when the trigger fires.
        :rtype: str
        """
        return self._properties['callback_url']
    
    @property
    def current_value(self):
        """
        :returns: The current value of the field the trigger is watching.
        :rtype: str
        """
        return self._properties['current_value']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_fired(self):
        """
        :returns: The date and time in GMT that the trigger was last fired specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_fired']
    
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
        :returns: The string that you assigned to describe the trigger.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def recurring(self):
        """
        :returns: 
        :rtype: UsageTriggerRecurring
        """
        return self._properties['recurring']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the UsageTrigger resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def trigger_by(self):
        """
        :returns: 
        :rtype: UsageTriggerTriggerField
        """
        return self._properties['trigger_by']
    
    @property
    def trigger_value(self):
        """
        :returns: The value at which the trigger will fire.  Must be a positive, numeric value.
        :rtype: str
        """
        return self._properties['trigger_value']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    @property
    def usage_category(self):
        """
        :returns: 
        :rtype: UsageTriggerUsageCategory
        """
        return self._properties['usage_category']
    
    @property
    def usage_record_uri(self):
        """
        :returns: The URI of the [UsageRecord](https://www.twilio.com/docs/usage/api/usage-record) resource this trigger watches, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['usage_record_uri']
    
    def delete(self):
        """
        Deletes the TriggerInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the TriggerInstance
        

        :returns: The fetched TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        """
        return self._proxy.fetch()
    
    def update(self, callback_method=values.unset, callback_url=values.unset, friendly_name=values.unset):
        """
        Update the TriggerInstance
        
        :params str callback_method: The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.
        :params str callback_url: The URL we should call using `callback_method` when the trigger fires.
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The updated TriggerInstance
        :rtype: twilio.rest.api.v2010.account.usage.trigger.TriggerInstance
        """
        return self._proxy.update(callback_method=callback_method, callback_url=callback_url, friendly_name=friendly_name, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.TriggerInstance {}>'.format(context)


