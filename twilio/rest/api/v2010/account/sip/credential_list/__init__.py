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
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.account.sip.credential_list.credential import CredentialList


class CredentialListInstance(InstanceResource):

    """
    :ivar account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) that owns this resource.
    :ivar date_created: The date that this resource was created, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
    :ivar date_updated: The date that this resource was last updated, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
    :ivar friendly_name: A human readable descriptive text that describes the CredentialList, up to 64 characters long.
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar subresource_uris: A list of credentials associated with this credential list.
    :ivar uri: The URI for this resource, relative to `https://api.twilio.com`.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.sid: Optional[str] = payload.get("sid")
        self.subresource_uris: Optional[Dict[str, object]] = payload.get(
            "subresource_uris"
        )
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[CredentialListContext] = None

    @property
    def _proxy(self) -> "CredentialListContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CredentialListContext for this CredentialListInstance
        """
        if self._context is None:
            self._context = CredentialListContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the CredentialListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CredentialListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "CredentialListInstance":
        """
        Fetch the CredentialListInstance


        :returns: The fetched CredentialListInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "CredentialListInstance":
        """
        Asynchronous coroutine to fetch the CredentialListInstance


        :returns: The fetched CredentialListInstance
        """
        return await self._proxy.fetch_async()

    def update(self, friendly_name: str) -> "CredentialListInstance":
        """
        Update the CredentialListInstance

        :param friendly_name: A human readable descriptive text for a CredentialList, up to 64 characters long.

        :returns: The updated CredentialListInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
        )

    async def update_async(self, friendly_name: str) -> "CredentialListInstance":
        """
        Asynchronous coroutine to update the CredentialListInstance

        :param friendly_name: A human readable descriptive text for a CredentialList, up to 64 characters long.

        :returns: The updated CredentialListInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
        )

    @property
    def credentials(self) -> CredentialList:
        """
        Access the credentials
        """
        return self._proxy.credentials

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.CredentialListInstance {}>".format(context)


class CredentialListContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the CredentialListContext

        :param version: Version that contains the resource
        :param account_sid: The unique id of the Account that is responsible for this resource.
        :param sid: The credential list Sid that uniquely identifies this resource
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/CredentialLists/{sid}.json".format(
            **self._solution
        )

        self._credentials: Optional[CredentialList] = None

    def delete(self) -> bool:
        """
        Deletes the CredentialListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the CredentialListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> CredentialListInstance:
        """
        Fetch the CredentialListInstance


        :returns: The fetched CredentialListInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return CredentialListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> CredentialListInstance:
        """
        Asynchronous coroutine to fetch the CredentialListInstance


        :returns: The fetched CredentialListInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return CredentialListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def update(self, friendly_name: str) -> CredentialListInstance:
        """
        Update the CredentialListInstance

        :param friendly_name: A human readable descriptive text for a CredentialList, up to 64 characters long.

        :returns: The updated CredentialListInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, friendly_name: str) -> CredentialListInstance:
        """
        Asynchronous coroutine to update the CredentialListInstance

        :param friendly_name: A human readable descriptive text for a CredentialList, up to 64 characters long.

        :returns: The updated CredentialListInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    @property
    def credentials(self) -> CredentialList:
        """
        Access the credentials
        """
        if self._credentials is None:
            self._credentials = CredentialList(
                self._version,
                self._solution["account_sid"],
                self._solution["sid"],
            )
        return self._credentials

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.CredentialListContext {}>".format(context)


class CredentialListPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> CredentialListInstance:
        """
        Build an instance of CredentialListInstance

        :param payload: Payload response from the API
        """
        return CredentialListInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.CredentialListPage>"


class CredentialListList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the CredentialListList

        :param version: Version that contains the resource
        :param account_sid: The unique id of the Account that is responsible for this resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/CredentialLists.json".format(
            **self._solution
        )

    def create(self, friendly_name: str) -> CredentialListInstance:
        """
        Create the CredentialListInstance

        :param friendly_name: A human readable descriptive text that describes the CredentialList, up to 64 characters long.

        :returns: The created CredentialListInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialListInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(self, friendly_name: str) -> CredentialListInstance:
        """
        Asynchronously create the CredentialListInstance

        :param friendly_name: A human readable descriptive text that describes the CredentialList, up to 64 characters long.

        :returns: The created CredentialListInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return CredentialListInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[CredentialListInstance]:
        """
        Streams CredentialListInstance records from the API as a generator stream.
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
    ) -> List[CredentialListInstance]:
        """
        Asynchronously streams CredentialListInstance records from the API as a generator stream.
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
    ) -> List[CredentialListInstance]:
        """
        Lists CredentialListInstance records from the API as a list.
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
    ) -> List[CredentialListInstance]:
        """
        Asynchronously lists CredentialListInstance records from the API as a list.
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
    ) -> CredentialListPage:
        """
        Retrieve a single page of CredentialListInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CredentialListPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> CredentialListPage:
        """
        Asynchronously retrieve a single page of CredentialListInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListInstance
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
        return CredentialListPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> CredentialListPage:
        """
        Retrieve a specific page of CredentialListInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CredentialListPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> CredentialListPage:
        """
        Asynchronously retrieve a specific page of CredentialListInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CredentialListPage(self._version, response, self._solution)

    def get(self, sid: str) -> CredentialListContext:
        """
        Constructs a CredentialListContext

        :param sid: The credential list Sid that uniquely identifies this resource
        """
        return CredentialListContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid: str) -> CredentialListContext:
        """
        Constructs a CredentialListContext

        :param sid: The credential list Sid that uniquely identifies this resource
        """
        return CredentialListContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.CredentialListList>"
