from . import InstanceResource, ListResource
from twilio.rest.resources.caller_ids import CallerIds
from twilio.rest.resources.conferences import Conferences
from twilio.rest.resources.connect_apps import ConnectApps, AuthorizedConnectApps
from twilio.rest.resources.media import MediaList
from twilio.rest.resources.messages import Messages
from twilio.rest.resources.phone_numbers import PhoneNumbers
from twilio.rest.resources.queues import Queues
from twilio.rest.resources.sip import Sip
from twilio.rest.resources.usage_records import UsageRecords
from twilio.rest.resources.usage_triggers import UsageTriggers
from twilio.rest.resources.v2010.account.application import Applications
from twilio.rest.resources.v2010.account.call import Calls
from twilio.rest.resources.v2010.account.notification import Notifications
from twilio.rest.resources.v2010.account.recording import Recordings
from twilio.rest.resources.v2010.account.sms import Sms
from twilio.rest.resources.v2010.account.transcription import Transcriptions

from v2010.account import (
    Account as BaseAccount,
    Accounts as BaseAccounts,
)


class Account(BaseAccount):
    subresources = [
        Applications,
        Notifications,
        Transcriptions,
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
        MediaList,
        Messages,
        Sip,
    ]

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
