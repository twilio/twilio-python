"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Ip_messaging
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


class MemberList(ListResource):

    def __init__(self, version: Version, service_sid: str, channel_sid: str):
        """
        Initialize the MemberList
        :param Version version: Version that contains the resource
        :param service_sid: 
        :param channel_sid: 
        
        :returns: twilio.ip_messaging.v1.member..MemberList
        :rtype: twilio.ip_messaging.v1.member..MemberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid,  }
        self._uri = '/Services/${service_sid}/Channels/${channel_sid}/Members'.format(**self._solution)
        
        
    
    
    
    
    def create(self, identity, role_sid=values.unset):
        """
        Create the MemberInstance
         :param str identity: 
         :param str role_sid: 
        
        :returns: The created MemberInstance
        :rtype: twilio.rest.ip_messaging.v1.member.MemberInstance
        """
        data = values.of({ 
            'Identity': identity,
            'RoleSid': role_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])
    
    
    def stream(self, identity=values.unset, limit=None, page_size=None):
        """
        Streams MemberInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param [str] identity: 
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v1.member.MemberInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            identity=identity,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, identity=values.unset, limit=None, page_size=None):
        """
        Lists MemberInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param [str] identity: 
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.ip_messaging.v1.member.MemberInstance]
        """
        return list(self.stream(
            identity=identity,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, identity=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MemberInstance records from the API.
        Request is executed immediately
        
        :param [str] identity: 
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MemberInstance
        :rtype: twilio.rest.ip_messaging.v1.member.MemberPage
        """
        data = values.of({ 
            'Identity': serialize.map(identity),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MemberPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MemberInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MemberInstance
        :rtype: twilio.rest.ip_messaging.v1.member.MemberPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MemberPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a MemberContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v1.member.MemberContext
        :rtype: twilio.rest.ip_messaging.v1.member.MemberContext
        """
        return MemberContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a MemberContext
        
        :param sid: 
        
        :returns: twilio.rest.ip_messaging.v1.member.MemberContext
        :rtype: twilio.rest.ip_messaging.v1.member.MemberContext
        """
        return MemberContext(self._version, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.MemberList>'










class MemberPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MemberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.ip_messaging.v1.member.MemberPage
        :rtype: twilio.rest.ip_messaging.v1.member.MemberPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MemberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.ip_messaging.v1.member.MemberInstance
        :rtype: twilio.rest.ip_messaging.v1.member.MemberInstance
        """
        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.MemberPage>'





class MemberContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, channel_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'channel_sid': channel_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Channels/${channel_sid}/Members/${sid}'
        
    
    def delete(self):
        
        

        """
        Deletes the MemberInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the MemberInstance

        :returns: The fetched MemberInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, role_sid, last_consumed_message_index):
        data = values.of({
            'role_sid': role_sid,'last_consumed_message_index': last_consumed_message_index,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return MemberInstance(self._version, payload, service_sid=self._solution['service_sid'], channel_sid=self._solution['channel_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.IpMessaging.V1.MemberContext>'



class MemberInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, channel_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'channel_sid' : payload.get('channel_sid'),
            'service_sid' : payload.get('service_sid'),
            'identity' : payload.get('identity'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'role_sid' : payload.get('role_sid'),
            'last_consumed_message_index' : payload.get('last_consumed_message_index'),
            'last_consumption_timestamp' : payload.get('last_consumption_timestamp'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'channel_sid': channel_sid or self._properties['channel_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = MemberContext(
                self._version,
                service_sid=self._solution['service_sid'],channel_sid=self._solution['channel_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.IpMessaging.V1.MemberInstance {}>'.format(context)



