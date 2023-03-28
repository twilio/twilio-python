r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
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
from twilio.rest.serverless.v1.service.environment.deployment import DeploymentList
from twilio.rest.serverless.v1.service.environment.log import LogList
from twilio.rest.serverless.v1.service.environment.variable import VariableList


class EnvironmentInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Environment resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Environment resource.
    :ivar service_sid: The SID of the Service that the Environment resource is associated with.
    :ivar build_sid: The SID of the build deployed in the environment.
    :ivar unique_name: A user-defined string that uniquely identifies the Environment resource.
    :ivar domain_suffix: A URL-friendly name that represents the environment and forms part of the domain name.
    :ivar domain_name: The domain name for all Functions and Assets deployed in the Environment, using the Service unique name, a randomly-generated Service suffix, and an optional Environment domain suffix.
    :ivar date_created: The date and time in GMT when the Environment resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Environment resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Environment resource.
    :ivar links: The URLs of the Environment resource's nested resources.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.build_sid: Optional[str] = payload.get("build_sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.domain_suffix: Optional[str] = payload.get("domain_suffix")
        self.domain_name: Optional[str] = payload.get("domain_name")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[EnvironmentContext] = None

    @property
    def _proxy(self) -> "EnvironmentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EnvironmentContext for this EnvironmentInstance
        """
        if self._context is None:
            self._context = EnvironmentContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the EnvironmentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the EnvironmentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "EnvironmentInstance":
        """
        Fetch the EnvironmentInstance


        :returns: The fetched EnvironmentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "EnvironmentInstance":
        """
        Asynchronous coroutine to fetch the EnvironmentInstance


        :returns: The fetched EnvironmentInstance
        """
        return await self._proxy.fetch_async()

    @property
    def deployments(self) -> DeploymentList:
        """
        Access the deployments
        """
        return self._proxy.deployments

    @property
    def logs(self) -> LogList:
        """
        Access the logs
        """
        return self._proxy.logs

    @property
    def variables(self) -> VariableList:
        """
        Access the variables
        """
        return self._proxy.variables

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.EnvironmentInstance {}>".format(context)


class EnvironmentContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the EnvironmentContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Environment resource from.
        :param sid: The SID of the Environment resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Environments/{sid}".format(
            **self._solution
        )

        self._deployments: Optional[DeploymentList] = None
        self._logs: Optional[LogList] = None
        self._variables: Optional[VariableList] = None

    def delete(self) -> bool:
        """
        Deletes the EnvironmentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the EnvironmentInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> EnvironmentInstance:
        """
        Fetch the EnvironmentInstance


        :returns: The fetched EnvironmentInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EnvironmentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> EnvironmentInstance:
        """
        Asynchronous coroutine to fetch the EnvironmentInstance


        :returns: The fetched EnvironmentInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EnvironmentInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def deployments(self) -> DeploymentList:
        """
        Access the deployments
        """
        if self._deployments is None:
            self._deployments = DeploymentList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._deployments

    @property
    def logs(self) -> LogList:
        """
        Access the logs
        """
        if self._logs is None:
            self._logs = LogList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._logs

    @property
    def variables(self) -> VariableList:
        """
        Access the variables
        """
        if self._variables is None:
            self._variables = VariableList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._variables

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.EnvironmentContext {}>".format(context)


class EnvironmentPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> EnvironmentInstance:
        """
        Build an instance of EnvironmentInstance

        :param payload: Payload response from the API
        """
        return EnvironmentInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.EnvironmentPage>"


class EnvironmentList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the EnvironmentList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Environment resources from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Environments".format(**self._solution)

    def create(
        self, unique_name: str, domain_suffix: Union[str, object] = values.unset
    ) -> EnvironmentInstance:
        """
        Create the EnvironmentInstance

        :param unique_name: A user-defined string that uniquely identifies the Environment resource. It can be a maximum of 100 characters.
        :param domain_suffix: A URL-friendly name that represents the environment and forms part of the domain name. It can be a maximum of 16 characters.

        :returns: The created EnvironmentInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "DomainSuffix": domain_suffix,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EnvironmentInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self, unique_name: str, domain_suffix: Union[str, object] = values.unset
    ) -> EnvironmentInstance:
        """
        Asynchronously create the EnvironmentInstance

        :param unique_name: A user-defined string that uniquely identifies the Environment resource. It can be a maximum of 100 characters.
        :param domain_suffix: A URL-friendly name that represents the environment and forms part of the domain name. It can be a maximum of 16 characters.

        :returns: The created EnvironmentInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "DomainSuffix": domain_suffix,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return EnvironmentInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[EnvironmentInstance]:
        """
        Streams EnvironmentInstance records from the API as a generator stream.
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
    ) -> List[EnvironmentInstance]:
        """
        Asynchronously streams EnvironmentInstance records from the API as a generator stream.
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
    ) -> List[EnvironmentInstance]:
        """
        Lists EnvironmentInstance records from the API as a list.
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
    ) -> List[EnvironmentInstance]:
        """
        Asynchronously lists EnvironmentInstance records from the API as a list.
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
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> EnvironmentPage:
        """
        Retrieve a single page of EnvironmentInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EnvironmentInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EnvironmentPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> EnvironmentPage:
        """
        Asynchronously retrieve a single page of EnvironmentInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EnvironmentInstance
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
        return EnvironmentPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> EnvironmentPage:
        """
        Retrieve a specific page of EnvironmentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EnvironmentInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EnvironmentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> EnvironmentPage:
        """
        Asynchronously retrieve a specific page of EnvironmentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EnvironmentInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EnvironmentPage(self._version, response, self._solution)

    def get(self, sid: str) -> EnvironmentContext:
        """
        Constructs a EnvironmentContext

        :param sid: The SID of the Environment resource to fetch.
        """
        return EnvironmentContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> EnvironmentContext:
        """
        Constructs a EnvironmentContext

        :param sid: The SID of the Environment resource to fetch.
        """
        return EnvironmentContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.EnvironmentList>"
