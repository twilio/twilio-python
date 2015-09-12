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
from twilio.rest.pricing.client import PricingClient
from twilio.rest.http import Response


class CountryIntegrationTest(unittest.TestCase):

    def test_read_full_can_parse_response(self):
        holodeck = Holodeck()
        client = PricingClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "countries": [
                {
                    "country": "Austria",
                    "iso_country": "AT",
                    "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries/AT"
                }
            ],
            "meta": {
                "first_page_url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0",
                "key": "countries",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0"
            }
        }
        """))
        
        query = client \
            .phone_numbers \
            .countries.list()
        
        instances = query.execute()
        
        self.assertEqual(1, len(instances))
        
        self.assertIsNotNone(instances[0].country)
        self.assertEqual(u"Austria", instances[0].country)
        self.assertIsNotNone(instances[0].iso_country)
        self.assertEqual(u"AT", instances[0].iso_country)

    def test_read_full_request_validation(self):
        holodeck = Holodeck()
        client = PricingClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "countries": [
                {
                    "country": "Austria",
                    "iso_country": "AT",
                    "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries/AT"
                }
            ],
            "meta": {
                "first_page_url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0",
                "key": "countries",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0"
            }
        }
        """))
        
        query = client \
            .phone_numbers \
            .countries.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://pricing.twilio.com/v1/PhoneNumbers/Countries",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_read_empty_can_parse_response(self):
        holodeck = Holodeck()
        client = PricingClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "countries": [],
            "meta": {
                "first_page_url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0",
                "key": "countries",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0"
            }
        }
        """))
        
        query = client \
            .phone_numbers \
            .countries.list()
        
        instances = query.execute()
        
        self.assertEqual(0, len(instances))

    def test_read_empty_request_validation(self):
        holodeck = Holodeck()
        client = PricingClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "countries": [],
            "meta": {
                "first_page_url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0",
                "key": "countries",
                "next_page_url": null,
                "page": 0,
                "page_size": 1,
                "previous_page_url": null,
                "url": "https://pricing.twilio.com/v1/PhoneNumbers/Countries?PageSize=1&Page=0"
            }
        }
        """))
        
        query = client \
            .phone_numbers \
            .countries.list()
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://pricing.twilio.com/v1/PhoneNumbers/Countries",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_request_validation(self):
        holodeck = Holodeck()
        client = PricingClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "country": "Estonia",
            "iso_country": "EE",
            "phone_number_prices": [
                {
                    "base_price": 3.0,
                    "current_price": 3.0,
                    "type": "mobile"
                },
                {
                    "base_price": 1.0,
                    "current_price": 1.0,
                    "type": "national"
                }
            ],
            "price_unit": "usd",
            "uri": "/PhoneNumbers/Countries/US"
        }
        """))
        
        query = client \
            .phone_numbers \
            .countries.get("US")
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "GET",
            "https://pricing.twilio.com/v1/PhoneNumbers/Countries/US",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={},
            query_params={},
        )

    def test_fetch_can_parse_response(self):
        holodeck = Holodeck()
        client = PricingClient("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "country": "Estonia",
            "iso_country": "EE",
            "phone_number_prices": [
                {
                    "base_price": 3.0,
                    "current_price": 3.0,
                    "type": "mobile"
                },
                {
                    "base_price": 1.0,
                    "current_price": 1.0,
                    "type": "national"
                }
            ],
            "price_unit": "usd",
            "uri": "/PhoneNumbers/Countries/US"
        }
        """))
        
        query = client \
            .phone_numbers \
            .countries.get("US")
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.country)
        self.assertEqual(u"Estonia", instance.country)
        self.assertIsNotNone(instance.iso_country)
        self.assertEqual(u"EE", instance.iso_country)
        self.assertIsNotNone(instance.price_unit)
        self.assertEqual(u"usd", instance.price_unit)
