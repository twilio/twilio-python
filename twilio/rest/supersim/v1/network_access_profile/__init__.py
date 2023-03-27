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


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.supersim.v1.network_access_profile.network_access_profile_network import (
    NetworkAccessProfileNetworkList,
)


class NetworkAccessProfileInstance(InstanceResource):

    """
    :ivar sid: The unique string that identifies the Network Access Profile resource.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Network Access Profile belongs to.
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Network Access Profile resource.
    :ivar links:
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
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
        self._context: Optional[NetworkAccessProfileContext] = None

    @property
    def _proxy(self) -> "NetworkAccessProfileContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NetworkAccessProfileContext for this NetworkAccessProfileInstance
        """
        if self._context is None:
            self._context = NetworkAccessProfileContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "NetworkAccessProfileInstance":
        """
        Fetch the NetworkAccessProfileInstance


        :returns: The fetched NetworkAccessProfileInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "NetworkAccessProfileInstance":
        """
        Asynchronous coroutine to fetch the NetworkAccessProfileInstance


        :returns: The fetched NetworkAccessProfileInstance
        """
        return await self._proxy.fetch_async()

    def update(self, unique_name=values.unset) -> "NetworkAccessProfileInstance":
        """
        Update the NetworkAccessProfileInstance

        :param str unique_name: The new unique name of the Network Access Profile.

        :returns: The updated NetworkAccessProfileInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
        )

    async def update_async(
        self, unique_name=values.unset
    ) -> "NetworkAccessProfileInstance":
        """
        Asynchronous coroutine to update the NetworkAccessProfileInstance

        :param str unique_name: The new unique name of the Network Access Profile.

        :returns: The updated NetworkAccessProfileInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
        )

    @property
    def networks(self) -> NetworkAccessProfileNetworkList:
        """
        Access the networks
        """
        return self._proxy.networks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkAccessProfileInstance {}>".format(context)


class NetworkAccessProfileContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the NetworkAccessProfileContext

        :param version: Version that contains the resource
        :param sid: The SID of the Network Access Profile to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/NetworkAccessProfiles/{sid}".format(**self._solution)

        self._networks: Optional[NetworkAccessProfileNetworkList] = None

    def fetch(self) -> NetworkAccessProfileInstance:
        """
        Fetch the NetworkAccessProfileInstance


        :returns: The fetched NetworkAccessProfileInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return NetworkAccessProfileInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> NetworkAccessProfileInstance:
        """
        Asynchronous coroutine to fetch the NetworkAccessProfileInstance


        :returns: The fetched NetworkAccessProfileInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return NetworkAccessProfileInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(self, unique_name=values.unset) -> NetworkAccessProfileInstance:
        """
        Update the NetworkAccessProfileInstance

        :param str unique_name: The new unique name of the Network Access Profile.

        :returns: The updated NetworkAccessProfileInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NetworkAccessProfileInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    async def update_async(
        self, unique_name=values.unset
    ) -> NetworkAccessProfileInstance:
        """
        Asynchronous coroutine to update the NetworkAccessProfileInstance

        :param str unique_name: The new unique name of the Network Access Profile.

        :returns: The updated NetworkAccessProfileInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NetworkAccessProfileInstance(
            self._version, payload, sid=self._solution["sid"]
        )

    @property
    def networks(self) -> NetworkAccessProfileNetworkList:
        """
        Access the networks
        """
        if self._networks is None:
            self._networks = NetworkAccessProfileNetworkList(
                self._version,
                self._solution["sid"],
            )
        return self._networks

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkAccessProfileContext {}>".format(context)


class NetworkAccessProfilePage(Page):
    def get_instance(self, payload) -> NetworkAccessProfileInstance:
        """
        Build an instance of NetworkAccessProfileInstance

        :param dict payload: Payload response from the API
        """
        return NetworkAccessProfileInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.NetworkAccessProfilePage>"


class NetworkAccessProfileList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the NetworkAccessProfileList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/NetworkAccessProfiles"

    def create(
        self, unique_name=values.unset, networks=values.unset
    ) -> NetworkAccessProfileInstance:
        """
        Create the NetworkAccessProfileInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param List[str] networks: List of Network SIDs that this Network Access Profile will allow connections to.

        :returns: The created NetworkAccessProfileInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "Networks": serialize.map(networks, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NetworkAccessProfileInstance(self._version, payload)

    async def create_async(
        self, unique_name=values.unset, networks=values.unset
    ) -> NetworkAccessProfileInstance:
        """
        Asynchronously create the NetworkAccessProfileInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param List[str] networks: List of Network SIDs that this Network Access Profile will allow connections to.

        :returns: The created NetworkAccessProfileInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "Networks": serialize.map(networks, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NetworkAccessProfileInstance(self._version, payload)

    def stream(self, limit=None, page_size=None) -> List[NetworkAccessProfileInstance]:
        """
        Streams NetworkAccessProfileInstance records from the API as a generator stream.
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
    ) -> List[NetworkAccessProfileInstance]:
        """
        Asynchronously streams NetworkAccessProfileInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[NetworkAccessProfileInstance]:
        """
        Lists NetworkAccessProfileInstance records from the API as a list.
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
    ) -> List[NetworkAccessProfileInstance]:
        """
        Asynchronously lists NetworkAccessProfileInstance records from the API as a list.
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
    ) -> NetworkAccessProfilePage:
        """
        Retrieve a single page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkAccessProfileInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return NetworkAccessProfilePage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> NetworkAccessProfilePage:
        """
        Asynchronously retrieve a single page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkAccessProfileInstance
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
        return NetworkAccessProfilePage(self._version, response)

    def get_page(self, target_url) -> NetworkAccessProfilePage:
        """
        Retrieve a specific page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NetworkAccessProfileInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return NetworkAccessProfilePage(self._version, response)

    async def get_page_async(self, target_url) -> NetworkAccessProfilePage:
        """
        Asynchronously retrieve a specific page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NetworkAccessProfileInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return NetworkAccessProfilePage(self._version, response)

    def get(self, sid) -> NetworkAccessProfileContext:
        """
        Constructs a NetworkAccessProfileContext

        :param sid: The SID of the Network Access Profile to update.
        """
        return NetworkAccessProfileContext(self._version, sid=sid)

    def __call__(self, sid) -> NetworkAccessProfileContext:
        """
        Constructs a NetworkAccessProfileContext

        :param sid: The SID of the Network Access Profile to update.
        """
        return NetworkAccessProfileContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.NetworkAccessProfileList>"
