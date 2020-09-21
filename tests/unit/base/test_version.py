from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.page import Page
from twilio.http.response import Response


class TestPage(Page):
    def __init__(self, version, response, *_args, **_kwargs):
        super(TestPage, self).__init__(version, response)

    def get_instance(self, payload):
        return payload


class StreamTestCase(IntegrationTestCase):
    def setUp(self):
        super(StreamTestCase, self).setUp()

        self.holodeck.mock(Response(
            200,
            '''
            {
                "next_page_uri": "/2010-04-01/Accounts/AC123/Messages.json?Page=1",
                "messages": [{"body": "payload0"}, {"body": "payload1"}]
            }
            '''
        ), Request(url='https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json'))

        self.holodeck.mock(Response(
            200,
            '''
            {
                "next_page_uri": "/2010-04-01/Accounts/AC123/Messages.json?Page=2",
                "messages": [{"body": "payload2"}, {"body": "payload3"}]
            }
            '''
        ), Request(url='https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json?Page=1'))

        self.holodeck.mock(Response(
            200,
            '''
            {
                "next_page_uri": null,
                "messages": [{"body": "payload4"}]
            }
            '''
        ), Request(url='https://api.twilio.com/2010-04-01/Accounts/AC123/Messages.json?Page=2'))

        self.version = self.client.api.v2010
        self.response = self.version.page(method='GET', uri='/Accounts/AC123/Messages.json')
        self.page = TestPage(self.version, self.response)

    def test_stream(self):
        messages = list(self.version.stream(self.page))

        self.assertEqual(len(messages), 5)

    def test_stream_limit(self):
        messages = list(self.version.stream(self.page, limit=3))

        self.assertEqual(len(messages), 3)

    def test_stream_page_limit(self):
        messages = list(self.version.stream(self.page, page_limit=1))

        self.assertEqual(len(messages), 2)


class VersionTestCase(IntegrationTestCase):
    def test_fetch_redirect(self):
        self.holodeck.mock(Response(
            307,
            '{"redirect_to": "some_place"}'
        ), Request(url='https://messaging.twilio.com/v1/Deactivations'))
        response = self.client.messaging.v1.fetch(
            method='GET',
            uri='/Deactivations'
        )

        self.assertIsNotNone(response)
