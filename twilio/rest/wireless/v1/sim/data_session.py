r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Wireless
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DataSessionList(ListResource):

    def __init__(self, version: Version, sim_sid: str):
        """
        Initialize the DataSessionList

        :param Version version: Version that contains the resource
        :param sim_sid: The SID of the [Sim resource](https://www.twilio.com/docs/wireless/api/sim-resource) with the Data Sessions to read.
        
        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionList
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'sim_sid': sim_sid,  }
        self._uri = '/Sims/{sim_sid}/DataSessions'.format(**self._solution)
        
        
    
    def stream(self, limit=None, page_size=None):
        """
        Streams DataSessionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.wireless.v1.sim.data_session.DataSessionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that streams DataSessionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.wireless.v1.sim.data_session.DataSessionInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DataSessionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.data_session.DataSessionInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronous coroutine that lists DataSessionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.wireless.v1.sim.data_session.DataSessionInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of DataSessionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return DataSessionPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronous coroutine that retrieve a single page of DataSessionInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return DataSessionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DataSessionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return DataSessionPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronous coroutine that retrieve a specific page of DataSessionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return DataSessionPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.DataSessionList>'


class DataSessionPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DataSessionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DataSessionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionInstance
        """
        return DataSessionInstance(self._version, payload, sim_sid=self._solution['sim_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Wireless.V1.DataSessionPage>'




class DataSessionInstance(InstanceResource):

    def __init__(self, version, payload, sim_sid: str):
        """
        Initialize the DataSessionInstance
        :returns: twilio.rest.wireless.v1.sim.data_session.DataSessionInstance
        :rtype: twilio.rest.wireless.v1.sim.data_session.DataSessionInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'sim_sid': payload.get('sim_sid'),
            'account_sid': payload.get('account_sid'),
            'radio_link': payload.get('radio_link'),
            'operator_mcc': payload.get('operator_mcc'),
            'operator_mnc': payload.get('operator_mnc'),
            'operator_country': payload.get('operator_country'),
            'operator_name': payload.get('operator_name'),
            'cell_id': payload.get('cell_id'),
            'cell_location_estimate': payload.get('cell_location_estimate'),
            'packets_uploaded': deserialize.integer(payload.get('packets_uploaded')),
            'packets_downloaded': deserialize.integer(payload.get('packets_downloaded')),
            'last_updated': deserialize.iso8601_datetime(payload.get('last_updated')),
            'start': deserialize.iso8601_datetime(payload.get('start')),
            'end': deserialize.iso8601_datetime(payload.get('end')),
            'imei': payload.get('imei'),
        }

        self._context = None
        self._solution = { 'sim_sid': sim_sid,  }
    
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the DataSession resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def sim_sid(self):
        """
        :returns: The SID of the [Sim resource](https://www.twilio.com/docs/wireless/api/sim-resource) that the Data Session is for.
        :rtype: str
        """
        return self._properties['sim_sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the DataSession resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def radio_link(self):
        """
        :returns: The generation of wireless technology that the device was using.
        :rtype: str
        """
        return self._properties['radio_link']
    
    @property
    def operator_mcc(self):
        """
        :returns: The 'mobile country code' is the unique ID of the home country where the Data Session took place. See: [MCC/MNC lookup](http://mcc-mnc.com/).
        :rtype: str
        """
        return self._properties['operator_mcc']
    
    @property
    def operator_mnc(self):
        """
        :returns: The 'mobile network code' is the unique ID specific to the mobile operator network where the Data Session took place.
        :rtype: str
        """
        return self._properties['operator_mnc']
    
    @property
    def operator_country(self):
        """
        :returns: The three letter country code representing where the device's Data Session took place. This is determined by looking up the `operator_mcc`.
        :rtype: str
        """
        return self._properties['operator_country']
    
    @property
    def operator_name(self):
        """
        :returns: The friendly name of the mobile operator network that the [SIM](https://www.twilio.com/docs/wireless/api/sim-resource)-connected device is attached to. This is determined by looking up the `operator_mnc`.
        :rtype: str
        """
        return self._properties['operator_name']
    
    @property
    def cell_id(self):
        """
        :returns: The unique ID of the cellular tower that the device was attached to at the moment when the Data Session was last updated.
        :rtype: str
        """
        return self._properties['cell_id']
    
    @property
    def cell_location_estimate(self):
        """
        :returns: An object that describes the estimated location in latitude and longitude where the device's Data Session took place. The location is derived from the `cell_id` when the Data Session was last updated. See [Cell Location Estimate Object](https://www.twilio.com/docs/wireless/api/datasession-resource#cell-location-estimate-object). 
        :rtype: dict
        """
        return self._properties['cell_location_estimate']
    
    @property
    def packets_uploaded(self):
        """
        :returns: The number of packets uploaded by the device between the `start` time and when the Data Session was last updated.
        :rtype: int
        """
        return self._properties['packets_uploaded']
    
    @property
    def packets_downloaded(self):
        """
        :returns: The number of packets downloaded by the device between the `start` time and when the Data Session was last updated.
        :rtype: int
        """
        return self._properties['packets_downloaded']
    
    @property
    def last_updated(self):
        """
        :returns: The date that the resource was last updated, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        :rtype: datetime
        """
        return self._properties['last_updated']
    
    @property
    def start(self):
        """
        :returns: The date that the Data Session started, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        :rtype: datetime
        """
        return self._properties['start']
    
    @property
    def end(self):
        """
        :returns: The date that the record ended, given as GMT in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format.
        :rtype: datetime
        """
        return self._properties['end']
    
    @property
    def imei(self):
        """
        :returns: The 'international mobile equipment identity' is the unique ID of the device using the SIM to connect. An IMEI is a 15-digit string: 14 digits for the device identifier plus a check digit calculated using the Luhn formula.
        :rtype: str
        """
        return self._properties['imei']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Wireless.V1.DataSessionInstance {}>'.format(context)



