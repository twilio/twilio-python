.. _usage-twiml:

.. module:: twilio.twiml

==============
TwiML Creation
==============

TwiML creation begins with the :class:`Response` verb.
Each successive verb is created by calling various methods on the response,
such as :meth:`say` or :meth:`play`.
These methods return the verbs they create to ease creation of nested TwiML.
To finish, call the :meth:`toxml` method on the :class:`Response`,
which returns raw TwiML.

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()
    r.say("Hello")
    print str(r)

.. code-block:: xml

   <?xml version="1.0" encoding="utf-8"?>
   <Response><Say>Hello</Say><Response>

The verb methods (outlined in the :doc:`complete reference </api/twiml>`)
take the body (only text) of the verb as the first argument.
All attributes are keyword arguments.

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()
    r.play("https://api.twilio.com/cowbell.mp3", loop=5)
    print str(r)

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <Response>
        <Play loop="3">https://api.twilio.com/cowbell.mp3</Play>
    <Response>

The Message and Sms verbs are slightly special: because :const:`from` is a
Python keyword, use the :const:`sender` parameter to specify the number
the message should come from:

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()
    m = r.message("Hello MMS Monkey!", sender="+14155551234")
    print str(r)

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <Response>
        <Message from="+14155551234">Hello MMS Monkey!</Message>
    <Response>

Python 2.6+ added the :const:`with` statement for context management.
Using :const:`with`, the module can *almost* emulate Ruby blocks.

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()
    r.say("hello")
    with r.gather(finishOnKey=4) as g:
        g.say("world")
    print str(r)

which returns the following

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <Response>
      <Say>Hello</Say>
      <Gather finishOnKey="4"><Say>World</Say></Gather>
    </Response>

If you don't want the XML declaration in your output,
use the :meth:`toxml` method

.. code-block:: python

    from twilio import twiml

    r = twiml.Response()
    r.say("hello")
    with r.gather(finishOnKey=4) as g:
        g.say("world")
    print r.toxml(xml_declaration=False)

.. code-block:: xml

    <Response>
      <Say>Hello</Say>
      <Gather finishOnKey="4"><Say>World</Say></Gather>
    </Response>

