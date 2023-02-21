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
from twilio.rest.conversations.v1.conversation.messages import MessageList
from twilio.rest.conversations.v1.conversation.participants import ParticipantList
from twilio.rest.conversations.v1.conversation.webhooks import WebhookList


class ConversationList(ListResource):

    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the ConversationList
        :param Version version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Conversation resource is associated with.
        
        :returns: twilio.conversations.v1.conversation..ConversationList
        :rtype: twilio.conversations.v1.conversation..ConversationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid,  }
        self._uri = '/Services/${chat_service_sid}/Conversations'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name=values.unset, unique_name=values.unset, attributes=values.unset, messaging_service_sid=values.unset, date_created=values.unset, date_updated=values.unset, state=values.unset, timers_inactive=values.unset, timers_closed=values.unset):
        """
        Create the ConversationInstance
         :param str friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
         :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used to address the resource in place of the resource's `sid` in the URL.
         :param str attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
         :param str messaging_service_sid: The unique ID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) this conversation belongs to.
         :param datetime date_created: The date that this resource was created.
         :param datetime date_updated: The date that this resource was last updated.
         :param ServiceConversationState state: 
         :param str timers_inactive: ISO8601 duration when conversation will be switched to `inactive` state. Minimum value for this timer is 1 minute.
         :param str timers_closed: ISO8601 duration when conversation will be switched to `closed` state. Minimum value for this timer is 10 minutes.
        
        :returns: The created ConversationInstance
        :rtype: twilio.rest.conversations.v1.conversation.ConversationInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Attributes': attributes,
            'MessagingServiceSid': messaging_service_sid,
            'DateCreated': date_created,
            'DateUpdated': date_updated,
            'State': state,
            'Timers.Inactive': timers_inactive,
            'Timers.Closed': timers_closed,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return ConversationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ConversationInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.conversations.v1.conversation.ConversationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ConversationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.conversation.ConversationInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ConversationInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConversationInstance
        :rtype: twilio.rest.conversations.v1.conversation.ConversationPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ConversationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ConversationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ConversationInstance
        :rtype: twilio.rest.conversations.v1.conversation.ConversationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ConversationPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ConversationContext
        
        :param sid: A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
        
        :returns: twilio.rest.conversations.v1.conversation.ConversationContext
        :rtype: twilio.rest.conversations.v1.conversation.ConversationContext
        """
        return ConversationContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ConversationContext
        
        :param sid: A 34 character string that uniquely identifies this resource. Can also be the `unique_name` of the Conversation.
        
        :returns: twilio.rest.conversations.v1.conversation.ConversationContext
        :rtype: twilio.rest.conversations.v1.conversation.ConversationContext
        """
        return ConversationContext(self._version, chat_service_sid=self._solution['chat_service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ConversationList>'










class ConversationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ConversationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.conversation.ConversationPage
        :rtype: twilio.rest.conversations.v1.conversation.ConversationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConversationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.conversation.ConversationInstance
        :rtype: twilio.rest.conversations.v1.conversation.ConversationInstance
        """
        return ConversationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ConversationPage>'





class ConversationContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'chat_service_sid': chat_service_sid, 'sid': sid,  }
        self._uri = '/Services/${chat_service_sid}/Conversations/${sid}'
        
        self._messages = None
        self._participants = None
        self._webhooks = None
    
    def delete(self, x_twilio_webhook_enabled):
        
        

        """
        Deletes the ConversationInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the ConversationInstance

        :returns: The fetched ConversationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConversationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, friendly_name, date_created, date_updated, attributes, messaging_service_sid, state, timers_inactive, timers_closed, unique_name):
        data = values.of({
            'friendly_name': friendly_name,'date_created': date_created,'date_updated': date_updated,'attributes': attributes,'messaging_service_sid': messaging_service_sid,'state': state,'timers_inactive': timers_inactive,'timers_closed': timers_closed,'unique_name': unique_name,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ConversationInstance(self._version, payload, chat_service_sid=self._solution['chat_service_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ConversationContext>'



class ConversationInstance(InstanceResource):
    def __init__(self, version, payload, chat_service_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'chat_service_sid' : payload.get('chat_service_sid'),
            'messaging_service_sid' : payload.get('messaging_service_sid'),
            'sid' : payload.get('sid'),
            'friendly_name' : payload.get('friendly_name'),
            'unique_name' : payload.get('unique_name'),
            'attributes' : payload.get('attributes'),
            'state' : payload.get('state'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'timers' : payload.get('timers'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
            'bindings' : payload.get('bindings'),
        }

        self._context = None
        self._solution = {
            'chat_service_sid': chat_service_sid or self._properties['chat_service_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ConversationContext(
                self._version,
                chat_service_sid=self._solution['chat_service_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def messages(self):
        return self._proxy.messages
    @property
    def participants(self):
        return self._proxy.participants
    @property
    def webhooks(self):
        return self._proxy.webhooks
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.ConversationInstance {}>'.format(context)



