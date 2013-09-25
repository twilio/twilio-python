Usage API
=========

Usage Records
-------------
You can query your :class:`UsageRecords` to see the activity
of your Twilio account. Here we'll make a query for the activity
over the last day.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    
    todays_usage = client.usage.records.today
    for category in todays_usage:
        print '{}: {}'.format(category.description, category.price)

This will print out the amount spent for each usage category over the
last day. To see all of the possible usage categories, as well as all of the 
possible time ranges to query over, check out the [REST API UsageRecord docs](https://www.twilio.com/docs/api/rest/usage-records#usage-all-categories).


Usage Triggers
--------------
You can also set up a :class:`UsageTrigger`. :class:`UsageTriggers` notify
you once your usage reaches a certain level. Here we'll set up a :class:`UsageTrigger`
to tell us when we've sent 1000 total messages.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    
    trigger = client.usage.triggers.create(
        friendly_name="1000 messages",
        usage_category="sms",
        trigger_value="1000",
        callback_url="http://example.com/thousand-sms",
        trigger_by="count"
    )

Once this trigger is created, Twilio will make a POST to "http://example.com/thousand-sms"
once your account has sent 1000 messages.

Relative Triggers
-----------------

The previous example is helpful, but it is an example of an *absolute* trigger value.
What if your account has already sent 1000 messages, and you want to be notified once
it sends the next 1000, regardless of how many you've previously sent? To do this,
you must add a '+' in front of the :attr:`trigger_value`, so Twilio knows this is a
relative count. Here's an example that shows how to set a relative trigger.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    
    trigger = client.usage.triggers.create(
        friendly_name="1000 messages",
        usage_category="sms",
        trigger_value="+1000",
        callback_url="http://example.com/thousand-sms",
        trigger_by="count"
    )

Once this trigger is created, Twilio will make a POST to "http://example.com/thousand-sms"
once your account has sent 1000 more messages.
