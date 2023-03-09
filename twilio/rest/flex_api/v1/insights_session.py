r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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



class InsightsSessionList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the InsightsSessionList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.flex_api.v1.insights_session.InsightsSessionList
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    def create(self, authorization=values.unset):
        """
        Create the InsightsSessionInstance

        :param str authorization: The Authorization HTTP request header
        
        :returns: The created InsightsSessionInstance
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionInstance
        """
        data = values.of({ 
        })
        headers = values.of({'Authorization': authorization, })
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return InsightsSessionInstance(self._version, payload)

    async def create_async(self, authorization=values.unset):
        """
        Asynchronously create the InsightsSessionInstance

        :param str authorization: The Authorization HTTP request header
        
        :returns: The created InsightsSessionInstance
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionInstance
        """
        data = values.of({ 
        })
        headers = values.of({'Authorization': authorization, })
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return InsightsSessionInstance(self._version, payload)
    

    def get(self):
        """
        Constructs a InsightsSessionContext
        
        :returns: twilio.rest.flex_api.v1.insights_session.InsightsSessionContext
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionContext
        """
        return InsightsSessionContext(self._version)

    def __call__(self):
        """
        Constructs a InsightsSessionContext
        
        :returns: twilio.rest.flex_api.v1.insights_session.InsightsSessionContext
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionContext
        """
        return InsightsSessionContext(self._version)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.FlexApi.V1.InsightsSessionList>'

class InsightsSessionInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the InsightsSessionInstance
        :returns: twilio.rest.flex_api.v1.insights_session.InsightsSessionInstance
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionInstance
        """
        super().__init__(version)

        self._properties = { 
            'workspace_id': payload.get('workspace_id'),
            'session_expiry': payload.get('session_expiry'),
            'session_id': payload.get('session_id'),
            'base_url': payload.get('base_url'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: InsightsSessionContext for this InsightsSessionInstance
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionContext
        """
        if self._context is None:
            self._context = InsightsSessionContext(self._version,)
        return self._context
    
    @property
    def workspace_id(self):
        """
        :returns: Unique ID to identify the user's workspace
        :rtype: str
        """
        return self._properties['workspace_id']
    
    @property
    def session_expiry(self):
        """
        :returns: The session expiry date and time, given in ISO 8601 format.
        :rtype: str
        """
        return self._properties['session_expiry']
    
    @property
    def session_id(self):
        """
        :returns: The unique ID for the session
        :rtype: str
        """
        return self._properties['session_id']
    
    @property
    def base_url(self):
        """
        :returns: The base URL to fetch reports and dashboards
        :rtype: str
        """
        return self._properties['base_url']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def create(self, authorization=values.unset):
        """
        Create the InsightsSessionInstance
        
        :param str authorization: The Authorization HTTP request header

        :returns: The created InsightsSessionInstance
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionInstance
        """
        return self._proxy.create(authorization=authorization, )
    async def create_async(self, authorization=values.unset):
        """
        Asynchronous coroutine to create the InsightsSessionInstance
        
        :param str authorization: The Authorization HTTP request header

        :returns: The created InsightsSessionInstance
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionInstance
        """
        return await self._proxy.create_async(authorization=authorization, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsSessionInstance {}>'.format(context)

class InsightsSessionContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the InsightsSessionContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.flex_api.v1.insights_session.InsightsSessionContext
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
        }
        self._uri = '/Insights/Session'.format(**self._solution)
        
    
    
    def create(self, authorization=values.unset):
        """
        Create the InsightsSessionInstance
        
        :param str authorization: The Authorization HTTP request header

        :returns: The created InsightsSessionInstance
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionInstance
        """
        data = values.of({ 
            'Authorization': authorization,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)

        return InsightsSessionInstance(
            self._version,
            payload
        )

    async def create_async(self, authorization=values.unset):
        """
        Asynchronous coroutine to create the InsightsSessionInstance
        
        :param str authorization: The Authorization HTTP request header

        :returns: The created InsightsSessionInstance
        :rtype: twilio.rest.flex_api.v1.insights_session.InsightsSessionInstance
        """
        data = values.of({ 
            'Authorization': authorization,
        })

        payload = await self._version.create_async(method='POST', uri=self._uri, data=data)

        return InsightsSessionInstance(
            self._version,
            payload
        )
    
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.FlexApi.V1.InsightsSessionContext {}>'.format(context)


