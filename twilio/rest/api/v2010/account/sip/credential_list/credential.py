"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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


class CredentialList(ListResource):

    def __init__(self, version: Version, account_sid: str, credential_list_sid: str):
        """
        Initialize the CredentialList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the Account that is responsible for this resource.
        :param credential_list_sid: The unique id that identifies the credential list that contains the desired credentials.
        
        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialList
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'credential_list_sid': credential_list_sid,  }
        self._uri = '/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials.json'.format(**self._solution)
        
        
    
    
    
    
    def create(self, username, password):
        """
        Create the CredentialInstance

        :param str username: The username that will be passed when authenticating SIP requests. The username should be sent in response to Twilio's challenge of the initial INVITE. It can be up to 32 characters long.
        :param str password: The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`)
        
        :returns: The created CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        data = values.of({ 
            'Username': username,
            'Password': password,
        })
        )
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return CredentialInstance(self._version, payload, account_sid=self._solution['account_sid'], credential_list_sid=self._solution['credential_list_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams CredentialInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CredentialInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CredentialInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CredentialPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CredentialInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CredentialPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a CredentialContext
        
        :param sid: The unique id that identifies the resource to update.
        
        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        """
        return CredentialContext(self._version, account_sid=self._solution['account_sid'], credential_list_sid=self._solution['credential_list_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a CredentialContext
        
        :param sid: The unique id that identifies the resource to update.
        
        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        """
        return CredentialContext(self._version, account_sid=self._solution['account_sid'], credential_list_sid=self._solution['credential_list_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialList>'










class CredentialPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CredentialPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialPage
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CredentialInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        return CredentialInstance(self._version, payload, account_sid=self._solution['account_sid'], credential_list_sid=self._solution['credential_list_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialPage>'




class CredentialContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, credential_list_sid: str, sid: str):
        """
        Initialize the CredentialContext

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the Account that is responsible for this resource.:param credential_list_sid: The unique id that identifies the credential list that includes this credential.:param sid: The unique id that identifies the resource to update.

        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'credential_list_sid': credential_list_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/CredentialLists/{credential_list_sid}/Credentials/{sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the CredentialInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the CredentialInstance
        

        :returns: The fetched CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CredentialInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            credential_list_sid=self._solution['credential_list_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, password=values.unset):
        """
        Update the CredentialInstance
        
        :params str password: The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`)

        :returns: The updated CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        data = values.of({ 
            'Password': password,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return CredentialInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            credential_list_sid=self._solution['credential_list_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CredentialContext {}>'.format(context)

class CredentialInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, credential_list_sid: str, sid: str=None):
        """
        Initialize the CredentialInstance
        :returns: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'credential_list_sid': payload.get('credential_list_sid'),
            'username': payload.get('username'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'uri': payload.get('uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'credential_list_sid': credential_list_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CredentialContext for this CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialContext
        """
        if self._context is None:
            self._context = CredentialContext(self._version, account_sid=self._solution['account_sid'], credential_list_sid=self._solution['credential_list_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account that is responsible for this resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def credential_list_sid(self):
        """
        :returns: The unique id that identifies the credential list that includes this credential.
        :rtype: str
        """
        return self._properties['credential_list_sid']
    
    @property
    def username(self):
        """
        :returns: The username for this credential.
        :rtype: str
        """
        return self._properties['username']
    
    @property
    def date_created(self):
        """
        :returns: The date that this resource was created, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def uri(self):
        """
        :returns: The URI for this resource, relative to `https://api.twilio.com`
        :rtype: str
        """
        return self._properties['uri']
    
    def delete(self):
        """
        Deletes the CredentialInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the CredentialInstance
        

        :returns: The fetched CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        return self._proxy.fetch()
    
    def update(self, password=values.unset):
        """
        Update the CredentialInstance
        
        :params str password: The password that the username will use when authenticating SIP requests. The password must be a minimum of 12 characters, contain at least 1 digit, and have mixed case. (eg `IWasAtSignal2018`)

        :returns: The updated CredentialInstance
        :rtype: twilio.rest.api.v2010.account.sip.credential_list.credential.CredentialInstance
        """
        return self._proxy.update(password=password, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CredentialInstance {}>'.format(context)


