r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class LocalInstance(InstanceResource):

    class AddressRequirement:
        NONE = "none"
        ANY = "any"
        LOCAL = "local"
        FOREIGN = "foreign"

    class EmergencyAddressStatus:
        REGISTERED = "registered"
        UNREGISTERED = "unregistered"
        PENDING_REGISTRATION = "pending-registration"
        REGISTRATION_FAILURE = "registration-failure"
        PENDING_UNREGISTRATION = "pending-unregistration"
        UNREGISTRATION_FAILURE = "unregistration-failure"

    class EmergencyStatus:
        ACTIVE = "Active"
        INACTIVE = "Inactive"

    class VoiceReceiveMode:
        VOICE = "voice"
        FAX = "fax"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resource.
    :ivar address_sid: The SID of the Address resource associated with the phone number.
    :ivar address_requirements: 
    :ivar api_version: The API version used to start a new TwiML session.
    :ivar beta: Whether the phone number is new to the Twilio platform. Can be: `true` or `false`.
    :ivar capabilities: 
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar identity_sid: The SID of the Identity resource that we associate with the phone number. Some regions require an Identity to meet local regulations.
    :ivar phone_number: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    :ivar origin: The phone number's origin. `twilio` identifies Twilio-owned phone numbers and `hosted` identifies hosted phone numbers.
    :ivar sid: The unique string that that we created to identify the resource.
    :ivar sms_application_sid: The SID of the application that handles SMS messages sent to the phone number. If an `sms_application_sid` is present, we ignore all `sms_*_url` values and use those of the application.
    :ivar sms_fallback_method: The HTTP method we use to call `sms_fallback_url`. Can be: `GET` or `POST`.
    :ivar sms_fallback_url: The URL that we call when an error occurs while retrieving or executing the TwiML from `sms_url`.
    :ivar sms_method: The HTTP method we use to call `sms_url`. Can be: `GET` or `POST`.
    :ivar sms_url: The URL we call when the phone number receives an incoming SMS message.
    :ivar status_callback: The URL we call using the `status_callback_method` to send status information to your application.
    :ivar status_callback_method: The HTTP method we use to call `status_callback`. Can be: `GET` or `POST`.
    :ivar trunk_sid: The SID of the Trunk that handles calls to the phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    :ivar voice_receive_mode: 
    :ivar voice_application_sid: The SID of the application that handles calls to the phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
    :ivar voice_caller_id_lookup: Whether we look up the caller's caller-ID name from the CNAM database ($0.01 per look up). Can be: `true` or `false`.
    :ivar voice_fallback_method: The HTTP method we use to call `voice_fallback_url`. Can be: `GET` or `POST`.
    :ivar voice_fallback_url: The URL that we call when an error occurs retrieving or executing the TwiML requested by `url`.
    :ivar voice_method: The HTTP method we use to call `voice_url`. Can be: `GET` or `POST`.
    :ivar voice_url: The URL we call when this phone number receives a call. The `voice_url` will not be used if a `voice_application_sid` or a `trunk_sid` is set.
    :ivar emergency_status: 
    :ivar emergency_address_sid: The SID of the emergency address configuration that we use for emergency calling from this phone number.
    :ivar emergency_address_status: 
    :ivar bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
    :ivar status: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], account_sid: str):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.address_sid: Optional[str] = payload.get("address_sid")
        self.address_requirements: Optional["LocalInstance.AddressRequirement"] = (
            payload.get("address_requirements")
        )
        self.api_version: Optional[str] = payload.get("api_version")
        self.beta: Optional[bool] = payload.get("beta")
        self.capabilities: Optional[str] = payload.get("capabilities")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.identity_sid: Optional[str] = payload.get("identity_sid")
        self.phone_number: Optional[str] = payload.get("phone_number")
        self.origin: Optional[str] = payload.get("origin")
        self.sid: Optional[str] = payload.get("sid")
        self.sms_application_sid: Optional[str] = payload.get("sms_application_sid")
        self.sms_fallback_method: Optional[str] = payload.get("sms_fallback_method")
        self.sms_fallback_url: Optional[str] = payload.get("sms_fallback_url")
        self.sms_method: Optional[str] = payload.get("sms_method")
        self.sms_url: Optional[str] = payload.get("sms_url")
        self.status_callback: Optional[str] = payload.get("status_callback")
        self.status_callback_method: Optional[str] = payload.get(
            "status_callback_method"
        )
        self.trunk_sid: Optional[str] = payload.get("trunk_sid")
        self.uri: Optional[str] = payload.get("uri")
        self.voice_receive_mode: Optional["LocalInstance.VoiceReceiveMode"] = (
            payload.get("voice_receive_mode")
        )
        self.voice_application_sid: Optional[str] = payload.get("voice_application_sid")
        self.voice_caller_id_lookup: Optional[bool] = payload.get(
            "voice_caller_id_lookup"
        )
        self.voice_fallback_method: Optional[str] = payload.get("voice_fallback_method")
        self.voice_fallback_url: Optional[str] = payload.get("voice_fallback_url")
        self.voice_method: Optional[str] = payload.get("voice_method")
        self.voice_url: Optional[str] = payload.get("voice_url")
        self.emergency_status: Optional["LocalInstance.EmergencyStatus"] = payload.get(
            "emergency_status"
        )
        self.emergency_address_sid: Optional[str] = payload.get("emergency_address_sid")
        self.emergency_address_status: Optional[
            "LocalInstance.EmergencyAddressStatus"
        ] = payload.get("emergency_address_status")
        self.bundle_sid: Optional[str] = payload.get("bundle_sid")
        self.status: Optional[str] = payload.get("status")

        self._solution = {
            "account_sid": account_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join(f"{k}={v}" for k, v in self._solution.items())
        return f"<Twilio.Api.V2010.LocalInstance {context}>"


class LocalPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> LocalInstance:
        """
        Build an instance of LocalInstance

        :param payload: Payload response from the API
        """
        return LocalInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.LocalPage>"


class LocalList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the LocalList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/IncomingPhoneNumbers/Local.json".format(
            **self._solution
        )

    def create(
        self,
        phone_number: str,
        api_version: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        sms_application_sid: Union[str, object] = values.unset,
        sms_fallback_method: Union[str, object] = values.unset,
        sms_fallback_url: Union[str, object] = values.unset,
        sms_method: Union[str, object] = values.unset,
        sms_url: Union[str, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        voice_application_sid: Union[str, object] = values.unset,
        voice_caller_id_lookup: Union[bool, object] = values.unset,
        voice_fallback_method: Union[str, object] = values.unset,
        voice_fallback_url: Union[str, object] = values.unset,
        voice_method: Union[str, object] = values.unset,
        voice_url: Union[str, object] = values.unset,
        identity_sid: Union[str, object] = values.unset,
        address_sid: Union[str, object] = values.unset,
        emergency_status: Union["LocalInstance.EmergencyStatus", object] = values.unset,
        emergency_address_sid: Union[str, object] = values.unset,
        trunk_sid: Union[str, object] = values.unset,
        voice_receive_mode: Union[
            "LocalInstance.VoiceReceiveMode", object
        ] = values.unset,
        bundle_sid: Union[str, object] = values.unset,
    ) -> LocalInstance:
        """
        Create the LocalInstance

        :param phone_number: The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
        :param api_version: The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`.
        :param friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.
        :param sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.
        :param sms_fallback_method: The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.
        :param sms_method: The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param sms_url: The URL we should call when the new phone number receives an incoming SMS message.
        :param status_callback: The URL we should call using the `status_callback_method` to send status information to your application.
        :param status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
        :param voice_application_sid: The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
        :param voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
        :param voice_fallback_method: The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
        :param voice_method: The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param voice_url: The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
        :param identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
        :param address_sid: The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
        :param emergency_status:
        :param emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the new phone number.
        :param trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
        :param voice_receive_mode:
        :param bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.

        :returns: The created LocalInstance
        """

        data = values.of(
            {
                "PhoneNumber": phone_number,
                "ApiVersion": api_version,
                "FriendlyName": friendly_name,
                "SmsApplicationSid": sms_application_sid,
                "SmsFallbackMethod": sms_fallback_method,
                "SmsFallbackUrl": sms_fallback_url,
                "SmsMethod": sms_method,
                "SmsUrl": sms_url,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "VoiceApplicationSid": voice_application_sid,
                "VoiceCallerIdLookup": serialize.boolean_to_string(
                    voice_caller_id_lookup
                ),
                "VoiceFallbackMethod": voice_fallback_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceMethod": voice_method,
                "VoiceUrl": voice_url,
                "IdentitySid": identity_sid,
                "AddressSid": address_sid,
                "EmergencyStatus": emergency_status,
                "EmergencyAddressSid": emergency_address_sid,
                "TrunkSid": trunk_sid,
                "VoiceReceiveMode": voice_receive_mode,
                "BundleSid": bundle_sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return LocalInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(
        self,
        phone_number: str,
        api_version: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        sms_application_sid: Union[str, object] = values.unset,
        sms_fallback_method: Union[str, object] = values.unset,
        sms_fallback_url: Union[str, object] = values.unset,
        sms_method: Union[str, object] = values.unset,
        sms_url: Union[str, object] = values.unset,
        status_callback: Union[str, object] = values.unset,
        status_callback_method: Union[str, object] = values.unset,
        voice_application_sid: Union[str, object] = values.unset,
        voice_caller_id_lookup: Union[bool, object] = values.unset,
        voice_fallback_method: Union[str, object] = values.unset,
        voice_fallback_url: Union[str, object] = values.unset,
        voice_method: Union[str, object] = values.unset,
        voice_url: Union[str, object] = values.unset,
        identity_sid: Union[str, object] = values.unset,
        address_sid: Union[str, object] = values.unset,
        emergency_status: Union["LocalInstance.EmergencyStatus", object] = values.unset,
        emergency_address_sid: Union[str, object] = values.unset,
        trunk_sid: Union[str, object] = values.unset,
        voice_receive_mode: Union[
            "LocalInstance.VoiceReceiveMode", object
        ] = values.unset,
        bundle_sid: Union[str, object] = values.unset,
    ) -> LocalInstance:
        """
        Asynchronously create the LocalInstance

        :param phone_number: The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
        :param api_version: The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`.
        :param friendly_name: A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, this is a formatted version of the phone number.
        :param sms_application_sid: The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those set on the application.
        :param sms_fallback_method: The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param sms_fallback_url: The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.
        :param sms_method: The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param sms_url: The URL we should call when the new phone number receives an incoming SMS message.
        :param status_callback: The URL we should call using the `status_callback_method` to send status information to your application.
        :param status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
        :param voice_application_sid: The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
        :param voice_caller_id_lookup: Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
        :param voice_fallback_method: The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param voice_fallback_url: The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
        :param voice_method: The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.
        :param voice_url: The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
        :param identity_sid: The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
        :param address_sid: The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
        :param emergency_status:
        :param emergency_address_sid: The SID of the emergency address configuration to use for emergency calling from the new phone number.
        :param trunk_sid: The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
        :param voice_receive_mode:
        :param bundle_sid: The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.

        :returns: The created LocalInstance
        """

        data = values.of(
            {
                "PhoneNumber": phone_number,
                "ApiVersion": api_version,
                "FriendlyName": friendly_name,
                "SmsApplicationSid": sms_application_sid,
                "SmsFallbackMethod": sms_fallback_method,
                "SmsFallbackUrl": sms_fallback_url,
                "SmsMethod": sms_method,
                "SmsUrl": sms_url,
                "StatusCallback": status_callback,
                "StatusCallbackMethod": status_callback_method,
                "VoiceApplicationSid": voice_application_sid,
                "VoiceCallerIdLookup": serialize.boolean_to_string(
                    voice_caller_id_lookup
                ),
                "VoiceFallbackMethod": voice_fallback_method,
                "VoiceFallbackUrl": voice_fallback_url,
                "VoiceMethod": voice_method,
                "VoiceUrl": voice_url,
                "IdentitySid": identity_sid,
                "AddressSid": address_sid,
                "EmergencyStatus": emergency_status,
                "EmergencyAddressSid": emergency_address_sid,
                "TrunkSid": trunk_sid,
                "VoiceReceiveMode": voice_receive_mode,
                "BundleSid": bundle_sid,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return LocalInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def stream(
        self,
        beta: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        origin: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[LocalInstance]:
        """
        Streams LocalInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str friendly_name: A string that identifies the resources to read.
        :param str phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param str origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        beta: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        origin: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[LocalInstance]:
        """
        Asynchronously streams LocalInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str friendly_name: A string that identifies the resources to read.
        :param str phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param str origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        beta: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        origin: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[LocalInstance]:
        """
        Lists LocalInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str friendly_name: A string that identifies the resources to read.
        :param str phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param str origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                beta=beta,
                friendly_name=friendly_name,
                phone_number=phone_number,
                origin=origin,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        beta: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        origin: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[LocalInstance]:
        """
        Asynchronously lists LocalInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param str friendly_name: A string that identifies the resources to read.
        :param str phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param str origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                beta=beta,
                friendly_name=friendly_name,
                phone_number=phone_number,
                origin=origin,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        beta: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        origin: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> LocalPage:
        """
        Retrieve a single page of LocalInstance records from the API.
        Request is executed immediately

        :param beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param friendly_name: A string that identifies the resources to read.
        :param phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of LocalInstance
        """
        data = values.of(
            {
                "Beta": serialize.boolean_to_string(beta),
                "FriendlyName": friendly_name,
                "PhoneNumber": phone_number,
                "Origin": origin,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return LocalPage(self._version, response, self._solution)

    async def page_async(
        self,
        beta: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        phone_number: Union[str, object] = values.unset,
        origin: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> LocalPage:
        """
        Asynchronously retrieve a single page of LocalInstance records from the API.
        Request is executed immediately

        :param beta: Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
        :param friendly_name: A string that identifies the resources to read.
        :param phone_number: The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
        :param origin: Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of LocalInstance
        """
        data = values.of(
            {
                "Beta": serialize.boolean_to_string(beta),
                "FriendlyName": friendly_name,
                "PhoneNumber": phone_number,
                "Origin": origin,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return LocalPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> LocalPage:
        """
        Retrieve a specific page of LocalInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of LocalInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return LocalPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> LocalPage:
        """
        Asynchronously retrieve a specific page of LocalInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of LocalInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return LocalPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.LocalList>"
