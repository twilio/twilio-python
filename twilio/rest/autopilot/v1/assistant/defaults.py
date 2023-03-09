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



class DefaultsList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the DefaultsList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
        
        :returns: twilio.rest.autopilot.v1.assistant.defaults.DefaultsList
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        
        
        
    
    

    def get(self):
        """
        Constructs a DefaultsContext
        
        :returns: twilio.rest.autopilot.v1.assistant.defaults.DefaultsContext
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsContext
        """
        return DefaultsContext(self._version, assistant_sid=self._solution['assistant_sid'])

    def __call__(self):
        """
        Constructs a DefaultsContext
        
        :returns: twilio.rest.autopilot.v1.assistant.defaults.DefaultsContext
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsContext
        """
        return DefaultsContext(self._version, assistant_sid=self._solution['assistant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.DefaultsList>'

class DefaultsInstance(InstanceResource):

    def __init__(self, version, payload, assistant_sid: str):
        """
        Initialize the DefaultsInstance
        :returns: twilio.rest.autopilot.v1.assistant.defaults.DefaultsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'assistant_sid': payload.get('assistant_sid'),
            'url': payload.get('url'),
            'data': payload.get('data'),
        }

        self._context = None
        self._solution = { 'assistant_sid': assistant_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DefaultsContext for this DefaultsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsContext
        """
        if self._context is None:
            self._context = DefaultsContext(self._version, assistant_sid=self._solution['assistant_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Defaults resource.
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
    def url(self):
        """
        :returns: The absolute URL of the Defaults resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def data(self):
        """
        :returns: The JSON string that describes the default task links for the `assistant_initiation`, `collect`, and `fallback` situations.
        :rtype: dict
        """
        return self._properties['data']
    
    
    def fetch(self):
        """
        Fetch the DefaultsInstance
        

        :returns: The fetched DefaultsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the DefaultsInstance
        

        :returns: The fetched DefaultsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, defaults=values.unset):
        """
        Update the DefaultsInstance
        
        :params object defaults: A JSON string that describes the default task links for the `assistant_initiation`, `collect`, and `fallback` situations.

        :returns: The updated DefaultsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsInstance
        """
        return self._proxy.update(defaults=defaults, )

    async def update_async(self, defaults=values.unset):
        """
        Asynchronous coroutine to update the DefaultsInstance
        
        :params object defaults: A JSON string that describes the default task links for the `assistant_initiation`, `collect`, and `fallback` situations.

        :returns: The updated DefaultsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsInstance
        """
        return await self._proxy.update_async(defaults=defaults, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.DefaultsInstance {}>'.format(context)

class DefaultsContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the DefaultsContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.

        :returns: twilio.rest.autopilot.v1.assistant.defaults.DefaultsContext
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
        }
        self._uri = '/Assistants/{assistant_sid}/Defaults'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the DefaultsInstance
        

        :returns: The fetched DefaultsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DefaultsInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            
        )
        
    def update(self, defaults=values.unset):
        """
        Update the DefaultsInstance
        
        :params object defaults: A JSON string that describes the default task links for the `assistant_initiation`, `collect`, and `fallback` situations.

        :returns: The updated DefaultsInstance
        :rtype: twilio.rest.autopilot.v1.assistant.defaults.DefaultsInstance
        """
        data = values.of({ 
            'Defaults': serialize.object(defaults),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return DefaultsInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.DefaultsContext {}>'.format(context)


