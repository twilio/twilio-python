"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Lookups
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class PhoneNumberList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.lookups.v2.phone_number.PhoneNumberList
        :rtype: twilio.rest.lookups.v2.phone_number.PhoneNumberList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self, phone_number):
        """
        Constructs a PhoneNumberContext
        
        :param phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North America).
        
        :returns: twilio.rest.lookups.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v2.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number):
        """
        Constructs a PhoneNumberContext
        
        :param phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North America).
        
        :returns: twilio.rest.lookups.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v2.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Lookups.V2.PhoneNumberList>'

class PhoneNumberInstance(InstanceResource):

    class ValidationError(object):
        TOO_SHORT = "TOO_SHORT"
        TOO_LONG = "TOO_LONG"
        INVALID_BUT_POSSIBLE = "INVALID_BUT_POSSIBLE"
        INVALID_COUNTRY_CODE = "INVALID_COUNTRY_CODE"
        INVALID_LENGTH = "INVALID_LENGTH"
        NOT_A_NUMBER = "NOT_A_NUMBER"

    def __init__(self, version, payload, phone_number: str=None):
        """
        Initialize the PhoneNumberInstance
        :returns: twilio.rest.lookups.v2.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.lookups.v2.phone_number.PhoneNumberInstance
        """
        super().__init__(version)

        self._properties = { 
            'calling_country_code': payload.get('calling_country_code'),
            'country_code': payload.get('country_code'),
            'phone_number': payload.get('phone_number'),
            'national_format': payload.get('national_format'),
            'valid': payload.get('valid'),
            'validation_errors': payload.get('validation_errors'),
            'caller_name': payload.get('caller_name'),
            'sim_swap': payload.get('sim_swap'),
            'call_forwarding': payload.get('call_forwarding'),
            'live_activity': payload.get('live_activity'),
            'line_type_intelligence': payload.get('line_type_intelligence'),
            'identity_match': payload.get('identity_match'),
            'sms_pumping_risk': payload.get('sms_pumping_risk'),
            'disposable_phone_number_risk': payload.get('disposable_phone_number_risk'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'phone_number': phone_number or self._properties['phone_number'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.lookups.v2.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(self._version, phone_number=self._solution['phone_number'],)
        return self._context
    
    @property
    def calling_country_code(self):
        """
        :returns: International dialing prefix of the phone number defined in the E.164 standard.
        :rtype: str
        """
        return self._properties['calling_country_code']
    
    @property
    def country_code(self):
        """
        :returns: The phone number's [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
        :rtype: str
        """
        return self._properties['country_code']
    
    @property
    def phone_number(self):
        """
        :returns: The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
        :rtype: str
        """
        return self._properties['phone_number']
    
    @property
    def national_format(self):
        """
        :returns: The phone number in [national format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers).
        :rtype: str
        """
        return self._properties['national_format']
    
    @property
    def valid(self):
        """
        :returns: Boolean which indicates if the phone number is in a valid range that can be freely assigned by a carrier to a user.
        :rtype: bool
        """
        return self._properties['valid']
    
    @property
    def validation_errors(self):
        """
        :returns: Contains reasons why a phone number is invalid. Possible values: TOO_SHORT, TOO_LONG, INVALID_BUT_POSSIBLE, INVALID_COUNTRY_CODE, INVALID_LENGTH, NOT_A_NUMBER.
        :rtype: list[PhoneNumberInstance.ValidationError]
        """
        return self._properties['validation_errors']
    
    @property
    def caller_name(self):
        """
        :returns: An object that contains caller name information based on [CNAM](https://support.twilio.com/hc/en-us/articles/360051670533-Getting-Started-with-CNAM-Caller-ID).
        :rtype: dict
        """
        return self._properties['caller_name']
    
    @property
    def sim_swap(self):
        """
        :returns: An object that contains information on the last date the subscriber identity module (SIM) was changed for a mobile phone number.
        :rtype: dict
        """
        return self._properties['sim_swap']
    
    @property
    def call_forwarding(self):
        """
        :returns: An object that contains information on the unconditional call forwarding status of mobile phone number.
        :rtype: dict
        """
        return self._properties['call_forwarding']
    
    @property
    def live_activity(self):
        """
        :returns: An object that contains live activity information for a mobile phone number.
        :rtype: dict
        """
        return self._properties['live_activity']
    
    @property
    def line_type_intelligence(self):
        """
        :returns: An object that contains line type information including the carrier name, mobile country code, and mobile network code.
        :rtype: dict
        """
        return self._properties['line_type_intelligence']
    
    @property
    def identity_match(self):
        """
        :returns: An object that contains identity match information. The result of comparing user-provided information including name, address, date of birth, national ID, against authoritative phone-based data sources
        :rtype: dict
        """
        return self._properties['identity_match']
    
    @property
    def sms_pumping_risk(self):
        """
        :returns: An object that contains information on if a phone number has been currently or previously blocked by Verify Fraud Guard for receiving malicious SMS pumping traffic as well as other signals associated with risky carriers and low conversion rates.
        :rtype: dict
        """
        return self._properties['sms_pumping_risk']
    
    @property
    def disposable_phone_number_risk(self):
        """
        :returns: An object that contains information on if a mobile phone number could be a disposable or burner number.
        :rtype: dict
        """
        return self._properties['disposable_phone_number_risk']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the resource.
        :rtype: str
        """
        return self._properties['url']
    
    def fetch(self, fields=values.unset, country_code=values.unset, first_name=values.unset, last_name=values.unset, address_line1=values.unset, address_line2=values.unset, city=values.unset, state=values.unset, postal_code=values.unset, address_country_code=values.unset, national_id=values.unset, date_of_birth=values.unset):
        """
        Fetch the PhoneNumberInstance
        
        :params str fields: A comma-separated list of fields to return. Possible values are caller_name, sim_swap, call_forwarding, live_activity, line_type_intelligence, identity_match.
        :params str country_code: The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
        :params str first_name: User’s first name. This query parameter is only used (optionally) for identity_match package requests.
        :params str last_name: User’s last name. This query parameter is only used (optionally) for identity_match package requests.
        :params str address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
        :params str address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
        :params str city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
        :params str state: User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
        :params str postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
        :params str address_country_code: User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
        :params str national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
        :params str date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.lookups.v2.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch(fields=fields, country_code=country_code, first_name=first_name, last_name=last_name, address_line1=address_line1, address_line2=address_line2, city=city, state=state, postal_code=postal_code, address_country_code=address_country_code, national_id=national_id, date_of_birth=date_of_birth, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Lookups.V2.PhoneNumberInstance {}>'.format(context)

class PhoneNumberContext(InstanceContext):

    def __init__(self, version: Version, phone_number: str):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param phone_number: The phone number to lookup in E.164 or national format. Default country code is +1 (North America).

        :returns: twilio.rest.lookups.v2.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v2.phone_number.PhoneNumberContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'phone_number': phone_number,
        }
        self._uri = '/PhoneNumbers/{phone_number}'.format(**self._solution)
        
    
    def fetch(self, fields=values.unset, country_code=values.unset, first_name=values.unset, last_name=values.unset, address_line1=values.unset, address_line2=values.unset, city=values.unset, state=values.unset, postal_code=values.unset, address_country_code=values.unset, national_id=values.unset, date_of_birth=values.unset):
        """
        Fetch the PhoneNumberInstance
        
        :params str fields: A comma-separated list of fields to return. Possible values are caller_name, sim_swap, call_forwarding, live_activity, line_type_intelligence, identity_match.
        :params str country_code: The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
        :params str first_name: User’s first name. This query parameter is only used (optionally) for identity_match package requests.
        :params str last_name: User’s last name. This query parameter is only used (optionally) for identity_match package requests.
        :params str address_line1: User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
        :params str address_line2: User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
        :params str city: User’s city. This query parameter is only used (optionally) for identity_match package requests.
        :params str state: User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
        :params str postal_code: User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
        :params str address_country_code: User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
        :params str national_id: User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
        :params str date_of_birth: User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.lookups.v2.phone_number.PhoneNumberInstance
        """
        
        data = values.of({ 
            'Fields': fields,
            'CountryCode': country_code,
            'FirstName': first_name,
            'LastName': last_name,
            'AddressLine1': address_line1,
            'AddressLine2': address_line2,
            'City': city,
            'State': state,
            'PostalCode': postal_code,
            'AddressCountryCode': address_country_code,
            'NationalId': national_id,
            'DateOfBirth': date_of_birth,
        })
        
        payload = self._version.fetch(method='GET', uri=self._uri, params=data)

        return PhoneNumberInstance(
            self._version,
            payload,
            phone_number=self._solution['phone_number'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Lookups.V2.PhoneNumberContext {}>'.format(context)


