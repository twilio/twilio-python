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


class BindingInstance(InstanceResource):
    class BindingType(object):
        APN = "apn"
        GCM = "gcm"
        FCM = "fcm"

    """
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar account_sid: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this binding.
    :ivar chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with.
    :ivar credential_sid: The SID of the [Credential](https://www.twilio.com/docs/conversations/api/credential-resource) for the binding. See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
    :ivar date_created: The date that this resource was created.
    :ivar date_updated: The date that this resource was last updated.
    :ivar endpoint: The unique endpoint identifier for the Binding. The format of this value depends on the `binding_type`.
    :ivar identity: The application-defined string that uniquely identifies the [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more info.
    :ivar binding_type: 
    :ivar message_types: The [Conversation message types](https://www.twilio.com/docs/chat/push-notification-configuration#push-types) the binding is subscribed to.
    :ivar url: An absolute API resource URL for this binding.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        chat_service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.chat_service_sid: Optional[str] = payload.get("chat_service_sid")
        self.credential_sid: Optional[str] = payload.get("credential_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.endpoint: Optional[str] = payload.get("endpoint")
        self.identity: Optional[str] = payload.get("identity")
        self.binding_type: Optional["BindingInstance.BindingType"] = payload.get(
            "binding_type"
        )
        self.message_types: Optional[List[str]] = payload.get("message_types")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "chat_service_sid": chat_service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[BindingContext] = None

    @property
    def _proxy(self) -> "BindingContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BindingContext for this BindingInstance
        """
        if self._context is None:
            self._context = BindingContext(
                self._version,
                chat_service_sid=self._solution["chat_service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the BindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the BindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "BindingInstance":
        """
        Fetch the BindingInstance


        :returns: The fetched BindingInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "BindingInstance":
        """
        Asynchronous coroutine to fetch the BindingInstance


        :returns: The fetched BindingInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.BindingInstance {}>".format(context)


class BindingContext(InstanceContext):
    def __init__(self, version: Version, chat_service_sid: str, sid: str):
        """
        Initialize the BindingContext

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with.
        :param sid: A 34 character string that uniquely identifies this resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{chat_service_sid}/Bindings/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the BindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the BindingInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> BindingInstance:
        """
        Fetch the BindingInstance


        :returns: The fetched BindingInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return BindingInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> BindingInstance:
        """
        Asynchronous coroutine to fetch the BindingInstance


        :returns: The fetched BindingInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return BindingInstance(
            self._version,
            payload,
            chat_service_sid=self._solution["chat_service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.BindingContext {}>".format(context)


class BindingPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> BindingInstance:
        """
        Build an instance of BindingInstance

        :param payload: Payload response from the API
        """
        return BindingInstance(
            self._version, payload, chat_service_sid=self._solution["chat_service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.BindingPage>"


class BindingList(ListResource):
    def __init__(self, version: Version, chat_service_sid: str):
        """
        Initialize the BindingList

        :param version: Version that contains the resource
        :param chat_service_sid: The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Binding resource is associated with.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "chat_service_sid": chat_service_sid,
        }
        self._uri = "/Services/{chat_service_sid}/Bindings".format(**self._solution)

    def stream(
        self,
        binding_type: Union[List["BindingInstance.BindingType"], object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BindingInstance]:
        """
        Streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param List[str] identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
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
            binding_type=binding_type, identity=identity, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        binding_type: Union[List["BindingInstance.BindingType"], object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BindingInstance]:
        """
        Asynchronously streams BindingInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param List[str] identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
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
            binding_type=binding_type, identity=identity, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        binding_type: Union[List["BindingInstance.BindingType"], object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BindingInstance]:
        """
        Lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param List[str] identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
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
                binding_type=binding_type,
                identity=identity,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        binding_type: Union[List["BindingInstance.BindingType"], object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BindingInstance]:
        """
        Asynchronously lists BindingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param List[&quot;BindingInstance.BindingType&quot;] binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param List[str] identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
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
                binding_type=binding_type,
                identity=identity,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        binding_type: Union[List["BindingInstance.BindingType"], object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> BindingPage:
        """
        Retrieve a single page of BindingInstance records from the API.
        Request is executed immediately

        :param binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BindingInstance
        """
        data = values.of(
            {
                "BindingType": serialize.map(binding_type, lambda e: e),
                "Identity": serialize.map(identity, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return BindingPage(self._version, response, self._solution)

    async def page_async(
        self,
        binding_type: Union[List["BindingInstance.BindingType"], object] = values.unset,
        identity: Union[List[str], object] = values.unset,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> BindingPage:
        """
        Asynchronously retrieve a single page of BindingInstance records from the API.
        Request is executed immediately

        :param binding_type: The push technology used by the Binding resources to read.  Can be: `apn`, `gcm`, or `fcm`.  See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info.
        :param identity: The identity of a [Conversation User](https://www.twilio.com/docs/conversations/api/user-resource) this binding belongs to. See [access tokens](https://www.twilio.com/docs/conversations/create-tokens) for more details.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BindingInstance
        """
        data = values.of(
            {
                "BindingType": serialize.map(binding_type, lambda e: e),
                "Identity": serialize.map(identity, lambda e: e),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return BindingPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> BindingPage:
        """
        Retrieve a specific page of BindingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BindingInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return BindingPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> BindingPage:
        """
        Asynchronously retrieve a specific page of BindingInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BindingInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return BindingPage(self._version, response, self._solution)

    def get(self, sid: str) -> BindingContext:
        """
        Constructs a BindingContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return BindingContext(
            self._version, chat_service_sid=self._solution["chat_service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> BindingContext:
        """
        Constructs a BindingContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return BindingContext(
            self._version, chat_service_sid=self._solution["chat_service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.BindingList>"
