import os
import logging

from twilio.rest import Client
# from twilio.twiml.voice_response import VoiceResponse

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
FROM_NUMBER = os.environ.get('FROM_NUMBER')
TO_NUMBER = os.environ.get('TO_NUMBER')


def example():
    """
    Some example usage of different twilio resources.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN, log_level=logging.DEBUG)

    # # Get all messages
    # all_messages = client.messages.list()
    # print('There are {} messages in your account.'.format(len(all_messages)))

    # Get only last 10 messages...
    some_messages = client.messages.list(limit=1)
    print('Here are the last 10 messages in your account:')
    for m in some_messages:
        print(m)

    # # Get messages in smaller pages...
    # all_messages = client.messages.list(page_size=10)
    # print('There are {} messages in your account.'.format(len(all_messages)))

    # print('Sending a message...')
    # new_message = client.messages.create(to=TO_NUMBER, from_=FROM_NUMBER, body='Twilio rocks!')

    # print('Making a call...')
    # new_call = client.calls.create(to=TO_NUMBER, from_=FROM_NUMBER, method='GET')
    #
    # print('Serving TwiML')
    # twiml_response = VoiceResponse()
    # twiml_response.say('Hello!')
    # twiml_response.hangup()
    # twiml_xml = twiml_response.to_xml()
    # print('Generated twiml: {}'.format(twiml_xml))


if __name__ == '__main__':
    example()
