import unittest

from twilio.base.exceptions import TwilioException
from twilio.rest import Client

API_KEY_SID = "SK" + "a" * 32
ACCOUNT_SID = "AC" + "b" * 32


class TestApiKeyWithoutAccountSid(unittest.TestCase):
    def test_api_key_without_account_sid_raises(self):
        with self.assertRaises(TwilioException) as ctx:
            Client(API_KEY_SID, "my-api-secret")
        message = str(ctx.exception)
        self.assertIn("API Key", message)
        self.assertIn("account_sid", message)

    def test_api_key_from_environment_without_account_sid_raises(self):
        environment = {
            "TWILIO_ACCOUNT_SID": API_KEY_SID,
            "TWILIO_AUTH_TOKEN": "my-api-secret",
        }
        with self.assertRaises(TwilioException):
            Client(environment=environment)

    def test_api_key_with_account_sid_works(self):
        client = Client(API_KEY_SID, "my-api-secret", account_sid=ACCOUNT_SID)
        self.assertEqual(client.account_sid, ACCOUNT_SID)
        self.assertEqual(client.username, API_KEY_SID)
        client.http_client.session.close()

    def test_account_sid_and_auth_token_still_work(self):
        client = Client(ACCOUNT_SID, "token")
        self.assertEqual(client.account_sid, ACCOUNT_SID)
        client.http_client.session.close()


if __name__ == "__main__":
    unittest.main()
