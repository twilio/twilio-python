"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
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
from twilio.rest.conversations.v1.service.conversation.message.delivery_receipt import DeliveryReceiptList


class MessageList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str, conversation_sid: str):
        """
        Initialize the MessageList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.
        
        :returns: twilio.rest.conversations.v1.service.conversation.message.MessageList
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'conversation_sid': conversation_sid,  }
        self._uri = '/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages'.format(**self._solution)
        
        
    
    
    
    
    def create(self, x_twilio_webhook_enabled=values.unset, author=values.unset, body=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset, media_sid=values.unset, content_sid=values.unset, content_variables=values.unset):
        """
        Create the MessageInstance

        :param MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str author: The channel specific identifier of the message's author. Defaults to `system`.
        :param str body: The content of the message, can be up to 1,600 characters long.
        :param datetime date_created: The date that this resource was created.
        :param datetime date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :param str attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param str media_sid: The Media SID to be attached to the new Message.
        :param str content_sid: The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content-api) template, required for template-generated messages.  **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.
        :param str content_variables: A structurally valid JSON string that contains values to resolve Rich Content template variables.
        
        :returns: The created MessageInstance
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        """
        data = values.of({ 
            'Author': author,
            'Body': body,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
            'MediaSid': media_sid,
            'ContentSid': content_sid,
            'ContentVariables': content_variables,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return MessageInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'])
    
    
    def stream(self, order=values.unset, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param MessageInstance.OrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.conversation.message.MessageInstance]
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
        
        :param MessageInstance.OrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.conversation.message.MessageInstance]
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
        
        :param MessageInstance.OrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessagePage
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
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessagePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MessagePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.service.conversation.message.MessageContext
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageContext
        """
        return MessageContext(self._version, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.service.conversation.message.MessageContext
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageContext
        """
        return MessageContext(self._version, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.MessageList>'










class MessagePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MessagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.service.conversation.message.MessagePage
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessagePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        """
        return MessageInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.MessagePage>'




class MessageInstance(InstanceResource):

    class OrderType(object):
        ASC = "asc"
        DESC = "desc"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, chat_service_sid: str, conversation_sid: str, sid: str=None):
        """
        Initialize the MessageInstance
        :returns: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'chat_service_sid': payload.get('chat_service_sid'),
            'conversation_sid': payload.get('conversation_sid'),
            'sid': payload.get('sid'),
            'index': deserialize.integer(payload.get('index')),
            'author': payload.get('author'),
            'body': payload.get('body'),
            'media': payload.get('media'),
            'attributes': payload.get('attributes'),
            'participant_sid': payload.get('participant_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'delivery': payload.get('delivery'),
            'url': payload.get('url'),
            'links': payload.get('links'),
            'content_sid': payload.get('content_sid'),
        }

        self._context = None
        self._solution = { 'chat_service_sid': chat_service_sid, 'conversation_sid': conversation_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MessageContext for this MessageInstance
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageContext
        """
        if self._context is None:
            self._context = MessageContext(self._version, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this message.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def chat_service_sid(self):
        """
        :returns: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        :rtype: str
        """
        return self._properties['chat_service_sid']
    
    @property
    def conversation_sid(self):
        """
        :returns: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
        :rtype: str
        """
        return self._properties['conversation_sid']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def index(self):
        """
        :returns: The index of the message within the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource).
        :rtype: int
        """
        return self._properties['index']
    
    @property
    def author(self):
        """
        :returns: The channel specific identifier of the message's author. Defaults to `system`.
        :rtype: str
        """
        return self._properties['author']
    
    @property
    def body(self):
        """
        :returns: The content of the message, can be up to 1,600 characters long.
        :rtype: str
        """
        return self._properties['body']
    
    @property
    def media(self):
        """
        :returns: An array of objects that describe the Message's media, if the message contains media. Each object contains these fields: `content_type` with the MIME type of the media, `filename` with the name of the media, `sid` with the SID of the Media resource, and `size` with the media object's file size in bytes. If the Message has no media, this value is `null`.
        :rtype: list[object]
        """
        return self._properties['media']
    
    @property
    def attributes(self):
        """
        :returns: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def participant_sid(self):
        """
        :returns: The unique ID of messages's author participant. Null in case of `system` sent message.
        :rtype: str
        """
        return self._properties['participant_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated. `null` if the message has not been edited.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def delivery(self):
        """
        :returns: An object that contains the summary of delivery statuses for the message to non-chat participants.
        :rtype: dict
        """
        return self._properties['delivery']
    
    @property
    def url(self):
        """
        :returns: An absolute API resource URL for this message.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Contains an absolute API resource URL to access the delivery & read receipts of this message.
        :rtype: dict
        """
        return self._properties['links']
    
    @property
    def content_sid(self):
        """
        :returns: The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content-api) template.
        :rtype: str
        """
        return self._properties['content_sid']
    
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
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        """
        return self._proxy.fetch()
    
    def update(self, x_twilio_webhook_enabled=values.unset, author=values.unset, body=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset):
        """
        Update the MessageInstance
        
        :params MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str author: The channel specific identifier of the message's author. Defaults to `system`.
        :params str body: The content of the message, can be up to 1,600 characters long.
        :params datetime date_created: The date that this resource was created.
        :params datetime date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :params str attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.

        :returns: The updated MessageInstance
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        """
        return self._proxy.update(x_twilio_webhook_enabled=x_twilio_webhook_enabled, author=author, body=body, date_created=date_created, date_updated=date_updated, attributes=attributes, )
    
    @property
    def delivery_receipts(self):
        """
        Access the delivery_receipts

        :returns: twilio.rest.conversations.v1.service.conversation.message.DeliveryReceiptList
        :rtype: twilio.rest.conversations.v1.service.conversation.message.DeliveryReceiptList
        """
        return self._proxy.delivery_receipts
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.MessageInstance {}>'.format(context)

