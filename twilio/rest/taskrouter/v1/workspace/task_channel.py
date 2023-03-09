r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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


class TaskChannelList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the TaskChannelList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Task Channel to read.
        
        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/{workspace_sid}/TaskChannels'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, unique_name, channel_optimized_routing=values.unset):
        """
        Create the TaskChannelInstance

        :param str friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
        :param str unique_name: An application-defined string that uniquely identifies the Task Channel, such as `voice` or `sms`.
        :param bool channel_optimized_routing: Whether the Task Channel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.
        
        :returns: The created TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'ChannelOptimizedRouting': channel_optimized_routing,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return TaskChannelInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])

    async def create_async(self, friendly_name, unique_name, channel_optimized_routing=values.unset):
        """
        Asynchronously create the TaskChannelInstance

        :param str friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
        :param str unique_name: An application-defined string that uniquely identifies the Task Channel, such as `voice` or `sms`.
        :param bool channel_optimized_routing: Whether the Task Channel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.
        
        :returns: The created TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'ChannelOptimizedRouting': channel_optimized_routing,
        })
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data,)

        return TaskChannelInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams TaskChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams TaskChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return await self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists TaskChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists TaskChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TaskChannelInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return TaskChannelPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronously retrieve a single page of TaskChannelInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return TaskChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TaskChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return TaskChannelPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of TaskChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return TaskChannelPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a TaskChannelContext
        
        :param sid: The SID of the Task Channel resource to update.
        
        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelContext
        """
        return TaskChannelContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a TaskChannelContext
        
        :param sid: The SID of the Task Channel resource to update.
        
        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelContext
        """
        return TaskChannelContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskChannelList>'










class TaskChannelPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TaskChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        return TaskChannelInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskChannelPage>'




class TaskChannelInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str, sid: str=None):
        """
        Initialize the TaskChannelInstance
        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'workspace_sid': payload.get('workspace_sid'),
            'channel_optimized_routing': payload.get('channel_optimized_routing'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'workspace_sid': workspace_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskChannelContext for this TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelContext
        """
        if self._context is None:
            self._context = TaskChannelContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Task Channel resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
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
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Task Channel resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the Task Channel, such as `voice` or `sms`.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Task Channel.
        :rtype: str
        """
        return self._properties['workspace_sid']
    
    @property
    def channel_optimized_routing(self):
        """
        :returns: Whether the Task Channel will prioritize Workers that have been idle. When `true`, Workers that have been idle the longest are prioritized.
        :rtype: bool
        """
        return self._properties['channel_optimized_routing']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Task Channel resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    
    def delete(self):
        """
        Deletes the TaskChannelInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the TaskChannelInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self):
        """
        Fetch the TaskChannelInstance
        

        :returns: The fetched TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TaskChannelInstance
        

        :returns: The fetched TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, friendly_name=values.unset, channel_optimized_routing=values.unset):
        """
        Update the TaskChannelInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
        :params bool channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.

        :returns: The updated TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        return self._proxy.update(friendly_name=friendly_name, channel_optimized_routing=channel_optimized_routing, )

    async def update_async(self, friendly_name=values.unset, channel_optimized_routing=values.unset):
        """
        Asynchronous coroutine to update the TaskChannelInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
        :params bool channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.

        :returns: The updated TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        return await self._proxy.update_async(friendly_name=friendly_name, channel_optimized_routing=channel_optimized_routing, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskChannelInstance {}>'.format(context)

class TaskChannelContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str, sid: str):
        """
        Initialize the TaskChannelContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Task Channel to update.
        :param sid: The SID of the Task Channel resource to update.

        :returns: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/TaskChannels/{sid}'.format(**self._solution)
        
    
    
    def delete(self):
        """
        Deletes the TaskChannelInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the TaskChannelInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self):
        """
        Fetch the TaskChannelInstance
        

        :returns: The fetched TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TaskChannelInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the TaskChannelInstance
        

        :returns: The fetched TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return TaskChannelInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def update(self, friendly_name=values.unset, channel_optimized_routing=values.unset):
        """
        Update the TaskChannelInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
        :params bool channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.

        :returns: The updated TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'ChannelOptimizedRouting': channel_optimized_routing,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return TaskChannelInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid']
        )

    async def update_async(self, friendly_name=values.unset, channel_optimized_routing=values.unset):
        """
        Asynchronous coroutine to update the TaskChannelInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
        :params bool channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.

        :returns: The updated TaskChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_channel.TaskChannelInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'ChannelOptimizedRouting': channel_optimized_routing,
        })
        

        payload = await self._version.update_async(method='POST', uri=self._uri, data=data,)

        return TaskChannelInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid']
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskChannelContext {}>'.format(context)


