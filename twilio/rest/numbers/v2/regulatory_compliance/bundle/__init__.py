"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Numbers
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
from twilio.rest.numbers.v2.regulatory_compliance.bundle.bundle_copy import BundleCopyList
from twilio.rest.numbers.v2.regulatory_compliance.bundle.evaluation import EvaluationList
from twilio.rest.numbers.v2.regulatory_compliance.bundle.item_assignment import ItemAssignmentList
from twilio.rest.numbers.v2.regulatory_compliance.bundle.replace_items import ReplaceItemsList


class BundleList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the BundleList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/RegulatoryCompliance/Bundles'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the BundleInstance

        :returns: The fetched BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return BundleInstance(self._version, payload)
    
    
    def update(self, status=values.unset, status_callback=values.unset, friendly_name=values.unset, email=values.unset):
        """
        Update the BundleInstance

        :param Status status: 
        :param str status_callback: The URL we call to inform your application of status changes.
        :param str friendly_name: The string that you assigned to describe the resource.
        :param str email: The email address that will receive updates when the Bundle resource changes status.
        
        :returns: The created BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        data = values.of({ 
            'Status': status,
            'StatusCallback': status_callback,
            'FriendlyName': friendly_name,
            'Email': email,
        })
        
        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return BundleInstance(self._version, payload)
    
    
    def create(self, friendly_name, email, status_callback=values.unset, regulation_sid=values.unset, iso_country=values.unset, end_user_type=values.unset, number_type=values.unset):
        """
        Create the BundleInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param str email: The email address that will receive updates when the Bundle resource changes status.
        :param str status_callback: The URL we call to inform your application of status changes.
        :param str regulation_sid: The unique string of a regulation that is associated to the Bundle resource.
        :param str iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle's phone number country ownership request.
        :param EndUserType end_user_type: 
        :param str number_type: The type of phone number of the Bundle's ownership request. Can be `local`, `mobile`, `national`, or `toll free`.
        
        :returns: The created BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Email': email,
            'StatusCallback': status_callback,
            'RegulationSid': regulation_sid,
            'IsoCountry': iso_country,
            'EndUserType': end_user_type,
            'NumberType': number_type,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return BundleInstance(self._version, payload)
    
    
    def stream(self, status=values.unset, friendly_name=values.unset, regulation_sid=values.unset, iso_country=values.unset, number_type=values.unset, has_valid_until_date=values.unset, sort_by=values.unset, sort_direction=values.unset, valid_until_date=values.unset, valid_until_date_before=values.unset, valid_until_date_after=values.unset, limit=None, page_size=None):
        """
        Streams BundleInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param Status status: The verification status of the Bundle resource. Please refer to [Bundle Statuses](https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses) for more details.
        :param str friendly_name: The string that you assigned to describe the resource. The column can contain 255 variable characters.
        :param str regulation_sid: The unique string of a [Regulation resource](https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations) that is associated to the Bundle resource.
        :param str iso_country: The 2-digit [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle's phone number country ownership request.
        :param str number_type: The type of phone number of the Bundle's ownership request. Can be `local`, `mobile`, `national`, or `tollfree`.
        :param bool has_valid_until_date: Indicates that the Bundle is a valid Bundle until a specified expiration date.
        :param SortBy sort_by: Can be `valid-until` or `date-updated`. Defaults to `date-created`.
        :param SortDirection sort_direction: Default is `DESC`. Can be `ASC` or `DESC`.
        :param datetime valid_until_date: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param datetime valid_until_date_before: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param datetime valid_until_date_after: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            status=status,
            friendly_name=friendly_name,
            regulation_sid=regulation_sid,
            iso_country=iso_country,
            number_type=number_type,
            has_valid_until_date=has_valid_until_date,
            sort_by=sort_by,
            sort_direction=sort_direction,
            valid_until_date=valid_until_date,
            valid_until_date_before=valid_until_date_before,
            valid_until_date_after=valid_until_date_after,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, status=values.unset, friendly_name=values.unset, regulation_sid=values.unset, iso_country=values.unset, number_type=values.unset, has_valid_until_date=values.unset, sort_by=values.unset, sort_direction=values.unset, valid_until_date=values.unset, valid_until_date_before=values.unset, valid_until_date_after=values.unset, limit=None, page_size=None):
        """
        Lists BundleInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param Status status: The verification status of the Bundle resource. Please refer to [Bundle Statuses](https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses) for more details.
        :param str friendly_name: The string that you assigned to describe the resource. The column can contain 255 variable characters.
        :param str regulation_sid: The unique string of a [Regulation resource](https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations) that is associated to the Bundle resource.
        :param str iso_country: The 2-digit [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle's phone number country ownership request.
        :param str number_type: The type of phone number of the Bundle's ownership request. Can be `local`, `mobile`, `national`, or `tollfree`.
        :param bool has_valid_until_date: Indicates that the Bundle is a valid Bundle until a specified expiration date.
        :param SortBy sort_by: Can be `valid-until` or `date-updated`. Defaults to `date-created`.
        :param SortDirection sort_direction: Default is `DESC`. Can be `ASC` or `DESC`.
        :param datetime valid_until_date: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param datetime valid_until_date_before: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param datetime valid_until_date_after: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance]
        """
        return list(self.stream(
            status=status,
            friendly_name=friendly_name,
            regulation_sid=regulation_sid,
            iso_country=iso_country,
            number_type=number_type,
            has_valid_until_date=has_valid_until_date,
            sort_by=sort_by,
            sort_direction=sort_direction,
            valid_until_date=valid_until_date,
            valid_until_date_before=valid_until_date_before,
            valid_until_date_after=valid_until_date_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, friendly_name=values.unset, regulation_sid=values.unset, iso_country=values.unset, number_type=values.unset, has_valid_until_date=values.unset, sort_by=values.unset, sort_direction=values.unset, valid_until_date=values.unset, valid_until_date_before=values.unset, valid_until_date_after=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of BundleInstance records from the API.
        Request is executed immediately
        
        :param Status status: The verification status of the Bundle resource. Please refer to [Bundle Statuses](https://www.twilio.com/docs/phone-numbers/regulatory/api/bundles#bundle-statuses) for more details.
        :param str friendly_name: The string that you assigned to describe the resource. The column can contain 255 variable characters.
        :param str regulation_sid: The unique string of a [Regulation resource](https://www.twilio.com/docs/phone-numbers/regulatory/api/regulations) that is associated to the Bundle resource.
        :param str iso_country: The 2-digit [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Bundle's phone number country ownership request.
        :param str number_type: The type of phone number of the Bundle's ownership request. Can be `local`, `mobile`, `national`, or `tollfree`.
        :param bool has_valid_until_date: Indicates that the Bundle is a valid Bundle until a specified expiration date.
        :param SortBy sort_by: Can be `valid-until` or `date-updated`. Defaults to `date-created`.
        :param SortDirection sort_direction: Default is `DESC`. Can be `ASC` or `DESC`.
        :param datetime valid_until_date: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param datetime valid_until_date_before: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param datetime valid_until_date_after: Date to filter Bundles having their `valid_until_date` before or after the specified date. Can be `ValidUntilDate>=` or `ValidUntilDate<=`. Both can be used in conjunction as well. [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) is the acceptable date format.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundlePage
        """
        data = values.of({ 
            'Status': status,
            'FriendlyName': friendly_name,
            'RegulationSid': regulation_sid,
            'IsoCountry': iso_country,
            'NumberType': number_type,
            'HasValidUntilDate': has_valid_until_date,
            'SortBy': sort_by,
            'SortDirection': sort_direction,
            'ValidUntilDate': serialize.iso8601_datetime(valid_until_date),
            'ValidUntilDate<': serialize.iso8601_datetime(valid_until_date_before),
            'ValidUntilDate>': serialize.iso8601_datetime(valid_until_date_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return BundlePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BundleInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundlePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return BundlePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a BundleContext
        
        :param sid: The unique string that we created to identify the Bundle resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleContext
        """
        return BundleContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a BundleContext
        
        :param sid: The unique string that we created to identify the Bundle resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleContext
        """
        return BundleContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.BundleList>'










class BundlePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the BundlePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundlePage
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundlePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BundleInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        return BundleInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.BundlePage>'




class BundleInstance(InstanceResource):

    class SortBy(object):
        VALID_UNTIL = "valid-until"
        DATE_UPDATED = "date-updated"

    class SortDirection(object):
        ASC = "ASC"
        DESC = "DESC"

    class Status(object):
        DRAFT = "draft"
        PENDING_REVIEW = "pending-review"
        IN_REVIEW = "in-review"
        TWILIO_REJECTED = "twilio-rejected"
        TWILIO_APPROVED = "twilio-approved"
        PROVISIONALLY_APPROVED = "provisionally-approved"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the BundleInstance
        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'regulation_sid': payload.get('regulation_sid'),
            'friendly_name': payload.get('friendly_name'),
            'status': payload.get('status'),
            'valid_until': deserialize.iso8601_datetime(payload.get('valid_until')),
            'email': payload.get('email'),
            'status_callback': payload.get('status_callback'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
            'links': payload.get('links'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: BundleContext for this BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleContext
        """
        if self._context is None:
            self._context = BundleContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the Bundle resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Bundle resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def regulation_sid(self):
        """
        :returns: The unique string of a regulation that is associated to the Bundle resource.
        :rtype: str
        """
        return self._properties['regulation_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: Status
        """
        return self._properties['status']
    
    @property
    def valid_until(self):
        """
        :returns: The date and time in GMT in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format when the resource will be valid until.
        :rtype: datetime
        """
        return self._properties['valid_until']
    
    @property
    def email(self):
        """
        :returns: The email address that will receive updates when the Bundle resource changes status.
        :rtype: str
        """
        return self._properties['email']
    
    @property
    def status_callback(self):
        """
        :returns: The URL we call to inform your application of status changes.
        :rtype: str
        """
        return self._properties['status_callback']
    
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
        :returns: The absolute URL of the Bundle resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def links(self):
        """
        :returns: The URLs of the Assigned Items of the Bundle resource.
        :rtype: dict
        """
        return self._properties['links']
    
    def delete(self):
        """
        Deletes the BundleInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the BundleInstance
        

        :returns: The fetched BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        return self._proxy.fetch()
    
    def update(self, status=values.unset, status_callback=values.unset, friendly_name=values.unset, email=values.unset):
        """
        Update the BundleInstance
        
        :params Status status: 
        :params str status_callback: The URL we call to inform your application of status changes.
        :params str friendly_name: The string that you assigned to describe the resource.
        :params str email: The email address that will receive updates when the Bundle resource changes status.

        :returns: The updated BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        return self._proxy.update(status=status, status_callback=status_callback, friendly_name=friendly_name, email=email, )
    
    @property
    def bundle_copies(self):
        """
        Access the bundle_copies

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleCopyList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleCopyList
        """
        return self._proxy.bundle_copies
    
    @property
    def evaluations(self):
        """
        Access the evaluations

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.EvaluationList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.EvaluationList
        """
        return self._proxy.evaluations
    
    @property
    def item_assignments(self):
        """
        Access the item_assignments

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.ItemAssignmentList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.ItemAssignmentList
        """
        return self._proxy.item_assignments
    
    @property
    def replace_items(self):
        """
        Access the replace_items

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.ReplaceItemsList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.ReplaceItemsList
        """
        return self._proxy.replace_items
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.BundleInstance {}>'.format(context)

class BundleContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the BundleContext

        :param Version version: Version that contains the resource
        :param sid: The unique string that we created to identify the Bundle resource.

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/RegulatoryCompliance/Bundles/{sid}'.format(**self._solution)
        
        self._bundle_copies = None
        self._evaluations = None
        self._item_assignments = None
        self._replace_items = None
    
    def delete(self):
        """
        Deletes the BundleInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the BundleInstance
        

        :returns: The fetched BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BundleInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, status=values.unset, status_callback=values.unset, friendly_name=values.unset, email=values.unset):
        """
        Update the BundleInstance
        
        :params Status status: 
        :params str status_callback: The URL we call to inform your application of status changes.
        :params str friendly_name: The string that you assigned to describe the resource.
        :params str email: The email address that will receive updates when the Bundle resource changes status.

        :returns: The updated BundleInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleInstance
        """
        data = values.of({ 
            'Status': status,
            'StatusCallback': status_callback,
            'FriendlyName': friendly_name,
            'Email': email,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return BundleInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    @property
    def bundle_copies(self):
        """
        Access the bundle_copies

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleCopyList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.BundleCopyList
        """
        if self._bundle_copies is None:
            self._bundle_copies = BundleCopyList(self._version, self._solution['sid'],
            )
        return self._bundle_copies
    
    @property
    def evaluations(self):
        """
        Access the evaluations

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.EvaluationList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.EvaluationList
        """
        if self._evaluations is None:
            self._evaluations = EvaluationList(self._version, self._solution['sid'],
            )
        return self._evaluations
    
    @property
    def item_assignments(self):
        """
        Access the item_assignments

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.ItemAssignmentList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.ItemAssignmentList
        """
        if self._item_assignments is None:
            self._item_assignments = ItemAssignmentList(self._version, self._solution['sid'],
            )
        return self._item_assignments
    
    @property
    def replace_items(self):
        """
        Access the replace_items

        :returns: twilio.rest.numbers.v2.regulatory_compliance.bundle.ReplaceItemsList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.bundle.ReplaceItemsList
        """
        if self._replace_items is None:
            self._replace_items = ReplaceItemsList(self._version, self._solution['sid'],
            )
        return self._replace_items
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.BundleContext {}>'.format(context)


