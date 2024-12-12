import os

from twilio.rest import Client
from twilio.credential.orgs_credential_provider import OrgsCredentialProvider

API_KEY = os.environ.get("TWILIO_API_KEY")
API_SECRET = os.environ.get("TWILIO_API_SECRET")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
CLIENT_ID = os.environ.get("TWILIO_CLIENT_ID")
CLIENT_SECRET = os.environ.get("TWILIO_CLIENT_SECRET")
ORGS_SID = os.environ.get("TWILIO_ORGS_SID")


def example(self=None):
    """
    Some example usage of fetching accounts within an organization
    """
    self.client = Client(
        username=API_KEY,
        password=API_SECRET,
        account_sid=ACCOUNT_SID,
        credential_provider= OrgsCredentialProvider(CLIENT_ID, CLIENT_SECRET)
    )
    accounts = self.client.preview_iam.organization(organization_sid=ORGS_SID).accounts.stream()
    self.assertIsNotNone(accounts)

if __name__ == "__main__":
    example()
