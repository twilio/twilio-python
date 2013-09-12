.. module:: twilio.rest.resources.sms_messages

============
Messages
============

For more information, see the
`SMS Message REST Resource <http://www.twilio.com/docs/api/rest/sms>`_
documentation.


Sending a Text Message
----------------------

Send a text message in only a few lines of code.

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

To send a picture, set :attr:`media_url` to the url of the picture you wish to send.

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

