# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DocumentPermissionList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, document_sid):
        """
        Initialize the DocumentPermissionList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Sync Service that the resource is associated with
        :param document_sid: The Sync Document SID

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionList
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionList
        """
        super(DocumentPermissionList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'document_sid': document_sid, }
        self._uri = '/Services/{service_sid}/Documents/{document_sid}/Permissions'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams DocumentPermissionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DocumentPermissionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of DocumentPermissionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return DocumentPermissionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DocumentPermissionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return DocumentPermissionPage(self._version, response, self._solution)

    def get(self, identity):
        """
        Constructs a DocumentPermissionContext

        :param identity: The application-defined string that uniquely identifies the User's Document Permission resource to fetch

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionContext
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionContext
        """
        return DocumentPermissionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            document_sid=self._solution['document_sid'],
            identity=identity,
        )

    def __call__(self, identity):
        """
        Constructs a DocumentPermissionContext

        :param identity: The application-defined string that uniquely identifies the User's Document Permission resource to fetch

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionContext
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionContext
        """
        return DocumentPermissionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            document_sid=self._solution['document_sid'],
            identity=identity,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.DocumentPermissionList>'


class DocumentPermissionPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the DocumentPermissionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Sync Service that the resource is associated with
        :param document_sid: The Sync Document SID

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionPage
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionPage
        """
        super(DocumentPermissionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DocumentPermissionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance
        """
        return DocumentPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            document_sid=self._solution['document_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.DocumentPermissionPage>'


class DocumentPermissionContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, document_sid, identity):
        """
        Initialize the DocumentPermissionContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Sync Service with the Document Permission resource to fetch
        :param document_sid: The SID of the Sync Document with the Document Permission resource to fetch
        :param identity: The application-defined string that uniquely identifies the User's Document Permission resource to fetch

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionContext
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionContext
        """
        super(DocumentPermissionContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'document_sid': document_sid, 'identity': identity, }
        self._uri = '/Services/{service_sid}/Documents/{document_sid}/Permissions/{identity}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a DocumentPermissionInstance

        :returns: Fetched DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return DocumentPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            document_sid=self._solution['document_sid'],
            identity=self._solution['identity'],
        )

    def delete(self):
        """
        Deletes the DocumentPermissionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, read, write, manage):
        """
        Update the DocumentPermissionInstance

        :param bool read: Read access
        :param bool write: Write access
        :param bool manage: Manage access

        :returns: Updated DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance
        """
        data = values.of({'Read': read, 'Write': write, 'Manage': manage, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return DocumentPermissionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            document_sid=self._solution['document_sid'],
            identity=self._solution['identity'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.DocumentPermissionContext {}>'.format(context)


class DocumentPermissionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, document_sid, identity=None):
        """
        Initialize the DocumentPermissionInstance

        :returns: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance
        """
        super(DocumentPermissionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'document_sid': payload.get('document_sid'),
            'identity': payload.get('identity'),
            'read': payload.get('read'),
            'write': payload.get('write'),
            'manage': payload.get('manage'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'document_sid': document_sid,
            'identity': identity or self._properties['identity'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DocumentPermissionContext for this DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionContext
        """
        if self._context is None:
            self._context = DocumentPermissionContext(
                self._version,
                service_sid=self._solution['service_sid'],
                document_sid=self._solution['document_sid'],
                identity=self._solution['identity'],
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
    def service_sid(self):
        """
        :returns: The SID of the Sync Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def document_sid(self):
        """
        :returns: The Sync Document SID
        :rtype: unicode
        """
        return self._properties['document_sid']

    @property
    def identity(self):
        """
        :returns: The identity of the user to whom the Sync Document Permission applies
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def read(self):
        """
        :returns: Read access
        :rtype: bool
        """
        return self._properties['read']

    @property
    def write(self):
        """
        :returns: Write access
        :rtype: bool
        """
        return self._properties['write']

    @property
    def manage(self):
        """
        :returns: Manage access
        :rtype: bool
        """
        return self._properties['manage']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Sync Document Permission resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a DocumentPermissionInstance

        :returns: Fetched DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the DocumentPermissionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, read, write, manage):
        """
        Update the DocumentPermissionInstance

        :param bool read: Read access
        :param bool write: Write access
        :param bool manage: Manage access

        :returns: Updated DocumentPermissionInstance
        :rtype: twilio.rest.sync.v1.service.document.document_permission.DocumentPermissionInstance
        """
        return self._proxy.update(read, write, manage, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.DocumentPermissionInstance {}>'.format(context)
