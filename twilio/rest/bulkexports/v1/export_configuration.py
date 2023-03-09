r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Bulkexports
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



class ExportConfigurationList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the ExportConfigurationList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationList
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        
        
        
    
    

    def get(self, resource_type):
        """
        Constructs a ExportConfigurationContext
        
        :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
        
        :returns: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationContext
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationContext
        """
        return ExportConfigurationContext(self._version, resource_type=resource_type)

    def __call__(self, resource_type):
        """
        Constructs a ExportConfigurationContext
        
        :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants
        
        :returns: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationContext
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationContext
        """
        return ExportConfigurationContext(self._version, resource_type=resource_type)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Bulkexports.V1.ExportConfigurationList>'

class ExportConfigurationInstance(InstanceResource):

    def __init__(self, version, payload, resource_type: str=None):
        """
        Initialize the ExportConfigurationInstance
        :returns: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationInstance
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationInstance
        """
        super().__init__(version)

        self._properties = { 
            'enabled': payload.get('enabled'),
            'webhook_url': payload.get('webhook_url'),
            'webhook_method': payload.get('webhook_method'),
            'resource_type': payload.get('resource_type'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'resource_type': resource_type or self._properties['resource_type'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ExportConfigurationContext for this ExportConfigurationInstance
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationContext
        """
        if self._context is None:
            self._context = ExportConfigurationContext(self._version, resource_type=self._solution['resource_type'],)
        return self._context
    
    @property
    def enabled(self):
        """
        :returns: If true, Twilio will automatically generate every day's file when the day is over.
        :rtype: bool
        """
        return self._properties['enabled']
    
    @property
    def webhook_url(self):
        """
        :returns: Stores the URL destination for the method specified in webhook_method.
        :rtype: str
        """
        return self._properties['webhook_url']
    
    @property
    def webhook_method(self):
        """
        :returns: Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url
        :rtype: str
        """
        return self._properties['webhook_method']
    
    @property
    def resource_type(self):
        """
        :returns: The type of communication – Messages, Calls, Conferences, and Participants
        :rtype: str
        """
        return self._properties['resource_type']
    
    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: str
        """
        return self._properties['url']
    
    
    def fetch(self):
        """
        Fetch the ExportConfigurationInstance
        

        :returns: The fetched ExportConfigurationInstance
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self):
        """
        Asynchronous coroutine to fetch the ExportConfigurationInstance
        

        :returns: The fetched ExportConfigurationInstance
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationInstance
        """
        return await self._proxy.fetch_async()
    
    
    def update(self, enabled=values.unset, webhook_url=values.unset, webhook_method=values.unset):
        """
        Update the ExportConfigurationInstance
        
        :params bool enabled: If true, Twilio will automatically generate every day's file when the day is over.
        :params str webhook_url: Stores the URL destination for the method specified in webhook_method.
        :params str webhook_method: Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url

        :returns: The updated ExportConfigurationInstance
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationInstance
        """
        return self._proxy.update(enabled=enabled, webhook_url=webhook_url, webhook_method=webhook_method, )

    async def update_async(self, enabled=values.unset, webhook_url=values.unset, webhook_method=values.unset):
        """
        Asynchronous coroutine to update the ExportConfigurationInstance
        
        :params bool enabled: If true, Twilio will automatically generate every day's file when the day is over.
        :params str webhook_url: Stores the URL destination for the method specified in webhook_method.
        :params str webhook_method: Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url

        :returns: The updated ExportConfigurationInstance
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationInstance
        """
        return await self._proxy.update_async(enabled=enabled, webhook_url=webhook_url, webhook_method=webhook_method, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Bulkexports.V1.ExportConfigurationInstance {}>'.format(context)

class ExportConfigurationContext(InstanceContext):

    def __init__(self, version: Version, resource_type: str):
        """
        Initialize the ExportConfigurationContext

        :param Version version: Version that contains the resource
        :param resource_type: The type of communication – Messages, Calls, Conferences, and Participants

        :returns: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationContext
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'resource_type': resource_type,
        }
        self._uri = '/Exports/{resource_type}/Configuration'.format(**self._solution)
        
    
    def fetch(self):
        """
        Fetch the ExportConfigurationInstance
        

        :returns: The fetched ExportConfigurationInstance
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ExportConfigurationInstance(
            self._version,
            payload,
            resource_type=self._solution['resource_type'],
            
        )
        
    def update(self, enabled=values.unset, webhook_url=values.unset, webhook_method=values.unset):
        """
        Update the ExportConfigurationInstance
        
        :params bool enabled: If true, Twilio will automatically generate every day's file when the day is over.
        :params str webhook_url: Stores the URL destination for the method specified in webhook_method.
        :params str webhook_method: Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url

        :returns: The updated ExportConfigurationInstance
        :rtype: twilio.rest.bulkexports.v1.export_configuration.ExportConfigurationInstance
        """
        data = values.of({ 
            'Enabled': enabled,
            'WebhookUrl': webhook_url,
            'WebhookMethod': webhook_method,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ExportConfigurationInstance(
            self._version,
            payload,
            resource_type=self._solution['resource_type']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Bulkexports.V1.ExportConfigurationContext {}>'.format(context)


