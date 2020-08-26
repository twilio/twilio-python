# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class TranscriptionList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the TranscriptionList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionList
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionList
        """
        super(TranscriptionList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/Transcriptions.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams TranscriptionInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.api.v2010.account.transcription.TranscriptionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists TranscriptionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.transcription.TranscriptionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of TranscriptionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return TranscriptionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of TranscriptionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return TranscriptionPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a TranscriptionContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        """
        return TranscriptionContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a TranscriptionContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        """
        return TranscriptionContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TranscriptionList>'


class TranscriptionPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the TranscriptionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionPage
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionPage
        """
        super(TranscriptionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TranscriptionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        return TranscriptionInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.TranscriptionPage>'


class TranscriptionContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, sid):
        """
        Initialize the TranscriptionContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource to fetch
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        """
        super(TranscriptionContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/Transcriptions/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch the TranscriptionInstance

        :returns: The fetched TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return TranscriptionInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the TranscriptionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.TranscriptionContext {}>'.format(context)


class TranscriptionInstance(InstanceResource):
    """  """

    class Status(object):
        IN_PROGRESS = "in-progress"
        COMPLETED = "completed"
        FAILED = "failed"

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the TranscriptionInstance

        :returns: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        super(TranscriptionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload.get('account_sid'),
            'api_version': payload.get('api_version'),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'duration': payload.get('duration'),
            'price': deserialize.decimal(payload.get('price')),
            'price_unit': payload.get('price_unit'),
            'recording_sid': payload.get('recording_sid'),
            'sid': payload.get('sid'),
            'status': payload.get('status'),
            'transcription_text': payload.get('transcription_text'),
            'type': payload.get('type'),
            'uri': payload.get('uri'),
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: TranscriptionContext for this TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionContext
        """
        if self._context is None:
            self._context = TranscriptionContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """
        :returns: The API version used to create the transcription
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def duration(self):
        """
        :returns: The duration of the transcribed audio in seconds.
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def price(self):
        """
        :returns: The charge for the transcription
        :rtype: unicode
        """
        return self._properties['price']

    @property
    def price_unit(self):
        """
        :returns: The currency in which price is measured
        :rtype: unicode
        """
        return self._properties['price_unit']

    @property
    def recording_sid(self):
        """
        :returns: The SID that identifies the transcription's recording
        :rtype: unicode
        """
        return self._properties['recording_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: The status of the transcription
        :rtype: TranscriptionInstance.Status
        """
        return self._properties['status']

    @property
    def transcription_text(self):
        """
        :returns: The text content of the transcription.
        :rtype: unicode
        """
        return self._properties['transcription_text']

    @property
    def type(self):
        """
        :returns: The transcription type
        :rtype: unicode
        """
        return self._properties['type']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch the TranscriptionInstance

        :returns: The fetched TranscriptionInstance
        :rtype: twilio.rest.api.v2010.account.transcription.TranscriptionInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the TranscriptionInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.TranscriptionInstance {}>'.format(context)
