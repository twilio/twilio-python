r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.trunking.v1.trunk.credential_list import CredentialListList
from twilio.rest.trunking.v1.trunk.ip_access_control_list import IpAccessControlListList
from twilio.rest.trunking.v1.trunk.origination_url import OriginationUrlList
from twilio.rest.trunking.v1.trunk.phone_number import PhoneNumberList
from twilio.rest.trunking.v1.trunk.recording import RecordingList


class TrunkInstance(InstanceResource):
    class TransferCallerId(object):
        FROM_TRANSFEREE = "from-transferee"
        FROM_TRANSFEROR = "from-transferor"

    class TransferSetting(object):
        DISABLE_ALL = "disable-all"
        ENABLE_ALL = "enable-all"
        SIP_ONLY = "sip-only"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Trunk resource.
    :ivar domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
    :ivar disaster_recovery_method: The HTTP method we use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
    :ivar disaster_recovery_url: The URL we call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from this URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
    :ivar recording: The recording settings for the trunk. Can be: `do-not-record`, `record-from-ringing`, `record-from-answer`. If set to `record-from-ringing` or `record-from-answer`, all calls going through the trunk will be recorded. The only way to change recording parameters is on a sub-resource of a Trunk after it has been created. e.g.`/Trunks/[Trunk_SID]/Recording -XPOST -d'Mode=record-from-answer'`. See [Recording](https://www.twilio.com/docs/sip-trunking#recording) for more information.
    :ivar transfer_mode: 
    :ivar transfer_caller_id: 
    :ivar cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
    :ivar auth_type: The types of authentication mapped to the domain. Can be: `IP_ACL` and `CREDENTIAL_LIST`. If both are mapped, the values are returned in a comma delimited list. If empty, the domain will not receive any traffic.
    :ivar auth_type_set: Reserved.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar sid: The unique string that we created to identify the Trunk resource.
    :ivar url: The absolute URL of the resource.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.domain_name: Optional[str] = payload.get("domain_name")
        self.disaster_recovery_method: Optional[str] = payload.get(
            "disaster_recovery_method"
        )
        self.disaster_recovery_url: Optional[str] = payload.get("disaster_recovery_url")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.secure: Optional[bool] = payload.get("secure")
        self.recording: Optional[Dict[str, object]] = payload.get("recording")
        self.transfer_mode: Optional["TrunkInstance.TransferSetting"] = payload.get(
            "transfer_mode"
        )
        self.transfer_caller_id: Optional["TrunkInstance.TransferCallerId"] = (
            payload.get("transfer_caller_id")
        )
        self.cnam_lookup_enabled: Optional[bool] = payload.get("cnam_lookup_enabled")
        self.auth_type: Optional[str] = payload.get("auth_type")
        self.auth_type_set: Optional[List[str]] = payload.get("auth_type_set")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.sid: Optional[str] = payload.get("sid")
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[TrunkContext] = None

    @property
    def _proxy(self) -> "TrunkContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TrunkContext for this TrunkInstance
        """
        if self._context is None:
            self._context = TrunkContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the TrunkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the TrunkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "TrunkInstance":
        """
        Fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "TrunkInstance":
        """
        Asynchronous coroutine to fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        domain_name: Union[str, object] = values.unset,
        disaster_recovery_url: Union[str, object] = values.unset,
        disaster_recovery_method: Union[str, object] = values.unset,
        transfer_mode: Union["TrunkInstance.TransferSetting", object] = values.unset,
        secure: Union[bool, object] = values.unset,
        cnam_lookup_enabled: Union[bool, object] = values.unset,
        transfer_caller_id: Union[
            "TrunkInstance.TransferCallerId", object
        ] = values.unset,
    ) -> "TrunkInstance":
        """
        Update the TrunkInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param transfer_mode:
        :param secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param transfer_caller_id:

        :returns: The updated TrunkInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            domain_name=domain_name,
            disaster_recovery_url=disaster_recovery_url,
            disaster_recovery_method=disaster_recovery_method,
            transfer_mode=transfer_mode,
            secure=secure,
            cnam_lookup_enabled=cnam_lookup_enabled,
            transfer_caller_id=transfer_caller_id,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        domain_name: Union[str, object] = values.unset,
        disaster_recovery_url: Union[str, object] = values.unset,
        disaster_recovery_method: Union[str, object] = values.unset,
        transfer_mode: Union["TrunkInstance.TransferSetting", object] = values.unset,
        secure: Union[bool, object] = values.unset,
        cnam_lookup_enabled: Union[bool, object] = values.unset,
        transfer_caller_id: Union[
            "TrunkInstance.TransferCallerId", object
        ] = values.unset,
    ) -> "TrunkInstance":
        """
        Asynchronous coroutine to update the TrunkInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param transfer_mode:
        :param secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param transfer_caller_id:

        :returns: The updated TrunkInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            domain_name=domain_name,
            disaster_recovery_url=disaster_recovery_url,
            disaster_recovery_method=disaster_recovery_method,
            transfer_mode=transfer_mode,
            secure=secure,
            cnam_lookup_enabled=cnam_lookup_enabled,
            transfer_caller_id=transfer_caller_id,
        )

    @property
    def credentials_lists(self) -> CredentialListList:
        """
        Access the credentials_lists
        """
        return self._proxy.credentials_lists

    @property
    def ip_access_control_lists(self) -> IpAccessControlListList:
        """
        Access the ip_access_control_lists
        """
        return self._proxy.ip_access_control_lists

    @property
    def origination_urls(self) -> OriginationUrlList:
        """
        Access the origination_urls
        """
        return self._proxy.origination_urls

    @property
    def phone_numbers(self) -> PhoneNumberList:
        """
        Access the phone_numbers
        """
        return self._proxy.phone_numbers

    @property
    def recordings(self) -> RecordingList:
        """
        Access the recordings
        """
        return self._proxy.recordings

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.TrunkInstance {}>".format(context)


class TrunkContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the TrunkContext

        :param version: Version that contains the resource
        :param sid: The unique string that we created to identify the OriginationUrl resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Trunks/{sid}".format(**self._solution)

        self._credentials_lists: Optional[CredentialListList] = None
        self._ip_access_control_lists: Optional[IpAccessControlListList] = None
        self._origination_urls: Optional[OriginationUrlList] = None
        self._phone_numbers: Optional[PhoneNumberList] = None
        self._recordings: Optional[RecordingList] = None

    def delete(self) -> bool:
        """
        Deletes the TrunkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the TrunkInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> TrunkInstance:
        """
        Fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TrunkInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> TrunkInstance:
        """
        Asynchronous coroutine to fetch the TrunkInstance


        :returns: The fetched TrunkInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TrunkInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        domain_name: Union[str, object] = values.unset,
        disaster_recovery_url: Union[str, object] = values.unset,
        disaster_recovery_method: Union[str, object] = values.unset,
        transfer_mode: Union["TrunkInstance.TransferSetting", object] = values.unset,
        secure: Union[bool, object] = values.unset,
        cnam_lookup_enabled: Union[bool, object] = values.unset,
        transfer_caller_id: Union[
            "TrunkInstance.TransferCallerId", object
        ] = values.unset,
    ) -> TrunkInstance:
        """
        Update the TrunkInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param transfer_mode:
        :param secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param transfer_caller_id:

        :returns: The updated TrunkInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DomainName": domain_name,
                "DisasterRecoveryUrl": disaster_recovery_url,
                "DisasterRecoveryMethod": disaster_recovery_method,
                "TransferMode": transfer_mode,
                "Secure": secure,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "TransferCallerId": transfer_caller_id,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrunkInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        domain_name: Union[str, object] = values.unset,
        disaster_recovery_url: Union[str, object] = values.unset,
        disaster_recovery_method: Union[str, object] = values.unset,
        transfer_mode: Union["TrunkInstance.TransferSetting", object] = values.unset,
        secure: Union[bool, object] = values.unset,
        cnam_lookup_enabled: Union[bool, object] = values.unset,
        transfer_caller_id: Union[
            "TrunkInstance.TransferCallerId", object
        ] = values.unset,
    ) -> TrunkInstance:
        """
        Asynchronous coroutine to update the TrunkInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param transfer_mode:
        :param secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param transfer_caller_id:

        :returns: The updated TrunkInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DomainName": domain_name,
                "DisasterRecoveryUrl": disaster_recovery_url,
                "DisasterRecoveryMethod": disaster_recovery_method,
                "TransferMode": transfer_mode,
                "Secure": secure,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "TransferCallerId": transfer_caller_id,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrunkInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def credentials_lists(self) -> CredentialListList:
        """
        Access the credentials_lists
        """
        if self._credentials_lists is None:
            self._credentials_lists = CredentialListList(
                self._version,
                self._solution["sid"],
            )
        return self._credentials_lists

    @property
    def ip_access_control_lists(self) -> IpAccessControlListList:
        """
        Access the ip_access_control_lists
        """
        if self._ip_access_control_lists is None:
            self._ip_access_control_lists = IpAccessControlListList(
                self._version,
                self._solution["sid"],
            )
        return self._ip_access_control_lists

    @property
    def origination_urls(self) -> OriginationUrlList:
        """
        Access the origination_urls
        """
        if self._origination_urls is None:
            self._origination_urls = OriginationUrlList(
                self._version,
                self._solution["sid"],
            )
        return self._origination_urls

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
    def recordings(self) -> RecordingList:
        """
        Access the recordings
        """
        if self._recordings is None:
            self._recordings = RecordingList(
                self._version,
                self._solution["sid"],
            )
        return self._recordings

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trunking.V1.TrunkContext {}>".format(context)


class TrunkPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> TrunkInstance:
        """
        Build an instance of TrunkInstance

        :param payload: Payload response from the API
        """
        return TrunkInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.TrunkPage>"


class TrunkList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the TrunkList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Trunks"

    def create(
        self,
        friendly_name: Union[str, object] = values.unset,
        domain_name: Union[str, object] = values.unset,
        disaster_recovery_url: Union[str, object] = values.unset,
        disaster_recovery_method: Union[str, object] = values.unset,
        transfer_mode: Union["TrunkInstance.TransferSetting", object] = values.unset,
        secure: Union[bool, object] = values.unset,
        cnam_lookup_enabled: Union[bool, object] = values.unset,
        transfer_caller_id: Union[
            "TrunkInstance.TransferCallerId", object
        ] = values.unset,
    ) -> TrunkInstance:
        """
        Create the TrunkInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param transfer_mode:
        :param secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param transfer_caller_id:

        :returns: The created TrunkInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DomainName": domain_name,
                "DisasterRecoveryUrl": disaster_recovery_url,
                "DisasterRecoveryMethod": disaster_recovery_method,
                "TransferMode": transfer_mode,
                "Secure": secure,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "TransferCallerId": transfer_caller_id,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrunkInstance(self._version, payload)

    async def create_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        domain_name: Union[str, object] = values.unset,
        disaster_recovery_url: Union[str, object] = values.unset,
        disaster_recovery_method: Union[str, object] = values.unset,
        transfer_mode: Union["TrunkInstance.TransferSetting", object] = values.unset,
        secure: Union[bool, object] = values.unset,
        cnam_lookup_enabled: Union[bool, object] = values.unset,
        transfer_caller_id: Union[
            "TrunkInstance.TransferCallerId", object
        ] = values.unset,
    ) -> TrunkInstance:
        """
        Asynchronously create the TrunkInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param domain_name: The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and `-` and must end with `pstn.twilio.com`. See [Termination Settings](https://www.twilio.com/docs/sip-trunking#termination) for more information.
        :param disaster_recovery_url: The URL we should call using the `disaster_recovery_method` if an error occurs while sending SIP traffic towards the configured Origination URL. We retrieve TwiML from the URL and execute the instructions like any other normal TwiML call. See [Disaster Recovery](https://www.twilio.com/docs/sip-trunking#disaster-recovery) for more information.
        :param disaster_recovery_method: The HTTP method we should use to call the `disaster_recovery_url`. Can be: `GET` or `POST`.
        :param transfer_mode:
        :param secure: Whether Secure Trunking is enabled for the trunk. If enabled, all calls going through the trunk will be secure using SRTP for media and TLS for signaling. If disabled, then RTP will be used for media. See [Secure Trunking](https://www.twilio.com/docs/sip-trunking#securetrunking) for more information.
        :param cnam_lookup_enabled: Whether Caller ID Name (CNAM) lookup should be enabled for the trunk. If enabled, all inbound calls to the SIP Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
        :param transfer_caller_id:

        :returns: The created TrunkInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "DomainName": domain_name,
                "DisasterRecoveryUrl": disaster_recovery_url,
                "DisasterRecoveryMethod": disaster_recovery_method,
                "TransferMode": transfer_mode,
                "Secure": secure,
                "CnamLookupEnabled": cnam_lookup_enabled,
                "TransferCallerId": transfer_caller_id,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TrunkInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[TrunkInstance]:
        """
        Streams TrunkInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[TrunkInstance]:
        """
        Asynchronously streams TrunkInstance records from the API as a generator stream.
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

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[TrunkInstance]:
        """
        Lists TrunkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[TrunkInstance]:
        """
        Asynchronously lists TrunkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> TrunkPage:
        """
        Retrieve a single page of TrunkInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of TrunkInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TrunkPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> TrunkPage:
        """
        Asynchronously retrieve a single page of TrunkInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of TrunkInstance
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
        return TrunkPage(self._version, response)

    def get_page(self, target_url: str) -> TrunkPage:
        """
        Retrieve a specific page of TrunkInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of TrunkInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TrunkPage(self._version, response)

    async def get_page_async(self, target_url: str) -> TrunkPage:
        """
        Asynchronously retrieve a specific page of TrunkInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of TrunkInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return TrunkPage(self._version, response)

    def get(self, sid: str) -> TrunkContext:
        """
        Constructs a TrunkContext

        :param sid: The unique string that we created to identify the OriginationUrl resource to update.
        """
        return TrunkContext(self._version, sid=sid)

    def __call__(self, sid: str) -> TrunkContext:
        """
        Constructs a TrunkContext

        :param sid: The unique string that we created to identify the OriginationUrl resource to update.
        """
        return TrunkContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trunking.V1.TrunkList>"
