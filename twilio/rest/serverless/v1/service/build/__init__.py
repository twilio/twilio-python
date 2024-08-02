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
from twilio.base.page import Page
from twilio.rest.serverless.v1.service.build.build_status import BuildStatusList


class BuildInstance(InstanceResource):

    class Runtime(object):
        NODE8 = "node8"
        NODE10 = "node10"
        NODE12 = "node12"
        NODE14 = "node14"
        NODE16 = "node16"
        NODE18 = "node18"

    class Status(object):
        BUILDING = "building"
        COMPLETED = "completed"
        FAILED = "failed"

    """
    :ivar sid: The unique string that we created to identify the Build resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Build resource.
    :ivar service_sid: The SID of the Service that the Build resource is associated with.
    :ivar status: 
    :ivar asset_versions: The list of Asset Version resource SIDs that are included in the Build.
    :ivar function_versions: The list of Function Version resource SIDs that are included in the Build.
    :ivar dependencies: A list of objects that describe the Dependencies included in the Build. Each object contains the `name` and `version` of the dependency.
    :ivar runtime: 
    :ivar date_created: The date and time in GMT when the Build resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Build resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Build resource.
    :ivar links: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], service_sid: str, sid: Optional[str] = None):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.service_sid: Optional[str] = payload.get("service_sid")
        self.status: Optional["BuildInstance.Status"] = payload.get("status")
        self.asset_versions: Optional[List[Dict[str, object]]] = payload.get("asset_versions")
        self.function_versions: Optional[List[Dict[str, object]]] = payload.get("function_versions")
        self.dependencies: Optional[List[Dict[str, object]]] = payload.get("dependencies")
        self.runtime: Optional["BuildInstance.Runtime"] = payload.get("runtime")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_created"))
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_updated"))
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        
        self._solution = { 
            "service_sid": service_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[BuildContext] = None

    @property
    def _proxy(self) -> "BuildContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BuildContext for this BuildInstance
        """
        if self._context is None:
            self._context = BuildContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    
    def delete(self) -> bool:
        """
        Deletes the BuildInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()
    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the BuildInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()
    
    
    def fetch(self) -> "BuildInstance":
        """
        Fetch the BuildInstance
        

        :returns: The fetched BuildInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "BuildInstance":
        """
        Asynchronous coroutine to fetch the BuildInstance
        

        :returns: The fetched BuildInstance
        """
        return await self._proxy.fetch_async()
    
    @property
    def build_status(self) -> BuildStatusList:
        """
        Access the build_status
        """
        return self._proxy.build_status
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildInstance {}>'.format(context)

class BuildContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BuildContext

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Build resource from.
        :param sid: The SID of the Build resource to fetch.
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Builds/{sid}'.format(**self._solution)
        
        self._build_status: Optional[BuildStatusList] = None
    
    
    def delete(self) -> bool:
        """
        Deletes the BuildInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(method='DELETE', uri=self._uri,)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the BuildInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(method='DELETE', uri=self._uri,)
    
    
    def fetch(self) -> BuildInstance:
        """
        Fetch the BuildInstance
        

        :returns: The fetched BuildInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BuildInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )

    async def fetch_async(self) -> BuildInstance:
        """
        Asynchronous coroutine to fetch the BuildInstance
        

        :returns: The fetched BuildInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return BuildInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
    
    
    @property
    def build_status(self) -> BuildStatusList:
        """
        Access the build_status
        """
        if self._build_status is None:
            self._build_status = BuildStatusList(
                self._version, 
                self._solution['service_sid'],
                self._solution['sid'],
            )
        return self._build_status
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildContext {}>'.format(context)









class BuildPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> BuildInstance:
        """
        Build an instance of BuildInstance

        :param payload: Payload response from the API
        """
        return BuildInstance(self._version, payload, service_sid=self._solution["service_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.BuildPage>"





class BuildList(ListResource):
    
    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the BuildList

        :param version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Build resources from.
        
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Builds'.format(**self._solution)
        
        
    
    
    
    def create(self, asset_versions: Union[List[str], object]=values.unset, function_versions: Union[List[str], object]=values.unset, dependencies: Union[str, object]=values.unset, runtime: Union[str, object]=values.unset) -> BuildInstance:
        """
        Create the BuildInstance

        :param asset_versions: The list of Asset Version resource SIDs to include in the Build.
        :param function_versions: The list of the Function Version resource SIDs to include in the Build.
        :param dependencies: A list of objects that describe the Dependencies included in the Build. Each object contains the `name` and `version` of the dependency.
        :param runtime: The Runtime version that will be used to run the Build resource when it is deployed.
        
        :returns: The created BuildInstance
        """
        
        data = values.of({ 
            'AssetVersions': serialize.map(asset_versions, lambda e: e),
            'FunctionVersions': serialize.map(function_versions, lambda e: e),
            'Dependencies': dependencies,
            'Runtime': runtime,
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return BuildInstance(self._version, payload, service_sid=self._solution['service_sid'])

    async def create_async(self, asset_versions: Union[List[str], object]=values.unset, function_versions: Union[List[str], object]=values.unset, dependencies: Union[str, object]=values.unset, runtime: Union[str, object]=values.unset) -> BuildInstance:
        """
        Asynchronously create the BuildInstance

        :param asset_versions: The list of Asset Version resource SIDs to include in the Build.
        :param function_versions: The list of the Function Version resource SIDs to include in the Build.
        :param dependencies: A list of objects that describe the Dependencies included in the Build. Each object contains the `name` and `version` of the dependency.
        :param runtime: The Runtime version that will be used to run the Build resource when it is deployed.
        
        :returns: The created BuildInstance
        """
        
        data = values.of({ 
            'AssetVersions': serialize.map(asset_versions, lambda e: e),
            'FunctionVersions': serialize.map(function_versions, lambda e: e),
            'Dependencies': dependencies,
            'Runtime': runtime,
        })
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return BuildInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[BuildInstance]:
        """
        Streams BuildInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[BuildInstance]:
        """
        Asynchronously streams BuildInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BuildInstance]:
        """
        Lists BuildInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[BuildInstance]:
        """
        Asynchronously lists BuildInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BuildPage:
        """
        Retrieve a single page of BuildInstance records from the API.
        Request is executed immediately
        
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BuildInstance
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return BuildPage(self._version, response, self._solution)

    async def page_async(self, 
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> BuildPage:
        """
        Asynchronously retrieve a single page of BuildInstance records from the API.
        Request is executed immediately
        
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of BuildInstance
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return BuildPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> BuildPage:
        """
        Retrieve a specific page of BuildInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BuildInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return BuildPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> BuildPage:
        """
        Asynchronously retrieve a specific page of BuildInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of BuildInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return BuildPage(self._version, response, self._solution)





    def get(self, sid: str) -> BuildContext:
        """
        Constructs a BuildContext
        
        :param sid: The SID of the Build resource to fetch.
        """
        return BuildContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid: str) -> BuildContext:
        """
        Constructs a BuildContext
        
        :param sid: The SID of the Build resource to fetch.
        """
        return BuildContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Serverless.V1.BuildList>'

