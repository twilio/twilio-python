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


class UserConversationList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str, user_sid: str):
        """
        Initialize the UserConversationList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
        :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
        
        :returns: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationList
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'user_sid': user_sid,  }
        self._uri = '/Services/{chat_service_sid}/Users/{user_sid}/Conversations'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the UserConversationInstance

        :returns: The fetched UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return UserConversationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], user_sid=self._solution['user_sid'])
    
    
    def update(self, notification_level=values.unset, last_read_timestamp=values.unset, last_read_message_index=values.unset):
        """
        Update the UserConversationInstance

        :param NotificationLevel notification_level: 
        :param datetime last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
        :param int last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
        
        :returns: The created UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        """
        data = values.of({ 
            'NotificationLevel': notification_level,
            'LastReadTimestamp': serialize.iso8601_datetime(last_read_timestamp),
            'LastReadMessageIndex': last_read_message_index,
        })
        
        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return UserConversationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], user_sid=self._solution['user_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams UserConversationInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UserConversationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UserConversationInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UserConversationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserConversationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UserConversationPage(self._version, response, self._solution)


    def get(self, conversation_sid):
        """
        Constructs a UserConversationContext
        
        :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
        
        :returns: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationContext
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationContext
        """
        return UserConversationContext(self._version, chat_service_sid=self._solution['chat_service_sid'], user_sid=self._solution['user_sid'], conversation_sid=conversation_sid)

    def __call__(self, conversation_sid):
        """
        Constructs a UserConversationContext
        
        :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
        
        :returns: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationContext
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationContext
        """
        return UserConversationContext(self._version, chat_service_sid=self._solution['chat_service_sid'], user_sid=self._solution['user_sid'], conversation_sid=conversation_sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserConversationList>'








class UserConversationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserConversationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationPage
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserConversationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        """
        return UserConversationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], user_sid=self._solution['user_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserConversationPage>'




class UserConversationInstance(InstanceResource):

    class NotificationLevel(object):
        DEFAULT = "default"
        MUTED = "muted"

    class State(object):
        INACTIVE = "inactive"
        ACTIVE = "active"
        CLOSED = "closed"

    def __init__(self, version, payload, chat_service_sid: str, user_sid: str, conversation_sid: str=None):
        """
        Initialize the UserConversationInstance
        :returns: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'chat_service_sid': payload.get('chat_service_sid'),
            'conversation_sid': payload.get('conversation_sid'),
            'unread_messages_count': deserialize.integer(payload.get('unread_messages_count')),
            'last_read_message_index': deserialize.integer(payload.get('last_read_message_index')),
            'participant_sid': payload.get('participant_sid'),
            'user_sid': payload.get('user_sid'),
            'friendly_name': payload.get('friendly_name'),
            'conversation_state': payload.get('conversation_state'),
            'timers': payload.get('timers'),
            'attributes': payload.get('attributes'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'created_by': payload.get('created_by'),
            'notification_level': payload.get('notification_level'),
            'unique_name': payload.get('unique_name'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'chat_service_sid': chat_service_sid, 'user_sid': user_sid, 'conversation_sid': conversation_sid or self._properties['conversation_sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserConversationContext for this UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationContext
        """
        if self._context is None:
            self._context = UserConversationContext(self._version, chat_service_sid=self._solution['chat_service_sid'], user_sid=self._solution['user_sid'], conversation_sid=self._solution['conversation_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def chat_service_sid(self):
        """
        :returns: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
        :rtype: str
        """
        return self._properties['chat_service_sid']
    
    @property
    def conversation_sid(self):
        """
        :returns: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this User Conversation.
        :rtype: str
        """
        return self._properties['conversation_sid']
    
    @property
    def unread_messages_count(self):
        """
        :returns: The number of unread Messages in the Conversation for the Participant.
        :rtype: int
        """
        return self._properties['unread_messages_count']
    
    @property
    def last_read_message_index(self):
        """
        :returns: The index of the last Message in the Conversation that the Participant has read.
        :rtype: int
        """
        return self._properties['last_read_message_index']
    
    @property
    def participant_sid(self):
        """
        :returns: The unique ID of the [participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) the user conversation belongs to.
        :rtype: str
        """
        return self._properties['participant_sid']
    
    @property
    def user_sid(self):
        """
        :returns: The unique string that identifies the [User resource](https://www.twilio.com/docs/conversations/api/user-resource).
        :rtype: str
        """
        return self._properties['user_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The human-readable name of this conversation, limited to 256 characters. Optional.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def conversation_state(self):
        """
        :returns: 
        :rtype: State
        """
        return self._properties['conversation_state']
    
    @property
    def timers(self):
        """
        :returns: Timer date values representing state update for this conversation.
        :rtype: dict
        """
        return self._properties['timers']
    
    @property
    def attributes(self):
        """
        :returns: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def date_created(self):
        """
        :returns: The date that this conversation was created, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this conversation was last updated, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def created_by(self):
        """
        :returns: Identity of the creator of this Conversation.
        :rtype: str
        """
        return self._properties['created_by']
    
    @property
    def notification_level(self):
        """
        :returns: 
        :rtype: NotificationLevel
        """
        return self._properties['notification_level']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the Conversation resource. It can be used to address the resource in place of the resource's `conversation_sid` in the URL.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Contains absolute URLs to access the [participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) and [conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) of this conversation.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the UserConversationInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the UserConversationInstance
        

        :returns: The fetched UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        """
        return self._proxy.fetch()
    
    def update(self, notification_level=values.unset, last_read_timestamp=values.unset, last_read_message_index=values.unset):
        """
        Update the UserConversationInstance
        
        :params NotificationLevel notification_level: 
        :params datetime last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
        :params int last_read_message_index: The index of the last Message in the Conversation that the Participant has read.

        :returns: The updated UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        """
        return self._proxy.update(notification_level=notification_level, last_read_timestamp=last_read_timestamp, last_read_message_index=last_read_message_index, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.UserConversationInstance {}>'.format(context)

class UserConversationContext(InstanceContext):

    def __init__(self, version: Version, chat_service_sid: str, user_sid: str, conversation_sid: str):
        """
        Initialize the UserConversationContext

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.:param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.:param conversation_sid: The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).

        :returns: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationContext
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'chat_service_sid': chat_service_sid,
            'user_sid': user_sid,
            'conversation_sid': conversation_sid,
        }
        self._uri = '/Services/{chat_service_sid}/Users/{user_sid}/Conversations/{conversation_sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the UserConversationInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the UserConversationInstance
        

        :returns: The fetched UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserConversationInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid'],
            user_sid=self._solution['user_sid'],
            conversation_sid=self._solution['conversation_sid'],
            
        )
        
    def update(self, notification_level=values.unset, last_read_timestamp=values.unset, last_read_message_index=values.unset):
        """
        Update the UserConversationInstance
        
        :params NotificationLevel notification_level: 
        :params datetime last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
        :params int last_read_message_index: The index of the last Message in the Conversation that the Participant has read.

        :returns: The updated UserConversationInstance
        :rtype: twilio.rest.conversations.v1.service.user.user_conversation.UserConversationInstance
        """
        data = values.of({ 
            'NotificationLevel': notification_level,
            'LastReadTimestamp': serialize.iso8601_datetime(last_read_timestamp),
            'LastReadMessageIndex': last_read_message_index,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return UserConversationInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid'],
            user_sid=self._solution['user_sid'],
            conversation_sid=self._solution['conversation_sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.UserConversationContext {}>'.format(context)


