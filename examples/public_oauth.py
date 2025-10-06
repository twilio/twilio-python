import os

from twilio.rest import Client
from twilio.credential.client_credential_provider import ClientCredentialProvider

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
MESSAGE_SID = os.environ.get("TWILIO_MESSAGE_SID")

CLIENT_ID = os.environ.get("TWILIO_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TWILIO_CLIENT_SECRET")


def example():
    """
    An example usage of message resource.
    """
    client = Client(
        account_sid=ACCOUNT_SID,
        credential_provider=ClientCredentialProvider(CLIENT_ID, CLIENT_SECRET),
    )

    msg = client.messages(MESSAGE_SID).fetch()

    print(msg)


if __name__ == "__main__":
    example()
