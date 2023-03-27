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
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.proxy.v1.service.session.participant.message_interaction import (
    MessageInteractionList,
)


class ParticipantInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Participant resource.
    :ivar session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource.
    :ivar service_sid: The SID of the resource's parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Participant resource.
    :ivar friendly_name: The string that you assigned to describe the participant. This value must be 255 characters or fewer. Supports UTF-8 characters. **This value should not have PII.**
    :ivar identifier: The phone number or channel identifier of the Participant. This value must be 191 characters or fewer. Supports UTF-8 characters.
    :ivar proxy_identifier: The phone number or short code (masked number) of the participant's partner. The participant will call or message the partner participant at this number.
    :ivar proxy_identifier_sid: The SID of the Proxy Identifier assigned to the Participant.
    :ivar date_deleted: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Participant was removed from the session.
    :ivar date_created: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created.
    :ivar date_updated: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated.
    :ivar url: The absolute URL of the Participant resource.
    :ivar links: The URLs to resources related the participant.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        session_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.session_sid: Optional[str] = payload.get("session_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.identifier: Optional[str] = payload.get("identifier")
        self.proxy_identifier: Optional[str] = payload.get("proxy_identifier")
        self.proxy_identifier_sid: Optional[str] = payload.get("proxy_identifier_sid")
        self.date_deleted: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_deleted")
        )
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
            "session_sid": session_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[ParticipantContext] = None

    @property
    def _proxy(self) -> "ParticipantContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ParticipantContext for this ParticipantInstance
        """
        if self._context is None:
            self._context = ParticipantContext(
                self._version,
                service_sid=self._solution["service_sid"],
                session_sid=self._solution["session_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ParticipantInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ParticipantInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ParticipantInstance":
        """
        Fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ParticipantInstance":
        """
        Asynchronous coroutine to fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """
        return await self._proxy.fetch_async()

    @property
    def message_interactions(self) -> MessageInteractionList:
        """
        Access the message_interactions
        """
        return self._proxy.message_interactions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.ParticipantInstance {}>".format(context)


class ParticipantContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, session_sid: str, sid: str):
        """
        Initialize the ParticipantContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
        :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "session_sid": session_sid,
            "sid": sid,
        }
        self._uri = (
            "/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}".format(
                **self._solution
            )
        )

        self._message_interactions: Optional[MessageInteractionList] = None

    def delete(self) -> bool:
        """
        Deletes the ParticipantInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ParticipantInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ParticipantInstance:
        """
        Fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ParticipantInstance:
        """
        Asynchronous coroutine to fetch the ParticipantInstance


        :returns: The fetched ParticipantInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
            sid=self._solution["sid"],
        )

    @property
    def message_interactions(self) -> MessageInteractionList:
        """
        Access the message_interactions
        """
        if self._message_interactions is None:
            self._message_interactions = MessageInteractionList(
                self._version,
                self._solution["service_sid"],
                self._solution["session_sid"],
                self._solution["sid"],
            )
        return self._message_interactions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.ParticipantContext {}>".format(context)


class ParticipantPage(Page):
    def get_instance(self, payload) -> ParticipantInstance:
        """
        Build an instance of ParticipantInstance

        :param dict payload: Payload response from the API
        """
        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.ParticipantPage>"


class ParticipantList(ListResource):
    def __init__(self, version: Version, service_sid: str, session_sid: str):
        """
        Initialize the ParticipantList

        :param version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resources to read.
        :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "session_sid": session_sid,
        }
        self._uri = (
            "/Services/{service_sid}/Sessions/{session_sid}/Participants".format(
                **self._solution
            )
        )

    def create(
        self,
        identifier,
        friendly_name=values.unset,
        proxy_identifier=values.unset,
        proxy_identifier_sid=values.unset,
    ) -> ParticipantInstance:
        """
        Create the ParticipantInstance

        :param str identifier: The phone number of the Participant.
        :param str friendly_name: The string that you assigned to describe the participant. This value must be 255 characters or fewer. **This value should not have PII.**
        :param str proxy_identifier: The proxy phone number to use for the Participant. If not specified, Proxy will select a number from the pool.
        :param str proxy_identifier_sid: The SID of the Proxy Identifier to assign to the Participant.

        :returns: The created ParticipantInstance
        """
        data = values.of(
            {
                "Identifier": identifier,
                "FriendlyName": friendly_name,
                "ProxyIdentifier": proxy_identifier,
                "ProxyIdentifierSid": proxy_identifier_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
        )

    async def create_async(
        self,
        identifier,
        friendly_name=values.unset,
        proxy_identifier=values.unset,
        proxy_identifier_sid=values.unset,
    ) -> ParticipantInstance:
        """
        Asynchronously create the ParticipantInstance

        :param str identifier: The phone number of the Participant.
        :param str friendly_name: The string that you assigned to describe the participant. This value must be 255 characters or fewer. **This value should not have PII.**
        :param str proxy_identifier: The proxy phone number to use for the Participant. If not specified, Proxy will select a number from the pool.
        :param str proxy_identifier_sid: The SID of the Proxy Identifier to assign to the Participant.

        :returns: The created ParticipantInstance
        """
        data = values.of(
            {
                "Identifier": identifier,
                "FriendlyName": friendly_name,
                "ProxyIdentifier": proxy_identifier,
                "ProxyIdentifierSid": proxy_identifier_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
        )

    def stream(self, limit=None, page_size=None) -> List[ParticipantInstance]:
        """
        Streams ParticipantInstance records from the API as a generator stream.
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
    ) -> List[ParticipantInstance]:
        """
        Asynchronously streams ParticipantInstance records from the API as a generator stream.
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

    def list(self, limit=None, page_size=None) -> List[ParticipantInstance]:
        """
        Lists ParticipantInstance records from the API as a list.
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

    async def list_async(self, limit=None, page_size=None) -> List[ParticipantInstance]:
        """
        Asynchronously lists ParticipantInstance records from the API as a list.
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
    ) -> ParticipantPage:
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ParticipantPage(self._version, response, self._solution)

    async def page_async(
        self, page_token=values.unset, page_number=values.unset, page_size=values.unset
    ) -> ParticipantPage:
        """
        Asynchronously retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
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
        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url) -> ParticipantPage:
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ParticipantPage(self._version, response, self._solution)

    async def get_page_async(self, target_url) -> ParticipantPage:
        """
        Asynchronously retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ParticipantPage(self._version, response, self._solution)

    def get(self, sid) -> ParticipantContext:
        """
        Constructs a ParticipantContext

        :param sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
        """
        return ParticipantContext(
            self._version,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
            sid=sid,
        )

    def __call__(self, sid) -> ParticipantContext:
        """
        Constructs a ParticipantContext

        :param sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
        """
        return ParticipantContext(
            self._version,
            service_sid=self._solution["service_sid"],
            session_sid=self._solution["session_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.ParticipantList>"
