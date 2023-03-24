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
from typing import Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address import (
    IpAddressList,
)


class IpAccessControlListInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, sid: Optional[str] = None):
        """
        Initialize the IpAccessControlListInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "friendly_name": payload.get("friendly_name"),
            "date_created": deserialize.rfc2822_datetime(payload.get("date_created")),
            "date_updated": deserialize.rfc2822_datetime(payload.get("date_updated")),
            "subresource_uris": payload.get("subresource_uris"),
            "uri": payload.get("uri"),
        }

        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[IpAccessControlListContext] = None

    @property
    def _proxy(self) -> "IpAccessControlListContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: IpAccessControlListContext for this IpAccessControlListInstance
        """
        if self._context is None:
            self._context = IpAccessControlListContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self) -> str:
        """
        :returns: A 34 character string that uniquely identifies this resource.
        """
        return self._properties["sid"]

    @property
    def account_sid(self) -> str:
        """
        :returns: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) that owns this resource.
        """
        return self._properties["account_sid"]

    @property
    def friendly_name(self) -> str:
        """
        :returns: A human readable descriptive text, up to 255 characters long.
        """
        return self._properties["friendly_name"]

    @property
    def date_created(self) -> datetime:
        """
        :returns: The date that this resource was created, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        """
        return self._properties["date_created"]

    @property
    def date_updated(self) -> datetime:
        """
        :returns: The date that this resource was last updated, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        """
        return self._properties["date_updated"]

    @property
    def subresource_uris(self) -> Dict[str, object]:
        """
        :returns: A list of the IpAddress resources associated with this IP access control list resource.
        """
        return self._properties["subresource_uris"]

    @property
    def uri(self) -> str:
        """
        :returns: The URI for this resource, relative to `https://api.twilio.com`
        """
        return self._properties["uri"]

    def delete(self) -> bool:
        """
        Deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "IpAccessControlListInstance":
        """
        Fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "IpAccessControlListInstance":
        """
        Asynchronous coroutine to fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        """
        return await self._proxy.fetch_async()

    def update(self, friendly_name) -> "IpAccessControlListInstance":
        """
        Update the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text, up to 255 characters long.

        :returns: The updated IpAccessControlListInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
        )

    async def update_async(self, friendly_name) -> "IpAccessControlListInstance":
        """
        Asynchronous coroutine to update the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text, up to 255 characters long.

        :returns: The updated IpAccessControlListInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
        )

    @property
    def ip_addresses(self) -> IpAddressList:
        """
        Access the ip_addresses
        """
        return self._proxy.ip_addresses

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.IpAccessControlListInstance {}>".format(context)


class IpAccessControlListContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the IpAccessControlListContext

        :param version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param sid: A 34 character string that uniquely identifies the resource to udpate.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/SIP/IpAccessControlLists/{sid}.json".format(
                **self._solution
            )
        )

        self._ip_addresses: Optional[IpAddressList] = None

    def delete(self) -> bool:
        """
        Deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the IpAccessControlListInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> IpAccessControlListInstance:
        """
        Fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> IpAccessControlListInstance:
        """
        Asynchronous coroutine to fetch the IpAccessControlListInstance


        :returns: The fetched IpAccessControlListInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def update(self, friendly_name) -> IpAccessControlListInstance:
        """
        Update the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text, up to 255 characters long.

        :returns: The updated IpAccessControlListInstance
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

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, friendly_name) -> IpAccessControlListInstance:
        """
        Asynchronous coroutine to update the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text, up to 255 characters long.

        :returns: The updated IpAccessControlListInstance
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

        return IpAccessControlListInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    @property
    def ip_addresses(self) -> IpAddressList:
        """
        Access the ip_addresses
        """
        if self._ip_addresses is None:
            self._ip_addresses = IpAddressList(
                self._version,
                self._solution["account_sid"],
                self._solution["sid"],
            )
        return self._ip_addresses

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.IpAccessControlListContext {}>".format(context)


class IpAccessControlListPage(Page):
    def get_instance(self, payload) -> IpAccessControlListInstance:
        """
        Build an instance of IpAccessControlListInstance

        :param dict payload: Payload response from the API
        """
        return IpAccessControlListInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.IpAccessControlListPage>"


class IpAccessControlListList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the IpAccessControlListList

        :param version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/IpAccessControlLists.json".format(
            **self._solution
        )

    def create(self, friendly_name) -> IpAccessControlListInstance:
        """
        Create the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text that describes the IpAccessControlList, up to 255 characters long.

        :returns: The created IpAccessControlListInstance
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

        return IpAccessControlListInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(self, friendly_name) -> IpAccessControlListInstance:
        """
        Asynchronously create the IpAccessControlListInstance

        :param str friendly_name: A human readable descriptive text that describes the IpAccessControlList, up to 255 characters long.

        :returns: The created IpAccessControlListInstance
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

        return IpAccessControlListInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def stream(self, limit=None, page_size=None) -> List[IpAccessControlListInstance]:
        """
        Streams IpAccessControlListInstance records from the API as a generator stream.
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

    async def stream_async(
        self, limit=None, page_size=None
    ) -> List[IpAccessControlListInstance]:
        """
        Asynchronously streams IpAccessControlListInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[IpAccessControlListInstance]:
        """
        Lists IpAccessControlListInstance records from the API as a list.
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

    async def list_async(
        self, limit=None, page_size=None
    ) -> List[IpAccessControlListInstance]:
        """
        Asynchronously lists IpAccessControlListInstance records from the API as a list.
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
    ) -> IpAccessControlListPage:
        """
        Retrieve a single page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpAccessControlListInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return IpAccessControlListPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> IpAccessControlListPage:
        """
        Asynchronously retrieve a single page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpAccessControlListInstance
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
        return IpAccessControlListPage(self._version, response, self._solution)

    def get_page(self, target_url) -> IpAccessControlListPage:
        """
        Retrieve a specific page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IpAccessControlListInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return IpAccessControlListPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> IpAccessControlListPage:
        """
        Asynchronously retrieve a specific page of IpAccessControlListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IpAccessControlListInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return IpAccessControlListPage(self._version, response, self._solution)

    def get(self, sid) -> IpAccessControlListContext:
        """
        Constructs a IpAccessControlListContext

        :param sid: A 34 character string that uniquely identifies the resource to udpate.
        """
        return IpAccessControlListContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid) -> IpAccessControlListContext:
        """
        Constructs a IpAccessControlListContext

        :param sid: A 34 character string that uniquely identifies the resource to udpate.
        """
        return IpAccessControlListContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.IpAccessControlListList>"
