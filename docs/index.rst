====================
Twilio Python
====================

Make requests to Twilio's `REST API <http://www.twilio.com/docs/api/twiml/>`_ and create `TwiML <http://www.twilio.com/docs/api/twiml/>`_ without a hassle. And you thought Twilio couldn't get any easier.

.. _installation:

Installation
================

.. code-block:: bash

    $ pip install twilio

You can also `download the source <https://github.com/twilio/twilio-python/zipball/master>`_ and install by downloading :data:`setuptools`, navigating in the Terminal to the folder containing the **twilio-python** library, and then running:

.. code-block:: bash

    $ python setup.py install

Getting Started
================

The :doc:`/getting-started` will get you up and running in a few quick minutes. This guide assumes you understand the core concepts of Twilio. If you've never used Twilio before, don't fret! Just read `about how Twilio works <http://www.twilio.com/api/>`_ and then jump in.

.. _user-guide:

User Guide
==================

Functionality is split over three different sub-packages within **twilio-python**. Below are in-depth guide to specific portions of the library.

REST API
----------

Query the Twilio REST API to create phone calls, send SMS messages and so much more

.. toctree::
    :maxdepth: 1

    usage/basics
    usage/phone-calls
    usage/phone-numbers
    usage/messages
    usage/accounts
    usage/conferences
    usage/applications
    usage/notifications
    usage/recordings
    usage/transcriptions

TwiML
---------

Generates valid TwiML for controlling and manipulating phone calls.

.. toctree::
    :maxdepth: 2

    usage/twiml

Utilites
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

Support and Development
==========================
All development occurs over on `Github <https://github.com/twilio/twilio-python>`_. To checkout the source,

.. code-block:: bash

    $ git clone git@github.com:twilio/twilio-python.git


Report bugs using the Github `issue tracker <https://github.com/twilio/twilio-python/issues>`_.

If you have questions that aren't answered by this documentation, ask the `#twilio IRC channel <irc://irc.freenode.net/#twilio>`_

See the :doc:`/changelog` for version history.
