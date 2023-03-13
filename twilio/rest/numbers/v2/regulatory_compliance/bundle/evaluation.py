"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class EvaluationList(ListResource):

    def __init__(self, version: Version, bundle_sid: str):
        """
        Initialize the EvaluationList

        :param Version version: Version that contains the resource
        :param bundle_sid: The unique string that identifies the Bundle resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'bundle_sid': bundle_sid,  }
        self._uri = '/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations'.format(**self._solution)
        
        
    
    
    def create(self):
        """
        Create the EvaluationInstance

        
        :returns: The created EvaluationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance
        """
        
        
        payload = self._version.create(method='POST', uri=self._uri, )

        return EvaluationInstance(self._version, payload, bundle_sid=self._solution['bundle_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams EvaluationInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists EvaluationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of EvaluationInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of EvaluationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return EvaluationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of EvaluationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of EvaluationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return EvaluationPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a EvaluationContext
        
        :param sid: The unique string that identifies the Evaluation resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationContext
        """
        return EvaluationContext(self._version, bundle_sid=self._solution['bundle_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a EvaluationContext
        
        :param sid: The unique string that identifies the Evaluation resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationContext
        """
        return EvaluationContext(self._version, bundle_sid=self._solution['bundle_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.EvaluationList>'






class EvaluationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the EvaluationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationPage
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of EvaluationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance
        """
        return EvaluationInstance(self._version, payload, bundle_sid=self._solution['bundle_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.EvaluationPage>'




class EvaluationInstance(InstanceResource):

    class Status(object):
        COMPLIANT = "compliant"
        NONCOMPLIANT = "noncompliant"

    def __init__(self, version, payload, bundle_sid: str, sid: str=None):
        """
        Initialize the EvaluationInstance
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'regulation_sid': payload.get('regulation_sid'),
            'bundle_sid': payload.get('bundle_sid'),
            'status': payload.get('status'),
            'results': payload.get('results'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'bundle_sid': bundle_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EvaluationContext for this EvaluationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationContext
        """
        if self._context is None:
            self._context = EvaluationContext(self._version, bundle_sid=self._solution['bundle_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Evaluation resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Bundle resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def regulation_sid(self):
        """
        :returns: The unique string of a regulation that is associated to the Bundle resource.
        :rtype: str
        """
        return self._properties['regulation_sid']
    
    @property
    def bundle_sid(self):
        """
        :returns: The unique string that we created to identify the Bundle resource.
        :rtype: str
        """
        return self._properties['bundle_sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: EvaluationInstance.Status
        """
        return self._properties['status']
    
    @property
    def results(self):
        """
        :returns: The results of the Evaluation which includes the valid and invalid attributes.
        :rtype: list[object]
        """
        return self._properties['results']
    
    @property
    def date_created(self):
        """
        :returns: 
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the EvaluationInstance
        

        :returns: The fetched EvaluationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.EvaluationInstance {}>'.format(context)

class EvaluationContext(InstanceContext):

    def __init__(self, version: Version, bundle_sid: str, sid: str):
        """
        Initialize the EvaluationContext

        :param Version version: Version that contains the resource
        :param bundle_sid: The unique string that we created to identify the Bundle resource.
        :param sid: The unique string that identifies the Evaluation resource.

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'bundle_sid': bundle_sid,
            'sid': sid,
        }
        self._uri = '/RegulatoryCompliance/Bundles/{bundle_sid}/Evaluations/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the EvaluationInstance
        

        :returns: The fetched EvaluationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation.EvaluationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return EvaluationInstance(
            self._version,
            payload,
            bundle_sid=self._solution['bundle_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.EvaluationContext {}>'.format(context)


