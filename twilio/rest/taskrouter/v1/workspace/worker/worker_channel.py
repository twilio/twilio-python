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


class WorkerChannelList(ListResource):
    """  """

    def __init__(self, version, workspace_sid, worker_sid):
        """
        Initialize the WorkerChannelList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace that contains the WorkerChannel
        :param worker_sid: The SID of the Worker that contains the WorkerChannel

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelList
        """
        super(WorkerChannelList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'worker_sid': worker_sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams WorkerChannelInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists WorkerChannelInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of WorkerChannelInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return WorkerChannelPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WorkerChannelInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return WorkerChannelPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a WorkerChannelContext

        :param sid: The SID of the to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelContext
        """
        return WorkerChannelContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a WorkerChannelContext

        :param sid: The SID of the to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelContext
        """
        return WorkerChannelContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerChannelList>'


class WorkerChannelPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the WorkerChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The SID of the Workspace that contains the WorkerChannel
        :param worker_sid: The SID of the Worker that contains the WorkerChannel

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelPage
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelPage
        """
        super(WorkerChannelPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkerChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance
        """
        return WorkerChannelInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerChannelPage>'


class WorkerChannelContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid, worker_sid, sid):
        """
        Initialize the WorkerChannelContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the WorkerChannel to fetch
        :param worker_sid: The SID of the Worker with the WorkerChannel to fetch
        :param sid: The SID of the to fetch

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelContext
        """
        super(WorkerChannelContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'worker_sid': worker_sid, 'sid': sid, }
        self._uri = '/Workspaces/{workspace_sid}/Workers/{worker_sid}/Channels/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the WorkerChannelInstance

        :returns: The fetched WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkerChannelInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
            sid=self._solution['sid'],
        )

    def update(self, capacity=values.unset, available=values.unset):
        """
        Update the WorkerChannelInstance

        :param unicode capacity: The total number of Tasks that the Worker should handle for the TaskChannel type
        :param bool available: Whether the WorkerChannel is available

        :returns: The updated WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance
        """
        data = values.of({'Capacity': capacity, 'Available': available, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return WorkerChannelInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            worker_sid=self._solution['worker_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkerChannelContext {}>'.format(context)


class WorkerChannelInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid, worker_sid, sid=None):
        """
        Initialize the WorkerChannelInstance

        :returns: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance
        """
        super(WorkerChannelInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'assigned_tasks': deserialize.integer(payload.get('assigned_tasks')),
            'available': payload.get('available'),
            'available_capacity_percentage': deserialize.integer(payload.get('available_capacity_percentage')),
            'configured_capacity': deserialize.integer(payload.get('configured_capacity')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'sid': payload.get('sid'),
            'task_channel_sid': payload.get('task_channel_sid'),
            'task_channel_unique_name': payload.get('task_channel_unique_name'),
            'worker_sid': payload.get('worker_sid'),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid,
            'worker_sid': worker_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WorkerChannelContext for this WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelContext
        """
        if self._context is None:
            self._context = WorkerChannelContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                worker_sid=self._solution['worker_sid'],
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
    def assigned_tasks(self):
        """
        :returns: The total number of Tasks assigned to Worker for the TaskChannel type
        :rtype: unicode
        """
        return self._properties['assigned_tasks']

    @property
    def available(self):
        """
        :returns: Whether the Worker should receive Tasks of the TaskChannel type
        :rtype: bool
        """
        return self._properties['available']

    @property
    def available_capacity_percentage(self):
        """
        :returns: The current available capacity between 0 to 100 for the TaskChannel
        :rtype: unicode
        """
        return self._properties['available_capacity_percentage']

    @property
    def configured_capacity(self):
        """
        :returns: The current configured capacity for the WorkerChannel
        :rtype: unicode
        """
        return self._properties['configured_capacity']

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
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def task_channel_sid(self):
        """
        :returns: The SID of the TaskChannel
        :rtype: unicode
        """
        return self._properties['task_channel_sid']

    @property
    def task_channel_unique_name(self):
        """
        :returns: The unique name of the TaskChannel, such as 'voice' or 'sms'
        :rtype: unicode
        """
        return self._properties['task_channel_unique_name']

    @property
    def worker_sid(self):
        """
        :returns: The SID of the Worker that contains the WorkerChannel
        :rtype: unicode
        """
        return self._properties['worker_sid']

    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the WorkerChannel
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The absolute URL of the WorkerChannel resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the WorkerChannelInstance

        :returns: The fetched WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance
        """
        return self._proxy.fetch()

    def update(self, capacity=values.unset, available=values.unset):
        """
        Update the WorkerChannelInstance

        :param unicode capacity: The total number of Tasks that the Worker should handle for the TaskChannel type
        :param bool available: Whether the WorkerChannel is available

        :returns: The updated WorkerChannelInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.worker_channel.WorkerChannelInstance
        """
        return self._proxy.update(capacity=capacity, available=available, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkerChannelInstance {}>'.format(context)
