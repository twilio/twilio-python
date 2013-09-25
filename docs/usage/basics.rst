.. module:: twilio.rest

=========================
Accessing REST Resources
=========================

To access Twilio REST resources, you'll first need to instantiate a
:class:`TwilioRestClient`.

Authentication
--------------------------

The :class:`TwilioRestClient` needs your Twilio credentials. While these can be
passed in directly to the constructor, we suggest storing your credentials as
environment variables. Why? You'll never have to worry about committing your
credentials and accidentally posting them somewhere public.

The :class:`TwilioRestClient` looks for :const:`TWILIO_ACCOUNT_SID` and
:const:`TWILIO_AUTH_TOKEN` inside the current environment.

With those two values set, create a new :class:`TwilioRestClient`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()

If you'd rather not use environment variables, pass your account credentials
directly to the the constructor.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    ACCOUNT_SID = "AXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)


Proxies
-------

:class:`TwilioRestClient` supports HTTP and SOCKS4/5 proxies. You can change
the proxy configuration at any time with the :class:`Connection` class:

.. code-block:: python

    from twilio.rest.resources import Connection
    from twilio.rest.resources.connection import PROXY_TYPE_SOCKS5

    Connection.set_proxy_info(
        'example.com',
        5000,
        proxy_type=PROXY_TYPE_SOCKS5,
        proxy_user='username',
        proxy_pass='password',
    )

The :class:`TwilioRestClient` will retrieve and use the current proxy
information for each request.


Listing Resources
-------------------

The :class:`TwilioRestClient` gives you access to various list resources.
:meth:`ListResource.list <twilio.rest.resources.ListResource.list>`, by default,
returns the most recent 50 instance resources.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    resources = client.calls.list()

:meth:`resource.ListResource.list` accepts paging arguments.
The following will return page 3 with page size of 25.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    resources = client.calls.list(page=3, page_size=25)


Listing All Resources
^^^^^^^^^^^^^^^^^^^^^^^

Sometimes you'd like to retrieve all records from a list resource.
Instead of manually paging over the resource,
the :class:`resources.ListResource.iter` method returns a generator.
After exhausting the current page,
the generator will request the next page of results.

.. warning:: Accessing all your records can be slow. We suggest only doing so when you absolutely need all the records.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for number in client.phone_numbers.iter():
        print number.friendly_name


Get an Individual Resource
-----------------------------

To get an individual instance resource, use
:meth:`resources.ListResource.get`.
Provide the :attr:`sid` of the resource you'd like to get.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    call = client.calls.get("CA123")
    print call.to

