import os

from twilio.rest import Client
from twilio.credential.orgs_credential_provider import OrgsCredentialProvider

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
API_KEY = os.environ.get("TWILIO_API_KEY")
API_SECRET = os.environ.get("TWILIO_API_SECRET")

CLIENT_ID = os.environ.get("TWILIO_CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
ORGS_SID = os.environ.get("ORGS_SID")


def example():
    """
    Some example usage of using organization resources
    """
    client = Client(
        account_sid=ACCOUNT_SID,
        credential_provider=OrgsCredentialProvider(CLIENT_ID, CLIENT_SECRET),
    )

    accounts = client.preview_iam.organization(
        organization_sid=ORGS_SID
    ).accounts.stream()
    for record in accounts:
        print(record)


if __name__ == "__main__":
    example()
