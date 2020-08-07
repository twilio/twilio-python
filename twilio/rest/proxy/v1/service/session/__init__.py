# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.proxy.v1.service.session.interaction import InteractionList
from twilio.rest.proxy.v1.service.session.participant import ParticipantList


class SessionList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the SessionList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the resource's parent Service

        :returns: twilio.rest.proxy.v1.service.session.SessionList
        :rtype: twilio.rest.proxy.v1.service.session.SessionList
        """
        super(SessionList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, }
        self._uri = '/Services/{service_sid}/Sessions'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams SessionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.session.SessionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SessionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.session.SessionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SessionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return SessionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SessionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SessionPage(self._version, response, self._solution)

    def create(self, unique_name=values.unset, date_expiry=values.unset,
               ttl=values.unset, mode=values.unset, status=values.unset,
               participants=values.unset):
        """
        Create the SessionInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param datetime date_expiry: The ISO 8601 date when the Session should expire
        :param unicode ttl: When the session will expire
        :param SessionInstance.Mode mode: The Mode of the Session
        :param SessionInstance.Status status: Session status
        :param dict participants: The Participant objects to include in the new session

        :returns: The created SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'DateExpiry': serialize.iso8601_datetime(date_expiry),
            'Ttl': ttl,
            'Mode': mode,
            'Status': status,
            'Participants': serialize.map(participants, lambda e: serialize.object(e)),
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return SessionInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def get(self, sid):
        """
        Constructs a SessionContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.proxy.v1.service.session.SessionContext
        :rtype: twilio.rest.proxy.v1.service.session.SessionContext
        """
        return SessionContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a SessionContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.proxy.v1.service.session.SessionContext
        :rtype: twilio.rest.proxy.v1.service.session.SessionContext
        """
        return SessionContext(self._version, service_sid=self._solution['service_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.SessionList>'


class SessionPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the SessionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the resource's parent Service

        :returns: twilio.rest.proxy.v1.service.session.SessionPage
        :rtype: twilio.rest.proxy.v1.service.session.SessionPage
        """
        super(SessionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SessionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.proxy.v1.service.session.SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionInstance
        """
        return SessionInstance(self._version, payload, service_sid=self._solution['service_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.SessionPage>'


class SessionContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the SessionContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the resource from
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.proxy.v1.service.session.SessionContext
        :rtype: twilio.rest.proxy.v1.service.session.SessionContext
        """
        super(SessionContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Sessions/{sid}'.format(**self._solution)

        # Dependents
        self._interactions = None
        self._participants = None

    def fetch(self):
        """
        Fetch the SessionInstance

        :returns: The fetched SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SessionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the SessionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def update(self, date_expiry=values.unset, ttl=values.unset,
               status=values.unset, fail_on_participant_conflict=values.unset):
        """
        Update the SessionInstance

        :param datetime date_expiry: The ISO 8601 date when the Session should expire
        :param unicode ttl: When the session will expire
        :param SessionInstance.Status status: The new status of the resource
        :param bool fail_on_participant_conflict: Opt-in to enable Proxy to return 400 on detected conflict on re-open request.

        :returns: The updated SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionInstance
        """
        data = values.of({
            'DateExpiry': serialize.iso8601_datetime(date_expiry),
            'Ttl': ttl,
            'Status': status,
            'FailOnParticipantConflict': fail_on_participant_conflict,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return SessionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    @property
    def interactions(self):
        """
        Access the interactions

        :returns: twilio.rest.proxy.v1.service.session.interaction.InteractionList
        :rtype: twilio.rest.proxy.v1.service.session.interaction.InteractionList
        """
        if self._interactions is None:
            self._interactions = InteractionList(
                self._version,
                service_sid=self._solution['service_sid'],
                session_sid=self._solution['sid'],
            )
        return self._interactions

    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantList
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantList
        """
        if self._participants is None:
            self._participants = ParticipantList(
                self._version,
                service_sid=self._solution['service_sid'],
                session_sid=self._solution['sid'],
            )
        return self._participants

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.SessionContext {}>'.format(context)


class SessionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class Status(object):
        OPEN = "open"
        IN_PROGRESS = "in-progress"
        CLOSED = "closed"
        FAILED = "failed"
        UNKNOWN = "unknown"

    class Mode(object):
        MESSAGE_ONLY = "message-only"
        VOICE_ONLY = "voice-only"
        VOICE_AND_MESSAGE = "voice-and-message"

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the SessionInstance

        :returns: twilio.rest.proxy.v1.service.session.SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionInstance
        """
        super(SessionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'service_sid': payload.get('service_sid'),
            'account_sid': payload.get('account_sid'),
            'date_started': deserialize.iso8601_datetime(payload.get('date_started')),
            'date_ended': deserialize.iso8601_datetime(payload.get('date_ended')),
            'date_last_interaction': deserialize.iso8601_datetime(payload.get('date_last_interaction')),
            'date_expiry': deserialize.iso8601_datetime(payload.get('date_expiry')),
            'unique_name': payload.get('unique_name'),
            'status': payload.get('status'),
            'closed_reason': payload.get('closed_reason'),
            'ttl': deserialize.integer(payload.get('ttl')),
            'mode': payload.get('mode'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SessionContext for this SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionContext
        """
        if self._context is None:
            self._context = SessionContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the resource's parent Service
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_started(self):
        """
        :returns: The ISO 8601 date when the Session started
        :rtype: datetime
        """
        return self._properties['date_started']

    @property
    def date_ended(self):
        """
        :returns: The ISO 8601 date when the Session ended
        :rtype: datetime
        """
        return self._properties['date_ended']

    @property
    def date_last_interaction(self):
        """
        :returns: The ISO 8601 date when the Session last had an interaction
        :rtype: datetime
        """
        return self._properties['date_last_interaction']

    @property
    def date_expiry(self):
        """
        :returns: The ISO 8601 date when the Session should expire
        :rtype: datetime
        """
        return self._properties['date_expiry']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def status(self):
        """
        :returns: The status of the Session
        :rtype: SessionInstance.Status
        """
        return self._properties['status']

    @property
    def closed_reason(self):
        """
        :returns: The reason the Session ended
        :rtype: unicode
        """
        return self._properties['closed_reason']

    @property
    def ttl(self):
        """
        :returns: When the session will expire
        :rtype: unicode
        """
        return self._properties['ttl']

    @property
    def mode(self):
        """
        :returns: The Mode of the Session
        :rtype: SessionInstance.Mode
        """
        return self._properties['mode']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Session resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The URLs of resources related to the Session
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the SessionInstance

        :returns: The fetched SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SessionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, date_expiry=values.unset, ttl=values.unset,
               status=values.unset, fail_on_participant_conflict=values.unset):
        """
        Update the SessionInstance

        :param datetime date_expiry: The ISO 8601 date when the Session should expire
        :param unicode ttl: When the session will expire
        :param SessionInstance.Status status: The new status of the resource
        :param bool fail_on_participant_conflict: Opt-in to enable Proxy to return 400 on detected conflict on re-open request.

        :returns: The updated SessionInstance
        :rtype: twilio.rest.proxy.v1.service.session.SessionInstance
        """
        return self._proxy.update(
            date_expiry=date_expiry,
            ttl=ttl,
            status=status,
            fail_on_participant_conflict=fail_on_participant_conflict,
        )

    @property
    def interactions(self):
        """
        Access the interactions

        :returns: twilio.rest.proxy.v1.service.session.interaction.InteractionList
        :rtype: twilio.rest.proxy.v1.service.session.interaction.InteractionList
        """
        return self._proxy.interactions

    @property
    def participants(self):
        """
        Access the participants

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantList
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantList
        """
        return self._proxy.participants

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.SessionInstance {}>'.format(context)
