.. module::twilio.rest

======================================
Accessing Twilio Pricing API Resources
======================================

To access the Twilio Pricing API resources, you'll first need to instantiate
a :class:`TwilioPricingClient`.

Authentication
--------------

The :class:`TwilioPricingClient` needs your Twilio credentials. While these can be
passed in directly to the constructor, we suggest storing your credentials as
environment variables. Why? You'll never have to worry about committing your
credentials and accidentally posting them somewhere public.

The :class:`TwilioPricingClient` looks for :const:`TWILIO_ACCOUNT_SID` and
:const:`TWILIO_AUTH_TOKEN` inside the current environment.

With those two values set, create a new :class:`TwilioPricingClient`.

.. code-block:: python

    from twilio.rest import TwilioPricingClient

    conn = TwilioPricingClient()

If you'd rather not use environment variables, pass your account credentials
directly to the the constructor.

.. code-block:: python

    from twilio.rest import TwilioPricingClient

    ACCOUNT_SID = "AXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"
    client = TwilioPricingClient(ACCOUNT_SID, AUTH_TOKEN)


For more advanced options to use with the :class:`TwilioPricingClient`,
including proxy configuration, see the :doc:`/usage/basics` page.
:class:`TwilioPricingClient` accepts the same options as
:class:`TwilioRestClient`.

=============
Voice Pricing
=============

Twilio Voice pricing is available by country and by phone number.

Voice calls are priced per minute and reflect the current Twilio list price
and any discounts available to the requesting account at the time of the
request.

Voice Countries
---------------

To retrieve a list of countries where Twilio Voice services are available:

.. code-block:: python

    from twilio.rest import TwilioPricingClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioPricingClient(ACCOUNT_SID, AUTH_TOKEN)
    countries = client.voice.countries.list()
    for c in countries:
        print c.iso_country

Note that the returned list of countries will not have actual prices populated.
You will need to retrieve the pricing information for each country you are
interested in individually:

.. code-block:: python

    from twilio.rest import TwilioPricingClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioPricingClient(ACCOUNT_SID, AUTH_TOKEN)
    country = client.voice.countries.get('GB')
    print country.iso_country
    print country.price_unit

    # A list of price rates for inbound calls to each type of Twilio
    # Number available in this country
    for p in country.inbound_call_prices:
        print p.number_type
        print p.call_base_price # Base price per minute
        print p.current_base_price # Price per minute after discounts

    # A list of price rates for outbound calls, organized by number prefixes.
    for p in country.outbound_prefix_prices:
        print p.prefixes # List of one or more prefixes this price applies to
        print p.call_base_price # Base price per minute
        print p.current_base_price # Price per minute after discounts

Voice Numbers
-------------

To retrieve pricing information for Twilio Voice calls to and from a specific
number:

.. code-block:: python

    from twilio.rest import TwilioPricingClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioPricingClient(ACCOUNT_SID, AUTH_TOKEN)
    number = client.voice.numbers.get('+15105551234')

    print number.iso_country
    print number.price_unit
    print number.outbound_call_price.call_base_price
    print number.inbound_call_price.call_base_price # None if the number is not Twilio-hosted

Phone Number Pricing
====================

To retrieve a list of countries where Twilio phone numbers are available:

.. code-block:: python

    from twilio.rest import TwilioPricingClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioPricingClient(ACCOUNT_SID, AUTH_TOKEN)
    countries = client.phone_numbers.countries.list()
    for c in countries:
        print c.iso_country

Note that the country objects in the returned list will not have pricing
information populated; you will need to retrieve the specific information for
each country you are interested in individually:

.. code-block:: python

    from twilio.rest import TwilioPricingClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioPricingClient(ACCOUNT_SID, AUTH_TOKEN)
    country = client.phone_numbers.countries.get('GB')
    print country.price_unit

    for p in country.phone_number_prices:
        print p.type
        print p.base_price
        print p.current_price

