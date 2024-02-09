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
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ShortCodeInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this ShortCode resource.
    :ivar api_version: The API version used to start a new TwiML session when an SMS message is sent to this short code.
    :ivar date_created: The date and time in GMT that this resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar friendly_name: A string that you assigned to describe this resource. By default, the `FriendlyName` is the short code.
    :ivar short_code: The short code. e.g., 894546.
    :ivar sid: The unique string that that we created to identify this ShortCode resource.
    :ivar sms_fallback_method: The HTTP method we use to call the `sms_fallback_url`. Can be: `GET` or `POST`.
    :ivar sms_fallback_url: The URL that we call if an error occurs while retrieving or executing the TwiML from `sms_url`.
    :ivar sms_method: The HTTP method we use to call the `sms_url`. Can be: `GET` or `POST`.
    :ivar sms_url: The URL we call when receiving an incoming SMS message to this short code.
    :ivar uri: The URI of this resource, relative to `https://api.twilio.com`.
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
        self.api_version: Optional[str] = payload.get("api_version")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.short_code: Optional[str] = payload.get("short_code")
        self.sid: Optional[str] = payload.get("sid")
        self.sms_fallback_method: Optional[str] = payload.get("sms_fallback_method")
        self.sms_fallback_url: Optional[str] = payload.get("sms_fallback_url")
        self.sms_method: Optional[str] = payload.get("sms_method")
        self.sms_url: Optional[str] = payload.get("sms_url")
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ShortCodeContext] = None

    @property
    def _proxy(self) -> "ShortCodeContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ShortCodeContext for this ShortCodeInstance
        """
        if self._context is None:
            self._context = ShortCodeContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "ShortCodeInstance":
        """
        Fetch the ShortCodeInstance


        :returns: The fetched ShortCodeInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ShortCodeInstance":
        """
        Asynchronous coroutine to fetch the ShortCodeInstance


        :returns: The fetched ShortCodeInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        api_version: Union[str, object] = values.unset,
        sms_url: Union[str, object] = values.unset,
        sms_method: Union[str, object] = values.unset,
        sms_fallback_url: Union[str, object] = values.unset,
        sms_fallback_method: Union[str, object] = values.unset,
    ) -> "ShortCodeInstance":
        """
        Update the ShortCodeInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the `FriendlyName` is the short code.
        :param api_version: The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`.
        :param sms_url: The URL we should call when receiving an incoming SMS message to this short code.
        :param sms_method: The HTTP method we should use when calling the `sms_url`. Can be: `GET` or `POST`.
        :param sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML from `sms_url`.
        :param sms_fallback_method: The HTTP method that we should use to call the `sms_fallback_url`. Can be: `GET` or `POST`.

        :returns: The updated ShortCodeInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            api_version=api_version,
            sms_url=sms_url,
            sms_method=sms_method,
            sms_fallback_url=sms_fallback_url,
            sms_fallback_method=sms_fallback_method,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        api_version: Union[str, object] = values.unset,
        sms_url: Union[str, object] = values.unset,
        sms_method: Union[str, object] = values.unset,
        sms_fallback_url: Union[str, object] = values.unset,
        sms_fallback_method: Union[str, object] = values.unset,
    ) -> "ShortCodeInstance":
        """
        Asynchronous coroutine to update the ShortCodeInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the `FriendlyName` is the short code.
        :param api_version: The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`.
        :param sms_url: The URL we should call when receiving an incoming SMS message to this short code.
        :param sms_method: The HTTP method we should use when calling the `sms_url`. Can be: `GET` or `POST`.
        :param sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML from `sms_url`.
        :param sms_fallback_method: The HTTP method that we should use to call the `sms_fallback_url`. Can be: `GET` or `POST`.

        :returns: The updated ShortCodeInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            api_version=api_version,
            sms_url=sms_url,
            sms_method=sms_method,
            sms_fallback_url=sms_fallback_url,
            sms_fallback_method=sms_fallback_method,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.ShortCodeInstance {}>".format(context)


class ShortCodeContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the ShortCodeContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to update.
        :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/SMS/ShortCodes/{sid}.json".format(
            **self._solution
        )

    def fetch(self) -> ShortCodeInstance:
        """
        Fetch the ShortCodeInstance


        :returns: The fetched ShortCodeInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ShortCodeInstance:
        """
        Asynchronous coroutine to fetch the ShortCodeInstance


        :returns: The fetched ShortCodeInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        api_version: Union[str, object] = values.unset,
        sms_url: Union[str, object] = values.unset,
        sms_method: Union[str, object] = values.unset,
        sms_fallback_url: Union[str, object] = values.unset,
        sms_fallback_method: Union[str, object] = values.unset,
    ) -> ShortCodeInstance:
        """
        Update the ShortCodeInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the `FriendlyName` is the short code.
        :param api_version: The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`.
        :param sms_url: The URL we should call when receiving an incoming SMS message to this short code.
        :param sms_method: The HTTP method we should use when calling the `sms_url`. Can be: `GET` or `POST`.
        :param sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML from `sms_url`.
        :param sms_fallback_method: The HTTP method that we should use to call the `sms_fallback_url`. Can be: `GET` or `POST`.

        :returns: The updated ShortCodeInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "ApiVersion": api_version,
                "SmsUrl": sms_url,
                "SmsMethod": sms_method,
                "SmsFallbackUrl": sms_fallback_url,
                "SmsFallbackMethod": sms_fallback_method,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        api_version: Union[str, object] = values.unset,
        sms_url: Union[str, object] = values.unset,
        sms_method: Union[str, object] = values.unset,
        sms_fallback_url: Union[str, object] = values.unset,
        sms_fallback_method: Union[str, object] = values.unset,
    ) -> ShortCodeInstance:
        """
        Asynchronous coroutine to update the ShortCodeInstance

        :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the `FriendlyName` is the short code.
        :param api_version: The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`.
        :param sms_url: The URL we should call when receiving an incoming SMS message to this short code.
        :param sms_method: The HTTP method we should use when calling the `sms_url`. Can be: `GET` or `POST`.
        :param sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML from `sms_url`.
        :param sms_fallback_method: The HTTP method that we should use to call the `sms_fallback_url`. Can be: `GET` or `POST`.

        :returns: The updated ShortCodeInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "ApiVersion": api_version,
                "SmsUrl": sms_url,
                "SmsMethod": sms_method,
                "SmsFallbackUrl": sms_fallback_url,
                "SmsFallbackMethod": sms_fallback_method,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ShortCodeInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.ShortCodeContext {}>".format(context)


class ShortCodePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ShortCodeInstance:
        """
        Build an instance of ShortCodeInstance

        :param payload: Payload response from the API
        """
        return ShortCodeInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.ShortCodePage>"


class ShortCodeList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the ShortCodeList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/SMS/ShortCodes.json".format(
            **self._solution
        )

    def stream(
        self,
        friendly_name: Union[str, object] = values.unset,
        short_code: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ShortCodeInstance]:
        """
        Streams ShortCodeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str friendly_name: The string that identifies the ShortCode resources to read.
        :param str short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name,
            short_code=short_code,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        short_code: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[ShortCodeInstance]:
        """
        Asynchronously streams ShortCodeInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str friendly_name: The string that identifies the ShortCode resources to read.
        :param str short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.
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
            friendly_name=friendly_name,
            short_code=short_code,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        friendly_name: Union[str, object] = values.unset,
        short_code: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ShortCodeInstance]:
        """
        Lists ShortCodeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str friendly_name: The string that identifies the ShortCode resources to read.
        :param str short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.
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
                friendly_name=friendly_name,
                short_code=short_code,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        short_code: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ShortCodeInstance]:
        """
        Asynchronously lists ShortCodeInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str friendly_name: The string that identifies the ShortCode resources to read.
        :param str short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.
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
                friendly_name=friendly_name,
                short_code=short_code,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        friendly_name: Union[str, object] = values.unset,
        short_code: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ShortCodePage:
        """
        Retrieve a single page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param friendly_name: The string that identifies the ShortCode resources to read.
        :param short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ShortCodeInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "ShortCode": short_code,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ShortCodePage(self._version, response, self._solution)

    async def page_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        short_code: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ShortCodePage:
        """
        Asynchronously retrieve a single page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param friendly_name: The string that identifies the ShortCode resources to read.
        :param short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ShortCodeInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "ShortCode": short_code,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return ShortCodePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ShortCodePage:
        """
        Retrieve a specific page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ShortCodeInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ShortCodePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ShortCodePage:
        """
        Asynchronously retrieve a specific page of ShortCodeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ShortCodeInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ShortCodePage(self._version, response, self._solution)

    def get(self, sid: str) -> ShortCodeContext:
        """
        Constructs a ShortCodeContext

        :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update
        """
        return ShortCodeContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid: str) -> ShortCodeContext:
        """
        Constructs a ShortCodeContext

        :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update
        """
        return ShortCodeContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.ShortCodeList>"
