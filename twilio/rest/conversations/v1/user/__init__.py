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
from twilio.rest.conversations.v1.user.user_conversation import UserConversationList


class UserList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.conversations.v1.user.UserList
        :rtype: twilio.rest.conversations.v1.user.UserList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Users'.format(**self._solution)
        
        
    
    
    
    
    def create(self, identity, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, attributes=values.unset, role_sid=values.unset):
        """
        Create the UserInstance

        :param str identity: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
        :param UserWebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.
        
        :returns: The created UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        data = values.of({ 
            'Identity': identity,
            'FriendlyName': friendly_name,
            'Attributes': attributes,
            'RoleSid': role_sid,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return UserInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams UserInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.conversations.v1.user.UserInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UserInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.user.UserInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UserPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a UserContext
        
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        
        :returns: twilio.rest.conversations.v1.user.UserContext
        :rtype: twilio.rest.conversations.v1.user.UserContext
        """
        return UserContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a UserContext
        
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        
        :returns: twilio.rest.conversations.v1.user.UserContext
        :rtype: twilio.rest.conversations.v1.user.UserContext
        """
        return UserContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserList>'










class UserPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.user.UserPage
        :rtype: twilio.rest.conversations.v1.user.UserPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.user.UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        return UserInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserPage>'




class UserContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the UserContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.

        :returns: twilio.rest.conversations.v1.user.UserContext
        :rtype: twilio.rest.conversations.v1.user.UserContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Users/{sid}'.format(**self._solution)
        
        self._user_conversations = None
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the UserInstance

        :param UserWebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)
        
    def fetch(self):
        """
        Fetch the UserInstance
        

        :returns: The fetched UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, attributes=values.unset, role_sid=values.unset):
        """
        Update the UserInstance
        
        :params UserWebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str friendly_name: The string that you assigned to describe the resource.
        :params str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :params str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Attributes': attributes,
            'RoleSid': role_sid,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return UserInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def user_conversations(self):
        """
        Access the user_conversations

        :returns: twilio.rest.conversations.v1.user.UserConversationList
        :rtype: twilio.rest.conversations.v1.user.UserConversationList
        """
        if self._user_conversations is None:
            self._user_conversations = UserConversationList(self._version, self._solution['sid'],
            )
        return self._user_conversations
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.UserContext {}>'.format(context)

class UserInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the UserInstance
        :returns: twilio.rest.conversations.v1.user.UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'chat_service_sid': payload.get('chat_service_sid'),
            'role_sid': payload.get('role_sid'),
            'identity': payload.get('identity'),
            'friendly_name': payload.get('friendly_name'),
            'attributes': payload.get('attributes'),
            'is_online': payload.get('is_online'),
            'is_notifiable': payload.get('is_notifiable'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserContext
        """
        if self._context is None:
            self._context = UserContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the User resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the User resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def chat_service_sid(self):
        """
        :returns: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
        :rtype: str
        """
        return self._properties['chat_service_sid']
    
    @property
    def role_sid(self):
        """
        :returns: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) assigned to the user.
        :rtype: str
        """
        return self._properties['role_sid']
    
    @property
    def identity(self):
        """
        :returns: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def attributes(self):
        """
        :returns: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def is_online(self):
        """
        :returns: Whether the User is actively connected to this Conversations Service and online. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, if the User has never been online for this Conversations Service, even if the Service's `reachability_enabled` is `true`.
        :rtype: bool
        """
        return self._properties['is_online']
    
    @property
    def is_notifiable(self):
        """
        :returns: Whether the User has a potentially valid Push Notification registration (APN or GCM) for this Conversations Service. If at least one registration exists, `true`; otherwise `false`. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, and if the User has never had a notification registration, even if the Service's `reachability_enabled` is `true`.
        :rtype: bool
        """
        return self._properties['is_notifiable']
    
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
    def url(self):
        """
        :returns: An absolute API resource URL for this user.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the UserInstance
        
        :params UserWebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )
    
    def fetch(self):
        """
        Fetch the UserInstance
        

        :returns: The fetched UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        return self._proxy.fetch()
    
    def update(self, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, attributes=values.unset, role_sid=values.unset):
        """
        Update the UserInstance
        
        :params UserWebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str friendly_name: The string that you assigned to describe the resource.
        :params str attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :params str role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        return self._proxy.update(x_twilio_webhook_enabled=x_twilio_webhook_enabled, friendly_name=friendly_name, attributes=attributes, role_sid=role_sid, )
    
    @property
    def user_conversations(self):
        """
        Access the user_conversations

        :returns: twilio.rest.conversations.v1.user.UserConversationList
        :rtype: twilio.rest.conversations.v1.user.UserConversationList
        """
        return self._proxy.user_conversations
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.UserInstance {}>'.format(context)


