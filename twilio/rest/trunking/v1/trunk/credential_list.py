"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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


class CredentialListList(ListResource):

    def __init__(self, version: Version, trunk_sid: str):
        """
        Initialize the CredentialListList

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to read the credential lists.
        
        :returns: twilio.rest.trunking.v1.trunk.credential_list.CredentialListList
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'trunk_sid': trunk_sid,  }
        self._uri = '/Trunks/{trunk_sid}/CredentialLists'.format(**self._solution)
        
        
    
    
    
    def create(self, credential_list_sid):
        """
        Create the CredentialListInstance

        :param str credential_list_sid: The SID of the [Credential List](https://www.twilio.com/docs/voice/sip/api/sip-credentiallist-resource) that you want to associate with the trunk. Once associated, we will authenticate access to the trunk against this list.
        
        :returns: The created CredentialListInstance
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance
        """
        data = values.of({ 
            'CredentialListSid': credential_list_sid,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return CredentialListInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams CredentialListInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CredentialListInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CredentialListInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CredentialListInstance
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CredentialListPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CredentialListInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CredentialListInstance
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CredentialListPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a CredentialListContext
        
        :param sid: The unique string that we created to identify the CredentialList resource to fetch.
        
        :returns: twilio.rest.trunking.v1.trunk.credential_list.CredentialListContext
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListContext
        """
        return CredentialListContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a CredentialListContext
        
        :param sid: The unique string that we created to identify the CredentialList resource to fetch.
        
        :returns: twilio.rest.trunking.v1.trunk.credential_list.CredentialListContext
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListContext
        """
        return CredentialListContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.CredentialListList>'








class CredentialListPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CredentialListPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.trunking.v1.trunk.credential_list.CredentialListPage
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CredentialListInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance
        """
        return CredentialListInstance(self._version, payload, trunk_sid=self._solution['trunk_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1.CredentialListPage>'




class CredentialListContext(InstanceContext):

    def __init__(self, version: Version, trunk_sid: str, sid: str):
        """
        Initialize the CredentialListContext

        :param Version version: Version that contains the resource
        :param trunk_sid: The SID of the Trunk from which to fetch the credential list.:param sid: The unique string that we created to identify the CredentialList resource to fetch.

        :returns: twilio.rest.trunking.v1.trunk.credential_list.CredentialListContext
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'trunk_sid': trunk_sid,
            'sid': sid,
        }
        self._uri = '/Trunks/{trunk_sid}/CredentialLists/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the CredentialListInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the CredentialListInstance
        

        :returns: The fetched CredentialListInstance
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CredentialListInstance(
            self._version,
            payload,
            trunk_sid=self._solution['trunk_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.CredentialListContext {}>'.format(context)

class CredentialListInstance(InstanceResource):

    def __init__(self, version, payload, trunk_sid: str, sid: str=None):
        """
        Initialize the CredentialListInstance
        :returns: twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'sid': payload.get('sid'),
            'trunk_sid': payload.get('trunk_sid'),
            'friendly_name': payload.get('friendly_name'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'trunk_sid': trunk_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: CredentialListContext for this CredentialListInstance
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListContext
        """
        if self._context is None:
            self._context = CredentialListContext(self._version, trunk_sid=self._solution['trunk_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialList resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the CredentialList resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def trunk_sid(self):
        """
        :returns: The SID of the Trunk the credential list in associated with.
        :rtype: str
        """
        return self._properties['trunk_sid']
    
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
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the CredentialListInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the CredentialListInstance
        

        :returns: The fetched CredentialListInstance
        :rtype: twilio.rest.trunking.v1.trunk.credential_list.CredentialListInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Trunking.V1.CredentialListInstance {}>'.format(context)


