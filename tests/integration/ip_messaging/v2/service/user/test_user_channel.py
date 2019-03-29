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


class UserChannelTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .users(sid="USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .user_channels.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://ip-messaging.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Users/USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "channels"
                },
                "channels": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "user_sid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "member_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "joined",
                        "last_consumed_message_index": 5,
                        "unread_messages_count": 5,
                        "notification_level": "default",
                        "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "channel": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                            "member": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .users(sid="USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .user_channels.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "channels"
                },
                "channels": []
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .users(sid="USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .user_channels.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .users(sid="USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .user_channels(channel_sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://ip-messaging.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Users/USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "user_sid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "member_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "joined",
                "last_consumed_message_index": 5,
                "unread_messages_count": 5,
                "notification_level": "default",
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "channel": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "member": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .users(sid="USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .user_channels(channel_sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .users(sid="USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                       .user_channels(channel_sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(notification_level="default")

        values = {'NotificationLevel': "default", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://ip-messaging.twilio.com/v2/Services/ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Users/USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Channels/CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_sid": "CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "user_sid": "USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "member_sid": "MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "joined",
                "last_consumed_message_index": 5,
                "unread_messages_count": 5,
                "notification_level": "muted",
                "url": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Users/USaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "channel": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "member": "https://chat.twilio.com/v2/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels/CHaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Members/MBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                }
            }
            '''
        ))

        actual = self.client.ip_messaging.v2.services(sid="ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .users(sid="USXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                            .user_channels(channel_sid="CHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(notification_level="default")

        self.assertIsNotNone(actual)
