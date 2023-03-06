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
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.insights.v1.call.annotation import AnnotationList
from twilio.rest.insights.v1.call.call_summary import CallSummaryList
from twilio.rest.insights.v1.call.event import EventList
from twilio.rest.insights.v1.call.metric import MetricList


class CallList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CallList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.insights.v1.call.CallList
        :rtype: twilio.rest.insights.v1.call.CallList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    def fetch(self):
        """
        Fetch the CallInstance

        :returns: The fetched CallInstance
        :rtype: twilio.rest.insights.v1.call.CallInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return CallInstance(self._version, payload)
    

    def get(self, sid):
        """
        Constructs a CallContext
        
        :param sid: 
        
        :returns: twilio.rest.insights.v1.call.CallContext
        :rtype: twilio.rest.insights.v1.call.CallContext
        """
        return CallContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a CallContext
        
        :param sid: 
        
        :returns: twilio.rest.insights.v1.call.CallContext
        :rtype: twilio.rest.insights.v1.call.CallContext
        """
        return CallContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.CallList>'

class CallInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the CallInstance
        :returns: twilio.rest.insights.v1.call.CallInstance
        :rtype: twilio.rest.insights.v1.call.CallInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CallContext for this CallInstance
        :rtype: twilio.rest.insights.v1.call.CallContext
        """
        if self._context is None:
            self._context = CallContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    def fetch(self):
        """
        Fetch the CallInstance
        

        :returns: The fetched CallInstance
        :rtype: twilio.rest.insights.v1.call.CallInstance
        """
        return self._proxy.fetch()
    
    @property
    def annotation(self):
        """
        Access the annotation

        :returns: twilio.rest.insights.v1.call.AnnotationList
        :rtype: twilio.rest.insights.v1.call.AnnotationList
        """
        return self._proxy.annotation
    
    @property
    def summary(self):
        """
        Access the summary

        :returns: twilio.rest.insights.v1.call.CallSummaryList
        :rtype: twilio.rest.insights.v1.call.CallSummaryList
        """
        return self._proxy.summary
    
    @property
    def events(self):
        """
        Access the events

        :returns: twilio.rest.insights.v1.call.EventList
        :rtype: twilio.rest.insights.v1.call.EventList
        """
        return self._proxy.events
    
    @property
    def metrics(self):
        """
        Access the metrics

        :returns: twilio.rest.insights.v1.call.MetricList
        :rtype: twilio.rest.insights.v1.call.MetricList
        """
        return self._proxy.metrics
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.CallInstance {}>'.format(context)

class CallContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the CallContext

        :param Version version: Version that contains the resource
        :param sid: 

        :returns: twilio.rest.insights.v1.call.CallContext
        :rtype: twilio.rest.insights.v1.call.CallContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Voice/{sid}'.format(**self._solution)
        
        self._annotation = None
        self._summary = None
        self._events = None
        self._metrics = None
    
    def fetch(self):
        """
        Fetch the CallInstance
        

        :returns: The fetched CallInstance
        :rtype: twilio.rest.insights.v1.call.CallInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CallInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    
    @property
    def annotation(self):
        """
        Access the annotation

        :returns: twilio.rest.insights.v1.call.AnnotationList
        :rtype: twilio.rest.insights.v1.call.AnnotationList
        """
        if self._annotation is None:
            self._annotation = AnnotationList(self._version, self._solution['sid'],
            )
        return self._annotation
    
    @property
    def summary(self):
        """
        Access the summary

        :returns: twilio.rest.insights.v1.call.CallSummaryList
        :rtype: twilio.rest.insights.v1.call.CallSummaryList
        """
        if self._summary is None:
            self._summary = CallSummaryList(self._version, self._solution['sid'],
            )
        return self._summary
    
    @property
    def events(self):
        """
        Access the events

        :returns: twilio.rest.insights.v1.call.EventList
        :rtype: twilio.rest.insights.v1.call.EventList
        """
        if self._events is None:
            self._events = EventList(self._version, self._solution['sid'],
            )
        return self._events
    
    @property
    def metrics(self):
        """
        Access the metrics

        :returns: twilio.rest.insights.v1.call.MetricList
        :rtype: twilio.rest.insights.v1.call.MetricList
        """
        if self._metrics is None:
            self._metrics = MetricList(self._version, self._solution['sid'],
            )
        return self._metrics
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.CallContext {}>'.format(context)


