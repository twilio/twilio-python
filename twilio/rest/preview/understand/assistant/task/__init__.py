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
from twilio.rest.preview.understand.assistant.task.field import FieldList
from twilio.rest.preview.understand.assistant.task.sample import SampleList
from twilio.rest.preview.understand.assistant.task.task_actions import TaskActionsList
from twilio.rest.preview.understand.assistant.task.task_statistics import TaskStatisticsList


class TaskList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid):
        """
        Initialize the TaskList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant.

        :returns: twilio.rest.preview.understand.assistant.task.TaskList
        :rtype: twilio.rest.preview.understand.assistant.task.TaskList
        """
        super(TaskList, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, }
        self._uri = '/Assistants/{assistant_sid}/Tasks'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams TaskInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.preview.understand.assistant.task.TaskInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists TaskInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.understand.assistant.task.TaskInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of TaskInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return TaskPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TaskInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return TaskPage(self._version, response, self._solution)

    def create(self, unique_name, friendly_name=values.unset, actions=values.unset,
               actions_url=values.unset):
        """
        Create a new TaskInstance

        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param unicode friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param dict actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param unicode actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: Newly created TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'FriendlyName': friendly_name,
            'Actions': serialize.object(actions),
            'ActionsUrl': actions_url,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return TaskInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def get(self, sid):
        """
        Constructs a TaskContext

        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.preview.understand.assistant.task.TaskContext
        :rtype: twilio.rest.preview.understand.assistant.task.TaskContext
        """
        return TaskContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a TaskContext

        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.preview.understand.assistant.task.TaskContext
        :rtype: twilio.rest.preview.understand.assistant.task.TaskContext
        """
        return TaskContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.TaskList>'


class TaskPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the TaskPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param assistant_sid: The unique ID of the Assistant.

        :returns: twilio.rest.preview.understand.assistant.task.TaskPage
        :rtype: twilio.rest.preview.understand.assistant.task.TaskPage
        """
        super(TaskPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.understand.assistant.task.TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        return TaskInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.TaskPage>'


class TaskContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, sid):
        """
        Initialize the TaskContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant.
        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.preview.understand.assistant.task.TaskContext
        :rtype: twilio.rest.preview.understand.assistant.task.TaskContext
        """
        super(TaskContext, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid, }
        self._uri = '/Assistants/{assistant_sid}/Tasks/{sid}'.format(**self._solution)

        # Dependents
        self._fields = None
        self._samples = None
        self._task_actions = None
        self._statistics = None

    def fetch(self):
        """
        Fetch a TaskInstance

        :returns: Fetched TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset, unique_name=values.unset,
               actions=values.unset, actions_url=values.unset):
        """
        Update the TaskInstance

        :param unicode friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param dict actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param unicode actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: Updated TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'UniqueName': unique_name,
            'Actions': serialize.object(actions),
            'ActionsUrl': actions_url,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the TaskInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def fields(self):
        """
        Access the fields

        :returns: twilio.rest.preview.understand.assistant.task.field.FieldList
        :rtype: twilio.rest.preview.understand.assistant.task.field.FieldList
        """
        if self._fields is None:
            self._fields = FieldList(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                task_sid=self._solution['sid'],
            )
        return self._fields

    @property
    def samples(self):
        """
        Access the samples

        :returns: twilio.rest.preview.understand.assistant.task.sample.SampleList
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleList
        """
        if self._samples is None:
            self._samples = SampleList(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                task_sid=self._solution['sid'],
            )
        return self._samples

    @property
    def task_actions(self):
        """
        Access the task_actions

        :returns: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsList
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsList
        """
        if self._task_actions is None:
            self._task_actions = TaskActionsList(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                task_sid=self._solution['sid'],
            )
        return self._task_actions

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.preview.understand.assistant.task.task_statistics.TaskStatisticsList
        :rtype: twilio.rest.preview.understand.assistant.task.task_statistics.TaskStatisticsList
        """
        if self._statistics is None:
            self._statistics = TaskStatisticsList(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                task_sid=self._solution['sid'],
            )
        return self._statistics

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.TaskContext {}>'.format(context)


class TaskInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, assistant_sid, sid=None):
        """
        Initialize the TaskInstance

        :returns: twilio.rest.preview.understand.assistant.task.TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        super(TaskInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'links': payload.get('links'),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'actions_url': payload.get('actions_url'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: TaskContext for this TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskContext
        """
        if self._context is None:
            self._context = TaskContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Task.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the Assistant.
        :rtype: unicode
        """
        return self._properties['assistant_sid']

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def actions_url(self):
        """
        :returns: User-provided HTTP endpoint where from the assistant fetches actions
        :rtype: unicode
        """
        return self._properties['actions_url']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a TaskInstance

        :returns: Fetched TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset, unique_name=values.unset,
               actions=values.unset, actions_url=values.unset):
        """
        Update the TaskInstance

        :param unicode friendly_name: A user-provided string that identifies this resource. It is non-unique and can up to 255 characters long.
        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :param dict actions: A user-provided JSON object encoded as a string to specify the actions for this task. It is optional and non-unique.
        :param unicode actions_url: User-provided HTTP endpoint where from the assistant fetches actions

        :returns: Updated TaskInstance
        :rtype: twilio.rest.preview.understand.assistant.task.TaskInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            unique_name=unique_name,
            actions=actions,
            actions_url=actions_url,
        )

    def delete(self):
        """
        Deletes the TaskInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def fields(self):
        """
        Access the fields

        :returns: twilio.rest.preview.understand.assistant.task.field.FieldList
        :rtype: twilio.rest.preview.understand.assistant.task.field.FieldList
        """
        return self._proxy.fields

    @property
    def samples(self):
        """
        Access the samples

        :returns: twilio.rest.preview.understand.assistant.task.sample.SampleList
        :rtype: twilio.rest.preview.understand.assistant.task.sample.SampleList
        """
        return self._proxy.samples

    @property
    def task_actions(self):
        """
        Access the task_actions

        :returns: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsList
        :rtype: twilio.rest.preview.understand.assistant.task.task_actions.TaskActionsList
        """
        return self._proxy.task_actions

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.preview.understand.assistant.task.task_statistics.TaskStatisticsList
        :rtype: twilio.rest.preview.understand.assistant.task.task_statistics.TaskStatisticsList
        """
        return self._proxy.statistics

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.TaskInstance {}>'.format(context)
