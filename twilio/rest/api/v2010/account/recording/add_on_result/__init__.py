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
from twilio.rest.api.v2010.account.recording.add_on_result.payload import PayloadList


class AddOnResultList(ListResource):

    def __init__(self, version: Version, account_sid: str, reference_sid: str):
        """
        Initialize the AddOnResultList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resources to read.
        :param reference_sid: The SID of the recording to which the result to read belongs.
        
        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'reference_sid': reference_sid,  }
        self._uri = '/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults.json'.format(**self._solution)
        
        
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams AddOnResultInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AddOnResultInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of AddOnResultInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return AddOnResultPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AddOnResultInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return AddOnResultPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a AddOnResultContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        """
        return AddOnResultContext(self._version, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a AddOnResultContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        """
        return AddOnResultContext(self._version, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AddOnResultList>'






class AddOnResultPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the AddOnResultPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultPage
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AddOnResultInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        """
        return AddOnResultInstance(self._version, payload, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AddOnResultPage>'




class AddOnResultInstance(InstanceResource):

    class Status(object):
        CANCELED = "canceled"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"
        IN_PROGRESS = "in-progress"
        INIT = "init"
        PROCESSING = "processing"
        QUEUED = "queued"

    def __init__(self, version, payload, account_sid: str, reference_sid: str, sid: str=None):
        """
        Initialize the AddOnResultInstance
        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'status': payload.get('status'),
            'add_on_sid': payload.get('add_on_sid'),
            'add_on_configuration_sid': payload.get('add_on_configuration_sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'date_completed': deserialize.rfc2822_datetime(payload.get('date_completed')),
            'reference_sid': payload.get('reference_sid'),
            'subresource_uris': payload.get('subresource_uris'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'reference_sid': reference_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AddOnResultContext for this AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        """
        if self._context is None:
            self._context = AddOnResultContext(self._version, account_sid=self._solution['account_sid'], reference_sid=self._solution['reference_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Recording AddOnResult resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: AddOnResultInstance.Status
        """
        return self._properties['status']
    
    @property
    def add_on_sid(self):
        """
        :returns: The SID of the Add-on to which the result belongs.
        :rtype: str
        """
        return self._properties['add_on_sid']
    
    @property
    def add_on_configuration_sid(self):
        """
        :returns: The SID of the Add-on configuration.
        :rtype: str
        """
        return self._properties['add_on_configuration_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def date_completed(self):
        """
        :returns: The date and time in GMT that the result was completed specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_completed']
    
    @property
    def reference_sid(self):
        """
        :returns: The SID of the recording to which the AddOnResult resource belongs.
        :rtype: str
        """
        return self._properties['reference_sid']
    
    @property
    def subresource_uris(self):
        """
        :returns: A list of related resources identified by their relative URIs.
        :rtype: dict
        """
        return self._properties['subresource_uris']
    
    def delete(self):
        """
        Deletes the AddOnResultInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the AddOnResultInstance
        

        :returns: The fetched AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        """
        return self._proxy.fetch()
    
    @property
    def payloads(self):
        """
        Access the payloads

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.PayloadList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.PayloadList
        """
        return self._proxy.payloads
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AddOnResultInstance {}>'.format(context)

class AddOnResultContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, reference_sid: str, sid: str):
        """
        Initialize the AddOnResultContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Recording AddOnResult resource to fetch.
        :param reference_sid: The SID of the recording to which the result to fetch belongs.
        :param sid: The Twilio-provided string that uniquely identifies the Recording AddOnResult resource to fetch.

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'reference_sid': reference_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Recordings/{reference_sid}/AddOnResults/{sid}.json'.format(**self._solution)
        
        self._payloads = None
    
    def delete(self):
        """
        Deletes the AddOnResultInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the AddOnResultInstance
        

        :returns: The fetched AddOnResultInstance
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.AddOnResultInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AddOnResultInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            reference_sid=self._solution['reference_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    @property
    def payloads(self):
        """
        Access the payloads

        :returns: twilio.rest.api.v2010.account.recording.add_on_result.PayloadList
        :rtype: twilio.rest.api.v2010.account.recording.add_on_result.PayloadList
        """
        if self._payloads is None:
            self._payloads = PayloadList(
                self._version, 
                self._solution['account_sid'],
                self._solution['reference_sid'],
                self._solution['sid'],
            )
        return self._payloads
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AddOnResultContext {}>'.format(context)


