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


class IpAddressInstance(InstanceResource):

    """
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar account_sid: The unique id of the Account that is responsible for this resource.
    :ivar friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
    :ivar ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
    :ivar cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
    :ivar ip_access_control_list_sid: The unique id of the IpAccessControlList resource that includes this resource.
    :ivar date_created: The date that this resource was created, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
    :ivar date_updated: The date that this resource was last updated, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
    :ivar uri: The URI for this resource, relative to `https://api.twilio.com`
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.ip_address: Optional[str] = payload.get("ip_address")
        self.cidr_prefix_length: Optional[int] = deserialize.integer(
            payload.get("cidr_prefix_length")
        )
        self.ip_access_control_list_sid: Optional[str] = payload.get(
            "ip_access_control_list_sid"
        )
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "ip_access_control_list_sid": ip_access_control_list_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[IpAddressContext] = None

    @property
    def _proxy(self) -> "IpAddressContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: IpAddressContext for this IpAddressInstance
        """
        if self._context is None:
            self._context = IpAddressContext(
                self._version,
                account_sid=self._solution["account_sid"],
                ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the IpAddressInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the IpAddressInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "IpAddressInstance":
        """
        Fetch the IpAddressInstance


        :returns: The fetched IpAddressInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "IpAddressInstance":
        """
        Asynchronous coroutine to fetch the IpAddressInstance


        :returns: The fetched IpAddressInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        ip_address: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        cidr_prefix_length: Union[int, object] = values.unset,
    ) -> "IpAddressInstance":
        """
        Update the IpAddressInstance

        :param ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :param cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: The updated IpAddressInstance
        """
        return self._proxy.update(
            ip_address=ip_address,
            friendly_name=friendly_name,
            cidr_prefix_length=cidr_prefix_length,
        )

    async def update_async(
        self,
        ip_address: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        cidr_prefix_length: Union[int, object] = values.unset,
    ) -> "IpAddressInstance":
        """
        Asynchronous coroutine to update the IpAddressInstance

        :param ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :param cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: The updated IpAddressInstance
        """
        return await self._proxy.update_async(
            ip_address=ip_address,
            friendly_name=friendly_name,
            cidr_prefix_length=cidr_prefix_length,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.IpAddressInstance {}>".format(context)


class IpAddressContext(InstanceContext):
    def __init__(
        self,
        version: Version,
        account_sid: str,
        ip_access_control_list_sid: str,
        sid: str,
    ):
        """
        Initialize the IpAddressContext

        :param version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to update.
        :param sid: A 34 character string that identifies the IpAddress resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "ip_access_control_list_sid": ip_access_control_list_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the IpAddressInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the IpAddressInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> IpAddressInstance:
        """
        Fetch the IpAddressInstance


        :returns: The fetched IpAddressInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> IpAddressInstance:
        """
        Asynchronous coroutine to fetch the IpAddressInstance


        :returns: The fetched IpAddressInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        ip_address: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        cidr_prefix_length: Union[int, object] = values.unset,
    ) -> IpAddressInstance:
        """
        Update the IpAddressInstance

        :param ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :param cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: The updated IpAddressInstance
        """
        data = values.of(
            {
                "IpAddress": ip_address,
                "FriendlyName": friendly_name,
                "CidrPrefixLength": cidr_prefix_length,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        ip_address: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        cidr_prefix_length: Union[int, object] = values.unset,
    ) -> IpAddressInstance:
        """
        Asynchronous coroutine to update the IpAddressInstance

        :param ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :param cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: The updated IpAddressInstance
        """
        data = values.of(
            {
                "IpAddress": ip_address,
                "FriendlyName": friendly_name,
                "CidrPrefixLength": cidr_prefix_length,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.IpAddressContext {}>".format(context)


class IpAddressPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> IpAddressInstance:
        """
        Build an instance of IpAddressInstance

        :param payload: Payload response from the API
        """
        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.IpAddressPage>"


class IpAddressList(ListResource):
    def __init__(
        self, version: Version, account_sid: str, ip_access_control_list_sid: str
    ):
        """
        Initialize the IpAddressList

        :param version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "ip_access_control_list_sid": ip_access_control_list_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json".format(
            **self._solution
        )

    def create(
        self,
        friendly_name: str,
        ip_address: str,
        cidr_prefix_length: Union[int, object] = values.unset,
    ) -> IpAddressInstance:
        """
        Create the IpAddressInstance

        :param friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :param ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: The created IpAddressInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "IpAddress": ip_address,
                "CidrPrefixLength": cidr_prefix_length,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
        )

    async def create_async(
        self,
        friendly_name: str,
        ip_address: str,
        cidr_prefix_length: Union[int, object] = values.unset,
    ) -> IpAddressInstance:
        """
        Asynchronously create the IpAddressInstance

        :param friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :param ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: The created IpAddressInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "IpAddress": ip_address,
                "CidrPrefixLength": cidr_prefix_length,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[IpAddressInstance]:
        """
        Streams IpAddressInstance records from the API as a generator stream.
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
    ) -> List[IpAddressInstance]:
        """
        Asynchronously streams IpAddressInstance records from the API as a generator stream.
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
    ) -> List[IpAddressInstance]:
        """
        Lists IpAddressInstance records from the API as a list.
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
    ) -> List[IpAddressInstance]:
        """
        Asynchronously lists IpAddressInstance records from the API as a list.
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
    ) -> IpAddressPage:
        """
        Retrieve a single page of IpAddressInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of IpAddressInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return IpAddressPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> IpAddressPage:
        """
        Asynchronously retrieve a single page of IpAddressInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of IpAddressInstance
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
        return IpAddressPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> IpAddressPage:
        """
        Retrieve a specific page of IpAddressInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of IpAddressInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return IpAddressPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> IpAddressPage:
        """
        Asynchronously retrieve a specific page of IpAddressInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of IpAddressInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return IpAddressPage(self._version, response, self._solution)

    def get(self, sid: str) -> IpAddressContext:
        """
        Constructs a IpAddressContext

        :param sid: A 34 character string that identifies the IpAddress resource to update.
        """
        return IpAddressContext(
            self._version,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> IpAddressContext:
        """
        Constructs a IpAddressContext

        :param sid: A 34 character string that identifies the IpAddress resource to update.
        """
        return IpAddressContext(
            self._version,
            account_sid=self._solution["account_sid"],
            ip_access_control_list_sid=self._solution["ip_access_control_list_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.IpAddressList>"
