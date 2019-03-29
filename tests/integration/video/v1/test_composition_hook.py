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


class CompositionHookTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.composition_hooks(sid="HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/CompositionHooks/HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "My composition hook",
                "enabled": true,
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:01:33Z",
                "sid": "HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "audio_sources": [
                    "user*"
                ],
                "audio_sources_excluded": [
                    "moderator*"
                ],
                "video_layout": {
                    "grid": {
                        "video_sources": [
                            "*"
                        ],
                        "video_sources_excluded": [
                            "moderator*"
                        ],
                        "reuse": "show_oldest",
                        "x_pos": 100,
                        "y_pos": 600,
                        "z_pos": 10,
                        "width": 0,
                        "height": 0,
                        "max_columns": 0,
                        "max_rows": 0,
                        "cells_excluded": []
                    },
                    "pip": {
                        "video_sources": [
                            "student*"
                        ],
                        "video_sources_excluded": [],
                        "reuse": "none",
                        "x_pos": 100,
                        "y_pos": 600,
                        "z_pos": 10,
                        "width": 0,
                        "height": 0,
                        "max_columns": 0,
                        "max_rows": 0,
                        "cells_excluded": []
                    }
                },
                "resolution": "1280x720",
                "format": "webm",
                "trim": true,
                "status_callback": "http://www.example.com",
                "status_callback_method": "POST",
                "url": "https://video.twilio.com/v1/CompositionHooks/HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.video.v1.composition_hooks(sid="HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.composition_hooks.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://video.twilio.com/v1/CompositionHooks',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "composition_hooks": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/CompositionHooks?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/CompositionHooks?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "composition_hooks"
                }
            }
            '''
        ))

        actual = self.client.video.v1.composition_hooks.list()

        self.assertIsNotNone(actual)

    def test_read_results_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "composition_hooks": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "My Special Hook1",
                        "enabled": true,
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:01:33Z",
                        "sid": "HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "audio_sources": [
                            "*"
                        ],
                        "audio_sources_excluded": [],
                        "video_layout": {
                            "grid": {
                                "video_sources": [
                                    "*"
                                ],
                                "video_sources_excluded": [
                                    "moderator*"
                                ],
                                "reuse": "show_oldest",
                                "x_pos": 100,
                                "y_pos": 600,
                                "z_pos": 10,
                                "width": 0,
                                "height": 0,
                                "max_columns": 0,
                                "max_rows": 0,
                                "cells_excluded": []
                            },
                            "pip": {
                                "video_sources": [
                                    "student*"
                                ],
                                "video_sources_excluded": [],
                                "reuse": "none",
                                "x_pos": 100,
                                "y_pos": 600,
                                "z_pos": 10,
                                "width": 0,
                                "height": 0,
                                "max_columns": 0,
                                "max_rows": 0,
                                "cells_excluded": []
                            }
                        },
                        "resolution": "1280x720",
                        "format": "webm",
                        "trim": true,
                        "status_callback": "http://www.example.com",
                        "status_callback_method": "POST",
                        "url": "https://video.twilio.com/v1/CompositionHooks/HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://video.twilio.com/v1/CompositionHooks?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://video.twilio.com/v1/CompositionHooks?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "composition_hooks"
                }
            }
            '''
        ))

        actual = self.client.video.v1.composition_hooks.list()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.composition_hooks(sid="HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://video.twilio.com/v1/CompositionHooks/HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.video.v1.composition_hooks(sid="HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.composition_hooks.create(friendly_name="friendly_name")

        values = {'FriendlyName': "friendly_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://video.twilio.com/v1/CompositionHooks',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "friendly_name": "My composition hook",
                "enabled": false,
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": null,
                "sid": "HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "audio_sources": [
                    "user*",
                    "moderator"
                ],
                "audio_sources_excluded": [
                    "admin"
                ],
                "video_layout": {
                    "custom": {
                        "video_sources": [
                            "user*"
                        ],
                        "video_sources_excluded": [
                            "moderator"
                        ],
                        "reuse": "show_oldest",
                        "x_pos": 100,
                        "y_pos": 600,
                        "z_pos": 10,
                        "width": 800,
                        "height": 0,
                        "max_columns": 0,
                        "max_rows": 0,
                        "cells_excluded": [
                            2,
                            3
                        ]
                    }
                },
                "trim": true,
                "format": "mp4",
                "resolution": "1280x720",
                "status_callback": "http://www.example.com",
                "status_callback_method": "POST",
                "url": "https://video.twilio.com/v1/CompositionHooks/HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.video.v1.composition_hooks.create(friendly_name="friendly_name")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.video.v1.composition_hooks(sid="HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(friendly_name="friendly_name")

        values = {'FriendlyName': "friendly_name", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://video.twilio.com/v1/CompositionHooks/HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
            data=values,
        ))

    def test_update_all_fields_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "friendly_name": "My composition hook",
                "enabled": true,
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "sid": "HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "audio_sources": [
                    "user*",
                    "moderator"
                ],
                "audio_sources_excluded": [
                    "admin"
                ],
                "video_layout": {
                    "custom": {
                        "video_sources": [
                            "user*"
                        ],
                        "video_sources_excluded": [
                            "moderator"
                        ],
                        "reuse": "show_oldest",
                        "x_pos": 100,
                        "y_pos": 600,
                        "z_pos": 10,
                        "width": 800,
                        "height": 0,
                        "max_columns": 0,
                        "max_rows": 0,
                        "cells_excluded": [
                            2,
                            3
                        ]
                    }
                },
                "trim": true,
                "format": "mp4",
                "resolution": "1280x720",
                "status_callback": "http://www.example.com",
                "status_callback_method": "POST",
                "url": "https://video.twilio.com/v1/CompositionHooks/HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.video.v1.composition_hooks(sid="HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(friendly_name="friendly_name")

        self.assertIsNotNone(actual)

    def test_update_with_defaults_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "friendly_name": "My composition hook",
                "enabled": true,
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "sid": "HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "audio_sources": [
                    "user*",
                    "moderator"
                ],
                "audio_sources_excluded": [
                    "admin"
                ],
                "video_layout": {},
                "trim": true,
                "format": "mp4",
                "resolution": "1280x720",
                "status_callback": null,
                "status_callback_method": "POST",
                "url": "https://video.twilio.com/v1/CompositionHooks/HKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.video.v1.composition_hooks(sid="HKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").update(friendly_name="friendly_name")

        self.assertIsNotNone(actual)
