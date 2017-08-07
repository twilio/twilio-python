# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base import serialize
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SyncMapItemTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_map_items(key="key").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "data": {},
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "key": "key",
                "map_sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key"
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_map_items(key="key").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_map_items(key="key").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_map_items(key="key").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_map_items.create(key="key", data="{}")

        values = {
            'Key': "key",
            'Data': serialize.object("{}"),
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "data": {},
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "key": "key",
                "map_sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key"
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_map_items.create(key="key", data="{}")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_map_items.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "items": [],
                "meta": {
                    "first_page_url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?PageSize=50&Page=0",
                    "key": "items",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_map_items.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "items": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "created_by": "created_by",
                        "data": {},
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "key": "key",
                        "map_sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "revision": "revision",
                        "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key"
                    }
                ],
                "meta": {
                    "first_page_url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?PageSize=50&Page=0",
                    "key": "items",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items?PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_map_items.list()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                    .sync_map_items(key="key").update(data="{}")

        values = {
            'Data': serialize.object("{}"),
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "created_by": "created_by",
                "data": {},
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "key": "key",
                "map_sid": "MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "revision": "revision",
                "service_sid": "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "url": "https://preview.twilio.com/Sync/Services/ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Maps/MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Items/key"
            }
            '''
        ))

        actual = self.client.preview.sync.services(sid="ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_maps(sid="MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                         .sync_map_items(key="key").update(data="{}")

        self.assertIsNotNone(actual)
