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
from twilio.rest.conversations.v1.service.binding import BindingList
from twilio.rest.conversations.v1.service.configuration import ConfigurationList
from twilio.rest.conversations.v1.service.conversation import ConversationList
from twilio.rest.conversations.v1.service.participant_conversation import ParticipantConversationList
from twilio.rest.conversations.v1.service.role import RoleList
from twilio.rest.conversations.v1.service.user import UserList


class ServiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.conversations.v1.service.ServiceList
        :rtype: twilio.rest.conversations.v1.service.ServiceList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the ServiceInstance

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServiceInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return ServiceInstance(self._version, payload)
    
    
    def create(self, friendly_name):
        """
        Create the ServiceInstance

        :param str friendly_name: The human-readable name of this service, limited to 256 characters. Optional.
        
        :returns: The created ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServiceInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ServiceInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ServiceInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.conversations.v1.service.ServiceInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ServiceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.service.ServiceInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServicePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ServicePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServicePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ServicePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.service.ServiceContext
        :rtype: twilio.rest.conversations.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a ServiceContext
        
        :param sid: A 34 character string that uniquely identifies this resource.
        
        :returns: twilio.rest.conversations.v1.service.ServiceContext
        :rtype: twilio.rest.conversations.v1.service.ServiceContext
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ServiceList>'








class ServicePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ServicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.service.ServicePage
        :rtype: twilio.rest.conversations.v1.service.ServicePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ServiceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.service.ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServiceInstance
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.ServicePage>'




class ServiceInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the ServiceInstance
        :returns: twilio.rest.conversations.v1.service.ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServiceInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
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

        :returns: ServiceContext for this ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServiceContext
        """
        if self._context is None:
            self._context = ServiceContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this service.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The human-readable name of this service, limited to 256 characters. Optional.
        :rtype: str
        """
        return self._properties['friendly_name']
    
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
        :returns: An absolute API resource URL for this service.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Contains absolute API resource URLs to access conversations, users, roles, bindings and configuration of this service.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the ServiceInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServiceInstance
        """
        return self._proxy.fetch()
    
    @property
    def bindings(self):
        """
        Access the bindings

        :returns: twilio.rest.conversations.v1.service.BindingList
        :rtype: twilio.rest.conversations.v1.service.BindingList
        """
        return self._proxy.bindings
    
    @property
    def configuration(self):
        """
        Access the configuration

        :returns: twilio.rest.conversations.v1.service.ConfigurationList
        :rtype: twilio.rest.conversations.v1.service.ConfigurationList
        """
        return self._proxy.configuration
    
    @property
    def conversations(self):
        """
        Access the conversations

        :returns: twilio.rest.conversations.v1.service.ConversationList
        :rtype: twilio.rest.conversations.v1.service.ConversationList
        """
        return self._proxy.conversations
    
    @property
    def participant_conversations(self):
        """
        Access the participant_conversations

        :returns: twilio.rest.conversations.v1.service.ParticipantConversationList
        :rtype: twilio.rest.conversations.v1.service.ParticipantConversationList
        """
        return self._proxy.participant_conversations
    
    @property
    def roles(self):
        """
        Access the roles

        :returns: twilio.rest.conversations.v1.service.RoleList
        :rtype: twilio.rest.conversations.v1.service.RoleList
        """
        return self._proxy.roles
    
    @property
    def users(self):
        """
        Access the users

        :returns: twilio.rest.conversations.v1.service.UserList
        :rtype: twilio.rest.conversations.v1.service.UserList
        """
        return self._proxy.users
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.ServiceInstance {}>'.format(context)

class ServiceContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param Version version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.service.ServiceContext
        :rtype: twilio.rest.conversations.v1.service.ServiceContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Services/{sid}'.format(**self._solution)
        
        self._bindings = None
        self._configuration = None
        self._conversations = None
        self._participant_conversations = None
        self._roles = None
        self._users = None
    
    def delete(self):
        """
        Deletes the ServiceInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ServiceInstance
        

        :returns: The fetched ServiceInstance
        :rtype: twilio.rest.conversations.v1.service.ServiceInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    
    @property
    def bindings(self):
        """
        Access the bindings

        :returns: twilio.rest.conversations.v1.service.BindingList
        :rtype: twilio.rest.conversations.v1.service.BindingList
        """
        if self._bindings is None:
            self._bindings = BindingList(self._version, self._solution['sid'],
            )
        return self._bindings
    
    @property
    def configuration(self):
        """
        Access the configuration

        :returns: twilio.rest.conversations.v1.service.ConfigurationList
        :rtype: twilio.rest.conversations.v1.service.ConfigurationList
        """
        if self._configuration is None:
            self._configuration = ConfigurationList(self._version, self._solution['sid'],
            )
        return self._configuration
    
    @property
    def conversations(self):
        """
        Access the conversations

        :returns: twilio.rest.conversations.v1.service.ConversationList
        :rtype: twilio.rest.conversations.v1.service.ConversationList
        """
        if self._conversations is None:
            self._conversations = ConversationList(self._version, self._solution['sid'],
            )
        return self._conversations
    
    @property
    def participant_conversations(self):
        """
        Access the participant_conversations

        :returns: twilio.rest.conversations.v1.service.ParticipantConversationList
        :rtype: twilio.rest.conversations.v1.service.ParticipantConversationList
        """
        if self._participant_conversations is None:
            self._participant_conversations = ParticipantConversationList(self._version, self._solution['sid'],
            )
        return self._participant_conversations
    
    @property
    def roles(self):
        """
        Access the roles

        :returns: twilio.rest.conversations.v1.service.RoleList
        :rtype: twilio.rest.conversations.v1.service.RoleList
        """
        if self._roles is None:
            self._roles = RoleList(self._version, self._solution['sid'],
            )
        return self._roles
    
    @property
    def users(self):
        """
        Access the users

        :returns: twilio.rest.conversations.v1.service.UserList
        :rtype: twilio.rest.conversations.v1.service.UserList
        """
        if self._users is None:
            self._users = UserList(self._version, self._solution['sid'],
            )
        return self._users
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.ServiceContext {}>'.format(context)


