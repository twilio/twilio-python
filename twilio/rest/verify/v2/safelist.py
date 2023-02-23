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
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class SafelistList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SafelistList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.verify.v2.safelist.SafelistList
        :rtype: twilio.rest.verify.v2.safelist.SafelistList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/SafeList/Numbers'.format(**self._solution)
        
        
    
    
    
    def create(self, phone_number):
        """
        Create the SafelistInstance

        :param str phone_number: The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        
        :returns: The created SafelistInstance
        :rtype: twilio.rest.verify.v2.safelist.SafelistInstance
        """
        data = values.of({ 
            'PhoneNumber': phone_number,
        })
        )
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SafelistInstance(self._version, payload)
    

    def get(self, phone_number):
        """
        Constructs a SafelistContext
        
        :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        
        :returns: twilio.rest.verify.v2.safelist.SafelistContext
        :rtype: twilio.rest.verify.v2.safelist.SafelistContext
        """
        return SafelistContext(self._version, phone_number=phone_number)

    def __call__(self, phone_number):
        """
        Constructs a SafelistContext
        
        :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
        
        :returns: twilio.rest.verify.v2.safelist.SafelistContext
        :rtype: twilio.rest.verify.v2.safelist.SafelistContext
        """
        return SafelistContext(self._version, phone_number=phone_number)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.SafelistList>'

class SafelistContext(InstanceContext):

    def __init__(self, version: Version, phone_number: str):
        """
        Initialize the SafelistContext

        :param Version version: Version that contains the resource
        :param phone_number: The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).

        :returns: twilio.rest.verify.v2.safelist.SafelistContext
        :rtype: twilio.rest.verify.v2.safelist.SafelistContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'phone_number': phone_number,
        }
        self._uri = '/SafeList/Numbers/{phone_number}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the SafelistInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SafelistInstance
        

        :returns: The fetched SafelistInstance
        :rtype: twilio.rest.verify.v2.safelist.SafelistInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SafelistInstance(
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
        return '<Twilio.Verify.V2.SafelistContext {}>'.format(context)

class SafelistInstance(InstanceResource):

    def __init__(self, version, payload, phone_number: str=None):
        """
        Initialize the SafelistInstance
        :returns: twilio.rest.verify.v2.safelist.SafelistInstance
        :rtype: twilio.rest.verify.v2.safelist.SafelistInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'phone_number': payload.get('phone_number'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'phone_number': phone_number or self._properties['phone_number'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SafelistContext for this SafelistInstance
        :rtype: twilio.rest.verify.v2.safelist.SafelistContext
        """
        if self._context is None:
            self._context = SafelistContext(self._version, phone_number=self._solution['phone_number'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the SafeList resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def phone_number(self):
        """
        :returns: The phone number in SafeList.
        :rtype: str
        """
        return self._properties['phone_number']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the SafeList resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the SafelistInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the SafelistInstance
        

        :returns: The fetched SafelistInstance
        :rtype: twilio.rest.verify.v2.safelist.SafelistInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.SafelistInstance {}>'.format(context)


