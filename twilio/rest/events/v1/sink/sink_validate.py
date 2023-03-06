"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
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



class SinkValidateList(ListResource):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the SinkValidateList

        :param Version version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies the Sink being validated.
        
        :returns: twilio.rest.events.v1.sink.sink_validate.SinkValidateList
        :rtype: twilio.rest.events.v1.sink.sink_validate.SinkValidateList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Sinks/{sid}/Validate'.format(**self._solution)
        
        
    
    def create(self, test_id):
        """
        Create the SinkValidateInstance

        :param str test_id: A 34 character string that uniquely identifies the test event for a Sink being validated.
        
        :returns: The created SinkValidateInstance
        :rtype: twilio.rest.events.v1.sink.sink_validate.SinkValidateInstance
        """
        data = values.of({ 
            'TestId': test_id,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SinkValidateInstance(self._version, payload, sid=self._solution['sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SinkValidateList>'


class SinkValidateInstance(InstanceResource):

    def __init__(self, version, payload, sid: str):
        """
        Initialize the SinkValidateInstance
        :returns: twilio.rest.events.v1.sink.sink_validate.SinkValidateInstance
        :rtype: twilio.rest.events.v1.sink.sink_validate.SinkValidateInstance
        """
        super().__init__(version)

        self._properties = { 
            'result': payload.get('result'),
        }

        self._context = None
        self._solution = { 'sid': sid,  }
    
    
    @property
    def result(self):
        """
        :returns: Feedback indicating whether the given Sink was validated.
        :rtype: str
        """
        return self._properties['result']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SinkValidateInstance {}>'.format(context)


