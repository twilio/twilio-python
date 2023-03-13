"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class AnonymizeList(ListResource):

    def __init__(self, version: Version, room_sid: str, sid: str):
        """
        Initialize the AnonymizeList

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the room with the participant to update.
        :param sid: The SID of the RoomParticipant resource to update.
        
        :returns: twilio.rest.video.v1.room.participant.anonymize.AnonymizeList
        :rtype: twilio.rest.video.v1.room.participant.anonymize.AnonymizeList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid, 'sid': sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a AnonymizeContext
        
        :returns: twilio.rest.video.v1.room.participant.anonymize.AnonymizeContext
        :rtype: twilio.rest.video.v1.room.participant.anonymize.AnonymizeContext
        """
        return AnonymizeContext(self._version, room_sid=self._solution['room_sid'], sid=self._solution['sid'])

    def __call__(self):
        """
        Constructs a AnonymizeContext
        
        :returns: twilio.rest.video.v1.room.participant.anonymize.AnonymizeContext
        :rtype: twilio.rest.video.v1.room.participant.anonymize.AnonymizeContext
        """
        return AnonymizeContext(self._version, room_sid=self._solution['room_sid'], sid=self._solution['sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.AnonymizeList>'

class AnonymizeInstance(InstanceResource):

    class Status(object):
        CONNECTED = "connected"
        DISCONNECTED = "disconnected"

    def __init__(self, version, payload, room_sid: str, sid: str):
        """
        Initialize the AnonymizeInstance
        :returns: twilio.rest.video.v1.room.participant.anonymize.AnonymizeInstance
        :rtype: twilio.rest.video.v1.room.participant.anonymize.AnonymizeInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'room_sid': payload.get('room_sid'),
            'account_sid': payload.get('account_sid'),
            'status': payload.get('status'),
            'identity': payload.get('identity'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'start_time': deserialize.iso8601_datetime(payload.get('start_time')),
            'end_time': deserialize.iso8601_datetime(payload.get('end_time')),
            'duration': deserialize.integer(payload.get('duration')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'room_sid': room_sid, 'sid': sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AnonymizeContext for this AnonymizeInstance
        :rtype: twilio.rest.video.v1.room.participant.anonymize.AnonymizeContext
        """
        if self._context is None:
            self._context = AnonymizeContext(self._version, room_sid=self._solution['room_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the RoomParticipant resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def room_sid(self):
        """
        :returns: The SID of the participant's room.
        :rtype: str
        """
        return self._properties['room_sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the RoomParticipant resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: AnonymizeInstance.Status
        """
        return self._properties['status']
    
    @property
    def identity(self):
        """
        :returns: The SID of the participant.
        :rtype: str
        """
        return self._properties['identity']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def start_time(self):
        """
        :returns: The time of participant connected to the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :rtype: datetime
        """
        return self._properties['start_time']
    
    @property
    def end_time(self):
        """
        :returns: The time when the participant disconnected from the room in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
        :rtype: datetime
        """
        return self._properties['end_time']
    
    @property
    def duration(self):
        """
        :returns: The duration in seconds that the participant was `connected`. Populated only after the participant is `disconnected`.
        :rtype: int
        """
        return self._properties['duration']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def update(self):
        """
        Update the AnonymizeInstance
        

        :returns: The updated AnonymizeInstance
        :rtype: twilio.rest.video.v1.room.participant.anonymize.AnonymizeInstance
        """
        return self._proxy.update()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.AnonymizeInstance {}>'.format(context)

class AnonymizeContext(InstanceContext):

    def __init__(self, version: Version, room_sid: str, sid: str):
        """
        Initialize the AnonymizeContext

        :param Version version: Version that contains the resource
        :param room_sid: The SID of the room with the participant to update.
        :param sid: The SID of the RoomParticipant resource to update.

        :returns: twilio.rest.video.v1.room.participant.anonymize.AnonymizeContext
        :rtype: twilio.rest.video.v1.room.participant.anonymize.AnonymizeContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'room_sid': room_sid,
            'sid': sid,
        }
        self._uri = '/Rooms/{room_sid}/Participants/{sid}/Anonymize'.format(**self._solution)
        
    
    def update(self):
        """
        Update the AnonymizeInstance
        

        :returns: The updated AnonymizeInstance
        :rtype: twilio.rest.video.v1.room.participant.anonymize.AnonymizeInstance
        """
        data = values.of({ 
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return AnonymizeInstance(
            self._version,
            payload,
            room_sid=self._solution['room_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Video.V1.AnonymizeContext {}>'.format(context)


