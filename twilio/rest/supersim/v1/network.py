r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class NetworkInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Network resource.
    :ivar friendly_name: A human readable identifier of this resource.
    :ivar url: The absolute URL of the Network resource.
    :ivar iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resource.
    :ivar identifiers: Array of objects identifying the [MCC-MNCs](https://en.wikipedia.org/wiki/Mobile_country_code) that are included in the Network resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.url: Optional[str] = payload.get("url")
        self.iso_country: Optional[str] = payload.get("iso_country")
        self.identifiers: Optional[List[object]] = payload.get("identifiers")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[NetworkContext] = None

    @property
    def _proxy(self) -> "NetworkContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NetworkContext for this NetworkInstance
        """
        if self._context is None:
            self._context = NetworkContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "NetworkInstance":
        """
        Fetch the NetworkInstance


        :returns: The fetched NetworkInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "NetworkInstance":
        """
        Asynchronous coroutine to fetch the NetworkInstance


        :returns: The fetched NetworkInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkInstance {}>".format(context)


class NetworkContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the NetworkContext

        :param version: Version that contains the resource
        :param sid: The SID of the Network resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Networks/{sid}".format(**self._solution)

    def fetch(self) -> NetworkInstance:
        """
        Fetch the NetworkInstance


        :returns: The fetched NetworkInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return NetworkInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> NetworkInstance:
        """
        Asynchronous coroutine to fetch the NetworkInstance


        :returns: The fetched NetworkInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return NetworkInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkContext {}>".format(context)


class NetworkPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> NetworkInstance:
        """
        Build an instance of NetworkInstance

        :param payload: Payload response from the API
        """
        return NetworkInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.NetworkPage>"


class NetworkList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the NetworkList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Networks"

    def stream(
        self,
        iso_country: Union[str, object] = values.unset,
        mcc: Union[str, object] = values.unset,
        mnc: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NetworkInstance]:
        """
        Streams NetworkInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
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
            iso_country=iso_country, mcc=mcc, mnc=mnc, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        iso_country: Union[str, object] = values.unset,
        mcc: Union[str, object] = values.unset,
        mnc: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NetworkInstance]:
        """
        Asynchronously streams NetworkInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
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
            iso_country=iso_country, mcc=mcc, mnc=mnc, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        iso_country: Union[str, object] = values.unset,
        mcc: Union[str, object] = values.unset,
        mnc: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NetworkInstance]:
        """
        Lists NetworkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
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
                iso_country=iso_country,
                mcc=mcc,
                mnc=mnc,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        iso_country: Union[str, object] = values.unset,
        mcc: Union[str, object] = values.unset,
        mnc: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[NetworkInstance]:
        """
        Asynchronously lists NetworkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param str mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param str mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
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
                iso_country=iso_country,
                mcc=mcc,
                mnc=mnc,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        iso_country: Union[str, object] = values.unset,
        mcc: Union[str, object] = values.unset,
        mnc: Union[str, object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> NetworkPage:
        """
        Retrieve a single page of NetworkInstance records from the API.
        Request is executed immediately

        :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkInstance
        """
        data = values.of(
            {
                "IsoCountry": iso_country,
                "Mcc": mcc,
                "Mnc": mnc,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return NetworkPage(self._version, response)

    async def page_async(
        self,
        iso_country: Union[str, object] = values.unset,
        mcc: Union[str, object] = values.unset,
        mnc: Union[str, object] = values.unset,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> NetworkPage:
        """
        Asynchronously retrieve a single page of NetworkInstance records from the API.
        Request is executed immediately

        :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
        :param mcc: The 'mobile country code' of a country. Network resources with this `mcc` in their `identifiers` will be read.
        :param mnc: The 'mobile network code' of a mobile operator network. Network resources with this `mnc` in their `identifiers` will be read.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkInstance
        """
        data = values.of(
            {
                "IsoCountry": iso_country,
                "Mcc": mcc,
                "Mnc": mnc,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return NetworkPage(self._version, response)

    def get_page(self, target_url: str) -> NetworkPage:
        """
        Retrieve a specific page of NetworkInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of NetworkInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return NetworkPage(self._version, response)

    async def get_page_async(self, target_url: str) -> NetworkPage:
        """
        Asynchronously retrieve a specific page of NetworkInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of NetworkInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return NetworkPage(self._version, response)

    def get(self, sid: str) -> NetworkContext:
        """
        Constructs a NetworkContext

        :param sid: The SID of the Network resource to fetch.
        """
        return NetworkContext(self._version, sid=sid)

    def __call__(self, sid: str) -> NetworkContext:
        """
        Constructs a NetworkContext

        :param sid: The SID of the Network resource to fetch.
        """
        return NetworkContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.NetworkList>"
