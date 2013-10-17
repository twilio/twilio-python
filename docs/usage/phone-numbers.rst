.. module:: twilio.rest.resources

=================
Phone Numbers
=================

With Twilio you can search and buy real phone numbers, just using the API.

For more information, see the
`IncomingPhoneNumbers REST Resource
<http://www.twilio.com/docs/api/rest/incoming-phone-numbers>`_ documentation.


Searching and Buying a Number
--------------------------------

Finding numbers to buy couldn't be easier.
We first search for a number in area code 530.
Once we find one, we'll purchase it for our account.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    numbers = client.phone_numbers.search(area_code=530)

    if numbers:
        numbers[0].purchase()
    else:
        print "No numbers in 530 available"


Local, Toll Free, and Mobile Numbers
------------------------------------

By default, :meth:`PhoneNumbers.search` looks for local phone numbers. To
search for numbers for a given type, include the desired type in the
:attr:`type` paramter.

Available types are:
- `local`
- `tollfree`
- `mobile`

.. code-block:: python

    # Local
    numbers = client.phone_numbers.search(type="local")

    # Toll Free
    numbers = client.phone_numbers.search(type="tollfree")

    # Mobile
    numbers = client.phone_numbers.search(type="mobile")

Similarly, you can purchase numbers of a given type. You must still include
the :attr:`phone_number` or :attr:`area_code` parameters.

.. code-block:: python

    # Local
    numbers = client.phone_numbers.purchase(type='local', phone_number'(919) 123-4567')

    # Toll Free
    numbers = client.phone_numbers.purchase(type='tollfree', phone_number'(919) 123-4567')

    # Mobile
    numbers = client.phone_numbers.purchase(type='mobile', phone_number'(919) 123-4567')

Numbers Containing Words
^^^^^^^^^^^^^^^^^^^^^^^^^^

Phone number search also supports looking for words inside phone numbers.
The following example will find any phone number with "FOO" in it.

.. code-block:: python

    numbers = client.phone_numbers.search(contains="FOO")

You can use the ''*'' wildcard to match any character. The following example finds any phone number that matches the pattern ''D*D''.

.. code-block:: python

    numbers = client.phone_numbers.search(contains="D*D")


International Numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, the client library will look for US numbers. Set the
:data:`country` keyword to a country code of your choice to search for
international numbers.

.. code-block:: python

    numbers = client.phone_numbers.search(country="FR")


:meth:`PhoneNumbers.search` method has plenty of other options to augment your search :

- :data:`region`: When searching the US, show numbers in this state
- :data:`postal_code`: Only show numbers in this area code
- :data:`rate_center`: US only.
- :data:`near_lat_long`: Find numbers near this latitude and longitude.
- :data:`distance`: Search radius for a Near- query in miles.

The `AvailablePhoneNumbers REST Resource
<http://www.twilio.com/docs/api/rest/available-phone-numbers>`_ documentation
has more information on the various search options.


Buying a Number
---------------

If you've found a phone number you want, you can purchase the number.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    number = client.phone_numbers.purchase(phone_number="+15305431234")

However, it's easier to purchase numbers after finding them using search (as
shown in the first example).


Updating Properties on a Number
-------------------------------

To update the properties on a phone number, call :meth:`update`
on the phone number object, with any of the parameters
listed in the `IncomingPhoneNumbers Resource documentation
<http://www.twilio.com/docs/api/rest/incoming-phone-numbers>`_

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    for number in client.phone_numbers.list(api_version="2010-04-01"):
        number.update(voice_url="http://twimlets.com/holdmusic?" + 
            "Bucket=com.twilio.music.ambient", 
            status_callback="http://example.com/callback")


Changing Applications
----------------------

An :class:`Application` encapsulates all necessary URLs for use with phone numbers. Update an application on a phone number using :meth:`update`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    phone_sid = "PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    number = client.phone_numbers.update(phone_sid, sms_application_sid="AP123")

See :doc:`/usage/applications` for instructions on updating and maintaining Applications.


Validate a Phone Number
-----------------------

See validation instructions here: :doc:`/usage/caller-ids`:

