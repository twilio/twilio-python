"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Pricing
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


class CountryList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the CountryList
        :param Version version: Version that contains the resource
        
        :returns: twilio.pricing.v2.country..CountryList
        :rtype: twilio.pricing.v2.country..CountryList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Trunking/Countries'.format(**self._solution)
        
        
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams CountryInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.pricing.v2.country.CountryInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists CountryInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.pricing.v2.country.CountryInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CountryInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return CountryPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CountryInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return CountryPage(self._version, response, self._solution)


    def get(self, iso_country):
        """
        Constructs a CountryContext
        
        :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch.
        
        :returns: twilio.rest.pricing.v2.country.CountryContext
        :rtype: twilio.rest.pricing.v2.country.CountryContext
        """
        return CountryContext(self._version, iso_country=iso_country)

    def __call__(self, iso_country):
        """
        Constructs a CountryContext
        
        :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch.
        
        :returns: twilio.rest.pricing.v2.country.CountryContext
        :rtype: twilio.rest.pricing.v2.country.CountryContext
        """
        return CountryContext(self._version, iso_country=iso_country)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V2.CountryList>'




class CountryPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the CountryPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.pricing.v2.country.CountryPage
        :rtype: twilio.rest.pricing.v2.country.CountryPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CountryInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.pricing.v2.country.CountryInstance
        :rtype: twilio.rest.pricing.v2.country.CountryInstance
        """
        return CountryInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V2.CountryPage>'





class CountryContext(InstanceContext):
    def __init__(self, version: Version, iso_country: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'iso_country': iso_country,  }
        self._uri = '/Trunking/Countries/${iso_country}'
        
    
    def fetch(self):
        
        """
        Fetch the CountryInstance

        :returns: The fetched CountryInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CountryInstance(self._version, payload, iso_country=self._solution['iso_country'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V2.CountryContext>'



class CountryInstance(InstanceResource):
    def __init__(self, version, payload, iso_country: str):
        super().__init__(version)
        self._properties = { 
            'country' : payload.get('country'),
            'iso_country' : payload.get('iso_country'),
            'terminating_prefix_prices' : payload.get('terminating_prefix_prices'),
            'originating_call_prices' : payload.get('originating_call_prices'),
            'price_unit' : payload.get('price_unit'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'iso_country': iso_country or self._properties['iso_country'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = CountryContext(
                self._version,
                iso_country=self._solution['iso_country'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Pricing.V2.CountryInstance {}>'.format(context)