class MessageContext(InstanceContext):

    def __init__(self, version: Version, chat_service_sid: str, conversation_sid: str, sid: str):
        """
        Initialize the MessageContext

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.service.conversation.message.MessageContext
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'chat_service_sid': chat_service_sid,
            'conversation_sid': conversation_sid,
            'sid': sid,
        }
        self._uri = '/Services/{chat_service_sid}/Conversations/{conversation_sid}/Messages/{sid}'.format(**self._solution)
        
        self._delivery_receipts = None
    
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
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid'],
            conversation_sid=self._solution['conversation_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, x_twilio_webhook_enabled=values.unset, author=values.unset, body=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset):
        """
        Update the MessageInstance
        
        :params MessageInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str author: The channel specific identifier of the message's author. Defaults to `system`.
        :params str body: The content of the message, can be up to 1,600 characters long.
        :params datetime date_created: The date that this resource was created.
        :params datetime date_updated: The date that this resource was last updated. `null` if the message has not been edited.
        :params str attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.

        :returns: The updated MessageInstance
        :rtype: twilio.rest.conversations.v1.service.conversation.message.MessageInstance
        """
        data = values.of({ 
            'Author': author,
            'Body': body,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return MessageInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid'],
            conversation_sid=self._solution['conversation_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def delivery_receipts(self):
        """
        Access the delivery_receipts

        :returns: twilio.rest.conversations.v1.service.conversation.message.DeliveryReceiptList
        :rtype: twilio.rest.conversations.v1.service.conversation.message.DeliveryReceiptList
        """
        if self._delivery_receipts is None:
            self._delivery_receipts = DeliveryReceiptList(
                self._version, 
                self._solution['chat_service_sid'],
                self._solution['conversation_sid'],
                self._solution['sid'],
            )
        return self._delivery_receipts
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.MessageContext {}>'.format(context)


