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


class TranscriptionInstance(InstanceResource):
    class Status(object):
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        FAILED = "failed"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource.
    :ivar api_version: The API version used to create the transcription.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar duration: The duration of the transcribed audio in seconds.
    :ivar price: The charge for the transcript in the currency associated with the account. This value is populated after the transcript is complete so it may not be available immediately.
    :ivar price_unit: The currency in which `price` is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. `usd`, `eur`, `jpy`).
    :ivar recording_sid: The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) from which the transcription was created.
    :ivar sid: The unique string that that we created to identify the Transcription resource.
    :ivar status: 
    :ivar transcription_text: The text content of the transcription.
    :ivar type: The transcription type. Can only be: `fast`.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.api_version: Optional[str] = payload.get("api_version")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.duration: Optional[str] = payload.get("duration")
        self.price: Optional[float] = deserialize.decimal(payload.get("price"))
        self.price_unit: Optional[str] = payload.get("price_unit")
        self.recording_sid: Optional[str] = payload.get("recording_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.status: Optional["TranscriptionInstance.Status"] = payload.get("status")
        self.transcription_text: Optional[str] = payload.get("transcription_text")
        self.type: Optional[str] = payload.get("type")
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[TranscriptionContext] = None

    @property
    def _proxy(self) -> "TranscriptionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TranscriptionContext for this TranscriptionInstance
        """
        if self._context is None:
            self._context = TranscriptionContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the TranscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the TranscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "TranscriptionInstance":
        """
        Fetch the TranscriptionInstance


        :returns: The fetched TranscriptionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "TranscriptionInstance":
        """
        Asynchronous coroutine to fetch the TranscriptionInstance


        :returns: The fetched TranscriptionInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.TranscriptionInstance {}>".format(context)


class TranscriptionContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the TranscriptionContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/Transcriptions/{sid}.json".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the TranscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the TranscriptionInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> TranscriptionInstance:
        """
        Fetch the TranscriptionInstance


        :returns: The fetched TranscriptionInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TranscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> TranscriptionInstance:
        """
        Asynchronous coroutine to fetch the TranscriptionInstance


        :returns: The fetched TranscriptionInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TranscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.TranscriptionContext {}>".format(context)


class TranscriptionPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> TranscriptionInstance:
        """
        Build an instance of TranscriptionInstance

        :param payload: Payload response from the API
        """
        return TranscriptionInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.TranscriptionPage>"


class TranscriptionList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the TranscriptionList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Transcriptions.json".format(
            **self._solution
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[TranscriptionInstance]:
        """
        Streams TranscriptionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[TranscriptionInstance]:
        """
        Asynchronously streams TranscriptionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[TranscriptionInstance]:
        """
        Lists TranscriptionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[TranscriptionInstance]:
        """
        Asynchronously lists TranscriptionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

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
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> TranscriptionPage:
        """
        Retrieve a single page of TranscriptionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of TranscriptionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TranscriptionPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = None,
        page_number: Union[int, object] = None,
        page_size: Union[int, object] = None,
    ) -> TranscriptionPage:
        """
        Asynchronously retrieve a single page of TranscriptionInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of TranscriptionInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return TranscriptionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> TranscriptionPage:
        """
        Retrieve a specific page of TranscriptionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of TranscriptionInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TranscriptionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> TranscriptionPage:
        """
        Asynchronously retrieve a specific page of TranscriptionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of TranscriptionInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return TranscriptionPage(self._version, response, self._solution)

    def get(self, sid: str) -> TranscriptionContext:
        """
        Constructs a TranscriptionContext

        :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to fetch.
        """
        return TranscriptionContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid: str) -> TranscriptionContext:
        """
        Constructs a TranscriptionContext

        :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to fetch.
        """
        return TranscriptionContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.TranscriptionList>"
