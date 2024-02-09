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

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class WebChannelInstance(InstanceResource):
    class ChatStatus(object):
        INACTIVE = "inactive"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the WebChannel resource and owns this Workflow.
    :ivar flex_flow_sid: The SID of the Flex Flow.
    :ivar sid: The unique string that we created to identify the WebChannel resource.
    :ivar url: The absolute URL of the WebChannel resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.flex_flow_sid: Optional[str] = payload.get("flex_flow_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.url: Optional[str] = payload.get("url")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[WebChannelContext] = None

    @property
    def _proxy(self) -> "WebChannelContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WebChannelContext for this WebChannelInstance
        """
        if self._context is None:
            self._context = WebChannelContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the WebChannelInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the WebChannelInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "WebChannelInstance":
        """
        Fetch the WebChannelInstance


        :returns: The fetched WebChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "WebChannelInstance":
        """
        Asynchronous coroutine to fetch the WebChannelInstance


        :returns: The fetched WebChannelInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        chat_status: Union["WebChannelInstance.ChatStatus", object] = values.unset,
        post_engagement_data: Union[str, object] = values.unset,
    ) -> "WebChannelInstance":
        """
        Update the WebChannelInstance

        :param chat_status:
        :param post_engagement_data: The post-engagement data.

        :returns: The updated WebChannelInstance
        """
        return self._proxy.update(
            chat_status=chat_status,
            post_engagement_data=post_engagement_data,
        )

    async def update_async(
        self,
        chat_status: Union["WebChannelInstance.ChatStatus", object] = values.unset,
        post_engagement_data: Union[str, object] = values.unset,
    ) -> "WebChannelInstance":
        """
        Asynchronous coroutine to update the WebChannelInstance

        :param chat_status:
        :param post_engagement_data: The post-engagement data.

        :returns: The updated WebChannelInstance
        """
        return await self._proxy.update_async(
            chat_status=chat_status,
            post_engagement_data=post_engagement_data,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.WebChannelInstance {}>".format(context)


class WebChannelContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the WebChannelContext

        :param version: Version that contains the resource
        :param sid: The SID of the WebChannel resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/WebChannels/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the WebChannelInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the WebChannelInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> WebChannelInstance:
        """
        Fetch the WebChannelInstance


        :returns: The fetched WebChannelInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return WebChannelInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> WebChannelInstance:
        """
        Asynchronous coroutine to fetch the WebChannelInstance


        :returns: The fetched WebChannelInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return WebChannelInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        chat_status: Union["WebChannelInstance.ChatStatus", object] = values.unset,
        post_engagement_data: Union[str, object] = values.unset,
    ) -> WebChannelInstance:
        """
        Update the WebChannelInstance

        :param chat_status:
        :param post_engagement_data: The post-engagement data.

        :returns: The updated WebChannelInstance
        """
        data = values.of(
            {
                "ChatStatus": chat_status,
                "PostEngagementData": post_engagement_data,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebChannelInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        chat_status: Union["WebChannelInstance.ChatStatus", object] = values.unset,
        post_engagement_data: Union[str, object] = values.unset,
    ) -> WebChannelInstance:
        """
        Asynchronous coroutine to update the WebChannelInstance

        :param chat_status:
        :param post_engagement_data: The post-engagement data.

        :returns: The updated WebChannelInstance
        """
        data = values.of(
            {
                "ChatStatus": chat_status,
                "PostEngagementData": post_engagement_data,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebChannelInstance(self._version, payload, sid=self._solution["sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.WebChannelContext {}>".format(context)


class WebChannelPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> WebChannelInstance:
        """
        Build an instance of WebChannelInstance

        :param payload: Payload response from the API
        """
        return WebChannelInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.WebChannelPage>"


class WebChannelList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the WebChannelList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/WebChannels"

    def create(
        self,
        flex_flow_sid: str,
        identity: str,
        customer_friendly_name: str,
        chat_friendly_name: str,
        chat_unique_name: Union[str, object] = values.unset,
        pre_engagement_data: Union[str, object] = values.unset,
    ) -> WebChannelInstance:
        """
        Create the WebChannelInstance

        :param flex_flow_sid: The SID of the Flex Flow.
        :param identity: The chat identity.
        :param customer_friendly_name: The chat participant's friendly name.
        :param chat_friendly_name: The chat channel's friendly name.
        :param chat_unique_name: The chat channel's unique name.
        :param pre_engagement_data: The pre-engagement data.

        :returns: The created WebChannelInstance
        """
        data = values.of(
            {
                "FlexFlowSid": flex_flow_sid,
                "Identity": identity,
                "CustomerFriendlyName": customer_friendly_name,
                "ChatFriendlyName": chat_friendly_name,
                "ChatUniqueName": chat_unique_name,
                "PreEngagementData": pre_engagement_data,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebChannelInstance(self._version, payload)

    async def create_async(
        self,
        flex_flow_sid: str,
        identity: str,
        customer_friendly_name: str,
        chat_friendly_name: str,
        chat_unique_name: Union[str, object] = values.unset,
        pre_engagement_data: Union[str, object] = values.unset,
    ) -> WebChannelInstance:
        """
        Asynchronously create the WebChannelInstance

        :param flex_flow_sid: The SID of the Flex Flow.
        :param identity: The chat identity.
        :param customer_friendly_name: The chat participant's friendly name.
        :param chat_friendly_name: The chat channel's friendly name.
        :param chat_unique_name: The chat channel's unique name.
        :param pre_engagement_data: The pre-engagement data.

        :returns: The created WebChannelInstance
        """
        data = values.of(
            {
                "FlexFlowSid": flex_flow_sid,
                "Identity": identity,
                "CustomerFriendlyName": customer_friendly_name,
                "ChatFriendlyName": chat_friendly_name,
                "ChatUniqueName": chat_unique_name,
                "PreEngagementData": pre_engagement_data,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebChannelInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[WebChannelInstance]:
        """
        Streams WebChannelInstance records from the API as a generator stream.
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
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[WebChannelInstance]:
        """
        Asynchronously streams WebChannelInstance records from the API as a generator stream.
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
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[WebChannelInstance]:
        """
        Lists WebChannelInstance records from the API as a list.
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
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[WebChannelInstance]:
        """
        Asynchronously lists WebChannelInstance records from the API as a list.
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
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> WebChannelPage:
        """
        Retrieve a single page of WebChannelInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of WebChannelInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return WebChannelPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> WebChannelPage:
        """
        Asynchronously retrieve a single page of WebChannelInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of WebChannelInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return WebChannelPage(self._version, response)

    def get_page(self, target_url: str) -> WebChannelPage:
        """
        Retrieve a specific page of WebChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of WebChannelInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return WebChannelPage(self._version, response)

    async def get_page_async(self, target_url: str) -> WebChannelPage:
        """
        Asynchronously retrieve a specific page of WebChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of WebChannelInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return WebChannelPage(self._version, response)

    def get(self, sid: str) -> WebChannelContext:
        """
        Constructs a WebChannelContext

        :param sid: The SID of the WebChannel resource to update.
        """
        return WebChannelContext(self._version, sid=sid)

    def __call__(self, sid: str) -> WebChannelContext:
        """
        Constructs a WebChannelContext

        :param sid: The SID of the WebChannel resource to update.
        """
        return WebChannelContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.WebChannelList>"
