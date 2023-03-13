"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class PoliciesList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PoliciesList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.trusthub.v1.policies.PoliciesList
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Policies'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams PoliciesInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trusthub.v1.policies.PoliciesInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists PoliciesInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trusthub.v1.policies.PoliciesInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of PoliciesInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PoliciesInstance
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return PoliciesPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PoliciesInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PoliciesInstance
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return PoliciesPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a PoliciesContext
        
        :param sid: The unique string that identifies the Policy resource.
        
        :returns: twilio.rest.trusthub.v1.policies.PoliciesContext
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesContext
        """
        return PoliciesContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a PoliciesContext
        
        :param sid: The unique string that identifies the Policy resource.
        
        :returns: twilio.rest.trusthub.v1.policies.PoliciesContext
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesContext
        """
        return PoliciesContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.PoliciesList>'




class PoliciesPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the PoliciesPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trusthub.v1.policies.PoliciesPage
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PoliciesInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trusthub.v1.policies.PoliciesInstance
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesInstance
        """
        return PoliciesInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trusthub.V1.PoliciesPage>'




class PoliciesInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the PoliciesInstance
        :returns: twilio.rest.trusthub.v1.policies.PoliciesInstance
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'requirements': payload.get('requirements'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PoliciesContext for this PoliciesInstance
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesContext
        """
        if self._context is None:
            self._context = PoliciesContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Policy resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def friendly_name(self):
        """
        :returns: A human-readable description that is assigned to describe the Policy resource. Examples can include Primary Customer profile policy
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def requirements(self):
        """
        :returns: The SID of an object that holds the policy information
        :rtype: dict
        """
        return self._properties['requirements']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Policy resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the PoliciesInstance
        

        :returns: The fetched PoliciesInstance
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.PoliciesInstance {}>'.format(context)

class PoliciesContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the PoliciesContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that identifies the Policy resource.

        :returns: twilio.rest.trusthub.v1.policies.PoliciesContext
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Policies/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the PoliciesInstance
        

        :returns: The fetched PoliciesInstance
        :rtype: twilio.rest.trusthub.v1.policies.PoliciesInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PoliciesInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trusthub.V1.PoliciesContext {}>'.format(context)


