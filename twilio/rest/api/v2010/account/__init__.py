r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.api.v2010.account.address import AddressList
from twilio.rest.api.v2010.account.application import ApplicationList
from twilio.rest.api.v2010.account.authorized_connect_app import (
    AuthorizedConnectAppList,
)
from twilio.rest.api.v2010.account.available_phone_number_country import (
    AvailablePhoneNumberCountryList,
)
from twilio.rest.api.v2010.account.balance import BalanceList
from twilio.rest.api.v2010.account.call import CallList
from twilio.rest.api.v2010.account.conference import ConferenceList
from twilio.rest.api.v2010.account.connect_app import ConnectAppList
from twilio.rest.api.v2010.account.incoming_phone_number import IncomingPhoneNumberList
from twilio.rest.api.v2010.account.key import KeyList
from twilio.rest.api.v2010.account.message import MessageList
from twilio.rest.api.v2010.account.new_key import NewKeyList
from twilio.rest.api.v2010.account.new_signing_key import NewSigningKeyList
from twilio.rest.api.v2010.account.notification import NotificationList
from twilio.rest.api.v2010.account.outgoing_caller_id import OutgoingCallerIdList
from twilio.rest.api.v2010.account.queue import QueueList
from twilio.rest.api.v2010.account.recording import RecordingList
from twilio.rest.api.v2010.account.short_code import ShortCodeList
from twilio.rest.api.v2010.account.signing_key import SigningKeyList
from twilio.rest.api.v2010.account.sip import SipList
from twilio.rest.api.v2010.account.token import TokenList
from twilio.rest.api.v2010.account.transcription import TranscriptionList
from twilio.rest.api.v2010.account.usage import UsageList
from twilio.rest.api.v2010.account.validation_request import ValidationRequestList


class AccountInstance(InstanceResource):
    class Status(object):
        ACTIVE = "active"
        SUSPENDED = "suspended"
        CLOSED = "closed"

    class Type(object):
        TRIAL = "Trial"
        FULL = "Full"

    """
    :ivar auth_token: The authorization token for this account. This token should be kept a secret, so no sharing.
    :ivar date_created: The date that this account was created, in GMT in RFC 2822 format
    :ivar date_updated: The date that this account was last updated, in GMT in RFC 2822 format.
    :ivar friendly_name: A human readable description of this account, up to 64 characters long. By default the FriendlyName is your email address.
    :ivar owner_account_sid: The unique 34 character id that represents the parent of this account. The OwnerAccountSid of a parent account is it's own sid.
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar status: 
    :ivar subresource_uris: A Map of various subresources available for the given Account Instance
    :ivar type: 
    :ivar uri: The URI for this resource, relative to `https://api.twilio.com`
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.auth_token: Optional[str] = payload.get("auth_token")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.owner_account_sid: Optional[str] = payload.get("owner_account_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.status: Optional["AccountInstance.Status"] = payload.get("status")
        self.subresource_uris: Optional[Dict[str, object]] = payload.get(
            "subresource_uris"
        )
        self.type: Optional["AccountInstance.Type"] = payload.get("type")
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[AccountContext] = None

    @property
    def _proxy(self) -> "AccountContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AccountContext for this AccountInstance
        """
        if self._context is None:
            self._context = AccountContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "AccountInstance":
        """
        Fetch the AccountInstance


        :returns: The fetched AccountInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AccountInstance":
        """
        Asynchronous coroutine to fetch the AccountInstance


        :returns: The fetched AccountInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
    ) -> "AccountInstance":
        """
        Update the AccountInstance

        :param friendly_name: Update the human-readable description of this Account
        :param status:

        :returns: The updated AccountInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            status=status,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
    ) -> "AccountInstance":
        """
        Asynchronous coroutine to update the AccountInstance

        :param friendly_name: Update the human-readable description of this Account
        :param status:

        :returns: The updated AccountInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            status=status,
        )

    @property
    def addresses(self) -> AddressList:
        """
        Access the addresses
        """
        return self._proxy.addresses

    @property
    def applications(self) -> ApplicationList:
        """
        Access the applications
        """
        return self._proxy.applications

    @property
    def authorized_connect_apps(self) -> AuthorizedConnectAppList:
        """
        Access the authorized_connect_apps
        """
        return self._proxy.authorized_connect_apps

    @property
    def available_phone_numbers(self) -> AvailablePhoneNumberCountryList:
        """
        Access the available_phone_numbers
        """
        return self._proxy.available_phone_numbers

    @property
    def balance(self) -> BalanceList:
        """
        Access the balance
        """
        return self._proxy.balance

    @property
    def calls(self) -> CallList:
        """
        Access the calls
        """
        return self._proxy.calls

    @property
    def conferences(self) -> ConferenceList:
        """
        Access the conferences
        """
        return self._proxy.conferences

    @property
    def connect_apps(self) -> ConnectAppList:
        """
        Access the connect_apps
        """
        return self._proxy.connect_apps

    @property
    def incoming_phone_numbers(self) -> IncomingPhoneNumberList:
        """
        Access the incoming_phone_numbers
        """
        return self._proxy.incoming_phone_numbers

    @property
    def keys(self) -> KeyList:
        """
        Access the keys
        """
        return self._proxy.keys

    @property
    def messages(self) -> MessageList:
        """
        Access the messages
        """
        return self._proxy.messages

    @property
    def new_keys(self) -> NewKeyList:
        """
        Access the new_keys
        """
        return self._proxy.new_keys

    @property
    def new_signing_keys(self) -> NewSigningKeyList:
        """
        Access the new_signing_keys
        """
        return self._proxy.new_signing_keys

    @property
    def notifications(self) -> NotificationList:
        """
        Access the notifications
        """
        return self._proxy.notifications

    @property
    def outgoing_caller_ids(self) -> OutgoingCallerIdList:
        """
        Access the outgoing_caller_ids
        """
        return self._proxy.outgoing_caller_ids

    @property
    def queues(self) -> QueueList:
        """
        Access the queues
        """
        return self._proxy.queues

    @property
    def recordings(self) -> RecordingList:
        """
        Access the recordings
        """
        return self._proxy.recordings

    @property
    def short_codes(self) -> ShortCodeList:
        """
        Access the short_codes
        """
        return self._proxy.short_codes

    @property
    def signing_keys(self) -> SigningKeyList:
        """
        Access the signing_keys
        """
        return self._proxy.signing_keys

    @property
    def sip(self) -> SipList:
        """
        Access the sip
        """
        return self._proxy.sip

    @property
    def tokens(self) -> TokenList:
        """
        Access the tokens
        """
        return self._proxy.tokens

    @property
    def transcriptions(self) -> TranscriptionList:
        """
        Access the transcriptions
        """
        return self._proxy.transcriptions

    @property
    def usage(self) -> UsageList:
        """
        Access the usage
        """
        return self._proxy.usage

    @property
    def validation_requests(self) -> ValidationRequestList:
        """
        Access the validation_requests
        """
        return self._proxy.validation_requests

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AccountInstance {}>".format(context)


class AccountContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the AccountContext

        :param version: Version that contains the resource
        :param sid: The Account Sid that uniquely identifies the account to update
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Accounts/{sid}.json".format(**self._solution)

        self._addresses: Optional[AddressList] = None
        self._applications: Optional[ApplicationList] = None
        self._authorized_connect_apps: Optional[AuthorizedConnectAppList] = None
        self._available_phone_numbers: Optional[AvailablePhoneNumberCountryList] = None
        self._balance: Optional[BalanceList] = None
        self._calls: Optional[CallList] = None
        self._conferences: Optional[ConferenceList] = None
        self._connect_apps: Optional[ConnectAppList] = None
        self._incoming_phone_numbers: Optional[IncomingPhoneNumberList] = None
        self._keys: Optional[KeyList] = None
        self._messages: Optional[MessageList] = None
        self._new_keys: Optional[NewKeyList] = None
        self._new_signing_keys: Optional[NewSigningKeyList] = None
        self._notifications: Optional[NotificationList] = None
        self._outgoing_caller_ids: Optional[OutgoingCallerIdList] = None
        self._queues: Optional[QueueList] = None
        self._recordings: Optional[RecordingList] = None
        self._short_codes: Optional[ShortCodeList] = None
        self._signing_keys: Optional[SigningKeyList] = None
        self._sip: Optional[SipList] = None
        self._tokens: Optional[TokenList] = None
        self._transcriptions: Optional[TranscriptionList] = None
        self._usage: Optional[UsageList] = None
        self._validation_requests: Optional[ValidationRequestList] = None

    def fetch(self) -> AccountInstance:
        """
        Fetch the AccountInstance


        :returns: The fetched AccountInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AccountInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AccountInstance:
        """
        Asynchronous coroutine to fetch the AccountInstance


        :returns: The fetched AccountInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AccountInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
    ) -> AccountInstance:
        """
        Update the AccountInstance

        :param friendly_name: Update the human-readable description of this Account
        :param status:

        :returns: The updated AccountInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Status": status,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
    ) -> AccountInstance:
        """
        Asynchronous coroutine to update the AccountInstance

        :param friendly_name: Update the human-readable description of this Account
        :param status:

        :returns: The updated AccountInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Status": status,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def addresses(self) -> AddressList:
        """
        Access the addresses
        """
        if self._addresses is None:
            self._addresses = AddressList(
                self._version,
                self._solution["sid"],
            )
        return self._addresses

    @property
    def applications(self) -> ApplicationList:
        """
        Access the applications
        """
        if self._applications is None:
            self._applications = ApplicationList(
                self._version,
                self._solution["sid"],
            )
        return self._applications

    @property
    def authorized_connect_apps(self) -> AuthorizedConnectAppList:
        """
        Access the authorized_connect_apps
        """
        if self._authorized_connect_apps is None:
            self._authorized_connect_apps = AuthorizedConnectAppList(
                self._version,
                self._solution["sid"],
            )
        return self._authorized_connect_apps

    @property
    def available_phone_numbers(self) -> AvailablePhoneNumberCountryList:
        """
        Access the available_phone_numbers
        """
        if self._available_phone_numbers is None:
            self._available_phone_numbers = AvailablePhoneNumberCountryList(
                self._version,
                self._solution["sid"],
            )
        return self._available_phone_numbers

    @property
    def balance(self) -> BalanceList:
        """
        Access the balance
        """
        if self._balance is None:
            self._balance = BalanceList(
                self._version,
                self._solution["sid"],
            )
        return self._balance

    @property
    def calls(self) -> CallList:
        """
        Access the calls
        """
        if self._calls is None:
            self._calls = CallList(
                self._version,
                self._solution["sid"],
            )
        return self._calls

    @property
    def conferences(self) -> ConferenceList:
        """
        Access the conferences
        """
        if self._conferences is None:
            self._conferences = ConferenceList(
                self._version,
                self._solution["sid"],
            )
        return self._conferences

    @property
    def connect_apps(self) -> ConnectAppList:
        """
        Access the connect_apps
        """
        if self._connect_apps is None:
            self._connect_apps = ConnectAppList(
                self._version,
                self._solution["sid"],
            )
        return self._connect_apps

    @property
    def incoming_phone_numbers(self) -> IncomingPhoneNumberList:
        """
        Access the incoming_phone_numbers
        """
        if self._incoming_phone_numbers is None:
            self._incoming_phone_numbers = IncomingPhoneNumberList(
                self._version,
                self._solution["sid"],
            )
        return self._incoming_phone_numbers

    @property
    def keys(self) -> KeyList:
        """
        Access the keys
        """
        if self._keys is None:
            self._keys = KeyList(
                self._version,
                self._solution["sid"],
            )
        return self._keys

    @property
    def messages(self) -> MessageList:
        """
        Access the messages
        """
        if self._messages is None:
            self._messages = MessageList(
                self._version,
                self._solution["sid"],
            )
        return self._messages

    @property
    def new_keys(self) -> NewKeyList:
        """
        Access the new_keys
        """
        if self._new_keys is None:
            self._new_keys = NewKeyList(
                self._version,
                self._solution["sid"],
            )
        return self._new_keys

    @property
    def new_signing_keys(self) -> NewSigningKeyList:
        """
        Access the new_signing_keys
        """
        if self._new_signing_keys is None:
            self._new_signing_keys = NewSigningKeyList(
                self._version,
                self._solution["sid"],
            )
        return self._new_signing_keys

    @property
    def notifications(self) -> NotificationList:
        """
        Access the notifications
        """
        if self._notifications is None:
            self._notifications = NotificationList(
                self._version,
                self._solution["sid"],
            )
        return self._notifications

    @property
    def outgoing_caller_ids(self) -> OutgoingCallerIdList:
        """
        Access the outgoing_caller_ids
        """
        if self._outgoing_caller_ids is None:
            self._outgoing_caller_ids = OutgoingCallerIdList(
                self._version,
                self._solution["sid"],
            )
        return self._outgoing_caller_ids

    @property
    def queues(self) -> QueueList:
        """
        Access the queues
        """
        if self._queues is None:
            self._queues = QueueList(
                self._version,
                self._solution["sid"],
            )
        return self._queues

    @property
    def recordings(self) -> RecordingList:
        """
        Access the recordings
        """
        if self._recordings is None:
            self._recordings = RecordingList(
                self._version,
                self._solution["sid"],
            )
        return self._recordings

    @property
    def short_codes(self) -> ShortCodeList:
        """
        Access the short_codes
        """
        if self._short_codes is None:
            self._short_codes = ShortCodeList(
                self._version,
                self._solution["sid"],
            )
        return self._short_codes

    @property
    def signing_keys(self) -> SigningKeyList:
        """
        Access the signing_keys
        """
        if self._signing_keys is None:
            self._signing_keys = SigningKeyList(
                self._version,
                self._solution["sid"],
            )
        return self._signing_keys

    @property
    def sip(self) -> SipList:
        """
        Access the sip
        """
        if self._sip is None:
            self._sip = SipList(
                self._version,
                self._solution["sid"],
            )
        return self._sip

    @property
    def tokens(self) -> TokenList:
        """
        Access the tokens
        """
        if self._tokens is None:
            self._tokens = TokenList(
                self._version,
                self._solution["sid"],
            )
        return self._tokens

    @property
    def transcriptions(self) -> TranscriptionList:
        """
        Access the transcriptions
        """
        if self._transcriptions is None:
            self._transcriptions = TranscriptionList(
                self._version,
                self._solution["sid"],
            )
        return self._transcriptions

    @property
    def usage(self) -> UsageList:
        """
        Access the usage
        """
        if self._usage is None:
            self._usage = UsageList(
                self._version,
                self._solution["sid"],
            )
        return self._usage

    @property
    def validation_requests(self) -> ValidationRequestList:
        """
        Access the validation_requests
        """
        if self._validation_requests is None:
            self._validation_requests = ValidationRequestList(
                self._version,
                self._solution["sid"],
            )
        return self._validation_requests

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AccountContext {}>".format(context)


class AccountPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AccountInstance:
        """
        Build an instance of AccountInstance

        :param payload: Payload response from the API
        """
        return AccountInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AccountPage>"


class AccountList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the AccountList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Accounts.json"

    def create(
        self, friendly_name: Union[str, object] = values.unset
    ) -> AccountInstance:
        """
        Create the AccountInstance

        :param friendly_name: A human readable description of the account to create, defaults to `SubAccount Created at {YYYY-MM-DD HH:MM meridian}`

        :returns: The created AccountInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountInstance(self._version, payload)

    async def create_async(
        self, friendly_name: Union[str, object] = values.unset
    ) -> AccountInstance:
        """
        Asynchronously create the AccountInstance

        :param friendly_name: A human readable description of the account to create, defaults to `SubAccount Created at {YYYY-MM-DD HH:MM meridian}`

        :returns: The created AccountInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AccountInstance(self._version, payload)

    def stream(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AccountInstance]:
        """
        Streams AccountInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str friendly_name: Only return the Account resources with friendly names that exactly match this name.
        :param &quot;AccountInstance.Status&quot; status: Only return Account resources with the given status. Can be `closed`, `suspended` or `active`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name, status=status, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AccountInstance]:
        """
        Asynchronously streams AccountInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str friendly_name: Only return the Account resources with friendly names that exactly match this name.
        :param &quot;AccountInstance.Status&quot; status: Only return Account resources with the given status. Can be `closed`, `suspended` or `active`.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            friendly_name=friendly_name, status=status, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AccountInstance]:
        """
        Lists AccountInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str friendly_name: Only return the Account resources with friendly names that exactly match this name.
        :param &quot;AccountInstance.Status&quot; status: Only return Account resources with the given status. Can be `closed`, `suspended` or `active`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            self.stream(
                friendly_name=friendly_name,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AccountInstance]:
        """
        Asynchronously lists AccountInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str friendly_name: Only return the Account resources with friendly names that exactly match this name.
        :param &quot;AccountInstance.Status&quot; status: Only return Account resources with the given status. Can be `closed`, `suspended` or `active`.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                friendly_name=friendly_name,
                status=status,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AccountPage:
        """
        Retrieve a single page of AccountInstance records from the API.
        Request is executed immediately

        :param friendly_name: Only return the Account resources with friendly names that exactly match this name.
        :param status: Only return Account resources with the given status. Can be `closed`, `suspended` or `active`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AccountInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AccountPage(self._version, response)

    async def page_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        status: Union["AccountInstance.Status", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AccountPage:
        """
        Asynchronously retrieve a single page of AccountInstance records from the API.
        Request is executed immediately

        :param friendly_name: Only return the Account resources with friendly names that exactly match this name.
        :param status: Only return Account resources with the given status. Can be `closed`, `suspended` or `active`.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AccountInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "Status": status,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AccountPage(self._version, response)

    def get_page(self, target_url: str) -> AccountPage:
        """
        Retrieve a specific page of AccountInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AccountInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AccountPage(self._version, response)

    async def get_page_async(self, target_url: str) -> AccountPage:
        """
        Asynchronously retrieve a specific page of AccountInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AccountInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AccountPage(self._version, response)

    def get(self, sid: str) -> AccountContext:
        """
        Constructs a AccountContext

        :param sid: The Account Sid that uniquely identifies the account to update
        """
        return AccountContext(self._version, sid=sid)

    def __call__(self, sid: str) -> AccountContext:
        """
        Constructs a AccountContext

        :param sid: The Account Sid that uniquely identifies the account to update
        """
        return AccountContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AccountList>"
