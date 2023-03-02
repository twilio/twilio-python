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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class MetricList(ListResource):

    def __init__(self, version: Version, call_sid: str):
        """
        Initialize the MetricList

        :param Version version: Version that contains the resource
        :param call_sid: 
        
        :returns: twilio.rest.insights.v1.call.metric.MetricList
        :rtype: twilio.rest.insights.v1.call.metric.MetricList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'call_sid': call_sid,  }
        self._uri = '/Voice/{call_sid}/Metrics'.format(**self._solution)
        
        
    
    def stream(self, edge=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Streams MetricInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param TwilioEdge edge: 
        :param StreamDirection direction: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call.metric.MetricInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            edge=edge,
            direction=direction,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, edge=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Lists MetricInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param TwilioEdge edge: 
        :param StreamDirection direction: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.call.metric.MetricInstance]
        """
        return list(self.stream(
            edge=edge,
            direction=direction,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, edge=values.unset, direction=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MetricInstance records from the API.
        Request is executed immediately
        
        :param TwilioEdge edge: 
        :param StreamDirection direction: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MetricInstance
        :rtype: twilio.rest.insights.v1.call.metric.MetricPage
        """
        data = values.of({ 
            'Edge': edge,
            'Direction': direction,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MetricPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MetricInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MetricInstance
        :rtype: twilio.rest.insights.v1.call.metric.MetricPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MetricPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.MetricList>'


class MetricPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MetricPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.insights.v1.call.metric.MetricPage
        :rtype: twilio.rest.insights.v1.call.metric.MetricPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MetricInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.call.metric.MetricInstance
        :rtype: twilio.rest.insights.v1.call.metric.MetricInstance
        """
        return MetricInstance(self._version, payload, call_sid=self._solution['call_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.MetricPage>'





class MetricInstance(InstanceResource):

    class StreamDirection(object):
        UNKNOWN = "unknown"
        INBOUND = "inbound"
        OUTBOUND = "outbound"
        BOTH = "both"

    class TwilioEdge(object):
        UNKNOWN_EDGE = "unknown_edge"
        CARRIER_EDGE = "carrier_edge"
        SIP_EDGE = "sip_edge"
        SDK_EDGE = "sdk_edge"
        CLIENT_EDGE = "client_edge"

    def __init__(self, version, payload, call_sid: str):
        """
        Initialize the MetricInstance
        :returns: twilio.rest.insights.v1.call.metric.MetricInstance
        :rtype: twilio.rest.insights.v1.call.metric.MetricInstance
        """
        super().__init__(version)

        self._properties = { 
            'timestamp': payload.get('timestamp'),
            'call_sid': payload.get('call_sid'),
            'account_sid': payload.get('account_sid'),
            'edge': payload.get('edge'),
            'direction': payload.get('direction'),
            'carrier_edge': payload.get('carrier_edge'),
            'sip_edge': payload.get('sip_edge'),
            'sdk_edge': payload.get('sdk_edge'),
            'client_edge': payload.get('client_edge'),
        }

        self._context = None
        self._solution = { 'call_sid': call_sid,  }
    
    
    @property
    def timestamp(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['timestamp']
    
    @property
    def call_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['call_sid']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def edge(self):
        """
        :returns: 
        :rtype: TwilioEdge
        """
        return self._properties['edge']
    
    @property
    def direction(self):
        """
        :returns: 
        :rtype: StreamDirection
        """
        return self._properties['direction']
    
    @property
    def carrier_edge(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['carrier_edge']
    
    @property
    def sip_edge(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['sip_edge']
    
    @property
    def sdk_edge(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['sdk_edge']
    
    @property
    def client_edge(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['client_edge']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.MetricInstance {}>'.format(context)


