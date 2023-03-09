"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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
from twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_invite import InteractionChannelInviteList
from twilio.rest.flex_api.v1.interaction.interaction_channel.interaction_channel_participant import InteractionChannelParticipantList


class InteractionChannelList(ListResource):

    def __init__(self, version: Version, interaction_sid: str):
        """
        Initialize the InteractionChannelList

        :param Version version: Version that contains the resource
        :param interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
        
        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'interaction_sid': interaction_sid,  }
        self._uri = '/Interactions/{interaction_sid}/Channels'.format(**self._solution)
        
        
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams InteractionChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists InteractionChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of InteractionChannelInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return InteractionChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InteractionChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return InteractionChannelPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a InteractionChannelContext
        
        :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        
        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        """
        return InteractionChannelContext(self._version, interaction_sid=self._solution['interaction_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a InteractionChannelContext
        
        :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        
        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        """
        return InteractionChannelContext(self._version, interaction_sid=self._solution['interaction_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InteractionChannelList>'






class InteractionChannelPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the InteractionChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelPage
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InteractionChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        """
        return InteractionChannelInstance(self._version, payload, interaction_sid=self._solution['interaction_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InteractionChannelPage>'




class InteractionChannelInstance(InstanceResource):

    class ChannelStatus(object):
        SETUP = "setup"
        ACTIVE = "active"
        FAILED = "failed"
        CLOSED = "closed"

    class Type(object):
        VOICE = "voice"
        SMS = "sms"
        EMAIL = "email"
        WEB = "web"
        WHATSAPP = "whatsapp"
        CHAT = "chat"
        MESSENGER = "messenger"
        GBM = "gbm"

    def __init__(self, version, payload, interaction_sid: str, sid: str=None):
        """
        Initialize the InteractionChannelInstance
        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'interaction_sid': payload.get('interaction_sid'),
            'type': payload.get('type'),
            'status': payload.get('status'),
            'error_code': deserialize.integer(payload.get('error_code')),
            'error_message': payload.get('error_message'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'interaction_sid': interaction_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InteractionChannelContext for this InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        """
        if self._context is None:
            self._context = InteractionChannelContext(self._version, interaction_sid=self._solution['interaction_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def interaction_sid(self):
        """
        :returns: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
        :rtype: str
        """
        return self._properties['interaction_sid']
    
    @property
    def type(self):
        """
        :returns: 
        :rtype: InteractionChannelInstance.Type
        """
        return self._properties['type']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: InteractionChannelInstance.ChannelStatus
        """
        return self._properties['status']
    
    @property
    def error_code(self):
        """
        :returns: The Twilio error code for a failed channel.
        :rtype: int
        """
        return self._properties['error_code']
    
    @property
    def error_message(self):
        """
        :returns: The error message for a failed channel.
        :rtype: str
        """
        return self._properties['error_message']
    
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
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    def fetch(self):
        """
        Fetch the InteractionChannelInstance
        

        :returns: The fetched InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        """
        return self._proxy.fetch()
    
    def update(self, status, routing=values.unset):
        """
        Update the InteractionChannelInstance
        
        :params InteractionChannelInstance.Status status: 
        :params object routing: Optional. The state of associated tasks. If not specified, all tasks will be set to `wrapping`.

        :returns: The updated InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        """
        return self._proxy.update(status=status, routing=routing, )
    
    @property
    def invites(self):
        """
        Access the invites

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInviteList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInviteList
        """
        return self._proxy.invites
    
    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelParticipantList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelParticipantList
        """
        return self._proxy.participants
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InteractionChannelInstance {}>'.format(context)

class InteractionChannelContext(InstanceContext):

    def __init__(self, version: Version, interaction_sid: str, sid: str):
        """
        Initialize the InteractionChannelContext

        :param Version version: Version that contains the resource
        :param interaction_sid: The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
        :param sid: The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'interaction_sid': interaction_sid,
            'sid': sid,
        }
        self._uri = '/Interactions/{interaction_sid}/Channels/{sid}'.format(**self._solution)
        
        self._invites = None
        self._participants = None
    
    def fetch(self):
        """
        Fetch the InteractionChannelInstance
        

        :returns: The fetched InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return InteractionChannelInstance(
            self._version,
            payload,
            interaction_sid=self._solution['interaction_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, status, routing=values.unset):
        """
        Update the InteractionChannelInstance
        
        :params InteractionChannelInstance.Status status: 
        :params object routing: Optional. The state of associated tasks. If not specified, all tasks will be set to `wrapping`.

        :returns: The updated InteractionChannelInstance
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInstance
        """
        data = values.of({ 
            'Status': status,
            'Routing': serialize.object(routing),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return InteractionChannelInstance(
            self._version,
            payload,
            interaction_sid=self._solution['interaction_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def invites(self):
        """
        Access the invites

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInviteList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelInviteList
        """
        if self._invites is None:
            self._invites = InteractionChannelInviteList(
                self._version, 
                self._solution['interaction_sid'],
                self._solution['sid'],
            )
        return self._invites
    
    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelParticipantList
        :rtype: twilio.rest.flex_api.v1.interaction.interaction_channel.InteractionChannelParticipantList
        """
        if self._participants is None:
            self._participants = InteractionChannelParticipantList(
                self._version, 
                self._solution['interaction_sid'],
                self._solution['sid'],
            )
        return self._participants
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InteractionChannelContext {}>'.format(context)


