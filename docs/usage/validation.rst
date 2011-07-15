.. module:: twilio.util

===========================
Validate Incoming Requests
===========================

Twilio requires that your TwiML-serving web server be open to the public. This is necessary so that Twilio can retrieve TwiML from urls and POST data back to your server.

However, there may be people out there trying to spoof the Twilio service. Luckily, there's an easy way to validate that incoming requests are from Twilio and Twilio alone.

An `indepth guide <http://www.twilio.com/docs/security>`_ to our security features can be found in our online documentation.

Before you can validate requests, you'll need four pieces of information

* your Twilio Auth Token
* the POST data for the request
* the requested URL
* the X-Twilio-Signature header value

Get your Auth Token from the `Twilio User Dashboard <https://www.twilio.com/user/account>`_.

Obtaining the other three pieces of information depends on the framework of your choosing. I will assume that you have the POST data as a dictionary and the url and X-Twilio-Signature as strings.

The below example will print out a confirmation message if the request is actually from Twilio.com

.. code-block:: python

    from twilio.util import RequestValidator

    AUTH_TOKEN = 'YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY'

    validator = RequestValidator(AUTH_TOKEN)

    url = "http://www.example.com/request/url"
    post_vars = {}

    signature = "X-Twilio-Signature header value"

    if validator.validate(url, post_vars, signature):
        print "Confirmed to have come from Twilio."
    else:
        print "NOT VALID.  It might have been spoofed!"

Trailing Slashes
==================

If your URL uses an "index" page, such as index.php or index.html to handle the request, such as: https://mycompany.com/twilio where the real page is served from https://mycompany.com/twilio/index.php, then Apache or PHP may rewrite that URL a little bit so it's got a trailing slash... https://mycompany.com/twilio/ for example.

Using the code above, or similar code in another language, you could end up with an incorrect hash because, Twilio built the hash using https://mycompany.com/twilio and you may have built the hash using https://mycompany.com/twilio/.



