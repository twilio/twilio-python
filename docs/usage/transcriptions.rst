.. module:: twilio.rest.resources

================
Transcriptions
================

Transcriptions are generated from recordings via the `TwiML <Record> verb <http://www.twilio.com/docs/api/twiml/record>`_. Using the API, you can only read your transcription records.

For more information, see the `Transcriptions REST Resource <http://www.twilio.com/docs/api/rest/transcription>`_ documentation.

Listing Your Transcriptions
----------------------------

The following code will print out lengths :attr:`friendly_name` for each :class:`Application`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()
    for transcription in conn.transcriptions.list():
        print transcription.duration
