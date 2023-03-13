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


from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class NotificationList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.
        
        :returns: twilio.rest.conversations.v1.service.configuration.notification.NotificationList
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        
        
        
    
    

    def get(self):
        """
        Constructs a NotificationContext
        
        :returns: twilio.rest.conversations.v1.service.configuration.notification.NotificationContext
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationContext
        """
        return NotificationContext(self._version, chat_service_sid=self._solution['chat_service_sid'])

    def __call__(self):
        """
        Constructs a NotificationContext
        
        :returns: twilio.rest.conversations.v1.service.configuration.notification.NotificationContext
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationContext
        """
        return NotificationContext(self._version, chat_service_sid=self._solution['chat_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.NotificationList>'

class NotificationInstance(InstanceResource):

    def __init__(self, version, payload, chat_service_sid: str):
        """
        Initialize the NotificationInstance
        :returns: twilio.rest.conversations.v1.service.configuration.notification.NotificationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'chat_service_sid': payload.get('chat_service_sid'),
            'new_message': payload.get('new_message'),
            'added_to_conversation': payload.get('added_to_conversation'),
            'removed_from_conversation': payload.get('removed_from_conversation'),
            'log_enabled': payload.get('log_enabled'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'chat_service_sid': chat_service_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NotificationContext for this NotificationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationContext
        """
        if self._context is None:
            self._context = NotificationContext(self._version, chat_service_sid=self._solution['chat_service_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this configuration.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def chat_service_sid(self):
        """
        :returns: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.
        :rtype: str
        """
        return self._properties['chat_service_sid']
    
    @property
    def new_message(self):
        """
        :returns: The Push Notification configuration for New Messages.
        :rtype: dict
        """
        return self._properties['new_message']
    
    @property
    def added_to_conversation(self):
        """
        :returns: The Push Notification configuration for being added to a Conversation.
        :rtype: dict
        """
        return self._properties['added_to_conversation']
    
    @property
    def removed_from_conversation(self):
        """
        :returns: The Push Notification configuration for being removed from a Conversation.
        :rtype: dict
        """
        return self._properties['removed_from_conversation']
    
    @property
    def log_enabled(self):
        """
        :returns: Weather the notification logging is enabled.
        :rtype: bool
        """
        return self._properties['log_enabled']
    
    @property
    def url(self):
        """
        :returns: An absolute API resource URL for this configuration.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the NotificationInstance
        

        :returns: The fetched NotificationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationInstance
        """
        return self._proxy.fetch()
    
    def update(self, log_enabled=values.unset, new_message_enabled=values.unset, new_message_template=values.unset, new_message_sound=values.unset, new_message_badge_count_enabled=values.unset, added_to_conversation_enabled=values.unset, added_to_conversation_template=values.unset, added_to_conversation_sound=values.unset, removed_from_conversation_enabled=values.unset, removed_from_conversation_template=values.unset, removed_from_conversation_sound=values.unset, new_message_with_media_enabled=values.unset, new_message_with_media_template=values.unset):
        """
        Update the NotificationInstance
        
        :params bool log_enabled: Weather the notification logging is enabled.
        :params bool new_message_enabled: Whether to send a notification when a new message is added to a conversation. The default is `false`.
        :params str new_message_template: The template to use to create the notification text displayed when a new message is added to a conversation and `new_message.enabled` is `true`.
        :params str new_message_sound: The name of the sound to play when a new message is added to a conversation and `new_message.enabled` is `true`.
        :params bool new_message_badge_count_enabled: Whether the new message badge is enabled. The default is `false`.
        :params bool added_to_conversation_enabled: Whether to send a notification when a participant is added to a conversation. The default is `false`.
        :params str added_to_conversation_template: The template to use to create the notification text displayed when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.
        :params str added_to_conversation_sound: The name of the sound to play when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.
        :params bool removed_from_conversation_enabled: Whether to send a notification to a user when they are removed from a conversation. The default is `false`.
        :params str removed_from_conversation_template: The template to use to create the notification text displayed to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.
        :params str removed_from_conversation_sound: The name of the sound to play to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.
        :params bool new_message_with_media_enabled: Whether to send a notification when a new message with media/file attachments is added to a conversation. The default is `false`.
        :params str new_message_with_media_template: The template to use to create the notification text displayed when a new message with media/file attachments is added to a conversation and `new_message.attachments.enabled` is `true`.

        :returns: The updated NotificationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationInstance
        """
        return self._proxy.update(log_enabled=log_enabled, new_message_enabled=new_message_enabled, new_message_template=new_message_template, new_message_sound=new_message_sound, new_message_badge_count_enabled=new_message_badge_count_enabled, added_to_conversation_enabled=added_to_conversation_enabled, added_to_conversation_template=added_to_conversation_template, added_to_conversation_sound=added_to_conversation_sound, removed_from_conversation_enabled=removed_from_conversation_enabled, removed_from_conversation_template=removed_from_conversation_template, removed_from_conversation_sound=removed_from_conversation_sound, new_message_with_media_enabled=new_message_with_media_enabled, new_message_with_media_template=new_message_with_media_template, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.NotificationInstance {}>'.format(context)

class NotificationContext(InstanceContext):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the NotificationContext

        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Configuration applies to.

        :returns: twilio.rest.conversations.v1.service.configuration.notification.NotificationContext
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'chat_service_sid': chat_service_sid,
        }
        self._uri = '/Services/{chat_service_sid}/Configuration/Notifications'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the NotificationInstance
        

        :returns: The fetched NotificationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return NotificationInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid'],
            
        )
        
    def update(self, log_enabled=values.unset, new_message_enabled=values.unset, new_message_template=values.unset, new_message_sound=values.unset, new_message_badge_count_enabled=values.unset, added_to_conversation_enabled=values.unset, added_to_conversation_template=values.unset, added_to_conversation_sound=values.unset, removed_from_conversation_enabled=values.unset, removed_from_conversation_template=values.unset, removed_from_conversation_sound=values.unset, new_message_with_media_enabled=values.unset, new_message_with_media_template=values.unset):
        """
        Update the NotificationInstance
        
        :params bool log_enabled: Weather the notification logging is enabled.
        :params bool new_message_enabled: Whether to send a notification when a new message is added to a conversation. The default is `false`.
        :params str new_message_template: The template to use to create the notification text displayed when a new message is added to a conversation and `new_message.enabled` is `true`.
        :params str new_message_sound: The name of the sound to play when a new message is added to a conversation and `new_message.enabled` is `true`.
        :params bool new_message_badge_count_enabled: Whether the new message badge is enabled. The default is `false`.
        :params bool added_to_conversation_enabled: Whether to send a notification when a participant is added to a conversation. The default is `false`.
        :params str added_to_conversation_template: The template to use to create the notification text displayed when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.
        :params str added_to_conversation_sound: The name of the sound to play when a participant is added to a conversation and `added_to_conversation.enabled` is `true`.
        :params bool removed_from_conversation_enabled: Whether to send a notification to a user when they are removed from a conversation. The default is `false`.
        :params str removed_from_conversation_template: The template to use to create the notification text displayed to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.
        :params str removed_from_conversation_sound: The name of the sound to play to a user when they are removed from a conversation and `removed_from_conversation.enabled` is `true`.
        :params bool new_message_with_media_enabled: Whether to send a notification when a new message with media/file attachments is added to a conversation. The default is `false`.
        :params str new_message_with_media_template: The template to use to create the notification text displayed when a new message with media/file attachments is added to a conversation and `new_message.attachments.enabled` is `true`.

        :returns: The updated NotificationInstance
        :rtype: twilio.rest.conversations.v1.service.configuration.notification.NotificationInstance
        """
        data = values.of({ 
            'LogEnabled': log_enabled,
            'NewMessage.Enabled': new_message_enabled,
            'NewMessage.Template': new_message_template,
            'NewMessage.Sound': new_message_sound,
            'NewMessage.BadgeCountEnabled': new_message_badge_count_enabled,
            'AddedToConversation.Enabled': added_to_conversation_enabled,
            'AddedToConversation.Template': added_to_conversation_template,
            'AddedToConversation.Sound': added_to_conversation_sound,
            'RemovedFromConversation.Enabled': removed_from_conversation_enabled,
            'RemovedFromConversation.Template': removed_from_conversation_template,
            'RemovedFromConversation.Sound': removed_from_conversation_sound,
            'NewMessage.WithMedia.Enabled': new_message_with_media_enabled,
            'NewMessage.WithMedia.Template': new_message_with_media_template,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return NotificationInstance(
            self._version,
            payload,
            chat_service_sid=self._solution['chat_service_sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.NotificationContext {}>'.format(context)


