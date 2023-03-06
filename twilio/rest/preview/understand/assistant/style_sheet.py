"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
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



class StyleSheetList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the StyleSheetList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant
        
        :returns: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetList
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        
        
        
    
    

    def get(self):
        """
        Constructs a StyleSheetContext
        
        :returns: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetContext
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetContext
        """
        return StyleSheetContext(self._version, assistant_sid=self._solution['assistant_sid'])

    def __call__(self):
        """
        Constructs a StyleSheetContext
        
        :returns: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetContext
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetContext
        """
        return StyleSheetContext(self._version, assistant_sid=self._solution['assistant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Understand.StyleSheetList>'

class StyleSheetContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the StyleSheetContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant

        :returns: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetContext
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
        }
        self._uri = '/Assistants/{assistant_sid}/StyleSheet'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the StyleSheetInstance
        

        :returns: The fetched StyleSheetInstance
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return StyleSheetInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            
        )
        
    def update(self, style_sheet=values.unset):
        """
        Update the StyleSheetInstance
        
        :params object style_sheet: The JSON Style sheet string

        :returns: The updated StyleSheetInstance
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetInstance
        """
        data = values.of({ 
            'StyleSheet': serialize.object(style_sheet),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return StyleSheetInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.StyleSheetContext {}>'.format(context)

class StyleSheetInstance(InstanceResource):

    def __init__(self, version, payload, assistant_sid: str):
        """
        Initialize the StyleSheetInstance
        :returns: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetInstance
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'assistant_sid': payload.get('assistant_sid'),
            'url': payload.get('url'),
            'data': payload.get('data'),
        }

        self._context = None
        self._solution = { 'assistant_sid': assistant_sid,  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: StyleSheetContext for this StyleSheetInstance
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetContext
        """
        if self._context is None:
            self._context = StyleSheetContext(self._version, assistant_sid=self._solution['assistant_sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Assistant
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the Assistant
        :rtype: str
        """
        return self._properties['assistant_sid']
    
    @property
    def url(self):
        """
        :returns: 
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def data(self):
        """
        :returns: The JSON style sheet object
        :rtype: dict
        """
        return self._properties['data']
    
    def fetch(self):
        """
        Fetch the StyleSheetInstance
        

        :returns: The fetched StyleSheetInstance
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetInstance
        """
        return self._proxy.fetch()
    
    def update(self, style_sheet=values.unset):
        """
        Update the StyleSheetInstance
        
        :params object style_sheet: The JSON Style sheet string

        :returns: The updated StyleSheetInstance
        :rtype: twilio.rest.preview.understand.assistant.style_sheet.StyleSheetInstance
        """
        return self._proxy.update(style_sheet=style_sheet, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Understand.StyleSheetInstance {}>'.format(context)


