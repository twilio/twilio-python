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


from datetime import date
from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class CredentialListMappingList(ListResource):

    def __init__(self, version: Version, account_sid: str, domain_sid: str):
        """
        Initialize the CredentialListMappingList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to read.
        
        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingList
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'domain_sid': domain_sid,  }
        self._uri = '/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings.json'.format(**self._solution)
        
        
    
    
    
    def create(self, credential_list_sid):
        """
        Create the CredentialListMappingInstance

        :param str credential_list_sid: A 34 character string that uniquely identifies the CredentialList resource to map to the SIP domain.
        
        :returns: The created CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        data = values.of({ 
            'CredentialListSid': credential_list_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return CredentialListMappingInstance(self._version, payload, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams CredentialListMappingInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CredentialListMappingInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CredentialListMappingInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CredentialListMappingPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CredentialListMappingInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CredentialListMappingPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a CredentialListMappingContext
        
        :param sid: A 34 character string that uniquely identifies the resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        """
        return CredentialListMappingContext(self._version, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a CredentialListMappingContext
        
        :param sid: A 34 character string that uniquely identifies the resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        """
        return CredentialListMappingContext(self._version, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialListMappingList>'








class CredentialListMappingPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CredentialListMappingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingPage
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CredentialListMappingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        return CredentialListMappingInstance(self._version, payload, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.CredentialListMappingPage>'




class CredentialListMappingInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, domain_sid: str, sid: str=None):
        """
        Initialize the CredentialListMappingInstance
        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'domain_sid': payload.get('domain_sid'),
            'friendly_name': payload.get('friendly_name'),
            'sid': payload.get('sid'),
            'uri': payload.get('uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'domain_sid': domain_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CredentialListMappingContext for this CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        """
        if self._context is None:
            self._context = CredentialListMappingContext(self._version, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account that is responsible for this resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
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
    def domain_sid(self):
        """
        :returns: The unique string that is created to identify the SipDomain resource.
        :rtype: str
        """
        return self._properties['domain_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: A human readable descriptive text for this resource, up to 64 characters long.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def uri(self):
        """
        :returns: The URI for this resource, relative to `https://api.twilio.com`
        :rtype: str
        """
        return self._properties['uri']
    
    def delete(self):
        """
        Deletes the CredentialListMappingInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the CredentialListMappingInstance
        

        :returns: The fetched CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CredentialListMappingInstance {}>'.format(context)

class CredentialListMappingContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, domain_sid: str, sid: str):
        """
        Initialize the CredentialListMappingContext

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param domain_sid: A 34 character string that uniquely identifies the SIP Domain that includes the resource to fetch.
        :param sid: A 34 character string that uniquely identifies the resource to fetch.

        :returns: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'domain_sid': domain_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/Domains/{domain_sid}/CredentialListMappings/{sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the CredentialListMappingInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the CredentialListMappingInstance
        

        :returns: The fetched CredentialListMappingInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.credential_list_mapping.CredentialListMappingInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CredentialListMappingInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            domain_sid=self._solution['domain_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.CredentialListMappingContext {}>'.format(context)


