r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class InsightsQuestionnairesCategoryInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Flex Insights resource and owns this resource.
    :ivar category_id: The unique ID for the category
    :ivar name: The name of this category.
    :ivar url:
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        category_id: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.category_id: Optional[str] = payload.get("category_id")
        self.name: Optional[str] = payload.get("name")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "category_id": category_id or self.category_id,
        }
        self._context: Optional[InsightsQuestionnairesCategoryContext] = None

    @property
    def _proxy(self) -> "InsightsQuestionnairesCategoryContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsQuestionnairesCategoryContext for this InsightsQuestionnairesCategoryInstance
        """
        if self._context is None:
            self._context = InsightsQuestionnairesCategoryContext(
                self._version,
                category_id=self._solution["category_id"],
            )
        return self._context

    def delete(self, token: Union[str, object] = values.unset) -> bool:
        """
        Deletes the InsightsQuestionnairesCategoryInstance

        :param token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete(
            token=token,
        )

    async def delete_async(self, token: Union[str, object] = values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the InsightsQuestionnairesCategoryInstance

        :param token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async(
            token=token,
        )

    def update(
        self, name: str, token: Union[str, object] = values.unset
    ) -> "InsightsQuestionnairesCategoryInstance":
        """
        Update the InsightsQuestionnairesCategoryInstance

        :param name: The name of this category.
        :param token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        """
        return self._proxy.update(
            name=name,
            token=token,
        )

    async def update_async(
        self, name: str, token: Union[str, object] = values.unset
    ) -> "InsightsQuestionnairesCategoryInstance":
        """
        Asynchronous coroutine to update the InsightsQuestionnairesCategoryInstance

        :param name: The name of this category.
        :param token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        """
        return await self._proxy.update_async(
            name=name,
            token=token,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryInstance {}>".format(
            context
        )


class InsightsQuestionnairesCategoryContext(InstanceContext):
    def __init__(self, version: Version, category_id: str):
        """
        Initialize the InsightsQuestionnairesCategoryContext

        :param version: Version that contains the resource
        :param category_id: The ID of the category to be update
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "category_id": category_id,
        }
        self._uri = "/Insights/QM/Categories/{category_id}".format(**self._solution)

    def delete(self, token: Union[str, object] = values.unset) -> bool:
        """
        Deletes the InsightsQuestionnairesCategoryInstance

        :param token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "Token": token,
            }
        )

        return self._version.delete(method="DELETE", uri=self._uri, headers=headers)

    async def delete_async(self, token: Union[str, object] = values.unset) -> bool:
        """
        Asynchronous coroutine that deletes the InsightsQuestionnairesCategoryInstance

        :param token: The Token HTTP request header

        :returns: True if delete succeeds, False otherwise
        """
        headers = values.of(
            {
                "Token": token,
            }
        )

        return await self._version.delete_async(
            method="DELETE", uri=self._uri, headers=headers
        )

    def update(
        self, name: str, token: Union[str, object] = values.unset
    ) -> InsightsQuestionnairesCategoryInstance:
        """
        Update the InsightsQuestionnairesCategoryInstance

        :param name: The name of this category.
        :param token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        """
        data = values.of(
            {
                "Name": name,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )

        payload = self._version.update(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsQuestionnairesCategoryInstance(
            self._version, payload, category_id=self._solution["category_id"]
        )

    async def update_async(
        self, name: str, token: Union[str, object] = values.unset
    ) -> InsightsQuestionnairesCategoryInstance:
        """
        Asynchronous coroutine to update the InsightsQuestionnairesCategoryInstance

        :param name: The name of this category.
        :param token: The Token HTTP request header

        :returns: The updated InsightsQuestionnairesCategoryInstance
        """
        data = values.of(
            {
                "Name": name,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )

        payload = await self._version.update_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsQuestionnairesCategoryInstance(
            self._version, payload, category_id=self._solution["category_id"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryContext {}>".format(
            context
        )


class InsightsQuestionnairesCategoryPage(Page):
    def get_instance(
        self, payload: Dict[str, Any]
    ) -> InsightsQuestionnairesCategoryInstance:
        """
        Build an instance of InsightsQuestionnairesCategoryInstance

        :param payload: Payload response from the API
        """
        return InsightsQuestionnairesCategoryInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryPage>"


class InsightsQuestionnairesCategoryList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the InsightsQuestionnairesCategoryList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Insights/QM/Categories"

    def create(
        self, name: str, token: Union[str, object] = values.unset
    ) -> InsightsQuestionnairesCategoryInstance:
        """
        Create the InsightsQuestionnairesCategoryInstance

        :param name: The name of this category.
        :param token: The Token HTTP request header

        :returns: The created InsightsQuestionnairesCategoryInstance
        """
        data = values.of(
            {
                "Name": name,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsQuestionnairesCategoryInstance(self._version, payload)

    async def create_async(
        self, name: str, token: Union[str, object] = values.unset
    ) -> InsightsQuestionnairesCategoryInstance:
        """
        Asynchronously create the InsightsQuestionnairesCategoryInstance

        :param name: The name of this category.
        :param token: The Token HTTP request header

        :returns: The created InsightsQuestionnairesCategoryInstance
        """
        data = values.of(
            {
                "Name": name,
            }
        )
        headers = values.of(
            {
                "Token": token,
            }
        )
        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return InsightsQuestionnairesCategoryInstance(self._version, payload)

    def stream(
        self,
        token: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsQuestionnairesCategoryInstance]:
        """
        Streams InsightsQuestionnairesCategoryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(token=token, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        token: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsQuestionnairesCategoryInstance]:
        """
        Asynchronously streams InsightsQuestionnairesCategoryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str token: The Token HTTP request header
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(token=token, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        token: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsQuestionnairesCategoryInstance]:
        """
        Lists InsightsQuestionnairesCategoryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
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
                token=token,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        token: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[InsightsQuestionnairesCategoryInstance]:
        """
        Asynchronously lists InsightsQuestionnairesCategoryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str token: The Token HTTP request header
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
                token=token,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        token: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InsightsQuestionnairesCategoryPage:
        """
        Retrieve a single page of InsightsQuestionnairesCategoryInstance records from the API.
        Request is executed immediately

        :param token: The Token HTTP request header
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesCategoryInstance
        """
        data = values.of(
            {
                "Token": token,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return InsightsQuestionnairesCategoryPage(self._version, response)

    async def page_async(
        self,
        token: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> InsightsQuestionnairesCategoryPage:
        """
        Asynchronously retrieve a single page of InsightsQuestionnairesCategoryInstance records from the API.
        Request is executed immediately

        :param token: The Token HTTP request header
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of InsightsQuestionnairesCategoryInstance
        """
        data = values.of(
            {
                "Token": token,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return InsightsQuestionnairesCategoryPage(self._version, response)

    def get_page(self, target_url: str) -> InsightsQuestionnairesCategoryPage:
        """
        Retrieve a specific page of InsightsQuestionnairesCategoryInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesCategoryInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return InsightsQuestionnairesCategoryPage(self._version, response)

    async def get_page_async(
        self, target_url: str
    ) -> InsightsQuestionnairesCategoryPage:
        """
        Asynchronously retrieve a specific page of InsightsQuestionnairesCategoryInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of InsightsQuestionnairesCategoryInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return InsightsQuestionnairesCategoryPage(self._version, response)

    def get(self, category_id: str) -> InsightsQuestionnairesCategoryContext:
        """
        Constructs a InsightsQuestionnairesCategoryContext

        :param category_id: The ID of the category to be update
        """
        return InsightsQuestionnairesCategoryContext(
            self._version, category_id=category_id
        )

    def __call__(self, category_id: str) -> InsightsQuestionnairesCategoryContext:
        """
        Constructs a InsightsQuestionnairesCategoryContext

        :param category_id: The ID of the category to be update
        """
        return InsightsQuestionnairesCategoryContext(
            self._version, category_id=category_id
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.FlexApi.V1.InsightsQuestionnairesCategoryList>"
