A module for using the Twilio REST API and generating valid TwiML.

## Installation

Install from PyPi using pip

    pip install twilio

## Getting Started

Getting started with the Twilio API couldn't be easier. Create a Twilio REST client to get started. For example, the following code makes a call using the Twilio REST API.

### API Credentials

`TwilioRestClient` needs your Twilio credentials. While these can be passed in directly to the constructor, we suggest storing your credentials as environment variables. Why? You'll never have to worry about committing your credentials and accidentally posting them somewhere public.

The `TwilioRestClient` looks for `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` inside the current environment.

### Making a Call

```python
from twilio.rest import TwilioRestClient

account = "AXXXXXXXXXXXXXXXXX"
token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account, token)

call = client.calls.make(to="9991231234", from_="9991231234",
                         url="http://foo.com/call.xml")
print call.length
print call.sid
```
#### API Credentials

`TwilioRestClient` needs your Twilio credentials. While these can be passed in directly to the constructor (see above), we suggest storing your credentials as environment variables. Why? You'll never have to worry about committing your credentials and accidentally posting them somewhere public.

The `TwilioRestClient` looks for `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` inside the current environment.

```python
from twilio.rest import TwilioRestClient
client = TwilioRestClient()
```

### Generating TwiML

To control phone calls, your application need to output TwiML. Use `twilio.twiml..Response` to easily create such responses.

```python
from twilio import twiml

r = twiml.Response()
r.play("monkey.mp3", loop=5)
print str(r)
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<Response><Play loop="5">monkey.mp3</Play><Response>
```

### Digging Deeper

The full power of the Twilio API is at your finger tips. The [full documentation](http://readthedocs.org/docs/twilio-python/en/latest/) explains all the awesome features available to use.
