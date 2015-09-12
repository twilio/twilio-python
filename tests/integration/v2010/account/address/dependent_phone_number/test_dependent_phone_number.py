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


class DependentPhoneNumberIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "dependent_phone_numbers": [
                {
                    "address_requirements": "any",
                    "capabilities": {
                        "MMS": "false",
                        "SMS": "true",
                        "voice": "true"
                    },
                    "friendly_name": "(510) 555-1212",
                    "iso_country": "US",
                    "lata": "722",
                    "latitude": "37.780000",
                    "longitude": "-122.380000",
                    "phone_number": "+15105551212",
                    "postal_code": "94703",
                    "rate_center": "OKLD TRNID",
                    "region": "CA"
                }
            ],
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.get("ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .dependent_phone_numbers.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].address_requirements)
        self.assertEqual(u"any", instances[0].address_requirements)
        self.assertIsNotNone(instances[0].capabilities)
        self.assertEqual({
            "MMS": "false",
            "SMS": "true",
            "voice": "true"
        }, instances[0].capabilities)
        self.assertIsNotNone(instances[0].friendly_name)
        self.assertEqual(u"(510) 555-1212", instances[0].friendly_name)
        self.assertIsNotNone(instances[0].iso_country)
        self.assertEqual(u"US", instances[0].iso_country)
        self.assertIsNotNone(instances[0].lata)
        self.assertEqual(u"722", instances[0].lata)
        self.assertIsNotNone(instances[0].latitude)
        self.assertEqual(u"37.780000", instances[0].latitude)
        self.assertIsNotNone(instances[0].longitude)
        self.assertEqual(u"-122.380000", instances[0].longitude)
        self.assertIsNotNone(instances[0].phone_number)
        self.assertEqual(u"+15105551212", instances[0].phone_number)
        self.assertIsNotNone(instances[0].postal_code)
        self.assertEqual(u"94703", instances[0].postal_code)
        self.assertIsNotNone(instances[0].rate_center)
        self.assertEqual(u"OKLD TRNID", instances[0].rate_center)
        self.assertIsNotNone(instances[0].region)
        self.assertEqual(u"CA", instances[0].region)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "dependent_phone_numbers": [
                {
                    "address_requirements": "any",
                    "capabilities": {
                        "MMS": "false",
                        "SMS": "true",
                        "voice": "true"
                    },
                    "friendly_name": "(510) 555-1212",
                    "iso_country": "US",
                    "lata": "722",
                    "latitude": "37.780000",
                    "longitude": "-122.380000",
                    "phone_number": "+15105551212",
                    "postal_code": "94703",
                    "rate_center": "OKLD TRNID",
                    "region": "CA"
                }
            ],
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.get("ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .dependent_phone_numbers.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "dependent_phone_numbers": [],
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.get("ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .dependent_phone_numbers.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "dependent_phone_numbers": [],
            "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json?Page=0&PageSize=50",
            "next_page_uri": null,
            "page": 0,
            "page_size": 50,
            "previous_page_uri": null,
            "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .addresses.get("ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .dependent_phone_numbers.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Addresses/ADaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/DependentPhoneNumbers.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )
