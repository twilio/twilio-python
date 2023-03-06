"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Messaging
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


class UsAppToPersonList(ListResource):

    def __init__(self, version: Version, messaging_service_sid: str):
        """
        Initialize the UsAppToPersonList

        :param Version version: Version that contains the resource
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.
        
        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonList
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'messaging_service_sid': messaging_service_sid,  }
        self._uri = '/Services/{messaging_service_sid}/Compliance/Usa2p'.format(**self._solution)
        
        
    
    
    
    def create(self, brand_registration_sid, description, message_flow, message_samples, us_app_to_person_usecase, has_embedded_links, has_embedded_phone, opt_in_message=values.unset, opt_out_message=values.unset, help_message=values.unset, opt_in_keywords=values.unset, opt_out_keywords=values.unset, help_keywords=values.unset):
        """
        Create the UsAppToPersonInstance

        :param str brand_registration_sid: A2P Brand Registration SID
        :param str description: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
        :param str message_flow: Required for all Campaigns. Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
        :param list[str] message_samples: Message samples, at least 1 and up to 5 sample messages (at least 2 for sole proprietor), >=20 chars, <=1024 chars each.
        :param str us_app_to_person_usecase: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING..]
        :param bool has_embedded_links: Indicates that this SMS campaign will send messages that contain links.
        :param bool has_embedded_phone: Indicates that this SMS campaign will send messages that contain phone numbers.
        :param str opt_in_message: If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
        :param str opt_out_message: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
        :param str help_message: When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
        :param list[str] opt_in_keywords: If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
        :param list[str] opt_out_keywords: End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
        :param list[str] help_keywords: End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
        
        :returns: The created UsAppToPersonInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance
        """
        data = values.of({ 
            'BrandRegistrationSid': brand_registration_sid,
            'Description': description,
            'MessageFlow': message_flow,
            'MessageSamples': serialize.map(message_samples, lambda e: e),
            'UsAppToPersonUsecase': us_app_to_person_usecase,
            'HasEmbeddedLinks': has_embedded_links,
            'HasEmbeddedPhone': has_embedded_phone,
            'OptInMessage': opt_in_message,
            'OptOutMessage': opt_out_message,
            'HelpMessage': help_message,
            'OptInKeywords': serialize.map(opt_in_keywords, lambda e: e),
            'OptOutKeywords': serialize.map(opt_out_keywords, lambda e: e),
            'HelpKeywords': serialize.map(help_keywords, lambda e: e),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return UsAppToPersonInstance(self._version, payload, messaging_service_sid=self._solution['messaging_service_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams UsAppToPersonInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UsAppToPersonInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of UsAppToPersonInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UsAppToPersonInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return UsAppToPersonPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UsAppToPersonInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UsAppToPersonInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return UsAppToPersonPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a UsAppToPersonContext
        
        :param sid: The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.
        
        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonContext
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonContext
        """
        return UsAppToPersonContext(self._version, messaging_service_sid=self._solution['messaging_service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a UsAppToPersonContext
        
        :param sid: The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.
        
        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonContext
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonContext
        """
        return UsAppToPersonContext(self._version, messaging_service_sid=self._solution['messaging_service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UsAppToPersonList>'








class UsAppToPersonPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UsAppToPersonPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonPage
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UsAppToPersonInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance
        """
        return UsAppToPersonInstance(self._version, payload, messaging_service_sid=self._solution['messaging_service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.UsAppToPersonPage>'




class UsAppToPersonContext(InstanceContext):

    def __init__(self, version: Version, messaging_service_sid: str, sid: str):
        """
        Initialize the UsAppToPersonContext

        :param Version version: Version that contains the resource
        :param messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) to fetch the resource from.:param sid: The SID of the US A2P Compliance resource to fetch `QE2c6890da8086d771620e9b13fadeba0b`.

        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonContext
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'messaging_service_sid': messaging_service_sid,
            'sid': sid,
        }
        self._uri = '/Services/{messaging_service_sid}/Compliance/Usa2p/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the UsAppToPersonInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the UsAppToPersonInstance
        

        :returns: The fetched UsAppToPersonInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UsAppToPersonInstance(
            self._version,
            payload,
            messaging_service_sid=self._solution['messaging_service_sid'],
            sid=self._solution['sid'],
            
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.UsAppToPersonContext {}>'.format(context)

class UsAppToPersonInstance(InstanceResource):

    def __init__(self, version, payload, messaging_service_sid: str, sid: str=None):
        """
        Initialize the UsAppToPersonInstance
        :returns: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'brand_registration_sid': payload.get('brand_registration_sid'),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'description': payload.get('description'),
            'message_samples': payload.get('message_samples'),
            'us_app_to_person_usecase': payload.get('us_app_to_person_usecase'),
            'has_embedded_links': payload.get('has_embedded_links'),
            'has_embedded_phone': payload.get('has_embedded_phone'),
            'campaign_status': payload.get('campaign_status'),
            'campaign_id': payload.get('campaign_id'),
            'is_externally_registered': payload.get('is_externally_registered'),
            'rate_limits': payload.get('rate_limits'),
            'message_flow': payload.get('message_flow'),
            'opt_in_message': payload.get('opt_in_message'),
            'opt_out_message': payload.get('opt_out_message'),
            'help_message': payload.get('help_message'),
            'opt_in_keywords': payload.get('opt_in_keywords'),
            'opt_out_keywords': payload.get('opt_out_keywords'),
            'help_keywords': payload.get('help_keywords'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'mock': payload.get('mock'),
        }

        self._context = None
        self._solution = { 'messaging_service_sid': messaging_service_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: UsAppToPersonContext for this UsAppToPersonInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonContext
        """
        if self._context is None:
            self._context = UsAppToPersonContext(self._version, messaging_service_sid=self._solution['messaging_service_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that identifies a US A2P Compliance resource `QE2c6890da8086d771620e9b13fadeba0b`.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that the Campaign belongs to.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def brand_registration_sid(self):
        """
        :returns: The unique string to identify the A2P brand.
        :rtype: str
        """
        return self._properties['brand_registration_sid']
    
    @property
    def messaging_service_sid(self):
        """
        :returns: The SID of the [Messaging Service](https://www.twilio.com/docs/messaging/services/api) that the resource is associated with.
        :rtype: str
        """
        return self._properties['messaging_service_sid']
    
    @property
    def description(self):
        """
        :returns: A short description of what this SMS campaign does. Min length: 40 characters. Max length: 4096 characters.
        :rtype: str
        """
        return self._properties['description']
    
    @property
    def message_samples(self):
        """
        :returns: Message samples, at least 1 and up to 5 sample messages (at least 2 for starter/sole proprietor), >=20 chars, <=1024 chars each.
        :rtype: list[str]
        """
        return self._properties['message_samples']
    
    @property
    def us_app_to_person_usecase(self):
        """
        :returns: A2P Campaign Use Case. Examples: [ 2FA, EMERGENCY, MARKETING, STARTER...]. STARTER campaign use cases can only be created by STARTER Brands, and there can only be one STARTER campaign created per STARTER Brand.
        :rtype: str
        """
        return self._properties['us_app_to_person_usecase']
    
    @property
    def has_embedded_links(self):
        """
        :returns: Indicate that this SMS campaign will send messages that contain links.
        :rtype: bool
        """
        return self._properties['has_embedded_links']
    
    @property
    def has_embedded_phone(self):
        """
        :returns: Indicates that this SMS campaign will send messages that contain phone numbers.
        :rtype: bool
        """
        return self._properties['has_embedded_phone']
    
    @property
    def campaign_status(self):
        """
        :returns: Campaign status. Examples: IN_PROGRESS, VERIFIED, FAILED.
        :rtype: str
        """
        return self._properties['campaign_status']
    
    @property
    def campaign_id(self):
        """
        :returns: The Campaign Registry (TCR) Campaign ID.
        :rtype: str
        """
        return self._properties['campaign_id']
    
    @property
    def is_externally_registered(self):
        """
        :returns: Indicates whether the campaign was registered externally or not.
        :rtype: bool
        """
        return self._properties['is_externally_registered']
    
    @property
    def rate_limits(self):
        """
        :returns: Rate limit and/or classification set by each carrier, Ex. AT&T or T-Mobile.
        :rtype: dict
        """
        return self._properties['rate_limits']
    
    @property
    def message_flow(self):
        """
        :returns: Details around how a consumer opts-in to their campaign, therefore giving consent to receive their messages. If multiple opt-in methods can be used for the same campaign, they must all be listed. 40 character minimum. 2048 character maximum.
        :rtype: str
        """
        return self._properties['message_flow']
    
    @property
    def opt_in_message(self):
        """
        :returns: If end users can text in a keyword to start receiving messages from this campaign, the auto-reply messages sent to the end users must be provided. The opt-in response should include the Brand name, confirmation of opt-in enrollment to a recurring message campaign, how to get help, and clear description of how to opt-out. This field is required if end users can text in a keyword to start receiving messages from this campaign. 20 character minimum. 320 character maximum.
        :rtype: str
        """
        return self._properties['opt_in_message']
    
    @property
    def opt_out_message(self):
        """
        :returns: Upon receiving the opt-out keywords from the end users, Twilio customers are expected to send back an auto-generated response, which must provide acknowledgment of the opt-out request and confirmation that no further messages will be sent. It is also recommended that these opt-out messages include the brand name. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
        :rtype: str
        """
        return self._properties['opt_out_message']
    
    @property
    def help_message(self):
        """
        :returns: When customers receive the help keywords from their end users, Twilio customers are expected to send back an auto-generated response; this may include the brand name and additional support contact information. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). 20 character minimum. 320 character maximum.
        :rtype: str
        """
        return self._properties['help_message']
    
    @property
    def opt_in_keywords(self):
        """
        :returns: If end users can text in a keyword to start receiving messages from this campaign, those keywords must be provided. This field is required if end users can text in a keyword to start receiving messages from this campaign. Values must be alphanumeric. 255 character maximum.
        :rtype: list[str]
        """
        return self._properties['opt_in_keywords']
    
    @property
    def opt_out_keywords(self):
        """
        :returns: End users should be able to text in a keyword to stop receiving messages from this campaign. Those keywords must be provided. This field is required if managing opt out keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
        :rtype: list[str]
        """
        return self._properties['opt_out_keywords']
    
    @property
    def help_keywords(self):
        """
        :returns: End users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. This field is required if managing help keywords yourself (i.e. not using Twilio's Default or Advanced Opt Out features). Values must be alphanumeric. 255 character maximum.
        :rtype: list[str]
        """
        return self._properties['help_keywords']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the US App to Person resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def mock(self):
        """
        :returns: A boolean that specifies whether campaign is a mock or not. Mock campaigns will be automatically created if using a mock brand. Mock campaigns should only be used for testing purposes.
        :rtype: bool
        """
        return self._properties['mock']
    
    def delete(self):
        """
        Deletes the UsAppToPersonInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the UsAppToPersonInstance
        

        :returns: The fetched UsAppToPersonInstance
        :rtype: twilio.rest.messaging.v1.service.us_app_to_person.UsAppToPersonInstance
        """
        return self._proxy.fetch()
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.UsAppToPersonInstance {}>'.format(context)


