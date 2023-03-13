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


from datetime import date
from twilio.base import deserialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class ExternalCampaignList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ExternalCampaignList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.messaging.v1.external_campaign.ExternalCampaignList
        :rtype: twilio.rest.messaging.v1.external_campaign.ExternalCampaignList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Services/PreregisteredUsa2p'.format(**self._solution)
        
        
    
    def create(self, campaign_id, messaging_service_sid):
        """
        Create the ExternalCampaignInstance

        :param str campaign_id: ID of the preregistered campaign.
        :param str messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.
        
        :returns: The created ExternalCampaignInstance
        :rtype: twilio.rest.messaging.v1.external_campaign.ExternalCampaignInstance
        """
        data = values.of({ 
            'CampaignId': campaign_id,
            'MessagingServiceSid': messaging_service_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ExternalCampaignInstance(self._version, payload)
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.ExternalCampaignList>'

class ExternalCampaignInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the ExternalCampaignInstance
        :returns: twilio.rest.messaging.v1.external_campaign.ExternalCampaignInstance
        :rtype: twilio.rest.messaging.v1.external_campaign.ExternalCampaignInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'campaign_id': payload.get('campaign_id'),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def sid(self):
        """
        :returns: The unique string that identifies a US A2P Compliance resource `QE2c6890da8086d771620e9b13fadeba0b`.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Campaign belongs to.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def campaign_id(self):
        """
        :returns: ID of the preregistered campaign.
        :rtype: str
        """
        return self._properties['campaign_id']
    
    @property
    def messaging_service_sid(self):
        """
        :returns: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.
        :rtype: str
        """
        return self._properties['messaging_service_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.ExternalCampaignInstance {}>'.format(context)



