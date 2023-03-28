r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
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


class FieldValueInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the FieldValue resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar field_type_sid: The SID of the Field Type associated with the Field Value.
    :ivar language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
    :ivar assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resource.
    :ivar sid: The unique string that we created to identify the FieldValue resource.
    :ivar value: The Field Value data.
    :ivar url: The absolute URL of the FieldValue resource.
    :ivar synonym_of: The word for which the field value is a synonym of.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        assistant_sid: str,
        field_type_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.field_type_sid: Optional[str] = payload.get("field_type_sid")
        self.language: Optional[str] = payload.get("language")
        self.assistant_sid: Optional[str] = payload.get("assistant_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.value: Optional[str] = payload.get("value")
        self.url: Optional[str] = payload.get("url")
        self.synonym_of: Optional[str] = payload.get("synonym_of")

        self._solution = {
            "assistant_sid": assistant_sid,
            "field_type_sid": field_type_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[FieldValueContext] = None

    @property
    def _proxy(self) -> "FieldValueContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FieldValueContext for this FieldValueInstance
        """
        if self._context is None:
            self._context = FieldValueContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                field_type_sid=self._solution["field_type_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the FieldValueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FieldValueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "FieldValueInstance":
        """
        Fetch the FieldValueInstance


        :returns: The fetched FieldValueInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FieldValueInstance":
        """
        Asynchronous coroutine to fetch the FieldValueInstance


        :returns: The fetched FieldValueInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.FieldValueInstance {}>".format(context)


class FieldValueContext(InstanceContext):
    def __init__(
        self, version: Version, assistant_sid: str, field_type_sid: str, sid: str
    ):
        """
        Initialize the FieldValueContext

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resource to fetch.
        :param field_type_sid: The SID of the Field Type associated with the Field Value to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the FieldValue resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "field_type_sid": field_type_sid,
            "sid": sid,
        }
        self._uri = "/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues/{sid}".format(
            **self._solution
        )

    def delete(self) -> bool:
        """
        Deletes the FieldValueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the FieldValueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> FieldValueInstance:
        """
        Fetch the FieldValueInstance


        :returns: The fetched FieldValueInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return FieldValueInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            field_type_sid=self._solution["field_type_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> FieldValueInstance:
        """
        Asynchronous coroutine to fetch the FieldValueInstance


        :returns: The fetched FieldValueInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return FieldValueInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            field_type_sid=self._solution["field_type_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.FieldValueContext {}>".format(context)


class FieldValuePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> FieldValueInstance:
        """
        Build an instance of FieldValueInstance

        :param payload: Payload response from the API
        """
        return FieldValueInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            field_type_sid=self._solution["field_type_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.FieldValuePage>"


class FieldValueList(ListResource):
    def __init__(self, version: Version, assistant_sid: str, field_type_sid: str):
        """
        Initialize the FieldValueList

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the FieldType associated with the resources to read.
        :param field_type_sid: The SID of the Field Type associated with the Field Value to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "field_type_sid": field_type_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/FieldTypes/{field_type_sid}/FieldValues".format(
            **self._solution
        )

    def create(
        self, language: str, value: str, synonym_of: Union[str, object] = values.unset
    ) -> FieldValueInstance:
        """
        Create the FieldValueInstance

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
        :param value: The Field Value data.
        :param synonym_of: The string value that indicates which word the field value is a synonym of.

        :returns: The created FieldValueInstance
        """
        data = values.of(
            {
                "Language": language,
                "Value": value,
                "SynonymOf": synonym_of,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FieldValueInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            field_type_sid=self._solution["field_type_sid"],
        )

    async def create_async(
        self, language: str, value: str, synonym_of: Union[str, object] = values.unset
    ) -> FieldValueInstance:
        """
        Asynchronously create the FieldValueInstance

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
        :param value: The Field Value data.
        :param synonym_of: The string value that indicates which word the field value is a synonym of.

        :returns: The created FieldValueInstance
        """
        data = values.of(
            {
                "Language": language,
                "Value": value,
                "SynonymOf": synonym_of,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return FieldValueInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            field_type_sid=self._solution["field_type_sid"],
        )

    def stream(
        self,
        language: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FieldValueInstance]:
        """
        Streams FieldValueInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(language=language, page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        language: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FieldValueInstance]:
        """
        Asynchronously streams FieldValueInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(language=language, page_size=limits["page_size"])

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        language: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FieldValueInstance]:
        """
        Lists FieldValueInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
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
                language=language,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        language: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[FieldValueInstance]:
        """
        Asynchronously lists FieldValueInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
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
                language=language,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        language: Union[str, object] = values.unset,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> FieldValuePage:
        """
        Retrieve a single page of FieldValueInstance records from the API.
        Request is executed immediately

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FieldValueInstance
        """
        data = values.of(
            {
                "Language": language,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return FieldValuePage(self._version, response, self._solution)

    async def page_async(
        self,
        language: Union[str, object] = values.unset,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> FieldValuePage:
        """
        Asynchronously retrieve a single page of FieldValueInstance records from the API.
        Request is executed immediately

        :param language: The [ISO language-country](https://docs.oracle.com/cd/E13214_01/wli/docs92/xref/xqisocodes.html) tag that specifies the language of the value. Currently supported tags: `en-US`
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of FieldValueInstance
        """
        data = values.of(
            {
                "Language": language,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return FieldValuePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> FieldValuePage:
        """
        Retrieve a specific page of FieldValueInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FieldValueInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return FieldValuePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> FieldValuePage:
        """
        Asynchronously retrieve a specific page of FieldValueInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of FieldValueInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return FieldValuePage(self._version, response, self._solution)

    def get(self, sid: str) -> FieldValueContext:
        """
        Constructs a FieldValueContext

        :param sid: The Twilio-provided string that uniquely identifies the FieldValue resource to fetch.
        """
        return FieldValueContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            field_type_sid=self._solution["field_type_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> FieldValueContext:
        """
        Constructs a FieldValueContext

        :param sid: The Twilio-provided string that uniquely identifies the FieldValue resource to fetch.
        """
        return FieldValueContext(
            self._version,
            assistant_sid=self._solution["assistant_sid"],
            field_type_sid=self._solution["field_type_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.FieldValueList>"
