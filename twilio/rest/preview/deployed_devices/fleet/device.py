r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
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


class DeviceInstance(InstanceResource):
    """
    :ivar sid: Contains a 34 character string that uniquely identifies this Device resource.
    :ivar url: Contains an absolute URL for this Device resource.
    :ivar unique_name: Contains a unique and addressable name of this Device, assigned by the developer, up to 128 characters long.
    :ivar friendly_name: Contains a human readable descriptive text for this Device, up to 256 characters long
    :ivar fleet_sid: Specifies the unique string identifier of the Fleet that the given Device belongs to.
    :ivar enabled: Contains a boolean flag indicating whether the device is enabled or not, blocks device connectivity if set to false.
    :ivar account_sid: Specifies the unique string identifier of the Account responsible for this Device.
    :ivar identity: Contains an arbitrary string identifier representing a human user associated with this Device, assigned by the developer, up to 256 characters long.
    :ivar deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is associated with.
    :ivar date_created: Specifies the date this Device was created, given in UTC ISO 8601 format.
    :ivar date_updated: Specifies the date this Device was last updated, given in UTC ISO 8601 format.
    :ivar date_authenticated: Specifies the date this Device was last authenticated, given in UTC ISO 8601 format.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        fleet_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.url: Optional[str] = payload.get("url")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.fleet_sid: Optional[str] = payload.get("fleet_sid")
        self.enabled: Optional[bool] = payload.get("enabled")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.deployment_sid: Optional[str] = payload.get("deployment_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.date_authenticated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_authenticated")
        )

        self._solution = {
            "fleet_sid": fleet_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[DeviceContext] = None

    @property
    def _proxy(self) -> "DeviceContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DeviceContext for this DeviceInstance
        """
        if self._context is None:
            self._context = DeviceContext(
                self._version,
                fleet_sid=self._solution["fleet_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the DeviceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the DeviceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "DeviceInstance":
        """
        Fetch the DeviceInstance


        :returns: The fetched DeviceInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "DeviceInstance":
        """
        Asynchronous coroutine to fetch the DeviceInstance


        :returns: The fetched DeviceInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        identity: Union[str, object] = values.unset,
        deployment_sid: Union[str, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> "DeviceInstance":
        """
        Update the DeviceInstance

        :param friendly_name: Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
        :param identity: Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
        :param deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
        :param enabled:

        :returns: The updated DeviceInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            identity=identity,
            deployment_sid=deployment_sid,
            enabled=enabled,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        identity: Union[str, object] = values.unset,
        deployment_sid: Union[str, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> "DeviceInstance":
        """
        Asynchronous coroutine to update the DeviceInstance

        :param friendly_name: Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
        :param identity: Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
        :param deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
        :param enabled:

        :returns: The updated DeviceInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            identity=identity,
            deployment_sid=deployment_sid,
            enabled=enabled,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.DeployedDevices.DeviceInstance {}>".format(context)


class DeviceContext(InstanceContext):
    def __init__(self, version: Version, fleet_sid: str, sid: str):
        """
        Initialize the DeviceContext

        :param version: Version that contains the resource
        :param fleet_sid:
        :param sid: Provides a 34 character string that uniquely identifies the requested Device resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "fleet_sid": fleet_sid,
            "sid": sid,
        }
        self._uri = "/Fleets/{fleet_sid}/Devices/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the DeviceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the DeviceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> DeviceInstance:
        """
        Fetch the DeviceInstance


        :returns: The fetched DeviceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return DeviceInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> DeviceInstance:
        """
        Asynchronous coroutine to fetch the DeviceInstance


        :returns: The fetched DeviceInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return DeviceInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        identity: Union[str, object] = values.unset,
        deployment_sid: Union[str, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> DeviceInstance:
        """
        Update the DeviceInstance

        :param friendly_name: Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
        :param identity: Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
        :param deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
        :param enabled:

        :returns: The updated DeviceInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Identity": identity,
                "DeploymentSid": deployment_sid,
                "Enabled": enabled,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        identity: Union[str, object] = values.unset,
        deployment_sid: Union[str, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> DeviceInstance:
        """
        Asynchronous coroutine to update the DeviceInstance

        :param friendly_name: Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
        :param identity: Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
        :param deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
        :param enabled:

        :returns: The updated DeviceInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Identity": identity,
                "DeploymentSid": deployment_sid,
                "Enabled": enabled,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceInstance(
            self._version,
            payload,
            fleet_sid=self._solution["fleet_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.DeployedDevices.DeviceContext {}>".format(context)


class DevicePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> DeviceInstance:
        """
        Build an instance of DeviceInstance

        :param payload: Payload response from the API
        """
        return DeviceInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.DeployedDevices.DevicePage>"


class DeviceList(ListResource):
    def __init__(self, version: Version, fleet_sid: str):
        """
        Initialize the DeviceList

        :param version: Version that contains the resource
        :param fleet_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "fleet_sid": fleet_sid,
        }
        self._uri = "/Fleets/{fleet_sid}/Devices".format(**self._solution)

    def create(
        self,
        unique_name: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        identity: Union[str, object] = values.unset,
        deployment_sid: Union[str, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> DeviceInstance:
        """
        Create the DeviceInstance

        :param unique_name: Provides a unique and addressable name to be assigned to this Device, to be used in addition to SID, up to 128 characters long.
        :param friendly_name: Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
        :param identity: Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
        :param deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
        :param enabled:

        :returns: The created DeviceInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "Identity": identity,
                "DeploymentSid": deployment_sid,
                "Enabled": enabled,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    async def create_async(
        self,
        unique_name: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        identity: Union[str, object] = values.unset,
        deployment_sid: Union[str, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
    ) -> DeviceInstance:
        """
        Asynchronously create the DeviceInstance

        :param unique_name: Provides a unique and addressable name to be assigned to this Device, to be used in addition to SID, up to 128 characters long.
        :param friendly_name: Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
        :param identity: Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
        :param deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
        :param enabled:

        :returns: The created DeviceInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "Identity": identity,
                "DeploymentSid": deployment_sid,
                "Enabled": enabled,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceInstance(
            self._version, payload, fleet_sid=self._solution["fleet_sid"]
        )

    def stream(
        self,
        deployment_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[DeviceInstance]:
        """
        Streams DeviceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str deployment_sid: Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(deployment_sid=deployment_sid, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        deployment_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[DeviceInstance]:
        """
        Asynchronously streams DeviceInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str deployment_sid: Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            deployment_sid=deployment_sid, page_size=limits["page_size"]
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        deployment_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DeviceInstance]:
        """
        Lists DeviceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str deployment_sid: Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
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
                deployment_sid=deployment_sid,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        deployment_sid: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DeviceInstance]:
        """
        Asynchronously lists DeviceInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str deployment_sid: Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
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
                deployment_sid=deployment_sid,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        deployment_sid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DevicePage:
        """
        Retrieve a single page of DeviceInstance records from the API.
        Request is executed immediately

        :param deployment_sid: Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DeviceInstance
        """
        data = values.of(
            {
                "DeploymentSid": deployment_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return DevicePage(self._version, response, self._solution)

    async def page_async(
        self,
        deployment_sid: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DevicePage:
        """
        Asynchronously retrieve a single page of DeviceInstance records from the API.
        Request is executed immediately

        :param deployment_sid: Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DeviceInstance
        """
        data = values.of(
            {
                "DeploymentSid": deployment_sid,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return DevicePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> DevicePage:
        """
        Retrieve a specific page of DeviceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DeviceInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return DevicePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> DevicePage:
        """
        Asynchronously retrieve a specific page of DeviceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DeviceInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return DevicePage(self._version, response, self._solution)

    def get(self, sid: str) -> DeviceContext:
        """
        Constructs a DeviceContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Device resource.
        """
        return DeviceContext(
            self._version, fleet_sid=self._solution["fleet_sid"], sid=sid
        )

    def __call__(self, sid: str) -> DeviceContext:
        """
        Constructs a DeviceContext

        :param sid: Provides a 34 character string that uniquely identifies the requested Device resource.
        """
        return DeviceContext(
            self._version, fleet_sid=self._solution["fleet_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.DeployedDevices.DeviceList>"
