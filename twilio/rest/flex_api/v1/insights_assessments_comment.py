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


from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InsightsAssessmentsCommentInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
    :ivar assessment_id: The unique ID of the assessment.
    :ivar comment: The comment added for assessment.
    :ivar offset: The offset
    :ivar report: The flag indicating if this assessment is part of report
    :ivar weight: The weightage given to this comment
    :ivar agent_id: The id of the agent.
    :ivar segment_id: The id of the segment.
    :ivar user_name: The name of the user.
    :ivar user_email: The email id of the user.
    :ivar timestamp: The timestamp when the record is inserted
    :ivar url:
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.assessment_id: Optional[str] = payload.get("assessment_id")
        self.comment: Optional[Dict[str, object]] = payload.get("comment")
        self.offset: Optional[float] = deserialize.decimal(payload.get("offset"))
        self.report: Optional[bool] = payload.get("report")
        self.weight: Optional[float] = deserialize.decimal(payload.get("weight"))
        self.agent_id: Optional[str] = payload.get("agent_id")
        self.segment_id: Optional[str] = payload.get("segment_id")
        self.user_name: Optional[str] = payload.get("user_name")
        self.user_email: Optional[str] = payload.get("user_email")
        self.timestamp: Optional[float] = deserialize.decimal(payload.get("timestamp"))
        self.url: Optional[str] = payload.get("url")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.FlexApi.V1.InsightsAssessmentsCommentInstance>"


class InsightsAssessmentsCommentPage(Page):
    def get_instance(
        self, payload: Dict[str, Any]
    ) -> InsightsAssessmentsCommentInstance:
        """
        Build an instance of InsightsAssessmentsCommentInstance

        :param payload: Payload response from the API
        """
        return InsightsAssessmentsCommentInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsAssessmentsCommentPage>"


class InsightsAssessmentsCommentList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InsightsAssessmentsCommentList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Insights/QM/Assessments/Comments"

    def create(
        self,
        category_id: str,
        category_name: str,
        comment: str,
        segment_id: str,
        user_name: str,
        user_email: str,
        agent_id: str,
        offset: float,
        token: Union[str, object] = values.unset,
    ) -> InsightsAssessmentsCommentInstance:
        """
        Create the InsightsAssessmentsCommentInstance

        :param category_id: The ID of the category
        :param category_name: The name of the category
        :param comment: The Assessment comment.
        :param segment_id: The id of the segment.
        :param user_name: The name of the user.
        :param user_email: The email id of the user.
        :param agent_id: The id of the agent.
        :param offset: The offset
        :param token: The Token HTTP request header

        :returns: The created InsightsAssessmentsCommentInstance
        """
        data = values.of(
            {
                "CategoryId": category_id,
                "CategoryName": category_name,
                "Comment": comment,
                "SegmentId": segment_id,
                "UserName": user_name,
                "UserEmail": user_email,
                "AgentId": agent_id,
                "Offset": offset,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsAssessmentsCommentInstance(self._version, payload)

    async def create_async(
        self,
        category_id: str,
        category_name: str,
        comment: str,
        segment_id: str,
        user_name: str,
        user_email: str,
        agent_id: str,
        offset: float,
        token: Union[str, object] = values.unset,
    ) -> InsightsAssessmentsCommentInstance:
        """
        Asynchronously create the InsightsAssessmentsCommentInstance

        :param category_id: The ID of the category
        :param category_name: The name of the category
        :param comment: The Assessment comment.
        :param segment_id: The id of the segment.
        :param user_name: The name of the user.
        :param user_email: The email id of the user.
        :param agent_id: The id of the agent.
        :param offset: The offset
        :param token: The Token HTTP request header

        :returns: The created InsightsAssessmentsCommentInstance
        """
        data = values.of(
            {
                "CategoryId": category_id,
                "CategoryName": category_name,
                "Comment": comment,
                "SegmentId": segment_id,
                "UserName": user_name,
                "UserEmail": user_email,
                "AgentId": agent_id,
                "Offset": offset,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsAssessmentsCommentInstance(self._version, payload)

    def stream(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        agent_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsAssessmentsCommentInstance]:
        """
        Streams InsightsAssessmentsCommentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
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
            token=token,
            segment_id=segment_id,
            agent_id=agent_id,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        agent_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsAssessmentsCommentInstance]:
        """
        Asynchronously streams InsightsAssessmentsCommentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
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
            token=token,
            segment_id=segment_id,
            agent_id=agent_id,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        agent_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsAssessmentsCommentInstance]:
        """
        Lists InsightsAssessmentsCommentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            self.stream(
                token=token,
                segment_id=segment_id,
                agent_id=agent_id,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        agent_id: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsAssessmentsCommentInstance]:
        """
        Asynchronously lists InsightsAssessmentsCommentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
        :param str segment_id: The id of the segment.
        :param str agent_id: The id of the agent.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                token=token,
                segment_id=segment_id,
                agent_id=agent_id,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        agent_id: Union[str, object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> InsightsAssessmentsCommentPage:
        """
        Retrieve a single page of InsightsAssessmentsCommentInstance records from the API.
        Request is executed immediately

        :param token: The Token HTTP request header
        :param segment_id: The id of the segment.
        :param agent_id: The id of the agent.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsAssessmentsCommentInstance
        """
        data = values.of(
            {
                "Token": token,
                "SegmentId": segment_id,
                "AgentId": agent_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InsightsAssessmentsCommentPage(self._version, response)

    async def page_async(
        self,
        token: Union[str, object] = values.unset,
        segment_id: Union[str, object] = values.unset,
        agent_id: Union[str, object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> InsightsAssessmentsCommentPage:
        """
        Asynchronously retrieve a single page of InsightsAssessmentsCommentInstance records from the API.
        Request is executed immediately

        :param token: The Token HTTP request header
        :param segment_id: The id of the segment.
        :param agent_id: The id of the agent.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsAssessmentsCommentInstance
        """
        data = values.of(
            {
                "Token": token,
                "SegmentId": segment_id,
                "AgentId": agent_id,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return InsightsAssessmentsCommentPage(self._version, response)

    def get_page(self, target_url: str) -> InsightsAssessmentsCommentPage:
        """
        Retrieve a specific page of InsightsAssessmentsCommentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InsightsAssessmentsCommentInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InsightsAssessmentsCommentPage(self._version, response)

    async def get_page_async(self, target_url: str) -> InsightsAssessmentsCommentPage:
        """
        Asynchronously retrieve a specific page of InsightsAssessmentsCommentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InsightsAssessmentsCommentInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InsightsAssessmentsCommentPage(self._version, response)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsAssessmentsCommentList>"
