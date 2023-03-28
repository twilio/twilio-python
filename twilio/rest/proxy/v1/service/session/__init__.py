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


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.proxy.v1.service.session.interaction import InteractionList
from twilio.rest.proxy.v1.service.session.participant import ParticipantList


class SessionInstance(InstanceResource):
    class Mode(object):
        MESSAGE_ONLY = "message-only"
        VOICE_ONLY = "voice-only"
        VOICE_AND_MESSAGE = "voice-and-message"

    class Status(object):
        OPEN = "open"
        IN_PROGRESS = "in-progress"
        CLOSED = "closed"
        FAILED = "failed"
        UNKNOWN = "unknown"

    """
    :ivar sid: The unique string that we created to identify the Session resource.
    :ivar service_sid: The SID of the [Service](https://www.twilio.com/docs/proxy/api/service) the session is associated with.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Session resource.
    :ivar date_started: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session started.
    :ivar date_ended: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session ended.
    :ivar date_last_interaction: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session last had an interaction.
    :ivar date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. Supports UTF-8 characters. **This value should not have PII.**
    :ivar status: 
    :ivar closed_reason: The reason the Session ended.
    :ivar ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
    :ivar mode: 
    :ivar date_created: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created.
    :ivar date_updated: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated.
    :ivar url: The absolute URL of the Session resource.
    :ivar links: The URLs of resources related to the Session.
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
        self.date_started: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_started")
        )
        self.date_ended: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_ended")
        )
        self.date_last_interaction: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_last_interaction")
        )
        self.date_expiry: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_expiry")
        )
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.status: Optional["SessionInstance.Status"] = payload.get("status")
        self.closed_reason: Optional[str] = payload.get("closed_reason")
        self.ttl: Optional[int] = deserialize.integer(payload.get("ttl"))
        self.mode: Optional["SessionInstance.Mode"] = payload.get("mode")
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
        self._context: Optional[SessionContext] = None

    @property
    def _proxy(self) -> "SessionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SessionContext for this SessionInstance
        """
        if self._context is None:
            self._context = SessionContext(
                self._version,
                service_sid=self._solution["service_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the SessionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SessionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "SessionInstance":
        """
        Fetch the SessionInstance


        :returns: The fetched SessionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SessionInstance":
        """
        Asynchronous coroutine to fetch the SessionInstance


        :returns: The fetched SessionInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        date_expiry: Union[datetime, object] = values.unset,
        ttl: Union[int, object] = values.unset,
        status: Union["SessionInstance.Status", object] = values.unset,
    ) -> "SessionInstance":
        """
        Update the SessionInstance

        :param date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
        :param ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
        :param status:

        :returns: The updated SessionInstance
        """
        return self._proxy.update(
            date_expiry=date_expiry,
            ttl=ttl,
            status=status,
        )

    async def update_async(
        self,
        date_expiry: Union[datetime, object] = values.unset,
        ttl: Union[int, object] = values.unset,
        status: Union["SessionInstance.Status", object] = values.unset,
    ) -> "SessionInstance":
        """
        Asynchronous coroutine to update the SessionInstance

        :param date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
        :param ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
        :param status:

        :returns: The updated SessionInstance
        """
        return await self._proxy.update_async(
            date_expiry=date_expiry,
            ttl=ttl,
            status=status,
        )

    @property
    def interactions(self) -> InteractionList:
        """
        Access the interactions
        """
        return self._proxy.interactions

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        return self._proxy.participants

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.SessionInstance {}>".format(context)


class SessionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the SessionContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the Session resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Sessions/{sid}".format(**self._solution)

        self._interactions: Optional[InteractionList] = None
        self._participants: Optional[ParticipantList] = None

    def delete(self) -> bool:
        """
        Deletes the SessionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the SessionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> SessionInstance:
        """
        Fetch the SessionInstance


        :returns: The fetched SessionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return SessionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> SessionInstance:
        """
        Asynchronous coroutine to fetch the SessionInstance


        :returns: The fetched SessionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return SessionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        date_expiry: Union[datetime, object] = values.unset,
        ttl: Union[int, object] = values.unset,
        status: Union["SessionInstance.Status", object] = values.unset,
    ) -> SessionInstance:
        """
        Update the SessionInstance

        :param date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
        :param ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
        :param status:

        :returns: The updated SessionInstance
        """
        data = values.of(
            {
                "DateExpiry": serialize.iso8601_datetime(date_expiry),
                "Ttl": ttl,
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SessionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        date_expiry: Union[datetime, object] = values.unset,
        ttl: Union[int, object] = values.unset,
        status: Union["SessionInstance.Status", object] = values.unset,
    ) -> SessionInstance:
        """
        Asynchronous coroutine to update the SessionInstance

        :param date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
        :param ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
        :param status:

        :returns: The updated SessionInstance
        """
        data = values.of(
            {
                "DateExpiry": serialize.iso8601_datetime(date_expiry),
                "Ttl": ttl,
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SessionInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            sid=self._solution["sid"],
        )

    @property
    def interactions(self) -> InteractionList:
        """
        Access the interactions
        """
        if self._interactions is None:
            self._interactions = InteractionList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._interactions

    @property
    def participants(self) -> ParticipantList:
        """
        Access the participants
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                self._solution["service_sid"],
                self._solution["sid"],
            )
        return self._participants

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.SessionContext {}>".format(context)


class SessionPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> SessionInstance:
        """
        Build an instance of SessionInstance

        :param payload: Payload response from the API
        """
        return SessionInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.SessionPage>"


class SessionList(ListResource):
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the SessionList

        :param version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
        }
        self._uri = "/Services/{service_sid}/Sessions".format(**self._solution)

    def create(
        self,
        unique_name: Union[str, object] = values.unset,
        date_expiry: Union[datetime, object] = values.unset,
        ttl: Union[int, object] = values.unset,
        mode: Union["SessionInstance.Mode", object] = values.unset,
        status: Union["SessionInstance.Status", object] = values.unset,
        participants: Union[List[object], object] = values.unset,
    ) -> SessionInstance:
        """
        Create the SessionInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
        :param ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
        :param mode:
        :param status:
        :param participants: The Participant objects to include in the new session.

        :returns: The created SessionInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "DateExpiry": serialize.iso8601_datetime(date_expiry),
                "Ttl": ttl,
                "Mode": mode,
                "Status": status,
                "Participants": serialize.map(
                    participants, lambda e: serialize.object(e)
                ),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SessionInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    async def create_async(
        self,
        unique_name: Union[str, object] = values.unset,
        date_expiry: Union[datetime, object] = values.unset,
        ttl: Union[int, object] = values.unset,
        mode: Union["SessionInstance.Mode", object] = values.unset,
        status: Union["SessionInstance.Status", object] = values.unset,
        participants: Union[List[object], object] = values.unset,
    ) -> SessionInstance:
        """
        Asynchronously create the SessionInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param date_expiry: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
        :param ttl: The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
        :param mode:
        :param status:
        :param participants: The Participant objects to include in the new session.

        :returns: The created SessionInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "DateExpiry": serialize.iso8601_datetime(date_expiry),
                "Ttl": ttl,
                "Mode": mode,
                "Status": status,
                "Participants": serialize.map(
                    participants, lambda e: serialize.object(e)
                ),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return SessionInstance(
            self._version, payload, service_sid=self._solution["service_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[SessionInstance]:
        """
        Streams SessionInstance records from the API as a generator stream.
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
    ) -> List[SessionInstance]:
        """
        Asynchronously streams SessionInstance records from the API as a generator stream.
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
    ) -> List[SessionInstance]:
        """
        Lists SessionInstance records from the API as a list.
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
    ) -> List[SessionInstance]:
        """
        Asynchronously lists SessionInstance records from the API as a list.
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
    ) -> SessionPage:
        """
        Retrieve a single page of SessionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SessionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return SessionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> SessionPage:
        """
        Asynchronously retrieve a single page of SessionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SessionInstance
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
        return SessionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> SessionPage:
        """
        Retrieve a specific page of SessionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SessionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return SessionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> SessionPage:
        """
        Asynchronously retrieve a specific page of SessionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SessionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return SessionPage(self._version, response, self._solution)

    def get(self, sid: str) -> SessionContext:
        """
        Constructs a SessionContext

        :param sid: The Twilio-provided string that uniquely identifies the Session resource to update.
        """
        return SessionContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __call__(self, sid: str) -> SessionContext:
        """
        Constructs a SessionContext

        :param sid: The Twilio-provided string that uniquely identifies the Session resource to update.
        """
        return SessionContext(
            self._version, service_sid=self._solution["service_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.SessionList>"
