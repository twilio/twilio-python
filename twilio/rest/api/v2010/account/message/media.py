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
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class MediaInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Media resource.
    :ivar content_type: The default [mime-type](https://en.wikipedia.org/wiki/Internet_media_type) of the media, for example `image/jpeg`, `image/png`, or `image/gif`
    :ivar date_created: The date and time in GMT that this resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar parent_sid: The SID of the resource that created the media.
    :ivar sid: The unique string that that we created to identify this Media resource.
    :ivar uri: The URI of this resource, relative to `https://api.twilio.com`.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        message_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.content_type: Optional[str] = payload.get("content_type")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.parent_sid: Optional[str] = payload.get("parent_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.uri: Optional[str] = payload.get("uri")

        self._solution = {
            "account_sid": account_sid,
            "message_sid": message_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[MediaContext] = None

    @property
    def _proxy(self) -> "MediaContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MediaContext for this MediaInstance
        """
        if self._context is None:
            self._context = MediaContext(
                self._version,
                account_sid=self._solution["account_sid"],
                message_sid=self._solution["message_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the MediaInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the MediaInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "MediaInstance":
        """
        Fetch the MediaInstance


        :returns: The fetched MediaInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "MediaInstance":
        """
        Asynchronous coroutine to fetch the MediaInstance


        :returns: The fetched MediaInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.MediaInstance {}>".format(context)


class MediaContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, message_sid: str, sid: str):
        """
        Initialize the MediaContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Media resource(s) to fetch.
        :param message_sid: The SID of the Message resource that this Media resource belongs to.
        :param sid: The Twilio-provided string that uniquely identifies the Media resource to fetch
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "message_sid": message_sid,
            "sid": sid,
        }
        self._uri = (
            "/Accounts/{account_sid}/Messages/{message_sid}/Media/{sid}.json".format(
                **self._solution
            )
        )

    def delete(self) -> bool:
        """
        Deletes the MediaInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the MediaInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> MediaInstance:
        """
        Fetch the MediaInstance


        :returns: The fetched MediaInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return MediaInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            message_sid=self._solution["message_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> MediaInstance:
        """
        Asynchronous coroutine to fetch the MediaInstance


        :returns: The fetched MediaInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return MediaInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            message_sid=self._solution["message_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.MediaContext {}>".format(context)


class MediaPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> MediaInstance:
        """
        Build an instance of MediaInstance

        :param payload: Payload response from the API
        """
        return MediaInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            message_sid=self._solution["message_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.MediaPage>"


class MediaList(ListResource):
    def __init__(self, version: Version, account_sid: str, message_sid: str):
        """
        Initialize the MediaList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Media resource(s) to read.
        :param message_sid: The SID of the Message resource that this Media resource belongs to.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "message_sid": message_sid,
        }
        self._uri = "/Accounts/{account_sid}/Messages/{message_sid}/Media.json".format(
            **self._solution
        )

    def stream(
        self,
        date_created: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MediaInstance]:
        """
        Streams MediaInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param datetime date_created_before: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param datetime date_created_after: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
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
            date_created=date_created,
            date_created_before=date_created_before,
            date_created_after=date_created_after,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        date_created: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MediaInstance]:
        """
        Asynchronously streams MediaInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime date_created: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param datetime date_created_before: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param datetime date_created_after: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
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
            date_created=date_created,
            date_created_before=date_created_before,
            date_created_after=date_created_after,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        date_created: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MediaInstance]:
        """
        Lists MediaInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param datetime date_created_before: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param datetime date_created_after: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
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
                date_created=date_created,
                date_created_before=date_created_before,
                date_created_after=date_created_after,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        date_created: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[MediaInstance]:
        """
        Asynchronously lists MediaInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime date_created: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param datetime date_created_before: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param datetime date_created_after: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
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
                date_created=date_created,
                date_created_before=date_created_before,
                date_created_after=date_created_after,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        date_created: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> MediaPage:
        """
        Retrieve a single page of MediaInstance records from the API.
        Request is executed immediately

        :param date_created: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param date_created_before: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param date_created_after: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MediaInstance
        """
        data = values.of(
            {
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateCreated<": serialize.iso8601_datetime(date_created_before),
                "DateCreated>": serialize.iso8601_datetime(date_created_after),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return MediaPage(self._version, response, self._solution)

    async def page_async(
        self,
        date_created: Union[datetime, object] = values.unset,
        date_created_before: Union[datetime, object] = values.unset,
        date_created_after: Union[datetime, object] = values.unset,
        page_token: Optional[str] = None,
        page_number: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> MediaPage:
        """
        Asynchronously retrieve a single page of MediaInstance records from the API.
        Request is executed immediately

        :param date_created: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param date_created_before: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param date_created_after: Only include media that was created on this date. Specify a date as `YYYY-MM-DD` in GMT, for example: `2009-07-06`, to read media that was created on this date. You can also specify an inequality, such as `StartTime<=YYYY-MM-DD`, to read media that was created on or before midnight of this date, and `StartTime>=YYYY-MM-DD` to read media that was created on or after midnight of this date.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of MediaInstance
        """
        data = values.of(
            {
                "DateCreated": serialize.iso8601_datetime(date_created),
                "DateCreated<": serialize.iso8601_datetime(date_created_before),
                "DateCreated>": serialize.iso8601_datetime(date_created_after),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return MediaPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> MediaPage:
        """
        Retrieve a specific page of MediaInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MediaInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return MediaPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> MediaPage:
        """
        Asynchronously retrieve a specific page of MediaInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of MediaInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return MediaPage(self._version, response, self._solution)

    def get(self, sid: str) -> MediaContext:
        """
        Constructs a MediaContext

        :param sid: The Twilio-provided string that uniquely identifies the Media resource to fetch
        """
        return MediaContext(
            self._version,
            account_sid=self._solution["account_sid"],
            message_sid=self._solution["message_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> MediaContext:
        """
        Constructs a MediaContext

        :param sid: The Twilio-provided string that uniquely identifies the Media resource to fetch
        """
        return MediaContext(
            self._version,
            account_sid=self._solution["account_sid"],
            message_sid=self._solution["message_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.MediaList>"
