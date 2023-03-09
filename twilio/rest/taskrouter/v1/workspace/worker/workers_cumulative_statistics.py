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



class WorkersCumulativeStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersCumulativeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the resource to fetch.
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a WorkersCumulativeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        return WorkersCumulativeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __call__(self):
        """
        Constructs a WorkersCumulativeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        return WorkersCumulativeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsList>'

class WorkersCumulativeStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str):
        """
        Initialize the WorkersCumulativeStatisticsInstance
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'start_time': deserialize.iso8601_datetime(payload.get('start_time')),
            'end_time': deserialize.iso8601_datetime(payload.get('end_time')),
            'activity_durations': payload.get('activity_durations'),
            'reservations_created': deserialize.integer(payload.get('reservations_created')),
            'reservations_accepted': deserialize.integer(payload.get('reservations_accepted')),
            'reservations_rejected': deserialize.integer(payload.get('reservations_rejected')),
            'reservations_timed_out': deserialize.integer(payload.get('reservations_timed_out')),
            'reservations_canceled': deserialize.integer(payload.get('reservations_canceled')),
            'reservations_rescinded': deserialize.integer(payload.get('reservations_rescinded')),
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

        :returns: WorkersCumulativeStatisticsContext for this WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        if self._context is None:
            self._context = WorkersCumulativeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
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
    def activity_durations(self):
        """
        :returns: The minimum, average, maximum, and total time (in seconds) that Workers spent in each Activity.
        :rtype: list[object]
        """
        return self._properties['activity_durations']
    
    @property
    def reservations_created(self):
        """
        :returns: The total number of Reservations that were created.
        :rtype: int
        """
        return self._properties['reservations_created']
    
    @property
    def reservations_accepted(self):
        """
        :returns: The total number of Reservations that were accepted.
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
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the Workers.
        :rtype: str
        """
        return self._properties['workspace_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Workers statistics resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self, end_date=values.unset, minutes=values.unset, start_date=values.unset, task_channel=values.unset):
        """
        Fetch the WorkersCumulativeStatisticsInstance
        
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params str task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        return self._proxy.fetch(end_date=end_date, minutes=minutes, start_date=start_date, task_channel=task_channel, )

    async def fetch_async(self, end_date=values.unset, minutes=values.unset, start_date=values.unset, task_channel=values.unset):
        """
        Asynchronous coroutine to fetch the WorkersCumulativeStatisticsInstance
        
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params str task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        return await self._proxy.fetch_async(end_date=end_date, minutes=minutes, start_date=start_date, task_channel=task_channel, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsInstance {}>'.format(context)

class WorkersCumulativeStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersCumulativeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the resource to fetch.

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Workers/CumulativeStatistics'.format(**self._solution)
        
    
    
    def fetch(self, end_date=values.unset, minutes=values.unset, start_date=values.unset, task_channel=values.unset):
        """
        Fetch the WorkersCumulativeStatisticsInstance
        
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params str task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        
        data = values.of({ 
            'EndDate': serialize.iso8601_datetime(end_date),
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskChannel': task_channel,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return WorkersCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            
        )

    async def fetch_async(self, end_date=values.unset, minutes=values.unset, start_date=values.unset, task_channel=values.unset):
        """
        Asynchronous coroutine to fetch the WorkersCumulativeStatisticsInstance
        
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params str task_channel: Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkersCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_cumulative_statistics.WorkersCumulativeStatisticsInstance
        """
        
        data = values.of({ 
            'EndDate': serialize.iso8601_datetime(end_date),
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskChannel': task_channel,
        })
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, params=data)

        return WorkersCumulativeStatisticsInstance(
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
        return '<Twilio.Taskrouter.V1.WorkersCumulativeStatisticsContext {}>'.format(context)


