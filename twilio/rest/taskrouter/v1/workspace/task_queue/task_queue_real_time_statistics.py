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
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class TaskQueueRealTimeStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str, task_queue_sid: str):
        """
        Initialize the TaskQueueRealTimeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch.
        :param task_queue_sid: The SID of the TaskQueue for which to fetch statistics.
        
        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a TaskQueueRealTimeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        return TaskQueueRealTimeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'], task_queue_sid=self._solution['task_queue_sid'])

    def __call__(self):
        """
        Constructs a TaskQueueRealTimeStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        return TaskQueueRealTimeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'], task_queue_sid=self._solution['task_queue_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsList>'

class TaskQueueRealTimeStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str, task_queue_sid: str):
        """
        Initialize the TaskQueueRealTimeStatisticsInstance
        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'activity_statistics': payload.get('activity_statistics'),
            'longest_task_waiting_age': deserialize.integer(payload.get('longest_task_waiting_age')),
            'longest_task_waiting_sid': payload.get('longest_task_waiting_sid'),
            'longest_relative_task_age_in_queue': deserialize.integer(payload.get('longest_relative_task_age_in_queue')),
            'longest_relative_task_sid_in_queue': payload.get('longest_relative_task_sid_in_queue'),
            'task_queue_sid': payload.get('task_queue_sid'),
            'tasks_by_priority': payload.get('tasks_by_priority'),
            'tasks_by_status': payload.get('tasks_by_status'),
            'total_available_workers': deserialize.integer(payload.get('total_available_workers')),
            'total_eligible_workers': deserialize.integer(payload.get('total_eligible_workers')),
            'total_tasks': deserialize.integer(payload.get('total_tasks')),
            'workspace_sid': payload.get('workspace_sid'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskQueueRealTimeStatisticsContext for this TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        if self._context is None:
            self._context = TaskQueueRealTimeStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'], task_queue_sid=self._solution['task_queue_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource.
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
    def longest_relative_task_age_in_queue(self):
        """
        :returns: The relative age in the TaskQueue for the longest waiting Task. Calculation is based on the time when the Task entered the TaskQueue.
        :rtype: int
        """
        return self._properties['longest_relative_task_age_in_queue']
    
    @property
    def longest_relative_task_sid_in_queue(self):
        """
        :returns: The Task SID of the Task waiting in the TaskQueue the longest. Calculation is based on the time when the Task entered the TaskQueue.
        :rtype: str
        """
        return self._properties['longest_relative_task_sid_in_queue']
    
    @property
    def task_queue_sid(self):
        """
        :returns: The SID of the TaskQueue from which these statistics were calculated.
        :rtype: str
        """
        return self._properties['task_queue_sid']
    
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
    def total_available_workers(self):
        """
        :returns: The total number of Workers available for Tasks in the TaskQueue.
        :rtype: int
        """
        return self._properties['total_available_workers']
    
    @property
    def total_eligible_workers(self):
        """
        :returns: The total number of Workers eligible for Tasks in the TaskQueue, independent of their Activity state.
        :rtype: int
        """
        return self._properties['total_eligible_workers']
    
    @property
    def total_tasks(self):
        """
        :returns: The total number of Tasks.
        :rtype: int
        """
        return self._properties['total_tasks']
    
    @property
    def workspace_sid(self):
        """
        :returns: The SID of the Workspace that contains the TaskQueue.
        :rtype: str
        """
        return self._properties['workspace_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the TaskQueue statistics resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self, task_channel=values.unset):
        """
        Fetch the TaskQueueRealTimeStatisticsInstance
        
        :params str task_channel: The TaskChannel for which to fetch statistics. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        return self._proxy.fetch(task_channel=task_channel, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsInstance {}>'.format(context)

class TaskQueueRealTimeStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str, task_queue_sid: str):
        """
        Initialize the TaskQueueRealTimeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to fetch.:param task_queue_sid: The SID of the TaskQueue for which to fetch statistics.

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
            'task_queue_sid': task_queue_sid,
        }
        self._uri = '/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/RealTimeStatistics'.format(**self._solution)
        
    
    def fetch(self, task_channel=values.unset):
        """
        Fetch the TaskQueueRealTimeStatisticsInstance
        
        :params str task_channel: The TaskChannel for which to fetch statistics. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.

        :returns: The fetched TaskQueueRealTimeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics.TaskQueueRealTimeStatisticsInstance
        """
        
        data = values.of({ 
            'TaskChannel': task_channel,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return TaskQueueRealTimeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueRealTimeStatisticsContext {}>'.format(context)


