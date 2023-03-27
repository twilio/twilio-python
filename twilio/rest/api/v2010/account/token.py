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
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class TokenInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Token resource.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar ice_servers: An array representing the ephemeral credentials and the STUN and TURN server URIs.
    :ivar password: The temporary password that the username will use when authenticating with Twilio.
    :ivar ttl: The duration in seconds for which the username and password are valid.
    :ivar username: The temporary username that uniquely identifies a Token.
    """

    def __init__(self, version: Version, payload: Dict[str, Any], account_sid: str):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.ice_servers: Optional[List[str]] = payload.get("ice_servers")
        self.password: Optional[str] = payload.get("password")
        self.ttl: Optional[str] = payload.get("ttl")
        self.username: Optional[str] = payload.get("username")

        self._solution = {
            "account_sid": account_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.TokenInstance {}>".format(context)


class TokenList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the TokenList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Tokens.json".format(**self._solution)

    def create(self, ttl=values.unset) -> TokenInstance:
        """
        Create the TokenInstance

        :param int ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours).

        :returns: The created TokenInstance
        """
        data = values.of(
            {
                "Ttl": ttl,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TokenInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(self, ttl=values.unset) -> TokenInstance:
        """
        Asynchronously create the TokenInstance

        :param int ttl: The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours).

        :returns: The created TokenInstance
        """
        data = values.of(
            {
                "Ttl": ttl,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TokenInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.TokenList>"
