r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date, datetime
from decimal import Decimal
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class FunctionVersionContentInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Function Version resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Function Version resource.
    :ivar service_sid: The SID of the Service that the Function Version resource is associated with.
    :ivar function_sid: The SID of the Function that is the parent of the Function Version.
    :ivar content: The content of the Function Version resource.
    :ivar url: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], service_sid: str, function_sid: str, sid: str):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.function_sid: Optional[str] = payload.get("function_sid")
        self.content: Optional[str] = payload.get("content")
        self.url: Optional[str] = payload.get("url")

        
        self._solution = { 
            "service_sid": service_sid,
            "function_sid": function_sid,
            "sid": sid,
        }
        self._context: Optional[FunctionVersionContentContext] = None

    @property
    def _proxy(self) -> "FunctionVersionContentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FunctionVersionContentContext for this FunctionVersionContentInstance
        """
        if self._context is None:
            self._context = FunctionVersionContentContext(self._version, service_sid=self._solution['service_sid'], function_sid=self._solution['function_sid'], sid=self._solution['sid'],)
        return self._context
    
    
    def fetch(self) -> "FunctionVersionContentInstance":
        """
        Fetch the FunctionVersionContentInstance
        

        :returns: The fetched FunctionVersionContentInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "FunctionVersionContentInstance":
        """
        Asynchronous coroutine to fetch the FunctionVersionContentInstance
        

        :returns: The fetched FunctionVersionContentInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionVersionContentInstance {}>'.format(context)

class FunctionVersionContentContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, function_sid: str, sid: str):
        """
        Initialize the FunctionVersionContentContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Function Version content from.
        :param function_sid: The SID of the Function that is the parent of the Function Version content to fetch.
        :param sid: The SID of the Function Version content to fetch.
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'function_sid': function_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}/Content'.format(**self._solution)
        
    
    
    def fetch(self) -> FunctionVersionContentInstance:
        """
        Fetch the FunctionVersionContentInstance
        

        :returns: The fetched FunctionVersionContentInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FunctionVersionContentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            function_sid=self._solution['function_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> FunctionVersionContentInstance:
        """
        Asynchronous coroutine to fetch the FunctionVersionContentInstance
        

        :returns: The fetched FunctionVersionContentInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return FunctionVersionContentInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            function_sid=self._solution['function_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionVersionContentContext {}>'.format(context)



class FunctionVersionContentList(ListResource):
    
    def __init__(self, version: Version, service_sid: str, function_sid: str, sid: str):
        """
        Initialize the FunctionVersionContentList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Function Version content from.
        :param function_sid: The SID of the Function that is the parent of the Function Version content to fetch.
        :param sid: The SID of the Function Version content to fetch.
        
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 'service_sid': service_sid, 'function_sid': function_sid, 'sid': sid,  }
        
        
        

    def get(self) -> FunctionVersionContentContext:
        """
        Constructs a FunctionVersionContentContext
        
        """
        return FunctionVersionContentContext(self._version, service_sid=self._solution['service_sid'], function_sid=self._solution['function_sid'], sid=self._solution['sid'])

    def __call__(self) -> FunctionVersionContentContext:
        """
        Constructs a FunctionVersionContentContext
        
        """
        return FunctionVersionContentContext(self._version, service_sid=self._solution['service_sid'], function_sid=self._solution['function_sid'], sid=self._solution['sid'])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Serverless.V1.FunctionVersionContentList>'

