from twilio.rest.api import ApiBase
from warnings import warn


class Api(ApiBase):

    @property
    def account(self):
        warn('account is deprecated. Use v2010.account instead.', DeprecationWarning, stacklevel=2)
        return self.v2010.account

    def accounts(self):
        warn('accounts is deprecated. Use v2010.accounts instead.', DeprecationWarning, stacklevel=2)
        return self.v2010.accounts

    @property
    def addresses(self):
        warn('addresses is deprecated. Use v2010.addresses instead.', DeprecationWarning, stacklevel=2)
        return self.account.addresses

    @property
    def applications(self):
        warn('applications is deprecated. Use v2010.applications instead.', DeprecationWarning, stacklevel=2)
        return self.account.applications

    @property
    def authorized_connect_apps(self):
        warn('authorized_connect_apps is deprecated. Use v2010.authorized_connect_apps instead.', DeprecationWarning, stacklevel=2)
        return self.account.authorized_connect_apps

    @property
    def available_phone_numbers(self):
        warn('available_phone_numbers is deprecated. Use v2010.available_phone_numbers instead.', DeprecationWarning, stacklevel=2)
        return self.account.available_phone_numbers

    @property
    def balance(self):
        warn('balance is deprecated. Use v2010.balance instead.', DeprecationWarning, stacklevel=2)
        return self.account.balance

    @property
    def calls(self):
        warn('calls is deprecated. Use v2010.calls instead.', DeprecationWarning, stacklevel=2)
        return self.account.calls

    @property
    def conferences(self):
        warn('conferences is deprecated. Use v2010.conferences instead.', DeprecationWarning, stacklevel=2)
        return self.account.conferences

    @property
    def connect_apps(self):
        warn('connect_apps is deprecated. Use v2010.connect_apps instead.', DeprecationWarning, stacklevel=2)
        return self.account.connect_apps

    @property
    def incoming_phone_numbers(self):
        warn('incoming_phone_numbers is deprecated. Use incoming_phone_numbers.calls instead.', DeprecationWarning, stacklevel=2)
        return self.account.incoming_phone_numbers

    @property
    def keys(self):
        warn('keys is deprecated. Use v2010.keys instead.', DeprecationWarning, stacklevel=2)
        return self.account.keys

    @property
    def messages(self):
        warn('messages is deprecated. Use v2010.messages instead.', DeprecationWarning, stacklevel=2)
        return self.account.messages

    @property
    def new_keys(self):
        warn('new_keys is deprecated. Use new_keys.calls instead.', DeprecationWarning, stacklevel=2)
        return self.account.new_keys

    @property
    def new_signing_keys(self):
        warn('new_signing_keys is deprecated. Use v2010.new_signing_keys instead.', DeprecationWarning, stacklevel=2)
        return self.account.new_signing_keys

    @property
    def notifications(self):
        warn('notifications is deprecated. Use v2010.notifications instead.', DeprecationWarning, stacklevel=2)
        return self.account.notifications

    @property
    def outgoing_caller_ids(self):
        warn('outgoing_caller_ids is deprecated. Use v2010.outgoing_caller_ids instead.', DeprecationWarning, stacklevel=2)
        return self.account.outgoing_caller_ids

    @property
    def queues(self):
        warn('queues is deprecated. Use v2010.queues instead.', DeprecationWarning, stacklevel=2)
        return self.account.queues

    @property
    def recordings(self):
        warn('recordings is deprecated. Use v2010.recordings instead.', DeprecationWarning, stacklevel=2)
        return self.account.recordings

    @property
    def signing_keys(self):
        warn('signing_keys is deprecated. Use v2010.signing_keys instead.', DeprecationWarning, stacklevel=2)
        return self.account.signing_keys

    @property
    def sip(self):
        warn('sip is deprecated. Use v2010.sip instead.', DeprecationWarning, stacklevel=2)
        return self.account.sip

    @property
    def short_codes(self):
        warn('short_codes is deprecated. Use v2010.short_codes instead.', DeprecationWarning, stacklevel=2)
        return self.account.short_codes

    @property
    def tokens(self):
        warn('tokens is deprecated. Use v2010.tokens instead.', DeprecationWarning, stacklevel=2)
        return self.account.tokens

    @property
    def transcriptions(self):
        warn('transcriptions is deprecated. Use v2010.transcriptions instead.', DeprecationWarning, stacklevel=2)
        return self.account.transcriptions

    @property
    def usage(self):
        warn('usage is deprecated. Use v2010.usage instead.', DeprecationWarning, stacklevel=2)
        return self.account.usage

    @property
    def validation_requests(self):
        warn('validation_requests is deprecated. Use v2010.validation_requests instead.', DeprecationWarning, stacklevel=2)
        return self.account.validation_requests

