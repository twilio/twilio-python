"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
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



class FlowValidateList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the FlowValidateList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.studio.v2.flow_validate.FlowValidateList
        :rtype: twilio.rest.studio.v2.flow_validate.FlowValidateList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Flows/Validate'.format(**self._solution)
        
        
    
    def update(self, friendly_name, status, definition, commit_message=values.unset):
        """
        Update the FlowValidateInstance

        :param str friendly_name: The string that you assigned to describe the Flow.
        :param FlowValidateInstance.Status status: 
        :param object definition: JSON representation of flow definition.
        :param str commit_message: Description of change made in the revision.
        
        :returns: The created FlowValidateInstance
        :rtype: twilio.rest.studio.v2.flow_validate.FlowValidateInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Status': status,
            'Definition': serialize.object(definition),
            'CommitMessage': commit_message,
        })
        
        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return FlowValidateInstance(self._version, payload)
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.FlowValidateList>'

class FlowValidateInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the FlowValidateInstance
        :returns: twilio.rest.studio.v2.flow_validate.FlowValidateInstance
        :rtype: twilio.rest.studio.v2.flow_validate.FlowValidateInstance
        """
        super().__init__(version)

        self._properties = { 
            'valid': payload.get('valid'),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def valid(self):
        """
        :returns: Boolean if the flow definition is valid.
        :rtype: bool
        """
        return self._properties['valid']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V2.FlowValidateInstance {}>'.format(context)



