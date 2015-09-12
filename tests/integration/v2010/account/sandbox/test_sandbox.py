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


class SandboxIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Fri, 18 Feb 2011 17:37:18 +0000",
            "phone_number": "4155992671",
            "pin": "66528411",
            "sms_method": "POST",
            "sms_url": "http://demo.twilio.com/welcome/sms",
            "status_callback": null,
            "status_callback_method": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
            "voice_method": "POST",
            "voice_url": "http://www.digg.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sandbox.get()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Fri, 18 Feb 2011 17:37:18 +0000",
            "phone_number": "4155992671",
            "pin": "66528411",
            "sms_method": "POST",
            "sms_url": "http://demo.twilio.com/welcome/sms",
            "status_callback": null,
            "status_callback_method": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
            "voice_method": "POST",
            "voice_url": "http://www.digg.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sandbox.get()
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 15 Mar 2009 02:08:47 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 17:37:18 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.phone_number)
        self.assertEqual(u"4155992671", instance.phone_number)
        self.assertIsNotNone(instance.pin)
        self.assertEqual(u"66528411", instance.pin)
        self.assertIsNotNone(instance.sms_method)
        self.assertEqual(u"POST", instance.sms_method)
        self.assertIsNotNone(instance.sms_url)
        self.assertEqual(u"http://demo.twilio.com/welcome/sms", instance.sms_url)
        self.assertIsNone(instance.status_callback)
        self.assertIsNone(instance.status_callback_method)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"POST", instance.voice_method)
        self.assertIsNotNone(instance.voice_url)
        self.assertEqual(u"http://www.digg.com", instance.voice_url)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Fri, 18 Feb 2011 17:37:18 +0000",
            "phone_number": "4155992671",
            "pin": "66528411",
            "sms_method": "POST",
            "sms_url": "http://demo.twilio.com/welcome/sms",
            "status_callback": null,
            "status_callback_method": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
            "voice_method": "POST",
            "voice_url": "http://www.digg.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sandbox.update(
                voice_url="https://example.com",
                voice_method="GET",
                sms_url="https://example.com",
                sms_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "SmsMethod": "GET",
                "SmsUrl": "https://example.com",
                "StatusCallback": "https://example.com",
                "StatusCallbackMethod": "GET",
                "VoiceMethod": "GET",
                "VoiceUrl": "https://example.com"
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "api_version": "2008-08-01",
            "date_created": "Sun, 15 Mar 2009 02:08:47 +0000",
            "date_updated": "Fri, 18 Feb 2011 17:37:18 +0000",
            "phone_number": "4155992671",
            "pin": "66528411",
            "sms_method": "POST",
            "sms_url": "http://demo.twilio.com/welcome/sms",
            "status_callback": null,
            "status_callback_method": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Sandbox.json",
            "voice_method": "POST",
            "voice_url": "http://www.digg.com"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .sandbox.update(
                voice_url="https://example.com",
                voice_method="GET",
                sms_url="https://example.com",
                sms_method="GET",
                status_callback="https://example.com",
                status_callback_method="GET"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.api_version)
        self.assertEqual(u"2008-08-01", instance.api_version)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Sun, 15 Mar 2009 02:08:47 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 18 Feb 2011 17:37:18 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.phone_number)
        self.assertEqual(u"4155992671", instance.phone_number)
        self.assertIsNotNone(instance.pin)
        self.assertEqual(u"66528411", instance.pin)
        self.assertIsNotNone(instance.sms_method)
        self.assertEqual(u"POST", instance.sms_method)
        self.assertIsNotNone(instance.sms_url)
        self.assertEqual(u"http://demo.twilio.com/welcome/sms", instance.sms_url)
        self.assertIsNone(instance.status_callback)
        self.assertIsNone(instance.status_callback_method)
        self.assertIsNotNone(instance.voice_method)
        self.assertEqual(u"POST", instance.voice_method)
        self.assertIsNotNone(instance.voice_url)
        self.assertEqual(u"http://www.digg.com", instance.voice_url)
