"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CallSummariesList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CallSummariesList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.insights.v1.call_summaries.CallSummariesList
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Voice/Summaries'.format(**self._solution)
        
        
    
    def stream(self, from_=values.unset, to=values.unset, from_carrier=values.unset, to_carrier=values.unset, from_country_code=values.unset, to_country_code=values.unset, branded=values.unset, verified_caller=values.unset, has_tag=values.unset, start_time=values.unset, end_time=values.unset, call_type=values.unset, call_state=values.unset, direction=values.unset, processing_state=values.unset, sort_by=values.unset, subaccount=values.unset, abnormal_session=values.unset, limit=None, page_size=None):
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
        :param CallSummariesProcessingStateRequest processing_state: 
        :param CallSummariesSortBy sort_by: 
        :param str subaccount: 
        :param bool abnormal_session: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call_summaries.CallSummariesInstance]
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
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, from_=values.unset, to=values.unset, from_carrier=values.unset, to_carrier=values.unset, from_country_code=values.unset, to_country_code=values.unset, branded=values.unset, verified_caller=values.unset, has_tag=values.unset, start_time=values.unset, end_time=values.unset, call_type=values.unset, call_state=values.unset, direction=values.unset, processing_state=values.unset, sort_by=values.unset, subaccount=values.unset, abnormal_session=values.unset, limit=None, page_size=None):
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
        :param CallSummariesProcessingStateRequest processing_state: 
        :param CallSummariesSortBy sort_by: 
        :param str subaccount: 
        :param bool abnormal_session: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call_summaries.CallSummariesInstance]
        """
        return list(self.stream(
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
        ))

    def page(self, from_=values.unset, to=values.unset, from_carrier=values.unset, to_carrier=values.unset, from_country_code=values.unset, to_country_code=values.unset, branded=values.unset, verified_caller=values.unset, has_tag=values.unset, start_time=values.unset, end_time=values.unset, call_type=values.unset, call_state=values.unset, direction=values.unset, processing_state=values.unset, sort_by=values.unset, subaccount=values.unset, abnormal_session=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
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
        :param CallSummariesProcessingStateRequest processing_state: 
        :param CallSummariesSortBy sort_by: 
        :param str subaccount: 
        :param bool abnormal_session: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CallSummariesInstance
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesPage
        """
        data = values.of({ 
            'From': from_,
            'To': to,
            'FromCarrier': from_carrier,
            'ToCarrier': to_carrier,
            'FromCountryCode': from_country_code,
            'ToCountryCode': to_country_code,
            'Branded': branded,
            'VerifiedCaller': verified_caller,
            'HasTag': has_tag,
            'StartTime': start_time,
            'EndTime': end_time,
            'CallType': call_type,
            'CallState': call_state,
            'Direction': direction,
            'ProcessingState': processing_state,
            'SortBy': sort_by,
            'Subaccount': subaccount,
            'AbnormalSession': abnormal_session,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CallSummariesPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CallSummariesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CallSummariesInstance
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CallSummariesPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummariesList>'


class CallSummariesPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CallSummariesPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.call_summaries.CallSummariesPage
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CallSummariesInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.call_summaries.CallSummariesInstance
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesInstance
        """
        return CallSummariesInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallSummariesPage>'




class CallSummariesInstance(InstanceResource):

    class CallSummariesAnsweredBy(object):
        UNKNOWN = "unknown"
        MACHINE_START = "machine_start"
        MACHINE_END_BEEP = "machine_end_beep"
        MACHINE_END_SILENCE = "machine_end_silence"
        MACHINE_END_OTHER = "machine_end_other"
        HUMAN = "human"
        FAX = "fax"

    class CallSummariesCallState(object):
        RINGING = "ringing"
        COMPLETED = "completed"
        BUSY = "busy"
        FAIL = "fail"
        NOANSWER = "noanswer"
        CANCELED = "canceled"
        ANSWERED = "answered"
        UNDIALED = "undialed"

    class CallSummariesCallType(object):
        CARRIER = "carrier"
        SIP = "sip"
        TRUNKING = "trunking"
        CLIENT = "client"

    class CallSummariesProcessingState(object):
        COMPLETE = "complete"
        PARTIAL = "partial"

    class CallSummariesProcessingStateRequest(object):
        COMPLETED = "completed"
        STARTED = "started"
        PARTIAL = "partial"
        ALL = "all"

    class CallSummariesSortBy(object):
        START_TIME = "start_time"
        END_TIME = "end_time"

    def __init__(self, version, payload):
        """
        Initialize the CallSummariesInstance
        :returns: twilio.rest.insights.v1.call_summaries.CallSummariesInstance
        :rtype: twilio.rest.insights.v1.call_summaries.CallSummariesInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'call_sid': payload.get('call_sid'),
            'answered_by': payload.get('answered_by'),
            'call_type': payload.get('call_type'),
            'call_state': payload.get('call_state'),
            'processing_state': payload.get('processing_state'),
            'created_time': deserialize.iso8601_datetime(payload.get('created_time')),
            'start_time': deserialize.iso8601_datetime(payload.get('start_time')),
            'end_time': deserialize.iso8601_datetime(payload.get('end_time')),
            'duration': deserialize.integer(payload.get('duration')),
            'connect_duration': deserialize.integer(payload.get('connect_duration')),
            '_from': payload.get('from'),
            'to': payload.get('to'),
            'carrier_edge': payload.get('carrier_edge'),
            'client_edge': payload.get('client_edge'),
            'sdk_edge': payload.get('sdk_edge'),
            'sip_edge': payload.get('sip_edge'),
            'tags': payload.get('tags'),
            'url': payload.get('url'),
            'attributes': payload.get('attributes'),
            'properties': payload.get('properties'),
            'trust': payload.get('trust'),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def call_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['call_sid']
    
    @property
    def answered_by(self):
        """
        :returns: 
        :rtype: CallSummariesAnsweredBy
        """
        return self._properties['answered_by']
    
    @property
    def call_type(self):
        """
        :returns: 
        :rtype: CallSummariesCallType
        """
        return self._properties['call_type']
    
    @property
    def call_state(self):
        """
        :returns: 
        :rtype: CallSummariesCallState
        """
        return self._properties['call_state']
    
    @property
    def processing_state(self):
        """
        :returns: 
        :rtype: CallSummariesProcessingState
        """
        return self._properties['processing_state']
    
    @property
    def created_time(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['created_time']
    
    @property
    def start_time(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['start_time']
    
    @property
    def end_time(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['end_time']
    
    @property
    def duration(self):
        """
        :returns: 
        :rtype: int
        """
        return self._properties['duration']
    
    @property
    def connect_duration(self):
        """
        :returns: 
        :rtype: int
        """
        return self._properties['connect_duration']
    
    @property
    def _from(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['_from']
    
    @property
    def to(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['to']
    
    @property
    def carrier_edge(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['carrier_edge']
    
    @property
    def client_edge(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['client_edge']
    
    @property
    def sdk_edge(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['sdk_edge']
    
    @property
    def sip_edge(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['sip_edge']
    
    @property
    def tags(self):
        """
        :returns: 
        :rtype: list[str]
        """
        return self._properties['tags']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def attributes(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['attributes']
    
    @property
    def properties(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['properties']
    
    @property
    def trust(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['trust']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.CallSummariesInstance {}>'.format(context)



