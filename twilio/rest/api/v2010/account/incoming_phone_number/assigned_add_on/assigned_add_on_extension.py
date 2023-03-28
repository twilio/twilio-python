r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class AssignedAddOnExtensionInstance(InstanceResource):

    """
    :ivar sid: The unique string that that we created to identify the resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource.
    :ivar resource_sid: The SID of the Phone Number to which the Add-on is assigned.
    :ivar assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar product_name: A string that you assigned to describe the Product this Extension is used within.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    :ivar enabled: Whether the Extension will be invoked.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.resource_sid: Optional[str] = payload.get("resource_sid")
        self.assigned_add_on_sid: Optional[str] = payload.get("assigned_add_on_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.product_name: Optional[str] = payload.get("product_name")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.uri: Optional[str] = payload.get("uri")
        self.enabled: Optional[bool] = payload.get("enabled")

        self._solution = {
            "account_sid": account_sid,
            "resource_sid": resource_sid,
            "assigned_add_on_sid": assigned_add_on_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[AssignedAddOnExtensionContext] = None

    @property
    def _proxy(self) -> "AssignedAddOnExtensionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssignedAddOnExtensionContext for this AssignedAddOnExtensionInstance
        """
        if self._context is None:
            self._context = AssignedAddOnExtensionContext(
                self._version,
                account_sid=self._solution["account_sid"],
                resource_sid=self._solution["resource_sid"],
                assigned_add_on_sid=self._solution["assigned_add_on_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "AssignedAddOnExtensionInstance":
        """
        Fetch the AssignedAddOnExtensionInstance


        :returns: The fetched AssignedAddOnExtensionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AssignedAddOnExtensionInstance":
        """
        Asynchronous coroutine to fetch the AssignedAddOnExtensionInstance


        :returns: The fetched AssignedAddOnExtensionInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AssignedAddOnExtensionInstance {}>".format(context)


class AssignedAddOnExtensionContext(InstanceContext):
    def __init__(
        self,
        version: Version,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
        sid: str,
    ):
        """
        Initialize the AssignedAddOnExtensionContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource to fetch.
        :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
        :param assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.
        :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "resource_sid": resource_sid,
            "assigned_add_on_sid": assigned_add_on_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions/{sid}.json".format(
            **self._solution
        )

    def fetch(self) -> AssignedAddOnExtensionInstance:
        """
        Fetch the AssignedAddOnExtensionInstance


        :returns: The fetched AssignedAddOnExtensionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AssignedAddOnExtensionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            assigned_add_on_sid=self._solution["assigned_add_on_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AssignedAddOnExtensionInstance:
        """
        Asynchronous coroutine to fetch the AssignedAddOnExtensionInstance


        :returns: The fetched AssignedAddOnExtensionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AssignedAddOnExtensionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            assigned_add_on_sid=self._solution["assigned_add_on_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AssignedAddOnExtensionContext {}>".format(context)


class AssignedAddOnExtensionPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AssignedAddOnExtensionInstance:
        """
        Build an instance of AssignedAddOnExtensionInstance

        :param payload: Payload response from the API
        """
        return AssignedAddOnExtensionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            assigned_add_on_sid=self._solution["assigned_add_on_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AssignedAddOnExtensionPage>"


class AssignedAddOnExtensionList(ListResource):
    def __init__(
        self,
        version: Version,
        account_sid: str,
        resource_sid: str,
        assigned_add_on_sid: str,
    ):
        """
        Initialize the AssignedAddOnExtensionList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
        :param resource_sid: The SID of the Phone Number to which the Add-on is assigned.
        :param assigned_add_on_sid: The SID that uniquely identifies the assigned Add-on installation.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "resource_sid": resource_sid,
            "assigned_add_on_sid": assigned_add_on_sid,
        }
        self._uri = "/Accounts/{account_sid}/IncomingPhoneNumbers/{resource_sid}/AssignedAddOns/{assigned_add_on_sid}/Extensions.json".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AssignedAddOnExtensionInstance]:
        """
        Streams AssignedAddOnExtensionInstance records from the API as a generator stream.
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
    ) -> List[AssignedAddOnExtensionInstance]:
        """
        Asynchronously streams AssignedAddOnExtensionInstance records from the API as a generator stream.
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
    ) -> List[AssignedAddOnExtensionInstance]:
        """
        Lists AssignedAddOnExtensionInstance records from the API as a list.
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
    ) -> List[AssignedAddOnExtensionInstance]:
        """
        Asynchronously lists AssignedAddOnExtensionInstance records from the API as a list.
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
    ) -> AssignedAddOnExtensionPage:
        """
        Retrieve a single page of AssignedAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssignedAddOnExtensionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AssignedAddOnExtensionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AssignedAddOnExtensionPage:
        """
        Asynchronously retrieve a single page of AssignedAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AssignedAddOnExtensionInstance
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
        return AssignedAddOnExtensionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AssignedAddOnExtensionPage:
        """
        Retrieve a specific page of AssignedAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssignedAddOnExtensionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AssignedAddOnExtensionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AssignedAddOnExtensionPage:
        """
        Asynchronously retrieve a specific page of AssignedAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AssignedAddOnExtensionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AssignedAddOnExtensionPage(self._version, response, self._solution)

    def get(self, sid: str) -> AssignedAddOnExtensionContext:
        """
        Constructs a AssignedAddOnExtensionContext

        :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
        """
        return AssignedAddOnExtensionContext(
            self._version,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            assigned_add_on_sid=self._solution["assigned_add_on_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> AssignedAddOnExtensionContext:
        """
        Constructs a AssignedAddOnExtensionContext

        :param sid: The Twilio-provided string that uniquely identifies the resource to fetch.
        """
        return AssignedAddOnExtensionContext(
            self._version,
            account_sid=self._solution["account_sid"],
            resource_sid=self._solution["resource_sid"],
            assigned_add_on_sid=self._solution["assigned_add_on_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AssignedAddOnExtensionList>"
