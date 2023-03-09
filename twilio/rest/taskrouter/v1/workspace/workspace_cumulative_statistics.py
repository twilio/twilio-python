r"""
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
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class WorkspaceCumulativeStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkspaceCumulativeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace to fetch.
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a WorkspaceCumulativeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsContext
        """
        return WorkspaceCumulativeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __call__(self):
        """
        Constructs a WorkspaceCumulativeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsContext
        """
        return WorkspaceCumulativeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceCumulativeStatisticsList>'

class WorkspaceCumulativeStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str):
        """
        Initialize the WorkspaceCumulativeStatisticsInstance
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'avg_task_acceptance_time': deserialize.integer(payload.get('avg_task_acceptance_time')),
            'start_time': deserialize.iso8601_datetime(payload.get('start_time')),
            'end_time': deserialize.iso8601_datetime(payload.get('end_time')),
            'reservations_created': deserialize.integer(payload.get('reservations_created')),
            'reservations_accepted': deserialize.integer(payload.get('reservations_accepted')),
            'reservations_rejected': deserialize.integer(payload.get('reservations_rejected')),
            'reservations_timed_out': deserialize.integer(payload.get('reservations_timed_out')),
            'reservations_canceled': deserialize.integer(payload.get('reservations_canceled')),
            'reservations_rescinded': deserialize.integer(payload.get('reservations_rescinded')),
            'split_by_wait_time': payload.get('split_by_wait_time'),
            'wait_duration_until_accepted': payload.get('wait_duration_until_accepted'),
            'wait_duration_until_canceled': payload.get('wait_duration_until_canceled'),
            'tasks_canceled': deserialize.integer(payload.get('tasks_canceled')),
            'tasks_completed': deserialize.integer(payload.get('tasks_completed')),
            'tasks_created': deserialize.integer(payload.get('tasks_created')),
            'tasks_deleted': deserialize.integer(payload.get('tasks_deleted')),
            'tasks_moved': deserialize.integer(payload.get('tasks_moved')),
            'tasks_timed_out_in_workflow': deserialize.integer(payload.get('tasks_timed_out_in_workflow')),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'workspace_sid': workspace_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: WorkspaceCumulativeStatisticsContext for this WorkspaceCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsContext
        """
        if self._context is None:
            self._context = WorkspaceCumulativeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workspace resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def avg_task_acceptance_time(self):
        """
        :returns: The average time in seconds between Task creation and acceptance.
        :rtype: int
        """
        return self._properties['avg_task_acceptance_time']
    
    @property
    def start_time(self):
        """
        :returns: The beginning of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['start_time']
    
    @property
    def end_time(self):
        """
        :returns: The end of the interval during which these statistics were calculated, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['end_time']
    
    @property
    def reservations_created(self):
        """
        :returns: The total number of Reservations that were created for Workers.
        :rtype: int
        """
        return self._properties['reservations_created']
    
    @property
    def reservations_accepted(self):
        """
        :returns: The total number of Reservations accepted by Workers.
        :rtype: int
        """
        return self._properties['reservations_accepted']
    
    @property
    def reservations_rejected(self):
        """
        :returns: The total number of Reservations that were rejected.
        :rtype: int
        """
        return self._properties['reservations_rejected']
    
    @property
    def reservations_timed_out(self):
        """
        :returns: The total number of Reservations that were timed out.
        :rtype: int
        """
        return self._properties['reservations_timed_out']
    
    @property
    def reservations_canceled(self):
        """
        :returns: The total number of Reservations that were canceled.
        :rtype: int
        """
        return self._properties['reservations_canceled']
    
    @property
    def reservations_rescinded(self):
        """
        :returns: The total number of Reservations that were rescinded.
        :rtype: int
        """
        return self._properties['reservations_rescinded']
    
    @property
    def split_by_wait_time(self):
        """
        :returns: A list of objects that describe the number of Tasks canceled and reservations accepted above and below the thresholds specified in seconds.
        :rtype: dict
        """
        return self._properties['split_by_wait_time']
    
    @property
    def wait_duration_until_accepted(self):
        """
        :returns: The wait duration statistics (`avg`, `min`, `max`, `total`) for Tasks that were accepted.
        :rtype: dict
        """
        return self._properties['wait_duration_until_accepted']
    
    @property
    def wait_duration_until_canceled(self):
        """
        :returns: The wait duration statistics (`avg`, `min`, `max`, `total`) for Tasks that were canceled.
        :rtype: dict
        """
        return self._properties['wait_duration_until_canceled']
    
    @property
    def tasks_canceled(self):
        """
        :returns: The total number of Tasks that were canceled.
        :rtype: int
        """
        return self._properties['tasks_canceled']
    
    @property
    def tasks_completed(self):
        """
        :returns: The total number of Tasks that were completed.
        :rtype: int
        """
        return self._properties['tasks_completed']
    
    @property
    def tasks_created(self):
        """
        :returns: The total number of Tasks created.
        :rtype: int
        """
        return self._properties['tasks_created']
    
    @property
    def tasks_deleted(self):
        """
        :returns: The total number of Tasks that were deleted.
        :rtype: int
        """
        return self._properties['tasks_deleted']
    
    @property
    def tasks_moved(self):
        """
        :returns: The total number of Tasks that were moved from one queue to another.
        :rtype: int
        """
        return self._properties['tasks_moved']
    
    @property
    def tasks_timed_out_in_workflow(self):
        """
        :returns: The total number of Tasks that were timed out of their Workflows (and deleted).
        :rtype: int
        """
        return self._properties['tasks_timed_out_in_workflow']
    
    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace.
        :rtype: str
        """
        return self._properties['workspace_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Workspace statistics resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self, end_date=values.unset, minutes=values.unset, start_date=values.unset, task_channel=values.unset, split_by_wait_time=values.unset):
        """
        Fetch the WorkspaceCumulativeStatisticsInstance
        
        :params datetime end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params str task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :params str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. TaskRouter will calculate statistics on up to 10,000 Tasks for any given threshold.

        :returns: The fetched WorkspaceCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsInstance
        """
        return self._proxy.fetch(end_date=end_date, minutes=minutes, start_date=start_date, task_channel=task_channel, split_by_wait_time=split_by_wait_time, )

    async def fetch_async(self, end_date=values.unset, minutes=values.unset, start_date=values.unset, task_channel=values.unset, split_by_wait_time=values.unset):
        """
        Asynchronous coroutine to fetch the WorkspaceCumulativeStatisticsInstance
        
        :params datetime end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params str task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :params str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. TaskRouter will calculate statistics on up to 10,000 Tasks for any given threshold.

        :returns: The fetched WorkspaceCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsInstance
        """
        return await self._proxy.fetch_async(end_date=end_date, minutes=minutes, start_date=start_date, task_channel=task_channel, split_by_wait_time=split_by_wait_time, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceCumulativeStatisticsInstance {}>'.format(context)

class WorkspaceCumulativeStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkspaceCumulativeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace to fetch.

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/CumulativeStatistics'.format(**self._solution)
        
    
    def fetch(self, end_date=values.unset, minutes=values.unset, start_date=values.unset, task_channel=values.unset, split_by_wait_time=values.unset):
        """
        Fetch the WorkspaceCumulativeStatisticsInstance
        
        :params datetime end_date: Only include usage that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params str task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :params str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA. TaskRouter will calculate statistics on up to 10,000 Tasks for any given threshold.

        :returns: The fetched WorkspaceCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_cumulative_statistics.WorkspaceCumulativeStatisticsInstance
        """
        
        data = values.of({ 
            'EndDate': serialize.iso8601_datetime(end_date),
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskChannel': task_channel,
            'SplitByWaitTime': split_by_wait_time,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return WorkspaceCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceCumulativeStatisticsContext {}>'.format(context)


