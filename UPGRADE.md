# Upgrade Guide

_`MAJOR` version bumps will have upgrade notes
posted here._

## [2024-02-20] 8.x.x to 9.x.x
### Overview

##### Twilio Python Helper Library’s major version 9.0.0 is now available. We ensured that you can upgrade to Python helper Library 9.0.0 version without any breaking changes of existing apis

Behind the scenes Python Helper is now auto-generated via OpenAPI with this release. This enables us to rapidly add new features and enhance consistency across versions and languages.
We're pleased to inform you that version 9.0.0 adds support for the application/json content type in the request body.


## [2023-04-05] 7.x.x to 8.x.x

- **Supported Python versions updated**
  - Dropped support for Python 3.6 ([#632](https://github.com/twilio/twilio-python/pull/632))
  - Python 3.7 is the new required minimum version to use twilio-python helper library
- **Deletion of TwiML Voice Deprecated Methods ([#643](https://github.com/twilio/twilio-python/pull/643))**

  - [`<Refer>`](https://www.twilio.com/docs/voice/twiml/refer)
    - `Refer.refer_sip()` replaced by `Refer.sip()`
  - [`<Say>`](https://www.twilio.com/docs/voice/twiml/say/text-speech#generating-ssml-via-helper-libraries)

    - `Say.ssml_break()` replaced by `Say.break_()`
    - `Say.ssml_emphasis()` replaced by `Say.emphasis()`
    - `Say.ssml_lang()` replaced by `Say.lang()`
    - `Say.ssml_p()` replaced by `Say.p()`
    - `Say.ssml_phoneme()` replaced by `Say.phoneme()`
    - `Say.ssml_prosody()` replaced by `Say.prosody()`
    - `Say.ssml_s()` replaced by `Say.s()`
    - `Say.ssml_say_as()` replaced by `Say.say_as()`
    - `Say.ssml_sub()` replaced by `Say.sub()`
    - `Say.ssml_w()` replaced by `Say.w()`

    Old:

    ```python
    from twilio.twiml.voice_response import VoiceResponse
    resp = VoiceResponse()
    say = resp.say("Hello")
    say.ssml_emphasis("you")
    ```

    New:

    ```python
    from twilio.twiml.voice_response import VoiceResponse
    resp = VoiceResponse()
    say = resp.say("Hello")
    say.emphasis("you")
    ```

- **JWT token building deprecations ([#644](https://github.com/twilio/twilio-python/pull/644))**
  - `ConversationsGrant` has been deprecated in favor of `VoiceGrant`
  - `IpMessagingGrant` has been removed
- `twilio.rest.api.v2010.account.available_phone_number` has been renamed to `twilio.rest.api.v2010.account.available_phone_number_country`
- **[TaskRouter Workers Statistics](https://www.twilio.com/docs/taskrouter/api/worker/statistics) operations updated ([#653](https://github.com/twilio/twilio-python/pull/653))**

  - Cumulative and Real-Time Workers Statistics no longer accept a WorkerSid
  - `GET /v1/Workspaces/{WorkspaceSid}/Workers/CumulativeStatistics`

    Old: `client.taskrouter.v1.workspaces('WS...').workers('WK...).cumulative_statistics()`

    New: `client.taskrouter.v1.workspaces('WS...').workers.cumulative_statistics()`

  - `GET /v1/Workspaces/{WorkspaceSid}/Workers/RealTimeStatistics`

    Old: `client.taskrouter.v1.workspaces('WS...').workers('WK...).real_time_statistics()`

    New: `client.taskrouter.v1.workspaces('WS...').workers.real_time_statistics()`

- **Internal refactor of `instance._properties`**
  - Instance properties moved out of the generic `_properties` dict ([#696](https://github.com/twilio/twilio-python/pull/696))
  - This is an implementation detail that should not be depended upon

## [2021-09-22] 6.x.x to 7.x.x

### Overview

Version `7.x.x` is the first version that officially drops support for Python versions 2.7, 3.4, and 3.5.

#### Removal of files and dependencies that were added to support Python 2.7, 3.4, and 3.5

- [Six](https://github.com/twilio/twilio-python/pull/560/files#diff-4d7c51b1efe9043e44439a949dfd92e5827321b34082903477fd04876edb7552L4)
  - Removed use of `u` a fake unicode literal
  - Removed use of `b` a fake bytes literal
  - Removed `PY3` a boolean indicating if the code is running on Python 3
  - `text_type` type for representing (Unicode) textual data --> `str`
  - `iteritems` returns an iterator over dictionary’s items --> `items`
  - `string_types` possible types for text data like basestring() in Python 2 and str in Python 3.--> `str`
- [twilio/compat.py](https://github.com/twilio/twilio-python/pull/560/files?file-filters%5B%5D=.md&file-filters%5B%5D=.py&file-filters%5B%5D=.toml&file-filters%5B%5D=.txt&file-filters%5B%5D=.yml&file-filters%5B%5D=No+extension#diff-e327449701a8717c94e1a084cdfc7dbf334c634cddf3867058b8f991d2de52c1L1)
  - `from twilio.compat import urlencode` --> `from urllib.parse import urlencode`
  - `izip` --> `zip`
- [twilio/jwt/compat.py](https://github.com/twilio/twilio-python/pull/560/files?file-filters%5B%5D=.md&file-filters%5B%5D=.py&file-filters%5B%5D=.toml&file-filters%5B%5D=.txt&file-filters%5B%5D=.yml&file-filters%5B%5D=No+extension#diff-03276a6bdd4ecdf37ab6bedf60032dd05f640e1b470e4353badc787d80ba73d5L1)
  - Removed `compat.compare_digest`
- [twilio/jwt/**init**.py](https://github.com/twilio/twilio-python/pull/560/files?file-filters%5B%5D=.ini&file-filters%5B%5D=.py&file-filters%5B%5D=.yml#diff-9152dd65476e69cc34a307781d5cef195070f48da5670ed0934fd34a9ac91150L12-L16)
  - Removed import for `simplejson` and `json`

#### Updated dependencies

- [Updated PyJWT to >=2.0.0](https://github.com/twilio/twilio-python/pull/560/files#diff-4d7c51b1efe9043e44439a949dfd92e5827321b34082903477fd04876edb7552L6)

### CHANGED - [Remove the ability to override the `algorithm` in `Jwt.to_jwt()`](https://github.com/twilio/twilio-python/pull/560/commits/dab158f429015e0894217d6503f55b517c27c474)

#### Removed the ability to override the algorithm while using a jwt access token

```python
// 6.x.x
from twilio.jwt.access_token import AccessToken
token.to_jwt(algorithm='HS512')
```

```python
// 7.x.x
from twilio.jwt.access_token import AccessToken
token.to_jwt()
```

## [2017-09-28] 6.6.x to 6.7.x

### CHANGED - `Body` parameter on Chat `Message` creation is no longer required

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
