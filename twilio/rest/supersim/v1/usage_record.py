r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from twilio.base import deserialize, serialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class UsageRecordInstance(InstanceResource):
    class Granularity(object):
        HOUR = "hour"
        DAY = "day"
        ALL = "all"

    class Group(object):
        SIM = "sim"
        FLEET = "fleet"
        NETWORK = "network"
        ISOCOUNTRY = "isoCountry"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that incurred the usage.
    :ivar sim_sid: SID of a Sim resource to which the UsageRecord belongs. Value will only be present when either a value for the `Sim` query parameter is provided or when UsageRecords are grouped by `sim`. Otherwise, the value will be `null`.
    :ivar network_sid: SID of the Network resource the usage occurred on. Value will only be present when either a value for the `Network` query parameter is provided or when UsageRecords are grouped by `network`. Otherwise, the value will be `null`.
    :ivar fleet_sid: SID of the Fleet resource the usage occurred on. Value will only be present when either a value for the `Fleet` query parameter is provided or when UsageRecords are grouped by `fleet`. Otherwise, the value will be `null`.
    :ivar iso_country: Alpha-2 ISO Country Code that the usage occurred in. Value will only be present when either a value for the `IsoCountry` query parameter is provided or when UsageRecords are grouped by `isoCountry`. Otherwise, the value will be `null`.
    :ivar period: The time period for which the usage is reported. The period is represented as a pair of `start_time` and `end_time` timestamps specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar data_upload: Total data uploaded in bytes, aggregated by the query parameters.
    :ivar data_download: Total data downloaded in bytes, aggregated by the query parameters.
    :ivar data_total: Total of data_upload and data_download.
    :ivar data_total_billed: Total amount in the `billed_unit` that was charged for the data uploaded or downloaded. Will return 0 for usage prior to February 1, 2022. Value may be 0 despite `data_total` being greater than 0 if the data usage is still being processed by Twilio's billing system. Refer to [Data Usage Processing](https://www.twilio.com/docs/iot/supersim/api/usage-record-resource#data-usage-processing) for more details.
    :ivar billed_unit: The currency in which the billed amounts are measured, specified in the 3 letter ISO 4127 format (e.g. `USD`, `EUR`, `JPY`). This can be null when data_toal_billed is 0 and we do not yet have billing information for the corresponding data usage. Refer to [Data Usage Processing](https://www.twilio.com/docs/iot/supersim/api/usage-record-resource#data-usage-processing) for more details.
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.sim_sid: Optional[str] = payload.get("sim_sid")
        self.network_sid: Optional[str] = payload.get("network_sid")
        self.fleet_sid: Optional[str] = payload.get("fleet_sid")
        self.iso_country: Optional[str] = payload.get("iso_country")
        self.period: Optional[Dict[str, object]] = payload.get("period")
        self.data_upload: Optional[int] = payload.get("data_upload")
        self.data_download: Optional[int] = payload.get("data_download")
        self.data_total: Optional[int] = payload.get("data_total")
        self.data_total_billed: Optional[float] = deserialize.decimal(
            payload.get("data_total_billed")
        )
        self.billed_unit: Optional[str] = payload.get("billed_unit")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Supersim.V1.UsageRecordInstance>"


class UsageRecordPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> UsageRecordInstance:
        """
        Build an instance of UsageRecordInstance

        :param payload: Payload response from the API
        """
        return UsageRecordInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.UsageRecordPage>"


class UsageRecordList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the UsageRecordList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/UsageRecords"

    def stream(
        self,
        sim: Union[str, object] = values.unset,
        fleet: Union[str, object] = values.unset,
        network: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        group: Union["UsageRecordInstance.Group", object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        start_time: Union[datetime, object] = values.unset,
        end_time: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsageRecordInstance]:
        """
        Streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param &quot;UsageRecordInstance.Group&quot; group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param &quot;UsageRecordInstance.Granularity&quot; granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
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
            sim=sim,
            fleet=fleet,
            network=network,
            iso_country=iso_country,
            group=group,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        sim: Union[str, object] = values.unset,
        fleet: Union[str, object] = values.unset,
        network: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        group: Union["UsageRecordInstance.Group", object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        start_time: Union[datetime, object] = values.unset,
        end_time: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsageRecordInstance]:
        """
        Asynchronously streams UsageRecordInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param &quot;UsageRecordInstance.Group&quot; group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param &quot;UsageRecordInstance.Granularity&quot; granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
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
            sim=sim,
            fleet=fleet,
            network=network,
            iso_country=iso_country,
            group=group,
            granularity=granularity,
            start_time=start_time,
            end_time=end_time,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        sim: Union[str, object] = values.unset,
        fleet: Union[str, object] = values.unset,
        network: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        group: Union["UsageRecordInstance.Group", object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        start_time: Union[datetime, object] = values.unset,
        end_time: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsageRecordInstance]:
        """
        Lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param &quot;UsageRecordInstance.Group&quot; group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param &quot;UsageRecordInstance.Granularity&quot; granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
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
                sim=sim,
                fleet=fleet,
                network=network,
                iso_country=iso_country,
                group=group,
                granularity=granularity,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        sim: Union[str, object] = values.unset,
        fleet: Union[str, object] = values.unset,
        network: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        group: Union["UsageRecordInstance.Group", object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        start_time: Union[datetime, object] = values.unset,
        end_time: Union[datetime, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[UsageRecordInstance]:
        """
        Asynchronously lists UsageRecordInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param str fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param str network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param str iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param &quot;UsageRecordInstance.Group&quot; group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param &quot;UsageRecordInstance.Granularity&quot; granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param datetime start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param datetime end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
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
                sim=sim,
                fleet=fleet,
                network=network,
                iso_country=iso_country,
                group=group,
                granularity=granularity,
                start_time=start_time,
                end_time=end_time,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        sim: Union[str, object] = values.unset,
        fleet: Union[str, object] = values.unset,
        network: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        group: Union["UsageRecordInstance.Group", object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        start_time: Union[datetime, object] = values.unset,
        end_time: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UsageRecordPage:
        """
        Retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Fleet": fleet,
                "Network": network,
                "IsoCountry": iso_country,
                "Group": group,
                "Granularity": granularity,
                "StartTime": serialize.iso8601_datetime(start_time),
                "EndTime": serialize.iso8601_datetime(end_time),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return UsageRecordPage(self._version, response)

    async def page_async(
        self,
        sim: Union[str, object] = values.unset,
        fleet: Union[str, object] = values.unset,
        network: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        group: Union["UsageRecordInstance.Group", object] = values.unset,
        granularity: Union["UsageRecordInstance.Granularity", object] = values.unset,
        start_time: Union[datetime, object] = values.unset,
        end_time: Union[datetime, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> UsageRecordPage:
        """
        Asynchronously retrieve a single page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param sim: SID or unique name of a Sim resource. Only show UsageRecords representing usage incurred by this Super SIM.
        :param fleet: SID or unique name of a Fleet resource. Only show UsageRecords representing usage for Super SIMs belonging to this Fleet resource at the time the usage occurred.
        :param network: SID of a Network resource. Only show UsageRecords representing usage on this network.
        :param iso_country: Alpha-2 ISO Country Code. Only show UsageRecords representing usage in this country.
        :param group: Dimension over which to aggregate usage records. Can be: `sim`, `fleet`, `network`, `isoCountry`. Default is to not aggregate across any of these dimensions, UsageRecords will be aggregated into the time buckets described by the `Granularity` parameter.
        :param granularity: Time-based grouping that UsageRecords should be aggregated by. Can be: `hour`, `day`, or `all`. Default is `all`. `all` returns one UsageRecord that describes the usage for the entire period.
        :param start_time: Only include usage that occurred at or after this time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is one month before the `end_time`.
        :param end_time: Only include usage that occurred before this time (exclusive), specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Default is the current time.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of UsageRecordInstance
        """
        data = values.of(
            {
                "Sim": sim,
                "Fleet": fleet,
                "Network": network,
                "IsoCountry": iso_country,
                "Group": group,
                "Granularity": granularity,
                "StartTime": serialize.iso8601_datetime(start_time),
                "EndTime": serialize.iso8601_datetime(end_time),
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return UsageRecordPage(self._version, response)

    def get_page(self, target_url: str) -> UsageRecordPage:
        """
        Retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return UsageRecordPage(self._version, response)

    async def get_page_async(self, target_url: str) -> UsageRecordPage:
        """
        Asynchronously retrieve a specific page of UsageRecordInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of UsageRecordInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return UsageRecordPage(self._version, response)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Supersim.V1.UsageRecordList>"
