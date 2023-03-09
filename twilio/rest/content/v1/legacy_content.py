r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Content
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import date
from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class LegacyContentList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the LegacyContentList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.content.v1.legacy_content.LegacyContentList
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/LegacyContent'.format(**self._solution)
        
        
    
    def stream(self, limit=None, page_size=None):
        """
        Streams LegacyContentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.content.v1.legacy_content.LegacyContentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    async def stream_async(self, limit=None, page_size=None):
        """
        Asynchronously streams LegacyContentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.content.v1.legacy_content.LegacyContentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            page_size=limits['page_size']
        )

        return await self._version.stream_async(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists LegacyContentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.content.v1.legacy_content.LegacyContentInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    async def list_async(self, limit=None, page_size=None):
        """
        Asynchronously lists LegacyContentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.content.v1.legacy_content.LegacyContentInstance]
        """
        return list(await self.stream_async(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of LegacyContentInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of LegacyContentInstance
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return LegacyContentPage(self._version, response, self._solution)

    async def page_async(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Asynchronously retrieve a single page of LegacyContentInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of LegacyContentInstance
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = await self._version.page_async(method='GET', uri=self._uri, params=data)
        return LegacyContentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of LegacyContentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of LegacyContentInstance
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return LegacyContentPage(self._version, response, self._solution)

    async def get_page_async(self, target_url):
        """
        Asynchronously retrieve a specific page of LegacyContentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of LegacyContentInstance
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentPage
        """
        response = await self._version.domain.twilio.request_async(
            'GET',
            target_url
        )
        return LegacyContentPage(self._version, response, self._solution)



    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Content.V1.LegacyContentList>'


class LegacyContentPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the LegacyContentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.content.v1.legacy_content.LegacyContentPage
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of LegacyContentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.content.v1.legacy_content.LegacyContentInstance
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentInstance
        """
        return LegacyContentInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Content.V1.LegacyContentPage>'




class LegacyContentInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the LegacyContentInstance
        :returns: twilio.rest.content.v1.legacy_content.LegacyContentInstance
        :rtype: twilio.rest.content.v1.legacy_content.LegacyContentInstance
        """
        super().__init__(version)

        self._properties = { 
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'language': payload.get('language'),
            'variables': payload.get('variables'),
            'types': payload.get('types'),
            'legacy_template_name': payload.get('legacy_template_name'),
            'legacy_body': payload.get('legacy_body'),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = {  }
    
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Content resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/usage/api/account) that created Content resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: A string name used to describe the Content resource. Not visible to the end recipient.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def language(self):
        """
        :returns: Two-letter (ISO 639-1) language code (e.g., en) identifying the language the Content resource is in.
        :rtype: str
        """
        return self._properties['language']
    
    @property
    def variables(self):
        """
        :returns: Defines the default placeholder values for variables included in the Content resource. e.g. {\"1\": \"Customer_Name\"}.
        :rtype: dict
        """
        return self._properties['variables']
    
    @property
    def types(self):
        """
        :returns: The [Content types](https://www.twilio.com/docs/content-api/content-types-overview) (e.g. twilio/text) for this Content resource.
        :rtype: dict
        """
        return self._properties['types']
    
    @property
    def legacy_template_name(self):
        """
        :returns: The string name of the legacy content template associated with this Content resource, unique across all template names for its account.  Only lowercase letters, numbers and underscores are allowed
        :rtype: str
        """
        return self._properties['legacy_template_name']
    
    @property
    def legacy_body(self):
        """
        :returns: The string body field of the legacy content template associated with this Content resource
        :rtype: str
        """
        return self._properties['legacy_body']
    
    @property
    def url(self):
        """
        :returns: The URL of the resource, relative to `https://content.twilio.com`.
        :rtype: str
        """
        return self._properties['url']
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Content.V1.LegacyContentInstance {}>'.format(context)



