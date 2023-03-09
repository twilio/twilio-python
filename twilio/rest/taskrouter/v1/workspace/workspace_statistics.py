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



class WorkspaceStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkspaceStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace to fetch.
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a WorkspaceStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsContext
        """
        return WorkspaceStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __call__(self):
        """
        Constructs a WorkspaceStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsContext
        """
        return WorkspaceStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceStatisticsList>'

class WorkspaceStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str):
        """
        Initialize the WorkspaceStatisticsInstance
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsInstance
        """
        super().__init__(version)

        self._properties = { 
            'realtime': payload.get('realtime'),
            'cumulative': payload.get('cumulative'),
            'account_sid': payload.get('account_sid'),
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

        :returns: WorkspaceStatisticsContext for this WorkspaceStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsContext
        """
        if self._context is None:
            self._context = WorkspaceStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'],)
        return self._context
    
    @property
    def realtime(self):
        """
        :returns: An object that contains the real-time statistics for the Workspace.
        :rtype: dict
        """
        return self._properties['realtime']
    
    @property
    def cumulative(self):
        """
        :returns: An object that contains the cumulative statistics for the Workspace.
        :rtype: dict
        """
        return self._properties['cumulative']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workspace resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
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
    
    
    def fetch(self, minutes=values.unset, start_date=values.unset, end_date=values.unset, task_channel=values.unset, split_by_wait_time=values.unset):
        """
        Fetch the WorkspaceStatisticsInstance
        
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :params str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :params str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkspaceStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsInstance
        """
        return self._proxy.fetch(minutes=minutes, start_date=start_date, end_date=end_date, task_channel=task_channel, split_by_wait_time=split_by_wait_time, )

    async def fetch_async(self, minutes=values.unset, start_date=values.unset, end_date=values.unset, task_channel=values.unset, split_by_wait_time=values.unset):
        """
        Asynchronous coroutine to fetch the WorkspaceStatisticsInstance
        
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :params str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :params str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkspaceStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsInstance
        """
        return await self._proxy.fetch_async(minutes=minutes, start_date=start_date, end_date=end_date, task_channel=task_channel, split_by_wait_time=split_by_wait_time, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceStatisticsInstance {}>'.format(context)

class WorkspaceStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkspaceStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace to fetch.

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/Statistics'.format(**self._solution)
        
    
    def fetch(self, minutes=values.unset, start_date=values.unset, end_date=values.unset, task_channel=values.unset, split_by_wait_time=values.unset):
        """
        Fetch the WorkspaceStatisticsInstance
        
        :params int minutes: Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
        :params datetime start_date: Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :params datetime end_date: Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
        :params str task_channel: Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
        :params str split_by_wait_time: A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. For example, `5,30` would show splits of Tasks that were canceled or accepted before and after 5 seconds and before and after 30 seconds. This can be used to show short abandoned Tasks or Tasks that failed to meet an SLA.

        :returns: The fetched WorkspaceStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_statistics.WorkspaceStatisticsInstance
        """
        
        data = values.of({ 
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'EndDate': serialize.iso8601_datetime(end_date),
            'TaskChannel': task_channel,
            'SplitByWaitTime': split_by_wait_time,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return WorkspaceStatisticsInstance(
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
        return '<Twilio.Taskrouter.V1.WorkspaceStatisticsContext {}>'.format(context)


