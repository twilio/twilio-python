from warnings import warn

from twilio.rest.iam.IamBase import IamBase
from twilio.rest.iam.v1.api_key import ApiKeyList
from twilio.rest.iam.v1.get_api_keys import GetApiKeysList
from twilio.rest.iam.v1.new_api_key import NewApiKeyList


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

    @property
    def new_api_key(self) -> NewApiKeyList:
        warn(
            "new_api_key is deprecated. Use v1.new_api_key instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.new_api_key
