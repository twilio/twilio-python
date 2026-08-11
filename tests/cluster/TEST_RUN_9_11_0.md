# twilio-python 9.11.0 — Integration Test Run Report

## Summary

| | |
|---|---|
| **Package** | `twilio==9.11.0` (PyPI) |
| **Test file** | `tests/cluster/test_9_11_0.py` |
| **Run date** | 2026-08-11 |
| **Result** | ✅ 17 passed, 0 failed, 0 skipped |
| **Duration** | 16.10s |
| **Python** | 3.13.9 |
| **pytest** | 9.1.1 |

## Package Verification

The tests were executed against the **published PyPI package**, not the local source tree.

```
pip install twilio==9.11.0

INSTALLER : pip
Location  : /tmp/twilio-9110-test/lib/python3.13/site-packages
Interpreter: /tmp/twilio-9110-test/bin/python3  (isolated venv)
```

Tests were run from outside the repository root (`cd /tmp`) to ensure the local
source directory was not prepended to `sys.path` and could not shadow the
installed package.

## Spec References

| PR | Repository | Description |
|----|-----------|-------------|
| [#150](https://github.com/twilio/twilio-oai/pull/150) | twilio-oai | OAI spec changes regenerated at `f443c9d` / `89762bc` |
| [#951](https://github.com/twilio/twilio-python/pull/951) | twilio-python | Generated SDK changes — Release 9.11.0 |

## Test Results

```
PASSED  test_accounts_suppress_email_notification_on_auth_token_promotion
PASSED  test_accounts_suppress_email_notification_on_secondary_auth_token
PASSED  test_conversations_v2_configurations_list
PASSED  test_conversations_v2_conversations_list
PASSED  test_insights_v3_metadata_fetch
PASSED  test_insights_v3_query_create
PASSED  test_intelligence_v3_conversations_list
PASSED  test_intelligence_v3_operators_list
PASSED  test_knowledge_v2_knowledge_bases_list
PASSED  test_memory_v1_store_lifecycle
PASSED  test_memory_v1_stores_list
PASSED  test_routes_v3_phone_number_fetch
PASSED  test_twiml_connect_no_assistant_noun
PASSED  test_twiml_dial_passports_attribute
PASSED  test_voice_v2_account_default_configuration_recording_fetch
PASSED  test_voice_v2_recording_configuration_fetch
PASSED  test_voice_v2_transcription_configuration_fetch

17 passed in 16.10s
```

## Coverage by Change Area

### TwiML
| Test | What it validates |
|------|------------------|
| `test_twiml_dial_passports_attribute` | New `passports` attribute on `<Dial>` renders correctly for SHAKEN/STIR passport passthrough |
| `test_twiml_connect_no_assistant_noun` | `<Assistant>` noun removed from `<Connect>` verb (AI Assistants deprecation breaking change) |

### Accounts
| Test | What it validates |
|------|------------------|
| `test_accounts_suppress_email_notification_on_secondary_auth_token` | `suppress_email_notification` parameter present on `SecondaryAuthToken.create()` and `.delete()` |
| `test_accounts_suppress_email_notification_on_auth_token_promotion` | `suppress_email_notification` parameter present on `AuthTokenPromotion.update()` |

> Auth token rotation tests are signature-only (no live API call) to avoid destructive side effects on the production account.

### Voice v2 (new module)
| Test | What it validates |
|------|------------------|
| `test_voice_v2_recording_configuration_fetch` | `voice.v2.recording(id).fetch()` routes correctly to `/Configurations/Recording/{id}` |
| `test_voice_v2_transcription_configuration_fetch` | `voice.v2.transcription(id).fetch()` routes correctly to `/Configurations/Transcription/{id}` |
| `test_voice_v2_account_default_configuration_recording_fetch` | `voice.v2.account_default_configuration("Recording").fetch()` routes correctly |

### Insights v3 (new module)
| Test | What it validates |
|------|------------------|
| `test_insights_v3_metadata_fetch` | `insights.v3.metadata.fetch()` returns metadata from `/InsightsDomains/Conversations/Metadata` |
| `test_insights_v3_query_create` | `insights.v3.query.create(InsightsQueryRequest)` sends a synchronous query |

### Intelligence v3 (new module)
| Test | What it validates |
|------|------------------|
| `test_intelligence_v3_operators_list` | `intelligence.v3.operators.list()` returns a list of Language Operators |
| `test_intelligence_v3_conversations_list` | `intelligence.v3.conversations.list()` returns paginated conversation records |

### Memory v1 (new module)
| Test | What it validates |
|------|------------------|
| `test_memory_v1_store_lifecycle` | Full async create → operation poll → fetch → delete lifecycle for a Memory Store |
| `test_memory_v1_stores_list` | `memory.v1.stores.list()` returns store IDs as strings; each ID is fetchable for full details |

> Memory store create returns HTTP 202 (Accepted) with a `status_url`. The lifecycle test polls the
> operation until `COMPLETED`, extracts the store ID from `result_url`, fetches it, then deletes it.
> A `uuid4`-based unique display name is used per run to avoid the 520045 name-reservation collision
> that occurs during the async deletion window.

### Knowledge v2 (new module)
| Test | What it validates |
|------|------------------|
| `test_knowledge_v2_knowledge_bases_list` | `knowledge.v2.knowledge_bases.list()` returns knowledge base records |

### Conversations v2 (new module)
| Test | What it validates |
|------|------------------|
| `test_conversations_v2_configurations_list` | `conversations.v2.configurations.list()` returns configuration records |
| `test_conversations_v2_conversations_list` | `conversations.v2.conversations.list()` returns conversation records |

### Routes v3 (new module)
| Test | What it validates |
|------|------------------|
| `test_routes_v3_phone_number_fetch` | `routes.v3.phone_numbers(number).fetch()` returns routing config for a known E.164 number |

> Requires `TWILIO_PHONE_NUMBER` env var. Test self-skips if not set.

## Environment Variables Required

```bash
export TWILIO_ACCOUNT_SID=<account_sid>
export TWILIO_AUTH_TOKEN=<auth_token>
export TWILIO_PHONE_NUMBER=<e164_number>   # optional — Routes v3 test skips if unset
```

## How to Run

```bash
# Isolated run against the published PyPI package (recommended)
python3 -m venv /tmp/twilio-9110-test
/tmp/twilio-9110-test/bin/pip install twilio==9.11.0 pytest

cd /tmp   # run outside repo root to prevent local source shadowing the installed package

TWILIO_ACCOUNT_SID=<sid> \
TWILIO_AUTH_TOKEN=<token> \
TWILIO_PHONE_NUMBER=<number> \
/tmp/twilio-9110-test/bin/python3 -m pytest \
  /path/to/twilio-python/tests/cluster/test_9_11_0.py -v

# Or from inside the repo (uses local source tree)
cd /path/to/twilio-python
export TWILIO_ACCOUNT_SID=<sid>
export TWILIO_AUTH_TOKEN=<token>
export TWILIO_PHONE_NUMBER=<number>
python3 -m pytest tests/cluster/test_9_11_0.py -v
```

## Notable Findings

### Memory Store create is asynchronous
`stores.create()` returns HTTP **202 Accepted**, not 201. The response body contains only a
`status_url` (operation URL) and a message — the store `id` is not present in the create
response. Callers must poll the operation endpoint until `status == "COMPLETED"` and then
read the store ID from `result_url`.

### Memory store list returns ID strings, not resource objects
`memory.v1.stores.list()` returns `List[str]` (store ID strings), not `List[StoreInstance]`.
Fetch each ID individually via `memory.v1.stores(store_id).fetch()` to get the full resource.

### Display name is reserved during async deletion
After deleting a store, the display name remains reserved while the async delete operation
is `RUNNING`. Attempting to create a new store with the same name during this window fails
with error **520045** ("Memory store already exists"). The lifecycle test uses a
`uuid4`-suffixed name to avoid this.
