===========
Quickstart
===========

Getting started with the Twilio API couldn't be easier. Create a Twilio REST
client to get started. For example, the following code makes a call using the
Twilio REST API.


Make a Call
===========

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls.create(to="9991231234", from_="9991231234",
        url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
    print call.length
    print call.sid


Send an SMS
===========

.. code-block:: python

    from twilio.rest import TwilioRestClient

    account = "ACXXXXXXXXXXXXXXXXX"
    token = "YYYYYYYYYYYYYYYYYY"
    client = TwilioRestClient(account, token)

    message = client.sms.messages.create(to="+12316851234",
                                         from_="+15555555555",
                                         body="Hello there!")

Send an MMS
===========

.. code-block:: python

    message = client.messages.create(
        body="Hello Monkey!",  # Message body, if any
        to="+12125551234",
        from_="+15105551234",
        media_url=[  # List of media URLs, if any
            "http://example.com/image1.jpg",
            "http://example.com/image2.jpg",
        ],
    )


Generating TwiML
================

To control phone calls, your application needs to output `TwiML
<http://www.twilio.com/docs/api/twiml/>`_. Use :class:`twilio.twiml.Response`
to easily create such responses.

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()
    r.play("https://api.twilio.com/cowbell.mp3", loop=5)
    print str(r)

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <Response>
        <Play loop="5">https://api.twilio.com/cowbell.mp3</Play>
    <Response>


Digging Deeper
========================

The full power of the Twilio API is at your fingertips. The :ref:`user-guide`
explains all the awesome features available to use.

