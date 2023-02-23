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
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class WorkersStatisticsList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Worker to fetch.
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a WorkersStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        """
        return WorkersStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __call__(self):
        """
        Constructs a WorkersStatisticsContext
        
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        """
        return WorkersStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.WorkersStatisticsList>'

class WorkersStatisticsContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the WorkersStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the Worker to fetch.

        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'workspace_sid': workspace_sid,
        }
        self._uri = '/Workspaces/${workspace_sid}/Workers/Statistics'.format(**self._solution)
        
    
    def fetch(self, minutes=values.unset, start_date=values.unset, end_date=values.unset, task_queue_sid=values.unset, task_queue_name=values.unset, friendly_name=values.unset, task_channel=values.unset):
        """
        Fetch the WorkersStatisticsInstance

        :returns: The fetched WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return WorkersStatisticsInstance(
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
        return '<Twilio.Taskrouter.V1.WorkersStatisticsContext {}>'.format(context)

class WorkersStatisticsInstance(InstanceResource):

    def __init__(self, version, payload, workspace_sid: str):
        """
        Initialize the WorkersStatisticsInstance
        :returns: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
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

        :returns: WorkersStatisticsContext for this WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsContext
        """
        if self._context is None:
            self._context = WorkersStatisticsContext(self._version, workspace_sid=self._solution['workspace_sid'],)
        return self._context
    
    @property
    def realtime(self):
        """
        :returns: An object that contains the real-time statistics for the Worker.
        :rtype: dict
        """
        return self._properties['realtime']
    
    @property
    def cumulative(self):
        """
        :returns: An object that contains the cumulative statistics for the Worker.
        :rtype: dict
        """
        return self._properties['cumulative']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Worker resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
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
        :returns: The absolute URL of the Worker statistics resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self, minutes=values.unset, start_date=values.unset, end_date=values.unset, task_queue_sid=values.unset, task_queue_name=values.unset, friendly_name=values.unset, task_channel=values.unset):
        """
        Fetch the WorkersStatisticsInstance

        :returns: The fetched WorkersStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.worker.workers_statistics.WorkersStatisticsInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.WorkersStatisticsInstance {}>'.format(context)


