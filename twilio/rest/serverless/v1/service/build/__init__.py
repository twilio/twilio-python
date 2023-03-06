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
from twilio.rest.serverless.v1.service.build.build_status import BuildStatusList


class BuildList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the BuildList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to read the Build resources from.
        
        :returns: twilio.rest.serverless.v1.service.build.BuildList
        :rtype: twilio.rest.serverless.v1.service.build.BuildList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/{service_sid}/Builds'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the BuildInstance

        :returns: The fetched BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return BuildInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def create(self, asset_versions=values.unset, function_versions=values.unset, dependencies=values.unset, runtime=values.unset):
        """
        Create the BuildInstance

        :param list[str] asset_versions: The list of Asset Version resource SIDs to include in the Build.
        :param list[str] function_versions: The list of the Function Version resource SIDs to include in the Build.
        :param str dependencies: A list of objects that describe the Dependencies included in the Build. Each object contains the `name` and `version` of the dependency.
        :param str runtime: The Runtime version that will be used to run the Build resource when it is deployed.
        
        :returns: The created BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        data = values.of({ 
            'AssetVersions': serialize.map(asset_versions, lambda e: e),
            'FunctionVersions': serialize.map(function_versions, lambda e: e),
            'Dependencies': dependencies,
            'Runtime': runtime,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return BuildInstance(self._version, payload, service_sid=self._solution['service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams BuildInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.build.BuildInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists BuildInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.build.BuildInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of BuildInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return BuildPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BuildInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return BuildPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a BuildContext
        
        :param sid: The SID of the Build resource to fetch.
        
        :returns: twilio.rest.serverless.v1.service.build.BuildContext
        :rtype: twilio.rest.serverless.v1.service.build.BuildContext
        """
        return BuildContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a BuildContext
        
        :param sid: The SID of the Build resource to fetch.
        
        :returns: twilio.rest.serverless.v1.service.build.BuildContext
        :rtype: twilio.rest.serverless.v1.service.build.BuildContext
        """
        return BuildContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.BuildList>'








class BuildPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the BuildPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.serverless.v1.service.build.BuildPage
        :rtype: twilio.rest.serverless.v1.service.build.BuildPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BuildInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.build.BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        return BuildInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.BuildPage>'




class BuildInstance(InstanceResource):

    class Runtime(object):
        NODE8 = "node8"
        NODE10 = "node10"
        NODE12 = "node12"
        NODE14 = "node14"
        NODE16 = "node16"

    class Status(object):
        BUILDING = "building"
        COMPLETED = "completed"
        FAILED = "failed"

    def __init__(self, version, payload, service_sid: str, sid: str=None):
        """
        Initialize the BuildInstance
        :returns: twilio.rest.serverless.v1.service.build.BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'status': payload.get('status'),
            'asset_versions': payload.get('asset_versions'),
            'function_versions': payload.get('function_versions'),
            'dependencies': payload.get('dependencies'),
            'runtime': payload.get('runtime'),
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

        :returns: BuildContext for this BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildContext
        """
        if self._context is None:
            self._context = BuildContext(self._version, service_sid=self._solution['service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Build resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Build resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Build resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: Status
        """
        return self._properties['status']
    
    @property
    def asset_versions(self):
        """
        :returns: The list of Asset Version resource SIDs that are included in the Build.
        :rtype: list[object]
        """
        return self._properties['asset_versions']
    
    @property
    def function_versions(self):
        """
        :returns: The list of Function Version resource SIDs that are included in the Build.
        :rtype: list[object]
        """
        return self._properties['function_versions']
    
    @property
    def dependencies(self):
        """
        :returns: A list of objects that describe the Dependencies included in the Build. Each object contains the `name` and `version` of the dependency.
        :rtype: list[object]
        """
        return self._properties['dependencies']
    
    @property
    def runtime(self):
        """
        :returns: 
        :rtype: Runtime
        """
        return self._properties['runtime']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the Build resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the Build resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Build resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: 
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the BuildInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the BuildInstance
        

        :returns: The fetched BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        return self._proxy.fetch()
    
    @property
    def build_status(self):
        """
        Access the build_status

        :returns: twilio.rest.serverless.v1.service.build.BuildStatusList
        :rtype: twilio.rest.serverless.v1.service.build.BuildStatusList
        """
        return self._proxy.build_status
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildInstance {}>'.format(context)

class BuildContext(InstanceContext):

    def __init__(self, version: Version, service_sid: str, sid: str):
        """
        Initialize the BuildContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Build resource from.:param sid: The SID of the Build resource to fetch.

        :returns: twilio.rest.serverless.v1.service.build.BuildContext
        :rtype: twilio.rest.serverless.v1.service.build.BuildContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'service_sid': service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{service_sid}/Builds/{sid}'.format(**self._solution)
        
        self._build_status = None
    
    def delete(self):
        """
        Deletes the BuildInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the BuildInstance
        

        :returns: The fetched BuildInstance
        :rtype: twilio.rest.serverless.v1.service.build.BuildInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BuildInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    @property
    def build_status(self):
        """
        Access the build_status

        :returns: twilio.rest.serverless.v1.service.build.BuildStatusList
        :rtype: twilio.rest.serverless.v1.service.build.BuildStatusList
        """
        if self._build_status is None:
            self._build_status = BuildStatusList(self._version, self._solution['service_sid'], self._solution['sid'],
            )
        return self._build_status
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.BuildContext {}>'.format(context)


