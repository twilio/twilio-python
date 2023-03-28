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
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class AccountSecretInstance(InstanceResource):

    """
    :ivar key: The secret key; up to 100 characters.
    :ivar date_rotated:
    :ivar url: The absolute URL of the Secret.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], key: Optional[str] = None
    ):
        super().__init__(version)

        self.key: Optional[str] = payload.get("key")
        self.date_rotated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_rotated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "key": key or self.key,
        }
        self._context: Optional[AccountSecretContext] = None

    @property
    def _proxy(self) -> "AccountSecretContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AccountSecretContext for this AccountSecretInstance
        """
        if self._context is None:
            self._context = AccountSecretContext(
                self._version,
                key=self._solution["key"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the AccountSecretInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AccountSecretInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AccountSecretInstance":
        """
        Fetch the AccountSecretInstance


        :returns: The fetched AccountSecretInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AccountSecretInstance":
        """
        Asynchronous coroutine to fetch the AccountSecretInstance


        :returns: The fetched AccountSecretInstance
        """
        return await self._proxy.fetch_async()

    def update(self, value: str) -> "AccountSecretInstance":
        """
        Update the AccountSecretInstance

        :param value: The secret value; up to 4096 characters.

        :returns: The updated AccountSecretInstance
        """
        return self._proxy.update(
            value=value,
        )

    async def update_async(self, value: str) -> "AccountSecretInstance":
        """
        Asynchronous coroutine to update the AccountSecretInstance

        :param value: The secret value; up to 4096 characters.

        :returns: The updated AccountSecretInstance
        """
        return await self._proxy.update_async(
            value=value,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Microvisor.V1.AccountSecretInstance {}>".format(context)


class AccountSecretContext(InstanceContext):
    def __init__(self, version: Version, key: str):
        """
        Initialize the AccountSecretContext

        :param version: Version that contains the resource
        :param key: The secret key; up to 100 characters.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "key": key,
        }
        self._uri = "/Secrets/{key}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the AccountSecretInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AccountSecretInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AccountSecretInstance:
        """
        Fetch the AccountSecretInstance


        :returns: The fetched AccountSecretInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AccountSecretInstance(
            self._version,
            payload,
            key=self._solution["key"],
        )

    async def fetch_async(self) -> AccountSecretInstance:
        """
        Asynchronous coroutine to fetch the AccountSecretInstance


        :returns: The fetched AccountSecretInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AccountSecretInstance(
            self._version,
            payload,
            key=self._solution["key"],
        )

    def update(self, value: str) -> AccountSecretInstance:
        """
        Update the AccountSecretInstance

        :param value: The secret value; up to 4096 characters.

        :returns: The updated AccountSecretInstance
        """
        data = values.of(
            {
                "Value": value,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountSecretInstance(self._version, payload, key=self._solution["key"])

    async def update_async(self, value: str) -> AccountSecretInstance:
        """
        Asynchronous coroutine to update the AccountSecretInstance

        :param value: The secret value; up to 4096 characters.

        :returns: The updated AccountSecretInstance
        """
        data = values.of(
            {
                "Value": value,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountSecretInstance(self._version, payload, key=self._solution["key"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Microvisor.V1.AccountSecretContext {}>".format(context)


class AccountSecretPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AccountSecretInstance:
        """
        Build an instance of AccountSecretInstance

        :param payload: Payload response from the API
        """
        return AccountSecretInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Microvisor.V1.AccountSecretPage>"


class AccountSecretList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AccountSecretList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Secrets"

    def create(self, key: str, value: str) -> AccountSecretInstance:
        """
        Create the AccountSecretInstance

        :param key: The secret key; up to 100 characters.
        :param value: The secret value; up to 4096 characters.

        :returns: The created AccountSecretInstance
        """
        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountSecretInstance(self._version, payload)

    async def create_async(self, key: str, value: str) -> AccountSecretInstance:
        """
        Asynchronously create the AccountSecretInstance

        :param key: The secret key; up to 100 characters.
        :param value: The secret value; up to 4096 characters.

        :returns: The created AccountSecretInstance
        """
        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountSecretInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AccountSecretInstance]:
        """
        Streams AccountSecretInstance records from the API as a generator stream.
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
    ) -> List[AccountSecretInstance]:
        """
        Asynchronously streams AccountSecretInstance records from the API as a generator stream.
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
    ) -> List[AccountSecretInstance]:
        """
        Lists AccountSecretInstance records from the API as a list.
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
    ) -> List[AccountSecretInstance]:
        """
        Asynchronously lists AccountSecretInstance records from the API as a list.
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
    ) -> AccountSecretPage:
        """
        Retrieve a single page of AccountSecretInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AccountSecretInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AccountSecretPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AccountSecretPage:
        """
        Asynchronously retrieve a single page of AccountSecretInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AccountSecretInstance
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
        return AccountSecretPage(self._version, response)

    def get_page(self, target_url: str) -> AccountSecretPage:
        """
        Retrieve a specific page of AccountSecretInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AccountSecretInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AccountSecretPage(self._version, response)

    async def get_page_async(self, target_url: str) -> AccountSecretPage:
        """
        Asynchronously retrieve a specific page of AccountSecretInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AccountSecretInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AccountSecretPage(self._version, response)

    def get(self, key: str) -> AccountSecretContext:
        """
        Constructs a AccountSecretContext

        :param key: The secret key; up to 100 characters.
        """
        return AccountSecretContext(self._version, key=key)

    def __call__(self, key: str) -> AccountSecretContext:
        """
        Constructs a AccountSecretContext

        :param key: The secret key; up to 100 characters.
        """
        return AccountSecretContext(self._version, key=key)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Microvisor.V1.AccountSecretList>"
