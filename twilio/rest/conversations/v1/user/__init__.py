r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
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
from twilio.rest.conversations.v1.user.user_conversation import UserConversationList


class UserInstance(InstanceResource):
    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    """
    :ivar sid: The unique string that we created to identify the User resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the User resource.
    :ivar chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with.
    :ivar role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) assigned to the user.
    :ivar identity: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
    :ivar is_online: Whether the User is actively connected to this Conversations Service and online. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, if the User has never been online for this Conversations Service, even if the Service's `reachability_enabled` is `true`.
    :ivar is_notifiable: Whether the User has a potentially valid Push Notification registration (APN or GCM) for this Conversations Service. If at least one registration exists, `true`; otherwise `false`. This value is only returned by Fetch actions that return a single resource and `null` is always returned by a Read action. This value is `null` if the Service's `reachability_enabled` is `false`, and if the User has never had a notification registration, even if the Service's `reachability_enabled` is `true`.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: An absolute API resource URL for this user.
    :ivar links: 
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.chat_service_sid: Optional[str] = payload.get("chat_service_sid")
        self.role_sid: Optional[str] = payload.get("role_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.attributes: Optional[str] = payload.get("attributes")
        self.is_online: Optional[bool] = payload.get("is_online")
        self.is_notifiable: Optional[bool] = payload.get("is_notifiable")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[UserContext] = None

    @property
    def _proxy(self) -> "UserContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        """
        if self._context is None:
            self._context = UserContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Deletes the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    async def delete_async(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Asynchronous coroutine that deletes the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    def fetch(self) -> "UserInstance":
        """
        Fetch the UserInstance


        :returns: The fetched UserInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UserInstance":
        """
        Asynchronous coroutine to fetch the UserInstance


        :returns: The fetched UserInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        role_sid: Union[str, object] = values.unset,
    ) -> "UserInstance":
        """
        Update the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The string that you assigned to describe the resource.
        :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        """
        return self._proxy.update(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
        )

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        role_sid: Union[str, object] = values.unset,
    ) -> "UserInstance":
        """
        Asynchronous coroutine to update the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The string that you assigned to describe the resource.
        :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        """
        return await self._proxy.update_async(
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
        )

    @property
    def user_conversations(self) -> UserConversationList:
        """
        Access the user_conversations
        """
        return self._proxy.user_conversations

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.UserInstance {}>".format(context)


class UserContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the UserContext

        :param version: Version that contains the resource
        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Users/{sid}".format(**self._solution)

        self._user_conversations: Optional[UserConversationList] = None

    def delete(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Deletes the UserInstance

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
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
    ) -> bool:
        """
        Asynchronous coroutine that deletes the UserInstance

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

    def fetch(self) -> UserInstance:
        """
        Fetch the UserInstance


        :returns: The fetched UserInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> UserInstance:
        """
        Asynchronous coroutine to fetch the UserInstance


        :returns: The fetched UserInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        role_sid: Union[str, object] = values.unset,
    ) -> UserInstance:
        """
        Update the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The string that you assigned to describe the resource.
        :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Attributes": attributes,
                "RoleSid": role_sid,
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

        return UserInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        role_sid: Union[str, object] = values.unset,
    ) -> UserInstance:
        """
        Asynchronous coroutine to update the UserInstance

        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The string that you assigned to describe the resource.
        :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The updated UserInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Attributes": attributes,
                "RoleSid": role_sid,
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

        return UserInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def user_conversations(self) -> UserConversationList:
        """
        Access the user_conversations
        """
        if self._user_conversations is None:
            self._user_conversations = UserConversationList(
                self._version,
                self._solution["sid"],
            )
        return self._user_conversations

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.UserContext {}>".format(context)


class UserPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> UserInstance:
        """
        Build an instance of UserInstance

        :param payload: Payload response from the API
        """
        return UserInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.UserPage>"


class UserList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the UserList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Users"

    def create(
        self,
        identity: str,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        role_sid: Union[str, object] = values.unset,
    ) -> UserInstance:
        """
        Create the UserInstance

        :param identity: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The string that you assigned to describe the resource.
        :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The created UserInstance
        """
        data = values.of(
            {
                "Identity": identity,
                "FriendlyName": friendly_name,
                "Attributes": attributes,
                "RoleSid": role_sid,
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

        return UserInstance(self._version, payload)

    async def create_async(
        self,
        identity: str,
        x_twilio_webhook_enabled: Union[
            "UserInstance.WebhookEnabledType", object
        ] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        attributes: Union[str, object] = values.unset,
        role_sid: Union[str, object] = values.unset,
    ) -> UserInstance:
        """
        Asynchronously create the UserInstance

        :param identity: The application-defined string that uniquely identifies the resource's User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive.
        :param x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header
        :param friendly_name: The string that you assigned to describe the resource.
        :param attributes: The JSON Object string that stores application-specific data. If attributes have not been set, `{}` is returned.
        :param role_sid: The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) to assign to the user.

        :returns: The created UserInstance
        """
        data = values.of(
            {
                "Identity": identity,
                "FriendlyName": friendly_name,
                "Attributes": attributes,
                "RoleSid": role_sid,
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

        return UserInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[UserInstance]:
        """
        Streams UserInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[UserInstance]:
        """
        Asynchronously streams UserInstance records from the API as a generator stream.
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
    ) -> List[UserInstance]:
        """
        Lists UserInstance records from the API as a list.
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
    ) -> List[UserInstance]:
        """
        Asynchronously lists UserInstance records from the API as a list.
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
    ) -> UserPage:
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UserPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UserPage:
        """
        Asynchronously retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
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
        return UserPage(self._version, response)

    def get_page(self, target_url: str) -> UserPage:
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UserPage(self._version, response)

    async def get_page_async(self, target_url: str) -> UserPage:
        """
        Asynchronously retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UserPage(self._version, response)

    def get(self, sid: str) -> UserContext:
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        return UserContext(self._version, sid=sid)

    def __call__(self, sid: str) -> UserContext:
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to update. This value can be either the `sid` or the `identity` of the User resource to update.
        """
        return UserContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.UserList>"
