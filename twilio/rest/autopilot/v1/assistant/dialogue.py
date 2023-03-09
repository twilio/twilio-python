r"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class DialogueList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the DialogueList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
        
        :returns: twilio.rest.autopilot.v1.assistant.dialogue.DialogueList
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        
        
        
    

    def get(self, sid):
        """
        Constructs a DialogueContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Dialogue resource to fetch.
        
        :returns: twilio.rest.autopilot.v1.assistant.dialogue.DialogueContext
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueContext
        """
        return DialogueContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a DialogueContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Dialogue resource to fetch.
        
        :returns: twilio.rest.autopilot.v1.assistant.dialogue.DialogueContext
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueContext
        """
        return DialogueContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.DialogueList>'

class DialogueInstance(InstanceResource):

    def __init__(self, version, payload, assistant_sid: str, sid: str=None):
        """
        Initialize the DialogueInstance
        :returns: twilio.rest.autopilot.v1.assistant.dialogue.DialogueInstance
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'data': payload.get('data'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DialogueContext for this DialogueInstance
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueContext
        """
        if self._context is None:
            self._context = DialogueContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Dialogue resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def assistant_sid(self):
        """
        :returns: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource.
        :rtype: str
        """
        return self._properties['assistant_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Dialogue resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def data(self):
        """
        :returns: The JSON string that describes the dialogue session object.
        :rtype: dict
        """
        return self._properties['data']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Dialogue resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self):
        """
        Fetch the DialogueInstance
        

        :returns: The fetched DialogueInstance
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the DialogueInstance
        

        :returns: The fetched DialogueInstance
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.DialogueInstance {}>'.format(context)

class DialogueContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str, sid: str):
        """
        Initialize the DialogueContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the Dialogue resource to fetch.

        :returns: twilio.rest.autopilot.v1.assistant.dialogue.DialogueContext
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
            'sid': sid,
        }
        self._uri = '/Assistants/{assistant_sid}/Dialogues/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the DialogueInstance
        

        :returns: The fetched DialogueInstance
        :rtype: twilio.rest.autopilot.v1.assistant.dialogue.DialogueInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DialogueInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.DialogueContext {}>'.format(context)


