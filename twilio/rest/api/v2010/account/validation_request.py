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



class ValidationRequestList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the ValidationRequestList
        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource.
        
        :returns: twilio.api.v2010.outgoing_caller_id..ValidationRequestList
        :rtype: twilio.api.v2010.outgoing_caller_id..ValidationRequestList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/OutgoingCallerIds.json'.format(**self._solution)
        
        
    
    def create(self, phone_number, friendly_name=values.unset, call_delay=values.unset, extension=values.unset, status_callback=values.unset, status_callback_method=values.unset):
        """
        Create the ValidationRequestInstance
         :param str phone_number: The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
         :param str friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number.
         :param int call_delay: The number of seconds to delay before initiating the verification call. Can be an integer between `0` and `60`, inclusive. The default is `0`.
         :param str extension: The digits to dial after connecting the verification call.
         :param str status_callback: The URL we should call using the `status_callback_method` to send status information about the verification process to your application.
         :param str status_callback_method: The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`, and the default is `POST`.
        
        :returns: The created ValidationRequestInstance
        :rtype: twilio.rest.api.v2010.outgoing_caller_id.ValidationRequestInstance
        """
        data = values.of({ 
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'CallDelay': call_delay,
            'Extension': extension,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return ValidationRequestInstance(self._version, payload, account_sid=self._solution['account_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ValidationRequestList>'



class ValidationRequestInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'call_sid' : payload.get('call_sid'),
            'friendly_name' : payload.get('friendly_name'),
            'phone_number' : payload.get('phone_number'),
            'validation_code' : payload.get('validation_code'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = ValidationRequestContext(
                self._version,
                account_sid=self._solution['account_sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ValidationRequestInstance {}>'.format(context)



