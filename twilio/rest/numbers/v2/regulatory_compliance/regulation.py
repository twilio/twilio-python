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
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class RegulationList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the RegulationList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/RegulatoryCompliance/Regulations'.format(**self._solution)
        
        
    
    
    def stream(self, end_user_type=values.unset, iso_country=values.unset, number_type=values.unset, limit=None, page_size=None):
        """
        Streams RegulationInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param RegulationEndUserType end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param str iso_country: The ISO country code of the phone number's country.
        :param str number_type: The type of phone number that the regulatory requiremnt is restricting.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            end_user_type=end_user_type,
            iso_country=iso_country,
            number_type=number_type,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, end_user_type=values.unset, iso_country=values.unset, number_type=values.unset, limit=None, page_size=None):
        """
        Lists RegulationInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param RegulationEndUserType end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param str iso_country: The ISO country code of the phone number's country.
        :param str number_type: The type of phone number that the regulatory requiremnt is restricting.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationInstance]
        """
        return list(self.stream(
            end_user_type=end_user_type,
            iso_country=iso_country,
            number_type=number_type,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, end_user_type=values.unset, iso_country=values.unset, number_type=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of RegulationInstance records from the API.
        Request is executed immediately
        
        :param RegulationEndUserType end_user_type: The type of End User the regulation requires - can be `individual` or `business`.
        :param str iso_country: The ISO country code of the phone number's country.
        :param str number_type: The type of phone number that the regulatory requiremnt is restricting.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of RegulationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationPage
        """
        data = values.of({ 
            'EndUserType': end_user_type,
            'IsoCountry': iso_country,
            'NumberType': number_type,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return RegulationPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of RegulationInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of RegulationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return RegulationPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a RegulationContext
        
        :param sid: The unique string that identifies the Regulation resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationContext
        """
        return RegulationContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a RegulationContext
        
        :param sid: The unique string that identifies the Regulation resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationContext
        """
        return RegulationContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.RegulationList>'




class RegulationPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the RegulationPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationPage
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of RegulationInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationInstance
        """
        return RegulationInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.RegulationPage>'




class RegulationContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the RegulationContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that identifies the Regulation resource.

        :returns: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/RegulatoryCompliance/Regulations/{sid}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the RegulationInstance
        

        :returns: The fetched RegulationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return RegulationInstance(
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
        return '<Twilio.Numbers.V2.RegulationContext {}>'.format(context)

class RegulationInstance(InstanceResource):

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the RegulationInstance
        :returns: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'friendly_name': payload.get('friendly_name'),
            'iso_country': payload.get('iso_country'),
            'number_type': payload.get('number_type'),
            'end_user_type': payload.get('end_user_type'),
            'requirements': payload.get('requirements'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: RegulationContext for this RegulationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationContext
        """
        if self._context is None:
            self._context = RegulationContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Regulation resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def friendly_name(self):
        """
        :returns: A human-readable description that is assigned to describe the Regulation resource. Examples can include Germany: Mobile - Business.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def iso_country(self):
        """
        :returns: The ISO country code of the phone number's country.
        :rtype: str
        """
        return self._properties['iso_country']
    
    @property
    def number_type(self):
        """
        :returns: The type of phone number restricted by the regulatory requirement. For example, Germany mobile phone numbers provisioned by businesses require a business name with commercial register proof from the Handelsregisterauszug and a proof of address from Handelsregisterauszug or a trade license by Gewerbeanmeldung.
        :rtype: str
        """
        return self._properties['number_type']
    
    @property
    def end_user_type(self):
        """
        :returns: 
        :rtype: RegulationEndUserType
        """
        return self._properties['end_user_type']
    
    @property
    def requirements(self):
        """
        :returns: The SID of an object that holds the regulatory information of the phone number country, phone number type, and end user type.
        :rtype: dict
        """
        return self._properties['requirements']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the Regulation resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self):
        """
        Fetch the RegulationInstance
        

        :returns: The fetched RegulationInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.regulation.RegulationInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.RegulationInstance {}>'.format(context)


