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


class ParticipantList(ListResource):

    def __init__(self, version: Version, conversation_sid: str):
        """
        Initialize the ParticipantList

        :param Version version: Version that contains the resource
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for participants.
        
        :returns: twilio.rest.conversations.v1.conversation.participant.ParticipantList
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'conversation_sid': conversation_sid,  }
        self._uri = '/Conversations/{conversation_sid}/Participants'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the ParticipantInstance

        :returns: The fetched ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return ParticipantInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'])
    
    
    def update(self, x_twilio_webhook_enabled=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset, role_sid=values.unset, messaging_binding_proxy_address=values.unset, messaging_binding_projected_address=values.unset, identity=values.unset, last_read_message_index=values.unset, last_read_timestamp=values.unset):
        """
        Update the ParticipantInstance

        :param WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param datetime date_created: The date that this resource was created.
        :param datetime date_updated: The date that this resource was last updated.
        :param str attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param str role_sid: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
        :param str messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact with. 'null' value will remove it.
        :param str messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS. 'null' value will remove it.
        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param int last_read_message_index: Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
        :param str last_read_timestamp: Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
        
        :returns: The created ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        data = values.of({ 
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
            'RoleSid': role_sid,
            'MessagingBinding.ProxyAddress': messaging_binding_proxy_address,
            'MessagingBinding.ProjectedAddress': messaging_binding_projected_address,
            'Identity': identity,
            'LastReadMessageIndex': last_read_message_index,
            'LastReadTimestamp': last_read_timestamp,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return ParticipantInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'])
    
    
    def create(self, x_twilio_webhook_enabled=values.unset, identity=values.unset, messaging_binding_address=values.unset, messaging_binding_proxy_address=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset, messaging_binding_projected_address=values.unset, role_sid=values.unset):
        """
        Create the ParticipantInstance

        :param WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :param str messaging_binding_address: The address of the participant's device, e.g. a phone or WhatsApp number. Together with the Proxy address, this determines a participant uniquely. This field (with proxy_address) is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
        :param str messaging_binding_proxy_address: The address of the Twilio phone number (or WhatsApp number) that the participant is in contact with. This field, together with participant address, is only null when the participant is interacting from an SDK endpoint (see the 'identity' field).
        :param datetime date_created: The date that this resource was created.
        :param datetime date_updated: The date that this resource was last updated.
        :param str attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :param str messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS. Communication mask for the Conversation participant with Identity.
        :param str role_sid: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
        
        :returns: The created ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        data = values.of({ 
            'Identity': identity,
            'MessagingBinding.Address': messaging_binding_address,
            'MessagingBinding.ProxyAddress': messaging_binding_proxy_address,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
            'MessagingBinding.ProjectedAddress': messaging_binding_projected_address,
            'RoleSid': role_sid,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return ParticipantInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ParticipantInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.conversations.v1.conversation.participant.ParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.conversation.participant.ParticipantInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ParticipantPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.conversation.participant.ParticipantContext
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantContext
        """
        return ParticipantContext(self._version, conversation_sid=self._solution['conversation_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.conversation.participant.ParticipantContext
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantContext
        """
        return ParticipantContext(self._version, conversation_sid=self._solution['conversation_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ParticipantList>'










class ParticipantPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.conversation.participant.ParticipantPage
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        return ParticipantInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ParticipantPage>'




class ParticipantInstance(InstanceResource):

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, conversation_sid: str, sid: str=None):
        """
        Initialize the ParticipantInstance
        :returns: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'conversation_sid': payload.get('conversation_sid'),
            'sid': payload.get('sid'),
            'identity': payload.get('identity'),
            'attributes': payload.get('attributes'),
            'messaging_binding': payload.get('messaging_binding'),
            'role_sid': payload.get('role_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'last_read_message_index': deserialize.integer(payload.get('last_read_message_index')),
            'last_read_timestamp': payload.get('last_read_timestamp'),
        }

        self._context = None
        self._solution = { 'conversation_sid': conversation_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ParticipantContext for this ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantContext
        """
        if self._context is None:
            self._context = ParticipantContext(self._version, conversation_sid=self._solution['conversation_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this participant.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def conversation_sid(self):
        """
        :returns: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.
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
    def identity(self):
        """
        :returns: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def attributes(self):
        """
        :returns: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def messaging_binding(self):
        """
        :returns: Information about how this participant exchanges messages with the conversation. A JSON parameter consisting of type and address fields of the participant.
        :rtype: dict
        """
        return self._properties['messaging_binding']
    
    @property
    def role_sid(self):
        """
        :returns: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
        :rtype: str
        """
        return self._properties['role_sid']
    
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
        :returns: The date that this resource was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: An absolute API resource URL for this participant.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def last_read_message_index(self):
        """
        :returns: Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
        :rtype: int
        """
        return self._properties['last_read_message_index']
    
    @property
    def last_read_timestamp(self):
        """
        :returns: Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
        :rtype: str
        """
        return self._properties['last_read_timestamp']
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the ParticipantInstance
        
        :params WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )
    
    def fetch(self):
        """
        Fetch the ParticipantInstance
        

        :returns: The fetched ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        return self._proxy.fetch()
    
    def update(self, x_twilio_webhook_enabled=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset, role_sid=values.unset, messaging_binding_proxy_address=values.unset, messaging_binding_projected_address=values.unset, identity=values.unset, last_read_message_index=values.unset, last_read_timestamp=values.unset):
        """
        Update the ParticipantInstance
        
        :params WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params datetime date_created: The date that this resource was created.
        :params datetime date_updated: The date that this resource was last updated.
        :params str attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :params str role_sid: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
        :params str messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact with. 'null' value will remove it.
        :params str messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS. 'null' value will remove it.
        :params str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :params int last_read_message_index: Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
        :params str last_read_timestamp: Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.

        :returns: The updated ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        return self._proxy.update(x_twilio_webhook_enabled=x_twilio_webhook_enabled, date_created=date_created, date_updated=date_updated, attributes=attributes, role_sid=role_sid, messaging_binding_proxy_address=messaging_binding_proxy_address, messaging_binding_projected_address=messaging_binding_projected_address, identity=identity, last_read_message_index=last_read_message_index, last_read_timestamp=last_read_timestamp, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.ParticipantInstance {}>'.format(context)

class ParticipantContext(InstanceContext):

    def __init__(self, version: Version, conversation_sid: str, sid: str):
        """
        Initialize the ParticipantContext

        :param Version version: Version that contains the resource
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this participant.:param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.conversation.participant.ParticipantContext
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'conversation_sid': conversation_sid,
            'sid': sid,
        }
        self._uri = '/Conversations/{conversation_sid}/Participants/{sid}'.format(**self._solution)
        
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the ParticipantInstance

        :param WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)
        
    def fetch(self):
        """
        Fetch the ParticipantInstance
        

        :returns: The fetched ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ParticipantInstance(
            self._version,
            payload,
            conversation_sid=self._solution['conversation_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, x_twilio_webhook_enabled=values.unset, date_created=values.unset, date_updated=values.unset, attributes=values.unset, role_sid=values.unset, messaging_binding_proxy_address=values.unset, messaging_binding_projected_address=values.unset, identity=values.unset, last_read_message_index=values.unset, last_read_timestamp=values.unset):
        """
        Update the ParticipantInstance
        
        :params WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params datetime date_created: The date that this resource was created.
        :params datetime date_updated: The date that this resource was last updated.
        :params str attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \\\"{}\\\" will be returned.
        :params str role_sid: The SID of a conversation-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the participant.
        :params str messaging_binding_proxy_address: The address of the Twilio phone number that the participant is in contact with. 'null' value will remove it.
        :params str messaging_binding_projected_address: The address of the Twilio phone number that is used in Group MMS. 'null' value will remove it.
        :params str identity: A unique string identifier for the conversation participant as [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource). This parameter is non-null if (and only if) the participant is using the Conversations SDK to communicate. Limited to 256 characters.
        :params int last_read_message_index: Index of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.
        :params str last_read_timestamp: Timestamp of last “read” message in the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for the Participant.

        :returns: The updated ParticipantInstance
        :rtype: twilio.rest.conversations.v1.conversation.participant.ParticipantInstance
        """
        data = values.of({ 
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
            'RoleSid': role_sid,
            'MessagingBinding.ProxyAddress': messaging_binding_proxy_address,
            'MessagingBinding.ProjectedAddress': messaging_binding_projected_address,
            'Identity': identity,
            'LastReadMessageIndex': last_read_message_index,
            'LastReadTimestamp': last_read_timestamp,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return ParticipantInstance(
            self._version,
            payload,
            conversation_sid=self._solution['conversation_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.ParticipantContext {}>'.format(context)


