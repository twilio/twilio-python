from warnings import warn

from twilio.rest.preview.PreviewBase import PreviewBase
from twilio.rest.preview.hosted_numbers.authorization_document import (
    AuthorizationDocumentList,
)
from twilio.rest.preview.hosted_numbers.hosted_number_order import HostedNumberOrderList
from twilio.rest.preview.marketplace.available_add_on import AvailableAddOnList
from twilio.rest.preview.marketplace.installed_add_on import InstalledAddOnList
from twilio.rest.preview.wireless.command import CommandList
from twilio.rest.preview.wireless.rate_plan import RatePlanList
from twilio.rest.preview.wireless.sim import SimList


class Preview(PreviewBase):

    @property
    def authorization_documents(self) -> AuthorizationDocumentList:
        warn(
            "authorization_documents is deprecated. Use hosted_numbers.authorization_documents instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.hosted_numbers.authorization_documents

    @property
    def hosted_number_orders(self) -> HostedNumberOrderList:
        warn(
            "hosted_number_orders is deprecated. Use hosted_numbers.hosted_number_orders instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.hosted_numbers.hosted_number_orders

    @property
    def available_add_ons(self) -> AvailableAddOnList:
        warn(
            "available_add_ons is deprecated. Use marketplace.available_add_ons instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.marketplace.available_add_ons

    @property
    def installed_add_ons(self) -> InstalledAddOnList:
        warn(
            "installed_add_ons is deprecated. Use marketplace.installed_add_ons instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.marketplace.installed_add_ons

    @property
    def commands(self) -> CommandList:
        warn(
            "commands is deprecated. Use wireless.commands instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.wireless.commands

    @property
    def rate_plans(self) -> RatePlanList:
        warn(
            "rate_plans is deprecated. Use wireless.rate_plans instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.wireless.rate_plans

    @property
    def sims(self) -> SimList:
        warn(
            "sims is deprecated. Use wireless.sims instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.wireless.sims
