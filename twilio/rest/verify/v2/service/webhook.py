r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class WebhookInstance(InstanceResource):
    class Methods(object):
        GET = "GET"
        POST = "POST"

    class Status(object):
        ENABLED = "enabled"
        DISABLED = "disabled"

    class Version(object):
        V1 = "v1"
        V2 = "v2"

    """
    :ivar sid: The unique string that we created to identify the Webhook resource.
    :ivar service_sid: The unique SID identifier of the Service.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
    :ivar friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
    :ivar event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
    :ivar status: 
    :ivar version: 
    :ivar webhook_url: The URL associated with this Webhook.
    :ivar webhook_method: 
    :ivar date_created: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Webhook resource.
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
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.event_types: Optional[List[str]] = payload.get("event_types")
        self.status: Optional["WebhookInstance.Status"] = payload.get("status")
        self.version: Optional["WebhookInstance.Version"] = payload.get("version")
        self.webhook_url: Optional[str] = payload.get("webhook_url")
        self.webhook_method: Optional["WebhookInstance.Methods"] = payload.get(
            "webhook_method"
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[WebhookContext] = None

    @property
    def _proxy(self) -> "WebhookContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WebhookContext for this WebhookInstance
        """
        if self._context is None:
            self._context = WebhookContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the WebhookInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the WebhookInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "WebhookInstance":
        """
        Fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "WebhookInstance":
        """
        Asynchronous coroutine to fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        event_types: Union[List[str], object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        status: Union["WebhookInstance.Status", object] = values.unset,
        version: Union["WebhookInstance.Version", object] = values.unset,
    ) -> "WebhookInstance":
        """
        Update the WebhookInstance

        :param friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param webhook_url: The URL associated with this Webhook.
        :param status:
        :param version:

        :returns: The updated WebhookInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            event_types=event_types,
            webhook_url=webhook_url,
            status=status,
            version=version,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        event_types: Union[List[str], object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        status: Union["WebhookInstance.Status", object] = values.unset,
        version: Union["WebhookInstance.Version", object] = values.unset,
    ) -> "WebhookInstance":
        """
        Asynchronous coroutine to update the WebhookInstance

        :param friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param webhook_url: The URL associated with this Webhook.
        :param status:
        :param version:

        :returns: The updated WebhookInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            event_types=event_types,
            webhook_url=webhook_url,
            status=status,
            version=version,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.WebhookInstance {}>".format(context)


class WebhookContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the WebhookContext

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Webhooks/{sid}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the WebhookInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the WebhookInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> WebhookInstance:
        """
        Fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> WebhookInstance:
        """
        Asynchronous coroutine to fetch the WebhookInstance


        :returns: The fetched WebhookInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        event_types: Union[List[str], object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        status: Union["WebhookInstance.Status", object] = values.unset,
        version: Union["WebhookInstance.Version", object] = values.unset,
    ) -> WebhookInstance:
        """
        Update the WebhookInstance

        :param friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param webhook_url: The URL associated with this Webhook.
        :param status:
        :param version:

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EventTypes": serialize.map(event_types, lambda e: e),
                "WebhookUrl": webhook_url,
                "Status": status,
                "Version": version,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        event_types: Union[List[str], object] = values.unset,
        webhook_url: Union[str, object] = values.unset,
        status: Union["WebhookInstance.Status", object] = values.unset,
        version: Union["WebhookInstance.Version", object] = values.unset,
    ) -> WebhookInstance:
        """
        Asynchronous coroutine to update the WebhookInstance

        :param friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param webhook_url: The URL associated with this Webhook.
        :param status:
        :param version:

        :returns: The updated WebhookInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EventTypes": serialize.map(event_types, lambda e: e),
                "WebhookUrl": webhook_url,
                "Status": status,
                "Version": version,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.WebhookContext {}>".format(context)


class WebhookPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> WebhookInstance:
        """
        Build an instance of WebhookInstance

        :param payload: Payload response from the API
        """
        return WebhookInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.WebhookPage>"


class WebhookList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the WebhookList

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Webhooks".format(**self._solution)

    def create(
        self,
        friendly_name: str,
        event_types: List[str],
        webhook_url: str,
        status: Union["WebhookInstance.Status", object] = values.unset,
        version: Union["WebhookInstance.Version", object] = values.unset,
    ) -> WebhookInstance:
        """
        Create the WebhookInstance

        :param friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param webhook_url: The URL associated with this Webhook.
        :param status:
        :param version:

        :returns: The created WebhookInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EventTypes": serialize.map(event_types, lambda e: e),
                "WebhookUrl": webhook_url,
                "Status": status,
                "Version": version,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        friendly_name: str,
        event_types: List[str],
        webhook_url: str,
        status: Union["WebhookInstance.Status", object] = values.unset,
        version: Union["WebhookInstance.Version", object] = values.unset,
    ) -> WebhookInstance:
        """
        Asynchronously create the WebhookInstance

        :param friendly_name: The string that you assigned to describe the webhook. **This value should not contain PII.**
        :param event_types: The array of events that this Webhook is subscribed to. Possible event types: `*, factor.deleted, factor.created, factor.verified, challenge.approved, challenge.denied`
        :param webhook_url: The URL associated with this Webhook.
        :param status:
        :param version:

        :returns: The created WebhookInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EventTypes": serialize.map(event_types, lambda e: e),
                "WebhookUrl": webhook_url,
                "Status": status,
                "Version": version,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[WebhookInstance]:
        """
        Streams WebhookInstance records from the API as a generator stream.
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
    ) -> List[WebhookInstance]:
        """
        Asynchronously streams WebhookInstance records from the API as a generator stream.
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
    ) -> List[WebhookInstance]:
        """
        Lists WebhookInstance records from the API as a list.
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
    ) -> List[WebhookInstance]:
        """
        Asynchronously lists WebhookInstance records from the API as a list.
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
    ) -> WebhookPage:
        """
        Retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of WebhookInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return WebhookPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> WebhookPage:
        """
        Asynchronously retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of WebhookInstance
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
        return WebhookPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> WebhookPage:
        """
        Retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return WebhookPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> WebhookPage:
        """
        Asynchronously retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return WebhookPage(self._version, response, self._solution)

    def get(self, sid: str) -> WebhookContext:
        """
        Constructs a WebhookContext

        :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
        """
        return WebhookContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> WebhookContext:
        """
        Constructs a WebhookContext

        :param sid: The Twilio-provided string that uniquely identifies the Webhook resource to update.
        """
        return WebhookContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.WebhookList>"
