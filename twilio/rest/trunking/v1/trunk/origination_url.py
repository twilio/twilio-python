r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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


class OriginationUrlInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the OriginationUrl resource.
    :ivar sid: The unique string that we created to identify the OriginationUrl resource.
    :ivar trunk_sid: The SID of the Trunk that owns the Origination URL.
    :ivar weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
    :ivar enabled: Whether the URL is enabled. The default is `true`.
    :ivar sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar url: The absolute URL of the resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        trunk_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.trunk_sid: Optional[str] = payload.get("trunk_sid")
        self.weight: Optional[int] = deserialize.integer(payload.get("weight"))
        self.enabled: Optional[bool] = payload.get("enabled")
        self.sip_url: Optional[str] = payload.get("sip_url")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.priority: Optional[int] = deserialize.integer(payload.get("priority"))
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[OriginationUrlContext] = None

    @property
    def _proxy(self) -> "OriginationUrlContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: OriginationUrlContext for this OriginationUrlInstance
        """
        if self._context is None:
            self._context = OriginationUrlContext(
                self._version,
                trunk_sid=self._solution["trunk_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the OriginationUrlInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the OriginationUrlInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "OriginationUrlInstance":
        """
        Fetch the OriginationUrlInstance


        :returns: The fetched OriginationUrlInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "OriginationUrlInstance":
        """
        Asynchronous coroutine to fetch the OriginationUrlInstance


        :returns: The fetched OriginationUrlInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        weight: Union[int, object] = values.unset,
        priority: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        sip_url: Union[str, object] = values.unset,
    ) -> "OriginationUrlInstance":
        """
        Update the OriginationUrlInstance

        :param weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :param priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :param enabled: Whether the URL is enabled. The default is `true`.
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.

        :returns: The updated OriginationUrlInstance
        """
        return self._proxy.update(
            weight=weight,
            priority=priority,
            enabled=enabled,
            friendly_name=friendly_name,
            sip_url=sip_url,
        )

    async def update_async(
        self,
        weight: Union[int, object] = values.unset,
        priority: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        sip_url: Union[str, object] = values.unset,
    ) -> "OriginationUrlInstance":
        """
        Asynchronous coroutine to update the OriginationUrlInstance

        :param weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :param priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :param enabled: Whether the URL is enabled. The default is `true`.
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.

        :returns: The updated OriginationUrlInstance
        """
        return await self._proxy.update_async(
            weight=weight,
            priority=priority,
            enabled=enabled,
            friendly_name=friendly_name,
            sip_url=sip_url,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.OriginationUrlInstance {}>".format(context)


class OriginationUrlContext(InstanceContext):
    def __init__(self, version: Version, trunk_sid: str, sid: str):
        """
        Initialize the OriginationUrlContext

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to update the OriginationUrl.
        :param sid: The unique string that we created to identify the OriginationUrl resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
            "sid": sid,
        }
        self._uri = "/Trunks/{trunk_sid}/OriginationUrls/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the OriginationUrlInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the OriginationUrlInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> OriginationUrlInstance:
        """
        Fetch the OriginationUrlInstance


        :returns: The fetched OriginationUrlInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> OriginationUrlInstance:
        """
        Asynchronous coroutine to fetch the OriginationUrlInstance


        :returns: The fetched OriginationUrlInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        weight: Union[int, object] = values.unset,
        priority: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        sip_url: Union[str, object] = values.unset,
    ) -> OriginationUrlInstance:
        """
        Update the OriginationUrlInstance

        :param weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :param priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :param enabled: Whether the URL is enabled. The default is `true`.
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.

        :returns: The updated OriginationUrlInstance
        """
        data = values.of(
            {
                "Weight": weight,
                "Priority": priority,
                "Enabled": enabled,
                "FriendlyName": friendly_name,
                "SipUrl": sip_url,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        weight: Union[int, object] = values.unset,
        priority: Union[int, object] = values.unset,
        enabled: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        sip_url: Union[str, object] = values.unset,
    ) -> OriginationUrlInstance:
        """
        Asynchronous coroutine to update the OriginationUrlInstance

        :param weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :param priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :param enabled: Whether the URL is enabled. The default is `true`.
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema. `sips` is NOT supported.

        :returns: The updated OriginationUrlInstance
        """
        data = values.of(
            {
                "Weight": weight,
                "Priority": priority,
                "Enabled": enabled,
                "FriendlyName": friendly_name,
                "SipUrl": sip_url,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return OriginationUrlInstance(
            self._version,
            payload,
            trunk_sid=self._solution["trunk_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.OriginationUrlContext {}>".format(context)


class OriginationUrlPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> OriginationUrlInstance:
        """
        Build an instance of OriginationUrlInstance

        :param payload: Payload response from the API
        """
        return OriginationUrlInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.OriginationUrlPage>"


class OriginationUrlList(ListResource):
    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the OriginationUrlList

        :param version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the OriginationUrl.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trunk_sid": trunk_sid,
        }
        self._uri = "/Trunks/{trunk_sid}/OriginationUrls".format(**self._solution)

    def create(
        self,
        weight: int,
        priority: int,
        enabled: bool,
        friendly_name: str,
        sip_url: str,
    ) -> OriginationUrlInstance:
        """
        Create the OriginationUrlInstance

        :param weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :param priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :param enabled: Whether the URL is enabled. The default is `true`.
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema.

        :returns: The created OriginationUrlInstance
        """
        data = values.of(
            {
                "Weight": weight,
                "Priority": priority,
                "Enabled": enabled,
                "FriendlyName": friendly_name,
                "SipUrl": sip_url,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return OriginationUrlInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    async def create_async(
        self,
        weight: int,
        priority: int,
        enabled: bool,
        friendly_name: str,
        sip_url: str,
    ) -> OriginationUrlInstance:
        """
        Asynchronously create the OriginationUrlInstance

        :param weight: The value that determines the relative share of the load the URI should receive compared to other URIs with the same priority. Can be an integer from 1 to 65535, inclusive, and the default is 10. URLs with higher values receive more load than those with lower ones with the same priority.
        :param priority: The relative importance of the URI. Can be an integer from 0 to 65535, inclusive, and the default is 10. The lowest number represents the most important URI.
        :param enabled: Whether the URL is enabled. The default is `true`.
        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param sip_url: The SIP address you want Twilio to route your Origination calls to. This must be a `sip:` schema.

        :returns: The created OriginationUrlInstance
        """
        data = values.of(
            {
                "Weight": weight,
                "Priority": priority,
                "Enabled": enabled,
                "FriendlyName": friendly_name,
                "SipUrl": sip_url,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return OriginationUrlInstance(
            self._version, payload, trunk_sid=self._solution["trunk_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[OriginationUrlInstance]:
        """
        Streams OriginationUrlInstance records from the API as a generator stream.
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
    ) -> List[OriginationUrlInstance]:
        """
        Asynchronously streams OriginationUrlInstance records from the API as a generator stream.
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
    ) -> List[OriginationUrlInstance]:
        """
        Lists OriginationUrlInstance records from the API as a list.
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
    ) -> List[OriginationUrlInstance]:
        """
        Asynchronously lists OriginationUrlInstance records from the API as a list.
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
    ) -> OriginationUrlPage:
        """
        Retrieve a single page of OriginationUrlInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of OriginationUrlInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return OriginationUrlPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> OriginationUrlPage:
        """
        Asynchronously retrieve a single page of OriginationUrlInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of OriginationUrlInstance
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
        return OriginationUrlPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> OriginationUrlPage:
        """
        Retrieve a specific page of OriginationUrlInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of OriginationUrlInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return OriginationUrlPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> OriginationUrlPage:
        """
        Asynchronously retrieve a specific page of OriginationUrlInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of OriginationUrlInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return OriginationUrlPage(self._version, response, self._solution)

    def get(self, sid: str) -> OriginationUrlContext:
        """
        Constructs a OriginationUrlContext

        :param sid: The unique string that we created to identify the OriginationUrl resource to update.
        """
        return OriginationUrlContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __call__(self, sid: str) -> OriginationUrlContext:
        """
        Constructs a OriginationUrlContext

        :param sid: The unique string that we created to identify the OriginationUrl resource to update.
        """
        return OriginationUrlContext(
            self._version, trunk_sid=self._solution["trunk_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.OriginationUrlList>"
