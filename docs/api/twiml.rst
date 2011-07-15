====================
:mod:`twilio.twiml`
====================

.. automodule:: twilio.twiml

.. autoclass:: twilio.twiml.Response
   :members:

Primary Verbs
~~~~~~~~~~~~~

.. autoclass:: twilio.twiml.Say
   :members:

.. autoclass:: twilio.twiml.Play
   :members:

.. autoclass:: twilio.twiml.Dial
   :members:

.. autoclass:: twilio.twiml.Gather
   :members:

.. autoclass:: twilio.twiml.Record
   :members:

Seconday Verbs
~~~~~~~~~~~~~~

.. autoclass:: twilio.twiml.Hangup
   :members:

.. autoclass:: twilio.twiml.Redirect
   :members:

.. autoclass:: twilio.twiml.Reject
   :members:

.. autoclass:: twilio.twiml.Pause
   :members:

.. autoclass:: twilio.twiml.Sms
   :members:

Nouns
~~~~~~

.. autoclass:: twilio.twiml.Conference
   :members:

.. autoclass:: twilio.twiml.Number
   :members:

Constants
~~~~~~~~~

Many TwiML verbs accept only certain values for specific attributes, such as :data:`MAN` and :data:`WOMAN` for voices.

Voices
>>>>>>
.. data:: MAN
.. data:: WOMAN

Languages
>>>>>>>>>
.. data:: ENGLISH
.. data:: SPANISH
.. data:: FRENCH
.. data:: GERMAN

HTTP Method
>>>>>>>>>>>
.. data:: GET
.. data:: POST

Rejection Reasons
>>>>>>>>>>>>>>>>>
.. data:: REJECTED
.. data:: BUSY
