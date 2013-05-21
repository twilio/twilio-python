==========================
Frequently Asked Questions
==========================

Hopefully you can find an answer here to one of your questions. If not, please
contact `help@twilio.com <mailto:help@twilio.com>`_.


ImportError messages
--------------------

If you get an error that looks like this:

.. code-block:: python

    Traceback (most recent call last):
      File "twilio.py", line 1, in <module>
        from twilio.rest import TwilioRestClient
      File "/.../twilio-python/docs/twilio.py", line 1, in <module>
        from twilio.rest import TwilioRestClient
    ImportError: No module named rest

Check to make sure that you don't have a file named ``twilio.py``;
Python will try to load the Twilio library from your ``twilio.py`` file
instead of from the Twilio library.

If you get an error that looks like this:

.. code-block:: python

    Traceback (most recent call last):
      File "test.py", line 1, in <module>
        import twilio.rest
    ImportError: No module named twilio.rest

Your Python installation cannot find the library.

Check which versions of ``pip`` and Python you are running with this command in
the Terminal:

.. code-block:: bash

    which -a python
    which -a pip

``pip`` needs to install the Twilio library to a path that your Python
executable can read from. Sometimes there will be more than one version of pip,
like pip-2.5, pip-2.7 etc. You can find all of them by running ``compgen -c |
grep pip`` (works with Bash on \*nix machines). There can also be more than one
version of Python, especially if you have Macports or homebrew.

You also may be using an outdated version of the twilio-python library, which
did not use a ``twilio.rest.TwilioRestClient`` object. Check which version of
the twilio library you have installed by running this command:

.. code-block:: bash

    $ pip freeze | grep twilio          # Or pip-2.7 freeze etc.

The latest version (as of January 2012) is 3.3. If you are running an outdated
version, you can upgrade with this command:

.. code-block:: bash

    $ pip install --upgrade twilio

Note that if you have code that uses the older version of the library, it may
break when you upgrade your site.


Formatting phone numbers
------------------------

Twilio always returns phone numbers that are formatted in the `E.164 format
<http://en.wikipedia.org/wiki/E.164>`_, like this: ``+12125551234``. However
your users may enter them like this: ``(212) 555-1234``. This can lead to
problems when, for example, Twilio makes a POST request to your server with the
``From`` phone number as ``+12125551234``, but you stored the phone number in
your database as ``(212) 555-1234``, causing a database lookup to fail.

We suggest that you convert the number to E.164 format
before you store it in the database. The `phonenumbers
<https://github.com/daviddrysdale/python-phonenumbers>`_ library is excellent
for this purpose. Install it like this:

.. code-block:: bash

    $ pip install phonenumbers

Then you can convert user input to phone numbers like this:

.. code-block:: python

    import phonenumbers

    def convert_to_e164(raw_phone):
        if not raw_phone:
            return

        if raw_phone[0] == '+':
            # Phone number may already be in E.164 format.
            parse_type = None
        else:
            # If no country code information present, assume it's a US number
            parse_type = "US"

        phone_representation = phonenumbers.parse(raw_phone, parse_type)
        return phonenumbers.format_number(phone_representation,
            phonenumbers.PhoneNumberFormat.E164)

    print convert_to_e164('212 555 1234')   # prints +12125551234

