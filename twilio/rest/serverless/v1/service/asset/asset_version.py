r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
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


class AssetVersionInstance(InstanceResource):
    class Visibility(object):
        PUBLIC = "public"
        PRIVATE = "private"
        PROTECTED = "protected"

    """
    :ivar sid: The unique string that we created to identify the Asset Version resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Asset Version resource.
    :ivar service_sid: The SID of the Service that the Asset Version resource is associated with.
    :ivar asset_sid: The SID of the Asset resource that is the parent of the Asset Version.
    :ivar path: The URL-friendly string by which the Asset Version can be referenced. It can be a maximum of 255 characters. All paths begin with a forward slash ('/'). If an Asset Version creation request is submitted with a path not containing a leading slash, the path will automatically be prepended with one.
    :ivar visibility: 
    :ivar date_created: The date and time in GMT when the Asset Version resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Asset Version resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        asset_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.asset_sid: Optional[str] = payload.get("asset_sid")
        self.path: Optional[str] = payload.get("path")
        self.visibility: Optional["AssetVersionInstance.Visibility"] = payload.get(
            "visibility"
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "asset_sid": asset_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[AssetVersionContext] = None

    @property
    def _proxy(self) -> "AssetVersionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssetVersionContext for this AssetVersionInstance
        """
        if self._context is None:
            self._context = AssetVersionContext(
                self._version,
                service_sid=self._solution["service_sid"],
                asset_sid=self._solution["asset_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "AssetVersionInstance":
        """
        Fetch the AssetVersionInstance


        :returns: The fetched AssetVersionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AssetVersionInstance":
        """
        Asynchronous coroutine to fetch the AssetVersionInstance


        :returns: The fetched AssetVersionInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.AssetVersionInstance {}>".format(context)


class AssetVersionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, asset_sid: str, sid: str):
        """
        Initialize the AssetVersionContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Asset Version resource from.
        :param asset_sid: The SID of the Asset resource that is the parent of the Asset Version resource to fetch.
        :param sid: The SID of the Asset Version resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "asset_sid": asset_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Assets/{asset_sid}/Versions/{sid}".format(
            **self._solution
        )

    def fetch(self) -> AssetVersionInstance:
        """
        Fetch the AssetVersionInstance


        :returns: The fetched AssetVersionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AssetVersionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            asset_sid=self._solution["asset_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AssetVersionInstance:
        """
        Asynchronous coroutine to fetch the AssetVersionInstance


        :returns: The fetched AssetVersionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AssetVersionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            asset_sid=self._solution["asset_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.AssetVersionContext {}>".format(context)


class AssetVersionPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AssetVersionInstance:
        """
        Build an instance of AssetVersionInstance

        :param payload: Payload response from the API
        """
        return AssetVersionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            asset_sid=self._solution["asset_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.AssetVersionPage>"


class AssetVersionList(ListResource):
    def __init__(self, version: Version, service_sid: str, asset_sid: str):
        """
        Initialize the AssetVersionList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Asset Version resource from.
        :param asset_sid: The SID of the Asset resource that is the parent of the Asset Version resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "asset_sid": asset_sid,
        }
        self._uri = "/Services/{service_sid}/Assets/{asset_sid}/Versions".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssetVersionInstance]:
        """
        Streams AssetVersionInstance records from the API as a generator stream.
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
    ) -> List[AssetVersionInstance]:
        """
        Asynchronously streams AssetVersionInstance records from the API as a generator stream.
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
    ) -> List[AssetVersionInstance]:
        """
        Lists AssetVersionInstance records from the API as a list.
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
    ) -> List[AssetVersionInstance]:
        """
        Asynchronously lists AssetVersionInstance records from the API as a list.
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
    ) -> AssetVersionPage:
        """
        Retrieve a single page of AssetVersionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssetVersionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AssetVersionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssetVersionPage:
        """
        Asynchronously retrieve a single page of AssetVersionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssetVersionInstance
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
        return AssetVersionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AssetVersionPage:
        """
        Retrieve a specific page of AssetVersionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssetVersionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AssetVersionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AssetVersionPage:
        """
        Asynchronously retrieve a specific page of AssetVersionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssetVersionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AssetVersionPage(self._version, response, self._solution)

    def get(self, sid: str) -> AssetVersionContext:
        """
        Constructs a AssetVersionContext

        :param sid: The SID of the Asset Version resource to fetch.
        """
        return AssetVersionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            asset_sid=self._solution["asset_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> AssetVersionContext:
        """
        Constructs a AssetVersionContext

        :param sid: The SID of the Asset Version resource to fetch.
        """
        return AssetVersionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            asset_sid=self._solution["asset_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.AssetVersionList>"
