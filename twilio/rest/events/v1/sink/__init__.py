"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Events
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
from twilio.rest.events.v1.sink.sink_test import SinkTestList
from twilio.rest.events.v1.sink.sink_validate import SinkValidateList


class SinkList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SinkList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.events.v1.sink.SinkList
        :rtype: twilio.rest.events.v1.sink.SinkList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Sinks'.format(**self._solution)
        
        
    
    
    
    
    def create(self, description, sink_configuration, sink_type):
        """
        Create the SinkInstance

        :param str description: A human readable description for the Sink **This value should not contain PII.**
        :param object sink_configuration: The information required for Twilio to connect to the provided Sink encoded as JSON.
        :param SinkSinkType sink_type: 
        
        :returns: The created SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        data = values.of({ 
            'Description': description,
            'SinkConfiguration': serialize.object(sink_configuration),
            'SinkType': sink_type,
        })
        )
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SinkInstance(self._version, payload)
    
    
    def stream(self, in_use=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Streams SinkInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param bool in_use: A boolean query parameter filtering the results to return sinks used/not used by a subscription.
        :param str status: A String query parameter filtering the results by status `initialized`, `validating`, `active` or `failed`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.sink.SinkInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            in_use=in_use,
            status=status,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, in_use=values.unset, status=values.unset, limit=None, page_size=None):
        """
        Lists SinkInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param bool in_use: A boolean query parameter filtering the results to return sinks used/not used by a subscription.
        :param str status: A String query parameter filtering the results by status `initialized`, `validating`, `active` or `failed`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.events.v1.sink.SinkInstance]
        """
        return list(self.stream(
            in_use=in_use,
            status=status,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, in_use=values.unset, status=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SinkInstance records from the API.
        Request is executed immediately
        
        :param bool in_use: A boolean query parameter filtering the results to return sinks used/not used by a subscription.
        :param str status: A String query parameter filtering the results by status `initialized`, `validating`, `active` or `failed`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkPage
        """
        data = values.of({ 
            'InUse': in_use,
            'Status': status,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SinkPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SinkInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SinkPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SinkContext
        
        :param sid: A 34 character string that uniquely identifies this Sink.
        
        :returns: twilio.rest.events.v1.sink.SinkContext
        :rtype: twilio.rest.events.v1.sink.SinkContext
        """
        return SinkContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a SinkContext
        
        :param sid: A 34 character string that uniquely identifies this Sink.
        
        :returns: twilio.rest.events.v1.sink.SinkContext
        :rtype: twilio.rest.events.v1.sink.SinkContext
        """
        return SinkContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SinkList>'










class SinkPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SinkPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.events.v1.sink.SinkPage
        :rtype: twilio.rest.events.v1.sink.SinkPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SinkInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.events.v1.sink.SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        return SinkInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Events.V1.SinkPage>'




class SinkContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the SinkContext

        :param Version version: Version that contains the resource
        :param sid: A 34 character string that uniquely identifies this Sink.

        :returns: twilio.rest.events.v1.sink.SinkContext
        :rtype: twilio.rest.events.v1.sink.SinkContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/Sinks/{sid}'.format(**self._solution)
        
        self._sink_test = None
        self._sink_validate = None
    
    def delete(self):
        """
        Deletes the SinkInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SinkInstance
        

        :returns: The fetched SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SinkInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, description):
        """
        Update the SinkInstance
        
        :params str description: A human readable description for the Sink **This value should not contain PII.**

        :returns: The updated SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        data = values.of({ 
            'Description': description,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SinkInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def sink_test(self):
        """
        Access the sink_test

        :returns: twilio.rest.events.v1.sink.SinkTestList
        :rtype: twilio.rest.events.v1.sink.SinkTestList
        """
        if self._sink_test is None:
            self._sink_test = SinkTestList(self._version, self._solution['sid'],
            )
        return self._sink_test
    
    @property
    def sink_validate(self):
        """
        Access the sink_validate

        :returns: twilio.rest.events.v1.sink.SinkValidateList
        :rtype: twilio.rest.events.v1.sink.SinkValidateList
        """
        if self._sink_validate is None:
            self._sink_validate = SinkValidateList(self._version, self._solution['sid'],
            )
        return self._sink_validate
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SinkContext {}>'.format(context)

class SinkInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the SinkInstance
        :returns: twilio.rest.events.v1.sink.SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        super().__init__(version)

        self._properties = { 
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'description': payload.get('description'),
            'sid': payload.get('sid'),
            'sink_configuration': payload.get('sink_configuration'),
            'sink_type': payload.get('sink_type'),
            'status': payload.get('status'),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SinkContext for this SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkContext
        """
        if self._context is None:
            self._context = SinkContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def date_created(self):
        """
        :returns: The date that this Sink was created, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this Sink was updated, given in ISO 8601 format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def description(self):
        """
        :returns: A human readable description for the Sink
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this Sink.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def sink_configuration(self):
        """
        :returns: The information required for Twilio to connect to the provided Sink encoded as JSON.
        :rtype: dict
        """
        return self._properties['sink_configuration']
    
    @property
    def sink_type(self):
        """
        :returns: 
        :rtype: SinkSinkType
        """
        return self._properties['sink_type']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: SinkStatus
        """
        return self._properties['status']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: Contains a dictionary of URL links to nested resources of this Sink.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the SinkInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the SinkInstance
        

        :returns: The fetched SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        return self._proxy.fetch()
    
    def update(self, description):
        """
        Update the SinkInstance
        
        :params str description: A human readable description for the Sink **This value should not contain PII.**

        :returns: The updated SinkInstance
        :rtype: twilio.rest.events.v1.sink.SinkInstance
        """
        return self._proxy.update(description=description, )
    
    @property
    def sink_test(self):
        """
        Access the sink_test

        :returns: twilio.rest.events.v1.sink.SinkTestList
        :rtype: twilio.rest.events.v1.sink.SinkTestList
        """
        return self._proxy.sink_test
    
    @property
    def sink_validate(self):
        """
        Access the sink_validate

        :returns: twilio.rest.events.v1.sink.SinkValidateList
        :rtype: twilio.rest.events.v1.sink.SinkValidateList
        """
        return self._proxy.sink_validate
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Events.V1.SinkInstance {}>'.format(context)


