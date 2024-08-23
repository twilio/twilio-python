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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SyncMapItemInstance(InstanceResource):

    class QueryFromBoundType:
        INCLUSIVE = "inclusive"
        EXCLUSIVE = "exclusive"

    class QueryResultOrder:
        ASC = "asc"
        DESC = "desc"

    """
    :ivar key: 
    :ivar account_sid: 
    :ivar service_sid: 
    :ivar map_sid: 
    :ivar url: 
    :ivar revision: 
    :ivar data: 
    :ivar date_created: 
    :ivar date_updated: 
    :ivar created_by: 
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        map_sid: str,
        key: Optional[str] = None,
    ):
        super().__init__(version)

        self.key: Optional[str] = payload.get("key")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.map_sid: Optional[str] = payload.get("map_sid")
        self.url: Optional[str] = payload.get("url")
        self.revision: Optional[str] = payload.get("revision")
        self.data: Optional[Dict[str, object]] = payload.get("data")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.created_by: Optional[str] = payload.get("created_by")

        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
            "key": key or self.key,
        }
        self._context: Optional[SyncMapItemContext] = None

    @property
    def _proxy(self) -> "SyncMapItemContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncMapItemContext for this SyncMapItemInstance
        """
        if self._context is None:
            self._context = SyncMapItemContext(
                self._version,
                service_sid=self._solution["service_sid"],
                map_sid=self._solution["map_sid"],
                key=self._solution["key"],
            )
        return self._context

    def delete(self, if_match: Union[str, object] = values.unset) -> bool:
        """
        Deletes the SyncMapItemInstance

        :param if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            if_match=if_match,
        )

    async def delete_async(self, if_match: Union[str, object] = values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the SyncMapItemInstance

        :param if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            if_match=if_match,
        )

    def fetch(self) -> "SyncMapItemInstance":
        """
        Fetch the SyncMapItemInstance


        :returns: The fetched SyncMapItemInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SyncMapItemInstance":
        """
        Asynchronous coroutine to fetch the SyncMapItemInstance


        :returns: The fetched SyncMapItemInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, data: object, if_match: Union[str, object] = values.unset
    ) -> "SyncMapItemInstance":
        """
        Update the SyncMapItemInstance

        :param data:
        :param if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
        """
        return self._proxy.update(
            data=data,
            if_match=if_match,
        )

    async def update_async(
        self, data: object, if_match: Union[str, object] = values.unset
    ) -> "SyncMapItemInstance":
        """
        Asynchronous coroutine to update the SyncMapItemInstance

        :param data:
        :param if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
        """
        return await self._proxy.update_async(
            data=data,
            if_match=if_match,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Preview.Sync.SyncMapItemInstance {context}>"


class SyncMapItemContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, map_sid: str, key: str):
        """
        Initialize the SyncMapItemContext

        :param version: Version that contains the resource
        :param service_sid:
        :param map_sid:
        :param key:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
            "key": key,
        }
        self._uri = "/Services/{service_sid}/Maps/{map_sid}/Items/{key}".format(
            **self._solution
        )

    def delete(self, if_match: Union[str, object] = values.unset) -> bool:
        """
        Deletes the SyncMapItemInstance

        :param if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(self, if_match: Union[str, object] = values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the SyncMapItemInstance

        :param if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def fetch(self) -> SyncMapItemInstance:
        """
        Fetch the SyncMapItemInstance


        :returns: The fetched SyncMapItemInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=self._solution["key"],
        )

    async def fetch_async(self) -> SyncMapItemInstance:
        """
        Asynchronous coroutine to fetch the SyncMapItemInstance


        :returns: The fetched SyncMapItemInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=self._solution["key"],
        )

    def update(
        self, data: object, if_match: Union[str, object] = values.unset
    ) -> SyncMapItemInstance:
        """
        Update the SyncMapItemInstance

        :param data:
        :param if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
        """
        data = values.of(
            {
                "Data": serialize.object(data),
            }
        )
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=self._solution["key"],
        )

    async def update_async(
        self, data: object, if_match: Union[str, object] = values.unset
    ) -> SyncMapItemInstance:
        """
        Asynchronous coroutine to update the SyncMapItemInstance

        :param data:
        :param if_match: The If-Match HTTP request header

        :returns: The updated SyncMapItemInstance
        """
        data = values.of(
            {
                "Data": serialize.object(data),
            }
        )
        headers = values.of(
            {
                "If-Match": if_match,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=self._solution["key"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Preview.Sync.SyncMapItemContext {context}>"


class SyncMapItemPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> SyncMapItemInstance:
        """
        Build an instance of SyncMapItemInstance

        :param payload: Payload response from the API
        """
        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncMapItemPage>"


class SyncMapItemList(ListResource):

    def __init__(self, version: Version, service_sid: str, map_sid: str):
        """
        Initialize the SyncMapItemList

        :param version: Version that contains the resource
        :param service_sid:
        :param map_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
        }
        self._uri = "/Services/{service_sid}/Maps/{map_sid}/Items".format(
            **self._solution
        )

    def create(self, key: str, data: object) -> SyncMapItemInstance:
        """
        Create the SyncMapItemInstance

        :param key:
        :param data:

        :returns: The created SyncMapItemInstance
        """

        data = values.of(
            {
                "Key": key,
                "Data": serialize.object(data),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
        )

    async def create_async(self, key: str, data: object) -> SyncMapItemInstance:
        """
        Asynchronously create the SyncMapItemInstance

        :param key:
        :param data:

        :returns: The created SyncMapItemInstance
        """

        data = values.of(
            {
                "Key": key,
                "Data": serialize.object(data),
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return SyncMapItemInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
        )

    def stream(
        self,
        order: Union["SyncMapItemInstance.QueryResultOrder", object] = values.unset,
        from_: Union[str, object] = values.unset,
        bounds: Union["SyncMapItemInstance.QueryFromBoundType", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SyncMapItemInstance]:
        """
        Streams SyncMapItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
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
            order=order, from_=from_, bounds=bounds, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        order: Union["SyncMapItemInstance.QueryResultOrder", object] = values.unset,
        from_: Union[str, object] = values.unset,
        bounds: Union["SyncMapItemInstance.QueryFromBoundType", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[SyncMapItemInstance]:
        """
        Asynchronously streams SyncMapItemInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
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
            order=order, from_=from_, bounds=bounds, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        order: Union["SyncMapItemInstance.QueryResultOrder", object] = values.unset,
        from_: Union[str, object] = values.unset,
        bounds: Union["SyncMapItemInstance.QueryFromBoundType", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SyncMapItemInstance]:
        """
        Lists SyncMapItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
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
                order=order,
                from_=from_,
                bounds=bounds,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        order: Union["SyncMapItemInstance.QueryResultOrder", object] = values.unset,
        from_: Union[str, object] = values.unset,
        bounds: Union["SyncMapItemInstance.QueryFromBoundType", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SyncMapItemInstance]:
        """
        Asynchronously lists SyncMapItemInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param &quot;SyncMapItemInstance.QueryResultOrder&quot; order:
        :param str from_:
        :param &quot;SyncMapItemInstance.QueryFromBoundType&quot; bounds:
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
                order=order,
                from_=from_,
                bounds=bounds,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        order: Union["SyncMapItemInstance.QueryResultOrder", object] = values.unset,
        from_: Union[str, object] = values.unset,
        bounds: Union["SyncMapItemInstance.QueryFromBoundType", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SyncMapItemPage:
        """
        Retrieve a single page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param order:
        :param from_:
        :param bounds:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapItemInstance
        """
        data = values.of(
            {
                "Order": order,
                "From": from_,
                "Bounds": bounds,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SyncMapItemPage(self._version, response, self._solution)

    async def page_async(
        self,
        order: Union["SyncMapItemInstance.QueryResultOrder", object] = values.unset,
        from_: Union[str, object] = values.unset,
        bounds: Union["SyncMapItemInstance.QueryFromBoundType", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SyncMapItemPage:
        """
        Asynchronously retrieve a single page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param order:
        :param from_:
        :param bounds:
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapItemInstance
        """
        data = values.of(
            {
                "Order": order,
                "From": from_,
                "Bounds": bounds,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return SyncMapItemPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> SyncMapItemPage:
        """
        Retrieve a specific page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapItemInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SyncMapItemPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> SyncMapItemPage:
        """
        Asynchronously retrieve a specific page of SyncMapItemInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapItemInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SyncMapItemPage(self._version, response, self._solution)

    def get(self, key: str) -> SyncMapItemContext:
        """
        Constructs a SyncMapItemContext

        :param key:
        """
        return SyncMapItemContext(
            self._version,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=key,
        )

    def __call__(self, key: str) -> SyncMapItemContext:
        """
        Constructs a SyncMapItemContext

        :param key:
        """
        return SyncMapItemContext(
            self._version,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            key=key,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncMapItemList>"
