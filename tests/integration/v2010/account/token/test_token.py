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


class TokenIntegrationTest(unittest.TestCase):

    def test_create_request_validation(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 24 Jul 2015 18:43:58 +0000",
            "date_updated": "Fri, 24 Jul 2015 18:43:58 +0000",
            "ice_servers": [
                {
                    "url": "stun:global.stun:3478?transport=udp"
                },
                {
                    "credential": "5SR2x8mZK1lTFJW3NVgLGw6UM9C0dja4jI/Hdw3xr+w=",
                    "url": "turn:global.turn:3478?transport=udp",
                    "username": "cda92e5006c7810494639fc466ecc80182cef8183fdf400f84c4126f3b59d0bb"
                }
            ],
            "password": "5SR2x8mZK1lTFJW3NVgLGw6UM9C0dja4jI/Hdw3xr+w=",
            "ttl": "86400",
            "username": "cda92e5006c7810494639fc466ecc80182cef8183fdf400f84c4126f3b59d0bb"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tokens.create(ttl=1)
        
        query.execute()
        
        holodeck.assert_called_once_with(
            "POST",
            "https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Tokens.json",
            ("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN"),
            form_params={
                "Ttl": 1
            },
            query_params={},
        )

    def test_create_can_parse_response(self):
        holodeck = Holodeck()
        client = V2010Client("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "AUTHTOKEN", client=holodeck)
        
        holodeck.mock(Response(200, """
        {
            "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "date_created": "Fri, 24 Jul 2015 18:43:58 +0000",
            "date_updated": "Fri, 24 Jul 2015 18:43:58 +0000",
            "ice_servers": [
                {
                    "url": "stun:global.stun:3478?transport=udp"
                },
                {
                    "credential": "5SR2x8mZK1lTFJW3NVgLGw6UM9C0dja4jI/Hdw3xr+w=",
                    "url": "turn:global.turn:3478?transport=udp",
                    "username": "cda92e5006c7810494639fc466ecc80182cef8183fdf400f84c4126f3b59d0bb"
                }
            ],
            "password": "5SR2x8mZK1lTFJW3NVgLGw6UM9C0dja4jI/Hdw3xr+w=",
            "ttl": "86400",
            "username": "cda92e5006c7810494639fc466ecc80182cef8183fdf400f84c4126f3b59d0bb"
        }
        """))
        
        query = client \
            .accounts.get("ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
            .tokens.create(ttl=1)
        
        instance = query.execute()
        
        self.assertIsNotNone(instance.account_sid)
        self.assertEqual(u"ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", instance.account_sid)
        self.assertIsNotNone(instance.date_created)
        self.assertEqual(parse_iso_date("Fri, 24 Jul 2015 18:43:58 +0000"), instance.date_created)
        self.assertIsNotNone(instance.date_updated)
        self.assertEqual(parse_iso_date("Fri, 24 Jul 2015 18:43:58 +0000"), instance.date_updated)
        self.assertIsNotNone(instance.password)
        self.assertEqual(u"5SR2x8mZK1lTFJW3NVgLGw6UM9C0dja4jI/Hdw3xr+w=", instance.password)
        self.assertIsNotNone(instance.ttl)
        self.assertEqual(u"86400", instance.ttl)
        self.assertIsNotNone(instance.username)
        self.assertEqual(u"cda92e5006c7810494639fc466ecc80182cef8183fdf400f84c4126f3b59d0bb", instance.username)
