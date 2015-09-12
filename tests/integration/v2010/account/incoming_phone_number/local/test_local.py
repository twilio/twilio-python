# coding=utf-8
"""
__  __                      __
\ \/ /___  __  ______  ____/ /_  ______  ___
 \  / __ \/ / / / __ \/ __  / / / / __ \/ _ \
 / / /_/ / /_/ / /_/ / /_/ / /_/ / / / /  __/
/_/\____/\__. /\____/\__._/\__. /_/ /_/\___/      version 0.0.1
        /____/            /____/
"""

import unittest
from datetime import datetime
from twilio.ext.holodeck import Holodeck
from twilio.rest.v2010.client import V2010Client
from twilio.rest.http import Response
from twilio.rest.resources.util import parse_iso_date


class LocalIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1&Page=0",
            "incoming_phone_numbers": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "address_requirements": "none",
                    "api_version": "2010-04-01",
                    "beta": null,
                    "capabilities": {
                        "mms": true,
                        "sms": false,
                        "voice": true
                    },
                    "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",
                    "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",
                    "friendly_name": "(808) 925-5327",
                    "phone_number": "+18089255327",
                    "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sms_application_sid": "",
                    "sms_fallback_method": "POST",
                    "sms_fallback_url": "",
                    "sms_method": "POST",
                    "sms_url": "",
                    "status_callback": "",
                    "status_callback_method": "POST",
                    "trunk_sid": null,
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "voice_application_sid": "",
                    "voice_caller_id_lookup": false,
                    "voice_fallback_method": "POST",
                    "voice_fallback_url": null,
                    "voice_method": "POST",
                    "voice_url": null
                }
            ],
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1&Page=2",
            "next_page_uri": null,
            "num_pages": 3,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 3,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .incoming_phone_numbers \
            .local.list(
                beta=True,
                friendly_name="friendly_name",
                phone_number="+987654321"
            )
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].address_requirements)
        self.assertEqual(u"none", instances[0].address_requirements)
        self.assertIsNotNone(instances[0].api_version)
        self.assertEqual(u"2010-04-01", instances[0].api_version)
        self.assertIsNone(instances[0].beta)
        self.assertIsNotNone(instances[0].date_created)
        self.assertEqual(parse_iso_date("Thu, 30 Jul 2015 23:19:04 +0000"), instances[0].date_created)
        self.assertIsNotNone(instances[0].date_updated)
        self.assertEqual(parse_iso_date("Thu, 30 Jul 2015 23:19:04 +0000"), instances[0].date_updated)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"(808) 925-5327", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].phone_number)
        self.assertEqual(u"+18089255327", instances[0].phone_number)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)
        self.assertIsNotNone(instances[0].sms_application_sid)
        self.assertEqual(u"", instances[0].sms_application_sid)
        self.assertIsNotNone(instances[0].sms_fallback_method)
        self.assertEqual(u"POST", instances[0].sms_fallback_method)
        self.assertIsNotNone(instances[0].sms_fallback_url)
        self.assertEqual(u"", instances[0].sms_fallback_url)
        self.assertIsNotNone(instances[0].sms_method)
        self.assertEqual(u"POST", instances[0].sms_method)
        self.assertIsNotNone(instances[0].sms_url)
        self.assertEqual(u"", instances[0].sms_url)
        self.assertIsNotNone(instances[0].status_callback)
        self.assertEqual(u"", instances[0].status_callback)
        self.assertIsNotNone(instances[0].status_callback_method)
        self.assertEqual(u"POST", instances[0].status_callback_method)
        self.assertIsNone(instances[0].trunk_sid)
        self.assertIsNotNone(instances[0].voice_application_sid)
        self.assertEqual(u"", instances[0].voice_application_sid)
        self.assertIsNotNone(instances[0].voice_caller_id_lookup)
        self.assertEqual(False, instances[0].voice_caller_id_lookup)
        self.assertIsNotNone(instances[0].voice_fallback_method)
        self.assertEqual(u"POST", instances[0].voice_fallback_method)
        self.assertIsNone(instances[0].voice_fallback_url)
        self.assertIsNotNone(instances[0].voice_method)
        self.assertEqual(u"POST", instances[0].voice_method)
        self.assertIsNone(instances[0].voice_url)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1&Page=0",
            "incoming_phone_numbers": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "address_requirements": "none",
                    "api_version": "2010-04-01",
                    "beta": null,
                    "capabilities": {
                        "mms": true,
                        "sms": false,
                        "voice": true
                    },
                    "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",
                    "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",
                    "friendly_name": "(808) 925-5327",
                    "phone_number": "+18089255327",
                    "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "sms_application_sid": "",
                    "sms_fallback_method": "POST",
                    "sms_fallback_url": "",
                    "sms_method": "POST",
                    "sms_url": "",
                    "status_callback": "",
                    "status_callback_method": "POST",
                    "trunk_sid": null,
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
                    "voice_application_sid": "",
                    "voice_caller_id_lookup": false,
                    "voice_fallback_method": "POST",
                    "voice_fallback_url": null,
                    "voice_method": "POST",
                    "voice_url": null
                }
            ],
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1&Page=2",
            "next_page_uri": null,
            "num_pages": 3,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 3,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .incoming_phone_numbers \
            .local.list(
                beta=True,
                friendly_name="friendly_name",
                phone_number="+987654321"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Beta": "true",
                "FriendlyName": "friendly_name",
                "PhoneNumber": "+987654321"
            },
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1&Page=0",
            "incoming_phone_numbers": [],
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1&Page=2",
            "next_page_uri": null,
            "num_pages": 3,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 3,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .incoming_phone_numbers \
            .local.list(
                beta=True,
                friendly_name="friendly_name",
                phone_number="+987654321"
            )
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1&Page=0",
            "incoming_phone_numbers": [],
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1&Page=2",
            "next_page_uri": null,
            "num_pages": 3,
            "page": 0,
            "page_size": 1,
            "previous_page_uri": null,
            "start": 0,
            "total": 3,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json?PageSize=1"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .incoming_phone_numbers \
            .local.list(
                beta=True,
                friendly_name="friendly_name",
                phone_number="+987654321"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "Beta": "true",
                "FriendlyName": "friendly_name",
                "PhoneNumber": "+987654321"
            },
        )

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "address_requirements": "none",
            "api_version": "2010-04-01",
            "beta": false,
            "capabilities": {
                "mms": true,
                "sms": false,
                "voice": true
            },
            "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",
            "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",
            "friendly_name": "(808) 925-5327",
            "phone_number": "+18089255327",
            "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_application_sid": "",
            "sms_fallback_method": "POST",
            "sms_fallback_url": "",
            "sms_method": "POST",
            "sms_url": "",
            "status_callback": "",
            "status_callback_method": "POST",
            "trunk_sid": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_application_sid": "",
            "voice_caller_id_lookup": false,
            "voice_fallback_method": "POST",
            "voice_fallback_url": null,
            "voice_method": "POST",
            "voice_url": null
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .incoming_phone_numbers \
            .local.create(
                "area_code",
                "+987654321",
                api_version="api_version",
                friendly_name="friendly_name",
                sms_application_sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                sms_fallback_method="GET",
                sms_fallback_url="https://example.com",
                sms_method="GET",
                sms_url="https://example.com",
                status_callback="https://example.com",
                status_callback_method="GET",
                voice_application_sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                voice_caller_id_lookup=True,
                voice_fallback_method="GET",
                voice_fallback_url="https://example.com",
                voice_method="GET",
                voice_url="https://example.com"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/Local.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "ApiVersion": "api_version",
                "AreaCode": "area_code",
                "FriendlyName": "friendly_name",
                "PhoneNumber": "+987654321",
                "SmsApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "SmsFallbackMethod": "GET",
                "SmsFallbackUrl": "https://example.com",
                "SmsMethod": "GET",
                "SmsUrl": "https://example.com",
                "StatusCallback": "https://example.com",
                "StatusCallbackMethod": "GET",
                "VoiceApplicationSid": "APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "VoiceCallerIdLookup": "true",
                "VoiceFallbackMethod": "GET",
                "VoiceFallbackUrl": "https://example.com",
                "VoiceMethod": "GET",
                "VoiceUrl": "https://example.com"
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "address_requirements": "none",
            "api_version": "2010-04-01",
            "beta": false,
            "capabilities": {
                "mms": true,
                "sms": false,
                "voice": true
            },
            "date_created": "Thu, 30 Jul 2015 23:19:04 +0000",
            "date_updated": "Thu, 30 Jul 2015 23:19:04 +0000",
            "friendly_name": "(808) 925-5327",
            "phone_number": "+18089255327",
            "sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "sms_application_sid": "",
            "sms_fallback_method": "POST",
            "sms_fallback_url": "",
            "sms_method": "POST",
            "sms_url": "",
            "status_callback": "",
            "status_callback_method": "POST",
            "trunk_sid": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/IncomingPhoneNumbers/PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            "voice_application_sid": "",
            "voice_caller_id_lookup": false,
            "voice_fallback_method": "POST",
            "voice_fallback_url": null,
            "voice_method": "POST",
            "voice_url": null
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .incoming_phone_numbers \
            .local.create(
                "area_code",
                "+987654321",
                api_version="api_version",
                friendly_name="friendly_name",
                sms_application_sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                sms_fallback_method="GET",
                sms_fallback_url="https://example.com",
                sms_method="GET",
                sms_url="https://example.com",
                status_callback="https://example.com",
                status_callback_method="GET",
                voice_application_sid="APaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                voice_caller_id_lookup=True,
                voice_fallback_method="GET",
                voice_fallback_url="https://example.com",
                voice_method="GET",
                voice_url="https://example.com"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.address_requirements)
        self.assertEqual(u"none", instance.address_requirements)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2010-04-01", instance.api_version)
        self.assertIsNotNone(instance.beta)
        self.assertEqual(False, instance.beta)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Thu, 30 Jul 2015 23:19:04 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Thu, 30 Jul 2015 23:19:04 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"(808) 925-5327", instance.friendly_name)
        self.assertIsNotNone(instance.phone_number)
        self.assertEqual(u"+18089255327", instance.phone_number)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)
        self.assertIsNotNone(instance.sms_application_sid)
        self.assertEqual(u"", instance.sms_application_sid)
        self.assertIsNotNone(instance.sms_fallback_method)
        self.assertEqual(u"POST", instance.sms_fallback_method)
        self.assertIsNotNone(instance.sms_fallback_url)
        self.assertEqual(u"", instance.sms_fallback_url)
        self.assertIsNotNone(instance.sms_method)
        self.assertEqual(u"POST", instance.sms_method)
        self.assertIsNotNone(instance.sms_url)
        self.assertEqual(u"", instance.sms_url)
        self.assertIsNotNone(instance.status_callback)
        self.assertEqual(u"", instance.status_callback)
        self.assertIsNotNone(instance.status_callback_method)
        self.assertEqual(u"POST", instance.status_callback_method)
        self.assertIsNone(instance.trunk_sid)
        self.assertIsNotNone(instance.voice_application_sid)
        self.assertEqual(u"", instance.voice_application_sid)
        self.assertIsNotNone(instance.voice_caller_id_lookup)
        self.assertEqual(False, instance.voice_caller_id_lookup)
        self.assertIsNotNone(instance.voice_fallback_method)
        self.assertEqual(u"POST", instance.voice_fallback_method)
        self.assertIsNone(instance.voice_fallback_url)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"POST", instance.voice_method)
        self.assertIsNone(instance.voice_url)
