r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
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
from twilio.rest.ip_messaging.v2.service.channel.invite import InviteList
from twilio.rest.ip_messaging.v2.service.channel.member import MemberList
from twilio.rest.ip_messaging.v2.service.channel.message import MessageList
from twilio.rest.ip_messaging.v2.service.channel.webhook import WebhookList


class ChannelList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the ChannelList

        :param Version version: Version that contains the resource
        :param service_sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.channel.ChannelList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Channels'.format(**self._solution)
        
        
    
    
    
    
    def create(self, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, unique_name=values.unset, attributes=values.unset, type=values.unset, date_created=values.unset, date_updated=values.unset, created_by=values.unset):
        """
        Create the ChannelInstance

        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: 
        :param str unique_name: 
        :param str attributes: 
        :param ChannelInstance.ChannelType type: 
        :param datetime date_created: 
        :param datetime date_updated: 
        :param str created_by: 
        
        :returns: The created ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Attributes': attributes,
            'Type': type,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'CreatedBy': created_by,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'])

    async def create_async(self, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, unique_name=values.unset, attributes=values.unset, type=values.unset, date_created=values.unset, date_updated=values.unset, created_by=values.unset):
        """
        Asynchronous coroutine to create the ChannelInstance

        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param str friendly_name: 
        :param str unique_name: 
        :param str attributes: 
        :param ChannelInstance.ChannelType type: 
        :param datetime date_created: 
        :param datetime date_updated: 
        :param str created_by: 
        
        :returns: The created ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Attributes': attributes,
            'Type': type,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'CreatedBy': created_by,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, type=values.unset, limit=None, page_size=None):
        """
        Streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[ChannelInstance.ChannelType] type: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.channel.ChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            type=type,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, type=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param list[ChannelInstance.ChannelType] type: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.channel.ChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            type=type,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, type=values.unset, limit=None, page_size=None):
        """
        Lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[ChannelInstance.ChannelType] type: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.channel.ChannelInstance]
        """
        return list(self.stream(
            type=type,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, type=values.unset, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param list[ChannelInstance.ChannelType] type: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.channel.ChannelInstance]
        """
        return list(await self.stream_async(
            type=type,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, type=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately
        
        :param list[ChannelInstance.ChannelType] type: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelPage
        """
        data = values.of({ 
            'Type': serialize.map(type, lambda e: e),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ChannelPage(self._version, response, self._solution)

    async def page_async(self, type=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately
        
        :param list[ChannelInstance.ChannelType] type: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelPage
        """
        data = values.of({ 
            'Type': serialize.map(type),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return ChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ChannelPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return ChannelPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ChannelContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.channel.ChannelContext
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelContext
        """
        return ChannelContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ChannelContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.channel.ChannelContext
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelContext
        """
        return ChannelContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.ChannelList>'










class ChannelPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.ip_messaging.v2.service.channel.ChannelPage
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        return ChannelInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.ChannelPage>'




class ChannelInstance(InstanceResource):

    class ChannelType(object):
        PUBLIC = "public"
        PRIVATE = "private"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the ChannelInstance
        :returns: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'friendly_name': payload.get('friendly_name'),
            'unique_name': payload.get('unique_name'),
            'attributes': payload.get('attributes'),
            'type': payload.get('type'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'created_by': payload.get('created_by'),
            'members_count': deserialize.integer(payload.get('members_count')),
            'messages_count': deserialize.integer(payload.get('messages_count')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ChannelContext for this ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelContext
        """
        if self._context is None:
            self._context = ChannelContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def unique_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def attributes(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def type(self):
        """
        :returns: 
        :rtype: ChannelInstance.ChannelType
        """
        return self._properties['type']
    
    @property
    def date_created(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def created_by(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['created_by']
    
    @property
    def members_count(self):
        """
        :returns: 
        :rtype: int
        """
        return self._properties['members_count']
    
    @property
    def messages_count(self):
        """
        :returns: 
        :rtype: int
        """
        return self._properties['messages_count']
    
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
    
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the ChannelInstance
        
        :params ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )
    async def delete_async(self, x_twilio_webhook_enabled=values.unset):
        """
        Asynchronous coroutine that deletes the ChannelInstance
        
        :params ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )
    
    
    def fetch(self):
        """
        Fetch the ChannelInstance
        

        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ChannelInstance
        

        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, unique_name=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, created_by=values.unset):
        """
        Update the ChannelInstance
        
        :params ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str friendly_name: 
        :params str unique_name: 
        :params str attributes: 
        :params datetime date_created: 
        :params datetime date_updated: 
        :params str created_by: 

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        return self._proxy.update(x_twilio_webhook_enabled=x_twilio_webhook_enabled, friendly_name=friendly_name, unique_name=unique_name, attributes=attributes, date_created=date_created, date_updated=date_updated, created_by=created_by, )

    async def update_async(self, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, unique_name=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, created_by=values.unset):
        """
        Asynchronous coroutine to update the ChannelInstance
        
        :params ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str friendly_name: 
        :params str unique_name: 
        :params str attributes: 
        :params datetime date_created: 
        :params datetime date_updated: 
        :params str created_by: 

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        return await self._proxy.update_async(x_twilio_webhook_enabled=x_twilio_webhook_enabled, friendly_name=friendly_name, unique_name=unique_name, attributes=attributes, date_created=date_created, date_updated=date_updated, created_by=created_by, )
    
    @property
    def invites(self):
        """
        Access the invites

        :returns: twilio.rest.ip_messaging.v2.service.channel.InviteList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.InviteList
        """
        return self._proxy.invites
    
    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.ip_messaging.v2.service.channel.MemberList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.MemberList
        """
        return self._proxy.members
    
    @property
    def messages(self):
        """
        Access the messages

        :returns: twilio.rest.ip_messaging.v2.service.channel.MessageList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.MessageList
        """
        return self._proxy.messages
    
    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.ip_messaging.v2.service.channel.WebhookList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.WebhookList
        """
        return self._proxy.webhooks
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.ChannelInstance {}>'.format(context)

class ChannelContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the ChannelContext

        :param Version version: Version that contains the resource
        :param service_sid: 
        :param sid: 

        :returns: twilio.rest.ip_messaging.v2.service.channel.ChannelContext
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Channels/{sid}'.format(**self._solution)
        
        self._invites = None
        self._members = None
        self._messages = None
        self._webhooks = None
    
    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the ChannelInstance

        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)
        
    def fetch(self):
        """
        Fetch the ChannelInstance
        

        :returns: The fetched ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, x_twilio_webhook_enabled=values.unset, friendly_name=values.unset, unique_name=values.unset, attributes=values.unset, date_created=values.unset, date_updated=values.unset, created_by=values.unset):
        """
        Update the ChannelInstance
        
        :params ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :params str friendly_name: 
        :params str unique_name: 
        :params str attributes: 
        :params datetime date_created: 
        :params datetime date_updated: 
        :params str created_by: 

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.ip_messaging.v2.service.channel.ChannelInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Attributes': attributes,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'CreatedBy': created_by,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def invites(self):
        """
        Access the invites

        :returns: twilio.rest.ip_messaging.v2.service.channel.InviteList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.InviteList
        """
        if self._invites is None:
            self._invites = InviteList(
                self._version, 
                self._solution['service_sid'],
                self._solution['sid'],
            )
        return self._invites
    
    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.ip_messaging.v2.service.channel.MemberList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.MemberList
        """
        if self._members is None:
            self._members = MemberList(
                self._version, 
                self._solution['service_sid'],
                self._solution['sid'],
            )
        return self._members
    
    @property
    def messages(self):
        """
        Access the messages

        :returns: twilio.rest.ip_messaging.v2.service.channel.MessageList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.MessageList
        """
        if self._messages is None:
            self._messages = MessageList(
                self._version, 
                self._solution['service_sid'],
                self._solution['sid'],
            )
        return self._messages
    
    @property
    def webhooks(self):
        """
        Access the webhooks

        :returns: twilio.rest.ip_messaging.v2.service.channel.WebhookList
        :rtype: twilio.rest.ip_messaging.v2.service.channel.WebhookList
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(
                self._version, 
                self._solution['service_sid'],
                self._solution['sid'],
            )
        return self._webhooks
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.ChannelContext {}>'.format(context)


