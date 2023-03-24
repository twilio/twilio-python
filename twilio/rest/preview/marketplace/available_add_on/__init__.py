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


from typing import Dict, List, Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.marketplace.available_add_on.available_add_on_extension import (
    AvailableAddOnExtensionList,
)


class AvailableAddOnInstance(InstanceResource):
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the AvailableAddOnInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "friendly_name": payload.get("friendly_name"),
            "description": payload.get("description"),
            "pricing_type": payload.get("pricing_type"),
            "configuration_schema": payload.get("configuration_schema"),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[AvailableAddOnContext] = None

    @property
    def _proxy(self) -> "AvailableAddOnContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AvailableAddOnContext for this AvailableAddOnInstance
        """
        if self._context is None:
            self._context = AvailableAddOnContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns: The unique string that we created to identify the AvailableAddOn resource.
        """
        return self._properties["sid"]

    @property
    def friendly_name(self) -> str:
        """
        :returns: The string that you assigned to describe the resource.
        """
        return self._properties["friendly_name"]

    @property
    def description(self) -> str:
        """
        :returns: A short description of the Add-on's functionality.
        """
        return self._properties["description"]

    @property
    def pricing_type(self) -> str:
        """
        :returns: How customers are charged for using this Add-on.
        """
        return self._properties["pricing_type"]

    @property
    def configuration_schema(self) -> Dict[str, object]:
        """
        :returns: The JSON object with the configuration that must be provided when installing a given Add-on.
        """
        return self._properties["configuration_schema"]

    @property
    def url(self) -> str:
        """
        :returns: The absolute URL of the resource.
        """
        return self._properties["url"]

    @property
    def links(self) -> Dict[str, object]:
        """
        :returns: The URLs of related resources.
        """
        return self._properties["links"]

    def fetch(self) -> "AvailableAddOnInstance":
        """
        Fetch the AvailableAddOnInstance


        :returns: The fetched AvailableAddOnInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AvailableAddOnInstance":
        """
        Asynchronous coroutine to fetch the AvailableAddOnInstance


        :returns: The fetched AvailableAddOnInstance
        """
        return await self._proxy.fetch_async()

    @property
    def extensions(self) -> AvailableAddOnExtensionList:
        """
        Access the extensions
        """
        return self._proxy.extensions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Marketplace.AvailableAddOnInstance {}>".format(context)


class AvailableAddOnContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the AvailableAddOnContext

        :param version: Version that contains the resource
        :param sid: The SID of the AvailableAddOn resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/AvailableAddOns/{sid}".format(**self._solution)

        self._extensions: Optional[AvailableAddOnExtensionList] = None

    def fetch(self) -> AvailableAddOnInstance:
        """
        Fetch the AvailableAddOnInstance


        :returns: The fetched AvailableAddOnInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AvailableAddOnInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AvailableAddOnInstance:
        """
        Asynchronous coroutine to fetch the AvailableAddOnInstance


        :returns: The fetched AvailableAddOnInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AvailableAddOnInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def extensions(self) -> AvailableAddOnExtensionList:
        """
        Access the extensions
        """
        if self._extensions is None:
            self._extensions = AvailableAddOnExtensionList(
                self._version,
                self._solution["sid"],
            )
        return self._extensions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Marketplace.AvailableAddOnContext {}>".format(context)


class AvailableAddOnPage(Page):
    def get_instance(self, payload) -> AvailableAddOnInstance:
        """
        Build an instance of AvailableAddOnInstance

        :param dict payload: Payload response from the API
        """
        return AvailableAddOnInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Marketplace.AvailableAddOnPage>"


class AvailableAddOnList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AvailableAddOnList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/AvailableAddOns"

    def stream(self, limit=None, page_size=None) -> List[AvailableAddOnInstance]:
        """
        Streams AvailableAddOnInstance records from the API as a generator stream.
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

    async def stream_async(
        self, limit=None, page_size=None
    ) -> List[AvailableAddOnInstance]:
        """
        Asynchronously streams AvailableAddOnInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[AvailableAddOnInstance]:
        """
        Lists AvailableAddOnInstance records from the API as a list.
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

    async def list_async(
        self, limit=None, page_size=None
    ) -> List[AvailableAddOnInstance]:
        """
        Asynchronously lists AvailableAddOnInstance records from the API as a list.
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
    ) -> AvailableAddOnPage:
        """
        Retrieve a single page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AvailableAddOnPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> AvailableAddOnPage:
        """
        Asynchronously retrieve a single page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnInstance
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
        return AvailableAddOnPage(self._version, response)

    def get_page(self, target_url) -> AvailableAddOnPage:
        """
        Retrieve a specific page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AvailableAddOnPage(self._version, response)

    async def get_page_async(self, target_url) -> AvailableAddOnPage:
        """
        Asynchronously retrieve a specific page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AvailableAddOnPage(self._version, response)

    def get(self, sid) -> AvailableAddOnContext:
        """
        Constructs a AvailableAddOnContext

        :param sid: The SID of the AvailableAddOn resource to fetch.
        """
        return AvailableAddOnContext(self._version, sid=sid)

    def __call__(self, sid) -> AvailableAddOnContext:
        """
        Constructs a AvailableAddOnContext

        :param sid: The SID of the AvailableAddOn resource to fetch.
        """
        return AvailableAddOnContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Marketplace.AvailableAddOnList>"
