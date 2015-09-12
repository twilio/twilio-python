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
from twilio.ext.holodeck import Holodeck
from twilio.rest.v2010.client import V2010Client
from twilio.rest.http import Response


class ConnectAppIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "authorize_redirect_url": "http://example.com/redirect",
            "company_name": "Twilio",
            "deauthorize_callback_method": "GET",
            "deauthorize_callback_url": "http://example.com/deauth",
            "description": null,
            "friendly_name": "Connect app for deletion",
            "homepage_url": "http://example.com/home",
            "permissions": [],
            "sid": "CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps/CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .connect_apps.get("CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps/CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
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
            "authorize_redirect_url": "http://example.com/redirect",
            "company_name": "Twilio",
            "deauthorize_callback_method": "GET",
            "deauthorize_callback_url": "http://example.com/deauth",
            "description": null,
            "friendly_name": "Connect app for deletion",
            "homepage_url": "http://example.com/home",
            "permissions": [],
            "sid": "CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps/CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .connect_apps.get("CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.authorize_redirect_url)
        self.assertEqual(u"http://example.com/redirect", instance.authorize_redirect_url)
        self.assertIsNotNone(instance.company_name)
        self.assertEqual(u"Twilio", instance.company_name)
        self.assertIsNotNone(instance.deauthorize_callback_method)
        self.assertEqual(u"GET", instance.deauthorize_callback_method)
        self.assertIsNotNone(instance.deauthorize_callback_url)
        self.assertEqual(u"http://example.com/deauth", instance.deauthorize_callback_url)
        self.assertIsNone(instance.description)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Connect app for deletion", instance.friendly_name)
        self.assertIsNotNone(instance.homepage_url)
        self.assertEqual(u"http://example.com/home", instance.homepage_url)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_update_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "authorize_redirect_url": "http://example.com/redirect",
            "company_name": "Twilio",
            "deauthorize_callback_method": "GET",
            "deauthorize_callback_url": "http://example.com/deauth",
            "description": null,
            "friendly_name": "Connect app for deletion",
            "homepage_url": "http://example.com/home",
            "permissions": [],
            "sid": "CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps/CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .connect_apps.update(
                "CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                authorize_redirect_url="https://example.com",
                company_name="company_name",
                deauthorize_callback_method="GET",
                deauthorize_callback_url="https://example.com",
                description="description",
                friendly_name="friendly_name",
                homepage_url="https://example.com",
                permissions=['get-all']
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps/CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "AuthorizeRedirectUrl": "https://example.com",
                "CompanyName": "company_name",
                "DeauthorizeCallbackMethod": "GET",
                "DeauthorizeCallbackUrl": "https://example.com",
                "Description": "description",
                "FriendlyName": "friendly_name",
                "HomepageUrl": "https://example.com",
                "Permissions": [
                    "get-all"
                ]
            },
            query_params={},
        )

    def test_update_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "authorize_redirect_url": "http://example.com/redirect",
            "company_name": "Twilio",
            "deauthorize_callback_method": "GET",
            "deauthorize_callback_url": "http://example.com/deauth",
            "description": null,
            "friendly_name": "Connect app for deletion",
            "homepage_url": "http://example.com/home",
            "permissions": [],
            "sid": "CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps/CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .connect_apps.update(
                "CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                authorize_redirect_url="https://example.com",
                company_name="company_name",
                deauthorize_callback_method="GET",
                deauthorize_callback_url="https://example.com",
                description="description",
                friendly_name="friendly_name",
                homepage_url="https://example.com",
                permissions=['get-all']
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.authorize_redirect_url)
        self.assertEqual(u"http://example.com/redirect", instance.authorize_redirect_url)
        self.assertIsNotNone(instance.company_name)
        self.assertEqual(u"Twilio", instance.company_name)
        self.assertIsNotNone(instance.deauthorize_callback_method)
        self.assertEqual(u"GET", instance.deauthorize_callback_method)
        self.assertIsNotNone(instance.deauthorize_callback_url)
        self.assertEqual(u"http://example.com/deauth", instance.deauthorize_callback_url)
        self.assertIsNone(instance.description)
        self.assertIsNotNone(instance.friendly_name)
        self.assertEqual(u"Connect app for deletion", instance.friendly_name)
        self.assertIsNotNone(instance.homepage_url)
        self.assertEqual(u"http://example.com/home", instance.homepage_url)
        self.assertIsNotNone(instance.sid)
        self.assertEqual(u"CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.sid)

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "connect_apps": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "authorize_redirect_url": "http://example.com/redirect",
                    "company_name": "Twilio",
                    "deauthorize_callback_method": "GET",
                    "deauthorize_callback_url": "http://example.com/deauth",
                    "description": null,
                    "friendly_name": "Connect app for deletion",
                    "homepage_url": "http://example.com/home",
                    "permissions": [],
                    "sid": "CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps/CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .connect_apps.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].account_sid)
        self.assertIsNotNone(instances[0].authorize_redirect_url)
        self.assertEqual(u"http://example.com/redirect", instances[0].authorize_redirect_url)
        self.assertIsNotNone(instances[0].company_name)
        self.assertEqual(u"Twilio", instances[0].company_name)
        self.assertIsNotNone(instances[0].deauthorize_callback_method)
        self.assertEqual(u"GET", instances[0].deauthorize_callback_method)
        self.assertIsNotNone(instances[0].deauthorize_callback_url)
        self.assertEqual(u"http://example.com/deauth", instances[0].deauthorize_callback_url)
        self.assertIsNone(instances[0].description)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"Connect app for deletion", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].homepage_url)
        self.assertEqual(u"http://example.com/home", instances[0].homepage_url)
        self.assertIsNotNone(instances[0].sid)
        self.assertEqual(u"CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instances[0].sid)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "connect_apps": [
                {
                    "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "authorize_redirect_url": "http://example.com/redirect",
                    "company_name": "Twilio",
                    "deauthorize_callback_method": "GET",
                    "deauthorize_callback_url": "http://example.com/deauth",
                    "description": null,
                    "friendly_name": "Connect app for deletion",
                    "homepage_url": "http://example.com/home",
                    "permissions": [],
                    "sid": "CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                    "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps/CNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json"
                }
            ],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .connect_apps.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "connect_apps": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .connect_apps.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "connect_apps": [],
            "end": 0,
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json?Page=0&PageSize=50",
            "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "num_pages": 1,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "start": 0,
            "total": 1,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .connect_apps.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ConnectApps.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )
