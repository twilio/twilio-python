r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Intelligence
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class OperatorResultInstance(InstanceResource):

    class OperatorType(object):
        CONVERSATION_CLASSIFY = "conversation_classify"
        UTTERANCE_CLASSIFY = "utterance_classify"
        EXTRACT = "extract"
        EXTRACT_NORMALIZE = "extract_normalize"
        PII_EXTRACT = "pii_extract"
        TEXT_GENERATION = "text_generation"
        JSON = "json"

    """
    :ivar operator_type: 
    :ivar name: The name of the applied Language Understanding.
    :ivar operator_sid: A 34 character string that identifies this Language Understanding operator sid.
    :ivar extract_match: Boolean to tell if extract Language Understanding Processing model matches results.
    :ivar match_probability: Percentage of 'matching' class needed to consider a sentence matches
    :ivar normalized_result: Normalized output of extraction stage which matches Label.
    :ivar utterance_results: List of mapped utterance object which matches sentences.
    :ivar utterance_match: Boolean to tell if Utterance matches results.
    :ivar predicted_label: The 'matching' class. This might be available on conversation classify model outputs.
    :ivar predicted_probability: Percentage of 'matching' class needed to consider a sentence matches.
    :ivar label_probabilities: The labels probabilities. This might be available on conversation classify model outputs.
    :ivar extract_results: List of text extraction results. This might be available on classify-extract model outputs.
    :ivar text_generation_results: Output of a text generation operator for example Conversation Sumamary.
    :ivar json_results: 
    :ivar transcript_sid: A 34 character string that uniquely identifies this Transcript.
    :ivar url: The URL of this resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        transcript_sid: str,
        operator_sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.operator_type: Optional["OperatorResultInstance.OperatorType"] = (
            payload.get("operator_type")
        )
        self.name: Optional[str] = payload.get("name")
        self.operator_sid: Optional[str] = payload.get("operator_sid")
        self.extract_match: Optional[bool] = payload.get("extract_match")
        self.match_probability: Optional[float] = deserialize.decimal(
            payload.get("match_probability")
        )
        self.normalized_result: Optional[str] = payload.get("normalized_result")
        self.utterance_results: Optional[List[Dict[str, object]]] = payload.get(
            "utterance_results"
        )
        self.utterance_match: Optional[bool] = payload.get("utterance_match")
        self.predicted_label: Optional[str] = payload.get("predicted_label")
        self.predicted_probability: Optional[float] = deserialize.decimal(
            payload.get("predicted_probability")
        )
        self.label_probabilities: Optional[Dict[str, object]] = payload.get(
            "label_probabilities"
        )
        self.extract_results: Optional[Dict[str, object]] = payload.get(
            "extract_results"
        )
        self.text_generation_results: Optional[Dict[str, object]] = payload.get(
            "text_generation_results"
        )
        self.json_results: Optional[Dict[str, object]] = payload.get("json_results")
        self.transcript_sid: Optional[str] = payload.get("transcript_sid")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "transcript_sid": transcript_sid,
            "operator_sid": operator_sid or self.operator_sid,
        }
        self._context: Optional[OperatorResultContext] = None

    @property
    def _proxy(self) -> "OperatorResultContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: OperatorResultContext for this OperatorResultInstance
        """
        if self._context is None:
            self._context = OperatorResultContext(
                self._version,
                transcript_sid=self._solution["transcript_sid"],
                operator_sid=self._solution["operator_sid"],
            )
        return self._context

    def fetch(
        self, redacted: Union[bool, object] = values.unset
    ) -> "OperatorResultInstance":
        """
        Fetch the OperatorResultInstance

        :param redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.

        :returns: The fetched OperatorResultInstance
        """
        return self._proxy.fetch(
            redacted=redacted,
        )

    async def fetch_async(
        self, redacted: Union[bool, object] = values.unset
    ) -> "OperatorResultInstance":
        """
        Asynchronous coroutine to fetch the OperatorResultInstance

        :param redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.

        :returns: The fetched OperatorResultInstance
        """
        return await self._proxy.fetch_async(
            redacted=redacted,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Intelligence.V2.OperatorResultInstance {}>".format(context)


class OperatorResultContext(InstanceContext):

    def __init__(self, version: Version, transcript_sid: str, operator_sid: str):
        """
        Initialize the OperatorResultContext

        :param version: Version that contains the resource
        :param transcript_sid: A 34 character string that uniquely identifies this Transcript.
        :param operator_sid: A 34 character string that identifies this Language Understanding operator sid.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "transcript_sid": transcript_sid,
            "operator_sid": operator_sid,
        }
        self._uri = (
            "/Transcripts/{transcript_sid}/OperatorResults/{operator_sid}".format(
                **self._solution
            )
        )

    def fetch(
        self, redacted: Union[bool, object] = values.unset
    ) -> OperatorResultInstance:
        """
        Fetch the OperatorResultInstance

        :param redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.

        :returns: The fetched OperatorResultInstance
        """

        data = values.of(
            {
                "Redacted": serialize.boolean_to_string(redacted),
            }
        )

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = self._version.fetch(
            method="GET", uri=self._uri, params=data, headers=headers
        )

        return OperatorResultInstance(
            self._version,
            payload,
            transcript_sid=self._solution["transcript_sid"],
            operator_sid=self._solution["operator_sid"],
        )

    async def fetch_async(
        self, redacted: Union[bool, object] = values.unset
    ) -> OperatorResultInstance:
        """
        Asynchronous coroutine to fetch the OperatorResultInstance

        :param redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.

        :returns: The fetched OperatorResultInstance
        """

        data = values.of(
            {
                "Redacted": serialize.boolean_to_string(redacted),
            }
        )

        headers = values.of({})

        headers["Accept"] = "application/json"

        payload = await self._version.fetch_async(
            method="GET", uri=self._uri, params=data, headers=headers
        )

        return OperatorResultInstance(
            self._version,
            payload,
            transcript_sid=self._solution["transcript_sid"],
            operator_sid=self._solution["operator_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Intelligence.V2.OperatorResultContext {}>".format(context)


class OperatorResultPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> OperatorResultInstance:
        """
        Build an instance of OperatorResultInstance

        :param payload: Payload response from the API
        """
        return OperatorResultInstance(
            self._version, payload, transcript_sid=self._solution["transcript_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.OperatorResultPage>"


class OperatorResultList(ListResource):

    def __init__(self, version: Version, transcript_sid: str):
        """
        Initialize the OperatorResultList

        :param version: Version that contains the resource
        :param transcript_sid: A 34 character string that uniquely identifies this Transcript.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "transcript_sid": transcript_sid,
        }
        self._uri = "/Transcripts/{transcript_sid}/OperatorResults".format(
            **self._solution
        )

    def stream(
        self,
        redacted: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[OperatorResultInstance]:
        """
        Streams OperatorResultInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(redacted=redacted, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        redacted: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[OperatorResultInstance]:
        """
        Asynchronously streams OperatorResultInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(redacted=redacted, page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        redacted: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[OperatorResultInstance]:
        """
        Lists OperatorResultInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                redacted=redacted,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        redacted: Union[bool, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[OperatorResultInstance]:
        """
        Asynchronously lists OperatorResultInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                redacted=redacted,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        redacted: Union[bool, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> OperatorResultPage:
        """
        Retrieve a single page of OperatorResultInstance records from the API.
        Request is executed immediately

        :param redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of OperatorResultInstance
        """
        data = values.of(
            {
                "Redacted": serialize.boolean_to_string(redacted),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = self._version.page(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return OperatorResultPage(self._version, response, self._solution)

    async def page_async(
        self,
        redacted: Union[bool, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> OperatorResultPage:
        """
        Asynchronously retrieve a single page of OperatorResultInstance records from the API.
        Request is executed immediately

        :param redacted: Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of OperatorResultInstance
        """
        data = values.of(
            {
                "Redacted": serialize.boolean_to_string(redacted),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        headers = values.of({"Content-Type": "application/x-www-form-urlencoded"})

        headers["Accept"] = "application/json"

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data, headers=headers
        )
        return OperatorResultPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> OperatorResultPage:
        """
        Retrieve a specific page of OperatorResultInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of OperatorResultInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return OperatorResultPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> OperatorResultPage:
        """
        Asynchronously retrieve a specific page of OperatorResultInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of OperatorResultInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return OperatorResultPage(self._version, response, self._solution)

    def get(self, operator_sid: str) -> OperatorResultContext:
        """
        Constructs a OperatorResultContext

        :param operator_sid: A 34 character string that identifies this Language Understanding operator sid.
        """
        return OperatorResultContext(
            self._version,
            transcript_sid=self._solution["transcript_sid"],
            operator_sid=operator_sid,
        )

    def __call__(self, operator_sid: str) -> OperatorResultContext:
        """
        Constructs a OperatorResultContext

        :param operator_sid: A 34 character string that identifies this Language Understanding operator sid.
        """
        return OperatorResultContext(
            self._version,
            transcript_sid=self._solution["transcript_sid"],
            operator_sid=operator_sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Intelligence.V2.OperatorResultList>"
