"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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



class InsightsSegmentsList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsSegmentsList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsList
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self, segment_id):
        """
        Constructs a InsightsSegmentsContext
        
        :param segment_id: To unique id of the segment
        
        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        """
        return InsightsSegmentsContext(self._version, segment_id=segment_id)

    def __call__(self, segment_id):
        """
        Constructs a InsightsSegmentsContext
        
        :param segment_id: To unique id of the segment
        
        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        """
        return InsightsSegmentsContext(self._version, segment_id=segment_id)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsSegmentsList>'

class InsightsSegmentsInstance(InstanceResource):

    def __init__(self, version, payload, segment_id: str=None):
        """
        Initialize the InsightsSegmentsInstance
        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """
        super().__init__(version)

        self._properties = { 
            'segment_id': payload.get('segment_id'),
            'external_id': payload.get('external_id'),
            'queue': payload.get('queue'),
            'external_contact': payload.get('external_contact'),
            'external_segment_link_id': payload.get('external_segment_link_id'),
            'date': payload.get('date'),
            'account_id': payload.get('account_id'),
            'external_segment_link': payload.get('external_segment_link'),
            'agent_id': payload.get('agent_id'),
            'agent_phone': payload.get('agent_phone'),
            'agent_name': payload.get('agent_name'),
            'agent_team_name': payload.get('agent_team_name'),
            'agent_team_name_in_hierarchy': payload.get('agent_team_name_in_hierarchy'),
            'agent_link': payload.get('agent_link'),
            'customer_phone': payload.get('customer_phone'),
            'customer_name': payload.get('customer_name'),
            'customer_link': payload.get('customer_link'),
            'segment_recording_offset': payload.get('segment_recording_offset'),
            'media': payload.get('media'),
            'assessment_type': payload.get('assessment_type'),
            'assessment_percentage': payload.get('assessment_percentage'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'segment_id': segment_id or self._properties['segment_id'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsSegmentsContext for this InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        """
        if self._context is None:
            self._context = InsightsSegmentsContext(self._version, segment_id=self._solution['segment_id'],)
        return self._context
    
    @property
    def segment_id(self):
        """
        :returns: To unique id of the segment
        :rtype: str
        """
        return self._properties['segment_id']
    
    @property
    def external_id(self):
        """
        :returns: The unique id for the conversation.
        :rtype: str
        """
        return self._properties['external_id']
    
    @property
    def queue(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['queue']
    
    @property
    def external_contact(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['external_contact']
    
    @property
    def external_segment_link_id(self):
        """
        :returns: The uuid for the external_segment_link.
        :rtype: str
        """
        return self._properties['external_segment_link_id']
    
    @property
    def date(self):
        """
        :returns: The date of the conversation.
        :rtype: str
        """
        return self._properties['date']
    
    @property
    def account_id(self):
        """
        :returns: The unique id for the account.
        :rtype: str
        """
        return self._properties['account_id']
    
    @property
    def external_segment_link(self):
        """
        :returns: The hyperlink to recording of the task event.
        :rtype: str
        """
        return self._properties['external_segment_link']
    
    @property
    def agent_id(self):
        """
        :returns: The unique id for the agent.
        :rtype: str
        """
        return self._properties['agent_id']
    
    @property
    def agent_phone(self):
        """
        :returns: The phone number of the agent.
        :rtype: str
        """
        return self._properties['agent_phone']
    
    @property
    def agent_name(self):
        """
        :returns: The name of the agent.
        :rtype: str
        """
        return self._properties['agent_name']
    
    @property
    def agent_team_name(self):
        """
        :returns: The team name to which agent belongs.
        :rtype: str
        """
        return self._properties['agent_team_name']
    
    @property
    def agent_team_name_in_hierarchy(self):
        """
        :returns: he team name to which agent belongs.
        :rtype: str
        """
        return self._properties['agent_team_name_in_hierarchy']
    
    @property
    def agent_link(self):
        """
        :returns: The link to the agent conversation.
        :rtype: str
        """
        return self._properties['agent_link']
    
    @property
    def customer_phone(self):
        """
        :returns: The phone number of the customer.
        :rtype: str
        """
        return self._properties['customer_phone']
    
    @property
    def customer_name(self):
        """
        :returns: The name of the customer.
        :rtype: str
        """
        return self._properties['customer_name']
    
    @property
    def customer_link(self):
        """
        :returns: The link to the customer conversation.
        :rtype: str
        """
        return self._properties['customer_link']
    
    @property
    def segment_recording_offset(self):
        """
        :returns: The offset value for the recording.
        :rtype: str
        """
        return self._properties['segment_recording_offset']
    
    @property
    def media(self):
        """
        :returns: The link for the conversation.
        :rtype: str
        """
        return self._properties['media']
    
    @property
    def assessment_type(self):
        """
        :returns: The type of the assessment.
        :rtype: dict
        """
        return self._properties['assessment_type']
    
    @property
    def assessment_percentage(self):
        """
        :returns: The percentage scored on the Assessments.
        :rtype: dict
        """
        return self._properties['assessment_percentage']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self, token=values.unset):
        """
        Fetch the InsightsSegmentsInstance
        
        :params str token: The Token HTTP request header

        :returns: The fetched InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """
        return self._proxy.fetch(token=token, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsSegmentsInstance {}>'.format(context)

class InsightsSegmentsContext(InstanceContext):

    def __init__(self, version: Version, segment_id: str):
        """
        Initialize the InsightsSegmentsContext

        :param Version version: Version that contains the resource
        :param segment_id: To unique id of the segment

        :returns: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'segment_id': segment_id,
        }
        self._uri = '/Insights/Segments/{segment_id}'.format(**self._solution)
        
    
    def fetch(self, token=values.unset):
        """
        Fetch the InsightsSegmentsInstance
        
        :params str token: The Token HTTP request header

        :returns: The fetched InsightsSegmentsInstance
        :rtype: twilio.rest.flex_api.v1.insights_segments.InsightsSegmentsInstance
        """
        
        data = values.of({ 
            'Token': token,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return InsightsSegmentsInstance(
            self._version,
            payload,
            segment_id=self._solution['segment_id'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsSegmentsContext {}>'.format(context)


