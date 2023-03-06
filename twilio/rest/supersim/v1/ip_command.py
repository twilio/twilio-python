"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
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


class IpCommandList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the IpCommandList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.supersim.v1.ip_command.IpCommandList
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/IpCommands'.format(**self._solution)
        
        
    
    
    def create(self, sim, payload, device_port, payload_type=values.unset, callback_url=values.unset, callback_method=values.unset):
        """
        Create the IpCommandInstance

        :param str sim: The `sid` or `unique_name` of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) to send the IP Command to.
        :param str payload: The data that will be sent to the device. The payload cannot exceed 1300 bytes. If the PayloadType is set to text, the payload is encoded in UTF-8. If PayloadType is set to binary, the payload is encoded in Base64.
        :param int device_port: The device port to which the IP Command will be sent.
        :param PayloadType payload_type: 
        :param str callback_url: The URL we should call using the `callback_method` after we have sent the IP Command.
        :param str callback_method: The HTTP method we should use to call `callback_url`. Can be `GET` or `POST`, and the default is `POST`.
        
        :returns: The created IpCommandInstance
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandInstance
        """
        data = values.of({ 
            'Sim': sim,
            'Payload': payload,
            'DevicePort': device_port,
            'PayloadType': payload_type,
            'CallbackUrl': callback_url,
            'CallbackMethod': callback_method,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return IpCommandInstance(self._version, payload)
    
    
    def stream(self, sim=values.unset, sim_iccid=values.unset, status=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Streams IpCommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str sim: The SID or unique name of the Sim resource that IP Command was sent to or from.
        :param str sim_iccid: The ICCID of the Sim resource that IP Command was sent to or from.
        :param Status status: The status of the IP Command. Can be: `queued`, `sent`, `received` or `failed`. See the [IP Command Status Values](https://www.twilio.com/docs/wireless/api/ipcommand-resource#status-values) for a description of each.
        :param Direction direction: The direction of the IP Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.ip_command.IpCommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            sim=sim,
            sim_iccid=sim_iccid,
            status=status,
            direction=direction,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, sim=values.unset, sim_iccid=values.unset, status=values.unset, direction=values.unset, limit=None, page_size=None):
        """
        Lists IpCommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str sim: The SID or unique name of the Sim resource that IP Command was sent to or from.
        :param str sim_iccid: The ICCID of the Sim resource that IP Command was sent to or from.
        :param Status status: The status of the IP Command. Can be: `queued`, `sent`, `received` or `failed`. See the [IP Command Status Values](https://www.twilio.com/docs/wireless/api/ipcommand-resource#status-values) for a description of each.
        :param Direction direction: The direction of the IP Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.ip_command.IpCommandInstance]
        """
        return list(self.stream(
            sim=sim,
            sim_iccid=sim_iccid,
            status=status,
            direction=direction,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sim=values.unset, sim_iccid=values.unset, status=values.unset, direction=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of IpCommandInstance records from the API.
        Request is executed immediately
        
        :param str sim: The SID or unique name of the Sim resource that IP Command was sent to or from.
        :param str sim_iccid: The ICCID of the Sim resource that IP Command was sent to or from.
        :param Status status: The status of the IP Command. Can be: `queued`, `sent`, `received` or `failed`. See the [IP Command Status Values](https://www.twilio.com/docs/wireless/api/ipcommand-resource#status-values) for a description of each.
        :param Direction direction: The direction of the IP Command. Can be `to_sim` or `from_sim`. The value of `to_sim` is synonymous with the term `mobile terminated`, and `from_sim` is synonymous with the term `mobile originated`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpCommandInstance
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandPage
        """
        data = values.of({ 
            'Sim': sim,
            'SimIccid': sim_iccid,
            'Status': status,
            'Direction': direction,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return IpCommandPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IpCommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IpCommandInstance
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return IpCommandPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a IpCommandContext
        
        :param sid: The SID of the IP Command resource to fetch.
        
        :returns: twilio.rest.supersim.v1.ip_command.IpCommandContext
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandContext
        """
        return IpCommandContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a IpCommandContext
        
        :param sid: The SID of the IP Command resource to fetch.
        
        :returns: twilio.rest.supersim.v1.ip_command.IpCommandContext
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandContext
        """
        return IpCommandContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.IpCommandList>'






class IpCommandPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the IpCommandPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.ip_command.IpCommandPage
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IpCommandInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.ip_command.IpCommandInstance
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandInstance
        """
        return IpCommandInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.IpCommandPage>'




class IpCommandInstance(InstanceResource):

    class Direction(object):
        TO_SIM = "to_sim"
        FROM_SIM = "from_sim"

    class PayloadType(object):
        TEXT = "text"
        BINARY = "binary"

    class Status(object):
        QUEUED = "queued"
        SENT = "sent"
        RECEIVED = "received"
        FAILED = "failed"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the IpCommandInstance
        :returns: twilio.rest.supersim.v1.ip_command.IpCommandInstance
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'sim_sid': payload.get('sim_sid'),
            'sim_iccid': payload.get('sim_iccid'),
            'status': payload.get('status'),
            'direction': payload.get('direction'),
            'device_ip': payload.get('device_ip'),
            'device_port': deserialize.integer(payload.get('device_port')),
            'payload_type': payload.get('payload_type'),
            'payload': payload.get('payload'),
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

        :returns: IpCommandContext for this IpCommandInstance
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandContext
        """
        if self._context is None:
            self._context = IpCommandContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the IP Command resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IP Command resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def sim_sid(self):
        """
        :returns: The SID of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) that this IP Command was sent to or from.
        :rtype: str
        """
        return self._properties['sim_sid']
    
    @property
    def sim_iccid(self):
        """
        :returns: The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) that this IP Command was sent to or from.
        :rtype: str
        """
        return self._properties['sim_iccid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: Status
        """
        return self._properties['status']
    
    @property
    def direction(self):
        """
        :returns: 
        :rtype: Direction
        """
        return self._properties['direction']
    
    @property
    def device_ip(self):
        """
        :returns: The IP address of the device that the IP Command was sent to or received from. For an IP Command sent to a Super SIM, `device_ip` starts out as `null`, and once the IP Command is “sent”, the `device_ip` will be filled out. An IP Command sent from a Super SIM have its `device_ip` always set.
        :rtype: str
        """
        return self._properties['device_ip']
    
    @property
    def device_port(self):
        """
        :returns: For an IP Command sent to a Super SIM, it would be the destination port of the IP message. For an IP Command sent from a Super SIM, it would be the source port of the IP message.
        :rtype: int
        """
        return self._properties['device_port']
    
    @property
    def payload_type(self):
        """
        :returns: 
        :rtype: PayloadType
        """
        return self._properties['payload_type']
    
    @property
    def payload(self):
        """
        :returns: The payload that is carried in the IP/UDP message. The payload can be encoded in either text or binary format. For text payload, UTF-8 encoding must be used.  For an IP Command sent to a Super SIM, the payload is appended to the IP/UDP message “as is”. The payload should not exceed 1300 bytes.  For an IP Command sent from a Super SIM, the payload from the received IP/UDP message is extracted and sent in binary encoding. For an IP Command sent from a Super SIM, the payload should not exceed 1300 bytes. If it is larger than 1300 bytes, there might be fragmentation on the upstream and the message may appear truncated.
        :rtype: str
        """
        return self._properties['payload']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the IP Command resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the IpCommandInstance
        

        :returns: The fetched IpCommandInstance
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.IpCommandInstance {}>'.format(context)

class IpCommandContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the IpCommandContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the IP Command resource to fetch.

        :returns: twilio.rest.supersim.v1.ip_command.IpCommandContext
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/IpCommands/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the IpCommandInstance
        

        :returns: The fetched IpCommandInstance
        :rtype: twilio.rest.supersim.v1.ip_command.IpCommandInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return IpCommandInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.IpCommandContext {}>'.format(context)


