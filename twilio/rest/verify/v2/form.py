r"""
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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version



class FormList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the FormList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.verify.v2.form.FormList
        :rtype: twilio.rest.verify.v2.form.FormList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    

    def get(self, form_type):
        """
        Constructs a FormContext
        
        :param form_type: The Type of this Form. Currently only `form-push` is supported.
        
        :returns: twilio.rest.verify.v2.form.FormContext
        :rtype: twilio.rest.verify.v2.form.FormContext
        """
        return FormContext(self._version, form_type=form_type)

    def __call__(self, form_type):
        """
        Constructs a FormContext
        
        :param form_type: The Type of this Form. Currently only `form-push` is supported.
        
        :returns: twilio.rest.verify.v2.form.FormContext
        :rtype: twilio.rest.verify.v2.form.FormContext
        """
        return FormContext(self._version, form_type=form_type)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.FormList>'

class FormInstance(InstanceResource):

    class FormTypes(object):
        FORM_PUSH = "form-push"

    def __init__(self, version, payload, form_type: FormTypes=None):
        """
        Initialize the FormInstance
        :returns: twilio.rest.verify.v2.form.FormInstance
        :rtype: twilio.rest.verify.v2.form.FormInstance
        """
        super().__init__(version)

        self._properties = { 
            'form_type': payload.get('form_type'),
            'forms': payload.get('forms'),
            'form_meta': payload.get('form_meta'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'form_type': form_type or self._properties['form_type'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: FormContext for this FormInstance
        :rtype: twilio.rest.verify.v2.form.FormContext
        """
        if self._context is None:
            self._context = FormContext(self._version, form_type=self._solution['form_type'],)
        return self._context
    
    @property
    def form_type(self):
        """
        :returns: 
        :rtype: FormInstance.FormTypes
        """
        return self._properties['form_type']
    
    @property
    def forms(self):
        """
        :returns: Object that contains the available forms for this type. This available forms are given in the standard [JSON Schema](https://json-schema.org/) format
        :rtype: dict
        """
        return self._properties['forms']
    
    @property
    def form_meta(self):
        """
        :returns: Additional information for the available forms for this type. E.g. The separator string used for `binding` in a Factor push.
        :rtype: dict
        """
        return self._properties['form_meta']
    
    @property
    def url(self):
        """
        :returns: The URL to access the forms for this type.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self):
        """
        Fetch the FormInstance
        

        :returns: The fetched FormInstance
        :rtype: twilio.rest.verify.v2.form.FormInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the FormInstance
        

        :returns: The fetched FormInstance
        :rtype: twilio.rest.verify.v2.form.FormInstance
        """
        return await self._proxy.fetch_async()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.FormInstance {}>'.format(context)

class FormContext(InstanceContext):

    def __init__(self, version: Version, form_type: FormInstance.FormTypes):
        """
        Initialize the FormContext

        :param Version version: Version that contains the resource
        :param form_type: The Type of this Form. Currently only `form-push` is supported.

        :returns: twilio.rest.verify.v2.form.FormContext
        :rtype: twilio.rest.verify.v2.form.FormContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'form_type': form_type,
        }
        self._uri = '/Forms/{form_type}'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the FormInstance
        

        :returns: The fetched FormInstance
        :rtype: twilio.rest.verify.v2.form.FormInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FormInstance(
            self._version,
            payload,
            form_type=self._solution['form_type'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.FormContext {}>'.format(context)


