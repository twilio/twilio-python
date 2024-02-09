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
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NewFactorInstance(InstanceResource):
    class FactorStatuses(object):
        UNVERIFIED = "unverified"
        VERIFIED = "verified"

    class FactorTypes(object):
        PUSH = "push"
        TOTP = "totp"

    class NotificationPlatforms(object):
        APN = "apn"
        FCM = "fcm"
        NONE = "none"

    class TotpAlgorithms(object):
        SHA1 = "sha1"
        SHA256 = "sha256"
        SHA512 = "sha512"

    """
    :ivar sid: A 34 character string that uniquely identifies this Factor.
    :ivar account_sid: The unique SID identifier of the Account.
    :ivar service_sid: The unique SID identifier of the Service.
    :ivar entity_sid: The unique SID identifier of the Entity.
    :ivar identity: Customer unique identity for the Entity owner of the Factor. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
    :ivar binding: Contains the `factor_type` specific secret and metadata. For push, this is `binding.public_key` and `binding.alg`. For totp, this is `binding.secret` and `binding.uri`. The `binding.uri` property is generated following the [google authenticator key URI format](https://github.com/google/google-authenticator/wiki/Key-Uri-Format), and `Factor.friendly_name` is used for the “accountname” value and `Service.friendly_name` or `Service.totp.issuer` is used for the `issuer` value.   The Binding property is ONLY returned upon Factor creation.
    :ivar date_created: The date that this Factor was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date that this Factor was updated, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar friendly_name: The friendly name of this Factor. This can be any string up to 64 characters, meant for humans to distinguish between Factors. For `factor_type` `push`, this could be a device name. For `factor_type` `totp`, this value is used as the “account name” in constructing the `binding.uri` property. At the same time, we recommend avoiding providing PII.
    :ivar status: 
    :ivar factor_type: 
    :ivar config: An object that contains configurations specific to a `factor_type`.
    :ivar metadata: Custom metadata associated with the factor. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\"os\": \"Android\"}`. Can be up to 1024 characters in length.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], service_sid: str, identity: str
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.entity_sid: Optional[str] = payload.get("entity_sid")
        self.identity: Optional[str] = payload.get("identity")
        self.binding: Optional[Dict[str, object]] = payload.get("binding")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.status: Optional["NewFactorInstance.FactorStatuses"] = payload.get(
            "status"
        )
        self.factor_type: Optional["NewFactorInstance.FactorTypes"] = payload.get(
            "factor_type"
        )
        self.config: Optional[Dict[str, object]] = payload.get("config")
        self.metadata: Optional[Dict[str, object]] = payload.get("metadata")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "service_sid": service_sid,
            "identity": identity,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Verify.V2.NewFactorInstance {}>".format(context)


class NewFactorList(ListResource):
    def __init__(self, version: Version, service_sid: str, identity: str):
        """
        Initialize the NewFactorList

        :param version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Factor. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.

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

    def create(
        self,
        friendly_name: str,
        factor_type: "NewFactorInstance.FactorTypes",
        binding_alg: Union[str, object] = values.unset,
        binding_public_key: Union[str, object] = values.unset,
        config_app_id: Union[str, object] = values.unset,
        config_notification_platform: Union[
            "NewFactorInstance.NotificationPlatforms", object
        ] = values.unset,
        config_notification_token: Union[str, object] = values.unset,
        config_sdk_version: Union[str, object] = values.unset,
        binding_secret: Union[str, object] = values.unset,
        config_time_step: Union[int, object] = values.unset,
        config_skew: Union[int, object] = values.unset,
        config_code_length: Union[int, object] = values.unset,
        config_alg: Union["NewFactorInstance.TotpAlgorithms", object] = values.unset,
        metadata: Union[object, object] = values.unset,
    ) -> NewFactorInstance:
        """
        Create the NewFactorInstance

        :param friendly_name: The friendly name of this Factor. This can be any string up to 64 characters, meant for humans to distinguish between Factors. For `factor_type` `push`, this could be a device name. For `factor_type` `totp`, this value is used as the “account name” in constructing the `binding.uri` property. At the same time, we recommend avoiding providing PII.
        :param factor_type:
        :param binding_alg: The algorithm used when `factor_type` is `push`. Algorithm supported: `ES256`
        :param binding_public_key: The Ecdsa public key in PKIX, ASN.1 DER format encoded in Base64.  Required when `factor_type` is `push`
        :param config_app_id: The ID that uniquely identifies your app in the Google or Apple store, such as `com.example.myapp`. It can be up to 100 characters long.  Required when `factor_type` is `push`.
        :param config_notification_platform:
        :param config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Must be between 32 and 255 characters long.  Required when `factor_type` is `push`.
        :param config_sdk_version: The Verify Push SDK version used to configure the factor  Required when `factor_type` is `push`
        :param binding_secret: The shared secret for TOTP factors encoded in Base32. This can be provided when creating the Factor, otherwise it will be generated.  Used when `factor_type` is `totp`
        :param config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. The default value is defined at the service level in the property `totp.time_step`. Defaults to 30 seconds if not configured.  Used when `factor_type` is `totp`
        :param config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. The default value is defined at the service level in the property `totp.skew`. If not configured defaults to 1.  Used when `factor_type` is `totp`
        :param config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. The default value is defined at the service level in the property `totp.code_length`. If not configured defaults to 6.  Used when `factor_type` is `totp`
        :param config_alg:
        :param metadata: Custom metadata associated with the factor. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\\\"os\\\": \\\"Android\\\"}`. Can be up to 1024 characters in length.

        :returns: The created NewFactorInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "FactorType": factor_type,
                "Binding.Alg": binding_alg,
                "Binding.PublicKey": binding_public_key,
                "Config.AppId": config_app_id,
                "Config.NotificationPlatform": config_notification_platform,
                "Config.NotificationToken": config_notification_token,
                "Config.SdkVersion": config_sdk_version,
                "Binding.Secret": binding_secret,
                "Config.TimeStep": config_time_step,
                "Config.Skew": config_skew,
                "Config.CodeLength": config_code_length,
                "Config.Alg": config_alg,
                "Metadata": serialize.object(metadata),
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NewFactorInstance(
            self._version,
            payload,
            service_sid=self._solution["service_sid"],
            identity=self._solution["identity"],
        )

    async def create_async(
        self,
        friendly_name: str,
        factor_type: "NewFactorInstance.FactorTypes",
        binding_alg: Union[str, object] = values.unset,
        binding_public_key: Union[str, object] = values.unset,
        config_app_id: Union[str, object] = values.unset,
        config_notification_platform: Union[
            "NewFactorInstance.NotificationPlatforms", object
        ] = values.unset,
        config_notification_token: Union[str, object] = values.unset,
        config_sdk_version: Union[str, object] = values.unset,
        binding_secret: Union[str, object] = values.unset,
        config_time_step: Union[int, object] = values.unset,
        config_skew: Union[int, object] = values.unset,
        config_code_length: Union[int, object] = values.unset,
        config_alg: Union["NewFactorInstance.TotpAlgorithms", object] = values.unset,
        metadata: Union[object, object] = values.unset,
    ) -> NewFactorInstance:
        """
        Asynchronously create the NewFactorInstance

        :param friendly_name: The friendly name of this Factor. This can be any string up to 64 characters, meant for humans to distinguish between Factors. For `factor_type` `push`, this could be a device name. For `factor_type` `totp`, this value is used as the “account name” in constructing the `binding.uri` property. At the same time, we recommend avoiding providing PII.
        :param factor_type:
        :param binding_alg: The algorithm used when `factor_type` is `push`. Algorithm supported: `ES256`
        :param binding_public_key: The Ecdsa public key in PKIX, ASN.1 DER format encoded in Base64.  Required when `factor_type` is `push`
        :param config_app_id: The ID that uniquely identifies your app in the Google or Apple store, such as `com.example.myapp`. It can be up to 100 characters long.  Required when `factor_type` is `push`.
        :param config_notification_platform:
        :param config_notification_token: For APN, the device token. For FCM, the registration token. It is used to send the push notifications. Must be between 32 and 255 characters long.  Required when `factor_type` is `push`.
        :param config_sdk_version: The Verify Push SDK version used to configure the factor  Required when `factor_type` is `push`
        :param binding_secret: The shared secret for TOTP factors encoded in Base32. This can be provided when creating the Factor, otherwise it will be generated.  Used when `factor_type` is `totp`
        :param config_time_step: Defines how often, in seconds, are TOTP codes generated. i.e, a new TOTP code is generated every time_step seconds. Must be between 20 and 60 seconds, inclusive. The default value is defined at the service level in the property `totp.time_step`. Defaults to 30 seconds if not configured.  Used when `factor_type` is `totp`
        :param config_skew: The number of time-steps, past and future, that are valid for validation of TOTP codes. Must be between 0 and 2, inclusive. The default value is defined at the service level in the property `totp.skew`. If not configured defaults to 1.  Used when `factor_type` is `totp`
        :param config_code_length: Number of digits for generated TOTP codes. Must be between 3 and 8, inclusive. The default value is defined at the service level in the property `totp.code_length`. If not configured defaults to 6.  Used when `factor_type` is `totp`
        :param config_alg:
        :param metadata: Custom metadata associated with the factor. This is added by the Device/SDK directly to allow for the inclusion of device information. It must be a stringified JSON with only strings values eg. `{\\\"os\\\": \\\"Android\\\"}`. Can be up to 1024 characters in length.

        :returns: The created NewFactorInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "FactorType": factor_type,
                "Binding.Alg": binding_alg,
                "Binding.PublicKey": binding_public_key,
                "Config.AppId": config_app_id,
                "Config.NotificationPlatform": config_notification_platform,
                "Config.NotificationToken": config_notification_token,
                "Config.SdkVersion": config_sdk_version,
                "Binding.Secret": binding_secret,
                "Config.TimeStep": config_time_step,
                "Config.Skew": config_skew,
                "Config.CodeLength": config_code_length,
                "Config.Alg": config_alg,
                "Metadata": serialize.object(metadata),
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return NewFactorInstance(
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
        return "<Twilio.Verify.V2.NewFactorList>"
