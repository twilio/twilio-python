r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.sync.v1.service.document import DocumentList
from twilio.rest.sync.v1.service.sync_list import SyncListList
from twilio.rest.sync.v1.service.sync_map import SyncMapList
from twilio.rest.sync.v1.service.sync_stream import SyncStreamList


class ServiceInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Service resource.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource. It is a read-only property, it cannot be assigned using REST API.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Service resource.
    :ivar webhook_url: The URL we call when Sync objects are manipulated.
    :ivar webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.
    :ivar reachability_webhooks_enabled: Whether the service instance calls `webhook_url` when client endpoints connect to Sync. The default is `false`.
    :ivar acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource. It is disabled (false) by default.
    :ivar reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
    :ivar reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before `webhook_url` is called, if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the reachability event from occurring.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.webhook_url: Optional[str] = payload.get("webhook_url")
        self.webhooks_from_rest_enabled: Optional[bool] = payload.get(
            "webhooks_from_rest_enabled"
        )
        self.reachability_webhooks_enabled: Optional[bool] = payload.get(
            "reachability_webhooks_enabled"
        )
        self.acl_enabled: Optional[bool] = payload.get("acl_enabled")
        self.reachability_debouncing_enabled: Optional[bool] = payload.get(
            "reachability_debouncing_enabled"
        )
        self.reachability_debouncing_window: Optional[int] = deserialize.integer(
            payload.get("reachability_debouncing_window")
        )
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[ServiceContext] = None

    @property
    def _proxy(self) -> "ServiceContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        """
        if self._context is None:
            self._context = ServiceContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ServiceInstance":
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ServiceInstance":
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        webhook_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_window: Union[int, object] = values.unset,
        webhooks_from_rest_enabled: Union[bool, object] = values.unset,
    ) -> "ServiceInstance":
        """
        Update the ServiceInstance

        :param webhook_url: The URL we should call when Sync objects are manipulated.
        :param friendly_name: A string that you assign to describe the resource.
        :param reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
        :param webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The updated ServiceInstance
        """
        return self._proxy.update(
            webhook_url=webhook_url,
            friendly_name=friendly_name,
            reachability_webhooks_enabled=reachability_webhooks_enabled,
            acl_enabled=acl_enabled,
            reachability_debouncing_enabled=reachability_debouncing_enabled,
            reachability_debouncing_window=reachability_debouncing_window,
            webhooks_from_rest_enabled=webhooks_from_rest_enabled,
        )

    async def update_async(
        self,
        webhook_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_window: Union[int, object] = values.unset,
        webhooks_from_rest_enabled: Union[bool, object] = values.unset,
    ) -> "ServiceInstance":
        """
        Asynchronous coroutine to update the ServiceInstance

        :param webhook_url: The URL we should call when Sync objects are manipulated.
        :param friendly_name: A string that you assign to describe the resource.
        :param reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
        :param webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The updated ServiceInstance
        """
        return await self._proxy.update_async(
            webhook_url=webhook_url,
            friendly_name=friendly_name,
            reachability_webhooks_enabled=reachability_webhooks_enabled,
            acl_enabled=acl_enabled,
            reachability_debouncing_enabled=reachability_debouncing_enabled,
            reachability_debouncing_window=reachability_debouncing_window,
            webhooks_from_rest_enabled=webhooks_from_rest_enabled,
        )

    @property
    def documents(self) -> DocumentList:
        """
        Access the documents
        """
        return self._proxy.documents

    @property
    def sync_lists(self) -> SyncListList:
        """
        Access the sync_lists
        """
        return self._proxy.sync_lists

    @property
    def sync_maps(self) -> SyncMapList:
        """
        Access the sync_maps
        """
        return self._proxy.sync_maps

    @property
    def sync_streams(self) -> SyncStreamList:
        """
        Access the sync_streams
        """
        return self._proxy.sync_streams

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.ServiceInstance {}>".format(context)


class ServiceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param version: Version that contains the resource
        :param sid: The SID of the Service resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Services/{sid}".format(**self._solution)

        self._documents: Optional[DocumentList] = None
        self._sync_lists: Optional[SyncListList] = None
        self._sync_maps: Optional[SyncMapList] = None
        self._sync_streams: Optional[SyncStreamList] = None

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ServiceInstance:
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ServiceInstance:
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        webhook_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_window: Union[int, object] = values.unset,
        webhooks_from_rest_enabled: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Update the ServiceInstance

        :param webhook_url: The URL we should call when Sync objects are manipulated.
        :param friendly_name: A string that you assign to describe the resource.
        :param reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
        :param webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "WebhookUrl": webhook_url,
                "FriendlyName": friendly_name,
                "ReachabilityWebhooksEnabled": reachability_webhooks_enabled,
                "AclEnabled": acl_enabled,
                "ReachabilityDebouncingEnabled": reachability_debouncing_enabled,
                "ReachabilityDebouncingWindow": reachability_debouncing_window,
                "WebhooksFromRestEnabled": webhooks_from_rest_enabled,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        webhook_url: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_window: Union[int, object] = values.unset,
        webhooks_from_rest_enabled: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronous coroutine to update the ServiceInstance

        :param webhook_url: The URL we should call when Sync objects are manipulated.
        :param friendly_name: A string that you assign to describe the resource.
        :param reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the webhook is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the webhook from being called.
        :param webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "WebhookUrl": webhook_url,
                "FriendlyName": friendly_name,
                "ReachabilityWebhooksEnabled": reachability_webhooks_enabled,
                "AclEnabled": acl_enabled,
                "ReachabilityDebouncingEnabled": reachability_debouncing_enabled,
                "ReachabilityDebouncingWindow": reachability_debouncing_window,
                "WebhooksFromRestEnabled": webhooks_from_rest_enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def documents(self) -> DocumentList:
        """
        Access the documents
        """
        if self._documents is None:
            self._documents = DocumentList(
                self._version,
                self._solution["sid"],
            )
        return self._documents

    @property
    def sync_lists(self) -> SyncListList:
        """
        Access the sync_lists
        """
        if self._sync_lists is None:
            self._sync_lists = SyncListList(
                self._version,
                self._solution["sid"],
            )
        return self._sync_lists

    @property
    def sync_maps(self) -> SyncMapList:
        """
        Access the sync_maps
        """
        if self._sync_maps is None:
            self._sync_maps = SyncMapList(
                self._version,
                self._solution["sid"],
            )
        return self._sync_maps

    @property
    def sync_streams(self) -> SyncStreamList:
        """
        Access the sync_streams
        """
        if self._sync_streams is None:
            self._sync_streams = SyncStreamList(
                self._version,
                self._solution["sid"],
            )
        return self._sync_streams

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Sync.V1.ServiceContext {}>".format(context)


class ServicePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ServiceInstance:
        """
        Build an instance of ServiceInstance

        :param payload: Payload response from the API
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.ServicePage>"


class ServiceList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Services"

    def create(
        self,
        friendly_name: Union[str, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_window: Union[int, object] = values.unset,
        webhooks_from_rest_enabled: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Create the ServiceInstance

        :param friendly_name: A string that you assign to describe the resource.
        :param webhook_url: The URL we should call when Sync objects are manipulated.
        :param reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the `webhook_url` is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the call to `webhook_url`.
        :param webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The created ServiceInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "ReachabilityWebhooksEnabled": reachability_webhooks_enabled,
                "AclEnabled": acl_enabled,
                "ReachabilityDebouncingEnabled": reachability_debouncing_enabled,
                "ReachabilityDebouncingWindow": reachability_debouncing_window,
                "WebhooksFromRestEnabled": webhooks_from_rest_enabled,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        reachability_webhooks_enabled: Union[bool, object] = values.unset,
        acl_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_enabled: Union[bool, object] = values.unset,
        reachability_debouncing_window: Union[int, object] = values.unset,
        webhooks_from_rest_enabled: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronously create the ServiceInstance

        :param friendly_name: A string that you assign to describe the resource.
        :param webhook_url: The URL we should call when Sync objects are manipulated.
        :param reachability_webhooks_enabled: Whether the service instance should call `webhook_url` when client endpoints connect to Sync. The default is `false`.
        :param acl_enabled: Whether token identities in the Service must be granted access to Sync objects by using the [Permissions](https://www.twilio.com/docs/sync/api/sync-permissions) resource.
        :param reachability_debouncing_enabled: Whether every `endpoint_disconnected` event should occur after a configurable delay. The default is `false`, where the `endpoint_disconnected` event occurs immediately after disconnection. When `true`, intervening reconnections can prevent the `endpoint_disconnected` event.
        :param reachability_debouncing_window: The reachability event delay in milliseconds if `reachability_debouncing_enabled` = `true`.  Must be between 1,000 and 30,000 and defaults to 5,000. This is the number of milliseconds after the last running client disconnects, and a Sync identity is declared offline, before the `webhook_url` is called if all endpoints remain offline. A reconnection from the same identity by any endpoint during this interval prevents the call to `webhook_url`.
        :param webhooks_from_rest_enabled: Whether the Service instance should call `webhook_url` when the REST API is used to update Sync objects. The default is `false`.

        :returns: The created ServiceInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "WebhookUrl": webhook_url,
                "ReachabilityWebhooksEnabled": reachability_webhooks_enabled,
                "AclEnabled": acl_enabled,
                "ReachabilityDebouncingEnabled": reachability_debouncing_enabled,
                "ReachabilityDebouncingWindow": reachability_debouncing_window,
                "WebhooksFromRestEnabled": webhooks_from_rest_enabled,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ServiceInstance]:
        """
        Streams ServiceInstance records from the API as a generator stream.
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
    ) -> List[ServiceInstance]:
        """
        Asynchronously streams ServiceInstance records from the API as a generator stream.
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
    ) -> List[ServiceInstance]:
        """
        Lists ServiceInstance records from the API as a list.
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
    ) -> List[ServiceInstance]:
        """
        Asynchronously lists ServiceInstance records from the API as a list.
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
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ServicePage:
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ServicePage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ServicePage:
        """
        Asynchronously retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
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
        return ServicePage(self._version, response)

    def get_page(self, target_url: str) -> ServicePage:
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ServicePage(self._version, response)

    async def get_page_async(self, target_url: str) -> ServicePage:
        """
        Asynchronously retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ServicePage(self._version, response)

    def get(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: The SID of the Service resource to update.
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: The SID of the Service resource to update.
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Sync.V1.ServiceList>"
