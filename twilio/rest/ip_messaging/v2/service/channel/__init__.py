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


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.ip_messaging.v2.service.channel.invite import InviteList
from twilio.rest.ip_messaging.v2.service.channel.member import MemberList
from twilio.rest.ip_messaging.v2.service.channel.message import MessageList
from twilio.rest.ip_messaging.v2.service.channel.webhook import WebhookList


class ChannelInstance(InstanceResource):
    class ChannelType(object):
        PUBLIC = "public"
        PRIVATE = "private"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    """
    :ivar sid: 
    :ivar account_sid: 
    :ivar service_sid: 
    :ivar friendly_name: 
    :ivar unique_name: 
    :ivar attributes: 
    :ivar type: 
    :ivar date_created: 
    :ivar date_updated: 
    :ivar created_by: 
    :ivar members_count: 
    :ivar messages_count: 
    :ivar url: 
    :ivar links: 
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.attributes: Optional[str] = payload.get("attributes")
        self.type: Optional["ChannelInstance.ChannelType"] = payload.get("type")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.created_by: Optional[str] = payload.get("created_by")
        self.members_count: Optional[int] = deserialize.integer(
            payload.get("members_count")
        )
        self.messages_count: Optional[int] = deserialize.integer(
            payload.get("messages_count")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "service_sid": service_sid,
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
            self._context = ChannelContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Deletes the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    async def delete_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Asynchronous coroutine that deletes the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

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

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        created_by: Union[str, object] = values.unset,
    ) -> "ChannelInstance":
        """
        Update the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name:
        :param unique_name:
        :param attributes:
        :param date_created:
        :param date_updated:
        :param created_by:

        :returns: The updated ChannelInstance
        """
        return self._proxy.update(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            unique_name=unique_name,
            attributes=attributes,
            date_created=date_created,
            date_updated=date_updated,
            created_by=created_by,
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        created_by: Union[str, object] = values.unset,
    ) -> "ChannelInstance":
        """
        Asynchronous coroutine to update the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name:
        :param unique_name:
        :param attributes:
        :param date_created:
        :param date_updated:
        :param created_by:

        :returns: The updated ChannelInstance
        """
        return await self._proxy.update_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            unique_name=unique_name,
            attributes=attributes,
            date_created=date_created,
            date_updated=date_updated,
            created_by=created_by,
        )

    @property
    def invites(self) -> InviteList:
        """
        Access the invites
        """
        return self._proxy.invites

    @property
    def members(self) -> MemberList:
        """
        Access the members
        """
        return self._proxy.members

    @property
    def messages(self) -> MessageList:
        """
        Access the messages
        """
        return self._proxy.messages

    @property
    def webhooks(self) -> WebhookList:
        """
        Access the webhooks
        """
        return self._proxy.webhooks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.ChannelInstance {}>".format(context)


class ChannelContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the ChannelContext

        :param version: Version that contains the resource
        :param service_sid:
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Channels/{sid}".format(**self._solution)

        self._invites: Optional[InviteList] = None
        self._members: Optional[MemberList] = None
        self._messages: Optional[MessageList] = None
        self._webhooks: Optional[WebhookList] = None

    def delete(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Deletes the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Asynchronous coroutine that deletes the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> ChannelInstance:
        """
        Fetch the ChannelInstance


        :returns: The fetched ChannelInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ChannelInstance:
        """
        Asynchronous coroutine to fetch the ChannelInstance


        :returns: The fetched ChannelInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        created_by: Union[str, object] = values.unset,
    ) -> ChannelInstance:
        """
        Update the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name:
        :param unique_name:
        :param attributes:
        :param date_created:
        :param date_updated:
        :param created_by:

        :returns: The updated ChannelInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Attributes": attributes,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "CreatedBy": created_by,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        created_by: Union[str, object] = values.unset,
    ) -> ChannelInstance:
        """
        Asynchronous coroutine to update the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name:
        :param unique_name:
        :param attributes:
        :param date_created:
        :param date_updated:
        :param created_by:

        :returns: The updated ChannelInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Attributes": attributes,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "CreatedBy": created_by,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def invites(self) -> InviteList:
        """
        Access the invites
        """
        if self._invites is None:
            self._invites = InviteList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._invites

    @property
    def members(self) -> MemberList:
        """
        Access the members
        """
        if self._members is None:
            self._members = MemberList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._members

    @property
    def messages(self) -> MessageList:
        """
        Access the messages
        """
        if self._messages is None:
            self._messages = MessageList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._messages

    @property
    def webhooks(self) -> WebhookList:
        """
        Access the webhooks
        """
        if self._webhooks is None:
            self._webhooks = WebhookList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._webhooks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V2.ChannelContext {}>".format(context)


class ChannelPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ChannelInstance:
        """
        Build an instance of ChannelInstance

        :param payload: Payload response from the API
        """
        return ChannelInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.ChannelPage>"


class ChannelList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the ChannelList

        :param version: Version that contains the resource
        :param service_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Channels".format(**self._solution)

    def create(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        type: Union["ChannelInstance.ChannelType", object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        created_by: Union[str, object] = values.unset,
    ) -> ChannelInstance:
        """
        Create the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name:
        :param unique_name:
        :param attributes:
        :param type:
        :param date_created:
        :param date_updated:
        :param created_by:

        :returns: The created ChannelInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Attributes": attributes,
                "Type": type,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "CreatedBy": created_by,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )
        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ChannelInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        x_twilio_webhook_enabled: Union[
            "ChannelInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        type: Union["ChannelInstance.ChannelType", object] = values.unset,
        date_created: Union[datetime, object] = values.unset,
        date_updated: Union[datetime, object] = values.unset,
        created_by: Union[str, object] = values.unset,
    ) -> ChannelInstance:
        """
        Asynchronously create the ChannelInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name:
        :param unique_name:
        :param attributes:
        :param type:
        :param date_created:
        :param date_updated:
        :param created_by:

        :returns: The created ChannelInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Attributes": attributes,
                "Type": type,
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateUpdated": serialize.iso8601_datetime(date_updated),
                "CreatedBy": created_by,
            }
        )
        headers = values.of(
            {
                "X-Twilio-Webhook-Enabled": x_twilio_webhook_enabled,
            }
        )
        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return ChannelInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        type: Union[List["ChannelInstance.ChannelType"], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ChannelInstance]:
        """
        Streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;ChannelInstance.ChannelType&quot;] type:
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(type=type, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        type: Union[List["ChannelInstance.ChannelType"], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ChannelInstance]:
        """
        Asynchronously streams ChannelInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;ChannelInstance.ChannelType&quot;] type:
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(type=type, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        type: Union[List["ChannelInstance.ChannelType"], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ChannelInstance]:
        """
        Lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;ChannelInstance.ChannelType&quot;] type:
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
                type=type,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        type: Union[List["ChannelInstance.ChannelType"], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ChannelInstance]:
        """
        Asynchronously lists ChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;ChannelInstance.ChannelType&quot;] type:
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
                type=type,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        type: Union[List["ChannelInstance.ChannelType"], object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ChannelPage:
        """
        Retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately

        :param type:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        """
        data = values.of(
            {
                "Type": serialize.map(type, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ChannelPage(self._version, response, self._solution)

    async def page_async(
        self,
        type: Union[List["ChannelInstance.ChannelType"], object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ChannelPage:
        """
        Asynchronously retrieve a single page of ChannelInstance records from the API.
        Request is executed immediately

        :param type:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ChannelInstance
        """
        data = values.of(
            {
                "Type": serialize.map(type, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ChannelPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ChannelPage:
        """
        Retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ChannelPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ChannelPage:
        """
        Asynchronously retrieve a specific page of ChannelInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ChannelInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ChannelPage(self._version, response, self._solution)

    def get(self, sid: str) -> ChannelContext:
        """
        Constructs a ChannelContext

        :param sid:
        """
        return ChannelContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> ChannelContext:
        """
        Constructs a ChannelContext

        :param sid:
        """
        return ChannelContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V2.ChannelList>"
