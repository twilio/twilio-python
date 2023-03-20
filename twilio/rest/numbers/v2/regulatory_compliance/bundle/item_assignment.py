r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
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


class ItemAssignmentInstance(InstanceResource):
    def __init__(self, version, payload, bundle_sid: str, sid: Optional[str] = None):
        """
        Initialize the ItemAssignmentInstance

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        """
        super().__init__(version)

        self._properties = {
            "sid": payload.get("sid"),
            "bundle_sid": payload.get("bundle_sid"),
            "account_sid": payload.get("account_sid"),
            "object_sid": payload.get("object_sid"),
            "date_created": deserialize.iso8601_datetime(payload.get("date_created")),
            "url": payload.get("url"),
        }

        self._solution = {
            "bundle_sid": bundle_sid,
            "sid": sid or self._properties["sid"],
        }
        self._context: Optional[ItemAssignmentContext] = None

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ItemAssignmentContext for this ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentContext
        """
        if self._context is None:
            self._context = ItemAssignmentContext(
                self._version,
                bundle_sid=self._solution["bundle_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Item Assignment resource.
        :rtype: str
        """
        return self._properties["sid"]

    @property
    def bundle_sid(self):
        """
        :returns: The unique string that we created to identify the Bundle resource.
        :rtype: str
        """
        return self._properties["bundle_sid"]

    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Item Assignment resource.
        :rtype: str
        """
        return self._properties["account_sid"]

    @property
    def object_sid(self):
        """
        :returns: The SID of an object bag that holds information of the different items.
        :rtype: str
        """
        return self._properties["object_sid"]

    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties["date_created"]

    @property
    def url(self):
        """
        :returns: The absolute URL of the Identity resource.
        :rtype: str
        """
        return self._properties["url"]

    def delete(self):
        """
        Deletes the ItemAssignmentInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ItemAssignmentInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._proxy.delete_async()

    def fetch(self):
        """
        Fetch the ItemAssignmentInstance


        :returns: The fetched ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ItemAssignmentInstance


        :returns: The fetched ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.ItemAssignmentInstance {}>".format(context)


class ItemAssignmentContext(InstanceContext):
    def __init__(self, version: Version, bundle_sid: str, sid: str):
        """
        Initialize the ItemAssignmentContext

        :param Version version: Version that contains the resource
        :param bundle_sid: The unique string that we created to identify the Bundle resource.
        :param sid: The unique string that we created to identify the Identity resource.

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "bundle_sid": bundle_sid,
            "sid": sid,
        }
        self._uri = (
            "/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments/{sid}".format(
                **self._solution
            )
        )

    def delete(self):
        """
        Deletes the ItemAssignmentInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self):
        """
        Asynchronous coroutine that deletes the ItemAssignmentInstance


        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self):
        """
        Fetch the ItemAssignmentInstance


        :returns: The fetched ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ItemAssignmentInstance(
            self._version,
            payload,
            bundle_sid=self._solution["bundle_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ItemAssignmentInstance


        :returns: The fetched ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ItemAssignmentInstance(
            self._version,
            payload,
            bundle_sid=self._solution["bundle_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Numbers.V2.ItemAssignmentContext {}>".format(context)


class ItemAssignmentList(ListResource):
    def __init__(self, version: Version, bundle_sid: str):
        """
        Initialize the ItemAssignmentList

        :param Version version: Version that contains the resource
        :param bundle_sid: The unique string that we created to identify the Bundle resource.

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "bundle_sid": bundle_sid,
        }
        self._uri = "/RegulatoryCompliance/Bundles/{bundle_sid}/ItemAssignments".format(
            **self._solution
        )

    def create(self, object_sid):
        """
        Create the ItemAssignmentInstance

        :param str object_sid: The SID of an object bag that holds information of the different items.

        :returns: The created ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        """
        data = values.of(
            {
                "ObjectSid": object_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ItemAssignmentInstance(
            self._version, payload, bundle_sid=self._solution["bundle_sid"]
        )

    async def create_async(self, object_sid):
        """
        Asynchronously create the ItemAssignmentInstance

        :param str object_sid: The SID of an object bag that holds information of the different items.

        :returns: The created ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        """
        data = values.of(
            {
                "ObjectSid": object_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ItemAssignmentInstance(
            self._version, payload, bundle_sid=self._solution["bundle_sid"]
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams ItemAssignmentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams ItemAssignmentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(self, limit=None, page_size=None):
        """
        Lists ItemAssignmentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance]
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists ItemAssignmentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance]
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
        Retrieve a single page of ItemAssignmentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentPage
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ItemAssignmentPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ):
        """
        Asynchronously retrieve a single page of ItemAssignmentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentPage
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
        return ItemAssignmentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ItemAssignmentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentPage
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ItemAssignmentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of ItemAssignmentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentPage
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ItemAssignmentPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a ItemAssignmentContext

        :param sid: The unique string that we created to identify the Identity resource.

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentContext
        """
        return ItemAssignmentContext(
            self._version, bundle_sid=self._solution["bundle_sid"], sid=sid
        )

    def __call__(self, sid):
        """
        Constructs a ItemAssignmentContext

        :param sid: The unique string that we created to identify the Identity resource.

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentContext
        """
        return ItemAssignmentContext(
            self._version, bundle_sid=self._solution["bundle_sid"], sid=sid
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return "<Twilio.Numbers.V2.ItemAssignmentList>"


class ItemAssignmentPage(Page):
    def get_instance(self, payload):
        """
        Build an instance of ItemAssignmentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment.ItemAssignmentInstance
        """
        return ItemAssignmentInstance(
            self._version, payload, bundle_sid=self._solution["bundle_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Numbers.V2.ItemAssignmentPage>"
