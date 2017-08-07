# coding=utf-8
"""
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
from twilio.rest.sync.v1.service.document.document_permission import DocumentPermissionList


class DocumentList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the DocumentList

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid

        :returns: twilio.rest.sync.v1.service.document.DocumentList
        :rtype: twilio.rest.sync.v1.service.document.DocumentList
        """
        super(DocumentList, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
        }
        self._uri = '/Services/{service_sid}/Documents'.format(**self._solution)

    def create(self, unique_name=values.unset, data=values.unset):
        """
        Create a new DocumentInstance

        :param unicode unique_name: The unique_name
        :param dict data: The data

        :returns: Newly created DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'Data': serialize.object(data),
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return DocumentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams DocumentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.sync.v1.service.document.DocumentInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.document.DocumentInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of DocumentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentPage
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return DocumentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DocumentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return DocumentPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a DocumentContext

        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.document.DocumentContext
        :rtype: twilio.rest.sync.v1.service.document.DocumentContext
        """
        return DocumentContext(
            self._version,
            service_sid=self._solution['service_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a DocumentContext

        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.document.DocumentContext
        :rtype: twilio.rest.sync.v1.service.document.DocumentContext
        """
        return DocumentContext(
            self._version,
            service_sid=self._solution['service_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.DocumentList>'


class DocumentPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the DocumentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The service_sid

        :returns: twilio.rest.sync.v1.service.document.DocumentPage
        :rtype: twilio.rest.sync.v1.service.document.DocumentPage
        """
        super(DocumentPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DocumentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.document.DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        return DocumentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.DocumentPage>'


class DocumentContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the DocumentContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: The sid

        :returns: twilio.rest.sync.v1.service.document.DocumentContext
        :rtype: twilio.rest.sync.v1.service.document.DocumentContext
        """
        super(DocumentContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Documents/{sid}'.format(**self._solution)

        # Dependents
        self._document_permissions = None

    def fetch(self):
        """
        Fetch a DocumentInstance

        :returns: Fetched DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return DocumentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the DocumentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, data):
        """
        Update the DocumentInstance

        :param dict data: The data

        :returns: Updated DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        data = values.of({
            'Data': serialize.object(data),
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return DocumentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    @property
    def document_permissions(self):
        """
        Access the document_permissions

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionList
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionList
        """
        if self._document_permissions is None:
            self._document_permissions = DocumentPermissionList(
                self._version,
                service_sid=self._solution['service_sid'],
                document_sid=self._solution['sid'],
            )
        return self._document_permissions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.DocumentContext {}>'.format(context)


class DocumentInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the DocumentInstance

        :returns: twilio.rest.sync.v1.service.document.DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        super(DocumentInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'url': payload['url'],
            'links': payload['links'],
            'revision': payload['revision'],
            'data': payload['data'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'created_by': payload['created_by'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DocumentContext for this DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentContext
        """
        if self._context is None:
            self._context = DocumentContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: The unique_name
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The service_sid
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def revision(self):
        """
        :returns: The revision
        :rtype: unicode
        """
        return self._properties['revision']

    @property
    def data(self):
        """
        :returns: The data
        :rtype: dict
        """
        return self._properties['data']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def created_by(self):
        """
        :returns: The created_by
        :rtype: unicode
        """
        return self._properties['created_by']

    def fetch(self):
        """
        Fetch a DocumentInstance

        :returns: Fetched DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the DocumentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, data):
        """
        Update the DocumentInstance

        :param dict data: The data

        :returns: Updated DocumentInstance
        :rtype: twilio.rest.sync.v1.service.document.DocumentInstance
        """
        return self._proxy.update(
            data,
        )

    @property
    def document_permissions(self):
        """
        Access the document_permissions

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionList
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionList
        """
        return self._proxy.document_permissions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.DocumentInstance {}>'.format(context)
