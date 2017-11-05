# Upgrade Guide

_After `6.0.0` all `MINOR` and `MAJOR` version bumps will have upgrade notes 
posted here._

[2017-09-28] 6.6.x to 6.7.x
---------------------------

### CHANGED - `Body` parameter on Chat `Message` creation is no longer required.

#### Rationale
This was changed to add support for sending media in Chat messages, users can now either provide a `body` or a `media_sid`.

#### 6.6.x
```python
from twilio.rest import Client

client = Client('AC123', 'auth')
client.chat.v2.services('IS123').channels('CH123').messages.create("this is the body")
```

#### 6.7.x
```python
from twilio.rest import Client

client = Client('AC123', 'auth')
client.chat.v2.services('IS123').channels('CH123').messages.create(body="this is the body")
```
