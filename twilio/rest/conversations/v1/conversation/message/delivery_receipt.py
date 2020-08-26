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


class DeliveryReceiptList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, conversation_sid, message_sid):
        """
        Initialize the DeliveryReceiptList

        :param Version version: Version that contains the resource
        :param conversation_sid: The conversation_sid
        :param message_sid: The sid of the message the delivery receipt belongs to

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptList
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptList
        """
        super(DeliveryReceiptList, self).__init__(version)

        # Path Solution
        self._solution = {'conversation_sid': conversation_sid, 'message_sid': message_sid, }
        self._uri = '/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams DeliveryReceiptInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DeliveryReceiptInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of DeliveryReceiptInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return DeliveryReceiptPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeliveryReceiptInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return DeliveryReceiptPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a DeliveryReceiptContext

        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        """
        return DeliveryReceiptContext(
            self._version,
            conversation_sid=self._solution['conversation_sid'],
            message_sid=self._solution['message_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a DeliveryReceiptContext

        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        """
        return DeliveryReceiptContext(
            self._version,
            conversation_sid=self._solution['conversation_sid'],
            message_sid=self._solution['message_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.DeliveryReceiptList>'


class DeliveryReceiptPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the DeliveryReceiptPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param conversation_sid: The conversation_sid
        :param message_sid: The sid of the message the delivery receipt belongs to

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptPage
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptPage
        """
        super(DeliveryReceiptPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeliveryReceiptInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        """
        return DeliveryReceiptInstance(
            self._version,
            payload,
            conversation_sid=self._solution['conversation_sid'],
            message_sid=self._solution['message_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.DeliveryReceiptPage>'


class DeliveryReceiptContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, conversation_sid, message_sid, sid):
        """
        Initialize the DeliveryReceiptContext

        :param Version version: Version that contains the resource
        :param conversation_sid: The unique id of the Conversation for this delivery receipt.
        :param message_sid: The sid of the message the delivery receipt belongs to
        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        """
        super(DeliveryReceiptContext, self).__init__(version)

        # Path Solution
        self._solution = {'conversation_sid': conversation_sid, 'message_sid': message_sid, 'sid': sid, }
        self._uri = '/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the DeliveryReceiptInstance

        :returns: The fetched DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DeliveryReceiptInstance(
            self._version,
            payload,
            conversation_sid=self._solution['conversation_sid'],
            message_sid=self._solution['message_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.DeliveryReceiptContext {}>'.format(context)


class DeliveryReceiptInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class DeliveryStatus(object):
        READ = "read"
        FAILED = "failed"
        DELIVERED = "delivered"
        UNDELIVERED = "undelivered"
        SENT = "sent"

    def __init__(self, version, payload, conversation_sid, message_sid, sid=None):
        """
        Initialize the DeliveryReceiptInstance

        :returns: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        """
        super(DeliveryReceiptInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'message_sid': payload.get('message_sid'),
            'conversation_sid': payload.get('conversation_sid'),
            'channel_message_sid': payload.get('channel_message_sid'),
            'participant_sid': payload.get('participant_sid'),
            'status': payload.get('status'),
            'error_code': deserialize.integer(payload.get('error_code')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'conversation_sid': conversation_sid,
            'message_sid': message_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DeliveryReceiptContext for this DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptContext
        """
        if self._context is None:
            self._context = DeliveryReceiptContext(
                self._version,
                conversation_sid=self._solution['conversation_sid'],
                message_sid=self._solution['message_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def message_sid(self):
        """
        :returns: The sid of the message the delivery receipt belongs to
        :rtype: unicode
        """
        return self._properties['message_sid']

    @property
    def conversation_sid(self):
        """
        :returns: The conversation_sid
        :rtype: unicode
        """
        return self._properties['conversation_sid']

    @property
    def channel_message_sid(self):
        """
        :returns: A messaging channel-specific identifier for the message delivered to participant
        :rtype: unicode
        """
        return self._properties['channel_message_sid']

    @property
    def participant_sid(self):
        """
        :returns: The unique id of the participant the delivery receipt belongs to.
        :rtype: unicode
        """
        return self._properties['participant_sid']

    @property
    def status(self):
        """
        :returns: The message delivery status
        :rtype: DeliveryReceiptInstance.DeliveryStatus
        """
        return self._properties['status']

    @property
    def error_code(self):
        """
        :returns: The message .. _delivery error code https://www.twilio.com/docs/sms/api/message-resource#delivery-related-errors for a `failed` status
        :rtype: unicode
        """
        return self._properties['error_code']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: An absolute URL for this delivery receipt.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the DeliveryReceiptInstance

        :returns: The fetched DeliveryReceiptInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.delivery_receipt.DeliveryReceiptInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.DeliveryReceiptInstance {}>'.format(context)
