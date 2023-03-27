r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class TrustProductsEvaluationsInstance(InstanceResource):
    class Status(object):
        COMPLIANT = "compliant"
        NONCOMPLIANT = "noncompliant"

    """
    :ivar sid: The unique string that identifies the Evaluation resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the trust_product resource.
    :ivar policy_sid: The unique string of a policy that is associated to the trust_product resource.
    :ivar trust_product_sid: The unique string that we created to identify the trust_product resource.
    :ivar status: 
    :ivar results: The results of the Evaluation which includes the valid and invalid attributes.
    :ivar date_created: 
    :ivar url: 
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        trust_product_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.policy_sid: Optional[str] = payload.get("policy_sid")
        self.trust_product_sid: Optional[str] = payload.get("trust_product_sid")
        self.status: Optional["TrustProductsEvaluationsInstance.Status"] = payload.get(
            "status"
        )
        self.results: Optional[List[object]] = payload.get("results")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "trust_product_sid": trust_product_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[TrustProductsEvaluationsContext] = None

    @property
    def _proxy(self) -> "TrustProductsEvaluationsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TrustProductsEvaluationsContext for this TrustProductsEvaluationsInstance
        """
        if self._context is None:
            self._context = TrustProductsEvaluationsContext(
                self._version,
                trust_product_sid=self._solution["trust_product_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "TrustProductsEvaluationsInstance":
        """
        Fetch the TrustProductsEvaluationsInstance


        :returns: The fetched TrustProductsEvaluationsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "TrustProductsEvaluationsInstance":
        """
        Asynchronous coroutine to fetch the TrustProductsEvaluationsInstance


        :returns: The fetched TrustProductsEvaluationsInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.TrustProductsEvaluationsInstance {}>".format(
            context
        )


class TrustProductsEvaluationsContext(InstanceContext):
    def __init__(self, version: Version, trust_product_sid: str, sid: str):
        """
        Initialize the TrustProductsEvaluationsContext

        :param version: Version that contains the resource
        :param trust_product_sid: The unique string that we created to identify the trust_product resource.
        :param sid: The unique string that identifies the Evaluation resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trust_product_sid": trust_product_sid,
            "sid": sid,
        }
        self._uri = "/TrustProducts/{trust_product_sid}/Evaluations/{sid}".format(
            **self._solution
        )

    def fetch(self) -> TrustProductsEvaluationsInstance:
        """
        Fetch the TrustProductsEvaluationsInstance


        :returns: The fetched TrustProductsEvaluationsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TrustProductsEvaluationsInstance(
            self._version,
            payload,
            trust_product_sid=self._solution["trust_product_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> TrustProductsEvaluationsInstance:
        """
        Asynchronous coroutine to fetch the TrustProductsEvaluationsInstance


        :returns: The fetched TrustProductsEvaluationsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TrustProductsEvaluationsInstance(
            self._version,
            payload,
            trust_product_sid=self._solution["trust_product_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.TrustProductsEvaluationsContext {}>".format(context)


class TrustProductsEvaluationsPage(Page):
    def get_instance(self, payload) -> TrustProductsEvaluationsInstance:
        """
        Build an instance of TrustProductsEvaluationsInstance

        :param dict payload: Payload response from the API
        """
        return TrustProductsEvaluationsInstance(
            self._version,
            payload,
            trust_product_sid=self._solution["trust_product_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.TrustProductsEvaluationsPage>"


class TrustProductsEvaluationsList(ListResource):
    def __init__(self, version: Version, trust_product_sid: str):
        """
        Initialize the TrustProductsEvaluationsList

        :param version: Version that contains the resource
        :param trust_product_sid: The unique string that we created to identify the trust_product resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "trust_product_sid": trust_product_sid,
        }
        self._uri = "/TrustProducts/{trust_product_sid}/Evaluations".format(
            **self._solution
        )

    def create(self, policy_sid) -> TrustProductsEvaluationsInstance:
        """
        Create the TrustProductsEvaluationsInstance

        :param str policy_sid: The unique string of a policy that is associated to the customer_profile resource.

        :returns: The created TrustProductsEvaluationsInstance
        """
        data = values.of(
            {
                "PolicySid": policy_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrustProductsEvaluationsInstance(
            self._version,
            payload,
            trust_product_sid=self._solution["trust_product_sid"],
        )

    async def create_async(self, policy_sid) -> TrustProductsEvaluationsInstance:
        """
        Asynchronously create the TrustProductsEvaluationsInstance

        :param str policy_sid: The unique string of a policy that is associated to the customer_profile resource.

        :returns: The created TrustProductsEvaluationsInstance
        """
        data = values.of(
            {
                "PolicySid": policy_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrustProductsEvaluationsInstance(
            self._version,
            payload,
            trust_product_sid=self._solution["trust_product_sid"],
        )

    def stream(
        self, limit=None, page_size=None
    ) -> List[TrustProductsEvaluationsInstance]:
        """
        Streams TrustProductsEvaluationsInstance records from the API as a generator stream.
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
    ) -> List[TrustProductsEvaluationsInstance]:
        """
        Asynchronously streams TrustProductsEvaluationsInstance records from the API as a generator stream.
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

    def list(
        self, limit=None, page_size=None
    ) -> List[TrustProductsEvaluationsInstance]:
        """
        Lists TrustProductsEvaluationsInstance records from the API as a list.
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
    ) -> List[TrustProductsEvaluationsInstance]:
        """
        Asynchronously lists TrustProductsEvaluationsInstance records from the API as a list.
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
    ) -> TrustProductsEvaluationsPage:
        """
        Retrieve a single page of TrustProductsEvaluationsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TrustProductsEvaluationsInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TrustProductsEvaluationsPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> TrustProductsEvaluationsPage:
        """
        Asynchronously retrieve a single page of TrustProductsEvaluationsInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TrustProductsEvaluationsInstance
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
        return TrustProductsEvaluationsPage(self._version, response, self._solution)

    def get_page(self, target_url) -> TrustProductsEvaluationsPage:
        """
        Retrieve a specific page of TrustProductsEvaluationsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TrustProductsEvaluationsInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TrustProductsEvaluationsPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> TrustProductsEvaluationsPage:
        """
        Asynchronously retrieve a specific page of TrustProductsEvaluationsInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TrustProductsEvaluationsInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return TrustProductsEvaluationsPage(self._version, response, self._solution)

    def get(self, sid) -> TrustProductsEvaluationsContext:
        """
        Constructs a TrustProductsEvaluationsContext

        :param sid: The unique string that identifies the Evaluation resource.
        """
        return TrustProductsEvaluationsContext(
            self._version,
            trust_product_sid=self._solution["trust_product_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> TrustProductsEvaluationsContext:
        """
        Constructs a TrustProductsEvaluationsContext

        :param sid: The unique string that identifies the Evaluation resource.
        """
        return TrustProductsEvaluationsContext(
            self._version,
            trust_product_sid=self._solution["trust_product_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.TrustProductsEvaluationsList>"
