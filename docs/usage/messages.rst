.. module:: twilio.rest.resources.sms_messages

============
Messages
============

The :class:`Messages` resource manages all interaction with Twilio SMS and MMS messages. For more information, see the
`Message REST Resource <http://www.twilio.com/docs/api/rest/message>`_
documentation.


Sending a Text Message
----------------------

The :class:`Message` resource allows you to send an SMS message in a few lines of code.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="Hello Monkey!",  # Message body, if any
        to="+12125551234",
        from_="+15105551234",
    )
    print message.sid


If you want to send a message from a `short code
<http://www.twilio.com/api/sms/short-codes>`_ on Twilio, just set :attr:`from_`
to your short code's number.


Sending a Picture Message
-------------------------

To send a picture message (MMS), set :attr:`media_url` to the url of the picture you wish to send.

Don't forget to check the `availability of MMS in your area <https://www.twilio.com/mms>`_ before using this functionality.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body="Hello Monkey!",  # Message body, if any
        to="+12125551234",
        from_="+15105551234",
        media_url="http://example.com/image1.jpg"
    )

You can send multiple pictures in the same message by setting :attr:`media_url` to
a list of urls.

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


Retrieving Sent Messages
-------------------------

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    for message in client.messages.list():
        print message.body


Filtering Your Messages
-------------------------

The :meth:`list` methods supports filtering on :attr:`to`, :attr:`from_`,
and :attr:`date_sent`.
The following will only show messages to "+5466758723" on January 1st, 2011.

.. code-block:: python

    from datetime import date
    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    messages = client.messages.list(
        to="+5466758723",
        date_sent=date(2011,1,1),
    )

    for message in messages:
        print message.body

Redacting or Deleting Message Records
-------------------------------------

To protect your users' privacy and/or comply with legal requirements,
Twilio allows you to redact your :class:`Message` bodies or delete the records
outright.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    message_sid = "MM123"

    client.messages.redact(message_sid)
    message = client.messages.get(message_sid)
    print message.body  # Will be an empty string

    client.messages.delete(message_sid)  # Deletes record entirely, subsequent requests will return 404

