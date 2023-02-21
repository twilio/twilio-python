"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Proxy
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
from twilio.rest.proxy.v1.participant.message_interactions import MessageInteractionList


class ParticipantList(ListResource):

    def __init__(self, version: Version, service_sid: str, session_sid: str):
        """
        Initialize the ParticipantList
        :param Version version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resources to read.
        :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resources to read.
        
        :returns: twilio.proxy.v1.participant..ParticipantList
        :rtype: twilio.proxy.v1.participant..ParticipantList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'session_sid': session_sid,  }
        self._uri = '/Services/${service_sid}/Sessions/${session_sid}/Participants'.format(**self._solution)
        
        
    
    
    
    def create(self, identifier, friendly_name=values.unset, proxy_identifier=values.unset, proxy_identifier_sid=values.unset):
        """
        Create the ParticipantInstance
         :param str identifier: The phone number of the Participant.
         :param str friendly_name: The string that you assigned to describe the participant. This value must be 255 characters or fewer. **This value should not have PII.**
         :param str proxy_identifier: The proxy phone number to use for the Participant. If not specified, Proxy will select a number from the pool.
         :param str proxy_identifier_sid: The SID of the Proxy Identifier to assign to the Participant.
        
        :returns: The created ParticipantInstance
        :rtype: twilio.rest.proxy.v1.participant.ParticipantInstance
        """
        data = values.of({ 
            'Identifier': identifier,
            'FriendlyName': friendly_name,
            'ProxyIdentifier': proxy_identifier,
            'ProxyIdentifierSid': proxy_identifier_sid,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return ParticipantInstance(self._version, payload, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ParticipantInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.proxy.v1.participant.ParticipantInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ParticipantInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.participant.ParticipantInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ParticipantInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.proxy.v1.participant.ParticipantPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ParticipantPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ParticipantInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ParticipantInstance
        :rtype: twilio.rest.proxy.v1.participant.ParticipantPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ParticipantPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
        
        :returns: twilio.rest.proxy.v1.participant.ParticipantContext
        :rtype: twilio.rest.proxy.v1.participant.ParticipantContext
        """
        return ParticipantContext(self._version, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ParticipantContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Participant resource to fetch.
        
        :returns: twilio.rest.proxy.v1.participant.ParticipantContext
        :rtype: twilio.rest.proxy.v1.participant.ParticipantContext
        """
        return ParticipantContext(self._version, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.ParticipantList>'








class ParticipantPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ParticipantPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.proxy.v1.participant.ParticipantPage
        :rtype: twilio.rest.proxy.v1.participant.ParticipantPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ParticipantInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.proxy.v1.participant.ParticipantInstance
        :rtype: twilio.rest.proxy.v1.participant.ParticipantInstance
        """
        return ParticipantInstance(self._version, payload, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.ParticipantPage>'





class ParticipantContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, session_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'session_sid': session_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Sessions/${session_sid}/Participants/${sid}'
        
        self._message_interactions = None
    
    def delete(self):
        
        

        """
        Deletes the ParticipantInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the ParticipantInstance

        :returns: The fetched ParticipantInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ParticipantInstance(self._version, payload, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.ParticipantContext>'



class ParticipantInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, session_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'session_sid' : payload.get('session_sid'),
            'service_sid' : payload.get('service_sid'),
            'account_sid' : payload.get('account_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'identifier' : payload.get('identifier'),
            'proxy_identifier' : payload.get('proxy_identifier'),
            'proxy_identifier_sid' : payload.get('proxy_identifier_sid'),
            'date_deleted' : payload.get('date_deleted'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'session_sid': session_sid or self._properties['session_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ParticipantContext(
                self._version,
                service_sid=self._solution['service_sid'],session_sid=self._solution['session_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def message_interactions(self):
        return self._proxy.message_interactions
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.ParticipantInstance {}>'.format(context)



