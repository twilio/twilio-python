r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class RoleInstance(InstanceResource):
    class RoleType(object):
        CHANNEL = "channel"
        DEPLOYMENT = "deployment"

    """
    :ivar sid: 
    :ivar account_sid: 
    :ivar service_sid: 
    :ivar friendly_name: 
    :ivar type: 
    :ivar permissions: 
    :ivar date_created: 
    :ivar date_updated: 
    :ivar url: 
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
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.type: Optional["RoleInstance.RoleType"] = payload.get("type")
        self.permissions: Optional[List[str]] = payload.get("permissions")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[RoleContext] = None

    @property
    def _proxy(self) -> "RoleContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoleContext for this RoleInstance
        """
        if self._context is None:
            self._context = RoleContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the RoleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RoleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "RoleInstance":
        """
        Fetch the RoleInstance


        :returns: The fetched RoleInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "RoleInstance":
        """
        Asynchronous coroutine to fetch the RoleInstance


        :returns: The fetched RoleInstance
        """
        return await self._proxy.fetch_async()

    def update(self, permission: List[str]) -> "RoleInstance":
        """
        Update the RoleInstance

        :param permission:

        :returns: The updated RoleInstance
        """
        return self._proxy.update(
            permission=permission,
        )

    async def update_async(self, permission: List[str]) -> "RoleInstance":
        """
        Asynchronous coroutine to update the RoleInstance

        :param permission:

        :returns: The updated RoleInstance
        """
        return await self._proxy.update_async(
            permission=permission,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V1.RoleInstance {}>".format(context)


class RoleContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the RoleContext

        :param version: Version that contains the resource
        :param service_sid:
        :param sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Roles/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the RoleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RoleInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> RoleInstance:
        """
        Fetch the RoleInstance


        :returns: The fetched RoleInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> RoleInstance:
        """
        Asynchronous coroutine to fetch the RoleInstance


        :returns: The fetched RoleInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(self, permission: List[str]) -> RoleInstance:
        """
        Update the RoleInstance

        :param permission:

        :returns: The updated RoleInstance
        """
        data = values.of(
            {
                "Permission": serialize.map(permission, lambda e: e),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, permission: List[str]) -> RoleInstance:
        """
        Asynchronous coroutine to update the RoleInstance

        :param permission:

        :returns: The updated RoleInstance
        """
        data = values.of(
            {
                "Permission": serialize.map(permission, lambda e: e),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.IpMessaging.V1.RoleContext {}>".format(context)


class RolePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> RoleInstance:
        """
        Build an instance of RoleInstance

        :param payload: Payload response from the API
        """
        return RoleInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V1.RolePage>"


class RoleList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the RoleList

        :param version: Version that contains the resource
        :param service_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Roles".format(**self._solution)

    def create(
        self, friendly_name: str, type: "RoleInstance.RoleType", permission: List[str]
    ) -> RoleInstance:
        """
        Create the RoleInstance

        :param friendly_name:
        :param type:
        :param permission:

        :returns: The created RoleInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Type": type,
                "Permission": serialize.map(permission, lambda e: e),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoleInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self, friendly_name: str, type: "RoleInstance.RoleType", permission: List[str]
    ) -> RoleInstance:
        """
        Asynchronously create the RoleInstance

        :param friendly_name:
        :param type:
        :param permission:

        :returns: The created RoleInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Type": type,
                "Permission": serialize.map(permission, lambda e: e),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return RoleInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RoleInstance]:
        """
        Streams RoleInstance records from the API as a generator stream.
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
    ) -> List[RoleInstance]:
        """
        Asynchronously streams RoleInstance records from the API as a generator stream.
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
    ) -> List[RoleInstance]:
        """
        Lists RoleInstance records from the API as a list.
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
    ) -> List[RoleInstance]:
        """
        Asynchronously lists RoleInstance records from the API as a list.
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
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> RolePage:
        """
        Retrieve a single page of RoleInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RoleInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return RolePage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> RolePage:
        """
        Asynchronously retrieve a single page of RoleInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RoleInstance
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
        return RolePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> RolePage:
        """
        Retrieve a specific page of RoleInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RoleInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return RolePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> RolePage:
        """
        Asynchronously retrieve a specific page of RoleInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RoleInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return RolePage(self._version, response, self._solution)

    def get(self, sid: str) -> RoleContext:
        """
        Constructs a RoleContext

        :param sid:
        """
        return RoleContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> RoleContext:
        """
        Constructs a RoleContext

        :param sid:
        """
        return RoleContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.IpMessaging.V1.RoleList>"
