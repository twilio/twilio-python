.. module:: twilio.util

===========================
Generate Capability Tokens
===========================

`Twilio Client <http://www.twilio.com/api/client>`_ allows you to make and
receive connections in the browser.
You can place a call to a phone on the PSTN network,
all without leaving your browser. See the `Twilio Client Quickstart
<http:/www.twilio.com/docs/quickstart/client>`_ to get up and running with
Twilio Client.

Capability tokens are used by `Twilio Client
<http://www.twilio.com/api/client>`_ to provide connection
security and authorization. The `Capability Token documentation
<http://www.twilio.com/docs/tokens>`_ explains in depth the purpose and
features of these tokens.

:class:`TwilioCapability` is responsible for the creation of these capability
tokens. You'll need your Twilio AccountSid and AuthToken.

.. code-block:: python

    from twilio.util import TwilioCapability

    # Find these values at twilio.com/user/account
    account_sid = "AC123123"
    auth_token = "secret"

    capability = TwilioCapability(account_sid, auth_token)


Allow Incoming Connections
==============================

Before a device running `Twilio Client <http://www.twilio.com/api/client>`_
can recieve incoming connections, the instance must first register a name
(such as "Alice" or "Bob").
The :meth:`allow_client_incoming` method adds the client name to the
capability token.

.. code-block:: python

    capability.allow_client_incoming("Alice")


Allow Outgoing Connections
==============================

To make an outgoing connection from a
`Twilio Client <http://www.twilio.com/api/client>`_ device,
you'll need to choose a
`Twilio Application <http://www.twilio.com/docs/api/rest/applications>`_
to handle TwiML URLs. A Twilio Application is a collection of URLs responsible
for outputting valid TwiML to control phone calls and SMS.

.. code-block:: python

    # Twilio Application Sid
    application_sid = "APabe7650f654fc34655fc81ae71caa3ff"
    capability.allow_client_outgoing(application_sid)


Generate a Token
==================

.. code-block:: python

    token = capability.generate()

By default, this token will expire in one hour. If you'd like to change the
token expiration, :meth:`generate` takes an optional :attr:`expires` argument.

.. code-block:: python

    token = capability.generate(expires=600)

This token will now expire in 10 minutes. If you haven't guessed already,
:attr:`expires` is expressed in seconds.

