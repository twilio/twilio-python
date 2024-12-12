import os

from twilio.rest import Client
from twilio.credential.client_credential_provider import ClientCredentialProvider

API_KEY = os.environ.get("TWILIO_API_KEY")
API_SECRET = os.environ.get("TWILIO_API_SECRET")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
CLIENT_ID = os.environ.get("TWILIO_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TWILIO_CLIENT_SECRET")
ORGS_SID = os.environ.get("TWILIO_ORGS_SID")
FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")


def example(self=None):
    """
    Some example usage of fetching accounts within an organization
    """
    self.client = Client(
        username=API_KEY,
        password=API_SECRET,
        account_sid=ACCOUNT_SID,
        credential_provider= ClientCredentialProvider(CLIENT_ID, CLIENT_SECRET)
    )
    msg = self.client.messages.create(
        to=self.to_number, from_=self.from_number, body="hello world"
    )
    self.assertEqual(msg.to, self.to_number)
    self.assertEqual(msg.from_, self.from_number)
    self.assertEqual(msg.body, "hello world")
    self.assertIsNotNone(msg.sid)

if __name__ == "__main__":
    example()
