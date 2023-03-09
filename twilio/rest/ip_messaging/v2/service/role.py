"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
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
from twilio.base.page import Page


class RoleList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the RoleList

        :param Version version: Version that contains the resource
        :param service_sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.role.RoleList
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Roles'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, type, permission):
        """
        Create the RoleInstance

        :param str friendly_name: 
        :param RoleInstance.RoleType type: 
        :param list[str] permission: 
        
        :returns: The created RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Type': type,
            'Permission': serialize.map(permission, lambda e: e),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return RoleInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams RoleInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.role.RoleInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists RoleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v2.service.role.RoleInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RoleInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RolePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RolePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RoleInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RolePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RolePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a RoleContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.role.RoleContext
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleContext
        """
        return RoleContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a RoleContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v2.service.role.RoleContext
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleContext
        """
        return RoleContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.RoleList>'










class RolePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RolePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.ip_messaging.v2.service.role.RolePage
        :rtype: twilio.rest.ip_messaging.v2.service.role.RolePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RoleInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        """
        return RoleInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V2.RolePage>'




class RoleInstance(InstanceResource):

    class RoleType(object):
        CHANNEL = "channel"
        DEPLOYMENT = "deployment"

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the RoleInstance
        :returns: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'friendly_name': payload.get('friendly_name'),
            'type': payload.get('type'),
            'permissions': payload.get('permissions'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RoleContext for this RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleContext
        """
        if self._context is None:
            self._context = RoleContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def type(self):
        """
        :returns: 
        :rtype: RoleInstance.RoleType
        """
        return self._properties['type']
    
    @property
    def permissions(self):
        """
        :returns: 
        :rtype: list[str]
        """
        return self._properties['permissions']
    
    @property
    def date_created(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the RoleInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the RoleInstance
        

        :returns: The fetched RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        """
        return self._proxy.fetch()
    
    def update(self, permission):
        """
        Update the RoleInstance
        
        :params list[str] permission: 

        :returns: The updated RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        """
        return self._proxy.update(permission=permission, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.RoleInstance {}>'.format(context)

class RoleContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the RoleContext

        :param Version version: Version that contains the resource
        :param service_sid: 
        :param sid: 

        :returns: twilio.rest.ip_messaging.v2.service.role.RoleContext
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Roles/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the RoleInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the RoleInstance
        

        :returns: The fetched RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, permission):
        """
        Update the RoleInstance
        
        :params list[str] permission: 

        :returns: The updated RoleInstance
        :rtype: twilio.rest.ip_messaging.v2.service.role.RoleInstance
        """
        data = values.of({ 
            'Permission': serialize.map(permission, lambda e: e),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return RoleInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V2.RoleContext {}>'.format(context)


