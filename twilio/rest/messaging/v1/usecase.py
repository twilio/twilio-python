"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
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



class UsecaseList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the UsecaseList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.messaging.v1.usecase.UsecaseList
        :rtype: twilio.rest.messaging.v1.usecase.UsecaseList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services/Usecases'.format(**self._solution)
        
        
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UsecaseList>'


class UsecaseInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the UsecaseInstance
        :returns: twilio.rest.messaging.v1.usecase.UsecaseInstance
        :rtype: twilio.rest.messaging.v1.usecase.UsecaseInstance
        """
        super().__init__(version)

        self._properties = { 
            'usecases': payload.get('usecases'),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def usecases(self):
        """
        :returns: Human readable use case details (usecase, description and purpose) of Messaging Service Use Cases.
        :rtype: list[object]
        """
        return self._properties['usecases']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.UsecaseInstance {}>'.format(context)


