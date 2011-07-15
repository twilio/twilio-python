.. module:: twilio.rest

===========
Accounts
===========

Managing Twilio accounts is straightforward. Update your own account information or create and manage multiple subaccounts.

For more information, see the `Account REST Resource <http://www.twilio.com/docs/api/rest/account>`_ documentation.


Updating Account Information
----------------------------

Use the :meth:`Account.update` to modify one of your accounts. Right now the only valid attribute is `FriendlyName`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()
    account = conn.accounts.get()
    account.update(name="My Awesome Account")

Creating Subaccounts
----------------------

Subaccounts are easy to make.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()
    subaccount = conn.accounts.create(name="My Awesome SubAccount")

Managing Subaccounts
-------------------------

Say you have a subaccount for Client X with an account sid `AC123`

.. code-block:: python

    from twilio.rest import TwilioRestClient

    conn = TwilioRestClient()

    # Client X's subaccount
    subaccount = conn.accounts.get('AC123')

Client X hasn't paid you recently, so let's suspend their account.

.. code-block:: python

    subaccount.suspend()

If it was just a misunderstanding, reenable their account.

.. code-block:: python

    subaccount.activate()

Otherwise, close their account permanently.

.. warning::
    This action can't be undone. Be careful

.. code-block:: python

    subaccount.close()





