r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Monitor
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


class AlertList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AlertList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.monitor.v1.alert.AlertList
        :rtype: twilio.rest.monitor.v1.alert.AlertList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Alerts'.format(**self._solution)
        
        
    
    
    def stream(self, log_level=values.unset, start_date=values.unset, end_date=values.unset, limit=None, page_size=None):
        """
        Streams AlertInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str log_level: Only show alerts for this log-level.  Can be: `error`, `warning`, `notice`, or `debug`.
        :param datetime start_date: Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param datetime end_date: Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.monitor.v1.alert.AlertInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            log_level=log_level,
            start_date=start_date,
            end_date=end_date,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, log_level=values.unset, start_date=values.unset, end_date=values.unset, limit=None, page_size=None):
        """
        Asynchronously streams AlertInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str log_level: Only show alerts for this log-level.  Can be: `error`, `warning`, `notice`, or `debug`.
        :param datetime start_date: Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param datetime end_date: Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.monitor.v1.alert.AlertInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            log_level=log_level,
            start_date=start_date,
            end_date=end_date,
            page_size=limits['page_size']
        )

        return await self._version.stream_async(page, limits['limit'])

    def list(self, log_level=values.unset, start_date=values.unset, end_date=values.unset, limit=None, page_size=None):
        """
        Lists AlertInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str log_level: Only show alerts for this log-level.  Can be: `error`, `warning`, `notice`, or `debug`.
        :param datetime start_date: Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param datetime end_date: Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.monitor.v1.alert.AlertInstance]
        """
        return list(self.stream(
            log_level=log_level,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, log_level=values.unset, start_date=values.unset, end_date=values.unset, limit=None, page_size=None):
        """
        Asynchronously lists AlertInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str log_level: Only show alerts for this log-level.  Can be: `error`, `warning`, `notice`, or `debug`.
        :param datetime start_date: Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param datetime end_date: Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.monitor.v1.alert.AlertInstance]
        """
        return list(await self.stream_async(
            log_level=log_level,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, log_level=values.unset, start_date=values.unset, end_date=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AlertInstance records from the API.
        Request is executed immediately
        
        :param str log_level: Only show alerts for this log-level.  Can be: `error`, `warning`, `notice`, or `debug`.
        :param datetime start_date: Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param datetime end_date: Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertPage
        """
        data = values.of({ 
            'LogLevel': log_level,
            'StartDate': serialize.iso8601_datetime(start_date),
            'EndDate': serialize.iso8601_datetime(end_date),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AlertPage(self._version, response, self._solution)

    async def page_async(self, log_level=values.unset, start_date=values.unset, end_date=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronously retrieve a single page of AlertInstance records from the API.
        Request is executed immediately
        
        :param str log_level: Only show alerts for this log-level.  Can be: `error`, `warning`, `notice`, or `debug`.
        :param datetime start_date: Only include alerts that occurred on or after this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param datetime end_date: Only include alerts that occurred on or before this date and time. Specify the date and time in GMT and format as `YYYY-MM-DD` or `YYYY-MM-DDThh:mm:ssZ`. Queries for alerts older than 30 days are not supported.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertPage
        """
        data = values.of({ 
            'LogLevel': log_level,
            'StartDate': serialize.iso8601_datetime(start_date),
            'EndDate': serialize.iso8601_datetime(end_date),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return AlertPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AlertInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AlertPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of AlertInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return AlertPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AlertContext
        
        :param sid: The SID of the Alert resource to fetch.
        
        :returns: twilio.rest.monitor.v1.alert.AlertContext
        :rtype: twilio.rest.monitor.v1.alert.AlertContext
        """
        return AlertContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a AlertContext
        
        :param sid: The SID of the Alert resource to fetch.
        
        :returns: twilio.rest.monitor.v1.alert.AlertContext
        :rtype: twilio.rest.monitor.v1.alert.AlertContext
        """
        return AlertContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Monitor.V1.AlertList>'




class AlertPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AlertPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.monitor.v1.alert.AlertPage
        :rtype: twilio.rest.monitor.v1.alert.AlertPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AlertInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.monitor.v1.alert.AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertInstance
        """
        return AlertInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Monitor.V1.AlertPage>'




class AlertInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the AlertInstance
        :returns: twilio.rest.monitor.v1.alert.AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'alert_text': payload.get('alert_text'),
            'api_version': payload.get('api_version'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_generated': deserialize.iso8601_datetime(payload.get('date_generated')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'error_code': payload.get('error_code'),
            'log_level': payload.get('log_level'),
            'more_info': payload.get('more_info'),
            'request_method': payload.get('request_method'),
            'request_url': payload.get('request_url'),
            'request_variables': payload.get('request_variables'),
            'resource_sid': payload.get('resource_sid'),
            'response_body': payload.get('response_body'),
            'response_headers': payload.get('response_headers'),
            'sid': payload.get('sid'),
            'url': payload.get('url'),
            'request_headers': payload.get('request_headers'),
            'service_sid': payload.get('service_sid'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AlertContext for this AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertContext
        """
        if self._context is None:
            self._context = AlertContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Alert resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def alert_text(self):
        """
        :returns: The text of the alert.
        :rtype: str
        """
        return self._properties['alert_text']
    
    @property
    def api_version(self):
        """
        :returns: The API version used when the alert was generated.  Can be empty for events that don't have a specific API version.
        :rtype: str
        """
        return self._properties['api_version']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_generated(self):
        """
        :returns: The date and time in GMT when the alert was generated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.  Due to buffering, this can be different than `date_created`.
        :rtype: datetime
        """
        return self._properties['date_generated']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def error_code(self):
        """
        :returns: The error code for the condition that generated the alert. See the [Error Dictionary](https://www.twilio.com/docs/api/errors) for possible causes and solutions to the error.
        :rtype: str
        """
        return self._properties['error_code']
    
    @property
    def log_level(self):
        """
        :returns: The log level.  Can be: `error`, `warning`, `notice`, or `debug`.
        :rtype: str
        """
        return self._properties['log_level']
    
    @property
    def more_info(self):
        """
        :returns: The URL of the page in our [Error Dictionary](https://www.twilio.com/docs/api/errors) with more information about the error condition.
        :rtype: str
        """
        return self._properties['more_info']
    
    @property
    def request_method(self):
        """
        :returns: The method used by the request that generated the alert. If the alert was generated by a request we made to your server, this is the method we used. If the alert was generated by a request from your application to our API, this is the method your application used.
        :rtype: str
        """
        return self._properties['request_method']
    
    @property
    def request_url(self):
        """
        :returns: The URL of the request that generated the alert. If the alert was generated by a request we made to your server, this is the URL on your server that generated the alert. If the alert was generated by a request from your application to our API, this is the URL of the resource requested.
        :rtype: str
        """
        return self._properties['request_url']
    
    @property
    def request_variables(self):
        """
        :returns: The variables passed in the request that generated the alert. This value is only returned when a single Alert resource is fetched.
        :rtype: str
        """
        return self._properties['request_variables']
    
    @property
    def resource_sid(self):
        """
        :returns: The SID of the resource for which the alert was generated.  For instance, if your server failed to respond to an HTTP request during the flow of a particular call, this value would be the SID of the server.  This value is empty if the alert was not generated for a particular resource.
        :rtype: str
        """
        return self._properties['resource_sid']
    
    @property
    def response_body(self):
        """
        :returns: The response body of the request that generated the alert. This value is only returned when a single Alert resource is fetched.
        :rtype: str
        """
        return self._properties['response_body']
    
    @property
    def response_headers(self):
        """
        :returns: The response headers of the request that generated the alert. This value is only returned when a single Alert resource is fetched.
        :rtype: str
        """
        return self._properties['response_headers']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Alert resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Alert resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def request_headers(self):
        """
        :returns: The request headers of the request that generated the alert. This value is only returned when a single Alert resource is fetched.
        :rtype: str
        """
        return self._properties['request_headers']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the service or resource that generated the alert. Can be `null`.
        :rtype: str
        """
        return self._properties['service_sid']
    
    
    def fetch(self):
        """
        Fetch the AlertInstance
        

        :returns: The fetched AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AlertInstance
        

        :returns: The fetched AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Monitor.V1.AlertInstance {}>'.format(context)

class AlertContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the AlertContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Alert resource to fetch.

        :returns: twilio.rest.monitor.v1.alert.AlertContext
        :rtype: twilio.rest.monitor.v1.alert.AlertContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Alerts/{sid}'.format(**self._solution)
        
    
    
    def fetch(self):
        """
        Fetch the AlertInstance
        

        :returns: The fetched AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AlertInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the AlertInstance
        

        :returns: The fetched AlertInstance
        :rtype: twilio.rest.monitor.v1.alert.AlertInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return AlertInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Monitor.V1.AlertContext {}>'.format(context)


