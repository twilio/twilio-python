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


class QueryList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid):
        """
        Initialize the QueryList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the Assistant that is the parent of the resource

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryList
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryList
        """
        super(QueryList, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, }
        self._uri = '/Assistants/{assistant_sid}/Queries'.format(**self._solution)

    def stream(self, language=values.unset, model_build=values.unset,
               status=values.unset, limit=None, page_size=None):
        """
        Streams QueryInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode language: The ISO language-country string that specifies the language used by the Query resources to read
        :param unicode model_build: The SID or unique name of the Model Build to be queried
        :param unicode status: The status of the resources to read
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.query.QueryInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            language=language,
            model_build=model_build,
            status=status,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, language=values.unset, model_build=values.unset,
             status=values.unset, limit=None, page_size=None):
        """
        Lists QueryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode language: The ISO language-country string that specifies the language used by the Query resources to read
        :param unicode model_build: The SID or unique name of the Model Build to be queried
        :param unicode status: The status of the resources to read
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.query.QueryInstance]
        """
        return list(self.stream(
            language=language,
            model_build=model_build,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, language=values.unset, model_build=values.unset,
             status=values.unset, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of QueryInstance records from the API.
        Request is executed immediately

        :param unicode language: The ISO language-country string that specifies the language used by the Query resources to read
        :param unicode model_build: The SID or unique name of the Model Build to be queried
        :param unicode status: The status of the resources to read
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryPage
        """
        params = values.of({
            'Language': language,
            'ModelBuild': model_build,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return QueryPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of QueryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return QueryPage(self._version, response, self._solution)

    def create(self, language, query, tasks=values.unset, model_build=values.unset):
        """
        Create a new QueryInstance

        :param unicode language: The ISO language-country string that specifies the language used for the new query
        :param unicode query: The end-user's natural language input
        :param unicode tasks: The list of tasks to limit the new query to
        :param unicode model_build: The SID or unique name of the Model Build to be queried

        :returns: Newly created QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        data = values.of({'Language': language, 'Query': query, 'Tasks': tasks, 'ModelBuild': model_build, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return QueryInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def get(self, sid):
        """
        Constructs a QueryContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryContext
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryContext
        """
        return QueryContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a QueryContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryContext
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryContext
        """
        return QueryContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.QueryList>'


class QueryPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the QueryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param assistant_sid: The SID of the Assistant that is the parent of the resource

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryPage
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryPage
        """
        super(QueryPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of QueryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        return QueryInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.QueryPage>'


class QueryContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, sid):
        """
        Initialize the QueryContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the Assistant that is the parent of the resource to fetch
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryContext
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryContext
        """
        super(QueryContext, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid, }
        self._uri = '/Assistants/{assistant_sid}/Queries/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a QueryInstance

        :returns: Fetched QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return QueryInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def update(self, sample_sid=values.unset, status=values.unset):
        """
        Update the QueryInstance

        :param unicode sample_sid: The SID of an optional reference to the Sample created from the query
        :param unicode status: The new status of the resource

        :returns: Updated QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        data = values.of({'SampleSid': sample_sid, 'Status': status, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return QueryInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the QueryInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.QueryContext {}>'.format(context)


class QueryInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, assistant_sid, sid=None):
        """
        Initialize the QueryInstance

        :returns: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        super(QueryInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'results': payload.get('results'),
            'language': payload.get('language'),
            'model_build_sid': payload.get('model_build_sid'),
            'query': payload.get('query'),
            'sample_sid': payload.get('sample_sid'),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'status': payload.get('status'),
            'url': payload.get('url'),
            'source_channel': payload.get('source_channel'),
        }

        # Context
        self._context = None
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: QueryContext for this QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryContext
        """
        if self._context is None:
            self._context = QueryContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def results(self):
        """
        :returns: The natural language analysis results that include the Task recognized and a list of identified Fields
        :rtype: dict
        """
        return self._properties['results']

    @property
    def language(self):
        """
        :returns: The ISO language-country string that specifies the language used by the Query
        :rtype: unicode
        """
        return self._properties['language']

    @property
    def model_build_sid(self):
        """
        :returns: The SID of the [Model Build](https://www.twilio.com/docs/autopilot/api/model-build) queried
        :rtype: unicode
        """
        return self._properties['model_build_sid']

    @property
    def query(self):
        """
        :returns: The end-user's natural language input
        :rtype: unicode
        """
        return self._properties['query']

    @property
    def sample_sid(self):
        """
        :returns: The SID of an optional reference to the Sample created from the query
        :rtype: unicode
        """
        return self._properties['sample_sid']

    @property
    def assistant_sid(self):
        """
        :returns: The SID of the Assistant that is the parent of the resource
        :rtype: unicode
        """
        return self._properties['assistant_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: The status of the Query
        :rtype: unicode
        """
        return self._properties['status']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Query resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def source_channel(self):
        """
        :returns: The communication channel from where the end-user input came
        :rtype: unicode
        """
        return self._properties['source_channel']

    def fetch(self):
        """
        Fetch a QueryInstance

        :returns: Fetched QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        return self._proxy.fetch()

    def update(self, sample_sid=values.unset, status=values.unset):
        """
        Update the QueryInstance

        :param unicode sample_sid: The SID of an optional reference to the Sample created from the query
        :param unicode status: The new status of the resource

        :returns: Updated QueryInstance
        :rtype: twilio.rest.autopilot.v1.assistant.query.QueryInstance
        """
        return self._proxy.update(sample_sid=sample_sid, status=status, )

    def delete(self):
        """
        Deletes the QueryInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.QueryInstance {}>'.format(context)
