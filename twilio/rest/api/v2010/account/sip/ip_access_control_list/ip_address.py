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
from twilio.base.page import Page


class IpAddressList(ListResource):

    def __init__(self, version: Version, account_sid: str, ip_access_control_list_sid: str):
        """
        Initialize the IpAddressList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.
        :param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to read.
        
        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressList
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'ip_access_control_list_sid': ip_access_control_list_sid,  }
        self._uri = '/Accounts/${account_sid}/SIP/IpAccessControlLists/${ip_access_control_list_sid}/IpAddresses.json'.format(**self._solution)
        
        
    
    
    
    
    def create(self, friendly_name, ip_address, cidr_prefix_length=values.unset):
        """
        Create the IpAddressInstance
        :param str friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :param str ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :param int cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
        
        :returns: The created IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'IpAddress': ip_address,
            'CidrPrefixLength': cidr_prefix_length,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data)
        return IpAddressInstance(self._version, payload, account_sid=self._solution['account_sid'], ip_access_control_list_sid=self._solution['ip_access_control_list_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams IpAddressInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists IpAddressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of IpAddressInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return IpAddressPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of IpAddressInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return IpAddressPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a IpAddressContext
        
        :param sid: A 34 character string that identifies the IpAddress resource to update.
        
        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        """
        return IpAddressContext(self._version, account_sid=self._solution['account_sid'], ip_access_control_list_sid=self._solution['ip_access_control_list_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a IpAddressContext
        
        :param sid: A 34 character string that identifies the IpAddress resource to update.
        
        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        """
        return IpAddressContext(self._version, account_sid=self._solution['account_sid'], ip_access_control_list_sid=self._solution['ip_access_control_list_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAddressList>'










class IpAddressPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the IpAddressPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressPage
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IpAddressInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        return IpAddressInstance(self._version, payload, account_sid=self._solution['account_sid'], ip_access_control_list_sid=self._solution['ip_access_control_list_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAddressPage>'




class IpAddressContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, ip_access_control_list_sid: str, sid: str):
        """
        Initialize the IpAddressContext

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this resource.:param ip_access_control_list_sid: The IpAccessControlList Sid that identifies the IpAddress resources to update.:param sid: A 34 character string that identifies the IpAddress resource to update.

        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/${account_sid}/SIP/IpAccessControlLists/${ip_access_control_list_sid}/IpAddresses/${sid}.json'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the IpAddressInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri)
        
    def fetch(self):
        """
        Fetch the IpAddressInstance

        :returns: The fetched IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri)

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, ip_address=values.unset, friendly_name=values.unset, cidr_prefix_length=values.unset):
        """
        Update the IpAddressInstance
        
        :params str ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :params str friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :params int cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: The updated IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        data = values.of({ 
            'IpAddress': ip_address,
            'FriendlyName': friendly_name,
            'CidrPrefixLength': cidr_prefix_length,
        })

        payload = self._version.update(method='POST', uri=self._uri, data=data)

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IpAddressContext {}>'.format(context)

class IpAddressInstance(InstanceResource):

    def __init__(self, version, payload, account_sid: str, ip_access_control_list_sid: str, sid: str=None):
        """
        Initialize the IpAddressInstance
        :returns: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'ip_address': payload.get('ip_address'),
            'cidr_prefix_length': deserialize.integer(payload.get('cidr_prefix_length')),
            'ip_access_control_list_sid': payload.get('ip_access_control_list_sid'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'uri': payload.get('uri'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'ip_access_control_list_sid': ip_access_control_list_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: IpAddressContext for this IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressContext
        """
        if self._context is None:
            self._context = IpAddressContext(self._version, account_sid=self._solution['account_sid'], ip_access_control_list_sid=self._solution['ip_access_control_list_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account that is responsible for this resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: A human readable descriptive text for this resource, up to 255 characters long.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def ip_address(self):
        """
        :returns: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :rtype: str
        """
        return self._properties['ip_address']
    
    @property
    def cidr_prefix_length(self):
        """
        :returns: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.
        :rtype: int
        """
        return self._properties['cidr_prefix_length']
    
    @property
    def ip_access_control_list_sid(self):
        """
        :returns: The unique id of the IpAccessControlList resource that includes this resource.
        :rtype: str
        """
        return self._properties['ip_access_control_list_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date that this resource was created, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated, given as GMT in [RFC 2822](https://www.php.net/manual/en/class.datetime.php#datetime.constants.rfc2822) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def uri(self):
        """
        :returns: The URI for this resource, relative to `https://api.twilio.com`
        :rtype: str
        """
        return self._properties['uri']
    
    def delete(self):
        """
        Deletes the IpAddressInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the IpAddressInstance

        :returns: The fetched IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        return self._proxy.fetch()
    
    def update(self, ip_address=values.unset, friendly_name=values.unset, cidr_prefix_length=values.unset):
        """
        Update the IpAddressInstance
        
        :params str ip_address: An IP address in dotted decimal notation from which you want to accept traffic. Any SIP requests from this IP address will be allowed by Twilio. IPv4 only supported today.
        :params str friendly_name: A human readable descriptive text for this resource, up to 255 characters long.
        :params int cidr_prefix_length: An integer representing the length of the CIDR prefix to use with this IP address when accepting traffic. By default the entire IP address is used.

        :returns: The updated IpAddressInstance
        :rtype: twilio.rest.api.v2010.account.sip.ip_access_control_list.ip_address.IpAddressInstance
        """
        return self._proxy.update(ip_address=ip_address, friendly_name=friendly_name, cidr_prefix_length=cidr_prefix_length, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IpAddressInstance {}>'.format(context)


