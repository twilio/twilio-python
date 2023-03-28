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
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UserConversationInstance(InstanceResource):
    class NotificationLevel(object):
        DEFAULT = "default"
        MUTED = "muted"

    class State(object):
        INACTIVE = "inactive"
        ACTIVE = "active"
        CLOSED = "closed"

    """
    :ivar account_sid: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this conversation.
    :ivar chat_service_sid: The unique ID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) this conversation belongs to.
    :ivar conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this User Conversation.
    :ivar unread_messages_count: The number of unread Messages in the Conversation for the Participant.
    :ivar last_read_message_index: The index of the last Message in the Conversation that the Participant has read.
    :ivar participant_sid: The unique ID of the [participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) the user conversation belongs to.
    :ivar user_sid: The unique string that identifies the [User resource](https://www.twilio.com/docs/conversations/api/user-resource).
    :ivar friendly_name: The human-readable name of this conversation, limited to 256 characters. Optional.
    :ivar conversation_state: 
    :ivar timers: Timer date values representing state update for this conversation.
    :ivar attributes: An optional string metadata field you can use to store any data you wish. The string value must contain structurally valid JSON if specified.  **Note** that if the attributes are not set \"{}\" will be returned.
    :ivar date_created: The date that this conversation was created, given in ISO 8601 format.
    :ivar date_updated: The date that this conversation was last updated, given in ISO 8601 format.
    :ivar created_by: Identity of the creator of this Conversation.
    :ivar notification_level: 
    :ivar unique_name: An application-defined string that uniquely identifies the Conversation resource. It can be used to address the resource in place of the resource's `conversation_sid` in the URL.
    :ivar url: 
    :ivar links: Contains absolute URLs to access the [participant](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) and [conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) of this conversation.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        user_sid: str,
        conversation_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.chat_service_sid: Optional[str] = payload.get("chat_service_sid")
        self.conversation_sid: Optional[str] = payload.get("conversation_sid")
        self.unread_messages_count: Optional[int] = deserialize.integer(
            payload.get("unread_messages_count")
        )
        self.last_read_message_index: Optional[int] = deserialize.integer(
            payload.get("last_read_message_index")
        )
        self.participant_sid: Optional[str] = payload.get("participant_sid")
        self.user_sid: Optional[str] = payload.get("user_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.conversation_state: Optional[
            "UserConversationInstance.State"
        ] = payload.get("conversation_state")
        self.timers: Optional[Dict[str, object]] = payload.get("timers")
        self.attributes: Optional[str] = payload.get("attributes")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.created_by: Optional[str] = payload.get("created_by")
        self.notification_level: Optional[
            "UserConversationInstance.NotificationLevel"
        ] = payload.get("notification_level")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "user_sid": user_sid,
            "conversation_sid": conversation_sid or self.conversation_sid,
        }
        self._context: Optional[UserConversationContext] = None

    @property
    def _proxy(self) -> "UserConversationContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UserConversationContext for this UserConversationInstance
        """
        if self._context is None:
            self._context = UserConversationContext(
                self._version,
                user_sid=self._solution["user_sid"],
                conversation_sid=self._solution["conversation_sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the UserConversationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserConversationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "UserConversationInstance":
        """
        Fetch the UserConversationInstance


        :returns: The fetched UserConversationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "UserConversationInstance":
        """
        Asynchronous coroutine to fetch the UserConversationInstance


        :returns: The fetched UserConversationInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        notification_level: Union[
            "UserConversationInstance.NotificationLevel", object
        ] = values.unset,
        last_read_timestamp: Union[datetime, object] = values.unset,
        last_read_message_index: Union[int, object] = values.unset,
    ) -> "UserConversationInstance":
        """
        Update the UserConversationInstance

        :param notification_level:
        :param last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
        :param last_read_message_index: The index of the last Message in the Conversation that the Participant has read.

        :returns: The updated UserConversationInstance
        """
        return self._proxy.update(
            notification_level=notification_level,
            last_read_timestamp=last_read_timestamp,
            last_read_message_index=last_read_message_index,
        )

    async def update_async(
        self,
        notification_level: Union[
            "UserConversationInstance.NotificationLevel", object
        ] = values.unset,
        last_read_timestamp: Union[datetime, object] = values.unset,
        last_read_message_index: Union[int, object] = values.unset,
    ) -> "UserConversationInstance":
        """
        Asynchronous coroutine to update the UserConversationInstance

        :param notification_level:
        :param last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
        :param last_read_message_index: The index of the last Message in the Conversation that the Participant has read.

        :returns: The updated UserConversationInstance
        """
        return await self._proxy.update_async(
            notification_level=notification_level,
            last_read_timestamp=last_read_timestamp,
            last_read_message_index=last_read_message_index,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.UserConversationInstance {}>".format(context)


class UserConversationContext(InstanceContext):
    def __init__(self, version: Version, user_sid: str, conversation_sid: str):
        """
        Initialize the UserConversationContext

        :param version: Version that contains the resource
        :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.
        :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "user_sid": user_sid,
            "conversation_sid": conversation_sid,
        }
        self._uri = "/Users/{user_sid}/Conversations/{conversation_sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the UserConversationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the UserConversationInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> UserConversationInstance:
        """
        Fetch the UserConversationInstance


        :returns: The fetched UserConversationInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return UserConversationInstance(
            self._version,
            payload,
            user_sid=self._solution["user_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    async def fetch_async(self) -> UserConversationInstance:
        """
        Asynchronous coroutine to fetch the UserConversationInstance


        :returns: The fetched UserConversationInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return UserConversationInstance(
            self._version,
            payload,
            user_sid=self._solution["user_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    def update(
        self,
        notification_level: Union[
            "UserConversationInstance.NotificationLevel", object
        ] = values.unset,
        last_read_timestamp: Union[datetime, object] = values.unset,
        last_read_message_index: Union[int, object] = values.unset,
    ) -> UserConversationInstance:
        """
        Update the UserConversationInstance

        :param notification_level:
        :param last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
        :param last_read_message_index: The index of the last Message in the Conversation that the Participant has read.

        :returns: The updated UserConversationInstance
        """
        data = values.of(
            {
                "NotificationLevel": notification_level,
                "LastReadTimestamp": serialize.iso8601_datetime(last_read_timestamp),
                "LastReadMessageIndex": last_read_message_index,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserConversationInstance(
            self._version,
            payload,
            user_sid=self._solution["user_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    async def update_async(
        self,
        notification_level: Union[
            "UserConversationInstance.NotificationLevel", object
        ] = values.unset,
        last_read_timestamp: Union[datetime, object] = values.unset,
        last_read_message_index: Union[int, object] = values.unset,
    ) -> UserConversationInstance:
        """
        Asynchronous coroutine to update the UserConversationInstance

        :param notification_level:
        :param last_read_timestamp: The date of the last message read in conversation by the user, given in ISO 8601 format.
        :param last_read_message_index: The index of the last Message in the Conversation that the Participant has read.

        :returns: The updated UserConversationInstance
        """
        data = values.of(
            {
                "NotificationLevel": notification_level,
                "LastReadTimestamp": serialize.iso8601_datetime(last_read_timestamp),
                "LastReadMessageIndex": last_read_message_index,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return UserConversationInstance(
            self._version,
            payload,
            user_sid=self._solution["user_sid"],
            conversation_sid=self._solution["conversation_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.UserConversationContext {}>".format(context)


class UserConversationPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> UserConversationInstance:
        """
        Build an instance of UserConversationInstance

        :param payload: Payload response from the API
        """
        return UserConversationInstance(
            self._version, payload, user_sid=self._solution["user_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.UserConversationPage>"


class UserConversationList(ListResource):
    def __init__(self, version: Version, user_sid: str):
        """
        Initialize the UserConversationList

        :param version: Version that contains the resource
        :param user_sid: The unique SID identifier of the [User resource](https://www.twilio.com/docs/conversations/api/user-resource). This value can be either the `sid` or the `identity` of the User resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "user_sid": user_sid,
        }
        self._uri = "/Users/{user_sid}/Conversations".format(**self._solution)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UserConversationInstance]:
        """
        Streams UserConversationInstance records from the API as a generator stream.
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
    ) -> List[UserConversationInstance]:
        """
        Asynchronously streams UserConversationInstance records from the API as a generator stream.
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

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UserConversationInstance]:
        """
        Lists UserConversationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UserConversationInstance]:
        """
        Asynchronously lists UserConversationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> UserConversationPage:
        """
        Retrieve a single page of UserConversationInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserConversationInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UserConversationPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> UserConversationPage:
        """
        Asynchronously retrieve a single page of UserConversationInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UserConversationInstance
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
        return UserConversationPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> UserConversationPage:
        """
        Retrieve a specific page of UserConversationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserConversationInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UserConversationPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> UserConversationPage:
        """
        Asynchronously retrieve a specific page of UserConversationInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UserConversationInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UserConversationPage(self._version, response, self._solution)

    def get(self, conversation_sid: str) -> UserConversationContext:
        """
        Constructs a UserConversationContext

        :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
        """
        return UserConversationContext(
            self._version,
            user_sid=self._solution["user_sid"],
            conversation_sid=conversation_sid,
        )

    def __call__(self, conversation_sid: str) -> UserConversationContext:
        """
        Constructs a UserConversationContext

        :param conversation_sid: The unique SID identifier of the Conversation. This value can be either the `sid` or the `unique_name` of the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource).
        """
        return UserConversationContext(
            self._version,
            user_sid=self._solution["user_sid"],
            conversation_sid=conversation_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.UserConversationList>"
