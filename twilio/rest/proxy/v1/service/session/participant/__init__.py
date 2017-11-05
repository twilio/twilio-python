# coding=utf-8
"""
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
from twilio.rest.proxy.v1.service.session.participant.message_interaction import MessageInteractionList


class ParticipantList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, session_sid):
        """
        Initialize the ParticipantList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param session_sid: Session Sid.

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantList
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantList
        """
        super(ParticipantList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'session_sid': session_sid,}
        self._uri = '/Services/{service_sid}/Sessions/{session_sid}/Participants'.format(**self._solution)

    def stream(self, participant_type=values.unset, identifier=values.unset,
               limit=None, page_size=None):
        """
        Streams ParticipantInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param ParticipantInstance.ParticipantType participant_type: The participant_type
        :param unicode identifier: The identifier
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.session.participant.ParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            participant_type=participant_type,
            identifier=identifier,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, participant_type=values.unset, identifier=values.unset,
             limit=None, page_size=None):
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param ParticipantInstance.ParticipantType participant_type: The participant_type
        :param unicode identifier: The identifier
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.session.participant.ParticipantInstance]
        """
        return list(self.stream(
            participant_type=participant_type,
            identifier=identifier,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, participant_type=values.unset, identifier=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param ParticipantInstance.ParticipantType participant_type: The participant_type
        :param unicode identifier: The identifier
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantPage
        """
        params = values.of({
            'ParticipantType': participant_type,
            'Identifier': identifier,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ParticipantPage(self._version, response, self._solution)

    def create(self, identifier, friendly_name=values.unset,
               participant_type=values.unset, proxy_identifier=values.unset,
               proxy_identifier_sid=values.unset):
        """
        Create a new ParticipantInstance

        :param unicode identifier: The phone number of this Participant.
        :param unicode friendly_name: A human readable description of this resource.
        :param ParticipantInstance.ParticipantType participant_type: The Participant Type of this Participant
        :param unicode proxy_identifier: The proxy phone number for this Participant.
        :param unicode proxy_identifier_sid: Proxy Identifier Sid.

        :returns: Newly created ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        data = values.of({
            'Identifier': identifier,
            'FriendlyName': friendly_name,
            'ParticipantType': participant_type,
            'ProxyIdentifier': proxy_identifier,
            'ProxyIdentifierSid': proxy_identifier_sid,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
        )

    def get(self, sid):
        """
        Constructs a ParticipantContext

        :param sid: A string that uniquely identifies this Participant.

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        """
        return ParticipantContext(
            self._version,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a ParticipantContext

        :param sid: A string that uniquely identifies this Participant.

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        """
        return ParticipantContext(
            self._version,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.ParticipantList>'


class ParticipantPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the ParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.
        :param session_sid: Session Sid.

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantPage
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantPage
        """
        super(ParticipantPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.ParticipantPage>'


class ParticipantContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, session_sid, sid):
        """
        Initialize the ParticipantContext

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param session_sid: Session Sid.
        :param sid: A string that uniquely identifies this Participant.

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        """
        super(ParticipantContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'session_sid': session_sid, 'sid': sid,}
        self._uri = '/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}'.format(**self._solution)

        # Dependents
        self._message_interactions = None

    def fetch(self):
        """
        Fetch a ParticipantInstance

        :returns: Fetched ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the ParticipantInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, participant_type=values.unset, identifier=values.unset,
               friendly_name=values.unset, proxy_identifier=values.unset,
               proxy_identifier_sid=values.unset):
        """
        Update the ParticipantInstance

        :param ParticipantInstance.ParticipantType participant_type: The Participant Type of this Participant
        :param unicode identifier: The phone number of this Participant.
        :param unicode friendly_name: A human readable description of this resource.
        :param unicode proxy_identifier: The proxy phone number for this Participant.
        :param unicode proxy_identifier_sid: Proxy Identifier Sid.

        :returns: Updated ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        data = values.of({
            'ParticipantType': participant_type,
            'Identifier': identifier,
            'FriendlyName': friendly_name,
            'ProxyIdentifier': proxy_identifier,
            'ProxyIdentifierSid': proxy_identifier_sid,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
            sid=self._solution['sid'],
        )

    @property
    def message_interactions(self):
        """
        Access the message_interactions

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionList
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionList
        """
        if self._message_interactions is None:
            self._message_interactions = MessageInteractionList(
                self._version,
                service_sid=self._solution['service_sid'],
                session_sid=self._solution['session_sid'],
                participant_sid=self._solution['sid'],
            )
        return self._message_interactions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.ParticipantContext {}>'.format(context)


class ParticipantInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class ParticipantType(object):
        MESSAGE_ONLY = "message-only"
        VOICE_ONLY = "voice-only"
        VOICE_AND_MESSAGE = "voice-and-message"

    def __init__(self, version, payload, service_sid, session_sid, sid=None):
        """
        Initialize the ParticipantInstance

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        super(ParticipantInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'session_sid': payload['session_sid'],
            'service_sid': payload['service_sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'participant_type': payload['participant_type'],
            'identifier': payload['identifier'],
            'proxy_identifier': payload['proxy_identifier'],
            'proxy_identifier_sid': payload['proxy_identifier_sid'],
            'date_deleted': deserialize.iso8601_datetime(payload['date_deleted']),
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'session_sid': session_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ParticipantContext for this ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        """
        if self._context is None:
            self._context = ParticipantContext(
                self._version,
                service_sid=self._solution['service_sid'],
                session_sid=self._solution['session_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Participant.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def session_sid(self):
        """
        :returns: Session Sid.
        :rtype: unicode
        """
        return self._properties['session_sid']

    @property
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def participant_type(self):
        """
        :returns: The Participant Type of this Participant
        :rtype: ParticipantInstance.ParticipantType
        """
        return self._properties['participant_type']

    @property
    def identifier(self):
        """
        :returns: The phone number of this Participant.
        :rtype: unicode
        """
        return self._properties['identifier']

    @property
    def proxy_identifier(self):
        """
        :returns: The proxy phone number for this Participant.
        :rtype: unicode
        """
        return self._properties['proxy_identifier']

    @property
    def proxy_identifier_sid(self):
        """
        :returns: Proxy Identifier Sid.
        :rtype: unicode
        """
        return self._properties['proxy_identifier_sid']

    @property
    def date_deleted(self):
        """
        :returns: The date this Participant was deleted
        :rtype: datetime
        """
        return self._properties['date_deleted']

    @property
    def date_created(self):
        """
        :returns: The date this Participant was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Participant was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a ParticipantInstance

        :returns: Fetched ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the ParticipantInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, participant_type=values.unset, identifier=values.unset,
               friendly_name=values.unset, proxy_identifier=values.unset,
               proxy_identifier_sid=values.unset):
        """
        Update the ParticipantInstance

        :param ParticipantInstance.ParticipantType participant_type: The Participant Type of this Participant
        :param unicode identifier: The phone number of this Participant.
        :param unicode friendly_name: A human readable description of this resource.
        :param unicode proxy_identifier: The proxy phone number for this Participant.
        :param unicode proxy_identifier_sid: Proxy Identifier Sid.

        :returns: Updated ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        return self._proxy.update(
            participant_type=participant_type,
            identifier=identifier,
            friendly_name=friendly_name,
            proxy_identifier=proxy_identifier,
            proxy_identifier_sid=proxy_identifier_sid,
        )

    @property
    def message_interactions(self):
        """
        Access the message_interactions

        :returns: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionList
        :rtype: twilio.rest.proxy.v1.service.session.participant.message_interaction.MessageInteractionList
        """
        return self._proxy.message_interactions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.ParticipantInstance {}>'.format(context)
