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
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.proxy.v1.service.phone_number import PhoneNumberList
from twilio.rest.proxy.v1.service.session import SessionList
from twilio.rest.proxy.v1.service.short_code import ShortCodeList


class ServiceInstance(InstanceResource):
    class GeoMatchLevel(object):
        AREA_CODE = "area-code"
        OVERLAY = "overlay"
        RADIUS = "radius"
        COUNTRY = "country"

    class NumberSelectionBehavior(object):
        AVOID_STICKY = "avoid-sticky"
        PREFER_STICKY = "prefer-sticky"

    """
    :ivar sid: The unique string that we created to identify the Service resource.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. Supports UTF-8 characters. **This value should not have PII.**
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
    :ivar chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
    :ivar callback_url: The URL we call when the interaction status changes.
    :ivar default_ttl: The default `ttl` value for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
    :ivar number_selection_behavior: 
    :ivar geo_match_level: 
    :ivar intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
    :ivar out_of_session_callback_url: The URL we call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
    :ivar date_created: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created.
    :ivar date_updated: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated.
    :ivar url: The absolute URL of the Service resource.
    :ivar links: The URLs of resources related to the Service.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.chat_instance_sid: Optional[str] = payload.get("chat_instance_sid")
        self.callback_url: Optional[str] = payload.get("callback_url")
        self.default_ttl: Optional[int] = deserialize.integer(
            payload.get("default_ttl")
        )
        self.number_selection_behavior: Optional[
            "ServiceInstance.NumberSelectionBehavior"
        ] = payload.get("number_selection_behavior")
        self.geo_match_level: Optional["ServiceInstance.GeoMatchLevel"] = payload.get(
            "geo_match_level"
        )
        self.intercept_callback_url: Optional[str] = payload.get(
            "intercept_callback_url"
        )
        self.out_of_session_callback_url: Optional[str] = payload.get(
            "out_of_session_callback_url"
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
            "sid": sid or self.sid,
        }
        self._context: Optional[ServiceContext] = None

    @property
    def _proxy(self) -> "ServiceContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        """
        if self._context is None:
            self._context = ServiceContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ServiceInstance":
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ServiceInstance":
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        unique_name: Union[str, object] = values.unset,
        default_ttl: Union[int, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        geo_match_level: Union["ServiceInstance.GeoMatchLevel", object] = values.unset,
        number_selection_behavior: Union[
            "ServiceInstance.NumberSelectionBehavior", object
        ] = values.unset,
        intercept_callback_url: Union[str, object] = values.unset,
        out_of_session_callback_url: Union[str, object] = values.unset,
        chat_instance_sid: Union[str, object] = values.unset,
    ) -> "ServiceInstance":
        """
        Update the ServiceInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :param callback_url: The URL we should call when the interaction status changes.
        :param geo_match_level:
        :param number_selection_behavior:
        :param intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :param out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :param chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.

        :returns: The updated ServiceInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            default_ttl=default_ttl,
            callback_url=callback_url,
            geo_match_level=geo_match_level,
            number_selection_behavior=number_selection_behavior,
            intercept_callback_url=intercept_callback_url,
            out_of_session_callback_url=out_of_session_callback_url,
            chat_instance_sid=chat_instance_sid,
        )

    async def update_async(
        self,
        unique_name: Union[str, object] = values.unset,
        default_ttl: Union[int, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        geo_match_level: Union["ServiceInstance.GeoMatchLevel", object] = values.unset,
        number_selection_behavior: Union[
            "ServiceInstance.NumberSelectionBehavior", object
        ] = values.unset,
        intercept_callback_url: Union[str, object] = values.unset,
        out_of_session_callback_url: Union[str, object] = values.unset,
        chat_instance_sid: Union[str, object] = values.unset,
    ) -> "ServiceInstance":
        """
        Asynchronous coroutine to update the ServiceInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :param callback_url: The URL we should call when the interaction status changes.
        :param geo_match_level:
        :param number_selection_behavior:
        :param intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :param out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :param chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.

        :returns: The updated ServiceInstance
        """
        return await self._proxy.update_async(
            unique_name=unique_name,
            default_ttl=default_ttl,
            callback_url=callback_url,
            geo_match_level=geo_match_level,
            number_selection_behavior=number_selection_behavior,
            intercept_callback_url=intercept_callback_url,
            out_of_session_callback_url=out_of_session_callback_url,
            chat_instance_sid=chat_instance_sid,
        )

    @property
    def phone_numbers(self) -> PhoneNumberList:
        """
        Access the phone_numbers
        """
        return self._proxy.phone_numbers

    @property
    def sessions(self) -> SessionList:
        """
        Access the sessions
        """
        return self._proxy.sessions

    @property
    def short_codes(self) -> ShortCodeList:
        """
        Access the short_codes
        """
        return self._proxy.short_codes

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.ServiceInstance {}>".format(context)


class ServiceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Services/{sid}".format(**self._solution)

        self._phone_numbers: Optional[PhoneNumberList] = None
        self._sessions: Optional[SessionList] = None
        self._short_codes: Optional[ShortCodeList] = None

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ServiceInstance:
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ServiceInstance:
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        unique_name: Union[str, object] = values.unset,
        default_ttl: Union[int, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        geo_match_level: Union["ServiceInstance.GeoMatchLevel", object] = values.unset,
        number_selection_behavior: Union[
            "ServiceInstance.NumberSelectionBehavior", object
        ] = values.unset,
        intercept_callback_url: Union[str, object] = values.unset,
        out_of_session_callback_url: Union[str, object] = values.unset,
        chat_instance_sid: Union[str, object] = values.unset,
    ) -> ServiceInstance:
        """
        Update the ServiceInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :param callback_url: The URL we should call when the interaction status changes.
        :param geo_match_level:
        :param number_selection_behavior:
        :param intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :param out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :param chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "DefaultTtl": default_ttl,
                "CallbackUrl": callback_url,
                "GeoMatchLevel": geo_match_level,
                "NumberSelectionBehavior": number_selection_behavior,
                "InterceptCallbackUrl": intercept_callback_url,
                "OutOfSessionCallbackUrl": out_of_session_callback_url,
                "ChatInstanceSid": chat_instance_sid,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        unique_name: Union[str, object] = values.unset,
        default_ttl: Union[int, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        geo_match_level: Union["ServiceInstance.GeoMatchLevel", object] = values.unset,
        number_selection_behavior: Union[
            "ServiceInstance.NumberSelectionBehavior", object
        ] = values.unset,
        intercept_callback_url: Union[str, object] = values.unset,
        out_of_session_callback_url: Union[str, object] = values.unset,
        chat_instance_sid: Union[str, object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronous coroutine to update the ServiceInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :param callback_url: The URL we should call when the interaction status changes.
        :param geo_match_level:
        :param number_selection_behavior:
        :param intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :param out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :param chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "DefaultTtl": default_ttl,
                "CallbackUrl": callback_url,
                "GeoMatchLevel": geo_match_level,
                "NumberSelectionBehavior": number_selection_behavior,
                "InterceptCallbackUrl": intercept_callback_url,
                "OutOfSessionCallbackUrl": out_of_session_callback_url,
                "ChatInstanceSid": chat_instance_sid,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def phone_numbers(self) -> PhoneNumberList:
        """
        Access the phone_numbers
        """
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(
                self._version,
                self._solution["sid"],
            )
        return self._phone_numbers

    @property
    def sessions(self) -> SessionList:
        """
        Access the sessions
        """
        if self._sessions is None:
            self._sessions = SessionList(
                self._version,
                self._solution["sid"],
            )
        return self._sessions

    @property
    def short_codes(self) -> ShortCodeList:
        """
        Access the short_codes
        """
        if self._short_codes is None:
            self._short_codes = ShortCodeList(
                self._version,
                self._solution["sid"],
            )
        return self._short_codes

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Proxy.V1.ServiceContext {}>".format(context)


class ServicePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ServiceInstance:
        """
        Build an instance of ServiceInstance

        :param payload: Payload response from the API
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.ServicePage>"


class ServiceList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Services"

    def create(
        self,
        unique_name: str,
        default_ttl: Union[int, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        geo_match_level: Union["ServiceInstance.GeoMatchLevel", object] = values.unset,
        number_selection_behavior: Union[
            "ServiceInstance.NumberSelectionBehavior", object
        ] = values.unset,
        intercept_callback_url: Union[str, object] = values.unset,
        out_of_session_callback_url: Union[str, object] = values.unset,
        chat_instance_sid: Union[str, object] = values.unset,
    ) -> ServiceInstance:
        """
        Create the ServiceInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :param callback_url: The URL we should call when the interaction status changes.
        :param geo_match_level:
        :param number_selection_behavior:
        :param intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :param out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :param chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.

        :returns: The created ServiceInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "DefaultTtl": default_ttl,
                "CallbackUrl": callback_url,
                "GeoMatchLevel": geo_match_level,
                "NumberSelectionBehavior": number_selection_behavior,
                "InterceptCallbackUrl": intercept_callback_url,
                "OutOfSessionCallbackUrl": out_of_session_callback_url,
                "ChatInstanceSid": chat_instance_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    async def create_async(
        self,
        unique_name: str,
        default_ttl: Union[int, object] = values.unset,
        callback_url: Union[str, object] = values.unset,
        geo_match_level: Union["ServiceInstance.GeoMatchLevel", object] = values.unset,
        number_selection_behavior: Union[
            "ServiceInstance.NumberSelectionBehavior", object
        ] = values.unset,
        intercept_callback_url: Union[str, object] = values.unset,
        out_of_session_callback_url: Union[str, object] = values.unset,
        chat_instance_sid: Union[str, object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronously create the ServiceInstance

        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
        :param default_ttl: The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
        :param callback_url: The URL we should call when the interaction status changes.
        :param geo_match_level:
        :param number_selection_behavior:
        :param intercept_callback_url: The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
        :param out_of_session_callback_url: The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
        :param chat_instance_sid: The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.

        :returns: The created ServiceInstance
        """
        data = values.of(
            {
                "UniqueName": unique_name,
                "DefaultTtl": default_ttl,
                "CallbackUrl": callback_url,
                "GeoMatchLevel": geo_match_level,
                "NumberSelectionBehavior": number_selection_behavior,
                "InterceptCallbackUrl": intercept_callback_url,
                "OutOfSessionCallbackUrl": out_of_session_callback_url,
                "ChatInstanceSid": chat_instance_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[ServiceInstance]:
        """
        Streams ServiceInstance records from the API as a generator stream.
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
    ) -> List[ServiceInstance]:
        """
        Asynchronously streams ServiceInstance records from the API as a generator stream.
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
    ) -> List[ServiceInstance]:
        """
        Lists ServiceInstance records from the API as a list.
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
    ) -> List[ServiceInstance]:
        """
        Asynchronously lists ServiceInstance records from the API as a list.
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
    ) -> ServicePage:
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ServicePage(self._version, response)

    async def page_async(
        self,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> ServicePage:
        """
        Asynchronously retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
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
        return ServicePage(self._version, response)

    def get_page(self, target_url: str) -> ServicePage:
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ServicePage(self._version, response)

    async def get_page_async(self, target_url: str) -> ServicePage:
        """
        Asynchronously retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ServicePage(self._version, response)

    def get(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: The Twilio-provided string that uniquely identifies the Service resource to update.
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Proxy.V1.ServiceList>"
