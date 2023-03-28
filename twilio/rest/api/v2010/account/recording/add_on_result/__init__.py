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


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.account.recording.add_on_result.payload import PayloadList


class AddOnResultInstance(InstanceResource):
    class Status(object):
        CANCELED = "canceled"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"
        IN_PROGRESS = "in-progress"
        INIT = "init"
        PROCESSING = "processing"
        QUEUED = "queued"

    """
    :ivar sid: The unique string that that we created to identify the Recording AddOnResult resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource.
    :ivar status: 
    :ivar add_on_sid: The SID of the Add-on to which the result belongs.
    :ivar add_on_configuration_sid: The SID of the Add-on configuration.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_completed: The date and time in GMT that the result was completed specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar reference_sid: The SID of the recording to which the AddOnResult resource belongs.
    :ivar subresource_uris: A list of related resources identified by their relative URIs.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        reference_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.status: Optional["AddOnResultInstance.Status"] = payload.get("status")
        self.add_on_sid: Optional[str] = payload.get("add_on_sid")
        self.add_on_configuration_sid: Optional[str] = payload.get(
            "add_on_configuration_sid"
        )
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.date_completed: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_completed")
        )
        self.reference_sid: Optional[str] = payload.get("reference_sid")
        self.subresource_uris: Optional[Dict[str, object]] = payload.get(
            "subresource_uris"
        )

        self._solution = {
            "account_sid": account_sid,
            "reference_sid": reference_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[AddOnResultContext] = None

    @property
    def _proxy(self) -> "AddOnResultContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AddOnResultContext for this AddOnResultInstance
        """
        if self._context is None:
            self._context = AddOnResultContext(
                self._version,
                account_sid=self._solution["account_sid"],
                reference_sid=self._solution["reference_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the AddOnResultInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AddOnResultInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AddOnResultInstance":
        """
        Fetch the AddOnResultInstance


        :returns: The fetched AddOnResultInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AddOnResultInstance":
        """
        Asynchronous coroutine to fetch the AddOnResultInstance


        :returns: The fetched AddOnResultInstance
        """
        return await self._proxy.fetch_async()

    @property
    def payloads(self) -> PayloadList:
        """
        Access the payloads
        """
        return self._proxy.payloads

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AddOnResultInstance {}>".format(context)


class AddOnResultContext(InstanceContext):
    def __init__(
        self, version: Version, account_sid: str, reference_sid: str, sid: str
    ):
        """
        Initialize the AddOnResultContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource to fetch.
        :param reference_sid: The SID of the recording to which the result to fetch belongs.
        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "reference_sid": reference_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json".format(
            **self._solution
        )

        self._payloads: Optional[PayloadList] = None

    def delete(self) -> bool:
        """
        Deletes the AddOnResultInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AddOnResultInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AddOnResultInstance:
        """
        Fetch the AddOnResultInstance


        :returns: The fetched AddOnResultInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AddOnResultInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AddOnResultInstance:
        """
        Asynchronous coroutine to fetch the AddOnResultInstance


        :returns: The fetched AddOnResultInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AddOnResultInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            sid=self._solution["sid"],
        )

    @property
    def payloads(self) -> PayloadList:
        """
        Access the payloads
        """
        if self._payloads is None:
            self._payloads = PayloadList(
                self._version,
                self._solution["account_sid"],
                self._solution["reference_sid"],
                self._solution["sid"],
            )
        return self._payloads

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AddOnResultContext {}>".format(context)


class AddOnResultPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AddOnResultInstance:
        """
        Build an instance of AddOnResultInstance

        :param payload: Payload response from the API
        """
        return AddOnResultInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AddOnResultPage>"


class AddOnResultList(ListResource):
    def __init__(self, version: Version, account_sid: str, reference_sid: str):
        """
        Initialize the AddOnResultList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to read.
        :param reference_sid: The SID of the recording to which the result to read belongs.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "reference_sid": reference_sid,
        }
        self._uri = "/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults.json".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AddOnResultInstance]:
        """
        Streams AddOnResultInstance records from the API as a generator stream.
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
    ) -> List[AddOnResultInstance]:
        """
        Asynchronously streams AddOnResultInstance records from the API as a generator stream.
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
    ) -> List[AddOnResultInstance]:
        """
        Lists AddOnResultInstance records from the API as a list.
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
    ) -> List[AddOnResultInstance]:
        """
        Asynchronously lists AddOnResultInstance records from the API as a list.
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
    ) -> AddOnResultPage:
        """
        Retrieve a single page of AddOnResultInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AddOnResultInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AddOnResultPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AddOnResultPage:
        """
        Asynchronously retrieve a single page of AddOnResultInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AddOnResultInstance
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
        return AddOnResultPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AddOnResultPage:
        """
        Retrieve a specific page of AddOnResultInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AddOnResultInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AddOnResultPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AddOnResultPage:
        """
        Asynchronously retrieve a specific page of AddOnResultInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AddOnResultInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AddOnResultPage(self._version, response, self._solution)

    def get(self, sid: str) -> AddOnResultContext:
        """
        Constructs a AddOnResultContext

        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
        """
        return AddOnResultContext(
            self._version,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> AddOnResultContext:
        """
        Constructs a AddOnResultContext

        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
        """
        return AddOnResultContext(
            self._version,
            account_sid=self._solution["account_sid"],
            reference_sid=self._solution["reference_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AddOnResultList>"
