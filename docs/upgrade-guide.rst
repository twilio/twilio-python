==============
Upgrade Guide
==============

Porting your application from **twilio-python** 2.0 to 3.0 is straightforward.
All the same methods are still offered. Only their location has changed.


Making API Requests
====================

:class:`twilio.Account` has been moved to
:class:`twilio.rest.TwilioRestClient`.
The rest client offers a greatly improved API;
however, the old :meth:`request` method still exists (in a deprecated state).
We suggest you migrate your code to use the new API.

Here is how you would place an outgoing call with the older version.

.. code-block:: python

    import twilio

    # Twilio REST API version
    API_VERSION = '2010-04-01'

    # Twilio AccountSid and AuthToken
    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    # Outgoing Caller ID previously validated with Twilio
    CALLER_ID = 'NNNNNNNNNN';

    # Create a Twilio REST account object using your account ID and token
    account = twilio.Account(ACCOUNT_SID, ACCOUNT_TOKEN)

    d = {
        'From': CALLER_ID,
        'To': '415-555-1212',
        'Url': 'http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient',
    }

    print account.request('/%s/Accounts/%s/Calls' %
                         (API_VERSION, ACCOUNT_SID), 'POST', d)

The same code, updated to work with the new version
(albeit using deprecated methods).

.. code-block:: python

    from twilio.rest import TwilioRestClient

    API_VERSION = '2010-04-01'
    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'
    CALLER_ID = 'NNNNNNNNNN';

    client = TwilioRestClient(ACCOUNT_SID, ACCOUNT_TOKEN)

    d = {
        'From': CALLER_ID,
        'To': '415-555-1212',
        'Url': 'http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient',
    }

    print client.request('/%s/Accounts/%s/Calls' %
                        (API_VERSION, ACCOUNT_SID), 'POST', d)

A final version using the new interface.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    client = TwilioRestClient(ACCOUNT_SID, ACCOUNT_TOKEN)
    call = client.calls.create(from_='NNNNNNNNNN', to='415-555-1212',
        url='http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient')

    print call


Generating TwiML
=================

:class:`Response` has moved into the :mod:`twiml` module. The `add*` methods
have also been deprecated in favor of method names without the 'add' prefix (as
shown below).

Here is how you would craft a response using the old library.

.. code-block:: python

    import twilio

    r = twilio.Response()
    r.addSay("Hello World", voice=twilio.Say.MAN, language=twilio.Say.FRENCH,
             loop=10)
    r.addDial("4155551212", timeLimit=45)
    r.addPlay("https://api.twilio.com/cowbell.mp3")
    print r

To use the new version, just change the import at the top.

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()
    r.addSay("Hello World", voice=twiml.Say.MAN, language=twiml.Say.FRENCH,
             loop=10)
    r.addDial("4155551212", timeLimit=45)
    r.addPlay("https://api.twilio.com/cowbell.mp3")
    print str(r)

The add methods are deprecated and undocumented, so please change them to the
new methods. For example, `r.addSay` would become `r.say`.

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()

    r.say("Hello World", voice=twiml.Say.MAN, language=twiml.Say.FRENCH,
             loop=10)
    r.dial("4155551212", timeLimit=45)
    r.play("https://api.twilio.com/cowbell.mp3")

    print str(r)


Checking Signatures
=====================

The :class:`Utils` class has been renamed to :class:`TwilioValidation` in the
:mod:`twilio.util` module and the :meth:`validateRequest` method has been
renamed :meth:`validate`.

A sample using the old version of **twilio-python**.

.. code-block:: python

    import twilio

    ACCOUNT_SID = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    utils = twilio.Utils(ACCOUNT_SID, ACCOUNT_TOKEN)

    # the callback URL you provided to Twilio for the phone number/app
    url = "http://UUUUUUUUUUUUUUUUUU"

    the POST variables attached to the request (e.g. "From", "To")
    post_vars = {}

    # X-Twilio-Signature header value
    signature = "HpS7PBa1Agvt4OtO+wZp75IuQa0=" # will look something like that

    if utils.validateRequest(url, post_vars, signature):
        print "was confirmed to have come from Twilio."
    else:
        print "was NOT VALID.  It might have been spoofed!"

The same sample, converted to use the new version.

.. code-block:: python

    from twilio import util

    ACCOUNT_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    utils = util.RequestValidator(ACCOUNT_TOKEN)

    # the callback URL you provided to Twilio
    url = "http://www.example.com/my/callback/url.xml"

    # the POST variables attached to the request (eg "From", "To")
    post_vars = {}

    # X-Twilio-Signature header value
    signature = "HpS7PBa1Agvt4OtO+wZp75IuQa0=" # will look something like that

    if utils.validate(url, post_vars, signature):
        print "was confirmed to have come from Twilio."
    else:
        print "was NOT VALID.  It might have been spoofed!"

