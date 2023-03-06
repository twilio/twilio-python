"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Accounts
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


class PublicKeyList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PublicKeyList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.accounts.v1.credential.public_key.PublicKeyList
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Credentials/PublicKeys'.format(**self._solution)
        
        
    
    
    
    
    def create(self, public_key, friendly_name=values.unset, account_sid=values.unset):
        """
        Create the PublicKeyInstance

        :param str public_key: A URL encoded representation of the public key. For example, `-----BEGIN PUBLIC KEY-----MIIBIjANB.pa9xQIDAQAB-----END PUBLIC KEY-----`
        :param str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :param str account_sid: The SID of the Subaccount that this Credential should be associated with. Must be a valid Subaccount of the account issuing the request
        
        :returns: The created PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        """
        data = values.of({ 
            'PublicKey': public_key,
            'FriendlyName': friendly_name,
            'AccountSid': account_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return PublicKeyInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams PublicKeyInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists PublicKeyInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of PublicKeyInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return PublicKeyPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of PublicKeyInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return PublicKeyPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a PublicKeyContext
        
        :param sid: The Twilio-provided string that uniquely identifies the PublicKey resource to update.
        
        :returns: twilio.rest.accounts.v1.credential.public_key.PublicKeyContext
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyContext
        """
        return PublicKeyContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a PublicKeyContext
        
        :param sid: The Twilio-provided string that uniquely identifies the PublicKey resource to update.
        
        :returns: twilio.rest.accounts.v1.credential.public_key.PublicKeyContext
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyContext
        """
        return PublicKeyContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.PublicKeyList>'










class PublicKeyPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the PublicKeyPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.accounts.v1.credential.public_key.PublicKeyPage
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PublicKeyInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        """
        return PublicKeyInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Accounts.V1.PublicKeyPage>'




class PublicKeyContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the PublicKeyContext

        :param Version version: Version that contains the resource
        :param sid: The Twilio-provided string that uniquely identifies the PublicKey resource to update.

        :returns: twilio.rest.accounts.v1.credential.public_key.PublicKeyContext
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Credentials/PublicKeys/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the PublicKeyInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the PublicKeyInstance
        

        :returns: The fetched PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PublicKeyInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset):
        """
        Update the PublicKeyInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The updated PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return PublicKeyInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Accounts.V1.PublicKeyContext {}>'.format(context)

class PublicKeyInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the PublicKeyInstance
        :returns: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PublicKeyContext for this PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyContext
        """
        if self._context is None:
            self._context = PublicKeyContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the PublicKey resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Credential that the PublicKey resource belongs to.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The URI for this resource, relative to `https://accounts.twilio.com`
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the PublicKeyInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the PublicKeyInstance
        

        :returns: The fetched PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset):
        """
        Update the PublicKeyInstance
        
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.

        :returns: The updated PublicKeyInstance
        :rtype: twilio.rest.accounts.v1.credential.public_key.PublicKeyInstance
        """
        return self._proxy.update(friendly_name=friendly_name, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Accounts.V1.PublicKeyInstance {}>'.format(context)


