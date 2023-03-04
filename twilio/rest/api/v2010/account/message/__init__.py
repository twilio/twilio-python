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
from twilio.rest.api.v2010.account.message.feedback import FeedbackList
from twilio.rest.api.v2010.account.message.media import MediaList


class MessageList(ListResource):

    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the MessageList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to read.
        
        :returns: twilio.rest.api.v2010.account.message.MessageList
        :rtype: twilio.rest.api.v2010.account.message.MessageList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/{account_sid}/Messages.json'.format(**self._solution)
        
        
    
    
    
    
    def create(self, to, status_callback=values.unset, application_sid=values.unset, max_price=values.unset, provide_feedback=values.unset, attempt=values.unset, validity_period=values.unset, force_delivery=values.unset, content_retention=values.unset, address_retention=values.unset, smart_encoded=values.unset, persistent_action=values.unset, shorten_urls=values.unset, schedule_type=values.unset, send_at=values.unset, send_as_mms=values.unset, content_sid=values.unset, content_variables=values.unset, from_=values.unset, messaging_service_sid=values.unset, body=values.unset, media_url=values.unset):
        """
        Create the MessageInstance

        :param str to: The destination phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format for SMS/MMS or [Channel user address](https://www.twilio.com/docs/sms/channels#channel-addresses) for other 3rd-party channels.
        :param str status_callback: The URL we should call using the `status_callback_method` to send status information to your application. If specified, we POST these message status changes to the URL: `queued`, `failed`, `sent`, `delivered`, or `undelivered`. Twilio will POST its [standard request parameters](https://www.twilio.com/docs/sms/twiml#request-parameters) as well as some additional parameters including `MessageSid`, `MessageStatus`, and `ErrorCode`. If you include this parameter with the `messaging_service_sid`, we use this URL instead of the Status Callback URL of the [Messaging Service](https://www.twilio.com/docs/sms/services/api). URLs must contain a valid hostname and underscores are not allowed.
        :param str application_sid: The SID of the application that should receive message status. We POST a `message_sid` parameter and a `message_status` parameter with a value of `sent` or `failed` to the [application](https://www.twilio.com/docs/usage/api/applications)'s `message_status_callback`. If a `status_callback` parameter is also passed, it will be ignored and the application's `message_status_callback` parameter will be used.
        :param float max_price: The maximum total price in US dollars that you will pay for the message to be delivered. Can be a decimal value that has up to 4 decimal places. All messages are queued for delivery and the message cost is checked before the message is sent. If the cost exceeds `max_price`, the message will fail and a status of `Failed` is sent to the status callback. If `MaxPrice` is not set, the message cost is not checked.
        :param bool provide_feedback: Whether to confirm delivery of the message. Set this value to `true` if you are sending messages that have a trackable user action and you intend to confirm delivery of the message using the [Message Feedback API](https://www.twilio.com/docs/sms/api/message-feedback-resource). This parameter is `false` by default.
        :param int attempt: Total number of attempts made ( including this ) to send out the message regardless of the provider used
        :param int validity_period: How long in seconds the message can remain in our outgoing message queue. After this period elapses, the message fails and we call your status callback. Can be between 1 and the default value of 14,400 seconds. After a message has been accepted by a carrier, however, we cannot guarantee that the message will not be queued after this period. We recommend that this value be at least 5 seconds.
        :param bool force_delivery: Reserved
        :param MessageContentRetention content_retention: 
        :param MessageAddressRetention address_retention: 
        :param bool smart_encoded: Whether to detect Unicode characters that have a similar GSM-7 character and replace them. Can be: `true` or `false`.
        :param list[str] persistent_action: Rich actions for Channels Messages.
        :param bool shorten_urls: Determines the usage of Click Tracking. Setting it to `true` will instruct Twilio to replace all links in the Message with a shortened version based on the associated Domain Sid and track clicks on them. If this parameter is not set on an API call, we will use the value set on the Messaging Service. If this parameter is not set and the value is not configured on the Messaging Service used this will default to `false`.
        :param MessageScheduleType schedule_type: 
        :param datetime send_at: The time that Twilio will send the message. Must be in ISO 8601 format.
        :param bool send_as_mms: If set to True, Twilio will deliver the message as a single MMS message, regardless of the presence of media.
        :param str content_sid: The SID of the Content object returned at Content API content create time (https://www.twilio.com/docs/content-api/create-and-send-your-first-content-api-template#create-a-template). If this parameter is not specified, then the Content API will not be utilized.
        :param str content_variables: Key-value pairs of variable names to substitution values, used alongside a content_sid. If not specified, Content API will default to the default variables defined at create time.
        :param str from_: A Twilio phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, an [alphanumeric sender ID](https://www.twilio.com/docs/sms/send-messages#use-an-alphanumeric-sender-id), or a [Channel Endpoint address](https://www.twilio.com/docs/sms/channels#channel-addresses) that is enabled for the type of message you want to send. Phone numbers or [short codes](https://www.twilio.com/docs/sms/api/short-code) purchased from Twilio also work here. You cannot, for example, spoof messages from a private cell phone number. If you are using `messaging_service_sid`, this parameter must be empty.
        :param str messaging_service_sid: The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services#send-a-message-with-copilot) you want to associate with the Message. Set this parameter to use the [Messaging Service Settings and Copilot Features](https://www.twilio.com/console/sms/services) you have configured and leave the `from` parameter empty. When only this parameter is set, Twilio will use your enabled Copilot Features to select the `from` phone number for delivery.
        :param str body: The text of the message you want to send. Can be up to 1,600 characters in length.
        :param list[str] media_url: The URL of the media to send with the message. The media can be of type `gif`, `png`, and `jpeg` and will be formatted correctly on the recipient's device. The media size limit is 5MB for supported file types (JPEG, PNG, GIF) and 500KB for [other types](https://www.twilio.com/docs/sms/accepted-mime-types) of accepted media. To send more than one image in the message body, provide multiple `media_url` parameters in the POST request. You can include up to 10 `media_url` parameters per message. You can send images in an SMS message in only the US and Canada.
        
        :returns: The created MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        data = values.of({ 
            'To': to,
            'StatusCallback': status_callback,
            'ApplicationSid': application_sid,
            'MaxPrice': max_price,
            'ProvideFeedback': provide_feedback,
            'Attempt': attempt,
            'ValidityPeriod': validity_period,
            'ForceDelivery': force_delivery,
            'ContentRetention': content_retention,
            'AddressRetention': address_retention,
            'SmartEncoded': smart_encoded,
            'PersistentAction': serialize.map(persistent_action, lambda e: e),
            'ShortenUrls': shorten_urls,
            'ScheduleType': schedule_type,
            'SendAt': serialize.iso8601_datetime(send_at),
            'SendAsMms': send_as_mms,
            'ContentSid': content_sid,
            'ContentVariables': content_variables,
            'From': from_,
            'MessagingServiceSid': messaging_service_sid,
            'Body': body,
            'MediaUrl': serialize.map(media_url, lambda e: e),
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return MessageInstance(self._version, payload, account_sid=self._solution['account_sid'])
    
    
    def stream(self, to=values.unset, from_=values.unset, date_sent=values.unset, date_sent_before=values.unset, date_sent_after=values.unset, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str to: Read messages sent to only this phone number.
        :param str from_: Read messages sent from only this phone number or alphanumeric sender ID.
        :param datetime date_sent: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param datetime date_sent_before: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param datetime date_sent_after: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.message.MessageInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            to=to,
            from_=from_,
            date_sent=date_sent,
            date_sent_before=date_sent_before,
            date_sent_after=date_sent_after,
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, to=values.unset, from_=values.unset, date_sent=values.unset, date_sent_before=values.unset, date_sent_after=values.unset, limit=None, page_size=None):
        """
        Lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str to: Read messages sent to only this phone number.
        :param str from_: Read messages sent from only this phone number or alphanumeric sender ID.
        :param datetime date_sent: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param datetime date_sent_before: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param datetime date_sent_after: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.message.MessageInstance]
        """
        return list(self.stream(
            to=to,
            from_=from_,
            date_sent=date_sent,
            date_sent_before=date_sent_before,
            date_sent_after=date_sent_after,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, to=values.unset, from_=values.unset, date_sent=values.unset, date_sent_before=values.unset, date_sent_after=values.unset, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately
        
        :param str to: Read messages sent to only this phone number.
        :param str from_: Read messages sent from only this phone number or alphanumeric sender ID.
        :param datetime date_sent: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param datetime date_sent_before: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param datetime date_sent_after: The date of the messages to show. Specify a date as `YYYY-MM-DD` in GMT to read only messages sent on this date. For example: `2009-07-06`. You can also specify an inequality, such as `DateSent<=YYYY-MM-DD`, to read messages sent on or before midnight on a date, and `DateSent>=YYYY-MM-DD` to read messages sent on or after midnight on a date.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessagePage
        """
        data = values.of({ 
            'To': to,
            'From': from_,
            'DateSent': serialize.iso8601_datetime(date_sent),
            'DateSent<': serialize.iso8601_datetime(date_sent_before),
            'DateSent>': serialize.iso8601_datetime(date_sent_after),
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return MessagePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessagePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return MessagePage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Message resource to update.
        
        :returns: twilio.rest.api.v2010.account.message.MessageContext
        :rtype: twilio.rest.api.v2010.account.message.MessageContext
        """
        return MessageContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a MessageContext
        
        :param sid: The Twilio-provided string that uniquely identifies the Message resource to update.
        
        :returns: twilio.rest.api.v2010.account.message.MessageContext
        :rtype: twilio.rest.api.v2010.account.message.MessageContext
        """
        return MessageContext(self._version, account_sid=self._solution['account_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MessageList>'










class MessagePage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the MessagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.api.v2010.account.message.MessagePage
        :rtype: twilio.rest.api.v2010.account.message.MessagePage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.message.MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        return MessageInstance(self._version, payload, account_sid=self._solution['account_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MessagePage>'




class MessageInstance(InstanceResource):

    class MessageDirection(object):
        INBOUND = "inbound"
        OUTBOUND_API = "outbound-api"
        OUTBOUND_CALL = "outbound-call"
        OUTBOUND_REPLY = "outbound-reply"

    class MessageStatus(object):
        QUEUED = "queued"
        SENDING = "sending"
        SENT = "sent"
        FAILED = "failed"
        DELIVERED = "delivered"
        UNDELIVERED = "undelivered"
        RECEIVING = "receiving"
        RECEIVED = "received"
        ACCEPTED = "accepted"
        SCHEDULED = "scheduled"
        READ = "read"
        PARTIALLY_DELIVERED = "partially_delivered"
        CANCELED = "canceled"

    def __init__(self, version, payload, account_sid: str, sid: str=None):
        """
        Initialize the MessageInstance
        :returns: twilio.rest.api.v2010.account.message.MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        super().__init__(version)

        self._properties = { 
            'body': payload.get('body'),
            'num_segments': payload.get('num_segments'),
            'direction': payload.get('direction'),
            '_from': payload.get('from'),
            'to': payload.get('to'),
            'date_updated': deserialize.rfc2822_datetime(payload.get('date_updated')),
            'price': payload.get('price'),
            'error_message': payload.get('error_message'),
            'uri': payload.get('uri'),
            'account_sid': payload.get('account_sid'),
            'num_media': payload.get('num_media'),
            'status': payload.get('status'),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'sid': payload.get('sid'),
            'date_sent': deserialize.rfc2822_datetime(payload.get('date_sent')),
            'date_created': deserialize.rfc2822_datetime(payload.get('date_created')),
            'error_code': deserialize.integer(payload.get('error_code')),
            'price_unit': payload.get('price_unit'),
            'api_version': payload.get('api_version'),
            'subresource_uris': payload.get('subresource_uris'),
        }

        self._context = None
        self._solution = { 'account_sid': account_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: MessageContext for this MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageContext
        """
        if self._context is None:
            self._context = MessageContext(self._version, account_sid=self._solution['account_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def body(self):
        """
        :returns: The message text. Can be up to 1,600 characters long.
        :rtype: str
        """
        return self._properties['body']
    
    @property
    def num_segments(self):
        """
        :returns: The number of segments that make up the complete message. A message body that is too large to be sent in a single SMS message is segmented and charged as multiple messages. Inbound messages over 160 characters are reassembled when the message is received. Note: When using a Messaging Service to send messages, `num_segments` will always be 0 in Twilio's response to your API request.
        :rtype: str
        """
        return self._properties['num_segments']
    
    @property
    def direction(self):
        """
        :returns: 
        :rtype: MessageDirection
        """
        return self._properties['direction']
    
    @property
    def _from(self):
        """
        :returns: The phone number (in [E.164](https://en.wikipedia.org/wiki/E.164) format), [alphanumeric sender ID](https://www.twilio.com/docs/sms/send-messages#use-an-alphanumeric-sender-id), or [Wireless SIM](https://www.twilio.com/docs/wireless/tutorials/communications-guides/how-to-send-and-receive-text-messages) that initiated the message. For incoming messages, this will be the number of the sending phone. For outgoing messages, this value will be one of your Twilio phone numbers or the alphanumeric sender ID used.
        :rtype: str
        """
        return self._properties['_from']
    
    @property
    def to(self):
        """
        :returns: The phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format that received the message. For incoming messages, this will be one of your Twilio phone numbers. For outgoing messages, this will be the sending phone.
        :rtype: str
        """
        return self._properties['to']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def price(self):
        """
        :returns: The amount billed for the message, in the currency specified by `price_unit`.  Note that your account is charged for each segment we send to the handset. Populated after the message has been sent. May not be immediately available.
        :rtype: str
        """
        return self._properties['price']
    
    @property
    def error_message(self):
        """
        :returns: The description of the `error_code` if your message `status` is `failed` or `undelivered`. If the message was successful, this value is null.
        :rtype: str
        """
        return self._properties['error_message']
    
    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`.
        :rtype: str
        """
        return self._properties['uri']
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that sent the message that created the resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def num_media(self):
        """
        :returns: The number of media files associated with the message. A message can send up to 10 media files.
        :rtype: str
        """
        return self._properties['num_media']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: MessageStatus
        """
        return self._properties['status']
    
    @property
    def messaging_service_sid(self):
        """
        :returns: The SID of the [Messaging Service](https://www.twilio.com/docs/sms/services/api) used with the message. The value is null if a Messaging Service was not used.
        :rtype: str
        """
        return self._properties['messaging_service_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that that we created to identify the Message resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def date_sent(self):
        """
        :returns: The date and time in GMT that the resource was sent specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. For outgoing messages, this is when we sent the message. For incoming messages, this is when we made the HTTP request to your application. 
        :rtype: datetime
        """
        return self._properties['date_sent']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def error_code(self):
        """
        :returns: The error code returned if your message `status` is `failed` or `undelivered`. The error_code provides more information about the failure. If the message was successful, this value is null.
        :rtype: int
        """
        return self._properties['error_code']
    
    @property
    def price_unit(self):
        """
        :returns: The currency in which `price` is measured, in [ISO 4127](https://www.iso.org/iso/home/standards/currency_codes.htm) format (e.g. `usd`, `eur`, `jpy`).
        :rtype: str
        """
        return self._properties['price_unit']
    
    @property
    def api_version(self):
        """
        :returns: The API version used to process the message.
        :rtype: str
        """
        return self._properties['api_version']
    
    @property
    def subresource_uris(self):
        """
        :returns: A list of related resources identified by their URIs relative to `https://api.twilio.com`
        :rtype: dict
        """
        return self._properties['subresource_uris']
    
    def delete(self):
        """
        Deletes the MessageInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the MessageInstance
        

        :returns: The fetched MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        return self._proxy.fetch()
    
    def update(self, body=values.unset, status=values.unset):
        """
        Update the MessageInstance
        
        :params str body: The text of the message you want to send. Can be up to 1,600 characters long.
        :params MessageUpdateStatus status: 

        :returns: The updated MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        return self._proxy.update(body=body, status=status, )
    
    @property
    def feedback(self):
        """
        Access the feedback

        :returns: twilio.rest.api.v2010.account.message.FeedbackList
        :rtype: twilio.rest.api.v2010.account.message.FeedbackList
        """
        return self._proxy.feedback
    
    @property
    def media(self):
        """
        Access the media

        :returns: twilio.rest.api.v2010.account.message.MediaList
        :rtype: twilio.rest.api.v2010.account.message.MediaList
        """
        return self._proxy.media
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.MessageInstance {}>'.format(context)

class MessageContext(InstanceContext):

    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the MessageContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Message resources to update.:param sid: The Twilio-provided string that uniquely identifies the Message resource to update.

        :returns: twilio.rest.api.v2010.account.message.MessageContext
        :rtype: twilio.rest.api.v2010.account.message.MessageContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/Messages/{sid}.json'.format(**self._solution)
        
        self._feedback = None
        self._media = None
    
    def delete(self):
        """
        Deletes the MessageInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the MessageInstance
        

        :returns: The fetched MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return MessageInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, body=values.unset, status=values.unset):
        """
        Update the MessageInstance
        
        :params str body: The text of the message you want to send. Can be up to 1,600 characters long.
        :params MessageUpdateStatus status: 

        :returns: The updated MessageInstance
        :rtype: twilio.rest.api.v2010.account.message.MessageInstance
        """
        data = values.of({ 
            'Body': body,
            'Status': status,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return MessageInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid']
        )
        
    
    @property
    def feedback(self):
        """
        Access the feedback

        :returns: twilio.rest.api.v2010.account.message.FeedbackList
        :rtype: twilio.rest.api.v2010.account.message.FeedbackList
        """
        if self._feedback is None:
            self._feedback = FeedbackList(self._version, self._solution['account_sid'], self._solution['sid'],
            )
        return self._feedback
    
    @property
    def media(self):
        """
        Access the media

        :returns: twilio.rest.api.v2010.account.message.MediaList
        :rtype: twilio.rest.api.v2010.account.message.MediaList
        """
        if self._media is None:
            self._media = MediaList(self._version, self._solution['account_sid'], self._solution['sid'],
            )
        return self._media
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.MessageContext {}>'.format(context)


