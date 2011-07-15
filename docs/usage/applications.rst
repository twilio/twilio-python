.. module:: twilio.rest.resources

=================
Applications
=================

An application inside of Twilio is just a set of URLs and other configuration data that tells Twilio how to behave when one of your Twilio numbers receives a call or SMS message.

For more information, see the `Application REST Resource <http://www.twilio.com/docs/api/rest/applications>`_ documentation.

Listing Your Applications
--------------------------

The following code will print out the :attr:`friendly_name` for each :class:`Application`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()
    for app in conn.applications.list():
        print app.friendly_name


Filtering Applications
---------------------------

You can filter applications by FriendlyName

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()
    for app in conn.applications.list(friendly_name="FOO"):
        print app.sid

Creating an Application
-------------------------

When creating an application, no fields are required. We create an application with only a :attr:`friendly_name`. :meth:`Applications.create()` accepts many other arguments for url configuration.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()
    application = conn.applications.create(friendly_name="My New App")


Updating an Application
------------------------

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()
    url = "http://www.example.com/twiml.xml"
    application = conn.applications.update(app_sid, voice_url=url)


Deleting an Application
-------------------------

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()
    conn.applications.delete(app_sid)
