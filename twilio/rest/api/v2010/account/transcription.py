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
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class TranscriptionList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the TranscriptionList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resources to read.
        
        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionList
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/Transcriptions.json'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the TranscriptionInstance

        :returns: The fetched TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return TranscriptionInstance(self._version, payload, account_sid=self._solution['account_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams TranscriptionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.transcription.TranscriptionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists TranscriptionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.transcription.TranscriptionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of TranscriptionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return TranscriptionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TranscriptionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return TranscriptionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a TranscriptionContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        """
        return TranscriptionContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a TranscriptionContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Transcription resource to fetch.
        
        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        """
        return TranscriptionContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TranscriptionList>'






class TranscriptionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the TranscriptionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionPage
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TranscriptionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        return TranscriptionInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TranscriptionPage>'




class TranscriptionInstance(InstanceResource):

    class Status(object):
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        FAILED = "failed"

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the TranscriptionInstance
        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'duration': payload.get('duration'),
            'price': deserialize.decimal(payload.get('price')),
            'price_unit': payload.get('price_unit'),
            'recording_sid': payload.get('recording_sid'),
            'sid': payload.get('sid'),
            'status': payload.get('status'),
            'transcription_text': payload.get('transcription_text'),
            'type': payload.get('type'),
            'uri': payload.get('uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TranscriptionContext for this TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        """
        if self._context is None:
            self._context = TranscriptionContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def api_version(self):
        """
        :returns: The API version used to create the transcription.
        :rtype: str
        """
        return self._properties['api_version']
    
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
    def duration(self):
        """
        :returns: The duration of the transcribed audio in seconds.
        :rtype: str
        """
        return self._properties['duration']
    
    @property
    def price(self):
        """
        :returns: The charge for the transcript in the currency associated with the account. This value is populated after the transcript is complete so it may not be available immediately.
        :rtype: float
        """
        return self._properties['price']
    
    @property
    def price_unit(self):
        """
        :returns: The currency in which `price` is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. `usd`, `eur`, `jpy`).
        :rtype: str
        """
        return self._properties['price_unit']
    
    @property
    def recording_sid(self):
        """
        :returns: The SID of the [Recording](https://www.twilio.com/docs/voice/api/recording) from which the transcription was created.
        :rtype: str
        """
        return self._properties['recording_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Transcription resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: Status
        """
        return self._properties['status']
    
    @property
    def transcription_text(self):
        """
        :returns: The text content of the transcription.
        :rtype: str
        """
        return self._properties['transcription_text']
    
    @property
    def type(self):
        """
        :returns: The transcription type. Can only be: `fast`.
        :rtype: str
        """
        return self._properties['type']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    def delete(self):
        """
        Deletes the TranscriptionInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the TranscriptionInstance
        

        :returns: The fetched TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.TranscriptionInstance {}>'.format(context)

class TranscriptionContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the TranscriptionContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Transcription resource to fetch.:param sid: The Twilio-provided string that uniquely identifies the Transcription resource to fetch.

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Transcriptions/{sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the TranscriptionInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the TranscriptionInstance
        

        :returns: The fetched TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TranscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.TranscriptionContext {}>'.format(context)


