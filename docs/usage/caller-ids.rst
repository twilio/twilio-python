.. module:: twilio.rest.resources

=================
Caller Ids
=================


Validate a Phone Number
-----------------------

Validating a phone number can be done with the Python helper library.

The code block below provides a simple example.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    response = client.caller_ids.validate("+449876543212")
    print response.validation_code

Twilio will call the provided number and wait for the validation code to be
entered.

Delete a Phone Number
---------------------

Deleting a validated phone number is just as easy as validating.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    account = "ACXXXXXXXXXXXXXXXXX"
    token = "YYYYYYYYYYYYYYYYYY"
    client = TwilioRestClient(account, token)

    response = client.caller_ids.list(phone_number="+15555555555")
    callerid = response[0]
    callerid.delete()
