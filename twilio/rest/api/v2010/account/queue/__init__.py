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
from twilio.rest.api.v2010.account.queue.member import MemberList


class QueueList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the QueueList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read.
        
        :returns: twilio.rest.api.v2010.account.queue.QueueList
        :rtype: twilio.rest.api.v2010.account.queue.QueueList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/Queues.json'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, max_size=values.unset):
        """
        Create the QueueInstance

        :param str friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :param int max_size: The maximum number of calls allowed to be in the queue. The default is 100. The maximum is 5000.
        
        :returns: The created QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueueInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'MaxSize': max_size,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return QueueInstance(self._version, payload, account_sid=self._solution['account_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams QueueInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.queue.QueueInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists QueueInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.queue.QueueInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of QueueInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueuePage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return QueuePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of QueueInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueuePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return QueuePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a QueueContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Queue resource to update
        
        :returns: twilio.rest.api.v2010.account.queue.QueueContext
        :rtype: twilio.rest.api.v2010.account.queue.QueueContext
        """
        return QueueContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a QueueContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Queue resource to update
        
        :returns: twilio.rest.api.v2010.account.queue.QueueContext
        :rtype: twilio.rest.api.v2010.account.queue.QueueContext
        """
        return QueueContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.QueueList>'










class QueuePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the QueuePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.queue.QueuePage
        :rtype: twilio.rest.api.v2010.account.queue.QueuePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of QueueInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.queue.QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueueInstance
        """
        return QueueInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.QueuePage>'




class QueueInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the QueueInstance
        :returns: twilio.rest.api.v2010.account.queue.QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueueInstance
        """
        super().__init__(version)

        self._properties = { 
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'current_size': deserialize.integer(payload.get('current_size')),
            'friendly_name': payload.get('friendly_name'),
            'uri': payload.get('uri'),
            'account_sid': payload.get('account_sid'),
            'average_wait_time': deserialize.integer(payload.get('average_wait_time')),
            'sid': payload.get('sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'max_size': deserialize.integer(payload.get('max_size')),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: QueueContext for this QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueueContext
        """
        if self._context is None:
            self._context = QueueContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that this resource was last updated, specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def current_size(self):
        """
        :returns: The number of calls currently in the queue.
        :rtype: int
        """
        return self._properties['current_size']
    
    @property
    def friendly_name(self):
        """
        :returns: A string that you assigned to describe this resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def uri(self):
        """
        :returns: The URI of this resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created this Queue resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def average_wait_time(self):
        """
        :returns:  The average wait time in seconds of the members in this queue. This is calculated at the time of the request.
        :rtype: int
        """
        return self._properties['average_wait_time']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify this Queue resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that this resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def max_size(self):
        """
        :returns:  The maximum number of calls that can be in the queue. The default is 100 and the maximum is 5000.
        :rtype: int
        """
        return self._properties['max_size']
    
    def delete(self):
        """
        Deletes the QueueInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the QueueInstance
        

        :returns: The fetched QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueueInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, max_size=values.unset):
        """
        Update the QueueInstance
        
        :params str friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :params int max_size: The maximum number of calls allowed to be in the queue. The default is 100. The maximum is 5000.

        :returns: The updated QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueueInstance
        """
        return self._proxy.update(friendly_name=friendly_name, max_size=max_size, )
    
    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.api.v2010.account.queue.MemberList
        :rtype: twilio.rest.api.v2010.account.queue.MemberList
        """
        return self._proxy.members
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.QueueInstance {}>'.format(context)

class QueueContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the QueueContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the Queue resource to update

        :returns: twilio.rest.api.v2010.account.queue.QueueContext
        :rtype: twilio.rest.api.v2010.account.queue.QueueContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Queues/{sid}.json'.format(**self._solution)
        
        self._members = None
    
    def delete(self):
        """
        Deletes the QueueInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the QueueInstance
        

        :returns: The fetched QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueueInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, max_size=values.unset):
        """
        Update the QueueInstance
        
        :params str friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
        :params int max_size: The maximum number of calls allowed to be in the queue. The default is 100. The maximum is 5000.

        :returns: The updated QueueInstance
        :rtype: twilio.rest.api.v2010.account.queue.QueueInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'MaxSize': max_size,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return QueueInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def members(self):
        """
        Access the members

        :returns: twilio.rest.api.v2010.account.queue.MemberList
        :rtype: twilio.rest.api.v2010.account.queue.MemberList
        """
        if self._members is None:
            self._members = MemberList(
                self._version, 
                self._solution['account_sid'],
                self._solution['sid'],
            )
        return self._members
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.QueueContext {}>'.format(context)


