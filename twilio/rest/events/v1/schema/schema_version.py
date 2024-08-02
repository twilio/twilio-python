r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
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


class SchemaVersionInstance(InstanceResource):

    """
    :ivar id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
    :ivar schema_version: The version of this schema.
    :ivar date_created: The date the schema version was created, given in ISO 8601 format.
    :ivar url: The URL of this resource.
    :ivar raw: 
    """

    def __init__(self, version: Version, payload: Dict[str, Any], id: str, schema_version: Optional[int] = None):
        super().__init__(version)

        
        self.id: Optional[str] = payload.get("id")
        self.schema_version: Optional[int] = deserialize.integer(payload.get("schema_version"))
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(payload.get("date_created"))
        self.url: Optional[str] = payload.get("url")
        self.raw: Optional[str] = payload.get("raw")

        
        self._solution = { 
            "id": id,
            "schema_version": schema_version or self.schema_version,
        }
        self._context: Optional[SchemaVersionContext] = None

    @property
    def _proxy(self) -> "SchemaVersionContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SchemaVersionContext for this SchemaVersionInstance
        """
        if self._context is None:
            self._context = SchemaVersionContext(self._version, id=self._solution['id'], schema_version=self._solution['schema_version'],)
        return self._context
    
    
    def fetch(self) -> "SchemaVersionInstance":
        """
        Fetch the SchemaVersionInstance
        

        :returns: The fetched SchemaVersionInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "SchemaVersionInstance":
        """
        Asynchronous coroutine to fetch the SchemaVersionInstance
        

        :returns: The fetched SchemaVersionInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SchemaVersionInstance {}>'.format(context)

class SchemaVersionContext(InstanceContext):

    def __init__(self, version: Version, id: str, schema_version: int):
        """
        Initialize the SchemaVersionContext

        :param version: Version that contains the resource
        :param id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
        :param schema_version: The version of the schema
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'id': id,
            'schema_version': schema_version,
        }
        self._uri = '/Schemas/{id}/Versions/{schema_version}'.format(**self._solution)
        
    
    
    def fetch(self) -> SchemaVersionInstance:
        """
        Fetch the SchemaVersionInstance
        

        :returns: The fetched SchemaVersionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SchemaVersionInstance(
            self._version,
            payload,
            id=self._solution['id'],
            schema_version=self._solution['schema_version'],
            
        )

    async def fetch_async(self) -> SchemaVersionInstance:
        """
        Asynchronous coroutine to fetch the SchemaVersionInstance
        

        :returns: The fetched SchemaVersionInstance
        """
        
        payload = await self._version.fetch_async(method='GET', uri=self._uri, )

        return SchemaVersionInstance(
            self._version,
            payload,
            id=self._solution['id'],
            schema_version=self._solution['schema_version'],
            
        )
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SchemaVersionContext {}>'.format(context)





class SchemaVersionPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> SchemaVersionInstance:
        """
        Build an instance of SchemaVersionInstance

        :param payload: Payload response from the API
        """
        return SchemaVersionInstance(self._version, payload, id=self._solution["id"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Events.V1.SchemaVersionPage>"





class SchemaVersionList(ListResource):
    
    def __init__(self, version: Version, id: str):
        """
        Initialize the SchemaVersionList

        :param version: Version that contains the resource
        :param id: The unique identifier of the schema. Each schema can have multiple versions, that share the same id.
        
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 'id': id,  }
        self._uri = '/Schemas/{id}/Versions'.format(**self._solution)
        
        
    
    
    def stream(self, 
        
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[SchemaVersionInstance]:
        """
        Streams SchemaVersionInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[SchemaVersionInstance]:
        """
        Asynchronously streams SchemaVersionInstance records from the API as a generator stream.
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
    ) -> List[SchemaVersionInstance]:
        """
        Lists SchemaVersionInstance records from the API as a list.
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
    ) -> List[SchemaVersionInstance]:
        """
        Asynchronously lists SchemaVersionInstance records from the API as a list.
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
    ) -> SchemaVersionPage:
        """
        Retrieve a single page of SchemaVersionInstance records from the API.
        Request is executed immediately
        
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SchemaVersionInstance
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SchemaVersionPage(self._version, response, self._solution)

    async def page_async(self, 
        
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> SchemaVersionPage:
        """
        Asynchronously retrieve a single page of SchemaVersionInstance records from the API.
        Request is executed immediately
        
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of SchemaVersionInstance
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return SchemaVersionPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> SchemaVersionPage:
        """
        Retrieve a specific page of SchemaVersionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SchemaVersionInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SchemaVersionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> SchemaVersionPage:
        """
        Asynchronously retrieve a specific page of SchemaVersionInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of SchemaVersionInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return SchemaVersionPage(self._version, response, self._solution)



    def get(self, schema_version: int) -> SchemaVersionContext:
        """
        Constructs a SchemaVersionContext
        
        :param schema_version: The version of the schema
        """
        return SchemaVersionContext(self._version, id=self._solution['id'], schema_version=schema_version)

    def __call__(self, schema_version: int) -> SchemaVersionContext:
        """
        Constructs a SchemaVersionContext
        
        :param schema_version: The version of the schema
        """
        return SchemaVersionContext(self._version, id=self._solution['id'], schema_version=schema_version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.Events.V1.SchemaVersionList>'

