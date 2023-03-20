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


from typing import Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class WebChannelInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the WebChannelInstance

        :returns: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "flex_flow_sid": payload.get("flex_flow_sid"),
            "sid": payload.get("sid"),
            "url": payload.get("url"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[WebChannelContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WebChannelContext for this WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelContext
        """
        if self._context is None:
            self._context = WebChannelContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the WebChannel resource and owns this Workflow.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def flex_flow_sid(self):
        """
        :returns: The SID of the Flex Flow.
        :rtype: str
        """
        return self._properties["flex_flow_sid"]

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the WebChannel resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the WebChannel resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    def delete(self):
        """
        Deletes the WebChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the WebChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the WebChannelInstance


        :returns: The fetched WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the WebChannelInstance


        :returns: The fetched WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
        """
        return await self._proxy.fetch_async()

    def update(self, chat_status=values.unset, post_engagement_data=values.unset):
        """
        Update the WebChannelInstance

        :param WebChannelInstance.ChatStatus chat_status:
        :param str post_engagement_data: The post-engagement data.

        :returns: The updated WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
        """
        return self._proxy.update(
            chat_status=chat_status,
            post_engagement_data=post_engagement_data,
        )

    async def update_async(
        self, chat_status=values.unset, post_engagement_data=values.unset
    ):
        """
        Asynchronous coroutine to update the WebChannelInstance

        :param WebChannelInstance.ChatStatus chat_status:
        :param str post_engagement_data: The post-engagement data.

        :returns: The updated WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
        """
        return await self._proxy.update_async(
            chat_status=chat_status,
            post_engagement_data=post_engagement_data,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.WebChannelInstance {}>".format(context)


class WebChannelContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the WebChannelContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the WebChannel resource to update.

        :returns: twilio.rest.flex_api.v1.web_channel.WebChannelContext
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/WebChannels/{sid}".format(**self._solution)

    def delete(self):
        """
        Deletes the WebChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the WebChannelInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the WebChannelInstance


        :returns: The fetched WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
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

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the WebChannelInstance


        :returns: The fetched WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
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

    def update(self, chat_status=values.unset, post_engagement_data=values.unset):
        """
        Update the WebChannelInstance

        :param WebChannelInstance.ChatStatus chat_status:
        :param str post_engagement_data: The post-engagement data.

        :returns: The updated WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
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
        self, chat_status=values.unset, post_engagement_data=values.unset
    ):
        """
        Asynchronous coroutine to update the WebChannelInstance

        :param WebChannelInstance.ChatStatus chat_status:
        :param str post_engagement_data: The post-engagement data.

        :returns: The updated WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
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

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.WebChannelContext {}>".format(context)


class WebChannelPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of WebChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
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

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.web_channel.WebChannelList
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelList
        """
        super().__init__(version)

        self._uri = "/WebChannels"

    def create(
        self,
        flex_flow_sid,
        identity,
        customer_friendly_name,
        chat_friendly_name,
        chat_unique_name=values.unset,
        pre_engagement_data=values.unset,
    ):
        """
        Create the WebChannelInstance

        :param str flex_flow_sid: The SID of the Flex Flow.
        :param str identity: The chat identity.
        :param str customer_friendly_name: The chat participant's friendly name.
        :param str chat_friendly_name: The chat channel's friendly name.
        :param str chat_unique_name: The chat channel's unique name.
        :param str pre_engagement_data: The pre-engagement data.

        :returns: The created WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
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
        flex_flow_sid,
        identity,
        customer_friendly_name,
        chat_friendly_name,
        chat_unique_name=values.unset,
        pre_engagement_data=values.unset,
    ):
        """
        Asynchronously create the WebChannelInstance

        :param str flex_flow_sid: The SID of the Flex Flow.
        :param str identity: The chat identity.
        :param str customer_friendly_name: The chat participant's friendly name.
        :param str chat_friendly_name: The chat channel's friendly name.
        :param str chat_unique_name: The chat channel's unique name.
        :param str pre_engagement_data: The pre-engagement data.

        :returns: The created WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelInstance
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

    def stream(self, limit=None, page_size=None):
        """
        Streams WebChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.flex_api.v1.web_channel.WebChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams WebChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.flex_api.v1.web_channel.WebChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists WebChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.web_channel.WebChannelInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists WebChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.flex_api.v1.web_channel.WebChannelInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of WebChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelPage
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
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of WebChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelPage
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

    def get_page(self, target_url):
        """
        Retrieve a specific page of WebChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return WebChannelPage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of WebChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WebChannelInstance
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return WebChannelPage(self._version, response)

    def get(self, sid):
        """
        Constructs a WebChannelContext

        :param sid: The SID of the WebChannel resource to update.

        :returns: twilio.rest.flex_api.v1.web_channel.WebChannelContext
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelContext
        """
        return WebChannelContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a WebChannelContext

        :param sid: The SID of the WebChannel resource to update.

        :returns: twilio.rest.flex_api.v1.web_channel.WebChannelContext
        :rtype: twilio.rest.flex_api.v1.web_channel.WebChannelContext
        """
        return WebChannelContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.FlexApi.V1.WebChannelList>"
