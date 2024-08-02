r"""
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


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class NotificationInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource.
    :ivar api_version: The API version used to create the Call Notification resource.
    :ivar call_sid: The SID of the [Call](https://www.twilio.com/docs/voice/api/call-resource) the Call Notification resource is associated with.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar error_code: A unique error code for the error condition that is described in our [Error Dictionary](https://www.twilio.com/docs/api/errors).
    :ivar log: An integer log level that corresponds to the type of notification: `0` is ERROR, `1` is WARNING.
    :ivar message_date: The date the notification was actually generated in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. Message buffering can cause this value to differ from `date_created`.
    :ivar message_text: The text of the notification.
    :ivar more_info: The URL for more information about the error condition. This value is a page in our [Error Dictionary](https://www.twilio.com/docs/api/errors).
    :ivar request_method: The HTTP method used to generate the notification. If the notification was generated during a phone call, this is the HTTP Method used to request the resource on your server. If the notification was generated by your use of our REST API, this is the HTTP method used to call the resource on our servers.
    :ivar request_url: The URL of the resource that generated the notification. If the notification was generated during a phone call, this is the URL of the resource on your server that caused the notification. If the notification was generated by your use of our REST API, this is the URL of the resource you called.
    :ivar request_variables: The HTTP GET or POST variables we sent to your server. However, if the notification was generated by our REST API, this contains the HTTP POST or PUT variables you sent to our API.
    :ivar response_body: The HTTP body returned by your server.
    :ivar response_headers: The HTTP headers returned by your server.
    :ivar sid: The unique string that that we created to identify the Call Notification resource.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], account_sid: str, call_sid: str, sid: Optional[str] = None):
        super().__init__(version)

        
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.api_version: Optional[str] = payload.get("api_version")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(payload.get("date_created"))
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(payload.get("date_updated"))
        self.error_code: Optional[str] = payload.get("error_code")
        self.log: Optional[str] = payload.get("log")
        self.message_date: Optional[datetime] = deserialize.rfc2822_datetime(payload.get("message_date"))
        self.message_text: Optional[str] = payload.get("message_text")
        self.more_info: Optional[str] = payload.get("more_info")
        self.request_method: Optional[str] = payload.get("request_method")
        self.request_url: Optional[str] = payload.get("request_url")
        self.request_variables: Optional[str] = payload.get("request_variables")
        self.response_body: Optional[str] = payload.get("response_body")
        self.response_headers: Optional[str] = payload.get("response_headers")
        self.sid: Optional[str] = payload.get("sid")
        self.uri: Optional[str] = payload.get("uri")

        
        self._solution = { 
            "account_sid": account_sid,
            "call_sid": call_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[NotificationContext] = None

    @property
    def _proxy(self) -> "NotificationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NotificationContext for this NotificationInstance
        """
        if self._context is None:
            self._context = NotificationContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=self._solution['sid'],)
        return self._context
    
    
    def fetch(self) -> "NotificationInstance":
        """
        Fetch the NotificationInstance
        

        :returns: The fetched NotificationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "NotificationInstance":
        """
        Asynchronous coroutine to fetch the NotificationInstance
        

        :returns: The fetched NotificationInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.NotificationInstance {}>'.format(context)

class NotificationContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, call_sid: str, sid: str):
        """
        Initialize the NotificationContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource to fetch.
        :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'call_sid': call_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications/{sid}.json'.format(**self._solution)
        
    
    
    def fetch(self) -> NotificationInstance:
        """
        Fetch the NotificationInstance
        

        :returns: The fetched NotificationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return NotificationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> NotificationInstance:
        """
        Asynchronous coroutine to fetch the NotificationInstance
        

        :returns: The fetched NotificationInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return NotificationInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            call_sid=self._solution['call_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.NotificationContext {}>'.format(context)





class NotificationPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> NotificationInstance:
        """
        Build an instance of NotificationInstance

        :param payload: Payload response from the API
        """
        return NotificationInstance(self._version, payload, account_sid=self._solution["account_sid"], call_sid=self._solution["call_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.NotificationPage>"





class NotificationList(ListResource):
    
    def __init__(self, version: Version, account_sid: str, call_sid: str):
        """
        Initialize the NotificationList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resources to read.
        :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resources to read.
        
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 'account_sid': account_sid, 'call_sid': call_sid,  }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Notifications.json'.format(**self._solution)
        
        
    
    
    def stream(self, 
        log: Union[int, object] = values.unset,
        message_date: Union[date, object] = values.unset,
        message_date_before: Union[date, object] = values.unset,
        message_date_after: Union[date, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[NotificationInstance]:
        """
        Streams NotificationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param date message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
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
            log=log,
            message_date=message_date,
            message_date_before=message_date_before,
            message_date_after=message_date_after,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        log: Union[int, object] = values.unset,
        message_date: Union[date, object] = values.unset,
        message_date_before: Union[date, object] = values.unset,
        message_date_after: Union[date, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[NotificationInstance]:
        """
        Asynchronously streams NotificationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param date message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
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
            log=log,
            message_date=message_date,
            message_date_before=message_date_before,
            message_date_after=message_date_after,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        log: Union[int, object] = values.unset,
        message_date: Union[date, object] = values.unset,
        message_date_before: Union[date, object] = values.unset,
        message_date_after: Union[date, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NotificationInstance]:
        """
        Lists NotificationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param date message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            log=log,
            message_date=message_date,
            message_date_before=message_date_before,
            message_date_after=message_date_after,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        log: Union[int, object] = values.unset,
        message_date: Union[date, object] = values.unset,
        message_date_before: Union[date, object] = values.unset,
        message_date_after: Union[date, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NotificationInstance]:
        """
        Asynchronously lists NotificationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param date message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param date message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            log=log,
            message_date=message_date,
            message_date_before=message_date_before,
            message_date_after=message_date_after,
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        log: Union[int, object] = values.unset,
        message_date: Union[date, object] = values.unset,
        message_date_before: Union[date, object] = values.unset,
        message_date_after: Union[date, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> NotificationPage:
        """
        Retrieve a single page of NotificationInstance records from the API.
        Request is executed immediately
        
        :param log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of NotificationInstance
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

    async def page_async(self, 
        log: Union[int, object] = values.unset,
        message_date: Union[date, object] = values.unset,
        message_date_before: Union[date, object] = values.unset,
        message_date_after: Union[date, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> NotificationPage:
        """
        Asynchronously retrieve a single page of NotificationInstance records from the API.
        Request is executed immediately
        
        :param log: Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
        :param message_date: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param message_date_before: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param message_date_after: Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of NotificationInstance
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

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return NotificationPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> NotificationPage:
        """
        Retrieve a specific page of NotificationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of NotificationInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return NotificationPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> NotificationPage:
        """
        Asynchronously retrieve a specific page of NotificationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of NotificationInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return NotificationPage(self._version, response, self._solution)



    def get(self, sid: str) -> NotificationContext:
        """
        Constructs a NotificationContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.
        """
        return NotificationContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=sid)

    def __call__(self, sid: str) -> NotificationContext:
        """
        Constructs a NotificationContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.
        """
        return NotificationContext(self._version, account_sid=self._solution['account_sid'], call_sid=self._solution['call_sid'], sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Api.V2010.NotificationList>'

