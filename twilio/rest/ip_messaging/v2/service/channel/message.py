r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
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


class MessageList(ListResource):

    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        """
        Initialize the MessageList

        :param Version version: Version that contains the resource
        :param service_sid: 
        :param channel_sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.channel.message.MessageList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid,  }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Messages'.format(**self._solution)
        
        
    
    
    
    
    def create(self, x_twilio_webhook_enabled=values.unset, from_=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, last_updated_by=values.unset, body=values.unset, media_sid=values.unset):
        """
        Create the MessageInstance

        :param MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str from_: 
        :param str attributes: 
        :param datetime date_created: 
        :param datetime date_updated: 
        :param str last_updated_by: 
        :param str body: 
        :param str media_sid: 
        
        :returns: The created MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        data = values.of({ 
            'From': from_,
            'Attributes': attributes,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'LastUpdatedBy': last_updated_by,
            'Body': body,
            'MediaSid': media_sid,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return MessageInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])

    async def create_async(self, x_twilio_webhook_enabled=values.unset, from_=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, last_updated_by=values.unset, body=values.unset, media_sid=values.unset):
        """
        Asynchronous coroutine to create the MessageInstance

        :param MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str from_: 
        :param str attributes: 
        :param datetime date_created: 
        :param datetime date_updated: 
        :param str last_updated_by: 
        :param str body: 
        :param str media_sid: 
        
        :returns: The created MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        data = values.of({ 
            'From': from_,
            'Attributes': attributes,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'LastUpdatedBy': last_updated_by,
            'Body': body,
            'MediaSid': media_sid,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return MessageInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])
    
    
    def stream(self, order=values.unset, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param MessageInstance.OrderType order: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            order=order,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, order=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param MessageInstance.OrderType order: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            order=order,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, order=values.unset, limit=None, page_size=None):
        """
        Lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param MessageInstance.OrderType order: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance]
        """
        return list(self.stream(
            order=order,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, order=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param MessageInstance.OrderType order: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance]
        """
        return list(await self.stream_async(
            order=order,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, order=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately
        
        :param MessageInstance.OrderType order: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessagePage
        """
        data = values.of({ 
            'Order': order,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MessagePage(self._version, response, self._solution)

    async def page_async(self, order=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of MessageInstance records from the API.
        Request is executed immediately
        
        :param MessageInstance.OrderType order: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessagePage
        """
        data = values.of({ 
            'Order': order,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return MessagePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessagePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MessagePage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessagePage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return MessagePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageContext
        """
        return MessageContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageContext
        """
        return MessageContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.MessageList>'










class MessagePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MessagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.ip_messaging.v2.service.channel.message.MessagePage
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessagePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        return MessageInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.MessagePage>'




class MessageInstance(InstanceResource):

    class OrderType(object):
        ASC = "asc"
        DESC = "desc"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, service_sid: str, channel_sid: str, sid: str=None):
        """
        Initialize the MessageInstance
        :returns: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'attributes': payload.get('attributes'),
            'service_sid': payload.get('service_sid'),
            'to': payload.get('to'),
            'channel_sid': payload.get('channel_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'last_updated_by': payload.get('last_updated_by'),
            'was_edited': payload.get('was_edited'),
            '_from': payload.get('from'),
            'body': payload.get('body'),
            'index': deserialize.integer(payload.get('index')),
            'type': payload.get('type'),
            'media': payload.get('media'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MessageContext for this MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageContext
        """
        if self._context is None:
            self._context = MessageContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def attributes(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def service_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def to(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['to']
    
    @property
    def channel_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['channel_sid']
    
    @property
    def date_created(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def last_updated_by(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['last_updated_by']
    
    @property
    def was_edited(self):
        """
        :returns: 
        :rtype: bool
        """
        return self._properties['was_edited']
    
    @property
    def _from(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['_from']
    
    @property
    def body(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['body']
    
    @property
    def index(self):
        """
        :returns: 
        :rtype: int
        """
        return self._properties['index']
    
    @property
    def type(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['type']
    
    @property
    def media(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['media']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the MessageInstance
        
        :params MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )
    async def delete_async(self, x_twilio_webhook_enabled=values.unset):
        """
        Asynchronous coroutine that deletes the MessageInstance
        
        :params MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )
    
    
    def fetch(self):
        """
        Fetch the MessageInstance
        

        :returns: The fetched MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the MessageInstance
        

        :returns: The fetched MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, x_twilio_webhook_enabled=values.unset, body=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, last_updated_by=values.unset, from_=values.unset):
        """
        Update the MessageInstance
        
        :params MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str body: 
        :params str attributes: 
        :params datetime date_created: 
        :params datetime date_updated: 
        :params str last_updated_by: 
        :params str from_: 

        :returns: The updated MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        return self._proxy.update(x_twilio_webhook_enabled=x_twilio_webhook_enabled, body=body, attributes=attributes, date_created=date_created, date_updated=date_updated, last_updated_by=last_updated_by, from_=from_, )

    async def update_async(self, x_twilio_webhook_enabled=values.unset, body=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, last_updated_by=values.unset, from_=values.unset):
        """
        Asynchronous coroutine to update the MessageInstance
        
        :params MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str body: 
        :params str attributes: 
        :params datetime date_created: 
        :params datetime date_updated: 
        :params str last_updated_by: 
        :params str from_: 

        :returns: The updated MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        return await self._proxy.update_async(x_twilio_webhook_enabled=x_twilio_webhook_enabled, body=body, attributes=attributes, date_created=date_created, date_updated=date_updated, last_updated_by=last_updated_by, from_=from_, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.MessageInstance {}>'.format(context)

class MessageContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        """
        Initialize the MessageContext

        :param Version version: Version that contains the resource
        :param service_sid: 
        :param channel_sid: 
        :param sid: 

        :returns: twilio.rest.ip_messaging.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Messages/{sid}'.format(**self._solution)
        
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the MessageInstance

        :param MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)
        
    def fetch(self):
        """
        Fetch the MessageInstance
        

        :returns: The fetched MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, x_twilio_webhook_enabled=values.unset, body=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, last_updated_by=values.unset, from_=values.unset):
        """
        Update the MessageInstance
        
        :params MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str body: 
        :params str attributes: 
        :params datetime date_created: 
        :params datetime date_updated: 
        :params str last_updated_by: 
        :params str from_: 

        :returns: The updated MessageInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.message.MessageInstance
        """
        data = values.of({ 
            'Body': body,
            'Attributes': attributes,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'LastUpdatedBy': last_updated_by,
            'From': from_,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return MessageInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.MessageContext {}>'.format(context)


