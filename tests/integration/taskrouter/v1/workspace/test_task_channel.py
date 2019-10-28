# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class TaskChannelTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TaskChannels/TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-04-14T17:35:54Z",
                "date_updated": "2016-04-14T17:35:54Z",
                "friendly_name": "Default",
                "sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "default",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_optimized_routing": true,
                "links": {
                    "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_fetch_unique_name_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2016-04-14T17:35:54Z",
                "date_updated": "2016-04-14T17:35:54Z",
                "friendly_name": "Default",
                "sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "unique_name": "default",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_optimized_routing": false,
                "links": {
                    "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .task_channels.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TaskChannels',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "channels": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "2016-04-14T17:35:54Z",
                        "date_updated": "2016-04-14T17:35:54Z",
                        "friendly_name": "Default",
                        "sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "unique_name": "default",
                        "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_optimized_routing": true,
                        "links": {
                            "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        }
                    }
                ],
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0",
                    "key": "channels",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "channels": [],
                "meta": {
                    "first_page_url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0",
                    "key": "channels",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TaskChannels/TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_update_sid_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Default",
                "unique_name": "default",
                "date_created": "2016-04-14T17:35:54Z",
                "date_updated": "2016-04-14T17:35:54Z",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_optimized_routing": true,
                "links": {
                    "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_update_unique_name_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Default",
                "unique_name": "default",
                "date_created": "2016-04-14T17:35:54Z",
                "date_updated": "2016-04-14T17:35:54Z",
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_optimized_routing": true,
                "links": {
                    "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TaskChannels/TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_sid_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_delete_unique_name_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels(sid="TCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .task_channels.create(friendly_name="friendly_name", unique_name="unique_name")

        values = {'FriendlyName': "friendly_name", 'UniqueName': "unique_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://taskrouter.twilio.com/v1/Workspaces/WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/TaskChannels',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "workspace_sid": "WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "Outbound Voice",
                "unique_name": "ovoice",
                "date_created": "2016-04-14T17:35:54Z",
                "date_updated": "2016-04-14T17:35:54Z",
                "channel_optimized_routing": true,
                "url": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/TaskChannels/TCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "workspace": "https://taskrouter.twilio.com/v1/Workspaces/WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.taskrouter.v1.workspaces(sid="WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .task_channels.create(friendly_name="friendly_name", unique_name="unique_name")

        self.assertIsNotNone(actual)
