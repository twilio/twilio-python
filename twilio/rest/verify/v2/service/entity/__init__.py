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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.verify.v2.service.entity.challenge import ChallengeList
from twilio.rest.verify.v2.service.entity.factor import FactorList
from twilio.rest.verify.v2.service.entity.new_factor import NewFactorList


class EntityInstance(InstanceResource):
    """
    :ivar sid: A 34 character string that uniquely identifies this Entity.
    :ivar identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar service_sid: The unique SID identifier of the Service.
    :ivar date_created: The date that this Entity was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date that this Entity was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The URL of this resource.
    :ivar links: Contains a dictionary of URL links to nested resources of this Entity.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        identity: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.identity: Optional[str] = payload.get("identity")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
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
            "identity": identity or self.identity,
        }
        self._context: Optional[EntityContext] = None

    @property
    def _proxy(self) -> "EntityContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EntityContext for this EntityInstance
        """
        if self._context is None:
            self._context = EntityContext(
                self._version,
                service_sid=self._solution["service_sid"],
                identity=self._solution["identity"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the EntityInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the EntityInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "EntityInstance":
        """
        Fetch the EntityInstance


        :returns: The fetched EntityInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "EntityInstance":
        """
        Asynchronous coroutine to fetch the EntityInstance


        :returns: The fetched EntityInstance
        """
        return await self._proxy.fetch_async()

    @property
    def challenges(self) -> ChallengeList:
        """
        Access the challenges
        """
        return self._proxy.challenges

    @property
    def factors(self) -> FactorList:
        """
        Access the factors
        """
        return self._proxy.factors

    @property
    def new_factors(self) -> NewFactorList:
        """
        Access the new_factors
        """
        return self._proxy.new_factors

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.EntityInstance {}>".format(context)


class EntityContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, identity: str):
        """
        Initialize the EntityContext

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "identity": identity,
        }
        self._uri = "/Services/{service_sid}/Entities/{identity}".format(
            **self._solution
        )

        self._challenges: Optional[ChallengeList] = None
        self._factors: Optional[FactorList] = None
        self._new_factors: Optional[NewFactorList] = None

    def delete(self) -> bool:
        """
        Deletes the EntityInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the EntityInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> EntityInstance:
        """
        Fetch the EntityInstance


        :returns: The fetched EntityInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EntityInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
        )

    async def fetch_async(self) -> EntityInstance:
        """
        Asynchronous coroutine to fetch the EntityInstance


        :returns: The fetched EntityInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EntityInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
        )

    @property
    def challenges(self) -> ChallengeList:
        """
        Access the challenges
        """
        if self._challenges is None:
            self._challenges = ChallengeList(
                self._version,
                self._solution["service_sid"],
                self._solution["identity"],
            )
        return self._challenges

    @property
    def factors(self) -> FactorList:
        """
        Access the factors
        """
        if self._factors is None:
            self._factors = FactorList(
                self._version,
                self._solution["service_sid"],
                self._solution["identity"],
            )
        return self._factors

    @property
    def new_factors(self) -> NewFactorList:
        """
        Access the new_factors
        """
        if self._new_factors is None:
            self._new_factors = NewFactorList(
                self._version,
                self._solution["service_sid"],
                self._solution["identity"],
            )
        return self._new_factors

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.EntityContext {}>".format(context)


class EntityPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> EntityInstance:
        """
        Build an instance of EntityInstance

        :param payload: Payload response from the API
        """
        return EntityInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.EntityPage>"


class EntityList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the EntityList

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Entities".format(**self._solution)

    def create(self, identity: str) -> EntityInstance:
        """
        Create the EntityInstance

        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.

        :returns: The created EntityInstance
        """

        data = values.of(
            {
                "Identity": identity,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EntityInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(self, identity: str) -> EntityInstance:
        """
        Asynchronously create the EntityInstance

        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.

        :returns: The created EntityInstance
        """

        data = values.of(
            {
                "Identity": identity,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EntityInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[EntityInstance]:
        """
        Streams EntityInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[EntityInstance]:
        """
        Asynchronously streams EntityInstance records from the API as a generator stream.
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

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EntityInstance]:
        """
        Lists EntityInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
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
    ) -> List[EntityInstance]:
        """
        Asynchronously lists EntityInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> EntityPage:
        """
        Retrieve a single page of EntityInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EntityInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EntityPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> EntityPage:
        """
        Asynchronously retrieve a single page of EntityInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EntityInstance
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
        return EntityPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> EntityPage:
        """
        Retrieve a specific page of EntityInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EntityInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EntityPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> EntityPage:
        """
        Asynchronously retrieve a specific page of EntityInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EntityInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EntityPage(self._version, response, self._solution)

    def get(self, identity: str) -> EntityContext:
        """
        Constructs a EntityContext

        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        """
        return EntityContext(
            self._version, service_sid=self._solution["service_sid"], identity=identity
        )

    def __call__(self, identity: str) -> EntityContext:
        """
        Constructs a EntityContext

        :param identity: The unique external identifier for the Entity of the Service. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        """
        return EntityContext(
            self._version, service_sid=self._solution["service_sid"], identity=identity
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.EntityList>"
