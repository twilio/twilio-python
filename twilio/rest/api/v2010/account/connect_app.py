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


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ConnectAppList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the ConnectAppList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to read.
        
        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppList
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/ConnectApps.json'.format(**self._solution)
        
        
    
    
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ConnectAppInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.connect_app.ConnectAppInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ConnectAppInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.connect_app.ConnectAppInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ConnectAppInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ConnectAppPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ConnectAppInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ConnectAppPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ConnectAppContext
        
        :param sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
        
        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        """
        return ConnectAppContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ConnectAppContext
        
        :param sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to update.
        
        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        """
        return ConnectAppContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConnectAppList>'








class ConnectAppPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ConnectAppPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppPage
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ConnectAppInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        return ConnectAppInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ConnectAppPage>'




class ConnectAppInstance(InstanceResource):

    class ConnectAppPermission(object):
        GET_ALL = "get-all"
        POST_ALL = "post-all"

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the ConnectAppInstance
        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'authorize_redirect_url': payload.get('authorize_redirect_url'),
            'company_name': payload.get('company_name'),
            'deauthorize_callback_method': payload.get('deauthorize_callback_method'),
            'deauthorize_callback_url': payload.get('deauthorize_callback_url'),
            'description': payload.get('description'),
            'friendly_name': payload.get('friendly_name'),
            'homepage_url': payload.get('homepage_url'),
            'permissions': payload.get('permissions'),
            'sid': payload.get('sid'),
            'uri': payload.get('uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ConnectAppContext for this ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        """
        if self._context is None:
            self._context = ConnectAppContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def authorize_redirect_url(self):
        """
        :returns: The URL we redirect the user to after we authenticate the user and obtain authorization to access the Connect App.
        :rtype: str
        """
        return self._properties['authorize_redirect_url']
    
    @property
    def company_name(self):
        """
        :returns: The company name set for the Connect App.
        :rtype: str
        """
        return self._properties['company_name']
    
    @property
    def deauthorize_callback_method(self):
        """
        :returns: The HTTP method we use to call `deauthorize_callback_url`.
        :rtype: str
        """
        return self._properties['deauthorize_callback_method']
    
    @property
    def deauthorize_callback_url(self):
        """
        :returns: The URL we call using the `deauthorize_callback_method` to de-authorize the Connect App.
        :rtype: str
        """
        return self._properties['deauthorize_callback_url']
    
    @property
    def description(self):
        """
        :returns: The description of the Connect App.
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def homepage_url(self):
        """
        :returns: The public URL where users can obtain more information about this Connect App.
        :rtype: str
        """
        return self._properties['homepage_url']
    
    @property
    def permissions(self):
        """
        :returns: The set of permissions that your ConnectApp requests.
        :rtype: list[ConnectAppPermission]
        """
        return self._properties['permissions']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the ConnectApp resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    def delete(self):
        """
        Deletes the ConnectAppInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ConnectAppInstance
        

        :returns: The fetched ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        return self._proxy.fetch()
    
    def update(self, authorize_redirect_url=values.unset, company_name=values.unset, deauthorize_callback_method=values.unset, deauthorize_callback_url=values.unset, description=values.unset, friendly_name=values.unset, homepage_url=values.unset, permissions=values.unset):
        """
        Update the ConnectAppInstance
        
        :params str authorize_redirect_url: The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App.
        :params str company_name: The company name to set for the Connect App.
        :params str deauthorize_callback_method: The HTTP method to use when calling `deauthorize_callback_url`.
        :params str deauthorize_callback_url: The URL to call using the `deauthorize_callback_method` to de-authorize the Connect App.
        :params str description: A description of the Connect App.
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str homepage_url: A public URL where users can obtain more information about this Connect App.
        :params list[ConnectAppPermission] permissions: A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: `get-all` and `post-all`.

        :returns: The updated ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        return self._proxy.update(authorize_redirect_url=authorize_redirect_url, company_name=company_name, deauthorize_callback_method=deauthorize_callback_method, deauthorize_callback_url=deauthorize_callback_url, description=description, friendly_name=friendly_name, homepage_url=homepage_url, permissions=permissions, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ConnectAppInstance {}>'.format(context)

class ConnectAppContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the ConnectAppContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ConnectApp resources to update.:param sid: The Twilio-provided string that uniquely identifies the ConnectApp resource to update.

        :returns: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/ConnectApps/{sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the ConnectAppInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ConnectAppInstance
        

        :returns: The fetched ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ConnectAppInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, authorize_redirect_url=values.unset, company_name=values.unset, deauthorize_callback_method=values.unset, deauthorize_callback_url=values.unset, description=values.unset, friendly_name=values.unset, homepage_url=values.unset, permissions=values.unset):
        """
        Update the ConnectAppInstance
        
        :params str authorize_redirect_url: The URL to redirect the user to after we authenticate the user and obtain authorization to access the Connect App.
        :params str company_name: The company name to set for the Connect App.
        :params str deauthorize_callback_method: The HTTP method to use when calling `deauthorize_callback_url`.
        :params str deauthorize_callback_url: The URL to call using the `deauthorize_callback_method` to de-authorize the Connect App.
        :params str description: A description of the Connect App.
        :params str friendly_name: A descriptive string that you create to describe the resource. It can be up to 64 characters long.
        :params str homepage_url: A public URL where users can obtain more information about this Connect App.
        :params list[ConnectAppPermission] permissions: A comma-separated list of the permissions you will request from the users of this ConnectApp.  Can include: `get-all` and `post-all`.

        :returns: The updated ConnectAppInstance
        :rtype: twilio.rest.api.v2010.account.connect_app.ConnectAppInstance
        """
        data = values.of({ 
            'AuthorizeRedirectUrl': authorize_redirect_url,
            'CompanyName': company_name,
            'DeauthorizeCallbackMethod': deauthorize_callback_method,
            'DeauthorizeCallbackUrl': deauthorize_callback_url,
            'Description': description,
            'FriendlyName': friendly_name,
            'HomepageUrl': homepage_url,
            'Permissions': serialize.map(permissions, lambda e: e),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ConnectAppInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.ConnectAppContext {}>'.format(context)


