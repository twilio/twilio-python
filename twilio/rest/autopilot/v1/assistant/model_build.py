r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
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


class ModelBuildInstance(InstanceResource):
    class Status(object):
        ENQUEUED = "enqueued"
        BUILDING = "building"
        COMPLETED = "completed"
        FAILED = "failed"
        CANCELED = "canceled"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ModelBuild resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource.
    :ivar sid: The unique string that we created to identify the ModelBuild resource.
    :ivar status: 
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource.
    :ivar url: The absolute URL of the ModelBuild resource.
    :ivar build_duration: The time in seconds it took to build the model.
    :ivar error_code: If the `status` for the model build is `failed`, this value is a code to more information about the failure. This value will be null for all other statuses. See [error code dictionary](https://www.twilio.com/docs/api/errors) for a description of the error.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        assistant_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.assistant_sid: Optional[str] = payload.get("assistant_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.status: Optional["ModelBuildInstance.Status"] = payload.get("status")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.url: Optional[str] = payload.get("url")
        self.build_duration: Optional[int] = deserialize.integer(
            payload.get("build_duration")
        )
        self.error_code: Optional[int] = deserialize.integer(payload.get("error_code"))

        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ModelBuildContext] = None

    @property
    def _proxy(self) -> "ModelBuildContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ModelBuildContext for this ModelBuildInstance
        """
        if self._context is None:
            self._context = ModelBuildContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ModelBuildInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ModelBuildInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ModelBuildInstance":
        """
        Fetch the ModelBuildInstance


        :returns: The fetched ModelBuildInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ModelBuildInstance":
        """
        Asynchronous coroutine to fetch the ModelBuildInstance


        :returns: The fetched ModelBuildInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, unique_name: Union[str, object] = values.unset
    ) -> "ModelBuildInstance":
        """
        Update the ModelBuildInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The updated ModelBuildInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
        )

    async def update_async(
        self, unique_name: Union[str, object] = values.unset
    ) -> "ModelBuildInstance":
        """
        Asynchronous coroutine to update the ModelBuildInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The updated ModelBuildInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.ModelBuildInstance {}>".format(context)


class ModelBuildContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, sid: str):
        """
        Initialize the ModelBuildContext

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid,
        }
        self._uri = "/Assistants/{assistant_sid}/ModelBuilds/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the ModelBuildInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ModelBuildInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ModelBuildInstance:
        """
        Fetch the ModelBuildInstance


        :returns: The fetched ModelBuildInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ModelBuildInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ModelBuildInstance:
        """
        Asynchronous coroutine to fetch the ModelBuildInstance


        :returns: The fetched ModelBuildInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ModelBuildInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self, unique_name: Union[str, object] = values.unset
    ) -> ModelBuildInstance:
        """
        Update the ModelBuildInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The updated ModelBuildInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ModelBuildInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self, unique_name: Union[str, object] = values.unset
    ) -> ModelBuildInstance:
        """
        Asynchronous coroutine to update the ModelBuildInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The updated ModelBuildInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ModelBuildInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.ModelBuildContext {}>".format(context)


class ModelBuildPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ModelBuildInstance:
        """
        Build an instance of ModelBuildInstance

        :param payload: Payload response from the API
        """
        return ModelBuildInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.ModelBuildPage>"


class ModelBuildList(ListResource):
    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the ModelBuildList

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/ModelBuilds".format(**self._solution)

    def create(
        self,
        status_callback: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> ModelBuildInstance:
        """
        Create the ModelBuildInstance

        :param status_callback: The URL we should call using a POST method to send status information to your application.
        :param unique_name: An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The created ModelBuildInstance
        """
        data = values.of(
            {
                "StatusCallback": status_callback,
                "UniqueName": unique_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ModelBuildInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    async def create_async(
        self,
        status_callback: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
    ) -> ModelBuildInstance:
        """
        Asynchronously create the ModelBuildInstance

        :param status_callback: The URL we should call using a POST method to send status information to your application.
        :param unique_name: An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The created ModelBuildInstance
        """
        data = values.of(
            {
                "StatusCallback": status_callback,
                "UniqueName": unique_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ModelBuildInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ModelBuildInstance]:
        """
        Streams ModelBuildInstance records from the API as a generator stream.
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
    ) -> List[ModelBuildInstance]:
        """
        Asynchronously streams ModelBuildInstance records from the API as a generator stream.
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
    ) -> List[ModelBuildInstance]:
        """
        Lists ModelBuildInstance records from the API as a list.
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
    ) -> List[ModelBuildInstance]:
        """
        Asynchronously lists ModelBuildInstance records from the API as a list.
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
    ) -> ModelBuildPage:
        """
        Retrieve a single page of ModelBuildInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ModelBuildInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ModelBuildPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ModelBuildPage:
        """
        Asynchronously retrieve a single page of ModelBuildInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ModelBuildInstance
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
        return ModelBuildPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> ModelBuildPage:
        """
        Retrieve a specific page of ModelBuildInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ModelBuildInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ModelBuildPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> ModelBuildPage:
        """
        Asynchronously retrieve a specific page of ModelBuildInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ModelBuildInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ModelBuildPage(self._version, response, self._solution)

    def get(self, sid: str) -> ModelBuildContext:
        """
        Constructs a ModelBuildContext

        :param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to update.
        """
        return ModelBuildContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __call__(self, sid: str) -> ModelBuildContext:
        """
        Constructs a ModelBuildContext

        :param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to update.
        """
        return ModelBuildContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.ModelBuildList>"
