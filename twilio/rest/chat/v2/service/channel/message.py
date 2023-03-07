"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Chat
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
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to read the Message resources from.
        :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to read belongs to. This value can be the Channel resource's `sid` or `unique_name`.
        
        :returns: twilio.rest.chat.v2.service.channel.message.MessageList
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid,  }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Messages'.format(**self._solution)
        
        
    
    
    
    
    def create(self, x_twilio_webhook_enabled=values.unset, from_=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, last_updated_by=values.unset, body=values.unset, media_sid=values.unset):
        """
        Create the MessageInstance

        :param MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str from_: The [Identity](https://www.twilio.com/docs/chat/identity) of the new message's author. The default value is `system`.
        :param str attributes: A valid JSON string that contains application-specific data.
        :param datetime date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat's history is being recreated from a backup/separate source.
        :param datetime date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
        :param str last_updated_by: The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
        :param str body: The message to send to the channel. Can be an empty string or `null`, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
        :param str media_sid: The SID of the [Media](https://www.twilio.com/docs/chat/rest/media) to attach to the new Message.
        
        :returns: The created MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
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
    
    
    def stream(self, order=values.unset, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param MessageInstance.OrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending) with `asc` as the default.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.message.MessageInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            order=order,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, order=values.unset, limit=None, page_size=None):
        """
        Lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param MessageInstance.OrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending) with `asc` as the default.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v2.service.channel.message.MessageInstance]
        """
        return list(self.stream(
            order=order,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, order=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately
        
        :param MessageInstance.OrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending) with `asc` as the default.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessagePage
        """
        data = values.of({ 
            'Order': order,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MessagePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessagePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MessagePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: The SID of the Message resource to update.
        
        :returns: twilio.rest.chat.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageContext
        """
        return MessageContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: The SID of the Message resource to update.
        
        :returns: twilio.rest.chat.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageContext
        """
        return MessageContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.MessageList>'










class MessagePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MessagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.chat.v2.service.channel.message.MessagePage
        :rtype: twilio.rest.chat.v2.service.channel.message.MessagePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v2.service.channel.message.MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        return MessageInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V2.MessagePage>'




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
        :returns: twilio.rest.chat.v2.service.channel.message.MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
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
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageContext
        """
        if self._context is None:
            self._context = MessageContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Message resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Message resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def to(self):
        """
        :returns: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) that the message was sent to.
        :rtype: str
        """
        return self._properties['to']
    
    @property
    def channel_sid(self):
        """
        :returns: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource belongs to.
        :rtype: str
        """
        return self._properties['channel_sid']
    
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
    def last_updated_by(self):
        """
        :returns: The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
        :rtype: str
        """
        return self._properties['last_updated_by']
    
    @property
    def was_edited(self):
        """
        :returns: Whether the message has been edited since it was created.
        :rtype: bool
        """
        return self._properties['was_edited']
    
    @property
    def _from(self):
        """
        :returns: The [Identity](https://www.twilio.com/docs/chat/identity) of the message's author. The default value is `system`.
        :rtype: str
        """
        return self._properties['_from']
    
    @property
    def body(self):
        """
        :returns: The content of the message.
        :rtype: str
        """
        return self._properties['body']
    
    @property
    def index(self):
        """
        :returns: The index of the message within the [Channel](https://www.twilio.com/docs/chat/channels). Indices may skip numbers, but will always be in order of when the message was received.
        :rtype: int
        """
        return self._properties['index']
    
    @property
    def type(self):
        """
        :returns: The Message type. Can be: `text` or `media`.
        :rtype: str
        """
        return self._properties['type']
    
    @property
    def media(self):
        """
        :returns: An object that describes the Message's media, if the message contains media. The object contains these fields: `content_type` with the MIME type of the media, `filename` with the name of the media, `sid` with the SID of the Media resource, and `size` with the media object's file size in bytes. If the Message has no media, this value is `null`.
        :rtype: dict
        """
        return self._properties['media']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Message resource.
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
    
    def fetch(self):
        """
        Fetch the MessageInstance
        

        :returns: The fetched MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        return self._proxy.fetch()
    
    def update(self, x_twilio_webhook_enabled=values.unset, body=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, last_updated_by=values.unset, from_=values.unset):
        """
        Update the MessageInstance
        
        :params MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str body: The message to send to the channel. Can be an empty string or `null`, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
        :params str attributes: A valid JSON string that contains application-specific data.
        :params datetime date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat's history is being recreated from a backup/separate source.
        :params datetime date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
        :params str last_updated_by: The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
        :params str from_: The [Identity](https://www.twilio.com/docs/chat/identity) of the message's author.

        :returns: The updated MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
        """
        return self._proxy.update(x_twilio_webhook_enabled=x_twilio_webhook_enabled, body=body, attributes=attributes, date_created=date_created, date_updated=date_updated, last_updated_by=last_updated_by, from_=from_, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V2.MessageInstance {}>'.format(context)

class MessageContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        """
        Initialize the MessageContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) to update the Message resource in.
        :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/chat/channels) the Message resource to update belongs to. This value can be the Channel resource's `sid` or `unique_name`.
        :param sid: The SID of the Message resource to update.

        :returns: twilio.rest.chat.v2.service.channel.message.MessageContext
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageContext
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
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
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
        :params str body: The message to send to the channel. Can be an empty string or `null`, which sets the value as an empty string. You can send structured data in the body by serializing it as a string.
        :params str attributes: A valid JSON string that contains application-specific data.
        :params datetime date_created: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was created. The default value is the current time set by the Chat service. This parameter should only be used when a Chat's history is being recreated from a backup/separate source.
        :params datetime date_updated: The date, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, to assign to the resource as the date it was last updated.
        :params str last_updated_by: The [Identity](https://www.twilio.com/docs/chat/identity) of the User who last updated the Message, if applicable.
        :params str from_: The [Identity](https://www.twilio.com/docs/chat/identity) of the message's author.

        :returns: The updated MessageInstance
        :rtype: twilio.rest.chat.v2.service.channel.message.MessageInstance
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
        return '<Twilio.Chat.V2.MessageContext {}>'.format(context)


