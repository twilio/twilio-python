r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class PoliciesInstance(InstanceResource):

    """
    :ivar sid: The unique string that identifies the Policy resource.
    :ivar friendly_name: A human-readable description that is assigned to describe the Policy resource. Examples can include Primary Customer profile policy
    :ivar requirements: The SID of an object that holds the policy information
    :ivar url: The absolute URL of the Policy resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.requirements: Optional[Dict[str, object]] = payload.get("requirements")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[PoliciesContext] = None

    @property
    def _proxy(self) -> "PoliciesContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PoliciesContext for this PoliciesInstance
        """
        if self._context is None:
            self._context = PoliciesContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "PoliciesInstance":
        """
        Fetch the PoliciesInstance


        :returns: The fetched PoliciesInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "PoliciesInstance":
        """
        Asynchronous coroutine to fetch the PoliciesInstance


        :returns: The fetched PoliciesInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.PoliciesInstance {}>".format(context)


class PoliciesContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the PoliciesContext

        :param version: Version that contains the resource
        :param sid: The unique string that identifies the Policy resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Policies/{sid}".format(**self._solution)

    def fetch(self) -> PoliciesInstance:
        """
        Fetch the PoliciesInstance


        :returns: The fetched PoliciesInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PoliciesInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> PoliciesInstance:
        """
        Asynchronous coroutine to fetch the PoliciesInstance


        :returns: The fetched PoliciesInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PoliciesInstance(
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
        return "<Twilio.Trusthub.V1.PoliciesContext {}>".format(context)


class PoliciesPage(Page):
    def get_instance(self, payload) -> PoliciesInstance:
        """
        Build an instance of PoliciesInstance

        :param dict payload: Payload response from the API
        """
        return PoliciesInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.PoliciesPage>"


class PoliciesList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the PoliciesList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Policies"

    def stream(self, limit=None, page_size=None) -> List[PoliciesInstance]:
        """
        Streams PoliciesInstance records from the API as a generator stream.
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

    async def stream_async(self, limit=None, page_size=None) -> List[PoliciesInstance]:
        """
        Asynchronously streams PoliciesInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[PoliciesInstance]:
        """
        Lists PoliciesInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[PoliciesInstance]:
        """
        Asynchronously lists PoliciesInstance records from the API as a list.
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
    ) -> PoliciesPage:
        """
        Retrieve a single page of PoliciesInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PoliciesInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return PoliciesPage(self._version, response)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> PoliciesPage:
        """
        Asynchronously retrieve a single page of PoliciesInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PoliciesInstance
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
        return PoliciesPage(self._version, response)

    def get_page(self, target_url) -> PoliciesPage:
        """
        Retrieve a specific page of PoliciesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PoliciesInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return PoliciesPage(self._version, response)

    async def get_page_async(self, target_url) -> PoliciesPage:
        """
        Asynchronously retrieve a specific page of PoliciesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PoliciesInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return PoliciesPage(self._version, response)

    def get(self, sid) -> PoliciesContext:
        """
        Constructs a PoliciesContext

        :param sid: The unique string that identifies the Policy resource.
        """
        return PoliciesContext(self._version, sid=sid)

    def __call__(self, sid) -> PoliciesContext:
        """
        Constructs a PoliciesContext

        :param sid: The unique string that identifies the Policy resource.
        """
        return PoliciesContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.PoliciesList>"
