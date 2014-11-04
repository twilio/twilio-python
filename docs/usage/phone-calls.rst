.. module:: twilio.rest.resources

=====================
Phone Calls
=====================

The :class:`Calls` resource manages all interaction with Twilio phone calls,
including the creation and termination of phone calls. For more information, see the `Calls REST Resource <http://www.twilio.com/docs/api/rest/call>`_
documentation.


Making a Phone Call
-------------------

The :class:`Calls` resource allows you to make outgoing calls. Before a call
can be successfully started, you'll need a to set up a url endpoint which
outputs valid `TwiML <http://www.twilio.com/docs/api/twiml/>`_. This can be done with the :class: `twiml.Response` class, `get started here <http://twilio-python.readthedocs.org/en/latest/usage/twiml.html#twiml-creation>`_.

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


Retrieve a Call Record
-------------------------

If you already have a :class:`Call` sid,
you can use the client to retrieve that record.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    sid = "CA12341234"
    call = client.calls.get(sid)



Delete a Call Record
--------------------

You can delete your :class:`Call` resources from Twilio's storage
to protect your users' privacy and/or comply with legal requirements.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    sid = "CA12341234"
    client.calls.delete(sid)

Accessing Specific Call Resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each :class:`Call` resource also has access to its ``notifications``,
``recordings``, and ``transcriptions``. These attributes are
:class:`ListResources <ListResource>`, just like the :class:`Calls` resource
itself.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    sid = "CA12341234"
    call = client.calls.get(sid)

    print call.notifications.list()
    print call.recordings.list()
    print call.transcriptions.list()

However, what if you only have a ``call_sid``, and not the actual
:class:`Resource <InstanceResource>`? No worries, as :meth:`Calls.list` can be
filtered based on a given ``call_sid``.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    sid = "CA24234"
    print client.notifications.list(call=sid)
    print client.recordings.list(call=sid)
    print client.transcriptions.list(call=sid)


Modifying Live Calls
--------------------

The :class:`Call` resource makes it easy to find current live calls and
redirect them as necessary

.. code-block:: python

    from twilio.rest import TwilioRestClient
    from twilio.rest.resources import Call

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    calls = client.calls.list(status=Call.IN_PROGRESS)
    for c in calls:
        c.route(
            "http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient",
            method="POST"
        )

Ending all live calls is also possible

.. code-block:: python

    from twilio.rest import TwilioRestClient
    from twilio.rest.resources import Call

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    calls = client.calls.list(status=Call.IN_PROGRESS)
    for c in calls:
        c.hangup()

Note that :meth:`~Call.hangup` will also cancel calls currently queued.

If you already have a :class:`Call` sid, you can use the :class:`Calls`
resource to update the record without having to use :meth:`~Calls.get` first.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    sid = "CA12341234"
    client.calls.update(sid, method="POST",
        url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

Hanging up the call also works.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    sid = "CA12341234"
    client.calls.hangup(sid)

