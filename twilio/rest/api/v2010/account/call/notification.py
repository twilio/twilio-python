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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class NotificationList(ListResource):

    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resources to read.
        :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resources to read.
        
        :returns: twilio.rest.api.v2010.account.call.notification.NotificationList
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid,  }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json'.format(**self._solution)
        
        
    
    def fetch(self):
        """
        Fetch the NotificationInstance

        :returns: The fetched NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return NotificationInstance(self._version, payload, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'])
    
    
    def stream(self, log=values.unset, message_date=values.unset, message_date_before=values.unset, message_date_after=values.unset, limit=None, page_size=None):
        """
        Streams NotificationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param date message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.notification.NotificationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            log=log,
            message_date=message_date,
            message_date_before=message_date_before,
            message_date_after=message_date_after,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, log=values.unset, message_date=values.unset, message_date_before=values.unset, message_date_after=values.unset, limit=None, page_size=None):
        """
        Lists NotificationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param date message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.call.notification.NotificationInstance]
        """
        return list(self.stream(
            log=log,
            message_date=message_date,
            message_date_before=message_date_before,
            message_date_after=message_date_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, log=values.unset, message_date=values.unset, message_date_before=values.unset, message_date_after=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of NotificationInstance records from the API.
        Request is executed immediately
        
        :param int log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param date message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        data = values.of({ 
            'Log': log,
            'MessageDate': serialize.iso8601_date(message_date),
            'MessageDate<': serialize.iso8601_date(message_date_before),
            'MessageDate>': serialize.iso8601_date(message_date_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return NotificationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of NotificationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return NotificationPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a NotificationContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        return NotificationContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a NotificationContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        return NotificationContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationList>'




class NotificationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the NotificationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationPage
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NotificationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        return NotificationInstance(self._version, payload, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.NotificationPage>'




class NotificationInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, call_sid: str, sid: str=None):
        """
        Initialize the NotificationInstance
        :returns: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'call_sid': payload.get('call_sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'error_code': payload.get('error_code'),
            'log': payload.get('log'),
            'message_date': deserialize.rfc2822_datetime(payload.get('message_date')),
            'message_text': payload.get('message_text'),
            'more_info': payload.get('more_info'),
            'request_method': payload.get('request_method'),
            'request_url': payload.get('request_url'),
            'request_variables': payload.get('request_variables'),
            'response_body': payload.get('response_body'),
            'response_headers': payload.get('response_headers'),
            'sid': payload.get('sid'),
            'uri': payload.get('uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NotificationContext for this NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        if self._context is None:
            self._context = NotificationContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def api_version(self):
        """
        :returns: The API version used to create the Call Notification resource.
        :rtype: str
        """
        return self._properties['api_version']
    
    @property
    def call_sid(self):
        """
        :returns: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Call Notification resource is associated with.
        :rtype: str
        """
        return self._properties['call_sid']
    
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
    def error_code(self):
        """
        :returns: A unique error code for the error condition that is described in our [Error Dictionary](https://www.twilio.com/docs/api/errors).
        :rtype: str
        """
        return self._properties['error_code']
    
    @property
    def log(self):
        """
        :returns: An integer log level that corresponds to the type of notification: `0` is ERROR, `1` is WARNING.
        :rtype: str
        """
        return self._properties['log']
    
    @property
    def message_date(self):
        """
        :returns: The date the notification was actually generated in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. Message buffering can cause this value to differ from `date_created`.
        :rtype: datetime
        """
        return self._properties['message_date']
    
    @property
    def message_text(self):
        """
        :returns: The text of the notification.
        :rtype: str
        """
        return self._properties['message_text']
    
    @property
    def more_info(self):
        """
        :returns: The URL for more information about the error condition. This value is a page in our [Error Dictionary](https://www.twilio.com/docs/api/errors).
        :rtype: str
        """
        return self._properties['more_info']
    
    @property
    def request_method(self):
        """
        :returns: The HTTP method used to generate the notification. If the notification was generated during a phone call, this is the HTTP Method used to request the resource on your server. If the notification was generated by your use of our REST API, this is the HTTP method used to call the resource on our servers.
        :rtype: str
        """
        return self._properties['request_method']
    
    @property
    def request_url(self):
        """
        :returns: The URL of the resource that generated the notification. If the notification was generated during a phone call, this is the URL of the resource on your server that caused the notification. If the notification was generated by your use of our REST API, this is the URL of the resource you called.
        :rtype: str
        """
        return self._properties['request_url']
    
    @property
    def request_variables(self):
        """
        :returns: The HTTP GET or POST variables we sent to your server. However, if the notification was generated by our REST API, this contains the HTTP POST or PUT variables you sent to our API.
        :rtype: str
        """
        return self._properties['request_variables']
    
    @property
    def response_body(self):
        """
        :returns: The HTTP body returned by your server.
        :rtype: str
        """
        return self._properties['response_body']
    
    @property
    def response_headers(self):
        """
        :returns: The HTTP headers returned by your server.
        :rtype: str
        """
        return self._properties['response_headers']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Call Notification resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    def fetch(self):
        """
        Fetch the NotificationInstance
        

        :returns: The fetched NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.NotificationInstance {}>'.format(context)

class NotificationContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, call_sid: str, sid: str):
        """
        Initialize the NotificationContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource to fetch.:param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resource to fetch.:param sid: The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.

        :returns: twilio.rest.api.v2010.account.call.notification.NotificationContext
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid}.json'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the NotificationInstance
        

        :returns: The fetched NotificationInstance
        :rtype: twilio.rest.api.v2010.account.call.notification.NotificationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return NotificationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.NotificationContext {}>'.format(context)


