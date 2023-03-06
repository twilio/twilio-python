"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.serverless.v1.service.function.function_version import FunctionVersionList


class FunctionList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the FunctionList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Function resources from.
        
        :returns: twilio.rest.serverless.v1.service.function.FunctionList
        :rtype: twilio.rest.serverless.v1.service.function.FunctionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Functions'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the FunctionInstance

        :returns: The fetched FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return FunctionInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def update(self, friendly_name):
        """
        Update the FunctionInstance

        :param str friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.
        
        :returns: The created FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        
        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return FunctionInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def create(self, friendly_name):
        """
        Create the FunctionInstance

        :param str friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.
        
        :returns: The created FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return FunctionInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams FunctionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.function.FunctionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FunctionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.function.FunctionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of FunctionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return FunctionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FunctionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return FunctionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a FunctionContext
        
        :param sid: The SID of the Function resource to update.
        
        :returns: twilio.rest.serverless.v1.service.function.FunctionContext
        :rtype: twilio.rest.serverless.v1.service.function.FunctionContext
        """
        return FunctionContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a FunctionContext
        
        :param sid: The SID of the Function resource to update.
        
        :returns: twilio.rest.serverless.v1.service.function.FunctionContext
        :rtype: twilio.rest.serverless.v1.service.function.FunctionContext
        """
        return FunctionContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.FunctionList>'










class FunctionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the FunctionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.serverless.v1.service.function.FunctionPage
        :rtype: twilio.rest.serverless.v1.service.function.FunctionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FunctionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.function.FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        return FunctionInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.FunctionPage>'




class FunctionInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the FunctionInstance
        :returns: twilio.rest.serverless.v1.service.function.FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FunctionContext for this FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionContext
        """
        if self._context is None:
            self._context = FunctionContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Function resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Function resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Function resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the Function resource. It can be a maximum of 255 characters.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the Function resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the Function resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Function resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of nested resources of the Function resource.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the FunctionInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the FunctionInstance
        

        :returns: The fetched FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name):
        """
        Update the FunctionInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.

        :returns: The updated FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        return self._proxy.update(friendly_name=friendly_name, )
    
    @property
    def function_versions(self):
        """
        Access the function_versions

        :returns: twilio.rest.serverless.v1.service.function.FunctionVersionList
        :rtype: twilio.rest.serverless.v1.service.function.FunctionVersionList
        """
        return self._proxy.function_versions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionInstance {}>'.format(context)

class FunctionContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the FunctionContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to update the Function resource from.:param sid: The SID of the Function resource to update.

        :returns: twilio.rest.serverless.v1.service.function.FunctionContext
        :rtype: twilio.rest.serverless.v1.service.function.FunctionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Functions/{sid}'.format(**self._solution)
        
        self._function_versions = None
    
    def delete(self):
        """
        Deletes the FunctionInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the FunctionInstance
        

        :returns: The fetched FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FunctionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name):
        """
        Update the FunctionInstance
        
        :params str friendly_name: A descriptive string that you create to describe the Function resource. It can be a maximum of 255 characters.

        :returns: The updated FunctionInstance
        :rtype: twilio.rest.serverless.v1.service.function.FunctionInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return FunctionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def function_versions(self):
        """
        Access the function_versions

        :returns: twilio.rest.serverless.v1.service.function.FunctionVersionList
        :rtype: twilio.rest.serverless.v1.service.function.FunctionVersionList
        """
        if self._function_versions is None:
            self._function_versions = FunctionVersionList(self._version, self._solution['service_sid'], self._solution['sid'],
            )
        return self._function_versions
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionContext {}>'.format(context)


