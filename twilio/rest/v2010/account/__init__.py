# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

from twilio.rest.resources.util import (
    parse_date,
    parse_iso_date,
)
from twilio.rest.resources.base import InstanceResource
from twilio.rest.v2010.account.address import (
    Address,
    Addresses,
)
from twilio.rest.v2010.account.application import (
    Application,
    Applications,
)
from twilio.rest.v2010.account.authorized_connect_app import (
    AuthorizedConnectApp,
    AuthorizedConnectApps,
)
from twilio.rest.v2010.account.available_phone_number import (
    AvailablePhoneNumberCountry,
    AvailablePhoneNumberCountries,
)
from twilio.rest.v2010.account.call import (
    Call,
    Calls,
)
from twilio.rest.v2010.account.conference import (
    Conference,
    Conferences,
)
from twilio.rest.v2010.account.connect_app import (
    ConnectApp,
    ConnectApps,
)
from twilio.rest.v2010.account.incoming_phone_number import (
    IncomingPhoneNumber,
    IncomingPhoneNumbers,
)
from twilio.rest.v2010.account.message import (
    Message,
    Messages,
)
from twilio.rest.v2010.account.notification import (
    Notification,
    Notifications,
)
from twilio.rest.v2010.account.outgoing_caller_id import (
    OutgoingCallerId,
    OutgoingCallerIds,
)
from twilio.rest.v2010.account.queue import (
    Queue,
    Queues,
)
from twilio.rest.v2010.account.recording import (
    Recording,
    Recordings,
)
from twilio.rest.v2010.account.sandbox import (
    Sandbox,
    Sandboxes,
)
from twilio.rest.v2010.account.sip import Sip
from twilio.rest.v2010.account.sms import Sms
from twilio.rest.v2010.account.token import (
    Token,
    Tokens,
)
from twilio.rest.v2010.account.transcription import (
    Transcription,
    Transcriptions,
)
from twilio.rest.v2010.account.usage import Usage
from twilio.rest.resources.base import ListResource


class Account(InstanceResource):
    """
    .. attribute:: auth_token
    
        The authorization token for this account. This token should be kept
        secret.
    
    .. attribute:: date_created
    
        The date this account was created in GMT RFC 2822 format
    
    .. attribute:: date_updated
    
        The date this account was last updated in GTM RFC 2822 format
    
    .. attribute:: friendly_name
    
        A human readable description of this account, up to 64 characters. It
        defaults to this accounts email address
    
    .. attribute:: owner_account_sid
    
        The unique 34 character id that represents the parent of this account.
        The OwnerAccountSid of a parent account is it's own sid.
    
    .. attribute:: sid
    
        A 34 character string that uniquely identifies this resource.
    
    .. attribute:: status
    
        The status of this account. Usually `active` but can be `suspended` or
        `closed`
    
    .. attribute:: subresource_uris
    
        A Map of various subresources available for the given Account Instance
    
    .. attribute:: type
    
        The type of this account. Either `Trial` or `Full` if it's been upgraded
    
    .. attribute:: uri
    
        The URI for this resource, relative to `https://api.twilio.com`
    """
    id_key = "sid"
    FULL = "Full"
    TRIAL = "Trial"
    ACTIVE = "active"
    CLOSED = "closed"
    SUSPENDED = "suspended"
    subresources = [
        Addresses,
        Applications,
        AuthorizedConnectApps,
        AvailablePhoneNumberCountries,
        Calls,
        Conferences,
        ConnectApps,
        IncomingPhoneNumbers,
        Messages,
        Notifications,
        OutgoingCallerIds,
        Queues,
        Recordings,
        Sandboxes,
        Sip,
        Sms,
        Tokens,
        Transcriptions,
        Usage
    ]

    def load(self, *args, **kwargs):
        super(Account, self).load(*args, **kwargs)
        
        if hasattr(self, "date_created") and self.date_created:
            self.date_created = parse_iso_date(self.date_created)
        
        if hasattr(self, "date_updated") and self.date_updated:
            self.date_updated = parse_iso_date(self.date_updated)

    def update(self, **kwargs):
        """
        Modify the properties of a given Account
        
        :param account.status status: Alter the status of this account with a given
            Status
        :param str friendly_name: Update the human-readable description of this Account
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns a new instance of the updated :class:`Account`
        """
        return self.update_instance(kwargs)


class Accounts(ListResource):
    name = "Accounts"
    mount_name = "accounts"
    key = "accounts"
    instance = Account

    def __init__(self, *args, **kwargs):
        super(Accounts, self).__init__(*args, **kwargs)

    def create(self, **kwargs):
        """
        Create a new Twilio Subaccount from the account making the request
        
        :param str friendly_name: A human readable description of the account to create,
            defaults to `SubAccount Created at {YYYY-MM-DD HH:MM meridian}`
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`CreateQuery`
        :returns: A CreateQuery when executed returns an instance of the created :class:`Account`
        """
        return self.create_instance(kwargs)

    def get(self, sid):
        """
        Fetch the account specified by the provided Account Sid
        
        :param str sid: The Account Sid that uniquely identifies the account to fetch
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`Account`
        :returns: A placeholder for a :class:`Account` resource
        """
        return self.get_instance(sid)

    def list(self, **kwargs):
        """
        Retrieves a collection of Accounts belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`ListQuery`
        :returns: A ListQuery when executed returns a list of :class:`Account`
        """
        return self.get_instances(kwargs)

    def update(self, sid, **kwargs):
        """
        Modify the properties of a given Account
        
        :param account.status status: Alter the status of this account with a given
            Status
        :param str friendly_name: Update the human-readable description of this Account
        :param str sid: The sid
        
        :raises TwilioRestException: when the request fails on execute
        
        :rtype: :class:`UpdateQuery`
        :returns: An UpdateQuery when executed returns an instance of the updated :class:`Account`
        """
        return self.update_instance(sid, kwargs)

    def iter(self, **kwargs):
        """
        Retrieves a collection of Accounts belonging to the account used to make the request
        
        :raises TwilioRestException: when the request fails on execute
        
        :returns: An iterator to fetch all :class:`Account`
        """
        return super(Accounts, self).iter(**kwargs)
