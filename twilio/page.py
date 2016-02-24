import json
from twilio.exceptions import TwilioException


class Page(object):
    META_KEYS = {
        'end',
        'first_page_uri',
        'next_page_uri',
        'last_page_uri',
        'page',
        'page_size',
        'previous_page_uri',
        'total',
        'num_pages',
        'start',
        'uri'
    }

    def __init__(self, version, response):
        payload = self.process_response(response)

        self._version = version
        self._payload = payload
        self._solution = {}
        self._records = iter(self.load_page(payload))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        return self.get_instance(next(self._records))

    @classmethod
    def process_response(self, response):
        if response.status_code != 200:
            raise TwilioException('Unable to fetch page', response)

        return json.loads(response.content)

    def load_page(self, payload):
        if 'meta' in payload and 'key' in payload['meta']:
            return payload[payload['meta']['key']]
        else:
            keys = set(payload.keys())
            key = keys - self.META_KEYS
            if len(key) == 1:
                return payload[key.pop()]

        raise TwilioException('Page Records can not be deserialized')

    @property
    def previous_page_url(self):
        if 'meta' in self._payload and 'previous_page_url' in self._payload['meta']:
            return self._payload['meta']['previous_page_url']
        elif 'previous_page_uri' in self._payload and self._payload['previous_page_uri']:
            return self._version.domain.absolute_url(self._payload['previous_page_uri'])

        return None

    @property
    def next_page_url(self):
        if 'meta' in self._payload and 'next_page_url' in self._payload['meta']:
            return self._payload['meta']['next_page_url']
        elif 'next_page_uri' in self._payload and self._payload['next_page_uri']:
            return self._version.domain.absolute_url(self._payload['next_page_uri'])

        return None

    def get_instance(self, payload):
        raise TwilioException('Page.get_instance() must be implemented in the derived class')

    def next_page(self):
        if not self.next_page_url:
            return None

        response = self._version.domain.twilio.request('GET', self.next_page_url)
        cls = type(self)
        return cls(self._version, response, self._solution)

    def previous_page(self):
        if not self.previous_page_url:
            return None

        response = self._version.domain.twilio.request('GET', self.previous_page_url)
        cls = type(self)
        return cls(self._version, response, self._solution)

    def __repr__(self):
        return '<Page>'

