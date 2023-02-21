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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.conversations.v1.message.delivery_receipts import DeliveryReceiptList


class MessageList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str, conversation_sid: str):
        """
        Initialize the MessageList
        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Participant resource is associated with.
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for messages.
        
        :returns: twilio.conversations.v1.message..MessageList
        :rtype: twilio.conversations.v1.message..MessageList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'conversation_sid': conversation_sid,  }
        self._uri = '/Services/${chat_service_sid}/Conversations/${conversation_sid}/Messages'.format(**self._solution)
        
        
    
    
    
    
    def create(self, author=values.unset, body=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset, media_sid=values.unset, content_sid=values.unset, content_variables=values.unset):
        """
        Create the MessageInstance
         :param str author: The channel specific identifier of the message's author. Defaults to `system`.
         :param str body: The content of the message, can be up to 1,600 characters long.
         :param datetime date_created: The date that this resource was created.
         :param datetime date_updated: The date that this resource was last updated. `null` if the message has not been edited.
         :param str attributes: A string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
         :param str media_sid: The Media SID to be attached to the new Message.
         :param str content_sid: The unique ID of the multi-channel [Rich Content](https://www.twilio.com/docs/content-api) template, required for template-generated messages.  **Note** that if this field is set, `Body` and `MediaSid` parameters are ignored.
         :param str content_variables: A structurally valid JSON string that contains values to resolve Rich Content template variables.
        
        :returns: The created MessageInstance
        :rtype: twilio.rest.conversations.v1.message.MessageInstance
        """
        data = values.of({ 
            'Author': author,
            'Body': body,
            'DateCreated': date_created,
            'DateUpdated': date_updated,
            'Attributes': attributes,
            'MediaSid': media_sid,
            'ContentSid': content_sid,
            'ContentVariables': content_variables,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return MessageInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'])
    
    
    def stream(self, order=values.unset, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param ServiceConversationMessageOrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.message.MessageInstance]
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
        
        :param ServiceConversationMessageOrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.message.MessageInstance]
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
        
        :param ServiceConversationMessageOrderType order: The sort order of the returned messages. Can be: `asc` (ascending) or `desc` (descending), with `asc` as the default.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.conversations.v1.message.MessagePage
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
        :rtype: twilio.rest.conversations.v1.message.MessagePage
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
        
        :returns: twilio.rest.conversations.v1.message.MessageContext
        :rtype: twilio.rest.conversations.v1.message.MessageContext
        """
        return MessageContext(self._version, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.message.MessageContext
        :rtype: twilio.rest.conversations.v1.message.MessageContext
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

        :returns: twilio.rest.conversations.v1.message.MessagePage
        :rtype: twilio.rest.conversations.v1.message.MessagePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.message.MessageInstance
        :rtype: twilio.rest.conversations.v1.message.MessageInstance
        """
        return MessageInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.MessagePage>'





class MessageContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str, conversation_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'conversation_sid': conversation_sid, 'sid': sid,  }
        self._uri = '/Services/${chat_service_sid}/Conversations/${conversation_sid}/Messages/${sid}'
        
        self._delivery_receipts = None
    
    def delete(self, x_twilio_webhook_enabled):
        
        

        """
        Deletes the MessageInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the MessageInstance

        :returns: The fetched MessageInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessageInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, author, body, date_created, date_updated, attributes):
        data = values.of({
            'author': author,'body': body,'date_created': date_created,'date_updated': date_updated,'attributes': attributes,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return MessageInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], conversation_sid=self._solution['conversation_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.MessageContext>'



class MessageInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str, conversation_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'chat_service_sid' : payload.get('chat_service_sid'),
            'conversation_sid' : payload.get('conversation_sid'),
            'sid' : payload.get('sid'),
            'index' : payload.get('index'),
            'author' : payload.get('author'),
            'body' : payload.get('body'),
            'media' : payload.get('media'),
            'attributes' : payload.get('attributes'),
            'participant_sid' : payload.get('participant_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'delivery' : payload.get('delivery'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
            'content_sid' : payload.get('content_sid'),
        }

        self._context = None
        self._solution = {
            'chat_service_sid': chat_service_sid or self._properties['chat_service_sid'],'conversation_sid': conversation_sid or self._properties['conversation_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = MessageContext(
                self._version,
                chat_service_sid=self._solution['chat_service_sid'],conversation_sid=self._solution['conversation_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def delivery_receipts(self):
        return self._proxy.delivery_receipts
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.MessageInstance {}>'.format(context)



