r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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
from twilio.rest.verify.v2.service.rate_limit.bucket import BucketList


class RateLimitInstance(InstanceResource):

    """
    :ivar sid: A 34 character string that uniquely identifies this Rate Limit.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Rate Limit resource.
    :ivar unique_name: Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.**
    :ivar description: Description of this Rate Limit
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The URL of this resource.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.description: Optional[str] = payload.get("description")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[RateLimitContext] = None

    @property
    def _proxy(self) -> "RateLimitContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RateLimitContext for this RateLimitInstance
        """
        if self._context is None:
            self._context = RateLimitContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the RateLimitInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RateLimitInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "RateLimitInstance":
        """
        Fetch the RateLimitInstance


        :returns: The fetched RateLimitInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RateLimitInstance":
        """
        Asynchronous coroutine to fetch the RateLimitInstance


        :returns: The fetched RateLimitInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, description: Union[str, object] = values.unset
    ) -> "RateLimitInstance":
        """
        Update the RateLimitInstance

        :param description: Description of this Rate Limit

        :returns: The updated RateLimitInstance
        """
        return self._proxy.update(
            description=description,
        )

    async def update_async(
        self, description: Union[str, object] = values.unset
    ) -> "RateLimitInstance":
        """
        Asynchronous coroutine to update the RateLimitInstance

        :param description: Description of this Rate Limit

        :returns: The updated RateLimitInstance
        """
        return await self._proxy.update_async(
            description=description,
        )

    @property
    def buckets(self) -> BucketList:
        """
        Access the buckets
        """
        return self._proxy.buckets

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.RateLimitInstance {}>".format(context)


class RateLimitContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the RateLimitContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
        :param sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/RateLimits/{sid}".format(**self._solution)

        self._buckets: Optional[BucketList] = None

    def delete(self) -> bool:
        """
        Deletes the RateLimitInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RateLimitInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> RateLimitInstance:
        """
        Fetch the RateLimitInstance


        :returns: The fetched RateLimitInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RateLimitInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RateLimitInstance:
        """
        Asynchronous coroutine to fetch the RateLimitInstance


        :returns: The fetched RateLimitInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RateLimitInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self, description: Union[str, object] = values.unset
    ) -> RateLimitInstance:
        """
        Update the RateLimitInstance

        :param description: Description of this Rate Limit

        :returns: The updated RateLimitInstance
        """
        data = values.of(
            {
                "Description": description,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RateLimitInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, description: Union[str, object] = values.unset
    ) -> RateLimitInstance:
        """
        Asynchronous coroutine to update the RateLimitInstance

        :param description: Description of this Rate Limit

        :returns: The updated RateLimitInstance
        """
        data = values.of(
            {
                "Description": description,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RateLimitInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def buckets(self) -> BucketList:
        """
        Access the buckets
        """
        if self._buckets is None:
            self._buckets = BucketList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._buckets

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.RateLimitContext {}>".format(context)


class RateLimitPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> RateLimitInstance:
        """
        Build an instance of RateLimitInstance

        :param payload: Payload response from the API
        """
        return RateLimitInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.RateLimitPage>"


class RateLimitList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the RateLimitList

        :param version: Version that contains the resource
        :param service_sid: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/RateLimits".format(**self._solution)

    def create(
        self, unique_name: str, description: Union[str, object] = values.unset
    ) -> RateLimitInstance:
        """
        Create the RateLimitInstance

        :param unique_name: Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.**
        :param description: Description of this Rate Limit

        :returns: The created RateLimitInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "Description": description,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RateLimitInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self, unique_name: str, description: Union[str, object] = values.unset
    ) -> RateLimitInstance:
        """
        Asynchronously create the RateLimitInstance

        :param unique_name: Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.**
        :param description: Description of this Rate Limit

        :returns: The created RateLimitInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "Description": description,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RateLimitInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RateLimitInstance]:
        """
        Streams RateLimitInstance records from the API as a generator stream.
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
    ) -> List[RateLimitInstance]:
        """
        Asynchronously streams RateLimitInstance records from the API as a generator stream.
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
    ) -> List[RateLimitInstance]:
        """
        Lists RateLimitInstance records from the API as a list.
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
    ) -> List[RateLimitInstance]:
        """
        Asynchronously lists RateLimitInstance records from the API as a list.
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
    ) -> RateLimitPage:
        """
        Retrieve a single page of RateLimitInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RateLimitInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RateLimitPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> RateLimitPage:
        """
        Asynchronously retrieve a single page of RateLimitInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RateLimitInstance
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
        return RateLimitPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> RateLimitPage:
        """
        Retrieve a specific page of RateLimitInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RateLimitInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RateLimitPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> RateLimitPage:
        """
        Asynchronously retrieve a specific page of RateLimitInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RateLimitInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RateLimitPage(self._version, response, self._solution)

    def get(self, sid: str) -> RateLimitContext:
        """
        Constructs a RateLimitContext

        :param sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
        """
        return RateLimitContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> RateLimitContext:
        """
        Constructs a RateLimitContext

        :param sid: The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
        """
        return RateLimitContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.RateLimitList>"
