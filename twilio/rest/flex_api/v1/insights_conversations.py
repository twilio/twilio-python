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

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InsightsConversationsInstance(InstanceResource):

    """
    :ivar account_id: The id of the account.
    :ivar conversation_id: The unique id of the conversation
    :ivar segment_count: The count of segments for a conversation
    :ivar segments: The Segments of a conversation
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        
        self.account_id: Optional[str] = payload.get("account_id")
        self.conversation_id: Optional[str] = payload.get("conversation_id")
        self.segment_count: Optional[int] = deserialize.integer(payload.get("segment_count"))
        self.segments: Optional[List[Dict[str, object]]] = payload.get("segments")

        
        
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        
        return '<Twilio.FlexApi.V1.InsightsConversationsInstance>'




class InsightsConversationsPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> InsightsConversationsInstance:
        """
        Build an instance of InsightsConversationsInstance

        :param payload: Payload response from the API
        """
        return InsightsConversationsInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsConversationsPage>"





class InsightsConversationsList(ListResource):
    
    def __init__(self, version: Version):
        """
        Initialize the InsightsConversationsList

        :param version: Version that contains the resource
        
        """
        super().__init__(version)

        
        self._uri = '/Insights/Conversations'
        
        
    
    def stream(self, 
        authorization: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[InsightsConversationsInstance]:
        """
        Streams InsightsConversationsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str authorization: The Authorization HTTP request header
        :param str segment_id: Unique Id of the segment for which conversation details needs to be fetched
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
            authorization=authorization,
            segment_id=segment_id,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        authorization: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[InsightsConversationsInstance]:
        """
        Asynchronously streams InsightsConversationsInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str authorization: The Authorization HTTP request header
        :param str segment_id: Unique Id of the segment for which conversation details needs to be fetched
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
            authorization=authorization,
            segment_id=segment_id,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        authorization: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsConversationsInstance]:
        """
        Lists InsightsConversationsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str authorization: The Authorization HTTP request header
        :param str segment_id: Unique Id of the segment for which conversation details needs to be fetched
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            authorization=authorization,
            segment_id=segment_id,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        authorization: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsConversationsInstance]:
        """
        Asynchronously lists InsightsConversationsInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str authorization: The Authorization HTTP request header
        :param str segment_id: Unique Id of the segment for which conversation details needs to be fetched
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            authorization=authorization,
            segment_id=segment_id,
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        authorization: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InsightsConversationsPage:
        """
        Retrieve a single page of InsightsConversationsInstance records from the API.
        Request is executed immediately
        
        :param authorization: The Authorization HTTP request header
        :param segment_id: Unique Id of the segment for which conversation details needs to be fetched
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsConversationsInstance
        """
        data = values.of({ 
            'Authorization': authorization,
            'SegmentId': segment_id,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return InsightsConversationsPage(self._version, response)

    async def page_async(self, 
        authorization: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InsightsConversationsPage:
        """
        Asynchronously retrieve a single page of InsightsConversationsInstance records from the API.
        Request is executed immediately
        
        :param authorization: The Authorization HTTP request header
        :param segment_id: Unique Id of the segment for which conversation details needs to be fetched
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsConversationsInstance
        """
        data = values.of({ 
            'Authorization': authorization,
            'SegmentId': segment_id,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return InsightsConversationsPage(self._version, response)

    def get_page(self, target_url: str) -> InsightsConversationsPage:
        """
        Retrieve a specific page of InsightsConversationsInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InsightsConversationsInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return InsightsConversationsPage(self._version, response)

    async def get_page_async(self, target_url: str) -> InsightsConversationsPage:
        """
        Asynchronously retrieve a specific page of InsightsConversationsInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InsightsConversationsInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return InsightsConversationsPage(self._version, response)




    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.FlexApi.V1.InsightsConversationsList>'

