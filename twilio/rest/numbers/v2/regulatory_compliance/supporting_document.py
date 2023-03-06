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


class SupportingDocumentList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the SupportingDocumentList

        :param Version version: Version that contains the resource
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentList
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentList
        """
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/RegulatoryCompliance/SupportingDocuments'.format(**self._solution)
        
        
    
    
    def fetch(self):
        """
        Fetch the SupportingDocumentInstance

        :returns: The fetched SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        payload = self._version.create(method='GET', uri=self._uri)

        return SupportingDocumentInstance(self._version, payload)
    
    
    def update(self, friendly_name=values.unset, attributes=values.unset):
        """
        Update the SupportingDocumentInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param object attributes: The set of parameters that are the attributes of the Supporting Document resource which are derived Supporting Document Types.
        
        :returns: The created SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Attributes': serialize.object(attributes),
        })
        
        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SupportingDocumentInstance(self._version, payload)
    
    
    def create(self, friendly_name, type, attributes=values.unset):
        """
        Create the SupportingDocumentInstance

        :param str friendly_name: The string that you assigned to describe the resource.
        :param str type: The type of the Supporting Document.
        :param object attributes: The set of parameters that are the attributes of the Supporting Documents resource which are derived Supporting Document Types.
        
        :returns: The created SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Type': type,
            'Attributes': serialize.object(attributes),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return SupportingDocumentInstance(self._version, payload)
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams SupportingDocumentInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SupportingDocumentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of SupportingDocumentInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return SupportingDocumentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SupportingDocumentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return SupportingDocumentPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a SupportingDocumentContext
        
        :param sid: The unique string created by Twilio to identify the Supporting Document resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentContext
        """
        return SupportingDocumentContext(self._version, sid=sid)

    def __call__(self, sid):
        """
        Constructs a SupportingDocumentContext
        
        :param sid: The unique string created by Twilio to identify the Supporting Document resource.
        
        :returns: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentContext
        """
        return SupportingDocumentContext(self._version, sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.SupportingDocumentList>'










class SupportingDocumentPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the SupportingDocumentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentPage
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SupportingDocumentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        return SupportingDocumentInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Numbers.V2.SupportingDocumentPage>'




class SupportingDocumentInstance(InstanceResource):

    class Status(object):
        DRAFT = "draft"
        PENDING_REVIEW = "pending-review"
        REJECTED = "rejected"
        APPROVED = "approved"
        EXPIRED = "expired"
        PROVISIONALLY_APPROVED = "provisionally-approved"

    def __init__(self, version, payload, sid: str=None):
        """
        Initialize the SupportingDocumentInstance
        :returns: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        super().__init__(version)

        self._properties = { 
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'friendly_name': payload.get('friendly_name'),
            'mime_type': payload.get('mime_type'),
            'status': payload.get('status'),
            'failure_reason': payload.get('failure_reason'),
            'type': payload.get('type'),
            'attributes': payload.get('attributes'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        self._context = None
        self._solution = { 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: SupportingDocumentContext for this SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentContext
        """
        if self._context is None:
            self._context = SupportingDocumentContext(self._version, sid=self._solution['sid'],)
        return self._context
    
    @property
    def sid(self):
        """
        :returns: The unique string created by Twilio to identify the Supporting Document resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Document resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource.
        :rtype: str
        """
        return self._properties['friendly_name']
    
    @property
    def mime_type(self):
        """
        :returns: The image type uploaded in the Supporting Document container.
        :rtype: str
        """
        return self._properties['mime_type']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: Status
        """
        return self._properties['status']
    
    @property
    def failure_reason(self):
        """
        :returns: The failure reason of the Supporting Document Resource.
        :rtype: str
        """
        return self._properties['failure_reason']
    
    @property
    def type(self):
        """
        :returns: The type of the Supporting Document.
        :rtype: str
        """
        return self._properties['type']
    
    @property
    def attributes(self):
        """
        :returns: The set of parameters that are the attributes of the Supporting Documents resource which are listed in the Supporting Document Types.
        :rtype: dict
        """
        return self._properties['attributes']
    
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
        :returns: The absolute URL of the Supporting Document resource.
        :rtype: str
        """
        return self._properties['url']
    
    def delete(self):
        """
        Deletes the SupportingDocumentInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the SupportingDocumentInstance
        

        :returns: The fetched SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        return self._proxy.fetch()
    
    def update(self, friendly_name=values.unset, attributes=values.unset):
        """
        Update the SupportingDocumentInstance
        
        :params str friendly_name: The string that you assigned to describe the resource.
        :params object attributes: The set of parameters that are the attributes of the Supporting Document resource which are derived Supporting Document Types.

        :returns: The updated SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        return self._proxy.update(friendly_name=friendly_name, attributes=attributes, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.SupportingDocumentInstance {}>'.format(context)

class SupportingDocumentContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the SupportingDocumentContext

        :param Version version: Version that contains the resource
        :param sid: The unique string created by Twilio to identify the Supporting Document resource.

        :returns: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentContext
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'sid': sid,
        }
        self._uri = '/RegulatoryCompliance/SupportingDocuments/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the SupportingDocumentInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the SupportingDocumentInstance
        

        :returns: The fetched SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return SupportingDocumentInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
            
        )
        
    def update(self, friendly_name=values.unset, attributes=values.unset):
        """
        Update the SupportingDocumentInstance
        
        :params str friendly_name: The string that you assigned to describe the resource.
        :params object attributes: The set of parameters that are the attributes of the Supporting Document resource which are derived Supporting Document Types.

        :returns: The updated SupportingDocumentInstance
        :rtype: twilio.rest.numbers.v2.regulatory_compliance.supporting_document.SupportingDocumentInstance
        """
        data = values.of({ 
            'FriendlyName': friendly_name,
            'Attributes': serialize.object(attributes),
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return SupportingDocumentInstance(
            self._version,
            payload,
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Numbers.V2.SupportingDocumentContext {}>'.format(context)


