r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Iam
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Optional
from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.iam.v1.api_key import ApiKeyList
from twilio.rest.iam.v1.get_api_keys import GetApiKeysList
from twilio.rest.iam.v1.key import KeyList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Iam

        :param domain: The Twilio.iam domain
        """
        super().__init__(domain, "v1")
        self._api_key: Optional[ApiKeyList] = None
        self._get_api_keys: Optional[GetApiKeysList] = None
        self._keys: Optional[KeyList] = None

    @property
    def api_key(self) -> ApiKeyList:
        if self._api_key is None:
            self._api_key = ApiKeyList(self)
        return self._api_key

    @property
    def get_api_keys(self) -> GetApiKeysList:
        if self._get_api_keys is None:
            self._get_api_keys = GetApiKeysList(self)
        return self._get_api_keys

    @property
    def keys(self) -> KeyList:
        if self._keys is None:
            self._keys = KeyList(self)
        return self._keys

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Iam.V1>"
