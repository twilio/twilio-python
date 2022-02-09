# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ConferenceParticipantList(ListResource):

    def __init__(self, version, conference_sid):
        """
        Initialize the ConferenceParticipantList

        :param Version version: Version that contains the resource
        :param conference_sid: Conference SID.

        :returns: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantList
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantList
        """
        super(ConferenceParticipantList, self).__init__(version)

        # Path Solution
        self._solution = {'conference_sid': conference_sid, }
        self._uri = '/Conferences/{conference_sid}/Participants'.format(**self._solution)

    def stream(self, participant_sid=values.unset, label=values.unset,
               events=values.unset, limit=None, page_size=None):
        """
        Streams ConferenceParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode participant_sid: Participant SID.
        :param unicode label: User-specified label for a participant.
        :param unicode events: Conference events generated by application or participant activity.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            participant_sid=participant_sid,
            label=label,
            events=events,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'])

    def list(self, participant_sid=values.unset, label=values.unset,
             events=values.unset, limit=None, page_size=None):
        """
        Lists ConferenceParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode participant_sid: Participant SID.
        :param unicode label: User-specified label for a participant.
        :param unicode events: Conference events generated by application or participant activity.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantInstance]
        """
        return list(self.stream(
            participant_sid=participant_sid,
            label=label,
            events=events,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, participant_sid=values.unset, label=values.unset,
             events=values.unset, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ConferenceParticipantInstance records from the API.
        Request is executed immediately

        :param unicode participant_sid: Participant SID.
        :param unicode label: User-specified label for a participant.
        :param unicode events: Conference events generated by application or participant activity.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConferenceParticipantInstance
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantPage
        """
        data = values.of({
            'ParticipantSid': participant_sid,
            'Label': label,
            'Events': events,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return ConferenceParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ConferenceParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ConferenceParticipantInstance
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ConferenceParticipantPage(self._version, response, self._solution)

    def get(self, participant_sid):
        """
        Constructs a ConferenceParticipantContext

        :param participant_sid: Participant SID.

        :returns: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantContext
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantContext
        """
        return ConferenceParticipantContext(
            self._version,
            conference_sid=self._solution['conference_sid'],
            participant_sid=participant_sid,
        )

    def __call__(self, participant_sid):
        """
        Constructs a ConferenceParticipantContext

        :param participant_sid: Participant SID.

        :returns: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantContext
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantContext
        """
        return ConferenceParticipantContext(
            self._version,
            conference_sid=self._solution['conference_sid'],
            participant_sid=participant_sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.ConferenceParticipantList>'


class ConferenceParticipantPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ConferenceParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param conference_sid: Conference SID.

        :returns: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantPage
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantPage
        """
        super(ConferenceParticipantPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConferenceParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantInstance
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantInstance
        """
        return ConferenceParticipantInstance(
            self._version,
            payload,
            conference_sid=self._solution['conference_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Insights.V1.ConferenceParticipantPage>'


class ConferenceParticipantContext(InstanceContext):

    def __init__(self, version, conference_sid, participant_sid):
        """
        Initialize the ConferenceParticipantContext

        :param Version version: Version that contains the resource
        :param conference_sid: Conference SID.
        :param participant_sid: Participant SID.

        :returns: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantContext
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantContext
        """
        super(ConferenceParticipantContext, self).__init__(version)

        # Path Solution
        self._solution = {'conference_sid': conference_sid, 'participant_sid': participant_sid, }
        self._uri = '/Conferences/{conference_sid}/Participants/{participant_sid}'.format(**self._solution)

    def fetch(self, events=values.unset, metrics=values.unset):
        """
        Fetch the ConferenceParticipantInstance

        :param unicode events: Conference events generated by application or participant activity.
        :param unicode metrics: Object. Contains call quality metrics.

        :returns: The fetched ConferenceParticipantInstance
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantInstance
        """
        data = values.of({'Events': events, 'Metrics': metrics, })

        payload = self._version.fetch(method='GET', uri=self._uri, params=data, )

        return ConferenceParticipantInstance(
            self._version,
            payload,
            conference_sid=self._solution['conference_sid'],
            participant_sid=self._solution['participant_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.ConferenceParticipantContext {}>'.format(context)


class ConferenceParticipantInstance(InstanceResource):

    class CallDirection(object):
        INBOUND = "inbound"
        OUTBOUND = "outbound"

    class CallStatus(object):
        ANSWERED = "answered"
        COMPLETED = "completed"
        BUSY = "busy"
        FAIL = "fail"
        NOANSWER = "noanswer"
        RINGING = "ringing"
        CANCELED = "canceled"

    class JitterBufferSize(object):
        LARGE = "large"
        SMALL = "small"
        MEDIUM = "medium"
        OFF = "off"

    class Region(object):
        US1 = "us1"
        US2 = "us2"
        AU1 = "au1"
        BR1 = "br1"
        IE1 = "ie1"
        JP1 = "jp1"
        SG1 = "sg1"
        DE1 = "de1"

    class CallType(object):
        CARRIER = "carrier"
        CLIENT = "client"
        SIP = "sip"

    class ProcessingState(object):
        COMPLETE = "complete"
        IN_PROGRESS = "in_progress"
        TIMEOUT = "timeout"

    def __init__(self, version, payload, conference_sid, participant_sid=None):
        """
        Initialize the ConferenceParticipantInstance

        :returns: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantInstance
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantInstance
        """
        super(ConferenceParticipantInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'participant_sid': payload.get('participant_sid'),
            'label': payload.get('label'),
            'conference_sid': payload.get('conference_sid'),
            'call_sid': payload.get('call_sid'),
            'account_sid': payload.get('account_sid'),
            'call_direction': payload.get('call_direction'),
            'from_': payload.get('from'),
            'to': payload.get('to'),
            'call_status': payload.get('call_status'),
            'country_code': payload.get('country_code'),
            'is_moderator': payload.get('is_moderator'),
            'join_time': deserialize.iso8601_datetime(payload.get('join_time')),
            'leave_time': deserialize.iso8601_datetime(payload.get('leave_time')),
            'duration_seconds': deserialize.integer(payload.get('duration_seconds')),
            'outbound_queue_length': deserialize.integer(payload.get('outbound_queue_length')),
            'outbound_time_in_queue': deserialize.integer(payload.get('outbound_time_in_queue')),
            'jitter_buffer_size': payload.get('jitter_buffer_size'),
            'is_coach': payload.get('is_coach'),
            'coached_participants': payload.get('coached_participants'),
            'participant_region': payload.get('participant_region'),
            'conference_region': payload.get('conference_region'),
            'call_type': payload.get('call_type'),
            'processing_state': payload.get('processing_state'),
            'properties': payload.get('properties'),
            'events': payload.get('events'),
            'metrics': payload.get('metrics'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'conference_sid': conference_sid,
            'participant_sid': participant_sid or self._properties['participant_sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ConferenceParticipantContext for this ConferenceParticipantInstance
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantContext
        """
        if self._context is None:
            self._context = ConferenceParticipantContext(
                self._version,
                conference_sid=self._solution['conference_sid'],
                participant_sid=self._solution['participant_sid'],
            )
        return self._context

    @property
    def participant_sid(self):
        """
        :returns: SID for this participant.
        :rtype: unicode
        """
        return self._properties['participant_sid']

    @property
    def label(self):
        """
        :returns: The user-specified label of this participant.
        :rtype: unicode
        """
        return self._properties['label']

    @property
    def conference_sid(self):
        """
        :returns: Conference SID.
        :rtype: unicode
        """
        return self._properties['conference_sid']

    @property
    def call_sid(self):
        """
        :returns: Unique SID identifier of the call.
        :rtype: unicode
        """
        return self._properties['call_sid']

    @property
    def account_sid(self):
        """
        :returns: Account SID.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def call_direction(self):
        """
        :returns: Call direction of the participant.
        :rtype: ConferenceParticipantInstance.CallDirection
        """
        return self._properties['call_direction']

    @property
    def from_(self):
        """
        :returns: Caller ID of the calling party.
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def to(self):
        """
        :returns: Called party.
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def call_status(self):
        """
        :returns: Call status of the call that generated the participant.
        :rtype: ConferenceParticipantInstance.CallStatus
        """
        return self._properties['call_status']

    @property
    def country_code(self):
        """
        :returns: ISO alpha-2 country code of the participant.
        :rtype: unicode
        """
        return self._properties['country_code']

    @property
    def is_moderator(self):
        """
        :returns: Boolean. Indicates whether participant had startConferenceOnEnter=true or endConferenceOnExit=true.
        :rtype: bool
        """
        return self._properties['is_moderator']

    @property
    def join_time(self):
        """
        :returns: ISO 8601 timestamp of participant join event.
        :rtype: datetime
        """
        return self._properties['join_time']

    @property
    def leave_time(self):
        """
        :returns: ISO 8601 timestamp of participant leave event.
        :rtype: datetime
        """
        return self._properties['leave_time']

    @property
    def duration_seconds(self):
        """
        :returns: Participant durations in seconds.
        :rtype: unicode
        """
        return self._properties['duration_seconds']

    @property
    def outbound_queue_length(self):
        """
        :returns: Estimated time in queue at call creation.
        :rtype: unicode
        """
        return self._properties['outbound_queue_length']

    @property
    def outbound_time_in_queue(self):
        """
        :returns: Actual time in queue (seconds).
        :rtype: unicode
        """
        return self._properties['outbound_time_in_queue']

    @property
    def jitter_buffer_size(self):
        """
        :returns: The Jitter Buffer Size of this Conference Participant.
        :rtype: ConferenceParticipantInstance.JitterBufferSize
        """
        return self._properties['jitter_buffer_size']

    @property
    def is_coach(self):
        """
        :returns: Boolean. Indicated whether participant was a coach.
        :rtype: bool
        """
        return self._properties['is_coach']

    @property
    def coached_participants(self):
        """
        :returns: Call SIDs coached by this participant.
        :rtype: list[unicode]
        """
        return self._properties['coached_participants']

    @property
    def participant_region(self):
        """
        :returns: Twilio region where the participant media originates.
        :rtype: ConferenceParticipantInstance.Region
        """
        return self._properties['participant_region']

    @property
    def conference_region(self):
        """
        :returns: The Conference Region of this Conference Participant.
        :rtype: ConferenceParticipantInstance.Region
        """
        return self._properties['conference_region']

    @property
    def call_type(self):
        """
        :returns: The Call Type of this Conference Participant.
        :rtype: ConferenceParticipantInstance.CallType
        """
        return self._properties['call_type']

    @property
    def processing_state(self):
        """
        :returns: Processing state of the Participant Summary.
        :rtype: ConferenceParticipantInstance.ProcessingState
        """
        return self._properties['processing_state']

    @property
    def properties(self):
        """
        :returns: Participant properties and metadata.
        :rtype: dict
        """
        return self._properties['properties']

    @property
    def events(self):
        """
        :returns: Object containing information of actions taken by participants. Nested resource URLs.
        :rtype: dict
        """
        return self._properties['events']

    @property
    def metrics(self):
        """
        :returns: Object. Contains participant quality metrics.
        :rtype: dict
        """
        return self._properties['metrics']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, events=values.unset, metrics=values.unset):
        """
        Fetch the ConferenceParticipantInstance

        :param unicode events: Conference events generated by application or participant activity.
        :param unicode metrics: Object. Contains call quality metrics.

        :returns: The fetched ConferenceParticipantInstance
        :rtype: twilio.rest.insights.v1.conference.conference_participant.ConferenceParticipantInstance
        """
        return self._proxy.fetch(events=events, metrics=metrics, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Insights.V1.ConferenceParticipantInstance {}>'.format(context)
