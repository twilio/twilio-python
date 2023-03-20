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


from typing import Optional
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class SyncMapPermissionInstance(InstanceResource):
    def __init__(
        self,
        version,
        payload,
        service_sid: str,
        map_sid: str,
        identity: Optional[str] = None,
    ):
        """
        Initialize the SyncMapPermissionInstance

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        super().__init__(version)

        self._properties = {
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "map_sid": payload.get("map_sid"),
            "identity": payload.get("identity"),
            "read": payload.get("read"),
            "write": payload.get("write"),
            "manage": payload.get("manage"),
            "url": payload.get("url"),
        }

        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
            "identity": identity or self._properties["identity"],
        }
        self._context: Optional[SyncMapPermissionContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SyncMapPermissionContext for this SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionContext
        """
        if self._context is None:
            self._context = SyncMapPermissionContext(
                self._version,
                service_sid=self._solution["service_sid"],
                map_sid=self._solution["map_sid"],
                identity=self._solution["identity"],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Twilio Account.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self):
        """
        :returns: The unique SID identifier of the Sync Service Instance.
        :rtype: str
        """
        return self._properties["service_sid"]

    @property
    def map_sid(self):
        """
        :returns: The unique SID identifier of the Sync Map to which the Permission applies.
        :rtype: str
        """
        return self._properties["map_sid"]

    @property
    def identity(self):
        """
        :returns: Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
        :rtype: str
        """
        return self._properties["identity"]

    @property
    def read(self):
        """
        :returns: Boolean flag specifying whether the identity can read the Sync Map and its Items.
        :rtype: bool
        """
        return self._properties["read"]

    @property
    def write(self):
        """
        :returns: Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map.
        :rtype: bool
        """
        return self._properties["write"]

    @property
    def manage(self):
        """
        :returns: Boolean flag specifying whether the identity can delete the Sync Map.
        :rtype: bool
        """
        return self._properties["manage"]

    @property
    def url(self):
        """
        :returns: Contains an absolute URL for this Sync Map Permission.
        :rtype: str
        """
        return self._properties["url"]

    def delete(self):
        """
        Deletes the SyncMapPermissionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the SyncMapPermissionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the SyncMapPermissionInstance


        :returns: The fetched SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SyncMapPermissionInstance


        :returns: The fetched SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        return await self._proxy.fetch_async()

    def update(self, read, write, manage):
        """
        Update the SyncMapPermissionInstance

        :param bool read: Boolean flag specifying whether the identity can read the Sync Map.
        :param bool write: Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map.
        :param bool manage: Boolean flag specifying whether the identity can delete the Sync Map.

        :returns: The updated SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        return self._proxy.update(
            read=read,
            write=write,
            manage=manage,
        )

    async def update_async(self, read, write, manage):
        """
        Asynchronous coroutine to update the SyncMapPermissionInstance

        :param bool read: Boolean flag specifying whether the identity can read the Sync Map.
        :param bool write: Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map.
        :param bool manage: Boolean flag specifying whether the identity can delete the Sync Map.

        :returns: The updated SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        return await self._proxy.update_async(
            read=read,
            write=write,
            manage=manage,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncMapPermissionInstance {}>".format(context)


class SyncMapPermissionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, map_sid: str, identity: str):
        """
        Initialize the SyncMapPermissionContext

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Sync Service Instance.
        :param map_sid: Identifier of the Sync Map. Either a SID or a unique name.
        :param identity: Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
            "identity": identity,
        }
        self._uri = (
            "/Services/{service_sid}/Maps/{map_sid}/Permissions/{identity}".format(
                **self._solution
            )
        )

    def delete(self):
        """
        Deletes the SyncMapPermissionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the SyncMapPermissionInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the SyncMapPermissionInstance


        :returns: The fetched SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SyncMapPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            identity=self._solution["identity"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the SyncMapPermissionInstance


        :returns: The fetched SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SyncMapPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            identity=self._solution["identity"],
        )

    def update(self, read, write, manage):
        """
        Update the SyncMapPermissionInstance

        :param bool read: Boolean flag specifying whether the identity can read the Sync Map.
        :param bool write: Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map.
        :param bool manage: Boolean flag specifying whether the identity can delete the Sync Map.

        :returns: The updated SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        data = values.of(
            {
                "Read": read,
                "Write": write,
                "Manage": manage,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncMapPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            identity=self._solution["identity"],
        )

    async def update_async(self, read, write, manage):
        """
        Asynchronous coroutine to update the SyncMapPermissionInstance

        :param bool read: Boolean flag specifying whether the identity can read the Sync Map.
        :param bool write: Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map.
        :param bool manage: Boolean flag specifying whether the identity can delete the Sync Map.

        :returns: The updated SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        data = values.of(
            {
                "Read": read,
                "Write": write,
                "Manage": manage,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SyncMapPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            identity=self._solution["identity"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Sync.SyncMapPermissionContext {}>".format(context)


class SyncMapPermissionList(ListResource):
    def __init__(self, version: Version, service_sid: str, map_sid: str):
        """
        Initialize the SyncMapPermissionList

        :param Version version: Version that contains the resource
        :param service_sid:
        :param map_sid: Identifier of the Sync Map. Either a SID or a unique name.

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionList
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "map_sid": map_sid,
        }
        self._uri = "/Services/{service_sid}/Maps/{map_sid}/Permissions".format(
            **self._solution
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams SyncMapPermissionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams SyncMapPermissionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncMapPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists SyncMapPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance]
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
        Retrieve a single page of SyncMapPermissionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SyncMapPermissionPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of SyncMapPermissionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionPage
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
        return SyncMapPermissionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncMapPermissionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SyncMapPermissionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of SyncMapPermissionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SyncMapPermissionPage(self._version, response, self._solution)

    def get(self, identity):
        """
        Constructs a SyncMapPermissionContext

        :param identity: Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionContext
        """
        return SyncMapPermissionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            identity=identity,
        )

    def __call__(self, identity):
        """
        Constructs a SyncMapPermissionContext

        :param identity: Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionContext
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionContext
        """
        return SyncMapPermissionContext(
            self._version,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
            identity=identity,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Preview.Sync.SyncMapPermissionList>"


class SyncMapPermissionPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of SyncMapPermissionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        :rtype: twilio.rest.preview.sync.service.sync_map.sync_map_permission.SyncMapPermissionInstance
        """
        return SyncMapPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            map_sid=self._solution["map_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Sync.SyncMapPermissionPage>"
