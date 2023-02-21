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


class MessageInteractionList(ListResource):

    def __init__(self, version: Version, service_sid: str, session_sid: str, participant_sid: str):
        """
        Initialize the MessageInteractionList
        :param Version version: Version that contains the resource
        :param service_sid: The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
        :param session_sid: The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from.
        :param participant_sid: The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) to read the resources from.
        
        :returns: twilio.proxy.v1.message_interaction..MessageInteractionList
        :rtype: twilio.proxy.v1.message_interaction..MessageInteractionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'session_sid': session_sid, 'participant_sid': participant_sid,  }
        self._uri = '/Services/${service_sid}/Sessions/${session_sid}/Participants/${participant_sid}/MessageInteractions'.format(**self._solution)
        
        
    
    
    def create(self, body=values.unset, media_url=values.unset):
        """
        Create the MessageInteractionInstance
         :param str body: The message to send to the participant
         :param [str] media_url: Reserved. Not currently supported.
        
        :returns: The created MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.message_interaction.MessageInteractionInstance
        """
        data = values.of({ 
            'Body': body,
            'MediaUrl': serialize.map(media_url, lambda e: e),
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return MessageInteractionInstance(self._version, payload, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], participant_sid=self._solution['participant_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams MessageInteractionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.proxy.v1.message_interaction.MessageInteractionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists MessageInteractionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.proxy.v1.message_interaction.MessageInteractionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MessageInteractionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.message_interaction.MessageInteractionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MessageInteractionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessageInteractionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.message_interaction.MessageInteractionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MessageInteractionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a MessageInteractionContext
        
        :param sid: The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
        
        :returns: twilio.rest.proxy.v1.message_interaction.MessageInteractionContext
        :rtype: twilio.rest.proxy.v1.message_interaction.MessageInteractionContext
        """
        return MessageInteractionContext(self._version, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], participant_sid=self._solution['participant_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a MessageInteractionContext
        
        :param sid: The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
        
        :returns: twilio.rest.proxy.v1.message_interaction.MessageInteractionContext
        :rtype: twilio.rest.proxy.v1.message_interaction.MessageInteractionContext
        """
        return MessageInteractionContext(self._version, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], participant_sid=self._solution['participant_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.MessageInteractionList>'






class MessageInteractionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MessageInteractionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.proxy.v1.message_interaction.MessageInteractionPage
        :rtype: twilio.rest.proxy.v1.message_interaction.MessageInteractionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInteractionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.proxy.v1.message_interaction.MessageInteractionInstance
        :rtype: twilio.rest.proxy.v1.message_interaction.MessageInteractionInstance
        """
        return MessageInteractionInstance(self._version, payload, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], participant_sid=self._solution['participant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.MessageInteractionPage>'





class MessageInteractionContext(InstanceContext):
    def __init__(self, version: Version, service_sid: str, session_sid: str, participant_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid, 'session_sid': session_sid, 'participant_sid': participant_sid, 'sid': sid,  }
        self._uri = '/Services/${service_sid}/Sessions/${session_sid}/Participants/${participant_sid}/MessageInteractions/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the MessageInteractionInstance

        :returns: The fetched MessageInteractionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessageInteractionInstance(self._version, payload, service_sid=self._solution['service_sid'], session_sid=self._solution['session_sid'], participant_sid=self._solution['participant_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Proxy.V1.MessageInteractionContext>'



class MessageInteractionInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, session_sid: str, participant_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'session_sid' : payload.get('session_sid'),
            'service_sid' : payload.get('service_sid'),
            'account_sid' : payload.get('account_sid'),
            'data' : payload.get('data'),
            'type' : payload.get('type'),
            'participant_sid' : payload.get('participant_sid'),
            'inbound_participant_sid' : payload.get('inbound_participant_sid'),
            'inbound_resource_sid' : payload.get('inbound_resource_sid'),
            'inbound_resource_status' : payload.get('inbound_resource_status'),
            'inbound_resource_type' : payload.get('inbound_resource_type'),
            'inbound_resource_url' : payload.get('inbound_resource_url'),
            'outbound_participant_sid' : payload.get('outbound_participant_sid'),
            'outbound_resource_sid' : payload.get('outbound_resource_sid'),
            'outbound_resource_status' : payload.get('outbound_resource_status'),
            'outbound_resource_type' : payload.get('outbound_resource_type'),
            'outbound_resource_url' : payload.get('outbound_resource_url'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],'session_sid': session_sid or self._properties['session_sid'],'participant_sid': participant_sid or self._properties['participant_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = MessageInteractionContext(
                self._version,
                service_sid=self._solution['service_sid'],session_sid=self._solution['session_sid'],participant_sid=self._solution['participant_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Proxy.V1.MessageInteractionInstance {}>'.format(context)



