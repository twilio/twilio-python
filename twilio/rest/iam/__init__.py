from warnings import warn

from twilio.rest.iam.IamBase import IamBase
from twilio.rest.iam.v1.api_key import ApiKeyList
from twilio.rest.iam.v1.get_api_keys import GetApiKeysList


class Iam(IamBase):
    @property
    def api_key(self) -> ApiKeyList:
        warn(
            "api_key is deprecated. Use v1.api_key instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.api_key

    @property
    def get_api_keys(self) -> GetApiKeysList:
        warn(
            "get_api_keys is deprecated. Use v1.get_api_keys instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.get_api_keys
