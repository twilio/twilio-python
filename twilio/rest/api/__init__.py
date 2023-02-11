from twilio.rest.api import ApiBase
from warnings import warn


class Api(ApiBase):

    @property
    def account(self):
        return self.v2010.account

    def accounts(self):
        return self.v2010.accounts

    @property
    def addresses(self):
        warn('addresses is deprecated. Use account.addresses instead.', DeprecationWarning, stacklevel=2)
        return self.account.addresses

    @property
    def applications(self):
        warn('applications is deprecated. Use account.applications instead.', DeprecationWarning, stacklevel=2)
        return self.account.applications

    @property
    def authorized_connect_apps(self):
        warn('authorized_connect_apps is deprecated. Use account.authorized_connect_apps instead.', DeprecationWarning, stacklevel=2)
        return self.account.authorized_connect_apps

    @property
    def available_phone_numbers(self):
        warn('available_phone_numbers is deprecated. Use account.available_phone_numbers instead.', DeprecationWarning, stacklevel=2)
        return self.account.available_phone_numbers

    @property
    def balance(self):
        warn('balance is deprecated. Use account.balance instead.', DeprecationWarning, stacklevel=2)
        return self.account.balance

    @property
    def calls(self):
        warn('calls is deprecated. Use account.calls instead.', DeprecationWarning, stacklevel=2)
        return self.account.calls

    @property
    def conferences(self):
        warn('conferences is deprecated. Use account.conferences instead.', DeprecationWarning, stacklevel=2)
        return self.account.conferences

    @property
    def connect_apps(self):
        warn('connect_apps is deprecated. Use account.connect_apps instead.', DeprecationWarning, stacklevel=2)
        return self.account.connect_apps

    @property
    def incoming_phone_numbers(self):
        warn('incoming_phone_numbers is deprecated. Use account.incoming_phone_numbers instead.', DeprecationWarning, stacklevel=2)
        return self.account.incoming_phone_numbers

    @property
    def keys(self):
        warn('keys is deprecated. Use account.keys instead.', DeprecationWarning, stacklevel=2)
        return self.account.keys

    @property
    def messages(self):
        warn('messages is deprecated. Use account.messages instead.', DeprecationWarning, stacklevel=2)
        return self.account.messages

    @property
    def new_keys(self):
        warn('new_keys is deprecated. Use account.new_keys instead.', DeprecationWarning, stacklevel=2)
        return self.account.new_keys

    @property
    def new_signing_keys(self):
        warn('new_signing_keys is deprecated. Use account.new_signing_keys instead.', DeprecationWarning, stacklevel=2)
        return self.account.new_signing_keys

    @property
    def notifications(self):
        warn('notifications is deprecated. Use account.notifications instead.', DeprecationWarning, stacklevel=2)
        return self.account.notifications

    @property
    def outgoing_caller_ids(self):
        warn('outgoing_caller_ids is deprecated. Use account.outgoing_caller_ids instead.', DeprecationWarning, stacklevel=2)
        return self.account.outgoing_caller_ids

    @property
    def queues(self):
        warn('queues is deprecated. Use account.queues instead.', DeprecationWarning, stacklevel=2)
        return self.account.queues

    @property
    def recordings(self):
        warn('recordings is deprecated. Use account.recordings instead.', DeprecationWarning, stacklevel=2)
        return self.account.recordings

    @property
    def signing_keys(self):
        warn('signing_keys is deprecated. Use account.signing_keys instead.', DeprecationWarning, stacklevel=2)
        return self.account.signing_keys

    @property
    def sip(self):
        warn('sip is deprecated. Use account.sip instead.', DeprecationWarning, stacklevel=2)
        return self.account.sip

    @property
    def short_codes(self):
        warn('short_codes is deprecated. Use account.short_codes instead.', DeprecationWarning, stacklevel=2)
        return self.account.short_codes

    @property
    def tokens(self):
        warn('tokens is deprecated. Use account.tokens instead.', DeprecationWarning, stacklevel=2)
        return self.account.tokens

    @property
    def transcriptions(self):
        warn('transcriptions is deprecated. Use account.transcriptions instead.', DeprecationWarning, stacklevel=2)
        return self.account.transcriptions

    @property
    def usage(self):
        warn('usage is deprecated. Use account.usage instead.', DeprecationWarning, stacklevel=2)
        return self.account.usage

    @property
    def validation_requests(self):
        warn('validation_requests is deprecated. Use account.validation_requests instead.', DeprecationWarning, stacklevel=2)
        return self.account.validation_requests

