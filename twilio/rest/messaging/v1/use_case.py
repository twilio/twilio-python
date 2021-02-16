# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class UseCaseList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version):
        """
        Initialize the UseCaseList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.use_case.UseCaseList
        :rtype: twilio.rest.messaging.v1.use_case.UseCaseList
        """
        super(UseCaseList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/a2p/UseCases'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams UseCaseInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.messaging.v1.use_case.UseCaseInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UseCaseInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.use_case.UseCaseInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of UseCaseInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UseCaseInstance
        :rtype: twilio.rest.messaging.v1.use_case.UseCasePage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return UseCasePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UseCaseInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UseCaseInstance
        :rtype: twilio.rest.messaging.v1.use_case.UseCasePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return UseCasePage(self._version, response, self._solution)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UseCaseList>'


class UseCasePage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the UseCasePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.use_case.UseCasePage
        :rtype: twilio.rest.messaging.v1.use_case.UseCasePage
        """
        super(UseCasePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UseCaseInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.use_case.UseCaseInstance
        :rtype: twilio.rest.messaging.v1.use_case.UseCaseInstance
        """
        return UseCaseInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UseCasePage>'


class UseCaseInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload):
        """
        Initialize the UseCaseInstance

        :returns: twilio.rest.messaging.v1.use_case.UseCaseInstance
        :rtype: twilio.rest.messaging.v1.use_case.UseCaseInstance
        """
        super(UseCaseInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'name': payload.get('name'),
            'code': payload.get('code'),
            'description': payload.get('description'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def name(self):
        """
        :returns: Human readable name
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def code(self):
        """
        :returns: Unique Use Case code
        :rtype: unicode
        """
        return self._properties['code']

    @property
    def description(self):
        """
        :returns: Description of Use Case
        :rtype: unicode
        """
        return self._properties['description']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UseCaseInstance>'
