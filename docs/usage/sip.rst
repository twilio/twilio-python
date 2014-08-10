=============
Sip In
=============

Getting started with Sip
==========================

Connect your SIP endpoints to Twilio and start building voice apps with Twilio’s APIs and application stack. If you're unfamiliar with SIP, please see the `SIP API Documentation <https://www.twilio.com/docs/api/rest/sip>`_ on our website.

Creating a Sip Domain
=========================

The :class:`Domains` resource allows you to create a new domain. To
create a new domain, you'll need to choose a unique domain that lives
under sip.twilio.com. For example, dunder-mifflin-scranton.sip.twilio.com.
For more information, see the `Domains resource documentation <https://www.twilio.com/docs/api/rest/domain>`_ on our website.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token  = "YYYYYYYYYYYYYYYYYY"
    client = TwilioRestClient(account_sid, auth_token)

    domain = client.sip.domains.create(
        friendly_name="The Office Domain",
        voice_url="http://example.com/voice",
        domain_name="dunder-mifflin-scranton.sip.twilio.com",
    )
    print domain.sid

Creating a new IpAccessControlList
====================================

To control access to your new domain, you'll need to explicitly grant access
to individual ip addresses. To do this, you'll first need to create an
:class:`IpAccessControlList` to hold the ip addresses you wish to allow.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token  = "YYYYYYYYYYYYYYYYYY"
    client = TwilioRestClient(account_sid, auth_token)

    ip_acl = client.sip.ip_access_control_lists.create(
        friendly_name="The Office IpAccessControlList",
    )
    print ip_acl.sid

Adding a new IpAddress
=========================

Now it's time to add an :class:`IpAddress` to your new :class:`IpAccessControlList`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token  = "YYYYYYYYYYYYYYYYYY"
    client = TwilioRestClient(account_sid, auth_token)

    ip_address = client.sip.ip_addresses(
        "AL456",  # IpAccessControlList sid
    ).create(
        friendly_name="Dwight's Computer",
        ip_address="192.168.1.42",
    )
    print ip_address.sid

Adding an IpAccessControlList to a Domain
===========================================

Once you've created a :class:`Domain` and an :class:`IpAccessControlList` you need to
associate them. To do this, create an :class:`IpAccessControlListMapping`.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token  = "YYYYYYYYYYYYYYYYYY"
    client = TwilioRestClient(account_sid, auth_token)

    ip_access_control_list_mapping = client.sip.ip_access_control_list_mappings(
        "SD456",  # SIP Domain sid
    ).create(ip_access_control_list_sid="AL789")
    print ip_access_control_list_mapping.sid

