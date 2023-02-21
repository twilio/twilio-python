"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.supersim.v1.network_access_profile.networks import NetworkAccessProfileNetworkList


class NetworkAccessProfileList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the NetworkAccessProfileList
        :param Version version: Version that contains the resource
        
        :returns: twilio.supersim.v1.network_access_profile..NetworkAccessProfileList
        :rtype: twilio.supersim.v1.network_access_profile..NetworkAccessProfileList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/NetworkAccessProfiles'.format(**self._solution)
        
        
    
    
    
    def create(self, unique_name=values.unset, networks=values.unset):
        """
        Create the NetworkAccessProfileInstance
         :param str unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
         :param [str] networks: List of Network SIDs that this Network Access Profile will allow connections to.
        
        :returns: The created NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
            'Networks': serialize.map(networks, lambda e: e),
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return NetworkAccessProfileInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams NetworkAccessProfileInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists NetworkAccessProfileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfilePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return NetworkAccessProfilePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of NetworkAccessProfileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfilePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return NetworkAccessProfilePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a NetworkAccessProfileContext
        
        :param sid: The SID of the Network Access Profile to update.
        
        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        """
        return NetworkAccessProfileContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a NetworkAccessProfileContext
        
        :param sid: The SID of the Network Access Profile to update.
        
        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileContext
        """
        return NetworkAccessProfileContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.NetworkAccessProfileList>'








class NetworkAccessProfilePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the NetworkAccessProfilePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfilePage
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfilePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NetworkAccessProfileInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        :rtype: twilio.rest.supersim.v1.network_access_profile.NetworkAccessProfileInstance
        """
        return NetworkAccessProfileInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.NetworkAccessProfilePage>'





class NetworkAccessProfileContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/NetworkAccessProfiles/${sid}'
        
        self._networks = None
    
    def fetch(self):
        
        """
        Fetch the NetworkAccessProfileInstance

        :returns: The fetched NetworkAccessProfileInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return NetworkAccessProfileInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, unique_name):
        data = values.of({
            'unique_name': unique_name,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return NetworkAccessProfileInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.NetworkAccessProfileContext>'



class NetworkAccessProfileInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'unique_name' : payload.get('unique_name'),
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = NetworkAccessProfileContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def networks(self):
        return self._proxy.networks
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.NetworkAccessProfileInstance {}>'.format(context)



