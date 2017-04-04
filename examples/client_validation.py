import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PublicFormat,
    PrivateFormat,
    NoEncryption
)

from twilio.http.validation_client import ValidationClient
from twilio.rest import Client


ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

def example():
    """
    Example of using the ValidationClient for signed requests to Twilio.
    This is only available to enterprise customers.

    This will walkthrough creating an API Key, generating an RSA keypair, setting up a
    ValidationClient with these values and making requests with the client.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Using Client Validation requires using API Keys for auth
    # First create an API key using the standard account sid, auth token client
    print('Creating new api key...')
    api_key = client.new_keys.create(friendly_name='ClientValidationApiKey')

    # Generate a new RSA Keypair
    print('Generating RSA key pair...')
    key_pair = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = key_pair.public_key().public_bytes(Encoding.PEM, PublicFormat.SubjectPublicKeyInfo)
    private_key = key_pair.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, NoEncryption())

    # Register the public key with Twilio
    print('Registering public key with Twilio...')
    credential = client.accounts.credentials.public_key.create(
        public_key,
        friendly_name='ClientValidationPublicKey'
    )

    # Create a new ValidationClient with the keys we created
    validation_client = ValidationClient(
        ACCOUNT_SID,
        api_key.sid,
        credential.sid,
        private_key
    )

    # Create a REST Client using the validation_client
    client = Client(api_key.sid, api_key.secret, ACCOUNT_SID, http_client=validation_client)

    # Use the library as usual
    print('Trying out client validation...')
    messages = client.messages.list(limit=10)
    for m in messages:
        print('Message {}'.format(m.sid))

    print('Client validation works!')


if __name__ == '__main__':
    example()
