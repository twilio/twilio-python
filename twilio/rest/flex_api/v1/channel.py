r"""
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


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ChannelInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Channel resource and owns this Workflow.
    :ivar flex_flow_sid: The SID of the Flex Flow.
    :ivar sid: The unique string that we created to identify the Channel resource.
    :ivar user_sid: The SID of the chat user.
    :ivar task_sid: The SID of the TaskRouter Task. Only valid when integration type is `task`. `null` for integration types `studio` & `external`
    :ivar url: The absolute URL of the Flex chat channel resource.
    :ivar date_created: The date and time in GMT when the Flex chat channel was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Flex chat channel was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None):
        super().__init__(version)

        
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.flex_flow_sid: Optional[str] = payload.get("flex_flow_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.user_sid: Optional[str] = payload.get("user_sid")
        self.task_sid: Optional[str] = payload.get("task_sid")
        self.url: Optional[str] = payload.get("url")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_created"))
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_updated"))

        
        self._solution = { 
            "sid": sid or self.sid,
        }
        self._context: Optional[ChannelContext] = None

    @property
    def _proxy(self) -> "ChannelContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ChannelContext for this ChannelInstance
        """
        if self._context is None:
            self._context = ChannelContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    
    def delete(self) -> bool:
        """
        Deletes the ChannelInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()
    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ChannelInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self) -> "ChannelInstance":
        """
        Fetch the ChannelInstance
        

        :returns: The fetched ChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ChannelInstance":
        """
        Asynchronous coroutine to fetch the ChannelInstance
        

        :returns: The fetched ChannelInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.ChannelInstance {}>'.format(context)

class ChannelContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the ChannelContext

        :param version: Version that contains the resource
        :param sid: The SID of the Flex chat channel resource to fetch.
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Channels/{sid}'.format(**self._solution)
        
    
    
    def delete(self) -> bool:
        """
        Deletes the ChannelInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ChannelInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self) -> ChannelInstance:
        """
        Fetch the ChannelInstance
        

        :returns: The fetched ChannelInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ChannelInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> ChannelInstance:
        """
        Asynchronous coroutine to fetch the ChannelInstance
        

        :returns: The fetched ChannelInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return ChannelInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.ChannelContext {}>'.format(context)









class ChannelPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> ChannelInstance:
        """
        Build an instance of ChannelInstance

        :param payload: Payload response from the API
        """
        return ChannelInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.ChannelPage>"





class ChannelList(ListResource):
    
    def __init__(self, version: Version):
        """
        Initialize the ChannelList

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/Channels'
        
        
    
    
    
    def create(self, flex_flow_sid: str, identity: str, chat_user_friendly_name: str, chat_friendly_name: str, target: Union[str, object]=values.unset, chat_unique_name: Union[str, object]=values.unset, pre_engagement_data: Union[str, object]=values.unset, task_sid: Union[str, object]=values.unset, task_attributes: Union[str, object]=values.unset, long_lived: Union[bool, object]=values.unset) -> ChannelInstance:
        """
        Create the ChannelInstance

        :param flex_flow_sid: The SID of the Flex Flow.
        :param identity: The `identity` value that uniquely identifies the new resource's chat User.
        :param chat_user_friendly_name: The chat participant's friendly name.
        :param chat_friendly_name: The chat channel's friendly name.
        :param target: The Target Contact Identity, for example the phone number of an SMS.
        :param chat_unique_name: The chat channel's unique name.
        :param pre_engagement_data: The pre-engagement data.
        :param task_sid: The SID of the TaskRouter Task. Only valid when integration type is `task`. `null` for integration types `studio` & `external`
        :param task_attributes: The Task attributes to be added for the TaskRouter Task.
        :param long_lived: Whether to create the channel as long-lived.
        
        :returns: The created ChannelInstance
        """
        
        data = values.of({ 
            'FlexFlowSid': flex_flow_sid,
            'Identity': identity,
            'ChatUserFriendlyName': chat_user_friendly_name,
            'ChatFriendlyName': chat_friendly_name,
            'Target': target,
            'ChatUniqueName': chat_unique_name,
            'PreEngagementData': pre_engagement_data,
            'TaskSid': task_sid,
            'TaskAttributes': task_attributes,
            'LongLived': serialize.boolean_to_string(long_lived),
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return ChannelInstance(self._version, payload)

    async def create_async(self, flex_flow_sid: str, identity: str, chat_user_friendly_name: str, chat_friendly_name: str, target: Union[str, object]=values.unset, chat_unique_name: Union[str, object]=values.unset, pre_engagement_data: Union[str, object]=values.unset, task_sid: Union[str, object]=values.unset, task_attributes: Union[str, object]=values.unset, long_lived: Union[bool, object]=values.unset) -> ChannelInstance:
        """
        Asynchronously create the ChannelInstance

        :param flex_flow_sid: The SID of the Flex Flow.
        :param identity: The `identity` value that uniquely identifies the new resource's chat User.
        :param chat_user_friendly_name: The chat participant's friendly name.
        :param chat_friendly_name: The chat channel's friendly name.
        :param target: The Target Contact Identity, for example the phone number of an SMS.
        :param chat_unique_name: The chat channel's unique name.
        :param pre_engagement_data: The pre-engagement data.
        :param task_sid: The SID of the TaskRouter Task. Only valid when integration type is `task`. `null` for integration types `studio` & `external`
        :param task_attributes: The Task attributes to be added for the TaskRouter Task.
        :param long_lived: Whether to create the channel as long-lived.
        
        :returns: The created ChannelInstance
        """
        
        data = values.of({ 
            'FlexFlowSid': flex_flow_sid,
            'Identity': identity,
            'ChatUserFriendlyName': chat_user_friendly_name,
            'ChatFriendlyName': chat_friendly_name,
            'Target': target,
            'ChatUniqueName': chat_unique_name,
            'PreEngagementData': pre_engagement_data,
            'TaskSid': task_sid,
            'TaskAttributes': task_attributes,
            'LongLived': serialize.boolean_to_string(long_lived),
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return ChannelInstance(self._version, payload)
    
    
    def stream(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ChannelInstance]:
        """
        Streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ChannelInstance]:
        """
        Asynchronously streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ChannelInstance]:
        """
        Lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ChannelInstance]:
        """
        Asynchronously lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ChannelPage:
        """
        Retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately
        
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ChannelPage(self._version, response)

    async def page_async(self, 
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ChannelPage:
        """
        Asynchronously retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately
        
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return ChannelPage(self._version, response)

    def get_page(self, target_url: str) -> ChannelPage:
        """
        Retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ChannelPage(self._version, response)

    async def get_page_async(self, target_url: str) -> ChannelPage:
        """
        Asynchronously retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return ChannelPage(self._version, response)



    def get(self, sid: str) -> ChannelContext:
        """
        Constructs a ChannelContext
        
        :param sid: The SID of the Flex chat channel resource to fetch.
        """
        return ChannelContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ChannelContext:
        """
        Constructs a ChannelContext
        
        :param sid: The SID of the Flex chat channel resource to fetch.
        """
        return ChannelContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.FlexApi.V1.ChannelList>'

