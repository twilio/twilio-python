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


class WebhookList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid):
        """
        Initialize the WebhookList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the Assistant that is the parent of the resource

        :returns: twilio.rest.autopilot.v1.assistant.webhook.WebhookList
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookList
        """
        super(WebhookList, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, }
        self._uri = '/Assistants/{assistant_sid}/Webhooks'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams WebhookInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists WebhookInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of WebhookInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return WebhookPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of WebhookInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return WebhookPage(self._version, response, self._solution)

    def create(self, unique_name, events, webhook_url, webhook_method=values.unset):
        """
        Create a new WebhookInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode events: The list of space-separated events that this Webhook will subscribe to.
        :param unicode webhook_url: The URL associated with this Webhook.
        :param unicode webhook_method: The method to be used when calling the webhook's URL.

        :returns: Newly created WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'Events': events,
            'WebhookUrl': webhook_url,
            'WebhookMethod': webhook_method,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return WebhookInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def get(self, sid):
        """
        Constructs a WebhookContext

        :param sid: The unique string that identifies the resource to fetch

        :returns: twilio.rest.autopilot.v1.assistant.webhook.WebhookContext
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookContext
        """
        return WebhookContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a WebhookContext

        :param sid: The unique string that identifies the resource to fetch

        :returns: twilio.rest.autopilot.v1.assistant.webhook.WebhookContext
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookContext
        """
        return WebhookContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.WebhookList>'


class WebhookPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the WebhookPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param assistant_sid: The SID of the Assistant that is the parent of the resource

        :returns: twilio.rest.autopilot.v1.assistant.webhook.WebhookPage
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookPage
        """
        super(WebhookPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of WebhookInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        """
        return WebhookInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.WebhookPage>'


class WebhookContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, sid):
        """
        Initialize the WebhookContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the Assistant that is the parent of the resource to fetch
        :param sid: The unique string that identifies the resource to fetch

        :returns: twilio.rest.autopilot.v1.assistant.webhook.WebhookContext
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookContext
        """
        super(WebhookContext, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid, }
        self._uri = '/Assistants/{assistant_sid}/Webhooks/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a WebhookInstance

        :returns: Fetched WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return WebhookInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def update(self, unique_name=values.unset, events=values.unset,
               webhook_url=values.unset, webhook_method=values.unset):
        """
        Update the WebhookInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode events: The list of space-separated events that this Webhook will subscribe to.
        :param unicode webhook_url: The URL associated with this Webhook.
        :param unicode webhook_method: The method to be used when calling the webhook's URL.

        :returns: Updated WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        """
        data = values.of({
            'UniqueName': unique_name,
            'Events': events,
            'WebhookUrl': webhook_url,
            'WebhookMethod': webhook_method,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return WebhookInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the WebhookInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.WebhookContext {}>'.format(context)


class WebhookInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, assistant_sid, sid=None):
        """
        Initialize the WebhookInstance

        :returns: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        """
        super(WebhookInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'url': payload.get('url'),
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'unique_name': payload.get('unique_name'),
            'events': payload.get('events'),
            'webhook_url': payload.get('webhook_url'),
            'webhook_method': payload.get('webhook_method'),
        }

        # Context
        self._context = None
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: WebhookContext for this WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookContext
        """
        if self._context is None:
            self._context = WebhookContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def url(self):
        """
        :returns: The absolute URL of the Webhook resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def assistant_sid(self):
        """
        :returns: The SID of the Assistant that is the parent of the resource
        :rtype: unicode
        """
        return self._properties['assistant_sid']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def events(self):
        """
        :returns: The list of space-separated events that this Webhook is subscribed to.
        :rtype: unicode
        """
        return self._properties['events']

    @property
    def webhook_url(self):
        """
        :returns: The URL associated with this Webhook.
        :rtype: unicode
        """
        return self._properties['webhook_url']

    @property
    def webhook_method(self):
        """
        :returns: The method used when calling the webhook's URL.
        :rtype: unicode
        """
        return self._properties['webhook_method']

    def fetch(self):
        """
        Fetch a WebhookInstance

        :returns: Fetched WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        """
        return self._proxy.fetch()

    def update(self, unique_name=values.unset, events=values.unset,
               webhook_url=values.unset, webhook_method=values.unset):
        """
        Update the WebhookInstance

        :param unicode unique_name: An application-defined string that uniquely identifies the resource
        :param unicode events: The list of space-separated events that this Webhook will subscribe to.
        :param unicode webhook_url: The URL associated with this Webhook.
        :param unicode webhook_method: The method to be used when calling the webhook's URL.

        :returns: Updated WebhookInstance
        :rtype: twilio.rest.autopilot.v1.assistant.webhook.WebhookInstance
        """
        return self._proxy.update(
            unique_name=unique_name,
            events=events,
            webhook_url=webhook_url,
            webhook_method=webhook_method,
        )

    def delete(self):
        """
        Deletes the WebhookInstance

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
        return '<Twilio.Autopilot.V1.WebhookInstance {}>'.format(context)
