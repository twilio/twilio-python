twilio-python Changelog
=======================

Here you can see the full list of changes between each twilio-python release.

Version 3.6.4
-------------

Released November 5, 2013

- Adds support for the 'digits' attribute of Play verbs in TwiML creation.
- Updates documentation for Message TwiML verb
- Bugfix for tty detection in error formatting

Version 3.6.3
-------------

Released October 21, 2013

- Adds support for filtering by type to IncomingPhoneNumbers.
- Adds support for filtering for mobile numbers to both
IncomingPhoneNumbers and AvailablePhoneNumbers.


Version 3.6.2
------------

Released on September 24, 2013

- Adds support for HTTP and SOCKS4/5 proxies to the REST client.


Version 3.6.0, 3.6.1
--------------------

Released on September 18, 2013

- Adds support for the new Message and SIP resources to the REST
API client.
- Adds support for the new Message verb to the TwiML generator.


Version 3.5.3, 3.5.4
--------------------

Released on September 6, 2013

- twilio-python now includes an SSL certfication file to ensure that
connections to api.twilio.com don't fail with SSLError.

Version 3.5.2
-------------

Released on August 26, 2013

- You can now delete transcriptions

Version 3.5.1
-------------

Released on May 21, 2013

- Fixes an issue in the 3.5.0 release where null dates would cause the library
  to raise a TypeError.

Version 3.5.0
-------------

Released on May 21, 2013

- `date_created` and `date_updated` objects are now returned as Python
  `datetime.datetime` objects instead of as RFC 2822 formatted strings. This is
  a backwards incompatible change. (via [@abrinsmead](/abrinsmead))
- The library will not throw a UnicodeDecodeError when parsing API responses
  with Python 3.
- You can pass integers to Twiml arguments. (via [@jvankoten](/jvankoten))
- Ensuring the tests always pass on Python 3. (via [@ftobia](/ftobia))
- Add the list of AUTHORS
- Fixes a timing attack vector in signature validation. (via [@zacharyvoase](/zacharyvoase))

Version 3.4.5
-------------

Released on April 1, 2013

Allow the Account object to access usage records and usage trigger data, in
addition to the client. Reporter: Trenton McManus

Version 3.4.4
-------------

Adds support for Sip

Version 3.4.3
-------------

Adds correct dependencies to the `setup.py` file.

Version 3.4.2
-------------

Released on January 2, 2013

Adds a convenience function to retrieve the members of a queue by running
client.members("QU123").

Version 3.4.1
-------------

Python3 support!

Version 3.3.11
--------------

- Fix a bug where participants could not be kicked from a Conference


Version 3.3.10
--------------

- Add support for Queue. Fix a bug where the library wouldn't work in Python 2.5


Version 3.3.9
-------------

- Fix an error introduced in 3.3.7 that prevented validation calls from
  succeeding.

Version 3.3.8
-------------

- Use next_page_uri when iterating over a list resource


Version 3.3.7
-------------

- Allow arbitrary keyword arguments on resource creation and listing

Version 3.3.6
-------------

- Remove doc/tmp directory which was preventing installation on certain Windows machines
- Add Travis CI integration
- Update httplib2 dependency

Version 3.3.5
-------------

Released on January 18, 2011

- Fix a bug with the deprecated `TwilioRestClient.request` method
- Fix a bug in filtering SMS messages by DateSent

Version 3.3.4
-------------

Released on December 16, 2011

- Allow both unicode strings and encoded byte strings in request data
- Add support for SMS and Voice application sids to phone number updating
- Fix documentation error relating to phone number purchasing
- Include doc string information for decorated functions

Version 3.3.3
-------------

Released on November 3, 2011

- Support unicode characters when validating requests
- Add support for Great Britain language on the Say verb
- Set Sms Application, Voice Application, and/or a Friendly
  Name when purchasing a number
- Add missing parameters for resource creation and update

Version 3.3.2
-------------

Released on September 29, 2011

- TwiML verbs can now be used as context managers

Version 3.3.1
-------------

Released on September 27, 2011

- Allow phone numbers to be transferred between accounts and subaccounts

Version 3.3.0
-------------

Released on September 21, 2011

- Add support for Twilio Connect. Connect applications and authorized Connect
  applications are now availble via the REST client.
- Fix a problem where date and datetimes weren't coverted to strings when
  querying list resources
