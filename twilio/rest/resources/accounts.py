from . import InstanceResource, ListResource
from twilio.rest.resources.applications import Applications
from twilio.rest.resources.caller_ids import CallerIds
from twilio.rest.resources.calls import Calls
from twilio.rest.resources.conferences import Conferences
from twilio.rest.resources.connect_apps import ConnectApps, AuthorizedConnectApps
from twilio.rest.resources.messages import Messages
from twilio.rest.resources.notifications import Notifications
from twilio.rest.resources.phone_numbers import PhoneNumbers
from twilio.rest.resources.queues import Queues
from twilio.rest.resources.recordings import Recordings
from twilio.rest.resources.sip import Sip
from twilio.rest.resources.sms_messages import Sms
from twilio.rest.v2010.account.usage.usage_record import UsageRecords
from twilio.rest.v2010.account.usage.usage_trigger import UsageTriggers

from twilio.rest.v2010.account import (
    Account as BaseAccount,
    Accounts as BaseAccounts,
)


class Account(BaseAccount):
    override_subresources = [
        Applications,
        Notifications,
        Recordings,
        Calls,
        Sms,
        CallerIds,
        PhoneNumbers,
        Conferences,
        ConnectApps,
        Queues,
        AuthorizedConnectApps,
        UsageRecords,
        UsageTriggers,
        Messages,
        Sip,
    ]

    def load_subresources(self):
        """
        Override existing subresources with backwards compatible versions
        """
        super(Account, self).load_subresources()

        for resource in self.override_subresources:
            list_resource = resource(
                self.uri,
                self.parent.auth,
                self.parent.timeout
            )
            self.__dict__[list_resource.key] = list_resource

    def close(self):
        """
        Permenently deactivate this account
        """
        return self.update_instance(status=Account.CLOSED)

    def suspend(self):
        """
        Temporarily suspend this account
        """
        return self.update_instance(status=Account.SUSPENDED)

    def activate(self):
        """
        Reactivate this account
        """
        return self.update_instance(status=Account.ACTIVE)


class Accounts(BaseAccounts):
    instance = Account

    def close(self, sid):
        """
        Permenently deactivate an account, Alias to update
        """
        return self.update(sid, status=Account.CLOSED)

    def suspend(self, sid):
        """
        Temporarily suspend an account, Alias to update
        """
        return self.update(sid, status=Account.SUSPENDED)

    def activate(self, sid):
        """
        Reactivate an account, Alias to update
        """
        return self.update(sid, status=Account.ACTIVE)
