"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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


class ReservationList(ListResource):

    def __init__(self, version: Version, workspace_sid: str, worker_sid: str):
        """
        Initialize the ReservationList
        :param Version version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the WorkerReservation resources to read.
        :param worker_sid: The SID of the reserved Worker resource with the WorkerReservation resources to read.
        
        :returns: twilio.taskrouter.v1.reservation..ReservationList
        :rtype: twilio.taskrouter.v1.reservation..ReservationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'worker_sid': worker_sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workers/${worker_sid}/Reservations'.format(**self._solution)
        
        
    
    
    
    def stream(self, reservation_status=values.unset, limit=None, page_size=None):
        """
        Streams ReservationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param WorkerReservationStatus reservation_status: Returns the list of reservations for a worker with a specified ReservationStatus. Can be: `pending`, `accepted`, `rejected`, `timeout`, `canceled`, or `rescinded`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.reservation.ReservationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            reservation_status=reservation_status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, reservation_status=values.unset, limit=None, page_size=None):
        """
        Lists ReservationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param WorkerReservationStatus reservation_status: Returns the list of reservations for a worker with a specified ReservationStatus. Can be: `pending`, `accepted`, `rejected`, `timeout`, `canceled`, or `rescinded`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.taskrouter.v1.reservation.ReservationInstance]
        """
        return list(self.stream(
            reservation_status=reservation_status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, reservation_status=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ReservationInstance records from the API.
        Request is executed immediately
        
        :param WorkerReservationStatus reservation_status: Returns the list of reservations for a worker with a specified ReservationStatus. Can be: `pending`, `accepted`, `rejected`, `timeout`, `canceled`, or `rescinded`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.reservation.ReservationPage
        """
        data = values.of({ 
            'ReservationStatus': reservation_status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ReservationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ReservationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.reservation.ReservationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ReservationPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ReservationContext
        
        :param sid: The SID of the WorkerReservation resource to update.
        
        :returns: twilio.rest.taskrouter.v1.reservation.ReservationContext
        :rtype: twilio.rest.taskrouter.v1.reservation.ReservationContext
        """
        return ReservationContext(self._version, workspace_sid=self._solution['workspace_sid'], worker_sid=self._solution['worker_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ReservationContext
        
        :param sid: The SID of the WorkerReservation resource to update.
        
        :returns: twilio.rest.taskrouter.v1.reservation.ReservationContext
        :rtype: twilio.rest.taskrouter.v1.reservation.ReservationContext
        """
        return ReservationContext(self._version, workspace_sid=self._solution['workspace_sid'], worker_sid=self._solution['worker_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ReservationList>'






class ReservationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ReservationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.taskrouter.v1.reservation.ReservationPage
        :rtype: twilio.rest.taskrouter.v1.reservation.ReservationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ReservationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.reservation.ReservationInstance
        :rtype: twilio.rest.taskrouter.v1.reservation.ReservationInstance
        """
        return ReservationInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], worker_sid=self._solution['worker_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ReservationPage>'





class ReservationContext(InstanceContext):
    def __init__(self, version: Version, workspace_sid: str, worker_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'workspace_sid': workspace_sid, 'worker_sid': worker_sid, 'sid': sid,  }
        self._uri = '/Workspaces/${workspace_sid}/Workers/${worker_sid}/Reservations/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the ReservationInstance

        :returns: The fetched ReservationInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ReservationInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], worker_sid=self._solution['worker_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, reservation_status, worker_activity_sid, instruction, dequeue_post_work_activity_sid, dequeue_from, dequeue_record, dequeue_timeout, dequeue_to, dequeue_status_callback_url, call_from, call_record, call_timeout, call_to, call_url, call_status_callback_url, call_accept, redirect_call_sid, redirect_accept, redirect_url, to, from_, status_callback, status_callback_method, status_callback_event, timeout, record, muted, beep, start_conference_on_enter, end_conference_on_exit, wait_url, wait_method, early_media, max_participants, conference_status_callback, conference_status_callback_method, conference_status_callback_event, conference_record, conference_trim, recording_channels, recording_status_callback, recording_status_callback_method, conference_recording_status_callback, conference_recording_status_callback_method, region, sip_auth_username, sip_auth_password, dequeue_status_callback_event, post_work_activity_sid, end_conference_on_customer_exit, beep_on_customer_entrance):
        data = values.of({
            'reservation_status': reservation_status,'worker_activity_sid': worker_activity_sid,'instruction': instruction,'dequeue_post_work_activity_sid': dequeue_post_work_activity_sid,'dequeue_from': dequeue_from,'dequeue_record': dequeue_record,'dequeue_timeout': dequeue_timeout,'dequeue_to': dequeue_to,'dequeue_status_callback_url': dequeue_status_callback_url,'call_from': call_from,'call_record': call_record,'call_timeout': call_timeout,'call_to': call_to,'call_url': call_url,'call_status_callback_url': call_status_callback_url,'call_accept': call_accept,'redirect_call_sid': redirect_call_sid,'redirect_accept': redirect_accept,'redirect_url': redirect_url,'to': to,'from_': from_,'status_callback': status_callback,'status_callback_method': status_callback_method,'status_callback_event': status_callback_event,'timeout': timeout,'record': record,'muted': muted,'beep': beep,'start_conference_on_enter': start_conference_on_enter,'end_conference_on_exit': end_conference_on_exit,'wait_url': wait_url,'wait_method': wait_method,'early_media': early_media,'max_participants': max_participants,'conference_status_callback': conference_status_callback,'conference_status_callback_method': conference_status_callback_method,'conference_status_callback_event': conference_status_callback_event,'conference_record': conference_record,'conference_trim': conference_trim,'recording_channels': recording_channels,'recording_status_callback': recording_status_callback,'recording_status_callback_method': recording_status_callback_method,'conference_recording_status_callback': conference_recording_status_callback,'conference_recording_status_callback_method': conference_recording_status_callback_method,'region': region,'sip_auth_username': sip_auth_username,'sip_auth_password': sip_auth_password,'dequeue_status_callback_event': dequeue_status_callback_event,'post_work_activity_sid': post_work_activity_sid,'end_conference_on_customer_exit': end_conference_on_customer_exit,'beep_on_customer_entrance': beep_on_customer_entrance,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ReservationInstance(self._version, payload, workspace_sid=self._solution['workspace_sid'], worker_sid=self._solution['worker_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.ReservationContext>'



class ReservationInstance(InstanceResource):
    def __init__(self, version, payload, workspace_sid: str, worker_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'reservation_status' : payload.get('reservation_status'),
            'sid' : payload.get('sid'),
            'task_sid' : payload.get('task_sid'),
            'worker_name' : payload.get('worker_name'),
            'worker_sid' : payload.get('worker_sid'),
            'workspace_sid' : payload.get('workspace_sid'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'workspace_sid': workspace_sid or self._properties['workspace_sid'],'worker_sid': worker_sid or self._properties['worker_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ReservationContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],worker_sid=self._solution['worker_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.ReservationInstance {}>'.format(context)



