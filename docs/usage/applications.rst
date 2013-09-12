.. module:: twilio.rest.resources

=================
Applications
=================

An application inside of Twilio is just a set of URLs and other configuration
data that tells Twilio how to behave when one of your Twilio numbers receives
a call or message.

For more information, see the `Application REST Resource
<http://www.twilio.com/docs/api/rest/applications>`_ documentation.


Listing Your Applications
--------------------------

The following code will print out the :attr:`friendly_name` for each :class:`Application`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for app in client.applications.list():
        print app.friendly_name


Filtering Applications
---------------------------

You can filter applications by FriendlyName

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for app in client.applications.list(friendly_name="FOO"):
        print app.sid


Creating an Application
-------------------------

When creating an application, no fields are required. We create an application
with only a :attr:`friendly_name`. The :meth:`Applications.create()` method
accepts many other arguments for url configuration.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    application = client.applications.create(friendly_name="My New App")


Updating an Application
------------------------

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    url = "http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient"
    app_sid = 'AP123' # the app you'd like to update
    application = client.applications.update(app_sid, voice_url=url)


Deleting an Application
-------------------------

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    app_sid = 'AP123' # the app you'd like to delete
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.applications.delete(app_sid)

