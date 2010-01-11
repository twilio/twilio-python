#!/usr/bin/env python
"""
The TwiML Python Response Library makes it easy to write TwiML without having
to touch XML. Error checking is built in to help preventing invalid markup.

USAGE:
To create TwiML, you will make new TwiML verbs and nest them inside another
TwiML verb. Convenience methods are provided to simplify TwiML creation.

SUPPORTED VERBS:
    Response
    Say
    Play
    Dial
    Gather
    Hangup
    Redirect
    Record
    Pause
    Number
    Conference
    Sms
"""

import twilio

# ===========================================================================
# Using Say, Dial, and Play
r = twilio.Response()
r.append(twilio.Say("Hello World", voice=twilio.Say.MAN,
    language=twilio.Say.FRENCH, loop=10))
r.append(twilio.Dial("4155551212", timeLimit=45))
r.append(twilio.Play("http://www.mp3.com"))
print r

""" outputs:
<Response>
    <Say voice="man" language="fr" loop="10">Hello World</Say>
    <Dial timeLimit="45">4155551212</Dial>
    <Play>http://www.mp3.com</Play>
</Response>
"""

# The same XML can be created above using the convenience methods
r = twilio.Response()
r.addSay("Hello World", voice=twilio.Say.MAN, language=twilio.Say.FRENCH,
    loop=10)
r.addDial("4155551212", timeLimit=45)
r.addPlay("http://www.mp3.com")
print r


# ===========================================================================
# Using Gather, Redirect
r = twilio.Response()
g = r.append(twilio.Gather(numDigits=1))
g.append(twilio.Say("Press 1"))
r.append(twilio.Redirect())
print r

""" outputs:
<Response>
    <Gather numDigits="1">
        <Say>Press 1</Say>
    </Gather>
    <Redirect/>
</Response>
"""

# ===========================================================================
# Adding a Say verb multiple times
r = twilio.Response()
s = twilio.Say("Press 1")
r.append(s)
r.append(s)
print r

""" outputs:
<Response>
    <Say>Press 1</Say>
    <Say>Press 1</Say>
</Response>
"""

# ===========================================================================
# You may want to add an attribute to a verb that the library doesn't support.
# To set arbitrary attribute / value pairs, just include the new attribute
# as a named parameter
r = twilio.Response()
r.append(twilio.Redirect(crazy="delicious"))
print r

""" outputs:
<Response>
	<Redirect crazy="delicious"/>
</Response>
"""
