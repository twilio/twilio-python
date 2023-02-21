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

from twilio.rest.api.v2010.auth_types.calls import AuthTypeCallsList
from twilio.rest.api.v2010.auth_types.registrations import AuthTypeRegistrationsList


class AuthTypesList(ListResource):

    def __init__(self, version: Version, account_sid: str, domain_sid: str):
        """
        Initialize the AuthTypesList
        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the CredentialListMapping resource to fetch.
        :param domain_sid: The SID of the SIP domain that contains the resource to fetch.
        
        :returns: twilio.api.v2010.auth_types..AuthTypesList
        :rtype: twilio.api.v2010.auth_types..AuthTypesList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'domain_sid': domain_sid,  }
        self._uri = '/Accounts/${account_sid}/SIP/Domains/${domain_sid}/Auth.json'.format(**self._solution)
        
        self._calls = None
        self._registrations = None
        

    @property
    def calls(self):
        """
        Access the calls

        :returns: twilio.rest.api.v2010.auth_types.calls.AuthTypeCallsList
        :rtype: twilio.rest.api.v2010.auth_types.calls.AuthTypeCallsList
        """
        if self._calls is None:
            self._calls = AuthTypeCallsList(self._version, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'])
        return self.calls
    @property
    def registrations(self):
        """
        Access the registrations

        :returns: twilio.rest.api.v2010.auth_types.registrations.AuthTypeRegistrationsList
        :rtype: twilio.rest.api.v2010.auth_types.registrations.AuthTypeRegistrationsList
        """
        if self._registrations is None:
            self._registrations = AuthTypeRegistrationsList(self._version, account_sid=self._solution['account_sid'], domain_sid=self._solution['domain_sid'])
        return self.registrations

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthTypesList>'




