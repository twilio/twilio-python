.. module:: twilio.rest.resources

================
Recordings
================

For more information, see the
`Recordings REST Resource <http://www.twilio.com/docs/api/rest/recording>`_
documentation.


Audio Formats
-----------------

Each :class:`Recording` has a :attr:`formats` dictionary which lists the audio
formats available for each recording.
Below is an example :attr:`formats` dictionary.

.. code-block:: python

   {
       "mp3": "https://api.twilio.com/cowbell.mp3",
       "wav": "http://www.dailywav.com/0112/noFateButWhatWeMake.wav",
   }


Listing Your Recordings
----------------------------

The following code will print out the :attr:`duration`
for each :class:`Recording`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for recording in client.recordings.list():
        print recording.duration

You can filter recordings by CallSid by passing the Sid as :attr:`call`.
Filter recordings using :attr:`before` and :attr:`after` dates.

The following will only show recordings made before January 1, 2011.

.. code-block:: python

    from datetime import date
    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for recording in client.recordings.list(before=date(2011,1,1)):
        print recording.duration


Deleting Recordings
---------------------

The :class:`Recordings` resource allows you to delete unnecessary recordings.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.recordings.delete("RC123")


Accessing Related Transcptions
-------------------------------

The :class:`Recordings` allows you to retrieve associated transcriptions.
The following prints out the text for each of the transcriptions associated
with this recording.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    recording = client.recordings.get("RC123")

    for transcription in recording.transcriptions.list():
        print transcription.transcription_text

