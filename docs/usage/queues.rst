.. module:: twilio.rest.resources

==============================
Queues and Members
==============================

The :class:`Queue` resource allows you to query and manage the state of individual call queues.For more information, see the `Queue REST Resource <http://www.twilio.com/docs/api/rest/queue>`_.

The :class:`Members` resource is a subresource of a Queue resource. It represents the set of members currently in a queue. See the `Member REST Resource <http://www.twilio.com/docs/api/rest/member>`_ documentation for more information.


Listing Queues
-----------------------

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    queues = client.queues.list()

    for queue in queues:
        print queue.sid


Listing Queue Members
----------------------

Each :class:`Queue` has a :attr:`~Queue.queue_members` instance which represents
all current calls in the queue.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    queue = client.queues.get("QU123")

    for member in queue.queue_members.list():
        print member.call_sid


Getting a specific Queue Member
-------------------------------

To retrieve information about a specific member in the queue, each
:class:`Members` has a :meth:`Members.get` method. :meth:`Members.get` accepts
one argument. The argument can either be a `call_sid` thats in the queue, in
which case :meth:`get` will return a :class:`Member` instance representing that
call, or the argument can be ``Front``, in which case :meth:`Get` will return a
:class:`Member` instance representing the first call in the queue.

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"
    QUEUE_SID = "QUaaaaaaaaaaaaa"
    CALL_SID = "CAxxxxxxxxxxxxxx"
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    members = client.queues.get(QUEUE_SID).queue_members

    # Get the first call in the queue
    print members.get('Front').date_enqueued

    # Get the call with the given call sid in the queue
    print members.get(CALL_SID).current_position


Dequeueing Queue Members
------------------------

To dequeue a specific member from the queue, each :class:`Members` has a
:meth:`~Members.dequeue` method. :meth:`~Members.dequeue` accepts an argument
and two optional keyword arguments. The first argument is the url of the
twiml document to be executed when the member is dequeued. The other two are
:attr:`call_sid` and :attr:`method`, their default values are 'Front' and 'GET'

.. code-block:: python

    from twilio.rest import TwilioRestClient

    # To find these visit https://www.twilio.com/user/account
    ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXX"
    AUTH_TOKEN = "YYYYYYYYYYYYYYYYYY"
    QUEUE_SID = "QUaaaaaaaaaaaaa"

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    members = client.queues.get(QUEUE_SID).queue_members

    # Dequeue the first call in the queue
    print members.dequeue('http://www.twilio.com/welcome/call')

