.. module:: twilio.rest.resources

=================
Caller Ids
=================

Validate a Phone Number
-----------------------

Validating a phone number is quick and easy.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    response = client.caller_ids.validate("+44 9876543212")
    print response.validation_code

Twilio will call the provided number and wait for the validation code to be
entered.

