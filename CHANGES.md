twilio-python Changelog
=======================

Here you can see the full list of changes between each twilio-python release.

[2017-06-27] Version 6.4.2
--------------------------

- Pin PyJWT to below version `1.5.1` to fix broken build.
- Fix json load error for python 3.3 - 3.5

[2017-06-16] Version 6.4.1
--------------------------

- Add several missing `<Gather>` attributes.
    - `partial_result_callback`
    - `partial_result_callback_method`
    - `language`
    - `hints`
    - `barge_in`
    - `acknowledge_sound_url`
    - `input`
- Remove client-side max page size validation.
- Support `announce_url` and `announce_url_method` on Conference Participants.
- TwiML docstring corrections.

[2017-06-15] Version 6.4.0
--------------------------

- Remove support for Python 2.6.
- Add `locality` field to `AvailablePhoneNumbers`.
- Add `origin` field to `IncomingPhoneNumbers`.
- Add `in_locality` parameter to `AvailablePhoneNumbers`.
- Add `origin` parameter to `IncomingPhoneNumbers`.
- Add new sync categories to `UsageRecords`.
- Support unicode in `validation_client`.
- Add `muted` parameter to `<Conference>` Twiml.

[2017-05-24] Version 6.3.0
--------------------------

- Rename RoomList to RoomRecordingsList.

[2017-05-19] Version 6.2.0
--------------------------

- Add video domain.
- Update usage record categories.
- Add `get_page` method for reentrant paging.

[2017-05-12] Version 6.1.2
----------------------------------

- Allow *kwargs in TwiML Gather

[2017-05-10] Version 6.1.1
----------------------------------

- Add Task verb to VoiceResponse
- Add Echo verb to VoiceResponse
- Add Sim verb to VoiceResponse

[2017-04-27] Version 6.1.0
--------------------------

- Add v2 of chat.twilio.com.
- Add `recording_channels` parameter to Participant create and update.
- Add `recording_status_callback` parameter to Participant create and update.
- Add `recording_status_callback_method` parameter to Participant create and update.
- Add `sip_auth_username` parameter to Participant create and update.
- Add `region` parameter to Participant create and update.
- Add `conference_recording_status_callback` parameter to Participant create and update.
- Add `conference_recording_status_callback_method` parameter to Participant create and update.
- Add `validity_period` parameter to Messages.

[2017-04-03] Version 6.0.0
--------------------------
**New Major Version**

The newest version of the `twilio-python` helper library!

This version brings a host of changes to update and modernize the `twilio-python` helper library. It is auto-generated to produce a more consistent and correct product.

- [Full API Documentation](https://twilio.github.io/twilio-python/)
- [General Documentation](https://www.twilio.com/docs/libraries/python)

Version 4.4.0
-------------

Released May 19, 2015:

- Add support for the beta field to IncomingPhoneNumbers and AvailablePhoneNumbers

Version 4.3.0
-------------

Released May 14, 2015:

- Add support for Call Status Events in TwiML

Version 4.2.0
-------------

Released May 7, 2015:

- Add support for the Twilio Monitor APIs: Events and Alerts

Version 4.1.0
-------------

Released May 6, 2015:

- Add support for the Twilio Pricing API

Version 4.0.0
-------------

Released April 16, 2015:

- Remove the deprecated count function from ListResource

Version 3.8.0
-------------

Released March 31, 2015:

- Support for the new Twilio Lookups API

Version 3.7.3
-------------

Released March 10, 2015:

- Add missing docstrings and examples for TaskRouter

Version 3.7.2
-------------

Released February 24, 2015:

- Restore Tokens resource to TwilioRestClient

Version 3.7.1
-------------

Released February 20, 2015:

- Restore Python 2.6 and 3.x support

Version 3.7.0
-------------

Released February 18, 2015:

- Add TaskRouterClient and resources to support the new TaskRouter API
- Stop prepending numeric error code to exception error messages

Version 3.6.15
--------------

Released January 14, 2015

- Update request construction for Tokens

Version 3.6.14
--------------

Released December 22, 2014

- Specify Python 3 dependencies in wheel package

Version 3.6.12
--------------

Released November 24, 2014

- Fix compatibility issue for Python 3.4

Version 3.6.11
--------------

Released November 21, 2014

- Add support for the new Tokens endpoint

Version 3.6.10
--------------

Released November 13, 2014

- Add support for DELETE to Call and Message records
- Add support for redacting Message body fields

Version 3.6.9
-------------

Released October 30, 2014

- Add Python 3.4 support
- Add wheel packaging
- Fix compatibility with earlier Python 2 releases

Version 3.6.8
-------------

Released October 9, 2014

- Remove unneeded unittest2py3k dependency.
- Restore backwards-compatible exception import paths.

Version 3.6.7
-------------

Released August 6, 2014

- Fix Python 2.5 compatibility.
- Add CallFeedback resources.
- Typo fixes and formatting cleanup.
- Refactor exception hierarchy and imports.
- Documentation improvements.

Version 3.6.6
--------------

Released on February 27, 2014

- Previously the error message was set based on the `tty` value; instead now we
  detect `tty` when you try to print the error message. The `msg` property of
  the exception is set to a decent value.
- `twilio-python` now uses entirely relative imports, so it may be easier to
  include it as a part of another package.

Version 3.6.5
--------------

- Remove unittest2 dependency.
- Tests no longer run against Python 2.5.
- update(), delete() work on Application, Transcription and UsageTrigger
  instance classes.

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

- Adds support for filtering for mobile numbers to both IncomingPhoneNumbers
  and AvailablePhoneNumbers.


Version 3.6.2
-------------

Released on September 24, 2013

- Adds support for HTTP and SOCKS4/5 proxies to the REST client.


Version 3.6.0, 3.6.1
--------------------

Released on September 18, 2013

- Adds support for the new Message and SIP resources to the REST API client.
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
