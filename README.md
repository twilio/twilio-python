# twilio-python

[![Tests](https://github.com/twilio/twilio-python/actions/workflows/test-and-deploy.yml/badge.svg)](https://github.com/twilio/twilio-python/actions/workflows/test-and-deploy.yml)
[![PyPI](https://img.shields.io/pypi/v/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![PyPI](https://img.shields.io/pypi/pyversions/twilio.svg)](https://pypi.python.org/pypi/twilio)
[![Learn OSS Contribution in TwilioQuest](https://img.shields.io/static/v1?label=TwilioQuest&message=Learn%20to%20contribute%21&color=F22F46&labelColor=1f243c&style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAMAAAD04JH5AAAASFBMVEUAAAAZGRkcHBwjIyMoKCgAAABgYGBoaGiAgICMjIyzs7PJycnMzMzNzc3UoBfd3d3m5ubqrhfrMEDu7u739/f4vSb/3AD///9tbdyEAAAABXRSTlMAAAAAAMJrBrEAAAKoSURBVHgB7ZrRcuI6EESdyxXGYoNFvMD//+l2bSszRgyUYpFAsXOeiJGmj4NkuWx1Qeh+Ekl9DgEXOBwOx+Px5xyQhDykfgq4wG63MxxaR4ddIkg6Ul3g84vCIcjPBA5gmUMeXESrlukuoK33+33uID8TWeLAdOWsKpJYzwVMB7bOzYSGOciyUlXSn0/ABXTosJ1M1SbypZ4O4MbZuIDMU02PMbauhhHMHXbmebmALIiEbbbbbUrpF1gwE9kFfRNAJaP+FQEXCCTGyJ4ngDrjOFo3jEL5JdqjF/pueR4cCeCGgAtwmuRS6gDwaRiGvu+DMFwSBLTE3+jF8JyuV1okPZ+AC4hDFhCHyHQjdjPHUKFDlHSJkHQXMB3KpSwXNGJPcwwTdZiXlRN0gSp0zpWxNtM0beYE0nRH6QIbO7rawwXaBYz0j78gxjokDuv12gVeUuBD0MDi0OQCLvDaAho4juP1Q/jkAncXqIcCfd+7gAu4QLMACCLxpRsSuQh0igu0C9Svhi7weAGZg50L3IE3cai4IfkNZAC8dfdhsUD3CgKBVC9JE5ABAFzg4QL/taYPAAWrHdYcgfLaIgAXWJ7OV38n1LEF8tt2TH29E+QAoDoO5Ve/LtCQDmKM9kPbvCEBApK+IXzbcSJ0cIGF6e8gpcRhUDogWZ8JnaWjPXc/fNnBBUKRngiHgTUSivSzDRDgHZQOLvBQgf8rRt+VdBUUhwkU6VpJ+xcOwQUqZr+mR0kvBUgv6cB4+37hQAkXqE8PwGisGhJtN4xAHMzrsgvI7rccXqSvKh6jltGlrOHA3Xk1At3LC4QiPdX9/0ndHpGVvTjR4bZA1ypAKgVcwE5vx74ulwIugDt8e/X7JgfkucBMIAr26ndnB4UCLnDOqvteQsHlgX9N4A+c4cW3DXSPbwAAAABJRU5ErkJggg==)](https://twil.io/learn-open-source)

## Documentation

The documentation for the Twilio API can be found [here][apidocs].

The Python library documentation can be found [here][libdocs].

## Versions

`twilio-python` uses a modified version of [Semantic Versioning](https://semver.org) for all changes. [See this document](VERSIONS.md) for details.

### Supported Python Versions

This library supports the following Python implementations:

- Python 3.7
- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11

## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a
package manager for Python.

```shell
pip3 install twilio
```

If pip install fails on Windows, check the path length of the directory. If it is greater 260 characters then enable [Long Paths](https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation) or choose other shorter location.

Don't have pip installed? Try installing it, by running this from the command
line:

```shell
curl https://bootstrap.pypa.io/get-pip.py | python
```

Or, you can [download the source code
(ZIP)](https://github.com/twilio/twilio-python/zipball/main 'twilio-python
source code') for `twilio-python`, and then run:

```shell
python3 setup.py install
```

> **Info**
> If the command line gives you an error message that says Permission Denied, try running the above commands with `sudo` (e.g., `sudo pip3 install twilio`).

### Test your installation

Try sending yourself an SMS message. Save the following code sample to your computer with a text editor. Be sure to update the `account_sid`, `auth_token`, and `from_` phone number with values from your [Twilio account](https://console.twilio.com). The `to` phone number will be your own mobile phone.

```python
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15558675309",
    from_="+15017250604",
    body="Hello from Python!")

print(message.sid)
```

Save the file as `send_sms.py`. In the terminal, `cd` to the directory containing the file you just saved then run:

```shell
python3 send_sms.py
```

After a brief delay, you will receive the text message on your phone.

> **Warning**
> It's okay to hardcode your credentials when testing locally, but you should use environment variables to keep them secret before committing any code or deploying to production. Check out [How to Set Environment Variables](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html) for more information.

## OAuth Feature for Twilio APIs
We are introducing Client Credentials Flow-based OAuth 2.0 authentication. This feature is currently in beta and its implementation is subject to change.

API examples [here](https://github.com/twilio/twilio-python/blob/main/examples/public_oauth.py)

Organisation API examples [here](https://github.com/twilio/twilio-python/blob/main/examples/organization_api.py)

## Use the helper library

### API Credentials

The `Twilio` client needs your Twilio credentials. You can either pass these directly to the constructor (see the code below) or via environment variables.

Authenticating with Account SID and Auth Token:

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)
```

Authenticating with API Key and API Secret:

```python
from twilio.rest import Client

api_key = "XXXXXXXXXXXXXXXXX"
api_secret = "YYYYYYYYYYYYYYYYYY"
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client = Client(api_key, api_secret, account_sid)
```

Alternatively, a `Client` constructor without these parameters will
look for `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` variables inside the
current environment.

We suggest storing your credentials as environment variables. Why? You'll never
have to worry about committing your credentials and accidentally posting them
somewhere public.

```python
from twilio.rest import Client
client = Client()
```

### Specify Region and/or Edge

To take advantage of Twilio's [Global Infrastructure](https://www.twilio.com/docs/global-infrastructure), specify the target Region and Edge for the client:

> **Note:** When specifying a `region` parameter for a helper library client, be sure to also specify the `edge` parameter. For backward compatibility purposes, specifying a `region` without specifying an `edge` will result in requests being routed to US1.

```python
from twilio.rest import Client

client = Client(region='au1', edge='sydney')
```

A `Client` constructor without these parameters will also look for `TWILIO_REGION` and `TWILIO_EDGE` variables inside the current environment.

Alternatively, you may specify the edge and/or region after constructing the Twilio client:

```python
from twilio.rest import Client

client = Client()
client.region = 'au1'
client.edge = 'sydney'
```

This will result in the `hostname` transforming from `api.twilio.com` to `api.sydney.au1.twilio.com`.

### Make a Call

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

call = client.calls.create(to="9991231234",
                           from_="9991231234",
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")
print(call.sid)
```

### Get data about an existing call

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

call = client.calls.get("CA42ed11f93dc08b952027ffbc406d0868")
print(call.to)
```

### Iterate through records

The library automatically handles paging for you. Collections, such as `calls` and `messages`, have `list` and `stream` methods that page under the hood. With both `list` and `stream`, you can specify the number of records you want to receive (`limit`) and the maximum size you want each page fetch to be (`page_size`). The library will then handle the task for you.

`list` eagerly fetches all records and returns them as a list, whereas `stream` returns an iterator and lazily retrieves pages of records as you iterate over the collection. You can also page manually using the `page` method.

`page_size` as a parameter is used to tell how many records should we get in every page and `limit` parameter is used to limit the max number of records we want to fetch.

#### Use the `list` method

```python
from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

for sms in client.messages.list():
  print(sms.to)
```

```python
client.messages.list(limit=20, page_size=20)
```
This will make 1 call that will fetch 20 records from backend service.

```python
client.messages.list(limit=20, page_size=10)
```
This will make 2 calls that will fetch 10 records each from backend service.

```python
client.messages.list(limit=20, page_size=100)
```
This  will make 1 call which will fetch 100 records but user will get only 20 records.

### Asynchronous API Requests

By default, the Twilio Client will make synchronous requests to the Twilio API. To allow for asynchronous, non-blocking requests, we've included an optional asynchronous HTTP client. When used with the Client and the accompanying `*_async` methods, requests made to the Twilio API will be performed asynchronously.

```python
from twilio.http.async_http_client import AsyncTwilioHttpClient
from twilio.rest import Client

async def main():
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token  = "your_auth_token"
    http_client = AsyncTwilioHttpClient()
    client = Client(account_sid, auth_token, http_client=http_client)

    message = await client.messages.create_async(to="+12316851234", from_="+15555555555",
                                                 body="Hello there!")

asyncio.run(main())
```

### Enable Debug Logging

Log the API request and response data to the console:

```python
import logging

client = Client(account_sid, auth_token)
logging.basicConfig()
client.http_client.logger.setLevel(logging.INFO)
```

Log the API request and response data to a file:

```python
import logging

client = Client(account_sid, auth_token)
logging.basicConfig(filename='./log.txt')
client.http_client.logger.setLevel(logging.INFO)
```

### Handling Exceptions

Version 8.x of `twilio-python` exports an exception class to help you handle exceptions that are specific to Twilio methods. To use it, import `TwilioRestException` and catch exceptions as follows:

```python
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
client = Client(account_sid, auth_token)

try:
  message = client.messages.create(to="+12316851234", from_="+15555555555",
                                   body="Hello there!")
except TwilioRestException as e:
  print(e)
```

### Generating TwiML

To control phone calls, your application needs to output [TwiML][twiml].

Use `twilio.twiml.Response` to easily create such responses.

```python
from twilio.twiml.voice_response import VoiceResponse

r = VoiceResponse()
r.say("Welcome to twilio!")
print(str(r))
```

```xml
<?xml version="1.0" encoding="utf-8"?>
<Response><Say>Welcome to twilio!</Say></Response>
```

### Other advanced examples

- [Learn how to create your own custom HTTP client](./advanced-examples/custom-http-client.md)

### Docker Image

The `Dockerfile` present in this repository and its respective `twilio/twilio-python` Docker image are currently used by Twilio for testing purposes only.

### Getting help

If you need help installing or using the library, please check the [Twilio Support Help Center](https://support.twilio.com) first, and [file a support ticket](https://twilio.com/help/contact) if you don't find an answer to your question.

If you've instead found a bug in the library or would like new features added, go ahead and open issues or pull requests against this repo!

[apidocs]: https://www.twilio.com/docs/api
[twiml]: https://www.twilio.com/docs/api/twiml
[libdocs]: https://twilio.github.io/twilio-python
