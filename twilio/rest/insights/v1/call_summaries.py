r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Insights
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional
from twilio.base import deserialize, values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CallSummariesInstance(InstanceResource):
    class AnsweredBy(object):
        UNKNOWN = "unknown"
        MACHINE_START = "machine_start"
        MACHINE_END_BEEP = "machine_end_beep"
        MACHINE_END_SILENCE = "machine_end_silence"
        MACHINE_END_OTHER = "machine_end_other"
        HUMAN = "human"
        FAX = "fax"

    class CallState(object):
        RINGING = "ringing"
        COMPLETED = "completed"
        BUSY = "busy"
        FAIL = "fail"
        NOANSWER = "noanswer"
        CANCELED = "canceled"
        ANSWERED = "answered"
        UNDIALED = "undialed"

    class CallType(object):
        CARRIER = "carrier"
        SIP = "sip"
        TRUNKING = "trunking"
        CLIENT = "client"

    class ProcessingState(object):
        COMPLETE = "complete"
        PARTIAL = "partial"

    class ProcessingStateRequest(object):
        COMPLETED = "completed"
        STARTED = "started"
        PARTIAL = "partial"
        ALL = "all"

    class SortBy(object):
        START_TIME = "start_time"
        END_TIME = "end_time"

    """
    :ivar account_sid: 
    :ivar call_sid: 
    :ivar answered_by: 
    :ivar call_type: 
    :ivar call_state: 
    :ivar processing_state: 
    :ivar created_time: 
    :ivar start_time: 
    :ivar end_time: 
    :ivar duration: 
    :ivar connect_duration: 
    :ivar _from: 
    :ivar to: 
    :ivar carrier_edge: 
    :ivar client_edge: 
    :ivar sdk_edge: 
    :ivar sip_edge: 
    :ivar tags: 
    :ivar url: 
    :ivar attributes: 
    :ivar properties: 
    :ivar trust: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.call_sid: Optional[str] = payload.get("call_sid")
        self.answered_by: Optional["CallSummariesInstance.AnsweredBy"] = payload.get(
            "answered_by"
        )
        self.call_type: Optional["CallSummariesInstance.CallType"] = payload.get(
            "call_type"
        )
        self.call_state: Optional["CallSummariesInstance.CallState"] = payload.get(
            "call_state"
        )
        self.processing_state: Optional[
            "CallSummariesInstance.ProcessingState"
        ] = payload.get("processing_state")
        self.created_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("created_time")
        )
        self.start_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("start_time")
        )
        self.end_time: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("end_time")
        )
        self.duration: Optional[int] = deserialize.integer(payload.get("duration"))
        self.connect_duration: Optional[int] = deserialize.integer(
            payload.get("connect_duration")
        )
        self._from: Optional[Dict[str, object]] = payload.get("from")
        self.to: Optional[Dict[str, object]] = payload.get("to")
        self.carrier_edge: Optional[Dict[str, object]] = payload.get("carrier_edge")
        self.client_edge: Optional[Dict[str, object]] = payload.get("client_edge")
        self.sdk_edge: Optional[Dict[str, object]] = payload.get("sdk_edge")
        self.sip_edge: Optional[Dict[str, object]] = payload.get("sip_edge")
        self.tags: Optional[List[str]] = payload.get("tags")
        self.url: Optional[str] = payload.get("url")
        self.attributes: Optional[Dict[str, object]] = payload.get("attributes")
        self.properties: Optional[Dict[str, object]] = payload.get("properties")
        self.trust: Optional[Dict[str, object]] = payload.get("trust")

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Insights.V1.CallSummariesInstance>"


class CallSummariesPage(Page):
    def get_instance(self, payload) -> CallSummariesInstance:
        """
        Build an instance of CallSummariesInstance

        :param dict payload: Payload response from the API
        """
        return CallSummariesInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.CallSummariesPage>"


class CallSummariesList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the CallSummariesList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Voice/Summaries"

    def stream(
        self,
        from_=values.unset,
        to=values.unset,
        from_carrier=values.unset,
        to_carrier=values.unset,
        from_country_code=values.unset,
        to_country_code=values.unset,
        branded=values.unset,
        verified_caller=values.unset,
        has_tag=values.unset,
        start_time=values.unset,
        end_time=values.unset,
        call_type=values.unset,
        call_state=values.unset,
        direction=values.unset,
        processing_state=values.unset,
        sort_by=values.unset,
        subaccount=values.unset,
        abnormal_session=values.unset,
        limit=None,
        page_size=None,
    ) -> List[CallSummariesInstance]:
        """
        Streams CallSummariesInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str from_:
        :param str to:
        :param str from_carrier:
        :param str to_carrier:
        :param str from_country_code:
        :param str to_country_code:
        :param bool branded:
        :param bool verified_caller:
        :param bool has_tag:
        :param str start_time:
        :param str end_time:
        :param str call_type:
        :param str call_state:
        :param str direction:
        :param &quot;CallSummariesInstance.ProcessingStateRequest&quot; processing_state:
        :param &quot;CallSummariesInstance.SortBy&quot; sort_by:
        :param str subaccount:
        :param bool abnormal_session:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            from_=from_,
            to=to,
            from_carrier=from_carrier,
            to_carrier=to_carrier,
            from_country_code=from_country_code,
            to_country_code=to_country_code,
            branded=branded,
            verified_caller=verified_caller,
            has_tag=has_tag,
            start_time=start_time,
            end_time=end_time,
            call_type=call_type,
            call_state=call_state,
            direction=direction,
            processing_state=processing_state,
            sort_by=sort_by,
            subaccount=subaccount,
            abnormal_session=abnormal_session,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        from_=values.unset,
        to=values.unset,
        from_carrier=values.unset,
        to_carrier=values.unset,
        from_country_code=values.unset,
        to_country_code=values.unset,
        branded=values.unset,
        verified_caller=values.unset,
        has_tag=values.unset,
        start_time=values.unset,
        end_time=values.unset,
        call_type=values.unset,
        call_state=values.unset,
        direction=values.unset,
        processing_state=values.unset,
        sort_by=values.unset,
        subaccount=values.unset,
        abnormal_session=values.unset,
        limit=None,
        page_size=None,
    ) -> List[CallSummariesInstance]:
        """
        Asynchronously streams CallSummariesInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str from_:
        :param str to:
        :param str from_carrier:
        :param str to_carrier:
        :param str from_country_code:
        :param str to_country_code:
        :param bool branded:
        :param bool verified_caller:
        :param bool has_tag:
        :param str start_time:
        :param str end_time:
        :param str call_type:
        :param str call_state:
        :param str direction:
        :param &quot;CallSummariesInstance.ProcessingStateRequest&quot; processing_state:
        :param &quot;CallSummariesInstance.SortBy&quot; sort_by:
        :param str subaccount:
        :param bool abnormal_session:
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            from_=from_,
            to=to,
            from_carrier=from_carrier,
            to_carrier=to_carrier,
            from_country_code=from_country_code,
            to_country_code=to_country_code,
            branded=branded,
            verified_caller=verified_caller,
            has_tag=has_tag,
            start_time=start_time,
            end_time=end_time,
            call_type=call_type,
            call_state=call_state,
            direction=direction,
            processing_state=processing_state,
            sort_by=sort_by,
            subaccount=subaccount,
            abnormal_session=abnormal_session,
            page_size=limits["page_size"],
        )

        return await self._version.stream_async(page, limits["limit"])

    def list(
        self,
        from_=values.unset,
        to=values.unset,
        from_carrier=values.unset,
        to_carrier=values.unset,
        from_country_code=values.unset,
        to_country_code=values.unset,
        branded=values.unset,
        verified_caller=values.unset,
        has_tag=values.unset,
        start_time=values.unset,
        end_time=values.unset,
        call_type=values.unset,
        call_state=values.unset,
        direction=values.unset,
        processing_state=values.unset,
        sort_by=values.unset,
        subaccount=values.unset,
        abnormal_session=values.unset,
        limit=None,
        page_size=None,
    ) -> List[CallSummariesInstance]:
        """
        Lists CallSummariesInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str from_:
        :param str to:
        :param str from_carrier:
        :param str to_carrier:
        :param str from_country_code:
        :param str to_country_code:
        :param bool branded:
        :param bool verified_caller:
        :param bool has_tag:
        :param str start_time:
        :param str end_time:
        :param str call_type:
        :param str call_state:
        :param str direction:
        :param &quot;CallSummariesInstance.ProcessingStateRequest&quot; processing_state:
        :param &quot;CallSummariesInstance.SortBy&quot; sort_by:
        :param str subaccount:
        :param bool abnormal_session:
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            self.stream(
                from_=from_,
                to=to,
                from_carrier=from_carrier,
                to_carrier=to_carrier,
                from_country_code=from_country_code,
                to_country_code=to_country_code,
                branded=branded,
                verified_caller=verified_caller,
                has_tag=has_tag,
                start_time=start_time,
                end_time=end_time,
                call_type=call_type,
                call_state=call_state,
                direction=direction,
                processing_state=processing_state,
                sort_by=sort_by,
                subaccount=subaccount,
                abnormal_session=abnormal_session,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        from_=values.unset,
        to=values.unset,
        from_carrier=values.unset,
        to_carrier=values.unset,
        from_country_code=values.unset,
        to_country_code=values.unset,
        branded=values.unset,
        verified_caller=values.unset,
        has_tag=values.unset,
        start_time=values.unset,
        end_time=values.unset,
        call_type=values.unset,
        call_state=values.unset,
        direction=values.unset,
        processing_state=values.unset,
        sort_by=values.unset,
        subaccount=values.unset,
        abnormal_session=values.unset,
        limit=None,
        page_size=None,
    ) -> List[CallSummariesInstance]:
        """
        Asynchronously lists CallSummariesInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str from_:
        :param str to:
        :param str from_carrier:
        :param str to_carrier:
        :param str from_country_code:
        :param str to_country_code:
        :param bool branded:
        :param bool verified_caller:
        :param bool has_tag:
        :param str start_time:
        :param str end_time:
        :param str call_type:
        :param str call_state:
        :param str direction:
        :param &quot;CallSummariesInstance.ProcessingStateRequest&quot; processing_state:
        :param &quot;CallSummariesInstance.SortBy&quot; sort_by:
        :param str subaccount:
        :param bool abnormal_session:
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        return list(
            await self.stream_async(
                from_=from_,
                to=to,
                from_carrier=from_carrier,
                to_carrier=to_carrier,
                from_country_code=from_country_code,
                to_country_code=to_country_code,
                branded=branded,
                verified_caller=verified_caller,
                has_tag=has_tag,
                start_time=start_time,
                end_time=end_time,
                call_type=call_type,
                call_state=call_state,
                direction=direction,
                processing_state=processing_state,
                sort_by=sort_by,
                subaccount=subaccount,
                abnormal_session=abnormal_session,
                limit=limit,
                page_size=page_size,
            )
        )

    def page(
        self,
        from_=values.unset,
        to=values.unset,
        from_carrier=values.unset,
        to_carrier=values.unset,
        from_country_code=values.unset,
        to_country_code=values.unset,
        branded=values.unset,
        verified_caller=values.unset,
        has_tag=values.unset,
        start_time=values.unset,
        end_time=values.unset,
        call_type=values.unset,
        call_state=values.unset,
        direction=values.unset,
        processing_state=values.unset,
        sort_by=values.unset,
        subaccount=values.unset,
        abnormal_session=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> CallSummariesPage:
        """
        Retrieve a single page of CallSummariesInstance records from the API.
        Request is executed immediately

        :param str from_:
        :param str to:
        :param str from_carrier:
        :param str to_carrier:
        :param str from_country_code:
        :param str to_country_code:
        :param bool branded:
        :param bool verified_caller:
        :param bool has_tag:
        :param str start_time:
        :param str end_time:
        :param str call_type:
        :param str call_state:
        :param str direction:
        :param &quot;CallSummariesInstance.ProcessingStateRequest&quot; processing_state:
        :param &quot;CallSummariesInstance.SortBy&quot; sort_by:
        :param str subaccount:
        :param bool abnormal_session:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CallSummariesInstance
        """
        data = values.of(
            {
                "From": from_,
                "To": to,
                "FromCarrier": from_carrier,
                "ToCarrier": to_carrier,
                "FromCountryCode": from_country_code,
                "ToCountryCode": to_country_code,
                "Branded": branded,
                "VerifiedCaller": verified_caller,
                "HasTag": has_tag,
                "StartTime": start_time,
                "EndTime": end_time,
                "CallType": call_type,
                "CallState": call_state,
                "Direction": direction,
                "ProcessingState": processing_state,
                "SortBy": sort_by,
                "Subaccount": subaccount,
                "AbnormalSession": abnormal_session,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return CallSummariesPage(self._version, response)

    async def page_async(
        self,
        from_=values.unset,
        to=values.unset,
        from_carrier=values.unset,
        to_carrier=values.unset,
        from_country_code=values.unset,
        to_country_code=values.unset,
        branded=values.unset,
        verified_caller=values.unset,
        has_tag=values.unset,
        start_time=values.unset,
        end_time=values.unset,
        call_type=values.unset,
        call_state=values.unset,
        direction=values.unset,
        processing_state=values.unset,
        sort_by=values.unset,
        subaccount=values.unset,
        abnormal_session=values.unset,
        page_token=values.unset,
        page_number=values.unset,
        page_size=values.unset,
    ) -> CallSummariesPage:
        """
        Asynchronously retrieve a single page of CallSummariesInstance records from the API.
        Request is executed immediately

        :param str from_:
        :param str to:
        :param str from_carrier:
        :param str to_carrier:
        :param str from_country_code:
        :param str to_country_code:
        :param bool branded:
        :param bool verified_caller:
        :param bool has_tag:
        :param str start_time:
        :param str end_time:
        :param str call_type:
        :param str call_state:
        :param str direction:
        :param &quot;CallSummariesInstance.ProcessingStateRequest&quot; processing_state:
        :param &quot;CallSummariesInstance.SortBy&quot; sort_by:
        :param str subaccount:
        :param bool abnormal_session:
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CallSummariesInstance
        """
        data = values.of(
            {
                "From": from_,
                "To": to,
                "FromCarrier": from_carrier,
                "ToCarrier": to_carrier,
                "FromCountryCode": from_country_code,
                "ToCountryCode": to_country_code,
                "Branded": branded,
                "VerifiedCaller": verified_caller,
                "HasTag": has_tag,
                "StartTime": start_time,
                "EndTime": end_time,
                "CallType": call_type,
                "CallState": call_state,
                "Direction": direction,
                "ProcessingState": processing_state,
                "SortBy": sort_by,
                "Subaccount": subaccount,
                "AbnormalSession": abnormal_session,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return CallSummariesPage(self._version, response)

    def get_page(self, target_url) -> CallSummariesPage:
        """
        Retrieve a specific page of CallSummariesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CallSummariesInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return CallSummariesPage(self._version, response)

    async def get_page_async(self, target_url) -> CallSummariesPage:
        """
        Asynchronously retrieve a specific page of CallSummariesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CallSummariesInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return CallSummariesPage(self._version, response)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Insights.V1.CallSummariesList>"
