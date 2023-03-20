r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Proxy
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class PhoneNumberInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, sid: Optional[str] = None):
        """
        Initialize the PhoneNumberInstance

        :returns: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "account_sid": payload.get("account_sid"),
            "service_sid": payload.get("service_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "date_updated": deserialize.iso8601_datetime(payload.get("date_updated")),
            "phone_number": payload.get("phone_number"),
            "friendly_name": payload.get("friendly_name"),
            "iso_country": payload.get("iso_country"),
            "capabilities": payload.get("capabilities"),
            "url": payload.get("url"),
            "is_reserved": payload.get("is_reserved"),
            "in_use": deserialize.integer(payload.get("in_use")),
        }

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[PhoneNumberContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the PhoneNumber resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the PhoneNumber resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def service_sid(self):
        """
        :returns: The SID of the PhoneNumber resource's parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
        :rtype: str
        """
        return self._properties["service_sid"]

    @property
    def date_created(self):
        """
        :returns: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def date_updated(self):
        """
        :returns: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated.
        :rtype: datetime
        """
        return self._properties["date_updated"]

    @property
    def phone_number(self):
        """
        :returns: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :rtype: str
        """
        return self._properties["phone_number"]

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties["friendly_name"]

    @property
    def iso_country(self):
        """
        :returns: The ISO Country Code for the phone number.
        :rtype: str
        """
        return self._properties["iso_country"]

    @property
    def capabilities(self):
        """
        :returns:
        :rtype: ProxyV1ServicePhoneNumberCapabilities
        """
        return self._properties["capabilities"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the PhoneNumber resource.
        :rtype: str
        """
        return self._properties["url"]

    @property
    def is_reserved(self):
        """
        :returns: Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.
        :rtype: bool
        """
        return self._properties["is_reserved"]

    @property
    def in_use(self):
        """
        :returns: The number of open session assigned to the number. See the [How many Phone Numbers do I need?](https://www.twilio.com/docs/proxy/phone-numbers-needed) guide for more information.
        :rtype: int
        """
        return self._properties["in_use"]

    def delete(self):
        """
        Deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        return await self._proxy.fetch_async()

    def update(self, is_reserved=values.unset):
        """
        Update the PhoneNumberInstance

        :param bool is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The updated PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        return self._proxy.update(
            is_reserved=is_reserved,
        )

    async def update_async(self, is_reserved=values.unset):
        """
        Asynchronous coroutine to update the PhoneNumberInstance

        :param bool is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The updated PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        return await self._proxy.update_async(
            is_reserved=is_reserved,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.PhoneNumberInstance {}>".format(context)


class PhoneNumberContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.

        :returns: twilio.rest.proxy.v1.service.phone_number.PhoneNumberContext
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/PhoneNumbers/{sid}".format(
            **self._solution
        )

    def delete(self):
        """
        Deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the PhoneNumberInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the PhoneNumberInstance


        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(self, is_reserved=values.unset):
        """
        Update the PhoneNumberInstance

        :param bool is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The updated PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        data = values.of(
            {
                "IsReserved": is_reserved,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(self, is_reserved=values.unset):
        """
        Asynchronous coroutine to update the PhoneNumberInstance

        :param bool is_reserved: Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The updated PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        data = values.of(
            {
                "IsReserved": is_reserved,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.PhoneNumberContext {}>".format(context)


class PhoneNumberList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resources to read.

        :returns: twilio.rest.proxy.v1.service.phone_number.PhoneNumberList
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/PhoneNumbers".format(**self._solution)

    def create(
        self, sid=values.unset, phone_number=values.unset, is_reserved=values.unset
    ):
        """
        Create the PhoneNumberInstance

        :param str sid: The SID of a Twilio [IncomingPhoneNumber](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) resource that represents the Twilio Number you would like to assign to your Proxy Service.
        :param str phone_number: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
        :param bool is_reserved: Whether the new phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The created PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        data = values.of(
            {
                "Sid": sid,
                "PhoneNumber": phone_number,
                "IsReserved": is_reserved,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self, sid=values.unset, phone_number=values.unset, is_reserved=values.unset
    ):
        """
        Asynchronously create the PhoneNumberInstance

        :param str sid: The SID of a Twilio [IncomingPhoneNumber](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) resource that represents the Twilio Number you would like to assign to your Proxy Service.
        :param str phone_number: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
        :param bool is_reserved: Whether the new phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.

        :returns: The created PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        data = values.of(
            {
                "Sid": sid,
                "PhoneNumber": phone_number,
                "IsReserved": is_reserved,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return PhoneNumberInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams PhoneNumberInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams PhoneNumberInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists PhoneNumberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance]
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
        Retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return PhoneNumberPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberPage
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
        return PhoneNumberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return PhoneNumberPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of PhoneNumberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return PhoneNumberPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a PhoneNumberContext

        :param sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.

        :returns: twilio.rest.proxy.v1.service.phone_number.PhoneNumberContext
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a PhoneNumberContext

        :param sid: The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.

        :returns: twilio.rest.proxy.v1.service.phone_number.PhoneNumberContext
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Proxy.V1.PhoneNumberList>"


class PhoneNumberPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.proxy.v1.service.phone_number.PhoneNumberInstance
        """
        return PhoneNumberInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.PhoneNumberPage>"
