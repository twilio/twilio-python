===========
Quickstart
===========

Getting started with the Twilio API couldn't be easier. Create a Twilio REST client to get started. For example, the following code makes a call using the Twilio REST API.

Making a Call
===============

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    call = client.calls.create(to="9991231234", from_="9991231234",
                               url="http://foo.com/call.xml")
    print call.length
    print call.sid

Generating TwiML
=================

To control phone calls, your application need to output TwiML. Use :class:`twilio.twiml.Response` to easily create such responses.

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()
    r.play("monkey.mp3", loop=5)
    print str(r)

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <Response><Play loop="5">monkey.mp3</Play><Response>

Digging Deeper
========================

The full power of the Twilio API is at your finger tips. The :ref:`user-guide` explains all the awesome features available to use.






