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
from twilio.rest.lookups.client import LookupsClient
from twilio.rest.http import Response


class PhoneNumberIntegrationTest(unittest.TestCase):

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = LookupsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "carrier": {
                "error_code": null,
                "mobile_country_code": "310",
                "mobile_network_code": "456",
                "name": "verizon",
                "type": "mobile"
            },
            "country_code": "US",
            "national_format": "(510) 867-5309",
            "phone_number": "+15108675309",
            "url": "https://lookups.twilio.com/v1/PhoneNumbers/phone_number"
        }
        """))
        
        query = client \
            .phone_numbers.get(
                "+987654321",
                country_code="country_code",
                type="type"
            )
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://lookups.twilio.com/v1/PhoneNumbers/+987654321",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={
                "CountryCode": "country_code",
                "Type": "type"
            },
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = LookupsClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "carrier": {
                "error_code": null,
                "mobile_country_code": "310",
                "mobile_network_code": "456",
                "name": "verizon",
                "type": "mobile"
            },
            "country_code": "US",
            "national_format": "(510) 867-5309",
            "phone_number": "+15108675309",
            "url": "https://lookups.twilio.com/v1/PhoneNumbers/phone_number"
        }
        """))
        
        query = client \
            .phone_numbers.get(
                "+987654321",
                country_code="country_code",
                type="type"
            )
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.carrier)
        self.assertEqual({
            "error_code": None,
            "mobile_country_code": "310",
            "mobile_network_code": "456",
            "name": "verizon",
            "type": "mobile"
        }, instance.carrier)
        self.assertIsNotNone(instance.country_code)
        self.assertEqual(u"US", instance.country_code)
        self.assertIsNotNone(instance.national_format)
        self.assertEqual(u"(510) 867-5309", instance.national_format)
        self.assertIsNotNone(instance.phone_number)
        self.assertEqual(u"+15108675309", instance.phone_number)
