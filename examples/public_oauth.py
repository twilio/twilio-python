import os

from twilio.rest import Client
from twilio.credential.client_credential_provider import ClientCredentialProvider

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
API_KEY = os.environ.get("TWILIO_API_KEY")
API_SECRET = os.environ.get("TWILIO_API_SECRET")
FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")

CLIENT_ID = os.environ.get("TWILIO_CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")


def example():
    """
    Some example usage of message resources.
    """
    client = Client(
        account_sid=ACCOUNT_SID,
        credential_provider=ClientCredentialProvider(CLIENT_ID, CLIENT_SECRET),
    )

    msg = client.messages.create(
        to=self.to_number, from_=self.from_number, body="hello world"
    )


if __name__ == "__main__":
    example()
