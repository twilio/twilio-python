"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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

# from twilio.rest.available_phone_number_country.local import LocalListInstancefrom twilio.rest.available_phone_number_country.machine_to_machine import MachineToMachineListInstancefrom twilio.rest.available_phone_number_country.mobile import MobileListInstancefrom twilio.rest.available_phone_number_country.national import NationalListInstancefrom twilio.rest.available_phone_number_country.shared_cost import SharedCostListInstancefrom twilio.rest.available_phone_number_country.toll_free import TollFreeListInstancefrom twilio.rest.available_phone_number_country.voip import VoipListInstance


class AvailablePhoneNumberCountryContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, country_code: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'country_code': country_code,  }
        self._uri = '/Accounts/${account_sid}/AvailablePhoneNumbers/${country_code}.json'
        
        self._local = None
        self._machine_to_machine = None
        self._mobile = None
        self._national = None
        self._shared_cost = None
        self._toll_free = None
        self._voip = None
    
    def fetch(self):
        
        """
        Fetch the AvailablePhoneNumberCountryInstance

        :returns: The fetched AvailablePhoneNumberCountryInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AvailablePhoneNumberCountryInstance(self._version, payload, account_sid=self._solution['account_sid'], country_code=self._solution['country_code'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryContext>'



class AvailablePhoneNumberCountryInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, country_code: str):
        super().__init__(version)
        self._properties = { 
            'country_code' : payload.get('country_code'),
            'country' : payload.get('country'),
            'uri' : payload.get('uri'),
            'beta' : payload.get('beta'),
            'subresource_uris' : payload.get('subresource_uris'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'country_code': country_code or self._properties['country_code'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AvailablePhoneNumberCountryContext(
                self._version,
                account_sid=self._solution['account_sid'],country_code=self._solution['country_code'],
            )
        return self._context

    @property
    def local(self):
        return self._proxy.local
    @property
    def machine_to_machine(self):
        return self._proxy.machine_to_machine
    @property
    def mobile(self):
        return self._proxy.mobile
    @property
    def national(self):
        return self._proxy.national
    @property
    def shared_cost(self):
        return self._proxy.shared_cost
    @property
    def toll_free(self):
        return self._proxy.toll_free
    @property
    def voip(self):
        return self._proxy.voip
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryInstance {}>'.format(context)



class AvailablePhoneNumberCountryList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/AvailablePhoneNumbers.json'
        

    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return AvailablePhoneNumberCountryPage(self._version, payload, account_sid=self._solution['account_sid'], )
    """


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AvailablePhoneNumberCountryList>'
