"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.taskrouter.v1.workspace.worker.reservation import ReservationList
from twilio.rest.taskrouter.v1.workspace.worker.worker_channel import WorkerChannelList
from twilio.rest.taskrouter.v1.workspace.worker.worker_statistics import WorkerStatisticsList
from twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics import WorkersCumulativeStatisticsList
from twilio.rest.taskrouter.v1.workspace.worker.workers_real_time_statistics import WorkersRealTimeStatisticsList
from twilio.rest.taskrouter.v1.workspace.worker.workers_statistics import WorkersStatisticsList


class WorkerList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkerList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Workers to read.
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        self._uri = '/Workspaces/{workspace_sid}/Workers'.format(**self._solution)
        
        self._cumulative_statistics = None
        self._real_time_statistics = None
        self._statistics = None
        
    
    
    
    
    def create(self, friendly_name, activity_sid=values.unset, attributes=values.unset):
        """
        Create the WorkerInstance

        :param str friendly_name: A descriptive string that you create to describe the new Worker. It can be up to 64 characters long.
        :param str activity_sid: The SID of a valid Activity that will describe the new Worker's initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information. If not provided, the new Worker's initial state is the `default_activity_sid` configured on the Workspace.
        :param str attributes: A valid JSON string that describes the new Worker. For example: `{ \\\"email\\\": \\\"Bob@example.com\\\", \\\"phone\\\": \\\"+5095551234\\\" }`. This data is passed to the `assignment_callback_url` when TaskRouter assigns a Task to the Worker. Defaults to {}.
        
        :returns: The created WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'ActivitySid': activity_sid,
            'Attributes': attributes,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return WorkerInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])
    
    
    def stream(self, activity_name=values.unset, activity_sid=values.unset, available=values.unset, friendly_name=values.unset, target_workers_expression=values.unset, task_queue_name=values.unset, task_queue_sid=values.unset, ordering=values.unset, limit=None, page_size=None):
        """
        Streams WorkerInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str activity_name: The `activity_name` of the Worker resources to read.
        :param str activity_sid: The `activity_sid` of the Worker resources to read.
        :param str available: Whether to return only Worker resources that are available or unavailable. Can be `true`, `1`, or `yes` to return Worker resources that are available, and `false`, or any value returns the Worker resources that are not available.
        :param str friendly_name: The `friendly_name` of the Worker resources to read.
        :param str target_workers_expression: Filter by Workers that would match an expression on a TaskQueue. This is helpful for debugging which Workers would match a potential queue.
        :param str task_queue_name: The `friendly_name` of the TaskQueue that the Workers to read are eligible for.
        :param str task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for.
        :param str ordering: Sorting parameter for Workers
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            activity_name=activity_name,
            activity_sid=activity_sid,
            available=available,
            friendly_name=friendly_name,
            target_workers_expression=target_workers_expression,
            task_queue_name=task_queue_name,
            task_queue_sid=task_queue_sid,
            ordering=ordering,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, activity_name=values.unset, activity_sid=values.unset, available=values.unset, friendly_name=values.unset, target_workers_expression=values.unset, task_queue_name=values.unset, task_queue_sid=values.unset, ordering=values.unset, limit=None, page_size=None):
        """
        Lists WorkerInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str activity_name: The `activity_name` of the Worker resources to read.
        :param str activity_sid: The `activity_sid` of the Worker resources to read.
        :param str available: Whether to return only Worker resources that are available or unavailable. Can be `true`, `1`, or `yes` to return Worker resources that are available, and `false`, or any value returns the Worker resources that are not available.
        :param str friendly_name: The `friendly_name` of the Worker resources to read.
        :param str target_workers_expression: Filter by Workers that would match an expression on a TaskQueue. This is helpful for debugging which Workers would match a potential queue.
        :param str task_queue_name: The `friendly_name` of the TaskQueue that the Workers to read are eligible for.
        :param str task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for.
        :param str ordering: Sorting parameter for Workers
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance]
        """
        return list(self.stream(
            activity_name=activity_name,
            activity_sid=activity_sid,
            available=available,
            friendly_name=friendly_name,
            target_workers_expression=target_workers_expression,
            task_queue_name=task_queue_name,
            task_queue_sid=task_queue_sid,
            ordering=ordering,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, activity_name=values.unset, activity_sid=values.unset, available=values.unset, friendly_name=values.unset, target_workers_expression=values.unset, task_queue_name=values.unset, task_queue_sid=values.unset, ordering=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of WorkerInstance records from the API.
        Request is executed immediately
        
        :param str activity_name: The `activity_name` of the Worker resources to read.
        :param str activity_sid: The `activity_sid` of the Worker resources to read.
        :param str available: Whether to return only Worker resources that are available or unavailable. Can be `true`, `1`, or `yes` to return Worker resources that are available, and `false`, or any value returns the Worker resources that are not available.
        :param str friendly_name: The `friendly_name` of the Worker resources to read.
        :param str target_workers_expression: Filter by Workers that would match an expression on a TaskQueue. This is helpful for debugging which Workers would match a potential queue.
        :param str task_queue_name: The `friendly_name` of the TaskQueue that the Workers to read are eligible for.
        :param str task_queue_sid: The SID of the TaskQueue that the Workers to read are eligible for.
        :param str ordering: Sorting parameter for Workers
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        """
        data = values.of({ 
            'ActivityName': activity_name,
            'ActivitySid': activity_sid,
            'Available': available,
            'FriendlyName': friendly_name,
            'TargetWorkersExpression': target_workers_expression,
            'TaskQueueName': task_queue_name,
            'TaskQueueSid': task_queue_sid,
            'Ordering': ordering,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return WorkerPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WorkerInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return WorkerPage(self._version, response, self._solution)


    @property
    def cumulative_statistics(self):
        """
        Access the cumulative_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkersCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkersCumulativeStatisticsList
        """
        if self._cumulative_statistics is None:
            self._cumulative_statistics = WorkersCumulativeStatisticsList(self._version, workspace_sid=self._solution['workspace_sid'])
        return self._cumulative_statistics

    @property
    def real_time_statistics(self):
        """
        Access the real_time_statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkersRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkersRealTimeStatisticsList
        """
        if self._real_time_statistics is None:
            self._real_time_statistics = WorkersRealTimeStatisticsList(self._version, workspace_sid=self._solution['workspace_sid'])
        return self._real_time_statistics

    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkersStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkersStatisticsList
        """
        if self._statistics is None:
            self._statistics = WorkersStatisticsList(self._version, workspace_sid=self._solution['workspace_sid'])
        return self._statistics

    def get(self, sid):
        """
        Constructs a WorkerContext
        
        :param sid: The SID of the Worker resource to update.
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        return WorkerContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a WorkerContext
        
        :param sid: The SID of the Worker resource to update.
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        return WorkerContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerList>'










class WorkerPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the WorkerPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WorkerInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        return WorkerInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkerPage>'




class WorkerInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str, sid: str=None):
        """
        Initialize the WorkerInstance
        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'activity_name': payload.get('activity_name'),
            'activity_sid': payload.get('activity_sid'),
            'attributes': payload.get('attributes'),
            'available': payload.get('available'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_status_changed': deserialize.iso8601_datetime(payload.get('date_status_changed')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'sid': payload.get('sid'),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'workspace_sid': workspace_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WorkerContext for this WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        if self._context is None:
            self._context = WorkerContext(self._version, workspace_sid=self._solution['workspace_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def activity_name(self):
        """
        :returns: The `friendly_name` of the Worker's current Activity.
        :rtype: str
        """
        return self._properties['activity_name']
    
    @property
    def activity_sid(self):
        """
        :returns: The SID of the Worker's current Activity.
        :rtype: str
        """
        return self._properties['activity_sid']
    
    @property
    def attributes(self):
        """
        :returns: The JSON string that describes the Worker. For example: `{ \"email\": \"Bob@example.com\", \"phone\": \"+5095551234\" }`. **Note** If this property has been assigned a value, it will only be displayed in FETCH actions that return a single resource. Otherwise, this property will be null, even if it has a value. This data is passed to the `assignment_callback_url` when TaskRouter assigns a Task to the Worker.
        :rtype: str
        """
        return self._properties['attributes']
    
    @property
    def available(self):
        """
        :returns: Whether the Worker is available to perform tasks.
        :rtype: bool
        """
        return self._properties['available']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_status_changed(self):
        """
        :returns: The date and time in GMT of the last change to the Worker's activity specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Used to calculate Workflow statistics.
        :rtype: datetime
        """
        return self._properties['date_status_changed']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource. Friendly names are case insensitive, and unique within the TaskRouter Workspace.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Worker resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Worker.
        :rtype: str
        """
        return self._properties['workspace_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Worker resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of related resources.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self, if_match=values.unset):
        """
        Deletes the WorkerInstance
        
        :params str if_match: The If-Match HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(if_match=if_match, )
    
    def fetch(self):
        """
        Fetch the WorkerInstance
        

        :returns: The fetched WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        return self._proxy.fetch()
    
    def update(self, if_match=values.unset, activity_sid=values.unset, attributes=values.unset, friendly_name=values.unset, reject_pending_reservations=values.unset):
        """
        Update the WorkerInstance
        
        :params str if_match: The If-Match HTTP request header
        :params str activity_sid: The SID of a valid Activity that will describe the Worker's initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information.
        :params str attributes: The JSON string that describes the Worker. For example: `{ \\\"email\\\": \\\"Bob@example.com\\\", \\\"phone\\\": \\\"+5095551234\\\" }`. This data is passed to the `assignment_callback_url` when TaskRouter assigns a Task to the Worker. Defaults to {}.
        :params str friendly_name: A descriptive string that you create to describe the Worker. It can be up to 64 characters long.
        :params bool reject_pending_reservations: Whether to reject the Worker's pending reservations. This option is only valid if the Worker's new [Activity](https://www.twilio.com/docs/taskrouter/api/activity) resource has its `availability` property set to `False`.

        :returns: The updated WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        return self._proxy.update(if_match=if_match, activity_sid=activity_sid, attributes=attributes, friendly_name=friendly_name, reject_pending_reservations=reject_pending_reservations, )
    
    @property
    def reservations(self):
        """
        Access the reservations

        :returns: twilio.rest.taskrouter.v1.workspace.worker.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.ReservationList
        """
        return self._proxy.reservations
    
    @property
    def worker_channels(self):
        """
        Access the worker_channels

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerChannelList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerChannelList
        """
        return self._proxy.worker_channels
    
    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerStatisticsList
        """
        return self._proxy.statistics
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkerInstance {}>'.format(context)

class WorkerContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str, sid: str):
        """
        Initialize the WorkerContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Worker to update.
        :param sid: The SID of the Worker resource to update.

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
            'sid': sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workers/{sid}'.format(**self._solution)
        
        self._reservations = None
        self._worker_channels = None
        self._statistics = None
    
    def delete(self, if_match=values.unset):
        """
        Deletes the WorkerInstance

        :param str if_match: The If-Match HTTP request header
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'If-Match': if_match, })
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)
        
    def fetch(self):
        """
        Fetch the WorkerInstance
        

        :returns: The fetched WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return WorkerInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, if_match=values.unset, activity_sid=values.unset, attributes=values.unset, friendly_name=values.unset, reject_pending_reservations=values.unset):
        """
        Update the WorkerInstance
        
        :params str if_match: The If-Match HTTP request header
        :params str activity_sid: The SID of a valid Activity that will describe the Worker's initial state. See [Activities](https://www.twilio.com/docs/taskrouter/api/activity) for more information.
        :params str attributes: The JSON string that describes the Worker. For example: `{ \\\"email\\\": \\\"Bob@example.com\\\", \\\"phone\\\": \\\"+5095551234\\\" }`. This data is passed to the `assignment_callback_url` when TaskRouter assigns a Task to the Worker. Defaults to {}.
        :params str friendly_name: A descriptive string that you create to describe the Worker. It can be up to 64 characters long.
        :params bool reject_pending_reservations: Whether to reject the Worker's pending reservations. This option is only valid if the Worker's new [Activity](https://www.twilio.com/docs/taskrouter/api/activity) resource has its `availability` property set to `False`.

        :returns: The updated WorkerInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerInstance
        """
        data = values.of({ 
            'ActivitySid': activity_sid,
            'Attributes': attributes,
            'FriendlyName': friendly_name,
            'RejectPendingReservations': reject_pending_reservations,
        })
        headers = values.of({'If-Match': if_match, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers)

        return WorkerInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def reservations(self):
        """
        Access the reservations

        :returns: twilio.rest.taskrouter.v1.workspace.worker.ReservationList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.ReservationList
        """
        if self._reservations is None:
            self._reservations = ReservationList(
                self._version, 
                self._solution['workspace_sid'],
                self._solution['sid'],
            )
        return self._reservations
    
    @property
    def worker_channels(self):
        """
        Access the worker_channels

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerChannelList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerChannelList
        """
        if self._worker_channels is None:
            self._worker_channels = WorkerChannelList(
                self._version, 
                self._solution['workspace_sid'],
                self._solution['sid'],
            )
        return self._worker_channels
    
    @property
    def statistics(self):
        """
        Access the statistics

        :returns: twilio.rest.taskrouter.v1.workspace.worker.WorkerStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.WorkerStatisticsList
        """
        if self._statistics is None:
            self._statistics = WorkerStatisticsList(
                self._version, 
                self._solution['workspace_sid'],
                self._solution['sid'],
            )
        return self._statistics
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkerContext {}>'.format(context)


