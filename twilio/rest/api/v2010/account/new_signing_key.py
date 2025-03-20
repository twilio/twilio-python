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
from typing import Any, Dict, Optional, Union
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class NewSigningKeyInstance(InstanceResource):
    """
    :ivar sid: The unique string that that we created to identify the NewSigningKey resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar secret: The secret your application uses to sign Access Tokens and to authenticate to the REST API (you will use this as the basic-auth `password`).  **Note that for security reasons, this field is ONLY returned when the API Key is first created.**
    """

    def __init__(self, version: Version, payload: Dict[str, Any], account_sid: str):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.secret: Optional[str] = payload.get("secret")

        self._solution = {
            "account_sid": account_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.NewSigningKeyInstance {}>".format(context)


class NewSigningKeyList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the NewSigningKeyList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will be responsible for the new Key resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/SigningKeys.json".format(**self._solution)

    def create(
        self, friendly_name: Union[str, object] = values.unset
    ) -> NewSigningKeyInstance:
        """
        Create the NewSigningKeyInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The created NewSigningKeyInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = self._version.create(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return NewSigningKeyInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(
        self, friendly_name: Union[str, object] = values.unset
    ) -> NewSigningKeyInstance:
        """
        Asynchronously create the NewSigningKeyInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The created NewSigningKeyInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )
        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Content-Type"] = "application/x-www-form-urlencoded"

        headers["Accept"] = "application/json"

        payload = await self._version.create_async(
            method="POST", uri=self._uri, data=data, headers=headers
        )

        return NewSigningKeyInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.NewSigningKeyList>"
