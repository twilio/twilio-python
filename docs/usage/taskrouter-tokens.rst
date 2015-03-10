.. module:: twilio.task_router

============================
TaskRouter Capability Tokens
============================


TaskRouter's Worker.js library lets you add `TaskRouter
<https://www.twilio.com/docs/taskrouter>`_ Worker Activity controls
and event notifications to your web applications. Worker.js uses a Websocket
connection to TaskRouter to receive realtime notifications of Worker
Reservations and Task details, and provides a simple API for modifying a
Worker's current Activity.

TaskRouter uses Twilio capability tokens to delegate scoped access to
TaskRouter resources to your JavaScript application. Twilio capability tokens
conform to the JSON Web Token (commonly referred to as a JWT and pronounced
"jot") standard, which allow for limited-time use of credentials by a third
party. Your web server needs to generate a Twilio capability token and provide
it to your JavaScript application in order to register a TaskRouter worker.

:class:`TaskRouterCapability` is responsible for the creation of these
capability tokens. You'll need your Twilio AccountSid and AuthToken,
the Sid of the Workspace you want to authorize access to, and the Sid
of the Worker you're granting authorization for.

.. code-block:: python

    from twilio.task_router import TaskRouterCapability

    # Get these values from https://twilio.com/user/account
    account_sid = "AC123"
    auth_token = "secret"

    # Create a Workspace and Worker in the TaskRouter account portal
    # or through the TaskRouter API
    workspace_sid = "WS456"
    worker_sid = "WK789"

    capability = TaskRouterCapability(account_sid, auth_token,
                                      workspace_sid, worker_sid)

By default, the Capability object will allow the Worker.js process to
read from and write to the websockets used to communicate events, and also
to fetch the list of available activities in the workspace.

There are three additional permissions you can grant using the Capability
token, and in most cases you'll want to allow all of them for your application:


Attribute Fetch
===============

This authorizes requests to retrieve the registered Worker's attributes from
the TaskRouter API.

.. code-block:: python

    capability.allow_worker_fetch_attributes()


Worker Activity Update
======================

This authorizes updates to the registered Worker's current Activity.

.. code-block:: python

    capability.allow_worker_activity_updates()


Task Reservation Update
=======================

This authorizes updates to a Task's reservation status.

.. code-block:: python

    capability.allow_task_reservation_updates()


Generate a Token
================

.. code-block:: python

    token = capability.generate_token()

By default, this token will expire in one hour. If you'd like to change the
token expiration, :meth:`generate_token` takes an optional :attr:`ttl`
argument.

.. code-block:: python

    token = capability.generate_token(ttl=600)

This token will now expire in 10 minutes. If you haven't guessed already,
:attr:`ttl` is expressed in seconds.






