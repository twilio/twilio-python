"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
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



class TaskStatisticsList(ListResource):

    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        """
        Initialize the TaskStatisticsList
        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
        :param task_sid: The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) that is associated with the resource to fetch.
        
        :returns: twilio.autopilot.v1.task_statistics..TaskStatisticsList
        :rtype: twilio.autopilot.v1.task_statistics..TaskStatisticsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a TaskStatisticsContext
        
        :returns: twilio.rest.autopilot.v1.task_statistics.TaskStatisticsContext
        :rtype: twilio.rest.autopilot.v1.task_statistics.TaskStatisticsContext
        """
        return TaskStatisticsContext(self._version, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'])

    def __call__(self):
        """
        Constructs a TaskStatisticsContext
        
        :returns: twilio.rest.autopilot.v1.task_statistics.TaskStatisticsContext
        :rtype: twilio.rest.autopilot.v1.task_statistics.TaskStatisticsContext
        """
        return TaskStatisticsContext(self._version, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.TaskStatisticsList>'


class TaskStatisticsContext(InstanceContext):
    def __init__(self, version: Version, assistant_sid: str, task_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid, 'task_sid': task_sid,  }
        self._uri = '/Assistants/${assistant_sid}/Tasks/${task_sid}/Statistics'
        
    
    def fetch(self):
        
        """
        Fetch the TaskStatisticsInstance

        :returns: The fetched TaskStatisticsInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TaskStatisticsInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], task_sid=self._solution['task_sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.TaskStatisticsContext>'



class TaskStatisticsInstance(InstanceResource):
    def __init__(self, version, payload, assistant_sid: str, task_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'assistant_sid' : payload.get('assistant_sid'),
            'task_sid' : payload.get('task_sid'),
            'samples_count' : payload.get('samples_count'),
            'fields_count' : payload.get('fields_count'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'assistant_sid': assistant_sid or self._properties['assistant_sid'],'task_sid': task_sid or self._properties['task_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TaskStatisticsContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],task_sid=self._solution['task_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.TaskStatisticsInstance {}>'.format(context)



