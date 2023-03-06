"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
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


class AccountSecretList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AccountSecretList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretList
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Secrets'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the AccountSecretInstance

        :returns: The fetched AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return AccountSecretInstance(self._version, payload)
    
    
    def create(self, key, value):
        """
        Create the AccountSecretInstance

        :param str key: The secret key; up to 100 characters.
        :param str value: The secret value; up to 4096 characters.
        
        :returns: The created AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        data = values.of({ 
            'Key': key,
            'Value': value,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return AccountSecretInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AccountSecretInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.microvisor.v1.account_secret.AccountSecretInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AccountSecretInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.microvisor.v1.account_secret.AccountSecretInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AccountSecretInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AccountSecretPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AccountSecretInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AccountSecretPage(self._version, response, self._solution)


    def get(self, key):
        """
        Constructs a AccountSecretContext
        
        :param key: The secret key; up to 100 characters.
        
        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        """
        return AccountSecretContext(self._version, key=key)

    def __call__(self, key):
        """
        Constructs a AccountSecretContext
        
        :param key: The secret key; up to 100 characters.
        
        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        """
        return AccountSecretContext(self._version, key=key)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.AccountSecretList>'








class AccountSecretPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AccountSecretPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AccountSecretInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        return AccountSecretInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1.AccountSecretPage>'




class AccountSecretInstance(InstanceResource):

    def __init__(self, version, payload, key: str=None):
        """
        Initialize the AccountSecretInstance
        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        super().__init__(version)

        self._properties = { 
            'key': payload.get('key'),
            'date_rotated': deserialize.iso8601_datetime(payload.get('date_rotated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'key': key or self._properties['key'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AccountSecretContext for this AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        """
        if self._context is None:
            self._context = AccountSecretContext(self._version, key=self._solution['key'],)
        return self._context
    
    @property
    def key(self):
        """
        :returns: The secret key; up to 100 characters.
        :rtype: str
        """
        return self._properties['key']
    
    @property
    def date_rotated(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_rotated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Secret.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the AccountSecretInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the AccountSecretInstance
        

        :returns: The fetched AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.AccountSecretInstance {}>'.format(context)

class AccountSecretContext(InstanceContext):

    def __init__(self, version: Version, key: str):
        """
        Initialize the AccountSecretContext

        :param Version version: Version that contains the resource
        :param key: The secret key; up to 100 characters.

        :returns: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'key': key,
        }
        self._uri = '/Secrets/{key}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the AccountSecretInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the AccountSecretInstance
        

        :returns: The fetched AccountSecretInstance
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AccountSecretInstance(
            self._version,
            payload,
            key=self._solution['key'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Microvisor.V1.AccountSecretContext {}>'.format(context)


