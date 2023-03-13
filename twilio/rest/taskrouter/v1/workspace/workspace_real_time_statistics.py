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


from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class WorkspaceRealTimeStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkspaceRealTimeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace to fetch.
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a WorkspaceRealTimeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        """
        return WorkspaceRealTimeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __call__(self):
        """
        Constructs a WorkspaceRealTimeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        """
        return WorkspaceRealTimeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkspaceRealTimeStatisticsList>'

class WorkspaceRealTimeStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str):
        """
        Initialize the WorkspaceRealTimeStatisticsInstance
        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'activity_statistics': payload.get('activity_statistics'),
            'longest_task_waiting_age': deserialize.integer(payload.get('longest_task_waiting_age')),
            'longest_task_waiting_sid': payload.get('longest_task_waiting_sid'),
            'tasks_by_priority': payload.get('tasks_by_priority'),
            'tasks_by_status': payload.get('tasks_by_status'),
            'total_tasks': deserialize.integer(payload.get('total_tasks')),
            'total_workers': deserialize.integer(payload.get('total_workers')),
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

        :returns: WorkspaceRealTimeStatisticsContext for this WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        """
        if self._context is None:
            self._context = WorkspaceRealTimeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workspace resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def activity_statistics(self):
        """
        :returns: The number of current Workers by Activity.
        :rtype: list[object]
        """
        return self._properties['activity_statistics']
    
    @property
    def longest_task_waiting_age(self):
        """
        :returns: The age of the longest waiting Task.
        :rtype: int
        """
        return self._properties['longest_task_waiting_age']
    
    @property
    def longest_task_waiting_sid(self):
        """
        :returns: The SID of the longest waiting Task.
        :rtype: str
        """
        return self._properties['longest_task_waiting_sid']
    
    @property
    def tasks_by_priority(self):
        """
        :returns: The number of Tasks by priority. For example: `{\"0\": \"10\", \"99\": \"5\"}` shows 10 Tasks at priority 0 and 5 at priority 99.
        :rtype: dict
        """
        return self._properties['tasks_by_priority']
    
    @property
    def tasks_by_status(self):
        """
        :returns: The number of Tasks by their current status. For example: `{\"pending\": \"1\", \"reserved\": \"3\", \"assigned\": \"2\", \"completed\": \"5\"}`.
        :rtype: dict
        """
        return self._properties['tasks_by_status']
    
    @property
    def total_tasks(self):
        """
        :returns: The total number of Tasks.
        :rtype: int
        """
        return self._properties['total_tasks']
    
    @property
    def total_workers(self):
        """
        :returns: The total number of Workers in the Workspace.
        :rtype: int
        """
        return self._properties['total_workers']
    
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
    
    def fetch(self, task_channel=values.unset):
        """
        Fetch the WorkspaceRealTimeStatisticsInstance
        
        :params str task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        """
        return self._proxy.fetch(task_channel=task_channel, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkspaceRealTimeStatisticsInstance {}>'.format(context)

class WorkspaceRealTimeStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkspaceRealTimeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace to fetch.

        :returns: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/RealTimeStatistics'.format(**self._solution)
        
    
    def fetch(self, task_channel=values.unset):
        """
        Fetch the WorkspaceRealTimeStatisticsInstance
        
        :params str task_channel: Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched WorkspaceRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.workspace_real_time_statistics.WorkspaceRealTimeStatisticsInstance
        """
        
        data = values.of({ 
            'TaskChannel': task_channel,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return WorkspaceRealTimeStatisticsInstance(
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
        return '<Twilio.Taskrouter.V1.WorkspaceRealTimeStatisticsContext {}>'.format(context)


