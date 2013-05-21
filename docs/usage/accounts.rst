.. module:: twilio.rest

===========
Accounts
===========

Managing Twilio accounts is straightforward.
Update your own account information or create and manage multiple subaccounts.

For more information, see the
`Account REST Resource <http://www.twilio.com/docs/api/rest/account>`_
documentation.


Updating Account Information
----------------------------

Use the :meth:`Account.update` to modify one of your accounts.
Right now the only valid attribute is `FriendlyName`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    account = client.accounts.get(ACCOUNT_SID)
    account.update(friendly_name="My Awesome Account")


Creating Subaccounts
----------------------

Subaccounts are easy to make.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    subaccount = client.accounts.create(name="My Awesome SubAccount")


Managing Subaccounts
-------------------------

Say you have a subaccount for Client X with an account sid `AC123`

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

    # Client X's subaccount
    subaccount = client.accounts.get('AC123')

Client X hasn't paid you recently, so let's suspend their account.

.. code-block:: python

    subaccount.suspend()

If it was just a misunderstanding, reenable their account.

.. code-block:: python

    subaccount.activate()

Otherwise, close their account permanently.

.. code-block:: python

    subaccount.close()

.. warning::
    This action can't be undone. 

