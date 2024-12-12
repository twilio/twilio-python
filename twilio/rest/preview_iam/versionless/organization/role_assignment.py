r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Organization Public API
    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

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


class RoleAssignmentInstance(InstanceResource):

    class PublicApiCreateRoleAssignmentRequest(object):
        """
            :ivar role_sid: Twilio Role Sid representing assigned role
            :ivar scope: Twilio Sid representing scope of this assignment
            :ivar identity: Twilio Sid representing identity of this assignment
        """

        def __init__(self, payload: Dict[str, Any]):

            
            self.role_sid: Optional[str] = payload.get("role_sid")
            self.scope: Optional[str] = payload.get("scope")
            self.identity: Optional[str] = payload.get("identity")

        def to_dict(self):
            return {
                
                    "role_sid": self.role_sid,
                    "scope": self.scope,
                    "identity": self.identity,
            }



    """
    :ivar sid: Twilio Role Assignment Sid representing this role assignment
    :ivar role_sid: Twilio Role Sid representing assigned role
    :ivar scope: Twilio Sid representing identity of this assignment
    :ivar identity: Twilio Sid representing scope of this assignment
    :ivar code: Twilio-specific error code
    :ivar message: Error message
    :ivar more_info: Link to Error Code References
    :ivar status: HTTP response status code
    """

    def __init__(self, version: Version, payload: Dict[str, Any], organization_sid: str, sid: Optional[str] = None):
        super().__init__(version)

        
        self.sid: Optional[str] = payload.get("sid")
        self.role_sid: Optional[str] = payload.get("role_sid")
        self.scope: Optional[str] = payload.get("scope")
        self.identity: Optional[str] = payload.get("identity")
        self.code: Optional[int] = payload.get("code")
        self.message: Optional[str] = payload.get("message")
        self.more_info: Optional[str] = payload.get("moreInfo")
        self.status: Optional[int] = payload.get("status")

        
        self._solution = { 
            "organization_sid": organization_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[RoleAssignmentContext] = None

    @property
    def _proxy(self) -> "RoleAssignmentContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoleAssignmentContext for this RoleAssignmentInstance
        """
        if self._context is None:
            self._context = RoleAssignmentContext(self._version, organization_sid=self._solution['organization_sid'], sid=self._solution['sid'],)
        return self._context
    
    
    def delete(self) -> bool:
        """
        Deletes the RoleAssignmentInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()
    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RoleAssignmentInstance
        

        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.PreviewIam.Versionless.RoleAssignmentInstance {}>'.format(context)

class RoleAssignmentContext(InstanceContext):

    class PublicApiCreateRoleAssignmentRequest(object):
        """
            :ivar role_sid: Twilio Role Sid representing assigned role
            :ivar scope: Twilio Sid representing scope of this assignment
            :ivar identity: Twilio Sid representing identity of this assignment
        """

        def __init__(self, payload: Dict[str, Any]):

            
            self.role_sid: Optional[str] = payload.get("role_sid")
            self.scope: Optional[str] = payload.get("scope")
            self.identity: Optional[str] = payload.get("identity")

        def to_dict(self):
            return {
                
                    "role_sid": self.role_sid,
                    "scope": self.scope,
                    "identity": self.identity,
            }


    def __init__(self, version: Version, organization_sid: str, sid: str):
        """
        Initialize the RoleAssignmentContext

        :param version: Version that contains the resource
        :param organization_sid: 
        :param sid: 
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 
            'organization_sid': organization_sid,
            'sid': sid,
        }
        self._uri = '/{organization_sid}/RoleAssignments/{sid}'.format(**self._solution)
        
    
    
    def delete(self) -> bool:
        """
        Deletes the RoleAssignmentInstance

        
        :returns: True if delete succeeds, False otherwise
        """

        
        headers = values.of({})
        
        
        
        headers["Accept"] = "application/scim+json"
        
        return self._version.delete(method='DELETE', uri=self._uri, headers=headers)

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the RoleAssignmentInstance

        
        :returns: True if delete succeeds, False otherwise
        """
        
        headers = values.of({})
        
        
        
        headers["Accept"] = "application/scim+json"
        
        return await self._version.delete_async(method='DELETE', uri=self._uri, headers=headers)
    
    
    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.PreviewIam.Versionless.RoleAssignmentContext {}>'.format(context)







class RoleAssignmentPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> RoleAssignmentInstance:
        """
        Build an instance of RoleAssignmentInstance

        :param payload: Payload response from the API
        """
        return RoleAssignmentInstance(self._version, payload, organization_sid=self._solution["organization_sid"])

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.PreviewIam.Versionless.RoleAssignmentPage>"





class RoleAssignmentList(ListResource):
    
    class PublicApiCreateRoleAssignmentRequest(object):
        """
            :ivar role_sid: Twilio Role Sid representing assigned role
            :ivar scope: Twilio Sid representing scope of this assignment
            :ivar identity: Twilio Sid representing identity of this assignment
        """

        def __init__(self, payload: Dict[str, Any]):

            
            self.role_sid: Optional[str] = payload.get("role_sid")
            self.scope: Optional[str] = payload.get("scope")
            self.identity: Optional[str] = payload.get("identity")

        def to_dict(self):
            return {
                
                    "role_sid": self.role_sid,
                    "scope": self.scope,
                    "identity": self.identity,
            }


    def __init__(self, version: Version, organization_sid: str):
        """
        Initialize the RoleAssignmentList

        :param version: Version that contains the resource
        :param organization_sid: 
        
        """
        super().__init__(version)

        
        # Path Solution
        self._solution = { 'organization_sid': organization_sid,  }
        self._uri = '/{organization_sid}/RoleAssignments'.format(**self._solution)
        
        
    
    
    def create(self, public_api_create_role_assignment_request: PublicApiCreateRoleAssignmentRequest) -> RoleAssignmentInstance:
        """
        Create the RoleAssignmentInstance

        :param public_api_create_role_assignment_request: 
        
        :returns: The created RoleAssignmentInstance
        """
        data = public_api_create_role_assignment_request.to_dict()
        
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        headers["Content-Type"] = "application/json"
        
        
        headers["Accept"] = "application/json"
        
        
        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers)

        return RoleAssignmentInstance(self._version, payload, organization_sid=self._solution['organization_sid'])

    async def create_async(self, public_api_create_role_assignment_request: PublicApiCreateRoleAssignmentRequest) -> RoleAssignmentInstance:
        """
        Asynchronously create the RoleAssignmentInstance

        :param public_api_create_role_assignment_request: 
        
        :returns: The created RoleAssignmentInstance
        """
        data = public_api_create_role_assignment_request.to_dict()
        
        headers = values.of({
                'Content-Type': 'application/x-www-form-urlencoded'
            })
        
        headers["Content-Type"] = "application/json"
        
        
        headers["Accept"] = "application/json"
        
        
        payload = await self._version.create_async(method='POST', uri=self._uri, data=data, headers=headers)

        return RoleAssignmentInstance(self._version, payload, organization_sid=self._solution['organization_sid'])
    
    
    def stream(self, 
        
        identity: Union[str, object] = values.unset,
        scope: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[RoleAssignmentInstance]:
        """
        Streams RoleAssignmentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str identity: 
        :param str scope: 
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
            identity=identity,
            scope=scope,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, 
        
        identity: Union[str, object] = values.unset,
        scope: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[RoleAssignmentInstance]:
        """
        Asynchronously streams RoleAssignmentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str identity: 
        :param str scope: 
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
            identity=identity,
            scope=scope,
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, 
        
        identity: Union[str, object] = values.unset,
        scope: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RoleAssignmentInstance]:
        """
        Lists RoleAssignmentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str identity: 
        :param str scope: 
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(self.stream(
            identity=identity,
            scope=scope,
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, 
        
        identity: Union[str, object] = values.unset,
        scope: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[RoleAssignmentInstance]:
        """
        Asynchronously lists RoleAssignmentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str identity: 
        :param str scope: 
        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [record async for record in await self.stream_async(
            identity=identity,
            scope=scope,
            limit=limit,
            page_size=page_size,
        )]

    def page(self, 
        
        identity: Union[str, object] = values.unset,
        scope: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RoleAssignmentPage:
        """
        Retrieve a single page of RoleAssignmentInstance records from the API.
        Request is executed immediately
        
        :param identity: 
        :param scope: 
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RoleAssignmentInstance
        """
        data = values.of({ 
            'Identity': identity,
            'Scope': scope,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        headers = values.of({
        'Content-Type': 'application/x-www-form-urlencoded'
        })
        
        
        headers["Accept"] = "application/json"
        

        response = self._version.page(method='GET', uri=self._uri, params=data, headers=headers)
        return RoleAssignmentPage(self._version, response, self._solution)

    async def page_async(self, 
        
        identity: Union[str, object] = values.unset,
        scope: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> RoleAssignmentPage:
        """
        Asynchronously retrieve a single page of RoleAssignmentInstance records from the API.
        Request is executed immediately
        
        :param identity: 
        :param scope: 
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of RoleAssignmentInstance
        """
        data = values.of({ 
            'Identity': identity,
            'Scope': scope,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        headers = values.of({
        'Content-Type': 'application/x-www-form-urlencoded'
        })
        
        
        headers["Accept"] = "application/json"
        

        response = await self._version.page_async(method='GET', uri=self._uri, params=data, headers=headers)
        return RoleAssignmentPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> RoleAssignmentPage:
        """
        Retrieve a specific page of RoleAssignmentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RoleAssignmentInstance
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RoleAssignmentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> RoleAssignmentPage:
        """
        Asynchronously retrieve a specific page of RoleAssignmentInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of RoleAssignmentInstance
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return RoleAssignmentPage(self._version, response, self._solution)



    def get(self, sid: str) -> RoleAssignmentContext:
        """
        Constructs a RoleAssignmentContext
        
        :param sid: 
        """
        return RoleAssignmentContext(self._version, organization_sid=self._solution['organization_sid'], sid=sid)

    def __call__(self, sid: str) -> RoleAssignmentContext:
        """
        Constructs a RoleAssignmentContext
        
        :param sid: 
        """
        return RoleAssignmentContext(self._version, organization_sid=self._solution['organization_sid'], sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return '<Twilio.PreviewIam.Versionless.RoleAssignmentList>'

