"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
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
from twilio.rest.studio.v2.execution.execution_context import ExecutionContextList
from twilio.rest.studio.v2.execution.steps import ExecutionStepList


class ExecutionList(ListResource):

    def __init__(self, version: Version, flow_sid: str):
        """
        Initialize the ExecutionList
        :param Version version: Version that contains the resource
        :param flow_sid: The SID of the Flow with the Execution resources to read.
        
        :returns: twilio.studio.v2.execution..ExecutionList
        :rtype: twilio.studio.v2.execution..ExecutionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid,  }
        self._uri = '/Flows/${flow_sid}/Executions'.format(**self._solution)
        
        
    
    
    
    
    def create(self, to, from_, parameters=values.unset):
        """
        Create the ExecutionInstance
         :param str to: The Contact phone number to start a Studio Flow Execution, available as variable `{{contact.channel.address}}`.
         :param str from_: The Twilio phone number to send messages or initiate calls from during the Flow's Execution. Available as variable `{{flow.channel.address}}`. For SMS, this can also be a Messaging Service SID.
         :param bool, date, datetime, dict, float, int, list, str, none_type parameters: JSON data that will be added to the Flow's context and that can be accessed as variables inside your Flow. For example, if you pass in `Parameters={\"name\":\"Zeke\"}`, a widget in your Flow can reference the variable `{{flow.data.name}}`, which returns \"Zeke\". Note: the JSON value must explicitly be passed as a string, not as a hash object. Depending on your particular HTTP library, you may need to add quotes or URL encode the JSON string.
        
        :returns: The created ExecutionInstance
        :rtype: twilio.rest.studio.v2.execution.ExecutionInstance
        """
        data = values.of({ 
            'To': to,
            'From': from_,
            'Parameters': parameters,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return ExecutionInstance(self._version, payload, flow_sid=self._solution['flow_sid'])
    
    
    def stream(self, date_created_from=values.unset, date_created_to=values.unset, limit=None, page_size=None):
        """
        Streams ExecutionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param datetime date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param datetime date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v2.execution.ExecutionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, date_created_from=values.unset, date_created_to=values.unset, limit=None, page_size=None):
        """
        Lists ExecutionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param datetime date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param datetime date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.studio.v2.execution.ExecutionInstance]
        """
        return list(self.stream(
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, date_created_from=values.unset, date_created_to=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ExecutionInstance records from the API.
        Request is executed immediately
        
        :param datetime date_created_from: Only show Execution resources starting on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param datetime date_created_to: Only show Execution resources starting before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time, given as `YYYY-MM-DDThh:mm:ss-hh:mm`.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ExecutionInstance
        :rtype: twilio.rest.studio.v2.execution.ExecutionPage
        """
        data = values.of({ 
            'DateCreatedFrom': serialize.iso8601_datetime(date_created_from),
            'DateCreatedTo': serialize.iso8601_datetime(date_created_to),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ExecutionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ExecutionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ExecutionInstance
        :rtype: twilio.rest.studio.v2.execution.ExecutionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ExecutionPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ExecutionContext
        
        :param sid: The SID of the Execution resource to update.
        
        :returns: twilio.rest.studio.v2.execution.ExecutionContext
        :rtype: twilio.rest.studio.v2.execution.ExecutionContext
        """
        return ExecutionContext(self._version, flow_sid=self._solution['flow_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ExecutionContext
        
        :param sid: The SID of the Execution resource to update.
        
        :returns: twilio.rest.studio.v2.execution.ExecutionContext
        :rtype: twilio.rest.studio.v2.execution.ExecutionContext
        """
        return ExecutionContext(self._version, flow_sid=self._solution['flow_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.ExecutionList>'










class ExecutionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ExecutionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.studio.v2.execution.ExecutionPage
        :rtype: twilio.rest.studio.v2.execution.ExecutionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ExecutionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.studio.v2.execution.ExecutionInstance
        :rtype: twilio.rest.studio.v2.execution.ExecutionInstance
        """
        return ExecutionInstance(self._version, payload, flow_sid=self._solution['flow_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.ExecutionPage>'





class ExecutionContext(InstanceContext):
    def __init__(self, version: Version, flow_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'flow_sid': flow_sid, 'sid': sid,  }
        self._uri = '/Flows/${flow_sid}/Executions/${sid}'
        
        self._execution_context = None
        self._steps = None
    
    def delete(self):
        
        

        """
        Deletes the ExecutionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the ExecutionInstance

        :returns: The fetched ExecutionInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ExecutionInstance(self._version, payload, flow_sid=self._solution['flow_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, status):
        data = values.of({
            'status': status,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return ExecutionInstance(self._version, payload, flow_sid=self._solution['flow_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Studio.V2.ExecutionContext>'



class ExecutionInstance(InstanceResource):
    def __init__(self, version, payload, flow_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'account_sid' : payload.get('account_sid'),
            'flow_sid' : payload.get('flow_sid'),
            'contact_channel_address' : payload.get('contact_channel_address'),
            'context' : payload.get('context'),
            'status' : payload.get('status'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'flow_sid': flow_sid or self._properties['flow_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ExecutionContext(
                self._version,
                flow_sid=self._solution['flow_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def execution_context(self):
        return self._proxy.execution_context
    @property
    def steps(self):
        return self._proxy.steps
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Studio.V2.ExecutionInstance {}>'.format(context)



