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
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class FactorInstance(InstanceResource):
    class FactorStatuses(object):
        UNVERIFIED = "unverified"
        VERIFIED = "verified"

    class FactorTypes(object):
        PUSH = "push"
        TOTP = "totp"

    """
    :ivar sid: A 34 character string that uniquely identifies this Factor.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar service_sid: The unique SID identifier of the Service.
    :ivar entity_sid: The unique SID identifier of the Entity.
    :ivar identity: Customer unique identity for the Entity owner of the Factor. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
    :ivar date_created: The date that this Factor was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date that this Factor was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar friendly_name: A human readable description of this resource, up to 64 characters. For a push factor, this can be the device's name.
    :ivar status: 
    :ivar factor_type: 
    :ivar config: An object that contains configurations specific to a `factor_type`.
    :ivar metadata: Custom metadata associated with the factor. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\"os\": \"Android\"}`. Can be up to 1024 characters in length.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        service_sid: str,
        identity: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.entity_sid: Optional[str] = payload.get("entity_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.status: Optional["FactorInstance.FactorStatuses"] = payload.get("status")
        self.factor_type: Optional["FactorInstance.FactorTypes"] = payload.get(
            "factor_type"
        )
        self.config: Optional[Dict[str, object]] = payload.get("config")
        self.metadata: Optional[Dict[str, object]] = payload.get("metadata")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "identity": identity,
            "sid": sid or self.sid,
        }
        self._context: Optional[FactorContext] = None

    @property
    def _proxy(self) -> "FactorContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FactorContext for this FactorInstance
        """
        if self._context is None:
            self._context = FactorContext(
                self._version,
                service_sid=self._solution["service_sid"],
                identity=self._solution["identity"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the FactorInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FactorInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "FactorInstance":
        """
        Fetch the FactorInstance


        :returns: The fetched FactorInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FactorInstance":
        """
        Asynchronous coroutine to fetch the FactorInstance


        :returns: The fetched FactorInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        auth_payload: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        config_notification_token: Union[str, object] = values.unset,
        config_sdk_version: Union[str, object] = values.unset,
        config_time_step: Union[int, object] = values.unset,
        config_skew: Union[int, object] = values.unset,
        config_code_length: Union[int, object] = values.unset,
        config_alg: Union["FactorInstance.TotpAlgorithms", object] = values.unset,
        config_notification_platform: Union[str, object] = values.unset,
    ) -> "FactorInstance":
        """
        Update the FactorInstance

        :param auth_payload: The optional payload needed to verify the Factor for the first time. E.g. for a TOTP, the numeric code.
        :param friendly_name: The new friendly name of this Factor. It can be up to 64 characters.
        :param config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Required when `factor_type` is `push`. If specified, this value must be between 32 and 255 characters long.
        :param config_sdk_version: The Verify Push SDK version used to configure the factor
        :param config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive
        :param config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive
        :param config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive
        :param config_alg:
        :param config_notification_platform: The transport technology used to generate the Notification Token. Can be `apn`, `fcm` or `none`.  Required when `factor_type` is `push`.

        :returns: The updated FactorInstance
        """
        return self._proxy.update(
            auth_payload=auth_payload,
            friendly_name=friendly_name,
            config_notification_token=config_notification_token,
            config_sdk_version=config_sdk_version,
            config_time_step=config_time_step,
            config_skew=config_skew,
            config_code_length=config_code_length,
            config_alg=config_alg,
            config_notification_platform=config_notification_platform,
        )

    async def update_async(
        self,
        auth_payload: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        config_notification_token: Union[str, object] = values.unset,
        config_sdk_version: Union[str, object] = values.unset,
        config_time_step: Union[int, object] = values.unset,
        config_skew: Union[int, object] = values.unset,
        config_code_length: Union[int, object] = values.unset,
        config_alg: Union["FactorInstance.TotpAlgorithms", object] = values.unset,
        config_notification_platform: Union[str, object] = values.unset,
    ) -> "FactorInstance":
        """
        Asynchronous coroutine to update the FactorInstance

        :param auth_payload: The optional payload needed to verify the Factor for the first time. E.g. for a TOTP, the numeric code.
        :param friendly_name: The new friendly name of this Factor. It can be up to 64 characters.
        :param config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Required when `factor_type` is `push`. If specified, this value must be between 32 and 255 characters long.
        :param config_sdk_version: The Verify Push SDK version used to configure the factor
        :param config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive
        :param config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive
        :param config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive
        :param config_alg:
        :param config_notification_platform: The transport technology used to generate the Notification Token. Can be `apn`, `fcm` or `none`.  Required when `factor_type` is `push`.

        :returns: The updated FactorInstance
        """
        return await self._proxy.update_async(
            auth_payload=auth_payload,
            friendly_name=friendly_name,
            config_notification_token=config_notification_token,
            config_sdk_version=config_sdk_version,
            config_time_step=config_time_step,
            config_skew=config_skew,
            config_code_length=config_code_length,
            config_alg=config_alg,
            config_notification_platform=config_notification_platform,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.FactorInstance {}>".format(context)


class FactorContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, identity: str, sid: str):
        """
        Initialize the FactorContext

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Factor. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        :param sid: A 34 character string that uniquely identifies this Factor.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "identity": identity,
            "sid": sid,
        }
        self._uri = "/Services/{service_sid}/Entities/{identity}/Factors/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the FactorInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FactorInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> FactorInstance:
        """
        Fetch the FactorInstance


        :returns: The fetched FactorInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> FactorInstance:
        """
        Asynchronous coroutine to fetch the FactorInstance


        :returns: The fetched FactorInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        auth_payload: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        config_notification_token: Union[str, object] = values.unset,
        config_sdk_version: Union[str, object] = values.unset,
        config_time_step: Union[int, object] = values.unset,
        config_skew: Union[int, object] = values.unset,
        config_code_length: Union[int, object] = values.unset,
        config_alg: Union["FactorInstance.TotpAlgorithms", object] = values.unset,
        config_notification_platform: Union[str, object] = values.unset,
    ) -> FactorInstance:
        """
        Update the FactorInstance

        :param auth_payload: The optional payload needed to verify the Factor for the first time. E.g. for a TOTP, the numeric code.
        :param friendly_name: The new friendly name of this Factor. It can be up to 64 characters.
        :param config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Required when `factor_type` is `push`. If specified, this value must be between 32 and 255 characters long.
        :param config_sdk_version: The Verify Push SDK version used to configure the factor
        :param config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive
        :param config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive
        :param config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive
        :param config_alg:
        :param config_notification_platform: The transport technology used to generate the Notification Token. Can be `apn`, `fcm` or `none`.  Required when `factor_type` is `push`.

        :returns: The updated FactorInstance
        """
        data = values.of(
            {
                "AuthPayload": auth_payload,
                "FriendlyName": friendly_name,
                "Config.NotificationToken": config_notification_token,
                "Config.SdkVersion": config_sdk_version,
                "Config.TimeStep": config_time_step,
                "Config.Skew": config_skew,
                "Config.CodeLength": config_code_length,
                "Config.Alg": config_alg,
                "Config.NotificationPlatform": config_notification_platform,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        auth_payload: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        config_notification_token: Union[str, object] = values.unset,
        config_sdk_version: Union[str, object] = values.unset,
        config_time_step: Union[int, object] = values.unset,
        config_skew: Union[int, object] = values.unset,
        config_code_length: Union[int, object] = values.unset,
        config_alg: Union["FactorInstance.TotpAlgorithms", object] = values.unset,
        config_notification_platform: Union[str, object] = values.unset,
    ) -> FactorInstance:
        """
        Asynchronous coroutine to update the FactorInstance

        :param auth_payload: The optional payload needed to verify the Factor for the first time. E.g. for a TOTP, the numeric code.
        :param friendly_name: The new friendly name of this Factor. It can be up to 64 characters.
        :param config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Required when `factor_type` is `push`. If specified, this value must be between 32 and 255 characters long.
        :param config_sdk_version: The Verify Push SDK version used to configure the factor
        :param config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive
        :param config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive
        :param config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive
        :param config_alg:
        :param config_notification_platform: The transport technology used to generate the Notification Token. Can be `apn`, `fcm` or `none`.  Required when `factor_type` is `push`.

        :returns: The updated FactorInstance
        """
        data = values.of(
            {
                "AuthPayload": auth_payload,
                "FriendlyName": friendly_name,
                "Config.NotificationToken": config_notification_token,
                "Config.SdkVersion": config_sdk_version,
                "Config.TimeStep": config_time_step,
                "Config.Skew": config_skew,
                "Config.CodeLength": config_code_length,
                "Config.Alg": config_alg,
                "Config.NotificationPlatform": config_notification_platform,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.FactorContext {}>".format(context)


class FactorPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> FactorInstance:
        """
        Build an instance of FactorInstance

        :param payload: Payload response from the API
        """
        return FactorInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.FactorPage>"


class FactorList(ListResource):
    def __init__(self, version: Version, service_sid: str, identity: str):
        """
        Initialize the FactorList

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Factors. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "service_sid": service_sid,
            "identity": identity,
        }
        self._uri = "/Services/{service_sid}/Entities/{identity}/Factors".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FactorInstance]:
        """
        Streams FactorInstance records from the API as a generator stream.
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
    ) -> List[FactorInstance]:
        """
        Asynchronously streams FactorInstance records from the API as a generator stream.
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
    ) -> List[FactorInstance]:
        """
        Lists FactorInstance records from the API as a list.
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
    ) -> List[FactorInstance]:
        """
        Asynchronously lists FactorInstance records from the API as a list.
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
    ) -> FactorPage:
        """
        Retrieve a single page of FactorInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FactorInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FactorPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> FactorPage:
        """
        Asynchronously retrieve a single page of FactorInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FactorInstance
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
        return FactorPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> FactorPage:
        """
        Retrieve a specific page of FactorInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FactorInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FactorPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> FactorPage:
        """
        Asynchronously retrieve a specific page of FactorInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FactorInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FactorPage(self._version, response, self._solution)

    def get(self, sid: str) -> FactorContext:
        """
        Constructs a FactorContext

        :param sid: A 34 character string that uniquely identifies this Factor.
        """
        return FactorContext(
            self._version,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
            sid=sid,
        )

    def __call__(self, sid: str) -> FactorContext:
        """
        Constructs a FactorContext

        :param sid: A 34 character string that uniquely identifies this Factor.
        """
        return FactorContext(
            self._version,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Verify.V2.FactorList>"
