.. module:: twilio.rest.resources

================
Transcriptions
================

Transcriptions are generated from recordings via the
`TwiML <Record> verb <http://www.twilio.com/docs/api/twiml/record>`_.
Using the API, you can only read your transcription records.

For more information, see the `Transcriptions REST Resource
<http://www.twilio.com/docs/api/rest/transcription>`_ documentation.


Listing Your Transcriptions
----------------------------

The following code will print out the length of each :class:`Transcription`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for transcription in client.transcriptions.list():
        print transcription.duration

