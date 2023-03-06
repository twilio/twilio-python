"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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



class NotificationList(ListResource):

    def __init__(self, version: Version, service_sid: str, identity: str, challenge_sid: str):
        """
        Initialize the NotificationList

        :param Version version: Version that contains the resource
        :param service_sid: The unique SID identifier of the Service.
        :param identity: Customer unique identity for the Entity owner of the Challenge. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        :param challenge_sid: The unique SID identifier of the Challenge.
        
        :returns: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationList
        :rtype: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'identity': identity, 'challenge_sid': challenge_sid,  }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Challenges/{challenge_sid}/Notifications'.format(**self._solution)
        
        
    
    def create(self, ttl=values.unset):
        """
        Create the NotificationInstance

        :param int ttl: How long, in seconds, the notification is valid. Can be an integer between 0 and 300. Default is 300. Delivery is attempted until the TTL elapses, even if the device is offline. 0 means that the notification delivery is attempted immediately, only once, and is not stored for future delivery.
        
        :returns: The created NotificationInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationInstance
        """
        data = values.of({ 
            'Ttl': ttl,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return NotificationInstance(self._version, payload, service_sid=self._solution['service_sid'], identity=self._solution['identity'], challenge_sid=self._solution['challenge_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.NotificationList>'


class NotificationInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, identity: str, challenge_sid: str):
        """
        Initialize the NotificationInstance
        :returns: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationInstance
        :rtype: twilio.rest.verify.v2.service.entity.challenge.notification.NotificationInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'entity_sid': payload.get('entity_sid'),
            'identity': payload.get('identity'),
            'challenge_sid': payload.get('challenge_sid'),
            'priority': payload.get('priority'),
            'ttl': deserialize.integer(payload.get('ttl')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'identity': identity, 'challenge_sid': challenge_sid,  }
    
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this Notification.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The unique SID identifier of the Account.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The unique SID identifier of the Service.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def entity_sid(self):
        """
        :returns: The unique SID identifier of the Entity.
        :rtype: str
        """
        return self._properties['entity_sid']
    
    @property
    def identity(self):
        """
        :returns: Customer unique identity for the Entity owner of the Challenge. This identifier should be immutable, not PII, length between 8 and 64 characters, and generated by your external system, such as your user's UUID, GUID, or SID. It can only contain dash (-) separated alphanumeric characters.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def challenge_sid(self):
        """
        :returns: The unique SID identifier of the Challenge.
        :rtype: str
        """
        return self._properties['challenge_sid']
    
    @property
    def priority(self):
        """
        :returns: The priority of the notification. For `push` Challenges it's always `high` which sends the notification immediately, and can wake up a sleeping device.
        :rtype: str
        """
        return self._properties['priority']
    
    @property
    def ttl(self):
        """
        :returns: How long, in seconds, the notification is valid. Max: 5 minutes
        :rtype: int
        """
        return self._properties['ttl']
    
    @property
    def date_created(self):
        """
        :returns: The date that this Notification was created, given in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
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
        return '<Twilio.Verify.V2.NotificationInstance {}>'.format(context)


