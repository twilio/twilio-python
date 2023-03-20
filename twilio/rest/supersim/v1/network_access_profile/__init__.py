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


from typing import Optional
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
    def __init__(self, version, payload, sid: Optional[str] = None):
        """
        Initialize the NetworkAccessProfileInstance

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "unique_name": payload.get("unique_name"),
            "account_sid": payload.get("account_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "url": payload.get("url"),
            "links": payload.get("links"),
        }

        self._solution = {
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[NetworkAccessProfileContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: NetworkAccessProfileContext for this NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        """
        if self._context is None:
            self._context = NetworkAccessProfileContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Network Access Profile resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :rtype: str
        """
        return self._properties["unique_name"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Network Access Profile belongs to.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Network Access Profile resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def links(self):
        """
        :returns:
        :rtype: dict
        """
        return self._properties["links"]

    def fetch(self):
        """
        Fetch the NetworkAccessProfileInstance


        :returns: The fetched NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the NetworkAccessProfileInstance


        :returns: The fetched NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        """
        return await self._proxy.fetch_async()

    def update(self, unique_name=values.unset):
        """
        Update the NetworkAccessProfileInstance

        :param str unique_name: The new unique name of the Network Access Profile.

        :returns: The updated NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
        )

    async def update_async(self, unique_name=values.unset):
        """
        Asynchronous coroutine to update the NetworkAccessProfileInstance

        :param str unique_name: The new unique name of the Network Access Profile.

        :returns: The updated NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
        )

    @property
    def networks(self):
        """
        Access the networks

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileNetworkList
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileNetworkList
        """
        return self._proxy.networks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkAccessProfileInstance {}>".format(context)


class NetworkAccessProfileContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the NetworkAccessProfileContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the Network Access Profile to update.

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/NetworkAccessProfiles/{sid}".format(**self._solution)

        self._networks: Optional[NetworkAccessProfileNetworkList] = None

    def fetch(self):
        """
        Fetch the NetworkAccessProfileInstance


        :returns: The fetched NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
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

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the NetworkAccessProfileInstance


        :returns: The fetched NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
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

    def update(self, unique_name=values.unset):
        """
        Update the NetworkAccessProfileInstance

        :param str unique_name: The new unique name of the Network Access Profile.

        :returns: The updated NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
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

    async def update_async(self, unique_name=values.unset):
        """
        Asynchronous coroutine to update the NetworkAccessProfileInstance

        :param str unique_name: The new unique name of the Network Access Profile.

        :returns: The updated NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
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
    def networks(self):
        """
        Access the networks

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileNetworkList
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileNetworkList
        """
        if self._networks is None:
            self._networks = NetworkAccessProfileNetworkList(
                self._version,
                self._solution["sid"],
            )
        return self._networks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Supersim.V1.NetworkAccessProfileContext {}>".format(context)


class NetworkAccessProfilePage(Page):
    def get_instance(self, payload):
        """
        Build an instance of NetworkAccessProfileInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
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

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileList
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileList
        """
        super().__init__(version)

        self._uri = "/NetworkAccessProfiles"

    def create(self, unique_name=values.unset, networks=values.unset):
        """
        Create the NetworkAccessProfileInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param list[str] networks: List of Network SIDs that this Network Access Profile will allow connections to.

        :returns: The created NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
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

    async def create_async(self, unique_name=values.unset, networks=values.unset):
        """
        Asynchronously create the NetworkAccessProfileInstance

        :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
        :param list[str] networks: List of Network SIDs that this Network Access Profile will allow connections to.

        :returns: The created NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
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

    def stream(self, limit=None, page_size=None):
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
        :rtype: list[twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
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
        :rtype: list[twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
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
        :rtype: list[twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
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
        :rtype: list[twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance]
        """
        return list(
            await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Retrieve a single page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfilePage
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
    ):
        """
        Asynchronously retrieve a single page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfilePage
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

    def get_page(self, target_url):
        """
        Retrieve a specific page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfilePage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return NetworkAccessProfilePage(self._version, response)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfilePage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return NetworkAccessProfilePage(self._version, response)

    def get(self, sid):
        """
        Constructs a NetworkAccessProfileContext

        :param sid: The SID of the Network Access Profile to update.

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        """
        return NetworkAccessProfileContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a NetworkAccessProfileContext

        :param sid: The SID of the Network Access Profile to update.

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        """
        return NetworkAccessProfileContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Supersim.V1.NetworkAccessProfileList>"
