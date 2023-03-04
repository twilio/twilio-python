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


class InviteList(ListResource):

    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        """
        Initialize the InviteList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to read the resources from.
        :param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resources to read belong to.
        
        :returns: twilio.rest.chat.v1.service.channel.invite.InviteList
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid,  }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Invites'.format(**self._solution)
        
        
    
    
    
    def create(self, identity, role_sid=values.unset):
        """
        Create the InviteInstance

        :param str identity: The `identity` value that uniquely identifies the new resource's [User](https://www.twilio.com/docs/api/chat/rest/v1/user) within the [Service](https://www.twilio.com/docs/api/chat/rest/v1/service). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more info.
        :param str role_sid: The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the new member.
        
        :returns: The created InviteInstance
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteInstance
        """
        data = values.of({ 
            'Identity': identity,
            'RoleSid': role_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return InviteInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])
    
    
    def stream(self, identity=values.unset, limit=None, page_size=None):
        """
        Streams InviteInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[str] identity: The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s `identity` value of the resources to read. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.channel.invite.InviteInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            identity=identity,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, identity=values.unset, limit=None, page_size=None):
        """
        Lists InviteInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[str] identity: The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s `identity` value of the resources to read. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.chat.v1.service.channel.invite.InviteInstance]
        """
        return list(self.stream(
            identity=identity,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, identity=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of InviteInstance records from the API.
        Request is executed immediately
        
        :param list[str] identity: The [User](https://www.twilio.com/docs/api/chat/rest/v1/user)'s `identity` value of the resources to read. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more details.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InviteInstance
        :rtype: twilio.rest.chat.v1.service.channel.invite.InvitePage
        """
        data = values.of({ 
            'Identity': serialize.map(identity, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return InvitePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InviteInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InviteInstance
        :rtype: twilio.rest.chat.v1.service.channel.invite.InvitePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return InvitePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a InviteContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Invite resource to fetch.
        
        :returns: twilio.rest.chat.v1.service.channel.invite.InviteContext
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteContext
        """
        return InviteContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a InviteContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Invite resource to fetch.
        
        :returns: twilio.rest.chat.v1.service.channel.invite.InviteContext
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteContext
        """
        return InviteContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V1.InviteList>'








class InvitePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the InvitePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.chat.v1.service.channel.invite.InvitePage
        :rtype: twilio.rest.chat.v1.service.channel.invite.InvitePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InviteInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v1.service.channel.invite.InviteInstance
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteInstance
        """
        return InviteInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V1.InvitePage>'




class InviteInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, channel_sid: str, sid: str=None):
        """
        Initialize the InviteInstance
        :returns: twilio.rest.chat.v1.service.channel.invite.InviteInstance
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'channel_sid': payload.get('channel_sid'),
            'service_sid': payload.get('service_sid'),
            'identity': payload.get('identity'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'role_sid': payload.get('role_sid'),
            'created_by': payload.get('created_by'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InviteContext for this InviteInstance
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteContext
        """
        if self._context is None:
            self._context = InviteContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Invite resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the Invite resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def channel_sid(self):
        """
        :returns: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource belongs to.
        :rtype: str
        """
        return self._properties['channel_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def identity(self):
        """
        :returns: The application-defined string that uniquely identifies the resource's [User](https://www.twilio.com/docs/api/chat/rest/users) within the [Service](https://www.twilio.com/docs/api/chat/rest/services). See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more info.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def role_sid(self):
        """
        :returns: The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the resource.
        :rtype: str
        """
        return self._properties['role_sid']
    
    @property
    def created_by(self):
        """
        :returns: The `identity` of the User that created the invite.
        :rtype: str
        """
        return self._properties['created_by']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Invite resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the InviteInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the InviteInstance
        

        :returns: The fetched InviteInstance
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V1.InviteInstance {}>'.format(context)

class InviteContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        """
        Initialize the InviteContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) to fetch the resource from.:param channel_sid: The SID of the [Channel](https://www.twilio.com/docs/api/chat/rest/channels) the resource to fetch belongs to.:param sid: The Twilio-provided string that uniquely identifies the Invite resource to fetch.

        :returns: twilio.rest.chat.v1.service.channel.invite.InviteContext
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'channel_sid': channel_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{channel_sid}/Invites/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the InviteInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the InviteInstance
        

        :returns: The fetched InviteInstance
        :rtype: twilio.rest.chat.v1.service.channel.invite.InviteInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return InviteInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            channel_sid=self._solution['channel_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V1.InviteContext {}>'.format(context)


