.. module:: twilio.rest.resources

====================
Notifications
====================

A :class:`Notification` resource represents a single log entry made by Twilio in the course of handling your calls or your use of the REST API.
For more information, see the `Notifications REST Resource
<http://www.twilio.com/docs/api/rest/notification>`_ documentation.


Listing Your Notifications
----------------------------

The following code will print out additional information about each of your
current :class:`Notification` resources.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for notification in client.notifications.list():
        print notification.more_info

You can filter transcriptions by :attr:`log` and :attr:`message_date`.
The :attr:`log` value is 0 for `ERROR` and 1 for `WARNING`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    ERROR = 0

    for notification in client.notifications.list(log=ERROR):
        print notification.error_code

.. note:: Due to the potentially voluminous amount of data in a notification,
    the full HTTP request and response data is only returned in the
    :class:`Notification` instance resource representation.


Deleting Notifications
------------------------

Your account can sometimes generate an inordinate amount of
:class:`Notification` resources. The :class:`Notifications` resource allows
you to delete unnecessary notifications.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.notifications.delete("NO123")

