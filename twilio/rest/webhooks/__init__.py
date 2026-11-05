from warnings import warn

from twilio.rest.webhooks.WebhooksBase import WebhooksBase
from twilio.rest.webhooks.v1.auth_profile import AuthProfileList
from twilio.rest.webhooks.v1.edge_zone import EdgeZoneList
from twilio.rest.webhooks.v1.operation import OperationList
from twilio.rest.webhooks.v1.rule import RuleList
from twilio.rest.webhooks.v1.setting import SettingList
from twilio.rest.webhooks.v1.shared_key import SharedKeyList
from twilio.rest.webhooks.v1.test import TestList


class Webhooks(WebhooksBase):

    @property
    def auth_profiles(self) -> AuthProfileList:
        warn(
            "auth_profiles is deprecated. Use v1.auth_profiles instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.auth_profiles

    @property
    def edge_zones(self) -> EdgeZoneList:
        warn(
            "edge_zones is deprecated. Use v1.edge_zones instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.edge_zones

    @property
    def operations(self) -> OperationList:
        warn(
            "operations is deprecated. Use v1.operations instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.operations

    @property
    def rules(self) -> RuleList:
        warn(
            "rules is deprecated. Use v1.rules instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.rules

    @property
    def settings(self) -> SettingList:
        warn(
            "settings is deprecated. Use v1.settings instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.settings

    @property
    def shared_keys(self) -> SharedKeyList:
        warn(
            "shared_keys is deprecated. Use v1.shared_keys instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.shared_keys

    @property
    def tests(self) -> TestList:
        warn(
            "tests is deprecated. Use v1.tests instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.tests
