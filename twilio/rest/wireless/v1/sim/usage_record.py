r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Wireless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UsageRecordInstance(InstanceResource):
    class Granularity(object):
        HOURLY = "hourly"
        DAILY = "daily"
        ALL = "all"

    """
    :ivar sim_sid: The SID of the [Sim resource](https://www.twilio.com/docs/wireless/api/sim-resource) that this Usage Record is for.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageRecord resource.
    :ivar period: The time period for which the usage is reported. Contains `start` and `end` datetime values given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
    :ivar commands: An object that describes the SIM's usage of Commands during the specified period. See [Commands Usage Object](https://www.twilio.com/docs/wireless/api/sim-usagerecord-resource#commands-usage-object).
    :ivar data: An object that describes the SIM's data usage during the specified period. See [Data Usage Object](https://www.twilio.com/docs/wireless/api/sim-usagerecord-resource#data-usage-object).
    """

    def __init__(self, version: Version, payload: Dict[str, Any], sim_sid: str):
        super().__init__(version)

        self.sim_sid: Optional[str] = payload.get("sim_sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.period: Optional[Dict[str, object]] = payload.get("period")
        self.commands: Optional[Dict[str, object]] = payload.get("commands")
        self.data: Optional[Dict[str, object]] = payload.get("data")

        self._solution = {
            "sim_sid": sim_sid,
        }

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Wireless.V1.UsageRecordInstance {}>".format(context)


class UsageRecordPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> UsageRecordInstance:
        """
        Build an instance of UsageRecordInstance

        :param payload: Payload response from the API
        """
        return UsageRecordInstance(
            self._version, payload, sim_sid=self._solution["sim_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.UsageRecordPage>"


class UsageRecordList(ListResource):
    def __init__(self, version: Version, sim_sid: str):
        """
        Initialize the UsageRecordList

        :param version: Version that contains the resource
        :param sim_sid: The SID of the [Sim resource](https://www.twilio.com/docs/wireless/api/sim-resource)  to read the usage from.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sim_sid": sim_sid,
        }
        self._uri = "/Sims/{sim_sid}/UsageRecords".format(**self._solution)

    def stream(
        self,
        end: Union[datetime, object] = values.unset,
        start: Union[datetime, object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsageRecordInstance]:
        """
        Streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param &quot;UsageRecordInstance.Granularity&quot; granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
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
            end=end, start=start, granularity=granularity, page_size=limits["page_size"]
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        end: Union[datetime, object] = values.unset,
        start: Union[datetime, object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsageRecordInstance]:
        """
        Asynchronously streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param &quot;UsageRecordInstance.Granularity&quot; granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
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
            end=end, start=start, granularity=granularity, page_size=limits["page_size"]
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        end: Union[datetime, object] = values.unset,
        start: Union[datetime, object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsageRecordInstance]:
        """
        Lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param &quot;UsageRecordInstance.Granularity&quot; granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
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
                end=end,
                start=start,
                granularity=granularity,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        end: Union[datetime, object] = values.unset,
        start: Union[datetime, object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsageRecordInstance]:
        """
        Asynchronously lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param datetime end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param datetime start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param &quot;UsageRecordInstance.Granularity&quot; granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
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
                end=end,
                start=start,
                granularity=granularity,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        end: Union[datetime, object] = values.unset,
        start: Union[datetime, object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UsageRecordPage:
        """
        Retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        """
        data = values.of(
            {
                "End": serialize.iso8601_datetime(end),
                "Start": serialize.iso8601_datetime(start),
                "Granularity": granularity,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UsageRecordPage(self._version, response, self._solution)

    async def page_async(
        self,
        end: Union[datetime, object] = values.unset,
        start: Union[datetime, object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UsageRecordPage:
        """
        Asynchronously retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param end: Only include usage that occurred on or before this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is the current time.
        :param start: Only include usage that has occurred on or after this date, specified in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html). The default is one month before the `end` parameter value.
        :param granularity: How to summarize the usage by time. Can be: `daily`, `hourly`, or `all`. The default is `all`. A value of `all` returns one Usage Record that describes the usage for the entire period.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        """
        data = values.of(
            {
                "End": serialize.iso8601_datetime(end),
                "Start": serialize.iso8601_datetime(start),
                "Granularity": granularity,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return UsageRecordPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> UsageRecordPage:
        """
        Retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UsageRecordPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> UsageRecordPage:
        """
        Asynchronously retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UsageRecordPage(self._version, response, self._solution)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Wireless.V1.UsageRecordList>"
