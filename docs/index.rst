=============================
Twilio Python Helper Library
=============================

.. _installation:

Installation
================

Install from PyPi using `pip <http://www.pip-installer.org/en/latest/>`_, a
package manager for Python.

.. code-block:: bash

    pip install twilio

Don't have pip installed? Try installing it, by running this from the command
line:

.. code-block:: bash

    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, install the library by downloading
`the source <https://github.com/twilio/twilio-python/zipball/master>`_,
installing `setuptools <http://pythonhosted.org/setuptools/>`_,
navigating in the Terminal to the folder containing the **twilio-python**
library, and then running:

.. code-block:: bash

    python setup.py install


Getting Started
================

The :doc:`/getting-started` will get you up and running in a few quick minutes.
This guide assumes you understand the core concepts of Twilio.
If you've never used Twilio before, don't fret! Just read
`about how Twilio works <http://www.twilio.com/api/>`_ and then jump in!


.. _user-guide:

User Guide
==================

Functionality is split over three different sub-packages within
**twilio-python**. Below are in-depth guides to specific portions of the
library.


REST API
----------

Query the Twilio REST API to create phone calls, send messages and more!

.. toctree::
    :maxdepth: 1

    usage/basics
    usage/messages
    usage/phone-calls
    usage/phone-numbers
    usage/accounts
    usage/conferences
    usage/applications
    usage/notifications
    usage/recordings
    usage/transcriptions
    usage/usage
    usage/caller-ids
    usage/queues
    usage/sip


TaskRouter
---------

Query the Twilio TaskRouter API to set up workspaces and task routing, and
create capability tokens to authorize your client-side code to safely update
state.

.. toctree::
    :maxdepth: 1

    usage/taskrouter
    usage/taskrouter-tokens


TwiML
---------

Generates valid TwiML for controlling and manipulating phone calls.

.. toctree::
    :maxdepth: 2

    usage/twiml


Utilities
----------

Small functions useful for validating requests are coming from Twilio

.. toctree::
    :maxdepth: 1

    usage/validation
    usage/token-generation


Upgrade Plan
==================

`twilio-python` 3.0 introduced backwards-incompatible changes to the API. See
the :doc:`/upgrade-guide` for step-by-step instructions for migrating to 3.0.
In many cases, the same methods are still offered, just in different locations.


API Reference
==================

A complete guide to all public APIs found in `twilio-python`. Auto-generated,
so only use when you really need to dive deep into the library.

.. toctree::
    :maxdepth: 2

    api


Deploying to Google App Engine
==============================

Want to run your app on Google App Engine? We've got a full guide to getting
started here:

.. toctree::
    :maxdepth: 1

    appengine

Frequently Asked Questions
==========================

What to do if you get an ``ImportError``, and some advice about how to format
phone numbers.

.. toctree::
    :maxdepth: 2

    faq

Changelog
=========

See the :doc:`/changelog` for version history.


Support and Development
==========================
All development occurs over on
`Github <https://github.com/twilio/twilio-python>`_. To checkout the source,

.. code-block:: bash

    git clone git@github.com:twilio/twilio-python.git


Report bugs using the Github
`issue tracker <https://github.com/twilio/twilio-python/issues>`_.

If you have questions that aren't answered by this documentation,
ask the `#twilio IRC channel <irc://irc.freenode.net/#twilio>`_
