import os

from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def example():
    """
    Some example usage of different twilio resources.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Get all messages
    all_messages = client.messages.list()
    print(f"There are {len(all_messages)} messages in your account.")

    # Get only last 10 messages...
    some_messages = client.messages.list(limit=10)
    print("Here are the last 10 messages in your account:")
    for m in some_messages:
        print(m)

    # Get messages in smaller pages...
    all_messages = client.messages.list(page_size=10)
    print(f"There are {len(all_messages)} messages in your account.")

    print("Sending a message...")
    new_message = client.messages.create(to="XXXX", from_="YYYY", body="Twilio rocks!")

    print("Making a call...")
    new_call = client.calls.create(to="XXXX", from_="YYYY", method="GET")

    print("Serving TwiML")
    twiml_response = VoiceResponse()
    twiml_response.say("Hello!")
    twiml_response.hangup()
    twiml_xml = twiml_response.to_xml()
    print(f"Generated twiml: {twiml_xml}")


if __name__ == "__main__":
    example()
