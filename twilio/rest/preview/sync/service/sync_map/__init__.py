r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.sync.service.sync_map.sync_map_item import SyncMapItemList
from twilio.rest.preview.sync.service.sync_map.sync_map_permission import (
    SyncMapPermissionList,
)


class SyncMapInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: Optional[str] = None):
        """
        Initialize the SyncMapInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "url": payload.get("url"),
            "links": payload.get("links"),
            "revision": payload.get("revision"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "created_by": payload.get("created_by"),
        }

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[SyncMapContext] = None

    @property
    def _proxy(self) -> "SyncMapContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncMapContext for this SyncMapInstance
        """
        if self._context is None:
            self._context = SyncMapContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns:
        """
        return self._properties["sid"]

    @property
    def unique_name(self) -> str:
        """
        :returns:
        """
        return self._properties["unique_name"]

    @property
    def account_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self) -> str:
        """
        :returns:
        """
        return self._properties["service_sid"]

    @property
    def url(self) -> str:
        """
        :returns:
        """
        return self._properties["url"]

    @property
    def links(self) -> Dict[str, object]:
        """
        :returns:
        """
        return self._properties["links"]

    @property
    def revision(self) -> str:
        """
        :returns:
        """
        return self._properties["revision"]

    @property
    def date_created(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns:
        """
        return self._properties["date_updated"]

    @property
    def created_by(self) -> str:
        """
        :returns:
        """
        return self._properties["created_by"]

    def delete(self) -> bool:
        """
        Deletes the SyncMapInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SyncMapInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SyncMapInstance":
        """
        Fetch the SyncMapInstance


        :returns: The fetched SyncMapInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SyncMapInstance":
        """
        Asynchronous coroutine to fetch the SyncMapInstance


        :returns: The fetched SyncMapInstance
        """
        return await self._proxy.fetch_async()

    @property
    def sync_map_items(self) -> SyncMapItemList:
        """
        Access the sync_map_items
        """
        return self._proxy.sync_map_items

    @property
    def sync_map_permissions(self) -> SyncMapPermissionList:
        """
        Access the sync_map_permissions
        """
        return self._proxy.sync_map_permissions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncMapInstance {}>".format(context)


class SyncMapContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the SyncMapContext

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
        self._uri = "/Services/{service_sid}/Maps/{sid}".format(**self._solution)

        self._sync_map_items: Optional[SyncMapItemList] = None
        self._sync_map_permissions: Optional[SyncMapPermissionList] = None

    def delete(self) -> bool:
        """
        Deletes the SyncMapInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SyncMapInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SyncMapInstance:
        """
        Fetch the SyncMapInstance


        :returns: The fetched SyncMapInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SyncMapInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SyncMapInstance:
        """
        Asynchronous coroutine to fetch the SyncMapInstance


        :returns: The fetched SyncMapInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SyncMapInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def sync_map_items(self) -> SyncMapItemList:
        """
        Access the sync_map_items
        """
        if self._sync_map_items is None:
            self._sync_map_items = SyncMapItemList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._sync_map_items

    @property
    def sync_map_permissions(self) -> SyncMapPermissionList:
        """
        Access the sync_map_permissions
        """
        if self._sync_map_permissions is None:
            self._sync_map_permissions = SyncMapPermissionList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._sync_map_permissions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncMapContext {}>".format(context)


class SyncMapPage(Page):
    def get_instance(self, payload) -> SyncMapInstance:
        """
        Build an instance of SyncMapInstance

        :param dict payload: Payload response from the API
        """
        return SyncMapInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncMapPage>"


class SyncMapList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the SyncMapList

        :param version: Version that contains the resource
        :param service_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Maps".format(**self._solution)

    def create(self, unique_name=values.unset) -> SyncMapInstance:
        """
        Create the SyncMapInstance

        :param str unique_name:

        :returns: The created SyncMapInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncMapInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(self, unique_name=values.unset) -> SyncMapInstance:
        """
        Asynchronously create the SyncMapInstance

        :param str unique_name:

        :returns: The created SyncMapInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncMapInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(self, limit=None, page_size=None) -> List[SyncMapInstance]:
        """
        Streams SyncMapInstance records from the API as a generator stream.
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
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None) -> List[SyncMapInstance]:
        """
        Asynchronously streams SyncMapInstance records from the API as a generator stream.
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
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None) -> List[SyncMapInstance]:
        """
        Lists SyncMapInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
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

    async def list_async(self, limit=None, page_size=None) -> List[SyncMapInstance]:
        """
        Asynchronously lists SyncMapInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
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
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> SyncMapPage:
        """
        Retrieve a single page of SyncMapInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SyncMapPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> SyncMapPage:
        """
        Asynchronously retrieve a single page of SyncMapInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapInstance
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
        return SyncMapPage(self._version, response, self._solution)

    def get_page(self, target_url) -> SyncMapPage:
        """
        Retrieve a specific page of SyncMapInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SyncMapPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> SyncMapPage:
        """
        Asynchronously retrieve a specific page of SyncMapInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SyncMapPage(self._version, response, self._solution)

    def get(self, sid) -> SyncMapContext:
        """
        Constructs a SyncMapContext

        :param sid:
        """
        return SyncMapContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid) -> SyncMapContext:
        """
        Constructs a SyncMapContext

        :param sid:
        """
        return SyncMapContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncMapList>"
