"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
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



class ExecutionStepContextList(ListResource):

    def __init__(self, version: Version, flow_sid: str, execution_sid: str, step_sid: str):
        """
        Initialize the ExecutionStepContextList

        :param Version version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Step to fetch.
        :param execution_sid: The SID of the Execution resource with the Step to fetch.
        :param step_sid: The SID of the Step to fetch.
        
        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextList
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'execution_sid': execution_sid, 'step_sid': step_sid,  }
        
        
        
    

    def get(self):
        """
        Constructs a ExecutionStepContextContext
        
        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        """
        return ExecutionStepContextContext(self._version, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'], step_sid=self._solution['step_sid'])

    def __call__(self):
        """
        Constructs a ExecutionStepContextContext
        
        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        """
        return ExecutionStepContextContext(self._version, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'], step_sid=self._solution['step_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V1.ExecutionStepContextList>'

class ExecutionStepContextInstance(InstanceResource):

    def __init__(self, version, payload, flow_sid: str, execution_sid: str, step_sid: str):
        """
        Initialize the ExecutionStepContextInstance
        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'context': payload.get('context'),
            'execution_sid': payload.get('execution_sid'),
            'flow_sid': payload.get('flow_sid'),
            'step_sid': payload.get('step_sid'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'flow_sid': flow_sid, 'execution_sid': execution_sid, 'step_sid': step_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ExecutionStepContextContext for this ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        """
        if self._context is None:
            self._context = ExecutionStepContextContext(self._version, flow_sid=self._solution['flow_sid'], execution_sid=self._solution['execution_sid'], step_sid=self._solution['step_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ExecutionStepContext resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def context(self):
        """
        :returns: The current state of the Flow's Execution. As a flow executes, we save its state in this context. We save data that your widgets can access as variables in configuration fields or in text areas as variable substitution.
        :rtype: dict
        """
        return self._properties['context']
    
    @property
    def execution_sid(self):
        """
        :returns: The SID of the context's Execution resource.
        :rtype: str
        """
        return self._properties['execution_sid']
    
    @property
    def flow_sid(self):
        """
        :returns: The SID of the Flow.
        :rtype: str
        """
        return self._properties['flow_sid']
    
    @property
    def step_sid(self):
        """
        :returns: The SID of the Step that the context is associated with.
        :rtype: str
        """
        return self._properties['step_sid']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the ExecutionStepContextInstance
        

        :returns: The fetched ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionStepContextInstance {}>'.format(context)

class ExecutionStepContextContext(InstanceContext):

    def __init__(self, version: Version, flow_sid: str, execution_sid: str, step_sid: str):
        """
        Initialize the ExecutionStepContextContext

        :param Version version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Step to fetch.
        :param execution_sid: The SID of the Execution resource with the Step to fetch.
        :param step_sid: The SID of the Step to fetch.

        :returns: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'flow_sid': flow_sid,
            'execution_sid': execution_sid,
            'step_sid': step_sid,
        }
        self._uri = '/Flows/{flow_sid}/Executions/{execution_sid}/Steps/{step_sid}/Context'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the ExecutionStepContextInstance
        

        :returns: The fetched ExecutionStepContextInstance
        :rtype: twilio.rest.studio.v1.flow.execution.execution_step.execution_step_context.ExecutionStepContextInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ExecutionStepContextInstance(
            self._version,
            payload,
            flow_sid=self._solution['flow_sid'],
            execution_sid=self._solution['execution_sid'],
            step_sid=self._solution['step_sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V1.ExecutionStepContextContext {}>'.format(context)


