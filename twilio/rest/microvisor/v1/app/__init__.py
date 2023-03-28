r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.microvisor.v1.app.app_manifest import AppManifestList


class AppInstance(InstanceResource):

    """
    :ivar sid: A 34-character string that uniquely identifies this App.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar hash: App manifest hash represented as `hash_algorithm:hash_value`.
    :ivar unique_name: A developer-defined string that uniquely identifies the App. This value must be unique for all Apps on this Account. The `unique_name` value may be used as an alternative to the `sid` in the URL path to address the resource.
    :ivar date_created: The date that this App was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date that this App was last updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The URL of this resource.
    :ivar links:
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.hash: Optional[str] = payload.get("hash")
        self.unique_name: Optional[str] = payload.get("unique_name")
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
        self._context: Optional[AppContext] = None

    @property
    def _proxy(self) -> "AppContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AppContext for this AppInstance
        """
        if self._context is None:
            self._context = AppContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the AppInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AppInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AppInstance":
        """
        Fetch the AppInstance


        :returns: The fetched AppInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AppInstance":
        """
        Asynchronous coroutine to fetch the AppInstance


        :returns: The fetched AppInstance
        """
        return await self._proxy.fetch_async()

    @property
    def app_manifests(self) -> AppManifestList:
        """
        Access the app_manifests
        """
        return self._proxy.app_manifests

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Microvisor.V1.AppInstance {}>".format(context)


class AppContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the AppContext

        :param version: Version that contains the resource
        :param sid: A 34-character string that uniquely identifies this App.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Apps/{sid}".format(**self._solution)

        self._app_manifests: Optional[AppManifestList] = None

    def delete(self) -> bool:
        """
        Deletes the AppInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AppInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AppInstance:
        """
        Fetch the AppInstance


        :returns: The fetched AppInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AppInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AppInstance:
        """
        Asynchronous coroutine to fetch the AppInstance


        :returns: The fetched AppInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AppInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def app_manifests(self) -> AppManifestList:
        """
        Access the app_manifests
        """
        if self._app_manifests is None:
            self._app_manifests = AppManifestList(
                self._version,
                self._solution["sid"],
            )
        return self._app_manifests

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Microvisor.V1.AppContext {}>".format(context)


class AppPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AppInstance:
        """
        Build an instance of AppInstance

        :param payload: Payload response from the API
        """
        return AppInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Microvisor.V1.AppPage>"


class AppList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AppList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Apps"

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AppInstance]:
        """
        Streams AppInstance records from the API as a generator stream.
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
    ) -> List[AppInstance]:
        """
        Asynchronously streams AppInstance records from the API as a generator stream.
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
    ) -> List[AppInstance]:
        """
        Lists AppInstance records from the API as a list.
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
    ) -> List[AppInstance]:
        """
        Asynchronously lists AppInstance records from the API as a list.
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
    ) -> AppPage:
        """
        Retrieve a single page of AppInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AppInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AppPage(self._version, response)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AppPage:
        """
        Asynchronously retrieve a single page of AppInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AppInstance
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
        return AppPage(self._version, response)

    def get_page(self, target_url: str) -> AppPage:
        """
        Retrieve a specific page of AppInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AppInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AppPage(self._version, response)

    async def get_page_async(self, target_url: str) -> AppPage:
        """
        Asynchronously retrieve a specific page of AppInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AppInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AppPage(self._version, response)

    def get(self, sid: str) -> AppContext:
        """
        Constructs a AppContext

        :param sid: A 34-character string that uniquely identifies this App.
        """
        return AppContext(self._version, sid=sid)

    def __call__(self, sid: str) -> AppContext:
        """
        Constructs a AppContext

        :param sid: A 34-character string that uniquely identifies this App.
        """
        return AppContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Microvisor.V1.AppList>"
