"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trunking
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

# from twilio.rest.trunk.credential_list import CredentialListListInstancefrom twilio.rest.trunk.ip_access_control_list import IpAccessControlListListInstancefrom twilio.rest.trunk.origination_url import OriginationUrlListInstancefrom twilio.rest.trunk.phone_number import PhoneNumberListInstancefrom twilio.rest.trunk.recording import RecordingListInstance


class TrunkContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'sid': sid,  }
        self._uri = '/Trunks/${sid}'
        
        self._credentials_lists = None
        self._ip_access_control_lists = None
        self._origination_urls = None
        self._phone_numbers = None
        self._recordings = None
    
    def delete(self):
        
        

        """
        Deletes the TrunkInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the TrunkInstance

        :returns: The fetched TrunkInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TrunkInstance(self._version, payload, sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return TrunkInstance(self._version, payload, sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TrunkContext>'



class TrunkInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'domain_name' : payload.get('domain_name'),
            'disaster_recovery_method' : payload.get('disaster_recovery_method'),
            'disaster_recovery_url' : payload.get('disaster_recovery_url'),
            'friendly_name' : payload.get('friendly_name'),
            'secure' : payload.get('secure'),
            'recording' : payload.get('recording'),
            'transfer_mode' : payload.get('transfer_mode'),
            'transfer_caller_id' : payload.get('transfer_caller_id'),
            'cnam_lookup_enabled' : payload.get('cnam_lookup_enabled'),
            'auth_type' : payload.get('auth_type'),
            'auth_type_set' : payload.get('auth_type_set'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'sid' : payload.get('sid'),
            'url' : payload.get('url'),
            'links' : payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = TrunkContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def credentials_lists(self):
        return self._proxy.credentials_lists
    @property
    def ip_access_control_lists(self):
        return self._proxy.ip_access_control_lists
    @property
    def origination_urls(self):
        return self._proxy.origination_urls
    @property
    def phone_numbers(self):
        return self._proxy.phone_numbers
    @property
    def recordings(self):
        return self._proxy.recordings
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.TrunkInstance {}>'.format(context)



class TrunkListInstance(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Trunks'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return TrunkInstance(self._version, payload, )
        
    """
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return TrunkPage(self._version, payload, )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.TrunkListInstance>'
