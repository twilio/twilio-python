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
from twilio.rest.proxy.v1.service.session.participant.message_interaction import MessageInteractionList


class ParticipantList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, session_sid):
        """
        Initialize the ParticipantList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the resource's parent Service
        :param session_sid: The SID of the resource's parent Session

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantList
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantList
        """
        super(ParticipantList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'session_sid': session_sid, }
        self._uri = '/Services/{service_sid}/Sessions/{session_sid}/Participants'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams ParticipantInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.proxy.v1.service.session.participant.ParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.service.session.participant.ParticipantInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

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
               proxy_identifier=values.unset, proxy_identifier_sid=values.unset):
        """
        Create the ParticipantInstance

        :param unicode identifier: The phone number of the Participant
        :param unicode friendly_name: The string that you assigned to describe the participant
        :param unicode proxy_identifier: The proxy phone number to use for the Participant
        :param unicode proxy_identifier_sid: The Proxy Identifier Sid

        :returns: The created ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        data = values.of({
            'Identifier': identifier,
            'FriendlyName': friendly_name,
            'ProxyIdentifier': proxy_identifier,
            'ProxyIdentifierSid': proxy_identifier_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return ParticipantInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            session_sid=self._solution['session_sid'],
        )

    def get(self, sid):
        """
        Constructs a ParticipantContext

        :param sid: The unique string that identifies the resource

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

        :param sid: The unique string that identifies the resource

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
        :param service_sid: The SID of the resource's parent Service
        :param session_sid: The SID of the resource's parent Session

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
        :param service_sid: The SID of the parent Service of the resource to fetch
        :param session_sid: The SID of the parent Session of the resource to fetch
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantContext
        """
        super(ParticipantContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'session_sid': session_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Sessions/{session_sid}/Participants/{sid}'.format(**self._solution)

        # Dependents
        self._message_interactions = None

    def fetch(self):
        """
        Fetch the ParticipantInstance

        :returns: The fetched ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

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
        return self._version.delete(method='DELETE', uri=self._uri, )

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

    def __init__(self, version, payload, service_sid, session_sid, sid=None):
        """
        Initialize the ParticipantInstance

        :returns: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        :rtype: twilio.rest.proxy.v1.service.session.participant.ParticipantInstance
        """
        super(ParticipantInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'session_sid': payload.get('session_sid'),
            'service_sid': payload.get('service_sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'identifier': payload.get('identifier'),
            'proxy_identifier': payload.get('proxy_identifier'),
            'proxy_identifier_sid': payload.get('proxy_identifier_sid'),
            'date_deleted': deserialize.iso8601_datetime(payload.get('date_deleted')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
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
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def session_sid(self):
        """
        :returns: The SID of the resource's parent Session
        :rtype: unicode
        """
        return self._properties['session_sid']

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
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the participant
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def identifier(self):
        """
        :returns: The phone number of the Participant
        :rtype: unicode
        """
        return self._properties['identifier']

    @property
    def proxy_identifier(self):
        """
        :returns: The phone number or short code of the participant's partner
        :rtype: unicode
        """
        return self._properties['proxy_identifier']

    @property
    def proxy_identifier_sid(self):
        """
        :returns: The SID of the Proxy Identifier assigned to the Participant
        :rtype: unicode
        """
        return self._properties['proxy_identifier_sid']

    @property
    def date_deleted(self):
        """
        :returns: The ISO 8601 date the Participant was removed
        :rtype: datetime
        """
        return self._properties['date_deleted']

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
        :returns: The absolute URL of the Participant resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The URLs to resources related the participant
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch the ParticipantInstance

        :returns: The fetched ParticipantInstance
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
