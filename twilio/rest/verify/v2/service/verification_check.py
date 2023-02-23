"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class VerificationCheckList(ListResource):

    def __init__(self, version: Version, service_sid: str):
        """
        Initialize the VerificationCheckList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the verification [Service](https://www.twilio.com/docs/verify/api/service) to create the resource under.
        
        :returns: twilio.rest.verify.v2.service.verification_check.VerificationCheckList
        :rtype: twilio.rest.verify.v2.service.verification_check.VerificationCheckList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'service_sid': service_sid,  }
        self._uri = '/Services/${service_sid}/VerificationCheck'.format(**self._solution)
        
        
    
    def create(self, code=values.unset, to=values.unset, verification_sid=values.unset, amount=values.unset, payee=values.unset):
        """
        Create the VerificationCheckInstance
        :param str code: The 4-10 character string being verified.
        :param str to: The phone number or [email](https://www.twilio.com/docs/verify/email) to verify. Either this parameter or the `verification_sid` must be specified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :param str verification_sid: A SID that uniquely identifies the Verification Check. Either this parameter or the `to` phone number/[email](https://www.twilio.com/docs/verify/email) must be specified.
        :param str amount: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :param str payee: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        
        :returns: The created VerificationCheckInstance
        :rtype: twilio.rest.verify.v2.service.verification_check.VerificationCheckInstance
        """
        data = values.of({ 
            'Code': code,
            'To': to,
            'VerificationSid': verification_sid,
            'Amount': amount,
            'Payee': payee,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return VerificationCheckInstance(self._version, payload, service_sid=self._solution['service_sid'])
    


    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.VerificationCheckList>'


class VerificationCheckInstance(InstanceResource):

    def __init__(self, version, payload, service_sid: str):
        """
        Initialize the VerificationCheckInstance
        :returns: twilio.rest.verify.v2.service.verification_check.VerificationCheckInstance
        :rtype: twilio.rest.verify.v2.service.verification_check.VerificationCheckInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'service_sid': payload.get('service_sid'),
            'account_sid': payload.get('account_sid'),
            'to': payload.get('to'),
            'channel': payload.get('channel'),
            'status': payload.get('status'),
            'valid': payload.get('valid'),
            'amount': payload.get('amount'),
            'payee': payload.get('payee'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'sna_attempts_error_codes': payload.get('sna_attempts_error_codes'),
        }

        self._context = None
        self._solution = { 'service_sid': service_sid,  }
    
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the VerificationCheck resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def service_sid(self):
        """
        :returns: The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
        :rtype: str
        """
        return self._properties['service_sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the VerificationCheck resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def to(self):
        """
        :returns: The phone number or [email](https://www.twilio.com/docs/verify/email) being verified. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        :rtype: str
        """
        return self._properties['to']
    
    @property
    def channel(self):
        """
        :returns: 
        :rtype: VerificationCheckChannel
        """
        return self._properties['channel']
    
    @property
    def status(self):
        """
        :returns: The status of the verification. Can be: `pending`, `approved`, or `canceled`.
        :rtype: str
        """
        return self._properties['status']
    
    @property
    def valid(self):
        """
        :returns: Use \"status\" instead. Legacy property indicating whether the verification was successful.
        :rtype: bool
        """
        return self._properties['valid']
    
    @property
    def amount(self):
        """
        :returns: The amount of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :rtype: str
        """
        return self._properties['amount']
    
    @property
    def payee(self):
        """
        :returns: The payee of the associated PSD2 compliant transaction. Requires the PSD2 Service flag enabled.
        :rtype: str
        """
        return self._properties['payee']
    
    @property
    def date_created(self):
        """
        :returns: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the Verification Check resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the Verification Check resource was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def sna_attempts_error_codes(self):
        """
        :returns: List of error codes as a result of attempting a verification using the `sna` channel. The error codes are chronologically ordered, from the first attempt to the latest attempt. This will be an empty list if no errors occured or `null` if the last channel used wasn't `sna`.
        :rtype: list[object]
        """
        return self._properties['sna_attempts_error_codes']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.VerificationCheckInstance {}>'.format(context)


