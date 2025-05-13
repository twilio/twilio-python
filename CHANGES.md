twilio-python Changelog
=======================

Here you can see the full list of changes between each twilio-python release.

[2025-05-13] Version 9.6.1
--------------------------
**Accounts**
- Changes to add date_of_consent param in Bulk Consent API

**Api**
- Change `friendly_name`, `date_created` and `date_updated` properties to type `string`.

**Twiml**
- Update twiml definition for `<ConversationRelay>` and `<Assistant>`


[2025-05-05] Version 9.6.0
--------------------------
**Library - Fix**
- [PR #848](https://github.com/twilio/twilio-python/pull/848): Timezone changes in token_auth_strategy.py. Thanks to [@Pablo2113](https://github.com/Pablo2113)!
- [PR #853](https://github.com/twilio/twilio-python/pull/853): Fix deprecated/invalid config in `setup.cfg`. Thanks to [@abravalheri](https://github.com/abravalheri)!

**Library - Chore**
- [PR #858](https://github.com/twilio/twilio-python/pull/858): fix oauth examples. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Library - Docs**
- [PR #855](https://github.com/twilio/twilio-python/pull/855): update pagination usage in README.md. Thanks to [@manisha1997](https://github.com/manisha1997)!

**Api**
- Add `response_key` for `Usage Triggers` fetch endpoint.

**Flex**
- Add Update Interaction API
- Adding `webhook_ttid` as optional parameter in Interactions API

**Serverless**
- Add node22 as a valid Build runtime
- Add node20 as a valid Build runtime

**Video**
- removed `transcribe_participants_on_connect` and `transcriptions_configuration` from the room resource **(breaking change)**
- Added `transcribe_participants_on_connect` and `transcriptions_configuration` to the room resource


[2025-04-07] Version 9.5.2
--------------------------
**Studio**
- Add documentation for parent_step_sid field in Step resource


[2025-03-20] Version 9.5.1
--------------------------
**Accounts**
- Update Safelist API docs as part of prefix supoort

**Flex**
- Removing `first_name`, `last_name`, and `friendly_name` from the Flex User API

**Messaging**
- Add missing tests under transaction/phone_numbers and transaction/short_code


[2025-03-11] Version 9.5.0
--------------------------
**Library - Feature**
- [PR #850](https://github.com/twilio/twilio-python/pull/850): Update UPGRADE.md. Thanks to [@manisha1997](https://github.com/manisha1997)!

**Library - Fix**
- [PR #847](https://github.com/twilio/twilio-python/pull/847): AssistantsBase import. Thanks to [@sbansla](https://github.com/sbansla)!

**Api**
- Add the missing `emergency_enabled` field for `Address Service` endpoints

**Messaging**
- Add missing enums for A2P and TF

**Numbers**
- add missing enum values to hosted_number_order_status

**Twiml**
- Convert Twiml Attribute `speechModel` of type enum to string **(breaking change)**


[2025-02-20] Version 9.4.6
--------------------------
**Library - Chore**
- [PR #842](https://github.com/twilio/twilio-python/pull/842): issue 841. Thanks to [@manisha1997](https://github.com/manisha1997)!

**Flex**
- Adding Digital Transfers APIs under v1/Interactions

**Numbers**
- Convert webhook_type to ienum type in v1/Porting/Configuration/Webhook/{webhook_type}

**Trusthub**
- Changing TrustHub SupportingDocument status enum from lowercase to uppercase since kyc-orch returns status capitalized and rest proxy requires strict casing


[2025-02-11] Version 9.4.5
--------------------------
**Api**
- Change downstream url and change media type for file `base/api/v2010/validation_request.json`.

**Intelligence**
- Add json_results for Generative JSON operator results

**Messaging**
- Add DestinationAlphaSender API to support Country-Specific Alpha Senders

**Video**
- Change codec type from enum to case-insensitive enum in recording and room_recording apis


[2025-01-28] Version 9.4.4
--------------------------
**Library - Fix**
- [PR #822](https://github.com/twilio/twilio-python/pull/822): Fix for 10 vulnerabilities. Thanks to [@twilio-product-security](https://github.com/twilio-product-security)!

**Library - Chore**
- [PR #834](https://github.com/twilio/twilio-python/pull/834): update httpclient. Thanks to [@manisha1997](https://github.com/manisha1997)!
- [PR #837](https://github.com/twilio/twilio-python/pull/837): enable newer versions of aiohttp-retry. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!
- [PR #833](https://github.com/twilio/twilio-python/pull/833): created bug report issue template. Thanks to [@sbansla](https://github.com/sbansla)!

**Api**
- Add open-api file tag to `conference/call recordings` and `recording_transcriptions`.

**Events**
- Add support for subaccount subscriptions (beta)

**Insights**
- add new region to conference APIs

**Lookups**
- Add new `parnter_sub_id` query parameter to the lookup request


[2025-01-13] Version 9.4.3
--------------------------
**Messaging**
- Adds validity period Default value in service resource documentation


[2025-01-09] Version 9.4.2
--------------------------
**Library - Chore**
- [PR #832](https://github.com/twilio/twilio-python/pull/832): remove test for 3.7. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Numbers**
- Change beta feature flag to use v2/BulkHostedNumberOrders


[2024-12-13] Version 9.4.1
--------------------------
**Library - Fix**
- [PR #827](https://github.com/twilio/twilio-python/pull/827): Fixing init file for preview iam domain. Thanks to [@AsabuHere](https://github.com/AsabuHere)!

**Library - Chore**
- [PR #826](https://github.com/twilio/twilio-python/pull/826): fix orgs api changes. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!


[2024-12-12] Version 9.4.0
--------------------------
**Library - Feature**
- [PR #825](https://github.com/twilio/twilio-python/pull/825): Docs update and examples for organization api uptake and public oauth. Thanks to [@AsabuHere](https://github.com/AsabuHere)!
- [PR #815](https://github.com/twilio/twilio-python/pull/815): Organizations Api uptake for twilio-python. Thanks to [@AsabuHere](https://github.com/AsabuHere)!


[2024-12-05] Version 9.3.8
--------------------------
**Api**
- Add optional parameter `intelligence_service` to `transcription`
- Updated `phone_number_sid` to be populated for sip trunking terminating calls.

**Numbers**
- Add Update Hosted Number Order V2 API endpoint
- Update Port in docs

**Twiml**
- Add optional parameter `intelligence_service` to `<Transcription>`
- Add support for new `<ConversationRelay>` and `<Assistant>` noun
- Add `events` attribute to `<Dial>` verb


[2024-11-15] Version 9.3.7
--------------------------
**Library - Chore**
- [PR #819](https://github.com/twilio/twilio-python/pull/819): use older verison of aiohttp_retry. Thanks to [@sbansla](https://github.com/sbansla)!

**Api**
- Added `ivr-virtual-agent-custom-voices` and `ivr-virtual-agent-genai` to `usage_record` API.
- Add open-api file tag to realtime_transcriptions

**Taskrouter**
- Add `api-tag` property to workers reservation
- Add `api-tag` property to task reservation


[2024-10-25] Version 9.3.6
--------------------------
**Library - Chore**
- [PR #818](https://github.com/twilio/twilio-python/pull/818): removing unavailable references from init files. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!


[2024-10-24] Version 9.3.5
--------------------------
**Conversations**
- Expose ConversationWithParticipants resource that allows creating a conversation with participants


[2024-10-17] Version 9.3.4
--------------------------
**Api**
- Add response key `country` to fetch AvailablePhoneNumber resource by specific country.

**Messaging**
- Make library and doc public for requestManagedCert Endpoint


[2024-10-03] Version 9.3.3
--------------------------
**Library - Chore**
- [PR #816](https://github.com/twilio/twilio-python/pull/816): add assistants init files. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Messaging**
- Add A2P external campaign CnpMigration flag

**Numbers**
- Add address sid to portability API

**Verify**
- Add `SnaClientToken` optional parameter on Verification check.
- Add `EnableSnaClientToken` optional parameter for Verification creation.


[2024-09-25] Version 9.3.2
--------------------------
**Accounts**
- Update docs and mounts.
- Change library visibility to public
- Enable consent and contact bulk upsert APIs in prod.

**Serverless**
- Add is_plugin parameter in deployments api to check if it is plugins deployment


[2024-09-18] Version 9.3.1
--------------------------
**Library - Chore**
- [PR #813](https://github.com/twilio/twilio-python/pull/813): add static init file to iam domain. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Intelligence**
- Remove public from operator_type
- Update operator_type to include general-availablity and deprecated

**Numbers**
- Remove beta flag for bundle clone API


[2024-09-05] Version 9.3.0
--------------------------
**Iam**
- updated library_visibility public for new public apikeys

**Numbers**
- Add new field in Error Codes for Regulatory Compliance.
- Change typing of Port In Request date_created field to date_time instead of date **(breaking change)**


[2024-08-26] Version 9.2.4
--------------------------
**Library - Chore**
- [PR #810](https://github.com/twilio/twilio-python/pull/810): add license identifier to project metadata. Thanks to [@mschoettle](https://github.com/mschoettle)!
- [PR #808](https://github.com/twilio/twilio-python/pull/808): preview iam removal. Thanks to [@manisha1997](https://github.com/manisha1997)!
- [PR #807](https://github.com/twilio/twilio-python/pull/807): update intersphinx_mapping. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!
- [PR #804](https://github.com/twilio/twilio-python/pull/804): add init file. Thanks to [@manisha1997](https://github.com/manisha1997)!

**Api**
- Update documentation of `error_code` and `error_message` on the Message resource.
- Remove generic parameters from `transcription` resource
- Added public documentation for Payload Data retrieval API

**Flex**
- Adding update Flex User api

**Insights**
- Added 'branded', 'business_profile' and 'voice_integrity' fields in List Call Summary

**Intelligence**
- Add `words` array information to the Sentences v2 entity.
- Add `X-Rate-Limit-Limit`, `X-Rate-Limit-Remaining`, and `X-Rate-Limit-Config` headers for Operator Results.
- Change the path parameter when fetching an `/OperatorType/{}` from `sid<EY>` to `string` to support searching by SID or by name
- Add `X-Rate-Limit-Limit`, `X-Rate-Limit-Remaining`, and `X-Rate-Limit-Config` headers for Transcript and Service endpoints.

**Messaging**
- Adds two new channel senders api to add/remove channel senders to/from a messaging service
- Extend ERC api to accept an optional attribute in request body to indicate CNP migration for an ERC

**Numbers**
- Modify visibility to public in bundle clone API
- Add `port_date` field to Port In Request and Port In Phone Numbers Fetch APIs
- Change properties docs for port in phone numbers api
- Add is_test body param to the Bundle Create API
- Change properties docs for port in api

**Trusthub**
- Add new field in themeSetId in compliance_inquiry.

**Verify**
- Update `custom_code_enabled` description on verification docs


[2024-07-02] Version 9.2.3
--------------------------
**Intelligence**
- Deprecate account flag api.twilio-intelligence.v2


[2024-06-27] Version 9.2.2
--------------------------
**Api**
- Add `transcription` resource

**Flex**
- Changed mount name for flex_team v2 api

**Intelligence**
- Add `X-Rate-Limit-Limit`, `X-Rate-Limit-Remaining`, and `X-Rate-Limit-Config` as Response Headers to Operator resources

**Numbers**
- Added include_constraints query parameter to the Regulations API

**Twiml**
- Add support for `<Transcription>` noun


[2024-06-21] Version 9.2.1
--------------------------
**Api**
- Add beta feature request managed cert


[2024-06-18] Version 9.2.0
--------------------------
**Library - Chore**
- [PR #796](https://github.com/twilio/twilio-python/pull/796): adding contentType in post and put. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Events**
- Add `status` and `documentation_url` to Event Types

**Lookups**
- Removed unused `fraud` lookups in V1 only to facilitate rest proxy migration

**Numbers**
- Add date_created field to the Get Port In Request API
- Rename the `status_last_time_updated_timestamp` field to `last_updated` in the Get Port In Phone Number API **(breaking change)**
- Add Rejection reason and rejection reason code to the Get Port In Phone Number API
- Remove the carrier information from the Portability API

**Proxy**
- Change property `type` from enum to ienum

**Trusthub**
- Add skipMessagingUseCase field in compliance_tollfree_inquiry.


[2024-06-06] Version 9.1.1
--------------------------
**Api**
- Mark MaxPrice as obsolete

**Lookups**
- Update examples for `phone_number_quality_score`

**Messaging**
- List tollfree verifications on parent account and all sub-accounts


[2024-05-24] Version 9.1.0
--------------------------
**Library - Chore**
- [PR #789](https://github.com/twilio/twilio-python/pull/789): [Snyk] Security upgrade aiohttp from 3.8.6 to 3.9.4. Thanks to [@twilio-product-security](https://github.com/twilio-product-security)!

**Library - Fix**
- [PR #716](https://github.com/twilio/twilio-python/pull/716): Connection pool is full, discarding connection. Thanks to [@lightiverson](https://github.com/lightiverson)!

**Api**
- Add ie1 as supported region for UserDefinedMessage and UserDefinedMessageSubscription.

**Flex**
- Adding validated field to `plugin_versions`
- Corrected the data type for `runtime_domain`, `call_recording_webhook_url`, `crm_callback_url`, `crm_fallback_url`, `flex_url` in Flex Configuration
- Making `routing` optional in Create Interactions endpoint

**Intelligence**
- Expose operator authoring apis to public visibility
- Deleted `language_code` parameter from updating service in v2 **(breaking change)**
- Add read_only_attached_operator_sids to v2 services

**Numbers**
- Add API endpoint for GET Porting Webhook Configurations By Account SID
- Remove bulk portability api under version `/v1`. **(breaking change)**
- Removed porting_port_in_fetch.json files and move the content into porting_port_in.json files
- Add API endpoint to deleting Webhook Configurations
- Add Get Phone Number by Port in request SID and Phone Number SID api
- Add Create Porting webhook configuration API
- Added bundle_sid and losing_carrier_information fields to Create PortInRequest api to support Japan porting

**Taskrouter**
- Add back `routing_target` property to tasks
- Add back `ignore_capacity` property to tasks
- Removing `routing_target` property to tasks due to revert
- Removing `ignore_capacity` property to tasks due to revert
- Add `routing_target` property to tasks
- Add `ignore_capacity` property to tasks

**Trusthub**
- Add new field errors to bundle as part of public API response in customer_profile.json and trust_product.json **(breaking change)**
- Add themeSetId field in compliance_tollfree_inquiry.

**Verify**
- Update `friendly_name` description on service docs


[2024-04-18] Version 9.0.5
--------------------------
**Library - Chore**
- [PR #742](https://github.com/twilio/twilio-python/pull/742): [Snyk] Fix for 3 vulnerabilities. Thanks to [@twilio-product-security](https://github.com/twilio-product-security)!

**Flex**
- Add header `ui_version` to `web_channels` API

**Messaging**
- Redeploy after failed pipeline

**Numbers**
- Add Delete Port In request phone number api and Add Delete Port In request api


[2024-04-04] Version 9.0.4
--------------------------
**Api**
- Correct conference filtering by date_created and date_updated documentation, clarifying that times are UTC.

**Flex**
- Remove optional parameter from `plugins` and it to `plugin_versions`

**Lookups**
- Add new `pre_fill` package to the lookup response

**Messaging**
- Cleanup api.messaging.next-gen from Messaging Services endpoints
- Readd Sending-Window after fixing test failure

**Verify**
- Add `whatsapp.msg_service_sid` and `whatsapp.from` parameters to create, update, get and list of services endpoints

**Voice**
- Correct conference filtering by date_created and date_updated documentation, clarifying that times are UTC.

**Twiml**
- Add new `token_type` value `payment-method` for `Pay` verb


[2024-04-01] Version 9.0.3
--------------------------
**Api**
- Add property `queue_time` to conference participant resource
- Update RiskCheck documentation
- Correct call filtering by start and end time documentation, clarifying that times are UTC.

**Flex**
- Adding optional parameter to `plugins`

**Media**
- Remove API: MediaProcessor

**Messaging**
- Remove Sending-Window due to test failure
- Add Sending-Window as a response property to Messaging Services, gated by a beta feature flag

**Numbers**
- Correct valid_until_date field to be visible in Bundles resource
- Adding port_in_status field to the Port In resource and phone_number_status and sid fields to the Port In Phone Number resource

**Oauth**
- Modified token endpoint response
- Added refresh_token and scope as optional parameter to token endpoint

**Trusthub**
- Add update inquiry endpoint in compliance_registration.
- Add new field in themeSetId in compliance_registration.

**Voice**
- Correct call filtering by start and end time documentation, clarifying that times are UTC.

**Twiml**
- Add support for new Google voices (Q1 2024) for `Say` verb - gu-IN voices
- Add support for new Amazon Polly and Google voices (Q1 2024) for `Say` verb - Niamh (en-IE) and Sofie (da-DK) voices


[2024-03-15] Version 9.0.2
--------------------------
**Oauth**
- Add new APIs for vendor authorize and token endpoints


[2024-03-12] Version 9.0.1
--------------------------
**Library - Chore**
- [PR #775](https://github.com/twilio/twilio-python/pull/775): removing preview.understand references. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Api**
- Correct precedence documentation for application_sid vs status_callback in message creation
- Mark MaxPrice as deprecated

**Flex**
- Making `plugins` visibility to public

**Messaging**
- Add new `errors` attribute to the Brand Registration resource.
- Mark `brand_feedback` attribute as deprecated.
- Mark `failure_reason` attribute as deprecated.
- The new `errors` attribute is expected to provide additional information about Brand registration failures and feedback (if any has been provided by The Campaign Registry). Consumers should use this attribute instead of `brand_feedback` and `failure_reason`.

**Numbers**
- Correcting mount_name for porting port in fetch API

**Trusthub**
- Add new field in statusCallbackUrl in compliance_registration.
- Add new field in isvRegisteringForSelfOrTenant in compliance_registration.

**Twiml**
- Expanded description of Action parameter for Message verb


[2024-02-27] Version 9.0.0
--------------------------
**Note:** This release contains breaking changes, check our [upgrade guide](./UPGRADE.md###-2024-02-20-8xx-to-9xx) for detailed migration notes.

**Library - Feature**
- [PR #767](https://github.com/twilio/twilio-python/pull/767): Merge branch '9.0.0-rc' into main. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)! **(breaking change)**

**Library - Chore**
- [PR #771](https://github.com/twilio/twilio-python/pull/771): added check for unset values. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!
- [PR #768](https://github.com/twilio/twilio-python/pull/768): cluster tests enabled. Thanks to [@sbansla](https://github.com/sbansla)!

**Api**
- remove feedback and feedback summary from call resource

**Flex**
- Adding `routing_properties` to Interactions Channels Participant

**Lookups**
- Add new `line_status` package to the lookup response
- Remove `live_activity` package from the lookup response **(breaking change)**

**Messaging**
- Add tollfree multiple rejection reasons response array

**Trusthub**
- Add ENUM for businessRegistrationAuthority in compliance_registration. **(breaking change)**
- Add new field in isIsvEmbed in compliance_registration.
- Add additional optional fields in compliance_registration for Individual business type.

**Twiml**
- Add support for new Amazon Polly and Google voices (Q1 2024) for `Say` verb


[2024-02-09] Version 8.13.0
---------------------------
**Library - Fix**
- [PR #753](https://github.com/twilio/twilio-python/pull/753): added boolean_to_string converter. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Library - Chore**
- [PR #758](https://github.com/twilio/twilio-python/pull/758): disable cluster test. Thanks to [@sbansla](https://github.com/sbansla)!
- [PR #760](https://github.com/twilio/twilio-python/pull/760): run make prettier. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Api**
- Updated service base url for connect apps and authorized connect apps APIs **(breaking change)**
- Update documentation to reflect RiskCheck GA
- Added optional parameter `CallToken` for create participant api

**Events**
- Marked as GA

**Flex**
- Adding `flex_instance_sid` to Flex Configuration
- Adding `provisioning_status` for Email Manager
- Adding `offline_config` to Flex Configuration

**Insights**
- add flag to restrict access to unapid customers
- decommission voice-qualitystats-endpoint role

**Intelligence**
- Add text-generation operator (for example conversation summary) results to existing OperatorResults collection.

**Lookups**
- Remove `carrier` field from `sms_pumping_risk` and leave `carrier_risk_category` **(breaking change)**
- Remove carrier information from call forwarding package **(breaking change)**

**Messaging**
- Add update instance endpoints to us_app_to_person api
- Add tollfree edit_allowed and edit_reason fields
- Update Phone Number, Short Code, Alpha Sender, US A2P and Channel Sender documentation
- Add DELETE support to Tollfree Verification resource

**Numbers**
- Add Get Port In request api

**Push**
- Migrated to new Push API V4 with Resilient Notification Delivery.

**Serverless**
- Add node18 as a valid Build runtime

**Taskrouter**
- Add `jitter_buffer_size` param in update reservation
- Add container attribute to task_queue_bulk_real_time_statistics endpoint
- Remove beta_feature check on task_queue_bulk_real_time_statistics endpoint

**Trusthub**
- Add optional field NotificationEmail to the POST /v1/ComplianceInquiries/Customers/Initialize API
- Add additional optional fields in compliance_tollfree_inquiry.json
- Rename did to tollfree_phone_number in compliance_tollfree_inquiry.json
- Add new optional field notification_email to compliance_tollfree_inquiry.json

**Verify**
- `Tags` property added again to Public Docs **(breaking change)**
- Remove `Tags` from Public Docs **(breaking change)**
- Add `VerifyEventSubscriptionEnabled` parameter to service create and update endpoints.
- Add `Tags` optional parameter on Verification creation.
- Update Verify TOTP maturity to GA.


[2024-01-25] Version 8.12.0
---------------------------
**Oauth**
- updated openid discovery endpoint uri **(breaking change)**
- Added device code authorization endpoint
- added oauth JWKS endpoint
- Get userinfo resource
- OpenID discovery resource
- Add new API for token endpoint


[2024-01-14] Version 8.11.1
---------------------------
**Library - Chore**
- [PR #749](https://github.com/twilio/twilio-python/pull/749): removing webhook test. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Push**
- Migrated to new Push API V4 with Resilient Notification Delivery.


[2023-12-14] Version 8.11.0
---------------------------
**Library - Chore**
- [PR #741](https://github.com/twilio/twilio-python/pull/741): upgrade to python 3.12. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!
- [PR #740](https://github.com/twilio/twilio-python/pull/740): bump aiohttp. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Api**
- Updated service base url for connect apps and authorized connect apps APIs **(breaking change)**

**Events**
- Marked as GA

**Insights**
- decommission voice-qualitystats-endpoint role

**Numbers**
- Add Get Port In request api

**Taskrouter**
- Add `jitter_buffer_size` param in update reservation

**Trusthub**
- Add additional optional fields in compliance_tollfree_inquiry.json

**Verify**
- Remove `Tags` from Public Docs **(breaking change)**


[2023-12-01] Version 8.10.3
---------------------------
**Verify**
- Add `VerifyEventSubscriptionEnabled` parameter to service create and update endpoints.


[2023-11-17] Version 8.10.2
---------------------------
**Library - Chore**
- [PR #733](https://github.com/twilio/twilio-python/pull/733): bumping aiohttp from 3.8.5 to 3.8.6. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Api**
- Update documentation to reflect RiskCheck GA

**Messaging**
- Add tollfree edit_allowed and edit_reason fields
- Update Phone Number, Short Code, Alpha Sender, US A2P and Channel Sender documentation

**Taskrouter**
- Add container attribute to task_queue_bulk_real_time_statistics endpoint

**Trusthub**
- Rename did to tollfree_phone_number in compliance_tollfree_inquiry.json
- Add new optional field notification_email to compliance_tollfree_inquiry.json

**Verify**
- Add `Tags` optional parameter on Verification creation.


[2023-11-06] Version 8.10.1
---------------------------
**Flex**
- Adding `provisioning_status` for Email Manager

**Intelligence**
- Add text-generation operator (for example conversation summary) results to existing OperatorResults collection.

**Messaging**
- Add DELETE support to Tollfree Verification resource

**Serverless**
- Add node18 as a valid Build runtime

**Verify**
- Update Verify TOTP maturity to GA.


[2023-10-19] Version 8.10.0
---------------------------
**Library - Fix**
- [PR #730](https://github.com/twilio/twilio-python/pull/730): Requirement changes. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!
- [PR #727](https://github.com/twilio/twilio-python/pull/727): Requirement changes. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!
- [PR #726](https://github.com/twilio/twilio-python/pull/726): requirements changes. Thanks to [@tiwarishubham635](https://github.com/tiwarishubham635)!

**Accounts**
- Updated Safelist metadata to correct the docs.
- Add Global SafeList API changes

**Api**
- Added optional parameter `CallToken` for create participant api

**Flex**
- Adding `offline_config` to Flex Configuration

**Intelligence**
- Deleted `redacted` parameter from fetching transcript in v2 **(breaking change)**

**Lookups**
- Add new `phone_number_quality_score` package to the lookup response
- Remove `disposable_phone_number_risk` package **(breaking change)**

**Messaging**
- Update US App To Person documentation with current `message_samples` requirements

**Taskrouter**
- Remove beta_feature check on task_queue_bulk_real_time_statistics endpoint
- Add `virtual_start_time` property to tasks
- Updating `task_queue_data` format from `map` to `array` in the response of bulk get endpoint of TaskQueue Real Time Statistics API **(breaking change)**


[2023-10-05] Version 8.9.1
--------------------------
**Library - Chore**
- [PR #721](https://github.com/twilio/twilio-python/pull/721): Drop dependency on `pytz` by using stdlib `datetime.timezone.utc`. Thanks to [@Zac-HD](https://github.com/Zac-HD)!
- [PR #723](https://github.com/twilio/twilio-python/pull/723): twilio help changes. Thanks to [@kridai](https://github.com/kridai)!

**Library - Fix**
- [PR #724](https://github.com/twilio/twilio-python/pull/724): Update ValidateSslCertificate method. Thanks to [@AsabuHere](https://github.com/AsabuHere)!

**Lookups**
- Add test api support for Lookup v2


[2023-09-21] Version 8.9.0
--------------------------
**Conversations**
- Enable conversation email bindings, email address configurations and email message subjects

**Flex**
- Adding `console_errors_included` to Flex Configuration field `debugger_integrations`
- Introducing new channel status as `inactive` in modify channel endpoint for leave functionality **(breaking change)**
- Adding `citrix_voice_vdi` to Flex Configuration

**Taskrouter**
- Add Update Queues, Workers, Workflow Real Time Statistics API to flex-rt-data-api-v2 endpoint
- Add Update Workspace Real Time Statistics API to flex-rt-data-api-v2 endpoint


[2023-09-07] Version 8.8.0
--------------------------
**Api**
- Make message tagging parameters public **(breaking change)**

**Flex**
- Adding `agent_conv_end_methods` to Flex Configuration

**Messaging**
- Mark Mesasging Services fallback_to_long_code feature obsolete

**Numbers**
- Add Create Port In request api
- Renaming sid for bulk_hosting_sid and remove account_sid response field in numbers/v2/BulkHostedNumberOrders **(breaking change)**

**Pricing**
- gate resources behind a beta_feature


[2023-08-24] Version 8.7.0
--------------------------
**Library - Test**
- [PR #719](https://github.com/twilio/twilio-python/pull/719): Update test_webhook.py. Thanks to [@kridai](https://github.com/kridai)!

**Api**
- Add new property `RiskCheck` for SMS pumping protection feature only (public beta to be available soon): Include this parameter with a value of `disable` to skip any kind of risk check on the respective message request

**Flex**
- Changing `sid<UO>` path param to `sid<UT>` in interaction channel participant update endpoint **(breaking change)**

**Messaging**
- Add Channel Sender api
- Fixing country code docs and removing Zipwhip references

**Numbers**
- Request status changed in numbers/v2/BulkHostedNumberOrders **(breaking change)**
- Add bulk hosting orders API under version `/v2


[2023-08-10] Version 8.6.0
--------------------------
**Insights**
- Normalize annotations parameters in list summary api to be prefixed

**Numbers**
- Change Bulk_hosted_sid from BHR to BH prefix in HNO and dependent under version `/v2` API's. **(breaking change)**
- Added parameter target_account_sid to portability and account_sid to response body

**Verify**
- Remove beta feature flag to list attempts API.
- Remove beta feature flag to verifications summary attempts API.


[2023-07-27] Version 8.5.1
--------------------------
**Api**
- Added `voice-intelligence`, `voice-intelligence-transcription` and `voice-intelligence-operators` to `usage_record` API.
- Added `tts-google` to `usage_record` API.

**Lookups**
- Add new `disposable_phone_number_risk` package to the lookup response

**Verify**
- Documentation of list attempts API was improved by correcting `date_created_after` and `date_created_before` expected date format.
- Documentation was improved by correcting `date_created_after` and `date_created_before` expected date format parameter on attempts summary API.
- Documentation was improved by adding `WHATSAPP` as optional valid parameter on attempts summary API.

**Twiml**
- Added support for he-il inside of ssm_lang.json that was missing
- Added support for he-il language in say.json that was missing
- Add `statusCallback` and `statusCallbackMethod` attributes to `<Siprec>`.


[2023-07-13] Version 8.5.0
--------------------------
**Library - Fix**
- [PR #718](https://github.com/twilio/twilio-python/pull/718): Create __init__.py for intelligence domain. Thanks to [@AsabuHere](https://github.com/AsabuHere)!

**Flex**
- Adding `interaction_context_sid` as optional parameter in Interactions API

**Messaging**
- Making visiblity public for tollfree_verification API

**Numbers**
- Remove Sms capability property from HNO creation under version `/v2` of HNO API. **(breaking change)**
- Update required properties in LOA creation under version `/v2` of Authorization document API. **(breaking change)**

**Taskrouter**
- Add api to fetch task queue statistics for multiple TaskQueues

**Verify**
- Add `RiskCheck` optional parameter on Verification creation.

**Twiml**
- Add Google Voices and languages


[2023-06-28] Version 8.4.0
--------------------------
**Lookups**
- Add `reassigned_number` package to the lookup response

**Numbers**
- Add hosted_number_order under version `/v2`.
- Update properties in Porting and Bulk Porting APIs. **(breaking change)**
- Added bulk Portability API under version `/v1`.
- Added Portability API under version `/v1`.


[2023-06-15] Version 8.3.0
--------------------------
**Api**
- Added `content_sid` as conditional parameter
- Removed `content_sid` as optional field **(breaking change)**

**Insights**
- Added `annotation` to list summary output


[2023-06-01] Version 8.2.2
--------------------------
**Api**
- Add `Trim` to create Conference Participant API

**Intelligence**
- First public beta release for Voice Intelligence APIs with client libraries

**Messaging**
- Add new `errors` attribute to us_app_to_person resource. This attribute will provide additional information about campaign registration errors.


[2023-05-18] Version 8.2.1
--------------------------
**Conversations**
- Added  `AddressCountry` parameter to Address Configuration endpoint, to support regional short code addresses
- Added query parameters `start_date`, `end_date` and `state` in list Conversations resource for filtering

**Insights**
- Added annotations parameters to list summary api

**Messaging**
- Add GET domainByMessagingService endpoint to linkShortening service
- Add `disable_https` to link shortening domain_config properties

**Numbers**
- Add bulk_eligibility api under version `/v1`.


[2023-05-04] Version 8.2.0
--------------------------
**Conversations**
- Remove `start_date`, `end_date` and `state` query parameters from list operation on Conversations resource **(breaking change)**

**Twiml**
- Add support for new Amazon Polly voices (Q1 2023) for `Say` verb


[2023-04-19] Version 8.1.0
--------------------------
**Library - Chore**
- [PR #709](https://github.com/twilio/twilio-python/pull/709): Drop `asyncio` from requirements. Thanks to [@setu4993](https://github.com/setu4993)!

**Library - Docs**
- [PR #705](https://github.com/twilio/twilio-python/pull/705): consolidate. Thanks to [@stern-shawn](https://github.com/stern-shawn)!

**Messaging**
- Remove `messaging_service_sids` and `messaging_service_sid_action` from domain config endpoint **(breaking change)**
- Add error_code and rejection_reason properties to tollfree verification API response

**Numbers**
- Added the new Eligibility API under version `/v1`.


[2023-04-05] Version 8.0.0
--------------------------
**Note:** This release contains breaking changes, check our [upgrade guide](./UPGRADE.md###-2023-04-05-7xx-to-8xx) for detailed migration notes.

**Library - Feature**
- [PR #702](https://github.com/twilio/twilio-python/pull/702): Merge branch '8.0.0-rc' to main. Thanks to [@childish-sambino](https://github.com/childish-sambino)! **(breaking change)**

**Conversations**
- Expose query parameters `start_date`, `end_date` and `state` in list operation on Conversations resource for sorting and filtering

**Insights**
- Added answered by filter in Call Summaries

**Lookups**
- Remove `disposable_phone_number_risk` package **(breaking change)**

**Messaging**
- Add support for `SOLE_PROPRIETOR` brand type and `SOLE_PROPRIETOR` campaign use case.
- New Sole Proprietor Brands should be created with `SOLE_PROPRIETOR` brand type. Brand registration requests with `STARTER` brand type will be rejected.
- New Sole Proprietor Campaigns should be created with `SOLE_PROPRIETOR` campaign use case. Campaign registration requests with `STARTER` campaign use case will be rejected.
- Add Brand Registrations OTP API


[2023-03-22] Version 7.17.0
---------------------------
**Api**
- Revert Corrected the data type for `friendly_name` in Available Phone Number Local, Mobile and TollFree resources
- Corrected the data type for `friendly_name` in Available Phone Number Local, Mobile and TollFree resources **(breaking change)**

**Messaging**
- Add `linkshortening_messaging_service` resource
- Add new endpoint for GetDomainConfigByMessagingServiceSid
- Remove `validated` parameter and add `cert_in_validation` parameter to Link Shortening API **(breaking change)**


[2023-03-09] Version 7.16.5
---------------------------
**Api**
- Add new categories for whatsapp template

**Lookups**
- Remove `validation_results` from the `default_output_properties`

**Supersim**
- Add ESimProfile's `matching_id` and `activation_code` parameters to libraries


[2023-02-22] Version 7.16.4
---------------------------
**Api**
- Remove `scheduled_for` property from message resource
- Add `scheduled_for` property to message resource


[2023-02-08] Version 7.16.3
---------------------------
**Lookups**
- Add `disposable_phone_number_risk` package to the lookup response
- Add `sms_pumping_risk` package to the lookup response


[2023-01-25] Version 7.16.2
---------------------------
**Library - Chore**
- [PR #638](https://github.com/twilio/twilio-python/pull/638): relax test dependencies and remove unused dependencies. Thanks to [@childish-sambino](https://github.com/childish-sambino)!
- [PR #609](https://github.com/twilio/twilio-python/pull/609): Security upgrade pygments from 2.5.2 to 2.7.4. Thanks to [@twilio-product-security](https://github.com/twilio-product-security)!

**Library - Docs**
- [PR #637](https://github.com/twilio/twilio-python/pull/637): remove docs output from repo. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Library - Test**
- [PR #636](https://github.com/twilio/twilio-python/pull/636): update tox config and replace deprecated test functions. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Add `public_application_connect_enabled` param to Application resource

**Messaging**
- Add new tollfree verification API property (ExternalReferenceId)]

**Verify**
- Add `device_ip` parameter and channel `auto` for sna/sms orchestration

**Twiml**
- Add support for `<Application>` noun and `<ApplicationSid>` noun, nested `<Parameter>` to `<Hangup>` and `<Leave>` verb


[2023-01-11] Version 7.16.1
---------------------------
**Conversations**
- Add support for creating Multi-Channel Rich Content Messages

**Lookups**
- Changed the no data message for match postal code from `no_data` to `data_not_available` in identity match package

**Messaging**
- Add update/edit tollfree verification API


[2022-12-14] Version 7.16.0
---------------------------
**Library - Docs**
- [PR #631](https://github.com/twilio/twilio-python/pull/631): Updated docstrings for timeout to be float instead of int. Thanks to [@byarmis](https://github.com/byarmis)!

**Library - Chore**
- [PR #627](https://github.com/twilio/twilio-python/pull/627): add support for python 3.11. Thanks to [@JenniferMah](https://github.com/JenniferMah)!

**Library - Test**
- [PR #628](https://github.com/twilio/twilio-python/pull/628): Pinning ubuntu version for python 3.6 test runs. Thanks to [@rakatyal](https://github.com/rakatyal)!

**Api**
- Add `street_secondary` param to address create and update
- Make `method` optional for user defined message subscription **(breaking change)**

**Flex**
- Flex Conversations is now Generally Available
- Adding the ie1 mapping for authorization api, updating service base uri and base url response attribute **(breaking change)**
- Change web channels to GA and library visibility to public
- Changing the uri for authorization api from using Accounts to Insights **(breaking change)**

**Media**
- Gate Twilio Live endpoints behind beta_feature for EOS

**Messaging**
- Mark `MessageFlow` as a required field for Campaign Creation **(breaking change)**

**Oauth**
- updated openid discovery endpoint uri **(breaking change)**
- Added device code authorization endpoint

**Supersim**
- Allow filtering the SettingsUpdates resource by `status`

**Twiml**
- Add new Polly Neural voices
- Add tr-TR, ar-AE, yue-CN, fi-FI languages to SSML `<lang>` element.
- Add x-amazon-jyutping, x-amazon-pinyin, x-amazon-pron-kana, x-amazon-yomigana alphabets to SSML `<phoneme>` element.
- Rename `character` value for SSML `<say-as>` `interpret-as` attribute to `characters`. **(breaking change)**
- Rename `role` attribute to `format` in SSML `<say-as>` element. **(breaking change)**


[2022-11-30] Version 7.15.4
---------------------------
**Flex**
- Adding new `assessments` api in version `v1`

**Lookups**
- Add `identity_match` package to the lookup response

**Messaging**
- Added `validated` parameter to Link Shortening API

**Serverless**
- Add node16 as a valid Build runtime
- Add ie1 and au1 as supported regions for all endpoints.


[2022-11-16] Version 7.15.3
---------------------------
**Library - Chore**
- [PR #624](https://github.com/twilio/twilio-python/pull/624): upgrade GitHub Actions dependencies. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Set the Content resource to have public visibility as Preview

**Flex**
- Adding new parameter `base_url` to 'gooddata' response in version `v1`

**Insights**
- Added `answered_by` field in List Call Summary
- Added `answered_by` field in call summary


[2022-11-10] Version 7.15.2
---------------------------
**Flex**
- Adding two new authorization API 'user_roles' and 'gooddata' in version `v1`

**Messaging**
- Add new Campaign properties (MessageFlow, OptInMessage, OptInKeywords, OptOutMessage, OptOutKeywords, HelpMessage, HelpKeywords)

**Twiml**
- Add new speech models to `Gather`.


[2022-10-31] Version 7.15.1
---------------------------
**Api**
- Added `contentSid` and `contentVariables` to Message resource with public visibility as Beta
- Add `UserDefinedMessageSubscription` and `UserDefinedMessage` resource

**Proxy**
- Remove FailOnParticipantConflict param from Proxy Session create and update and Proxy Participant create

**Supersim**
- Update SettingsUpdates resource to remove PackageSid

**Taskrouter**
- Add `Ordering` query parameter to Workers and TaskQueues for sorting by
- Add `worker_sid` query param for list reservations endpoint

**Twiml**
- Add `url` and `method` attributes to `<Conversation>`


[2022-10-19] Version 7.15.0
---------------------------
**Api**
- Make link shortening parameters public **(breaking change)**

**Oauth**
- added oauth JWKS endpoint
- Get userinfo resource
- OpenID discovery resource
- Add new API for token endpoint

**Supersim**
- Add SettingsUpdates resource

**Verify**
- Update Verify Push endpoints to `ga` maturity
- Verify BYOT add Channels property to the Get Templates response

**Twiml**
- Add `requireMatchingInputs` attribute and `input-matching-failed` errorType to `<Prompt>`


[2022-10-05] Version 7.14.2
---------------------------
**Api**
- Added `virtual-agent` to `usage_record` API.
- Add AMD attributes to participant create request

**Twiml**
- Add AMD attributes to `Number` and `Sip`


[2022-09-21] Version 7.14.1
---------------------------
**Library - Fix**
- [PR #617](https://github.com/twilio/twilio-python/pull/617): support duplicated query param values. Thanks to [@childish-sambino](https://github.com/childish-sambino)!


[2022-09-07] Version 7.14.0
---------------------------
**Library - Fix**
- [PR #615](https://github.com/twilio/twilio-python/pull/615): support duplicate query param values. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Flex**
- Removed redundant `close` status from Flex Interactions flow **(breaking change)**
- Adding `debugger_integration` and `flex_ui_status_report` to Flex Configuration

**Messaging**
- Add create, list and get tollfree verification API

**Verify**
- Verify SafeList API endpoints added.

**Video**
- Add `Anonymize` API

**Twiml**
- Update `event` value `call-in-progress` to `call-answered`


[2022-08-24] Version 7.13.0
---------------------------
**Library - Test**
- [PR #614](https://github.com/twilio/twilio-python/pull/614): add test-docker rule. Thanks to [@beebzz](https://github.com/beebzz)!

**Api**
- Remove `beta feature` from scheduling params and remove optimize parameters. **(breaking change)**

**Routes**
- Remove Duplicate Create Method - Update Method will work even if Inbound Processing Region is currently empty/404. **(breaking change)**

**Twiml**
- Add new Polly Neural voices
- Add new languages to SSML `<lang>`.


[2022-08-10] Version 7.12.1
---------------------------
**Routes**
- Inbound Proccessing Region API - Public GA

**Supersim**
- Allow updating `DataLimit` on a Fleet


[2022-07-21] Version 7.12.0
---------------------------
**Flex**
- Add `status`, `error_code`, and `error_message` fields to Interaction `Channel`
- Adding `messenger` and `gbm` as supported channels for Interactions API

**Messaging**
- Update alpha_sender docs with new valid characters

**Verify**
- Reorder Verification Check parameters so `code` stays as the first parameter **(breaking change)**
- Rollback List Attempts API V2 back to pilot stage.


[2022-07-13] Version 7.11.0
---------------------------
**Library - Fix**
- [PR #611](https://github.com/twilio/twilio-python/pull/611): useragent regrex unit test for RC branch. Thanks to [@claudiachua](https://github.com/claudiachua)!

**Library - Test**
- [PR #610](https://github.com/twilio/twilio-python/pull/610): Adding misc as PR type. Thanks to [@rakatyal](https://github.com/rakatyal)!

**Conversations**
- Allowed to use `identity` as part of Participant's resource **(breaking change)**

**Lookups**
- Remove `enhanced_line_type` from the lookup response **(breaking change)**

**Supersim**
- Add support for `sim_ip_addresses` resource to helper libraries

**Verify**
- Changed summary param `service_sid` to `verify_service_sid` to be consistent with list attempts API **(breaking change)**
- Make `code` optional on Verification check to support `sna` attempts. **(breaking change)**


[2022-06-29] Version 7.10.0
---------------------------
**Api**
- Added `amazon-polly` to `usage_record` API.

**Insights**
- Added `annotation` field in call summary
- Added new endpoint to fetch/create/update Call Annotations

**Verify**
- Remove `api.verify.totp` beta flag and set maturity to `beta` for Verify TOTP properties and parameters. **(breaking change)**
- Changed summary param `verify_service_sid` to `service_sid` to be consistent with list attempts API **(breaking change)**

**Twiml**
- Add `maxQueueSize` to `Enqueue`


[2022-06-15] Version 7.9.3
--------------------------
**Lookups**
- Adding support for Lookup V2 API

**Studio**
- Corrected PII labels to be 30 days and added context to be PII

**Twiml**
- Add `statusCallbackMethod` attribute, nested `<Config` and `<Parameter>` elements to `<VirtualAgent>` noun.
- Add support for new Amazon Polly voices (Q2 2022) for `Say` verb
- Add support for `<Conversation>` noun


[2022-06-01] Version 7.9.2
--------------------------
**Library - Chore**
- [PR #608](https://github.com/twilio/twilio-python/pull/608): use Docker 'rc' tag for release candidate images. Thanks to [@childish-sambino](https://github.com/childish-sambino)!


[2022-05-18] Version 7.9.1
--------------------------
**Library - Fix**
- [PR #592](https://github.com/twilio/twilio-python/pull/592): Respect HTTPS_PROXY and other settings from env vars. Thanks to [@AlanCoding](https://github.com/AlanCoding)!

**Api**
- Add property `media_url` to the recording resources

**Verify**
- Include `silent` as a channel type in the verifications API.


[2022-05-04] Version 7.9.0
--------------------------
**Conversations**
- Expose query parameter `type` in list operation on Address Configurations resource

**Supersim**
- Add `data_total_billed` and `billed_units` fields to Super SIM UsageRecords API response.
- Change ESimProfiles `Eid` parameter to optional to enable Activation Code download method support **(breaking change)**

**Verify**
- Deprecate `push.include_date` parameter in create and update service.


[2022-04-20] Version 7.8.2
--------------------------
**Library - Fix**
- [PR #601](https://github.com/twilio/twilio-python/pull/601): Fixing logging of http request and response. Thanks to [@rakatyal](https://github.com/rakatyal)!


[2022-04-06] Version 7.8.1
--------------------------
**Library - Chore**
- [PR #600](https://github.com/twilio/twilio-python/pull/600): add jinja2 for make docs. Thanks to [@JenniferMah](https://github.com/JenniferMah)!
- [PR #599](https://github.com/twilio/twilio-python/pull/599): DI-1565 test case. Thanks to [@claudiachua](https://github.com/claudiachua)!
- [PR #597](https://github.com/twilio/twilio-python/pull/597): update user-agent string to standardize format. Thanks to [@claudiachua](https://github.com/claudiachua)!

**Library - Fix**
- [PR #593](https://github.com/twilio/twilio-python/pull/593): revise malformed __str__(self) function. Thanks to [@twilio-aiss](https://github.com/twilio-aiss)!

**Api**
- Updated `provider_sid` visibility to private

**Verify**
- Verify List Attempts API summary endpoint added.
- Update PII documentation for `AccessTokens` `factor_friendly_name` property.

**Voice**
- make annotation parameter from /Calls API private


[2022-03-23] Version 7.8.0
--------------------------
**Api**
- Change `stream` url parameter to non optional
- Add `verify-totp` and `verify-whatsapp-conversations-business-initiated` categories to `usage_record` API

**Chat**
- Added v3 Channel update endpoint to support Public to Private channel migration

**Flex**
- Private Beta release of the Interactions API to support the upcoming release of Flex Conversations at the end of Q1 2022.
- Adding `channel_configs` object to Flex Configuration

**Media**
- Add max_duration param to PlayerStreamer

**Supersim**
- Remove Commands resource, use SmsCommands resource instead **(breaking change)**

**Taskrouter**
- Add limits to `split_by_wait_time` for Cumulative Statistics Endpoint

**Video**
- Change recording `status_callback_method` type from `enum` to `http_method` **(breaking change)**
- Add `status_callback` and `status_callback_method` to composition
- Add `status_callback` and `status_callback_method` to recording


[2022-03-09] Version 7.7.1
--------------------------
**Library - Chore**
- [PR #591](https://github.com/twilio/twilio-python/pull/591): push Datadog Release Metric upon deploy success. Thanks to [@eshanholtz](https://github.com/eshanholtz)!

**Api**
- Add optional boolean include_soft_deleted parameter to retrieve soft deleted recordings

**Chat**
- Add `X-Twilio-Wehook-Enabled` header to `delete` method in UserChannel resource

**Numbers**
- Expose `failure_reason` in the Supporting Documents resources

**Verify**
- Add optional `metadata` parameter to "verify challenge" endpoint, so the SDK/App can attach relevant information from the device when responding to challenges.
- remove beta feature flag to list atempt api operations.
- Add `ttl` and `date_created` properties to `AccessTokens`.


[2022-02-23] Version 7.7.0
--------------------------
**Api**
- Add `uri` to `stream` resource
- Add A2P Registration Fee category (`a2p-registration-fee`) to usage records
- Detected a bug and removed optional boolean include_soft_deleted parameter to retrieve soft deleted recordings. **(breaking change)**
- Add optional boolean include_soft_deleted parameter to retrieve soft deleted recordings.

**Numbers**
- Unrevert valid_until and sort filter params added to List Bundles resource
- Revert valid_until and sort filter params added to List Bundles resource
- Update sorting params added to List Bundles resource in the previous release

**Preview**
- Moved `web_channels` from preview to beta under `flex-api` **(breaking change)**

**Taskrouter**
- Add `ETag` as Response Header to List of Task, Reservation & Worker

**Verify**
- Remove outdated documentation commentary to contact sales. Product is already in public beta.
- Add optional `metadata` to factors.

**Twiml**
- Add new Polly Neural voices


[2022-02-09] Version 7.6.0
--------------------------
**Library - Chore**
- [PR #589](https://github.com/twilio/twilio-python/pull/589): upgrade supported language versions. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Library - Test**
- [PR #588](https://github.com/twilio/twilio-python/pull/588): migrate to pytest for python 3.10 compatibility. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Add `stream` resource

**Conversations**
- Fixed DELETE request to accept "sid_like" params in Address Configuration resources **(breaking change)**
- Expose Address Configuration resource for `sms` and `whatsapp`

**Fax**
- Removed deprecated Programmable Fax Create and Update methods **(breaking change)**

**Insights**
- Rename `call_state` to `call_status` and remove `whisper` in conference participant summary **(breaking change)**

**Numbers**
- Expose valid_until filters as part of provisionally-approved compliance feature on the List Bundles resource

**Supersim**
- Fix typo in Fleet resource docs
- Updated documentation for the Fleet resource indicating that fields related to commands have been deprecated and to use sms_command fields instead.
- Add support for setting and reading `ip_commands_url` and `ip_commands_method` on Fleets resource for helper libraries
- Changed `sim` property in requests to create an SMS Command made to the /SmsCommands to accept SIM UniqueNames in addition to SIDs

**Verify**
- Update list attempts API to include new filters and response fields.


[2022-01-26] Version 7.5.1
--------------------------
**Insights**
- Added new endpoint to fetch Conference Participant Summary
- Added new endpoint to fetch Conference Summary

**Messaging**
- Add government_entity parameter to brand apis

**Verify**
- Add Access Token fetch endpoint to retrieve a previously created token.
- Add Access Token payload to the Access Token creation endpoint, including a unique Sid, so it's addressable while it's TTL is valid.


[2022-01-12] Version 7.5.0
--------------------------
**Library - Chore**
- [PR #587](https://github.com/twilio/twilio-python/pull/587): add sonarcloud integration. Thanks to [@BrimmingDev](https://github.com/BrimmingDev)!

**Library - Feature**
- [PR #586](https://github.com/twilio/twilio-python/pull/586): add GitHub release step during deploy. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Make fixed time scheduling parameters public **(breaking change)**

**Messaging**
- Add update brand registration API

**Numbers**
- Add API endpoint for List Bundle Copies resource

**Video**
- Enable external storage for all customers


[2021-12-15] Version 7.4.0
--------------------------
**Library - Feature**
- [PR #582](https://github.com/twilio/twilio-python/pull/582): run tests before deploying. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Add optional boolean send_as_mms parameter to the create action of Message resource **(breaking change)**
- Change team ownership for `call` delete

**Conversations**
- Change wording for `Service Webhook Configuration` resource fields

**Insights**
- Added new APIs for updating and getting voice insights flags by accountSid.

**Media**
- Add max_duration param to MediaProcessor

**Video**
- Add `EmptyRoomTimeout` and `UnusedRoomTimeout` properties to a room; add corresponding parameters to room creation

**Voice**
- Add endpoint to delete archived Calls


[2021-12-01] Version 7.3.2
--------------------------
**Conversations**
- Add `Service Webhook Configuration` resource

**Flex**
- Adding `flex_insights_drilldown` and `flex_url` objects to Flex Configuration

**Messaging**
- Update us_app_to_person endpoints to remove beta feature flag based access

**Supersim**
- Add IP Commands resource

**Verify**
- Add optional `factor_friendly_name` parameter to the create access token endpoint.

**Video**
- Add maxParticipantDuration param to Rooms

**Twiml**
- Unrevert Add supported SSML children to `<emphasis>`, `<lang>`, `<p>`, `<prosody>`, `<s>`, and `<w>`.
- Revert Add supported SSML children to `<emphasis>`, `<lang>`, `<p>`, `<prosody>`, `<s>`, and `<w>`.


[2021-11-17] Version 7.3.1
--------------------------
**Library - Fix**
- [PR #578](https://github.com/twilio/twilio-python/pull/578): git log retrieval issues. Thanks to [@shwetha-manvinkurke](https://github.com/shwetha-manvinkurke)!

**Frontline**
- Added `is_available` to User's resource

**Messaging**
- Added GET vetting API

**Verify**
- Add `WHATSAPP` to the attempts API.
- Allow to update `config.notification_platform` from `none` to `apn` or `fcm` and viceversa for Verify Push
- Add `none` as a valid `config.notification_platform` value for Verify Push

**Twiml**
- Add supported SSML children to `<emphasis>`, `<lang>`, `<p>`, `<prosody>`, `<s>`, and `<w>`.


[2021-11-03] Version 7.3.0
--------------------------
**Library - Chore**
- [PR #577](https://github.com/twilio/twilio-python/pull/577): migrate from travis ci to gh actions. Thanks to [@shwetha-manvinkurke](https://github.com/shwetha-manvinkurke)!

**Api**
- Updated `media_url` property to be treated as PII

**Messaging**
- Added a new enum for brand registration status named DELETED **(breaking change)**
- Add a new K12_EDUCATION use case in us_app_to_person_usecase api transaction
- Added a new enum for brand registration status named IN_REVIEW

**Serverless**
- Add node14 as a valid Build runtime

**Verify**
- Fix typos in Verify Push Factor documentation for the `config.notification_token` parameter.
- Added `TemplateCustomSubstitutions` on verification creation
- Make `TemplateSid` parameter public for Verification resource and `DefaultTemplateSid` parameter public for Service resource. **(breaking change)**


[2021-10-18] Version 7.2.0
--------------------------
**Library - Feature**
- [PR #576](https://github.com/twilio/twilio-python/pull/576): Add PlaybackGrant. Thanks to [@sarahcstringer](https://github.com/sarahcstringer)!

**Api**
- Corrected enum values for `emergency_address_status` values in `/IncomingPhoneNumbers` response. **(breaking change)**
- Clarify `emergency_address_status` values in `/IncomingPhoneNumbers` response.

**Messaging**
- Add PUT and List brand vettings api
- Removes beta feature flag based visibility for us_app_to_person_registered and usecase field.Updates test cases to add POLITICAL usecase. **(breaking change)**
- Add brand_feedback as optional field to BrandRegistrations

**Video**
- Add `AudioOnly` to create room


[2021-10-06] Version 7.1.0
--------------------------
**Api**
- Add `emergency_address_status` attribute to `/IncomingPhoneNumbers` response.
- Add `siprec` resource

**Conversations**
- Added attachment parameters in configuration for `NewMessage` type of push notifications

**Flex**
- Adding `flex_insights_hr` object to Flex Configuration

**Numbers**
- Add API endpoint for Bundle ReplaceItems resource
- Add API endpoint for Bundle Copies resource

**Serverless**
- Add domain_base field to Service response

**Taskrouter**
- Add `If-Match` Header based on ETag for Worker Delete **(breaking change)**
- Add `If-Match` Header based on Etag for Reservation Update
- Add `If-Match` Header based on ETag for Worker Update
- Add `If-Match` Header based on ETag for Worker Delete
- Add `ETag` as Response Header to Worker

**Trunking**
- Added `transfer_caller_id` property on Trunks.

**Verify**
- Document new pilot `whatsapp` channel.


[2021-09-22] Version 7.0.0
--------------------------
**Note:** This release contains breaking changes, check our [upgrade guide](./UPGRADE.md#2021-09-22-6xx-to-7xx) for detailed migration notes.

**Library - Fix**
- [PR #560](https://github.com/twilio/twilio-python/pull/560): update code and tests for pyjwt>=2.0.0. Thanks to [@karls](https://github.com/karls)! **(breaking change)**

**Library - Docs**
- [PR #570](https://github.com/twilio/twilio-python/pull/570): Add upgrade guide for dropping python 2.7, 3.4 & 3.5. Thanks to [@JenniferMah](https://github.com/JenniferMah)!

**Events**
- Add segment sink

**Messaging**
- Add post_approval_required attribute in GET us_app_to_person_usecase api response
- Add Identity Status, Russell 3000, Tax Exempt Status and Should Skip SecVet fields for Brand Registrations
- Add Should Skip Secondary Vetting optional flag parameter to create Brand API


[2021-09-08] Version 6.63.2
---------------------------
**Api**
- Revert adding `siprec` resource
- Add `siprec` resource

**Messaging**
- Add 'mock' as an optional field to brand_registration api
- Add 'mock' as an optional field to us_app_to_person api
- Adds more Use Cases in us_app_to_person_usecase api transaction and updates us_app_to_person_usecase docs

**Verify**
- Verify List Templates API endpoint added.


[2021-08-25] Version 6.63.1
---------------------------
**Api**
- Add Programmabled Voice SIP Refer call transfers (`calls-transfers`) to usage records
- Add Flex Voice Usage category (`flex-usage`) to usage records

**Conversations**
- Add `Order` query parameter to Message resource read operation

**Insights**
- Added `partial` to enum processing_state_request
- Added abnormal session filter in Call Summaries

**Messaging**
- Add brand_registration_sid as an optional query param for us_app_to_person_usecase api

**Pricing**
- add trunking_numbers resource (v2)
- add trunking_country resource (v2)

**Verify**
- Changed to private beta the `TemplateSid` optional parameter on Verification creation.
- Added the optional parameter `Order` to the list Challenges endpoint to define the list order.


[2021-08-11] Version 6.63.0
---------------------------
**Library - Fix**
- [PR #572](https://github.com/twilio/twilio-python/pull/572): fix sonar analysis. Thanks to [@shwetha-manvinkurke](https://github.com/shwetha-manvinkurke)!

**Library - Chore**
- [PR #571](https://github.com/twilio/twilio-python/pull/571): integrate with sonarcloud. Thanks to [@shwetha-manvinkurke](https://github.com/shwetha-manvinkurke)!

**Api**
- Corrected the `price`, `call_sid_to_coach`, and `uri` data types for Conference, Participant, and Recording **(breaking change)**
- Made documentation for property `time_limit` in the call api public. **(breaking change)**
- Added `domain_sid` in sip_credential_list_mapping and sip_ip_access_control_list_mapping APIs **(breaking change)**

**Insights**
- Added new endpoint to fetch Call Summaries

**Messaging**
- Add brand_type field to a2p brand_registration api
- Revert brand registration api update to add brand_type field
- Add brand_type field to a2p brand_registration api

**Taskrouter**
- Add `X-Rate-Limit-Limit`, `X-Rate-Limit-Remaining`, and `X-Rate-Limit-Config` as Response Headers to all TaskRouter endpoints

**Verify**
- Add `TemplateSid` optional parameter on Verification creation.
- Include `whatsapp` as a channel type in the verifications API.


[2021-07-28] Version 6.62.1
---------------------------
**Conversations**
- Expose ParticipantConversations resource

**Taskrouter**
- Adding `links` to the activity resource

**Verify**
- Added a `Version` to Verify Factors `Webhooks` to add new fields without breaking old Webhooks.


[2021-07-14] Version 6.62.0
---------------------------
**Conversations**
- Changed `last_read_message_index` and `unread_messages_count` type in User Conversation's resource **(breaking change)**
- Expose UserConversations resource

**Messaging**
- Add brand_score field to brand registration responses


[2021-06-30] Version 6.61.0
---------------------------
**Conversations**
- Read-only Conversation Email Binding property `binding`

**Supersim**
- Add Billing Period resource for the Super Sim Pilot
- Add List endpoint to Billing Period resource for Super Sim Pilot
- Add Fetch endpoint to Billing Period resource for Super Sim Pilot

**Taskrouter**
- Update `transcribe` & `transcription_configuration` form params in Reservation update endpoint to have private visibility **(breaking change)**
- Add `transcribe` & `transcription_configuration` form params to Reservation update endpoint

**Twiml**
- Add `modify` event to `statusCallbackEvent` for `<Conference>`.


[2021-06-16] Version 6.60.0
---------------------------
**Api**
- Update `status` enum for Messages to include 'canceled'
- Update `update_status` enum for Messages to include 'canceled'

**Trusthub**
- Corrected the sid for policy sid in customer_profile_evaluation.json and trust_product_evaluation.json **(breaking change)**


[2021-06-02] Version 6.59.1
---------------------------
**Events**
- join Sinks and Subscriptions service

**Verify**
- Improved the documentation of `challenge` adding the maximum and minimum expected lengths of some fields.
- Improve documentation regarding `notification` by updating the documentation of the field `ttl`.


[2021-05-19] Version 6.59.0
---------------------------
**Events**
- add query param to return types filtered by Schema Id
- Add query param to return sinks filtered by status
- Add query param to return sinks used/not used by a subscription

**Messaging**
- Add fetch and delete instance endpoints to us_app_to_person api **(breaking change)**
- Remove delete list endpoint from us_app_to_person api **(breaking change)**
- Update read list endpoint to return a list of us_app_to_person compliance objects **(breaking change)**
- Add `sid` field to Preregistered US App To Person response

**Supersim**
- Mark `unique_name` in Sim, Fleet, NAP resources as not PII

**Video**
- [Composer] GA maturity level


[2021-05-05] Version 6.58.0
---------------------------
**Api**
- Corrected the data types for feedback summary fields **(breaking change)**
- Update the conference participant create `from` and `to` param to be endpoint type for supporting client identifier and sip address

**Bulkexports**
- promoting API maturity to GA

**Events**
- Add endpoint to update description in sink
- Remove beta-feature account flag

**Messaging**
- Update `status` field in us_app_to_person api to `campaign_status` **(breaking change)**

**Verify**
- Improve documentation regarding `push` factor and include extra information about `totp` factor.


[2021-04-21] Version 6.57.0
---------------------------
**Api**
- Revert Update the conference participant create `from` and `to` param to be endpoint type for supporting client identifier and sip address
- Update the conference participant create `from` and `to` param to be endpoint type for supporting client identifier and sip address

**Bulkexports**
- moving enum to doc root for auto generating documentation
- adding status enum and default output properties

**Events**
- Change schema_versions prop and key to versions **(breaking change)**

**Messaging**
- Add `use_inbound_webhook_on_number` field in Service API for fetch, create, update, read

**Taskrouter**
- Add `If-Match` Header based on ETag for Task Delete

**Verify**
- Add `AuthPayload` parameter to support verifying a `Challenge` upon creation. This is only supported for `totp` factors.
- Add support to resend the notifications of a `Challenge`. This is only supported for `push` factors.

**Twiml**
- Add Polly Neural voices.


[2021-04-07] Version 6.56.0
---------------------------
**Api**
- Added `announcement` event to conference status callback events
- Removed optional property `time_limit` in the call create request. **(breaking change)**

**Messaging**
- Add rate_limits field to Messaging Services US App To Person API
- Add usecase field in Service API for fetch, create, update, read
- Add us app to person api and us app to person usecase api as dependents in service
- Add us_app_to_person_registered field in service api for fetch, read, create, update
- Add us app to person api
- Add us app to person usecase api
- Add A2P external campaign api
- Add Usecases API

**Supersim**
- Add Create endpoint to Sims resource

**Verify**
- The `Binding` field is now returned when creating a `Factor`. This value won't be returned for other endpoints.

**Video**
- [Rooms] max_concurrent_published_tracks has got GA maturity

**Twiml**
- Add `announcement` event to `statusCallbackEvent` for `<Conference>`.


[2021-03-24] Version 6.55.0
---------------------------
**Api**
- Added optional parameter `CallToken` for create calls api
- Add optional property `time_limit` in the call create request.

**Bulkexports**
- adding two new fields with job api queue_position and estimated_completion_time

**Events**
- Add new endpoints to manage subscribed_events in subscriptions

**Numbers**
- Remove feature flags for RegulatoryCompliance endpoints

**Supersim**
- Add SmsCommands resource
- Add fields `SmsCommandsUrl`, `SmsCommandsMethod` and `SmsCommandsEnabled` to a Fleet resource

**Taskrouter**
- Add `If-Match` Header based on ETag for Task Update
- Add `ETag` as Response Headers to Tasks and Reservations

**Video**
- Recording rule beta flag **(breaking change)**
- [Rooms] Add RecordingRules param to Rooms


[2021-03-15] Version 6.54.0
---------------------------
**Library - Chore**
- [PR #563](https://github.com/twilio/twilio-python/pull/563): Add support for python 3.9. Thanks to [@tim-schilling](https://github.com/tim-schilling)!

**Events**
- Set maturity to beta

**Messaging**
- Adjust A2P brand registration status enum **(breaking change)**

**Studio**
- Remove internal safeguards for Studio V2 API usage now that it's GA

**Verify**
- Add support for creating and verifying totp factors. Support for totp factors is behind the `api.verify.totp` beta feature.

**Twiml**
- Add support for `<VirtualAgent>` noun


[2021-02-24] Version 6.53.0
---------------------------
**Library - Chore**
- [PR #561](https://github.com/twilio/twilio-python/pull/561): removed file exec to get version. Thanks to [@shwetha-manvinkurke](https://github.com/shwetha-manvinkurke)!

**Events**
- Update description of types in the create sink resource

**Messaging**
- Add WA template header and footer
- Remove A2P campaign and use cases API **(breaking change)**
- Add number_registration_status field to read and fetch campaign responses

**Trusthub**
- Make all resources public

**Verify**
- Verify List Attempts API endpoints added.


[2021-02-10] Version 6.52.0
---------------------------
**Library - Docs**
- [PR #553](https://github.com/twilio/twilio-python/pull/553): fix simple typo, ommited -> omitted. Thanks to [@timgates42](https://github.com/timgates42)!

**Library - Fix**
- [PR #558](https://github.com/twilio/twilio-python/pull/558): shortcut syntax for new non-GA versions. Thanks to [@eshanholtz](https://github.com/eshanholtz)!

**Api**
- Revert change that conference participant create `from` and `to` param to be endpoint type for supporting client identifier and sip address
- Update the conference participant create `from` and `to` param to be endpoint type for supporting client identifier and sip address

**Events**
- Documentation should state that no fields are PII

**Flex**
- Adding `notifications` and `markdown` to Flex Configuration

**Messaging**
- Add A2P use cases API
- Add Brand Registrations API
- Add Campaigns API

**Serverless**
- Add runtime field to Build response and as an optional parameter to the Build create endpoint.
- Add @twilio/runtime-handler dependency to Build response example.

**Sync**
- Remove If-Match header for Document **(breaking change)**

**Twiml**
- Add `refer_url` and `refer_method` to `Dial`.


[2021-01-27] Version 6.51.1
---------------------------
**Studio**
- Studio V2 API is now GA

**Supersim**
- Allow updating `CommandsUrl` and `CommandsMethod` on a Fleet

**Twiml**
- Add `status_callback` and `status_callback_method` to `Stream`.


[2021-01-13] Version 6.51.0
---------------------------
**Library - Docs**
- [PR #555](https://github.com/twilio/twilio-python/pull/555): Fixing documentation for list parameter types. Thanks to [@shwetha-manvinkurke](https://github.com/shwetha-manvinkurke)!

**Library - Fix**
- [PR #552](https://github.com/twilio/twilio-python/pull/552): pin pyjwt dependency. Thanks to [@thinkingserious](https://github.com/thinkingserious)!

**Api**
- Add 'Electric Imp v1 Usage' to usage categories

**Conversations**
- Changed `last_read_message_index` type in Participant's resource **(breaking change)**

**Insights**
- Added `created_time` to call summary.

**Sync**
- Remove HideExpired query parameter for filtering Sync Documents with expired **(breaking change)**

**Video**
- [Rooms] Expose maxConcurrentPublishedTracks property in Room resource


[2020-12-16] Version 6.50.1
---------------------------
**Api**
- Updated `call_event` default_output_properties to request and response.

**Conversations**
- Added `last_read_message_index` and `last_read_timestamp` to Participant's resource update operation
- Added `is_notifiable` and `is_online` to User's resource
- Added `reachability_enabled` parameters to update method for Conversation Service Configuration resource

**Messaging**
- Added WA template quick reply, URL, and phone number buttons

**Twiml**
- Add `sequential` to `Dial`.


[2020-12-08] Version 6.50.0
---------------------------
**Api**
- Added optional `RecordingTrack` parameter for create calls, create participants, and create call recordings
- Removed deprecated Programmable Chat usage record categories **(breaking change)**

**Twiml**
- Add `recordingTrack` to `Dial`.


[2020-12-02] Version 6.49.0
---------------------------
**Library - Feature**
- [PR #546](https://github.com/twilio/twilio-python/pull/546): Regional twr header in the access token. Thanks to [@charliesantos](https://github.com/charliesantos)!

**Api**
- Remove `RecordingTrack` parameter for create calls, create participants, and create call recordings **(breaking change)**
- Added `RecordingTrack` parameter for create calls and create call recordings
- Add optional property `recording_track` in the participant create request

**Lookups**
- Changed `caller_name` and `carrier` properties type to object **(breaking change)**

**Trunking**
- Added dual channel recording options for Trunks.

**Twiml**
- Add `jitterBufferSize` and `participantLabel` to `Conference`.


[2020-11-18] Version 6.48.0
---------------------------
**Api**
- Add new call events resource - GET /2010-04-01/Accounts/{account_sid}/Calls/{call_sid}/Events.json

**Conversations**
- Fixed default response property issue for Service Notifications Configuration

**Insights**
- Removing call_sid from participant summary. **(breaking change)**

**Serverless**
- Allow Service unique name to be used in path (in place of SID) in Service update request

**Sync**
- Added HideExpired query parameter for filtering Sync Documents with expired

**Verify**
- Challenge `Details` and `HiddenDetails` properties are now marked as `PII`
- Challenge `expiration_date` attribute updated to set a default value of five (5) minutes and to allow max dates of one (1) hour after creation.
- Entity `identity` attribute updated to allow values between 8 and 64 characters.
- Verify Service frinedly_name attribute updated from 64 max lenght to 30 characters.


[2020-11-05] Version 6.47.0
---------------------------
**Library - Docs**
- [PR #544](https://github.com/twilio/twilio-python/pull/544): add debug logging example. Thanks to [@thinkingserious](https://github.com/thinkingserious)!

**Api**
- Added `verify-push` to `usage_record` API

**Bulkexports**
- When creating a custom export the StartDay, EndDay, and FriendlyName fields were required but this was not reflected in the API documentation.  The API itself failed the request without these fields. **(breaking change)**
- Added property descriptions for Custom Export create method
- Clarified WebhookUrl and WebhookMethod must be provided together for Custom Export

**Insights**
- Added video room and participant summary apis.

**Ip_messaging**
- Create separate definition for ip-messaging
- Restore v2 endpoints for ip-messaging

**Verify**
- Verify Push madurity were updated from `preview` to `beta`
- `twilio_sandbox_mode` header was removed from Verify Push resources **(breaking change)**

**Video**
- [Rooms] Add Recording Rules API


[2020-10-14] Version 6.46.0
---------------------------
**Library - Docs**
- [PR #542](https://github.com/twilio/twilio-python/pull/542): add path limit error for windows. Thanks to [@hack3r-0m](https://github.com/hack3r-0m)!

**Ai**
- Add `Annotation Project` and `Annotation Task` endpoints
- Add `Primitives` endpoints
- Add `meta.total` to the search endpoint

**Conversations**
- Mutable Conversation Unique Names

**Insights**
- Added `trust` to summary.

**Preview**
- Simplified `Channels` resource. The path is now `/BrandedChannels/branded_channel_sid/Channels` **(breaking change)**

**Verify**
- Changed parameters (`config` and `binding`) to use dot notation instead of JSON string (e.i. Before: `binding={"alg":"ES256", "public_key": "xxx..."}`, Now: `Binding.Alg="ES256"`, `Binding.PublicKey="xxx..."`). **(breaking change)**
- Changed parameters (`details` and `hidden_details`) to use dot notation instead of JSON string (e.i. Before: `details={"message":"Test message", "fields": "[{\"label\": \"Action 1\", \"value\":\"value 1\"}]"}`, Now: `details.Message="Test message"`, `Details.Fields=["{\"label\": \"Action 1\", \"value\":\"value 1\"}"]`). **(breaking change)**
- Removed `notify_service_sid` from `push` service configuration object. Add `Push.IncludeDate`, `Push.ApnCredentialSid` and `Push.FcmCredentialSid` service configuration parameters. **(breaking change)**


[2020-09-28] Version 6.45.4
---------------------------
**Library - Docs**
- [PR #541](https://github.com/twilio/twilio-python/pull/541): Fix pip download link. Thanks to [@swarnava](https://github.com/swarnava)!

**Api**
- Add optional property `call_reason` in the participant create request
- Make sip-domain-service endpoints available in stage-au1 and prod-au1

**Messaging**
- Removed beta feature gate from WhatsApp Templates API

**Serverless**
- Add Build Status endpoint

**Video**
- [Rooms] Add new room type "go" for WebRTC Go


[2020-09-21] Version 6.45.3
---------------------------
**Library - Fix**
- [PR #540](https://github.com/twilio/twilio-python/pull/540): allow API redirect responses. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Accounts**
- Add Auth Token rotation API

**Conversations**
- Change resource path for Webhook Configuration

**Events**
- Schemas API get all Schemas names and versions


[2020-09-16] Version 6.45.2
---------------------------
**Conversations**
- Expose Configuration and Service Configuration resources
- Add Unique Name support for Conversations
- Add Services Push Notification resource
- Add Service scoped Conversation resources
- Support Identity in Users resource endpoint

**Messaging**
- GA Deactivation List API
- Add domain cert API's(fetch, update, create) for link tracker

**Numbers**
- Add API endpoint for Supporting Document deletion

**Proxy**
- Updated usage of FailOnParticipantConflict param to apply only to accounts with ProxyAllowParticipantConflict account flag

**Supersim**
- Add `AccountSid` parameter to Sim resource update request
- Add `ready` status as an available status for a Sim resource


[2020-09-02] Version 6.45.1
---------------------------
**Library - Docs**
- [PR #538](https://github.com/twilio/twilio-python/pull/538): convert markdown links to rst formatted links. Thanks to [@thinkingserious](https://github.com/thinkingserious)!

**Ai**
- Initial release

**Bulkexports**
- removing public beta feature flag from BulkExports Jobs API

**Messaging**
- Add Deactivation List API
- Added page token parameter for fetch in WhatsApp Templates API

**Numbers**
- Add API endpoint for End User deletion

**Routes**
- Add Resource Route Configurations API
- Add Route Configurations API
- Initial Release

**Trunking**
- Added `transfer_mode` property on Trunks.


[2020-08-19] Version 6.45.0
---------------------------
**Library - Chore**
- [PR #536](https://github.com/twilio/twilio-python/pull/536): update GitHub branch references to use HEAD. Thanks to [@thinkingserious](https://github.com/thinkingserious)!

**Conversations**
- Allow Identity addition to Participants

**Events**
- Sinks API Get all Sinks

**Proxy**
- Clarified usage of FailOnParticipantConflict param as experimental
- Add FailOnParticipantConflict param to Proxy Session create and Proxy Participant create

**Supersim**
- Add fleet, network, and isoCountryCode to the UsageRecords resource
- Change sort order of UsageRecords from ascending to descending with respect to start time field, records are now returned newest to oldest

**Wireless**
- Removed `Start` and `End` parameters from the Data Sessions list endpoint. **(breaking change)**


[2020-08-05] Version 6.44.2
---------------------------
**Messaging**
- Add rejection reason support to WhatsApp API
- Removed status parameter for create and update in WhatsApp Templates API

**Proxy**
- Add FailOnParticipantConflict param to Proxy Session update

**Verify**
- Add `CustomFriendlyName` optional parameter on Verification creation.
- Changes in `Challenge` resource to update documentation of both `details` and `hidden_details` properties.


[2020-07-22] Version 6.44.1
---------------------------
**Api**
- Add optional Click Tracking and Scheduling parameters to Create action of Message resource

**Supersim**
- Add callback_url and callback_method parameters to Sim resource update request


[2020-07-08] Version 6.44.0
---------------------------
**Library - Feature**
- [PR #528](https://github.com/twilio/twilio-python/pull/528): include API response headers in 'Last Response'. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Conversations**
- Allow Address updates for Participants
- Message delivery receipts

**Events**
- Add account_sid to subscription and subscribed_events resources

**Flex**
- Changed `wfm_integrations` Flex Configuration key to private **(breaking change)**

**Messaging**
- Add error states to WhatsApp Sender status with failed reason **(breaking change)**
- Delete WhatsApp Template API
- Update WhatsApp Template API
- Add WhatsApp Template Get Api (fetch and read)

**Numbers**
- Add `valid_until` in the Bundles resource
- Add API for Bundle deletion

**Verify**
- Removed support for `sms`, `totp` and `app-push` factor types in Verify push **(breaking change)**


[2020-06-24] Version 6.43.0
---------------------------
**Api**
- Added optional `JitterBufferSize` parameter for creating conference participant
- Added optional `label` property for conference participants
- Added optional parameter `caller_id` for creating conference participant endpoint.

**Autopilot**
- Remove Export resource from Autopilot Assistant

**Conversations**
- Expose Conversation timers

**Monitor**
- Update start/end date filter params to support date-or-time format **(breaking change)**

**Numbers**
- Add `provisionally-approved` as a Supporting Document status

**Preview**
- Removed `Authy` resources. **(breaking change)**

**Supersim**
- Add ready state to the allowed transitions in the sim update call behind the feature flag supersim.ready-state.v1

**Verify**
- Webhook resources added to Verify services and put behind the `api.verify.push` beta feature

**Twiml**
- Add more supported locales for the `Gather` verb.


[2020-06-10] Version 6.42.0
---------------------------
**Library - Docs**
- [PR #525](https://github.com/twilio/twilio-python/pull/525): link to handling exceptions. Thanks to [@thinkingserious](https://github.com/thinkingserious)!
- [PR #524](https://github.com/twilio/twilio-python/pull/524): link to custom HTTP client instructions. Thanks to [@thinkingserious](https://github.com/thinkingserious)!

**Library - Fix**
- [PR #523](https://github.com/twilio/twilio-python/pull/523): drop the page limit calculation and correct the page limit stop condition. Thanks to [@childish-sambino](https://github.com/childish-sambino)!
- [PR #522](https://github.com/twilio/twilio-python/pull/522): drop passing a page limit when listing/streaming resources. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Added `pstnconnectivity` to `usage_record` API

**Autopilot**
- Add dialogue_sid param to Query list resource

**Notify**
- delivery_callback_url and delivery_callback_enabled added

**Numbers**
- Add `provisionally-approved` as a Bundle status

**Preview**
- `BrandsInformation` endpoint now returns a single `BrandsInformation`
- Deleted phone number required field in the brand phone number endpoint from `kyc-api`
- Removed insights `preview API` from API Definitions **(breaking change)**
- Added `BrandsInformation` endpoint to query brands information stored in KYC

**Supersim**
- Require a Network Access Profile when creating a Fleet **(breaking change)**


[2020-05-27] Version 6.41.0
---------------------------
**Api**
- Added `reason_conference_ended` and `call_sid_ending_conference` to Conference read/fetch/update
- Fixed some examples to use the correct "TK" SID prefix for Trunk resources.

**Authy**
- Renamed `twilio_authy_sandbox_mode` headers to `twilio_sandbox_mode` **(breaking change)**
- Renamed `Twilio-Authy-*` headers to `Twilio-Veriry-*` **(breaking change)**

**Flex**
- Adding `flex_service_instance_sid` to Flex Configuration

**Preview**
- Removed insights preview API from API Definitions **(breaking change)**
- Added `Channels` endpoint to brand a phone number for BrandedCalls

**Serverless**
- Add Build Sid to Log results

**Supersim**
- Add Network Access Profile resource Networks subresource
- Allow specifying a Data Limit on Fleets

**Trunking**
- Fixed some examples to use the correct "TK" SID prefix for Trunk resources.


[2020-05-13] Version 6.40.0
---------------------------
**Library - Feature**
- [PR #520](https://github.com/twilio/twilio-python/pull/520): add regional and edge support. Thanks to [@eshanholtz](https://github.com/eshanholtz)!

**Api**
- Add optional `emergency_caller_sid` parameter to SIP Domain
- Updated `call_reason` optional property to be treated as PII
- Added optional BYOC Trunk Sid property to Sip Domain API resource

**Autopilot**
- Add Restore resource to Autopilot Assistant

**Contacts**
- Added contacts Create API definition

**Events**
- Subscriptions API initial release

**Numbers**
- Add Evaluations API

**Supersim**
- Allow filtering the Fleets resource by Network Access Profile
- Allow assigning a Network Access Profile when creating and updating a Fleet
- Add Network Access Profiles resource

**Verify**
- Add `CustomCode` optional parameter on Verification creation.
- Add delete action on Service resource.

**Voice**
- Added endpoints for BYOC trunks, SIP connection policies and source IP mappings


[2020-04-29] Version 6.39.0
---------------------------
**Library - Feature**
- [PR #517](https://github.com/twilio/twilio-python/pull/517): add details to TwilioRestException. Thanks to [@ashish-s](https://github.com/ashish-s)!

**Preview**
- Added `Dispatch` version to `preview`

**Studio**
- Reroute Create Execution for V2 to the V2 downstream

**Supersim**
- Add Networks resource


[2020-04-15] Version 6.38.1
---------------------------
**Library - Chore**
- [PR #513](https://github.com/twilio/twilio-python/pull/513): remove S3 URLs from test data. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Updated description for property `call_reason` in the call create request

**Contacts**
- Added Read, Delete All, and Delete by SID docs
- Initial Release

**Studio**
- Rename `flow_valid` to `flow_validate`
- Removed `errors` and `warnings` from flows error response and added new property named `details`
- Add Update Execution endpoints to v1 and v2 to end execution via API
- Add new `warnings` attribute v2 flow POST api

**Twiml**
- Add enhanced attribute to use with `speech_model` for the `Gather` verb


[2020-04-01] Version 6.38.0
---------------------------
**Api**
- Add optional 'secure' parameter to SIP Domain

**Authy**
- Added an endpoint to list the challenges of a factor
- Added optional parameter `Push` when updating a service to send the service level push factor configuration

**Bulkexports**
- exposing bulk exports (vault/slapchop) API as public beta API

**Flex**
- Adding `queue_stats_configuration` and `wfm_integrations` to Flex Configuration

**Serverless**
- Add Function Version Content endpoint
- Allow build_sid to be optional for deployment requests

**Supersim**
- Remove `deactivated` status for Super SIM which is replaced by `inactive` **(breaking change)**


[2020-03-18] Version 6.37.0
---------------------------
**Api**
- Add optional `emergency_calling_enabled` parameter to SIP Domain
- Add optional property `call_reason` in the call create request

**Authy**
- Added `friendly_name` and `config` as optional params to Factor update
- Added `config` param to Factor creation **(breaking change)**

**Preview**
- Renamed `SuccessRate` endpoint to `ImpressionsRate` for Branded Calls (fka. Verified by Twilio) **(breaking change)**


[2020-03-04] Version 6.36.0
---------------------------
**Library - Feature**
- [PR #507](https://github.com/twilio/twilio-python/pull/507): add new max_retries param to TwilioHttpClient. Thanks to [@msaelices](https://github.com/msaelices)!

**Authy**
- Added the `configuration` property to services to return the service level configurations
- Added optional parameter `Push` when creating a service to send the service level push factor configuration
- Remove FactorStrength support for Factors and Challenges **(breaking change)**

**Messaging**
- Correct the alpha sender capabilities property type **(breaking change)**

**Preview**
- Removed `/Devices` register Branded Calls endpoint, as per iOS sample app deprecation **(breaking change)**
- Removed `Twilio-Sandbox-Mode` request header from the Branded Calls endpoints, as not officially supported **(breaking change)**
- Removed `Verify` version from `preview` subdomain in favor to `verify` subdomain. **(breaking change)**

**Serverless**
- Add UI-Editable field to Services

**Supersim**
- Add `inactive` status for Super SIM which is an alias for `deactivated`

**Taskrouter**
- Adding value range to `priority` in task endpoint

**Verify**
- Fix `SendCodeAttempts` type. It's an array of objects instead of a unique object. **(breaking change)**


[2020-02-19] Version 6.35.5
---------------------------
**Api**
- Make call create parameters `async_amd`, `async_amd_status_callback`, and `async_amd_status_callback_method` public
- Add `trunk_sid` as an optional field to Call resource fetch/read responses
- Add property `queue_time` to successful response of create, fetch, and update requests for Call
- Add optional parameter `byoc` to conference participant create.

**Authy**
- Added support for challenges associated to push factors

**Flex**
- Adding `ui_dependencies` to Flex Configuration

**Messaging**
- Deprecate Session API **(breaking change)**

**Numbers**
- Add Regulations API

**Studio**
- Add Execution and Step endpoints to v2 API
- Add webhook_url to Flow response and add new /TestUsers endpoint to v2 API

**Taskrouter**
- Adding `longest_relative_task_age_in_queue` and `longest_relative_task_sid_in_queue` to TaskQueue Real Time Statistics API.
- Add `wait_duration_in_queue_until_accepted` aggregations to TaskQueues Cumulative Statistics endpoint
- Add TaskQueueEnteredDate property to Tasks.

**Video**
- [Composer] Clarification for the composition hooks creation documentation: one source is mandatory, either the `audio_sources` or the `video_layout`, but one of them has to be provided
- [Composer] `audio_sources` type on the composer HTTP POST command, changed from `sid[]` to `string[]` **(breaking change)**
- [Composer] Clarification for the composition creation documentation: one source is mandatory, either the `audio_sources` or the `video_layout`, but one of them has to be provided


[2020-02-05] Version 6.35.4
---------------------------
**Api**
- Making content retention and address retention public
- Update `status` enum for Messages to include 'partially_delivered'

**Authy**
- Added support for push factors

**Autopilot**
- Add one new property in Query i.e dialogue_sid

**Verify**
- Add `SendCodeAttempts` to create verification response.

**Video**
- Clarification in composition creation documentation: one source is mandatory, either `audio_sources` or `video_layout`, but on of them has to be provided

**Twiml**
- Add Polly Neural voices.


[2020-01-22] Version 6.35.3
---------------------------
**Library - Docs**
- [PR #504](https://github.com/twilio/twilio-python/pull/504): baseline all the templated markdown docs. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Add payments public APIs
- Add optional parameter `byoc` to call create request.

**Flex**
- Updating a Flex Flow `creation_on_message` parameter documentation

**Preview**
-
- Removed Verify v2 from preview in favor of its own namespace as GA **(breaking change)**

**Studio**
- Flow definition type update from string to object

**Verify**
- Add `AppHash` parameter when creating a Verification.
- Add `DoNotShareWarningEnabled` parameter to the Service resource.

**Twiml**
- Add `track` attribute to siprec noun.
- Add attribute `byoc` to `<Number>`


[2020-01-08] Version 6.35.2
---------------------------
**Numbers**
- Add Regulatory Compliance CRUD APIs

**Studio**
- Add parameter validation for Studio v2 Flows API

**Twiml**
- Add support for `speech_model` to `Gather` verb


[2019-12-18] Version 6.35.1
---------------------------
**Preview**
- Add `/Insights/SuccessRate` endpoint for Businesses Branded Calls (Verified by Twilio)

**Studio**
- StudioV2 API in beta

**Verify**
- Add `MailerSid` property to Verify Service resource.

**Wireless**
- Added `data_limit_strategy` to Rate Plan resource.


[2019-12-12] Version 6.35.0
---------------------------
**Library**
- [PR #500](https://github.com/twilio/twilio-python/pull/500): feat: support http proxy in TwilioHttpClient. Thanks to [@thehackercat](https://github.com/thehackercat)!

**Api**
- Make `twiml` conditional for create. One of `url`, `twiml`, or `application_sid` is now required.
- Add `bundle_sid` parameter to /IncomingPhoneNumbers API
- Removed discard / obfuscate parameters from ContentRetention, AddressRetention **(breaking change)**

**Chat**
- Added `last_consumed_message_index` and `last_consumption_timestamp` parameters in update method for UserChannel resource **(breaking change)**

**Conversations**
- Add Participant SID to Message properties

**Messaging**
- Fix incorrectly typed capabilities property for ShortCodes. **(breaking change)**


[2019-12-04] Version 6.34.0
---------------------------
**Library**
- [PR #501](https://github.com/twilio/twilio-python/pull/501): BREAKING CHANGE feat: add custom HTTP header support. Thanks to [@eshanholtz](https://github.com/eshanholtz)! **(breaking change)**
- [PR #502](https://github.com/twilio/twilio-python/pull/502): fix: regenerate python lib with yoyodyne refactor. Thanks to [@eshanholtz](https://github.com/eshanholtz)!
- [PR #499](https://github.com/twilio/twilio-python/pull/499): docs: add supported language versions to README. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Api**
- Add optional `twiml` parameter for call create

**Chat**
- Added `delete` method in UserChannel resource

**Conversations**
- Allow Messaging Service update

**Taskrouter**
- Support ReEvaluateTasks parameter on Workflow update

**Twiml**
- Remove unsupported `mixed_track` value from `<Stream>` **(breaking change)**
- Add missing fax `<Receive>` optional attributes


[2019-11-13] Version 6.33.1
---------------------------
**Library**
- [PR #498](https://github.com/twilio/twilio-python/pull/498): docs: Add local testing docs. Thanks to [@childish-sambino](https://github.com/childish-sambino)!
- [PR #497](https://github.com/twilio/twilio-python/pull/497): fix: Resolve some bug risks and code quality issues. Thanks to [@sanketsaurav](https://github.com/sanketsaurav)!
- [PR #495](https://github.com/twilio/twilio-python/pull/495): Rename child twiml methods to be the tag name and deprecate old methods. Thanks to [@eshanholtz](https://github.com/eshanholtz)!
- [PR #490](https://github.com/twilio/twilio-python/pull/490): fix: Change ObsoleteException to inherit from Exception instead of BaseException. Thanks to [@fefi95](https://github.com/fefi95)!

**Api**
- Make `persistent_action` parameter public
- Add `twiml` optional private parameter for call create
- Update the call `price` property type to be string **(breaking change)**

**Autopilot**
- Add Export resource to Autopilot Assistant.

**Flex**
- Added Integration.RetryCount attribute to Flex Flow
- Updating a Flex Flow `channel_type` options documentation

**Insights**
- Added edges to events and metrics
- Added new endpoint definitions for Events and Metrics

**Messaging**
- **create** support for sender registration
- **fetch** support for fetching a sender
- **update** support for sender verification

**Supersim**
- Add `Direction` filter parameter to list commands endpoint
- Allow filtering commands list by Sim Unique Name
- Add `Iccid` filter parameter to list sims endpoint

**Twiml**
- Add support for `<Refer>` verb


[2019-10-30] Version 6.33.0
---------------------------
**Library**
- [PR #414](https://github.com/twilio/twilio-python/pull/414): Add support for passing custom logger into TwilioHttpClient. Thanks to [@tysonholub](https://github.com/tysonholub)!
- [PR #423](https://github.com/twilio/twilio-python/pull/423): Document exception case in README. Thanks to [@prateem](https://github.com/prateem)!
- [PR #489](https://github.com/twilio/twilio-python/pull/489): Include the license file when packaging the library. Thanks to [@marcelotrevisani](https://github.com/marcelotrevisani)!
- [PR #485](https://github.com/twilio/twilio-python/pull/485): Adding timeout to TwilioHttpClient constructor. Thanks to [@Kerl1310](https://github.com/Kerl1310)!
- [PR #488](https://github.com/twilio/twilio-python/pull/488): Update resources after sorting. Thanks to [@childish-sambino](https://github.com/childish-sambino)!
- [PR #486](https://github.com/twilio/twilio-python/pull/486): Declare support for Python 3.8. Thanks to [@Jamim](https://github.com/Jamim)!

**Api**
- Add new usage categories to the public api `sms-messages-carrierfees` and `mms-messages-carrierfees`

**Conversations**
- Add ProjectedAddress to Conversations Participant resource

**Preview**
- Implemented different `Sid` for Current Calls (Verified by Twilio), instead of relying in `Call.Sid` from Voice API team **(breaking change)**

**Supersim**
- Add List endpoint to Commands resource for Super Sim Pilot
- Add UsageRecords resource for the Super Sim Pilot
- Add List endpoint to UsageRecords resource for the Super Sim Pilot
- Allow assigning a Sim to a Fleet by Fleet SID or Unique Name for Super SIM Pilot
- Add Update endpoint to Fleets resource for Super Sim Pilot
- Add Fetch endpoint to Commands resource for Super Sim Pilot
- Allow filtering the Sims resource List endpoint by Fleet
- Add List endpoint to Fleets resource for Super Sim Pilot

**Wireless**
- Added `account_sid` to Sim update parameters.

**Twiml**
- Add new locales and voices for `Say` from Polly


[2019-10-16] Version 6.32.0
---------------------------
**Library**
- [PR #482](https://github.com/twilio/twilio-python/pull/482): Update a few property types in the lookups and trunking responses. Thanks to [@childish-sambino](https://github.com/childish-sambino)!
- [PR #483](https://github.com/twilio/twilio-python/pull/483): Update instance property marshaling to allow missing properties. Thanks to [@childish-sambino](https://github.com/childish-sambino)!
- [PR #484](https://github.com/twilio/twilio-python/pull/484): Feature/remove socks dependency. Thanks to [@Kerl1310](https://github.com/Kerl1310)!
- [PR #481](https://github.com/twilio/twilio-python/pull/481): Change typehint for `PhoneNumberInstance.carrier`. Thanks to [@NCPlayz](https://github.com/NCPlayz)!
- [PR #480](https://github.com/twilio/twilio-python/pull/480): Auto-deploy via Travis CI upon tagged commit to master. Thanks to [@thinkingserious](https://github.com/thinkingserious)!
- [PR #479](https://github.com/twilio/twilio-python/pull/479): breaking: Correct video composition date types. Thanks to [@childish-sambino](https://github.com/childish-sambino)! **(breaking change)**

**Api**
- Add new property `attempt` to sms_messages
- Fixed a typo in the documentation for Feedback outcome enum **(breaking change)**
- Update the call price to be optional for deserializing **(breaking change)**

**Flex**
- Added `JanitorEnabled` attribute to Flex Flow
- Change `features_enabled` Flex Configuration key to private **(breaking change)**

**Supersim**
- Add Fetch endpoint to Fleets resource for Super Sim Pilot
- Allow assigning a Sim to a Fleet for Super Sim Pilot
- Add Create endpoint to Fleets resource for Super Sim Pilot

**Twiml**
- Update `<Conference>` rename "whisper" attribute to "coach" **(breaking change)**


[2019-10-02] Version 6.31.1
---------------------------
**Library**
- [PR #477](https://github.com/twilio/twilio-python/pull/477): added validation of signature without stripping port number. Thanks to [@eshanholtz](https://github.com/eshanholtz)!

**Conversations**
- Add media to Conversations Message resource

**Supersim**
- Add List endpoint to Sims resource for Super Sim Pilot


[2019-09-18] Version 6.31.0
----------------------------
**Numbers**
- Add v2 of the Identites API

**Preview**
- Changed authentication method for SDK Trusted Comms endpoints: `/CPS`, `/CurrentCall`, and `/Devices`. Please use `Authorization: Bearer <xCNAM JWT>` **(breaking change)**

**Voice**
- Add Recordings endpoints


[2019-09-04] Version 6.30.0
----------------------------
**Api**
-  Pass Twiml in call update request

**Conversations**
- Add attributes to Conversations resources

**Flex**
- Adding `features_enabled` and `serverless_service_sids` to Flex Configuration

**Messaging**
- Message API required params updated **(breaking change)**

**Preview**
- Added support for the optional `CallSid` to `/BrandedCalls` endpoint


[2019-08-21] Version 6.29.4
----------------------------
**Library**
- [PR #474](https://github.com/twilio/twilio-python/pull/474): Use PyJWT version >= 1.4.2 in requirements.txt. Thanks to [@storymode7](https://github.com/storymode7)!
- [PR #473](https://github.com/twilio/twilio-python/pull/473): Update the IP messaging domain name to be 'chat'. Thanks to [@childish-sambino](https://github.com/childish-sambino)!

**Conversations**
- Add Chat Conversation SID to conversation default output properties

**Flex**
- Adding `outbound_call_flows` object to Flex Configuration
- Adding read and fetch to channels API

**Supersim**
- Add Sims and Commands resources for the Super Sim Pilot

**Sync**
- Added configuration option for enabling webhooks from REST.

**Wireless**
- Added `usage_notification_method` and `usage_notification_url` properties to `rate_plan`.

**Twiml**
- Add support for `ach-debit` transactions in `Pay` verb


[2019-08-05] Version 6.29.3
----------------------------
**Preview**
- Added support for the header `Twilio-Sandbox-Mode` to mock all Voice dependencies

**Twiml**
- Add support for `<Siprec>` noun
- Add support for `<Stream>` noun
- Create verbs `<Start>` and `<Stop>`


[2019-07-24] Version 6.29.2
----------------------------
**Insights**
- Added `properties` to summary.

**Preview**
- Added endpoint to brand a call without initiating it, so it can be initiated manually by the Customer

**Twiml**
- Update `<Conference>` recording events **(breaking change)**


[2019-07-10] Version 6.29.1
----------------------------
**Api**
- Make `friendly_name` optional for applications create
- Add new property `as_of` date to Usage Record API calls

**Wireless**
- Added Usage Records resource.


[2019-06-26] Version 6.29.0
----------------------------
**Autopilot**
- Adds two new properties in Assistant i.e needs_model_build and development_stage

**Preview**
- Changed phone numbers from _URL|Path_ to `X-XCNAM-Sensitive` headers **(breaking change)**

**Verify**
- Add `MessagingConfiguration` resource to verify service


[2019-06-12] Version 6.28.0
----------------------------
**Autopilot**
- Add Webhooks resource to Autopilot Assistant.

**Flex**
- Added missing 'custom' type to Flex Flow
- Adding `integrations` to Flex Configuration

**Insights**
- Added attributes to summary.

**Messaging**
- Message API Create updated with conditional params **(breaking change)**

**Proxy**
- Document that Proxy will return a maximum of 100 records for read/list endpoints **(breaking change)**
- Remove non-updatable property parameters for Session update (mode, participants) **(breaking change)**

**Sync**
- Added reachability debouncing configuration options.

**Verify**
- Add `RateLimits` and `Buckets` resources to Verify Services
- Add `RateLimits` optional parameter on `Verification` creation.

**Twiml**
- Fix `<Room>` participantIdentity casing


[2019-05-29] Version 6.27.1
----------------------------
**Verify**
- Add `approved` to status enum


[2019-05-15] Version 6.27.0
----------------------------
**Api**
- Make `method` optional for queue members update

**Chat**
- Removed `webhook.*.format` update parameters in Service resource from public library visibility in v1 **(breaking change)**

**Insights**
- Added client metrics as sdk_edge to summary.
- Added optional query param processing_state.

**Numbers**
- Add addtional metadata fields on a Document
- Add status callback fields and parameters

**Taskrouter**
- Added `channel_optimized_routing` attribute to task-channel endpoint

**Video**
- [Rooms] Add Video Subscription API

**Wireless**
- Added `imei` to Data Session resource.
- Remove `imeisv` from Data Session resource. **(breaking change)**


[2019-05-01] Version 6.26.3
----------------------------
**Serverless**
- Documentation

**Wireless**
- Added `imeisv` to Data Session resource.


[2019-04-24] Version 6.26.2
----------------------------
**Library**
- PR #465: Prepend the repo root to the system paths during doc generation. Thanks to @childish-sambino!
- PR #463: Migrate the README to markdown. Thanks to @childish-sambino!

**Api**
- Add `verified` property to Addresses

**Numbers**
- Add API for Identites and documents

**Proxy**
- Add in use count on number instance


[2019-04-12] Version 6.26.1
----------------------------
**Library**
- PR #459: Add py37 to TravisCI config. Thanks to @childish-sambino!
- PR #458: Make the Yoyodyne watermark a raw string. Thanks to @childish-sambino!

**Flex**
- Adding PluginService to Flex Configuration

**Numbers**
- Add API for Proof of Addresses

**Proxy**
- Clarify documentation for Service and Session fetch

**Serverless**
- Serverless scaffolding


[2019-03-28] Version 6.26.0
----------------------------
**Api**
- Remove optional `if_machine` call create parameter from helper libraries **(breaking change)**
- Changed `call_sid` path parameter type on QueueMember fetch and update requests **(breaking change)**

**Voice**
- changed file names to dialing_permissions prefix **(breaking change)**

**Wireless**
- Added `ResetStatus` property to Sim resource to allow resetting connectivity via the API.


[2019-03-15] Version 6.25.2
----------------------------
**Library**
- PR #457: Add Help Center and Support Ticket links to the README. Thanks to @childish-sambino!

**Api**
- Add `machine_detection_speech_threshold`, `machine_detection_speech_end_threshold`, `machine_detection_silence_timeout` optional params to Call create request

**Flex**
- Adding Flex Channel Orchestration
- Adding Flex Flow


[2019-03-06] Version 6.25.1
----------------------------
**Twiml**
- Add `de1` to `<Conference>` regions


[2019-03-01] Version 6.25.0
----------------------------
**Api**
- Make conference participant preview parameters public

**Authy**
- Added support for FactorType and FactorStrength for Factors and Challenges

**Iam**
- First public release

**Verify**
- Add endpoint to update/cancel a Verification **(breaking change)**

**Video**
- [Composer] Make RoomSid mandatory **(breaking change)**
- [Composer] Add `enqueued` state to Composition

**Twiml**
- Update message body to not be required for TwiML `Dial` noun.


[2019-02-15] Version 6.24.1
----------------------------
**Api**
- Add `force_opt_in` optional param to Messages create request
- Add agent conference category to usage records

**Flex**
- First public release

**Taskrouter**
- Adding `reject_pending_reservations` to worker update endpoint
- Added `event_date_ms` and `worker_time_in_previous_activity_ms` to Events API response
- Add ability to filter events by TaskChannel

**Verify**
- Add `EnablePsd2` optional parameter for PSD2 on Service resource creation or update.
- Add `Amount`, `Payee` optional parameters for PSD2.


[2019-02-04] Version 6.24.0
----------------------------
**Library**
- PR #453: Switch body validator to use hex instead of base64. Thanks to @cjcodes!

**Video**
- [Recordings] Add media type filter to list operation
- [Composer] Filter Composition Hook resources by FriendlyName

**Twiml**
- Update `language` enum for `Gather` to fix language code for Filipino (Philippines) and include additional supported languages **(breaking change)**


[2019-01-11] Version 6.23.1
----------------------------
**Verify**
- Add `lookup` information in the response when creating a new verification (depends on the LookupEnabled flag being enabled at the service level)
- Add `VerificationSid` optional parameter on Verification check.


[2019-01-10] Version 6.23.0
----------------------------
**Chat**
- Mark Member attributes as PII

**Proxy**
- Remove unsupported query parameters **(breaking change)**
- Remove invalid session statuses in doc


[2019-01-02] Version 6.22.1
----------------------------
**Insights**
- Initial revision.


[2018-12-17] Version 6.22.0
----------------------------
**Authy**
- Reverted the change to `FactorType` and `FormType`, avoiding conflicts with Helper Libraries reserved words (`type`) **(breaking change)**

**Proxy**
- Remove incorrect parameter for Session List

**Studio**
- Support date created filtering on list of executions

**Taskrouter**
- Adding ability to Create, Modify and Delete Task Channels.

**Verify**
- Add `SkipSmsToLandlines`, `TtsName`, `DtmfInputRequired` optional parameters on Service resource creation or update.

**Wireless**
- Added delete action on Command resource.
- Added delete action on Sim resource.

**Twiml**
- Change `currency` from enum to string for `Pay` **(breaking change)**


[2018-11-30] Version 6.21.0
----------------------------
**Api**
- Add `interactive_data` optional param to Messages create request

**Authy**
- Required authentication for `/v1/Forms/{type}` endpoint **(breaking change)**
- Removed `Challenge.reason` to `Challenge.responded_reason`
- Removed `verification_sid` from Challenge responses
- Removed `config` param from the Factor creation
- Replaced all occurrences of `FactorType` and `FormType` in favor of a unified `Type` **(breaking change)**

**Chat**
- Add Member attributes

**Preview**
- Removed `Authy` version from `preview` subdomain in favor to `authy` subdomain. **(breaking change)**

**Verify**
- Add `CustomCode` optional parameter on Verication creation.


[2018-11-16] Version 6.20.0
----------------------------
**Messaging**
- Session API

**Twiml**
- Change `master-card` to `mastercard` as `cardType` for `Pay` and `Prompt`, remove attribute `credential_sid` from `Pay` **(breaking change)**


[2018-10-29] Version 6.19.2
----------------------------
**Api**
- Add new Balance resource:
    - url: '/v1/Accounts/{account sid}/Balance'
    - supported methods: GET
    - returns the balance of the account

**Proxy**
- Add chat_instance_sid to Service

**Verify**
- Add `Locale` optional parameter on Verification creation.


[2018-10-15] Version 6.19.1
----------------------------
**Api**
- Add <Pay> Verb Transactions category to usage records

**Twiml**
- Add support for `Pay` verb


[2018-10-15] Version 6.19.0
----------------------------
**Api**
- Add `coaching` and `call_sid_to_coach` to participant properties, create and update requests.

**Authy**
- Set public library visibility, and added PII stanza
- Dropped support for `FactorType` param given new Factor prefixes **(breaking change)**
- Supported `DELETE` actions for Authy resources
- Move Authy Services resources to `authy` subdomain

**Autopilot**
- Introduce `autopilot` subdomain with all resources from `preview.understand`

**Preview**
- Renamed Understand intent to task **(breaking change)**
- Deprecated Authy endpoints from `preview` to `authy` subdomain

**Taskrouter**
- Allow TaskQueue ReservationActivitySid and AssignmentActivitySid to not be configured for MultiTask Workspaces

**Verify**
- Add `LookupEnabled` optional parameter on Service resource creation or update.
- Add `SendDigits` optional parameter on Verification creation.
- Add delete action on Service resourse.

**Twiml**
- Add custom parameters to TwiML `Client` noun and renamed the optional `name` field to `identity`. This is a breaking change in Ruby, and applications will need to transition from `dial.client ''` and `dial.client 'alice'` formats to `dial.client` and `dial.client(identity: alice)` formats. **(breaking change)**


[2018-10-04] Version 6.18.1
----------------------------
**Preview**
- Renamed response headers for Challenge and Factors Signatures

**Video**
- [Composer] Add Composition Hook resources

**Twiml**
- Add `debug` to `Gather`
- Add `participantIdentity` to `Room`


[2018-09-28] Version 6.18.0
----------------------------
**Api**
- Set `call_sid_to_coach` parameter in participant to be `preview`

**Preview**
- Supported `totp` in Authy preview endpoints
- Allowed `latest` in Authy Challenges endpoints

**Voice**
- changed path param name from parent_iso_code to iso_code for highrisk_special_prefixes api **(breaking change)**
- added geo permissions public api


[2018-09-20] Version 6.17.0
----------------------------
**Preview**
- Add `Form` resource to Authy preview given a `form_type`
- Add Authy initial api-definitions in the 4 main resources: Services, Entities, Factors, Challenges

**Pricing**
- add voice_numbers resource (v2)

**Verify**
- Move from preview to beta **(breaking change)**


[2018-08-31] Version 6.16.4
----------------------------
**Library**
- PR #444: VCORE-3651 Add support for *for* attribute in twiml element. Thanks to @nmahure!

**Api**
- Add `call_sid_to_coach` parameter to participant create request
- Add `voice_receive_mode` param to IncomingPhoneNumbers create

**Video**
- [Recordings] Expose `offset` property in resource


[2018-08-23] Version 6.16.3
----------------------------
**Chat**
- Add User Channel instance resource


[2018-08-17] Version 6.16.2
----------------------------
**Api**
- Add Proxy Active Sessions category to usage records

**Preview**
- Add `Actions` endpoints and remove `ResponseUrl` from assistants on the Understand api

**Pricing**
- add voice_country resource (v2)


[2018-08-09] Version 6.16.1
----------------------------
**Library**
- PR #443: move index and readme_include to root. Thanks to @mbichoffe!

**Studio**
- Studio is now GA


[2018-08-03] Version 6.16.0
----------------------------
**Library**
- PR #442: Auto generate docs with sphinx. Thanks to @mbichoffe!
- PR #437: Tag and push Docker latest image when deploying with TravisCI. Thanks to @jonatasbaldin!

**Chat**
- Make message From field updatable
- Add REST API webhooks

**Notify**
- Removing deprecated `segments`, `users`, `segment_memberships`, `user_bindings` classes from helper libraries. **(breaking change)**

**Preview**
- Add new Intent Statistics endpoint
- Remove `ttl` from Assistants

**Twiml**
- Add `Connect` and `Room` for Programmable Video Rooms


[2018-07-27] Version 6.15.2
----------------------------
**Api**
- Add support for sip domains to map credential lists for registrations

**Preview**
- Remove `ttl` from Assistants

**Proxy**
- Enable setting a proxy number as reserved

**Twiml**
- Add support for SSML lang tag on Say verb


[2018-07-17] Version 6.15.1
----------------------------
**Library**
- PR #439: Override generated attributes when generating TwiML. Thanks to @cjcodes!

**Video**
- Add `group-small` room type


[2018-07-16] Version 6.15.0
----------------------------
**Library**
- PR #436: Add request body validation. Thanks to @cjcodes!

**Twiml**
- Add support for SSML on Say verb, the message body is changed to be optional **(breaking change)**


[2018-07-11] Version 6.14.10
-----------------------------
**Api**
- Add `cidr_prefix_length` param to SIP IpAddresses API

**Studio**
- Add new /Execution endpoints to begin Engagement -> Execution migration

**Video**
- [Rooms] Allow deletion of individual recordings from a room


[2018-07-05] Version 6.14.9
----------------------------
**Library**
- PR #434: Escape DOCKER_PASSWORD and DOCKER_USERNAME when logging into Docker Hub. Thanks to @jonatasbaldin!


[2018-07-05] Version 6.14.8
----------------------------
**Library**
- PR #433: Fix all Docker image build and push issues. Thanks to @jonatasbaldin!
- PR #432: Add docker to TravisCI. Thanks to @jonatasbaldin!
- PR #431: Add provider to TravisCI. Thanks to @jonatasbaldin!
- PR #430: Deploy just on tags and Python 3.6. Thanks to @jonatasbaldin!

**Api**
- Release `Call Recording Controls` feature support in helper libraries
- Add Voice Insights sub-category keys to usage records


[2018-06-29] Version 6.14.7
----------------------------
**Library**
- PR #428: Add Dockerfile and related changes to build the Docker image. Thanks to @jonatasbaldin!


[2018-06-21] Version 6.14.6
----------------------------
**Library**
- PR #429: Do not use ElementTree.__nonzero__; add test for mixed content. Thanks to @ekarson!

**Api**
- Add Fraud Lookups category to usage records

**Video**
- Allow user to set `ContentDisposition` when obtaining media URLs for Room Recordings and Compositions
- Add Composition Settings resource


[2018-06-19] Version 6.14.5
----------------------------
**Library**
- PR #425: Allow adding TwiML children with generic tag names. Thanks to @mbichoffe!
- PR #422: Allow adding text to TwiML nodes. Thanks to @ekarson!
- PR #421: Add method to validate ssl certificate. Thanks to @yannieyip!

**Twiml**
- Add methods to helper libraries to inject arbitrary text under a TwiML node


[2018-06-04] Version 6.14.4
----------------------------
**Lookups**
- Add back support for `fraud` lookup type


[2018-05-25] Version 6.14.3
----------------------------
**Library**
- PR #417: Migrate readme to rst and load it in with setup.py. Thanks to @cjcodes!


[2018-05-25] Version 6.14.2
----------------------------
**Chat**
- Add Binding and UserBinding documentation


[2018-05-25] Version 6.14.1
----------------------------
**Library**
- PR #416: Remove Python 3.3 support. Thanks to @cjcodes!

**Api**
- Add more programmable video categories to usage records
- Add 'include_subaccounts' parameter to all variation of usage_record fetch

**Studio**
- Add endpoint to delete engagements

**Trunking**
- Added cnam_lookup_enabled parameter to Trunk resource.
- Added case-insensitivity for recording parameter to Trunk resource.


[2018-05-11] Version 6.14.0
----------------------------
**Chat**
- Add Channel Webhooks resource

**Monitor**
- Update event filtering to support date/time **(breaking change)**

**Wireless**
- Updated `maturity` to `ga` for all wireless apis


[2018-04-28] Version 6.13.0
----------------------------
**Video**
- Redesign API by adding custom `VideoLayout` object. **(breaking change)**


[2018-04-20] Version 6.12.1
----------------------------
**Twiml**
- Gather input Enum: remove unnecessary "dtmf speech" value as you can now specify multiple enum values for this parameter and both "dtmf" and "speech" are already available.


[2018-04-13] Version 6.12.0
----------------------------
**Library**
- PR #413: Add incoming.allow to AccessToken VoiceGrant. Thanks to @ryan-rowland!

**Preview**
- Support for Understand V2 APIs - renames various resources and adds new fields

**Studio**
- Change parameters type from string to object in engagement resource

**Video**
- [Recordings] Change `size` type to `long`. **(breaking change)**


[2018-03-22] Version 6.11.0
----------------------------
**Lookups**
- Disable support for `fraud` lookups *(breaking change)*

**Preview**
- Add `BuildDuration` and `ErrorCode` to Understand ModelBuild

**Studio**
- Add new /Context endpoint for step and engagement resources.


[2018-03-12] Version 6.10.5
----------------------------
**Api**
- Add `caller_id` param to Outbound Calls API
- Release `trim` recording Outbound Calls API functionality in helper libraries

**Video**
- [composer] Add `room_sid` to Composition resource.

**Twiml**
- Adds support for passing in multiple input type enums when setting `input` on `Gather`


[2018-02-23] Version 6.10.4
----------------------------
**Api**
- Add `trim` param to Outbound Calls API

**Lookups**
- Add support for `fraud` lookup type

**Numbers**
- Initial Release

**Video**
- [composer] Add `SEQUENCE` value to available layouts, and `trim` and `reuse` params.


[2018-02-09] Version 6.10.3
----------------------------
**Api**
- Add `AnnounceUrl` and `AnnounceMethod` params for conference announce

**Chat**
- Add support to looking up user channels by identity in v1


[2018-01-30] Version 6.10.2
----------------------------
**Preview**
- Remove Studio Engagement Deletion

**Studio**
- Initial Release


[2018-01-30] Version 6.10.1
----------------------------
**Api**
- Add `studio-engagements` usage key

**Video**
- [omit] Beta: Allow updates to `SubscribedTracks`.
- Add `SubscribedTracks`.
- Add track name to Video Recording resource
- Add Composition and Composition Media resources


[2018-01-19] Version 6.10.1
----------------------------
**Api**
- Add `conference_sid` property on Recordings
- Add proxy and sms usage key

**Chat**
- Make user channels accessible by identity
- Add notifications logs flag parameter

**Fax**
- Added `ttl` parameter
  `ttl` is the number of minutes a fax is considered valid.

**Preview**
- Add `call_delay`, `extension`, `verification_code`, and `verification_call_sids`.
- Add `failure_reason` to HostedNumberOrders.
- Add DependentHostedNumberOrders endpoint for AuthorizationDocuments preview API.

**Taskrouter**
- Less verbose naming of cumulative and real time statistics *(breaking change)*


[2017-12-15] Version 6.10.0
----------------------------
**Library**
- Fix camelCased custom twiml parameters getting converted to lower case. (Issue #349)

**Api**
- Add `voip`, `national`, `shared_cost`, and `machine_to_machine` sub-resources to `/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{IsoCountryCode}/`
- Add programmable video keys

**Preview**
- Add `verification_type` and `verification_document_sid` to HostedNumberOrders.

**Proxy**
- Fixed typo in session status enum value

**Twiml**
- Fix Dial record property incorrectly typed as accepting TrimEnum values when it actually has its own enum of values. *(breaking change)*
- Add `priority` and `timeout` properties to Task TwiML.
- Add support for `recording_status_callback_event` for Dial verb and for Conference


[2017-12-01] Version 6.9.1
---------------------------
**Api**
- Use the correct properties for Dependent Phone Numbers of an Address *(breaking change)*
- Update Call Recordings with the correct properties

**Preview**
- Add `status` and `email` query param filters for AuthorizationDocument list endpoint

**Proxy**
- Added DELETE support to Interaction
- Standardized enum values to dash-case
- Rename Service#friendly_name to Service#unique_name

**Video**
- Remove beta flag from `media_region` and `video_codecs`

**Wireless**
- Bug fix: Changed `operator_mcc` and `operator_mnc` in `DataSessions` subresource from `integer` to `string`


[2017-11-17] Version 6.9.0
---------------------------
**Sync**
- Add TTL support for Sync objects *(breaking change)*
  - The required `data` parameter on the following actions is now optional: "Update Document", "Update Map Item", "Update List Item"
  - New actions available for updating TTL of Sync objects: "Update List", "Update Map", "Update Stream"

**Video**
- [bi] Rename `RoomParticipant` to `Participant`
- Add Recording Settings resource
- Expose EncryptionKey and MediaExternalLocation properties in Recording resource


[2017-11-10] Version 6.8.4
---------------------------
**Accounts**
- Add AWS credential type

**Preview**
- Removed `iso_country` as required field for creating a HostedNumberOrder.

**Proxy**
- Added new fields to Service: geo_match_level, number_selection_behavior, intercept_callback_url, out_of_session_callback_url


[2017-11-03] Version 6.8.3
---------------------------
**Api**
- Add programmable video keys

**Video**
- Add `Participants`


[2017-10-27] Version 6.8.2
---------------------------
**Chat**
- Add Binding resource
- Add UserBinding resource


[2017-10-20] Version 6.8.1
---------------------------
**Library**
- #394 Update request validator to remove port numbers from https urls. Thanks @Brodan!
- #385 Add request logging and hooking. Thanks @tysonholub!

**Api**
- Add `address_sid` param to IncomingPhoneNumbers create and update
- Add 'fax_enabled' option for Phone Number Search


[2017-10-13] Version 6.8.0
---------------------------
**Api**
- Add `smart_encoded` param for Messages
- Add `identity_sid` param to IncomingPhoneNumbers create and update

**Preview**
- Make 'address_sid' and 'email' optional fields when creating a HostedNumberOrder
- Add AuthorizationDocuments preview API.

**Proxy**
- Initial Release

**Wireless**
- Added `ip_address` to sim resource

**Twiml**
- Rename `number` to `phone_number` in Voice Number TwiML. *(breaking change)*
- Rename `message` to `body` in Messaging TwiML. *(breaking change)*


[2017-10-06] Version 6.7.1
---------------------------
**Preview**
- Add `acc_security` (authy-phone-verification) initial api-definitions

**Taskrouter**
- [bi] Less verbose naming of cumulative and real time statistics


[2017-09-28] Version 6.7.0
---------------------------
**Chat**
- Make member accessible through identity
- Make channel subresources accessible by channel unique name
- Set get list 'max_page_size' parameter to 100
- Add service instance webhook retry configuration
- Add media message capability
- Make `body` an optional parameter on Message creation. *(breaking change)*

**Notify**
- `data`, `apn`, `gcm`, `fcm`, `sms` parameters in `Notifications` create resource are dicts/objects instead of strings. Passing manually stringified json will continue to work.

**Taskrouter**
- Add new query ability by TaskChannelSid or TaskChannelUniqueName
- Move Events, Worker, Workers endpoint over to CPR
- Add new RealTime and Cumulative Statistics endpoints

**Video**
- Create should allow an array of video_codecs.
- Add video_codecs as a property of room to make it externally visible.


[2017-09-15] Version 6.6.3
---------------------------
**Api**
- Add `sip_registration` property on SIP Domains
- Add new video and market usage category keys


[2017-09-01] Version 6.6.2
---------------------------
- Added last_response and last_request to http_client

[2017-09-01] Version 6.6.1
---------------------------
**Sync**
- Add support for Streams

**Wireless**
- Added DataSessions sub-resource to Sims.


[2017-08-25] Version 6.6.0
---------------------------
**Library**
- Allow creating AccessTokens/Jwts without generating `nbf`. Passing `None` in the constructor will remove `nbf` from jwt payload.

**Api**
- Update `status` enum for Recordings to include 'failed'
- Add `error_code` property on Recordings

**Chat**
- Add mutable parameters for channel, members and messages

**Video**
- New `media_region` parameter when creating a room, which controls which region media will be served out of.

**Twiml**
- Add support for `speech_timeout`, `max_speech_time`, and `profanity_filter` attributes on Gather verb.


[2017-08-18] Version 6.5.2
---------------------------
**Library**
- Remove bundled certificates, use `certifi` package via `requests`.
- Add option to use connection pooling. This is enabled by default and will use one Session for all requests
in Client.
    - To disable this, pass `pool_connections` parameter when creating your Twilio client.
```python
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

client = Client(
    username,
    password,
    http_client=TwilioHttpClient(pool_connections=False)
)
```

**Api**
- Add VoiceReceiveMode {'voice', 'fax'} option to IncomingPhoneNumber UPDATE requests

**Chat**
- Add channel message media information
- Add service instance message media information

**Preview**
- Removed 'email' from bulk_exports configuration api [bi]. No migration plan needed because api has not been used yet.
- Add DeployedDevices.

**Sync**
- Add support for Service Instance unique names

[2017-08-10] Version 6.5.1
---------------------------
Fixed PyJWT >= 1.5.1 exception


**Api**
- Add New wireless usage keys added
- Add `auto_correct_address` param for Addresses create and update
- Add ChatGrant grant and deprecate IpMessagingGrant

**Video**
- Add `video_codec` enum and `video_codecs` parameter, which can be set to either `VP8` or `H264` during room creation.
- Restrict recordings page size to 100

[2017-07-27] Version 6.5.0
---------------------------
This release adds Beta and Preview products to main artifact.

Previously, Beta and Preview products were only included in the `alpha`
artifact. They are now being included in the main artifact to ease product
discoverability and the collective operational overhead of maintaining multiple
artifacts per library.

**Api**
- Remove unused `encryption_type` property on Recordings *(breaking change)*
- Update `status` enum for Messages to include 'accepted'

**Messaging**
- Fix incorrectly typed capabilities property for PhoneNumbers.

**Notify**
- Add `ToBinding` optional parameter on Notifications resource creation. Accepted values are json strings.

**Preview**
- Add `sms_application_sid` to HostedNumberOrders.

**Taskrouter**
- Fully support conference functionality in reservations.


[2017-07-12] Version 6.4.3
---------------------------
**Api**
- Update `AnnounceMethod` parameter naming for consistency

**Notify**
- Add `ToBinding` optional parameter on Notifications resource creation. Accepted values are json strings.

**Preview**
- Add `verification_attempts` to HostedNumberOrders.
- Add `status_callback_url` and `status_callback_method` to HostedNumberOrders.

**Video**
- Filter recordings by date using the parameters `DateCreatedAfter` and `DateCreatedBefore`.
- Override the default time-to-live of a recording's media URL through the `Ttl` parameter (in seconds, default value is 3600).
- Add query parameters `SourceSid`, `Status`, `DateCreatedAfter` and `DateCreatedBefore` to the convenience method for retrieving Room recordings.

**Wireless**
- Added national and international data limits to the RatePlans resource.


[2017-06-27] Version 6.4.2
--------------------------

- Pin PyJWT to below version `1.5.1` to fix broken build.
- Fix json load error for python 3.3 - 3.5

[2017-06-16] Version 6.4.1
--------------------------

- Add several missing `<Gather>` attributes.
    - `partial_result_callback`
    - `partial_result_callback_method`
    - `language`
    - `hints`
    - `barge_in`
    - `acknowledge_sound_url`
    - `input`
- Remove client-side max page size validation.
- Support `announce_url` and `announce_url_method` on Conference Participants.
- TwiML docstring corrections.

[2017-06-15] Version 6.4.0
--------------------------

- Remove support for Python 2.6.
- Add `locality` field to `AvailablePhoneNumbers`.
- Add `origin` field to `IncomingPhoneNumbers`.
- Add `in_locality` parameter to `AvailablePhoneNumbers`.
- Add `origin` parameter to `IncomingPhoneNumbers`.
- Add new sync categories to `UsageRecords`.
- Support unicode in `validation_client`.
- Add `muted` parameter to `<Conference>` Twiml.

[2017-05-24] Version 6.3.0
--------------------------

- Rename RoomList to RoomRecordingsList.

[2017-05-19] Version 6.2.0
--------------------------

- Add video domain.
- Update usage record categories.
- Add `get_page` method for reentrant paging.

[2017-05-12] Version 6.1.2
----------------------------------

- Allow *kwargs in TwiML Gather

[2017-05-10] Version 6.1.1
----------------------------------

- Add Task verb to VoiceResponse
- Add Echo verb to VoiceResponse
- Add Sim verb to VoiceResponse

[2017-04-27] Version 6.1.0
--------------------------

- Add v2 of chat.twilio.com.
- Add `recording_channels` parameter to Participant create and update.
- Add `recording_status_callback` parameter to Participant create and update.
- Add `recording_status_callback_method` parameter to Participant create and update.
- Add `sip_auth_username` parameter to Participant create and update.
- Add `region` parameter to Participant create and update.
- Add `conference_recording_status_callback` parameter to Participant create and update.
- Add `conference_recording_status_callback_method` parameter to Participant create and update.
- Add `validity_period` parameter to Messages.

[2017-04-03] Version 6.0.0
--------------------------
**New Major Version**

The newest version of the `twilio-python` helper library!

This version brings a host of changes to update and modernize the `twilio-python` helper library. It is auto-generated to produce a more consistent and correct product.

- [Full API Documentation](https://twilio.github.io/twilio-python/)
- [General Documentation](https://www.twilio.com/docs/libraries/python)

Version 4.4.0
-------------

Released May 19, 2015:

- Add support for the beta field to IncomingPhoneNumbers and AvailablePhoneNumbers

Version 4.3.0
-------------

Released May 14, 2015:

- Add support for Call Status Events in TwiML

Version 4.2.0
-------------

Released May 7, 2015:

- Add support for the Twilio Monitor APIs: Events and Alerts

Version 4.1.0
-------------

Released May 6, 2015:

- Add support for the Twilio Pricing API

Version 4.0.0
-------------

Released April 16, 2015:

- Remove the deprecated count function from ListResource

Version 3.8.0
-------------

Released March 31, 2015:

- Support for the new Twilio Lookups API

Version 3.7.3
-------------

Released March 10, 2015:

- Add missing docstrings and examples for TaskRouter

Version 3.7.2
-------------

Released February 24, 2015:

- Restore Tokens resource to TwilioRestClient

Version 3.7.1
-------------

Released February 20, 2015:

- Restore Python 2.6 and 3.x support

Version 3.7.0
-------------

Released February 18, 2015:

- Add TaskRouterClient and resources to support the new TaskRouter API
- Stop prepending numeric error code to exception error messages

Version 3.6.15
--------------

Released January 14, 2015

- Update request construction for Tokens

Version 3.6.14
--------------

Released December 22, 2014

- Specify Python 3 dependencies in wheel package

Version 3.6.12
--------------

Released November 24, 2014

- Fix compatibility issue for Python 3.4

Version 3.6.11
--------------

Released November 21, 2014

- Add support for the new Tokens endpoint

Version 3.6.10
--------------

Released November 13, 2014

- Add support for DELETE to Call and Message records
- Add support for redacting Message body fields

Version 3.6.9
-------------

Released October 30, 2014

- Add Python 3.4 support
- Add wheel packaging
- Fix compatibility with earlier Python 2 releases

Version 3.6.8
-------------

Released October 9, 2014

- Remove unneeded unittest2py3k dependency.
- Restore backwards-compatible exception import paths.

Version 3.6.7
-------------

Released August 6, 2014

- Fix Python 2.5 compatibility.
- Add CallFeedback resources.
- Typo fixes and formatting cleanup.
- Refactor exception hierarchy and imports.
- Documentation improvements.

Version 3.6.6
--------------

Released on February 27, 2014

- Previously the error message was set based on the `tty` value; instead now we
  detect `tty` when you try to print the error message. The `msg` property of
  the exception is set to a decent value.
- `twilio-python` now uses entirely relative imports, so it may be easier to
  include it as a part of another package.

Version 3.6.5
--------------

- Remove unittest2 dependency.
- Tests no longer run against Python 2.5.
- update(), delete() work on Application, Transcription and UsageTrigger
  instance classes.

Version 3.6.4
-------------

Released November 5, 2013

- Adds support for the 'digits' attribute of Play verbs in TwiML creation.
- Updates documentation for Message TwiML verb
- Bugfix for tty detection in error formatting

Version 3.6.3
-------------

Released October 21, 2013

- Adds support for filtering by type to IncomingPhoneNumbers.

- Adds support for filtering for mobile numbers to both IncomingPhoneNumbers
  and AvailablePhoneNumbers.


Version 3.6.2
-------------

Released on September 24, 2013

- Adds support for HTTP and SOCKS4/5 proxies to the REST client.


Version 3.6.0, 3.6.1
--------------------

Released on September 18, 2013

- Adds support for the new Message and SIP resources to the REST API client.
- Adds support for the new Message verb to the TwiML generator.


Version 3.5.3, 3.5.4
--------------------

Released on September 6, 2013

- twilio-python now includes an SSL certfication file to ensure that
  connections to api.twilio.com don't fail with SSLError.

Version 3.5.2
-------------

Released on August 26, 2013

- You can now delete transcriptions

Version 3.5.1
-------------

Released on May 21, 2013

- Fixes an issue in the 3.5.0 release where null dates would cause the library
  to raise a TypeError.

Version 3.5.0
-------------

Released on May 21, 2013

- `date_created` and `date_updated` objects are now returned as Python
  `datetime.datetime` objects instead of as RFC 2822 formatted strings. This is
  a backwards incompatible change. (via [@abrinsmead](/abrinsmead))
- The library will not throw a UnicodeDecodeError when parsing API responses
  with Python 3.
- You can pass integers to Twiml arguments. (via [@jvankoten](/jvankoten))
- Ensuring the tests always pass on Python 3. (via [@ftobia](/ftobia))
- Add the list of AUTHORS
- Fixes a timing attack vector in signature validation. (via [@zacharyvoase](/zacharyvoase))

Version 3.4.5
-------------

Released on April 1, 2013

Allow the Account object to access usage records and usage trigger data, in
addition to the client. Reporter: Trenton McManus

Version 3.4.4
-------------

Adds support for Sip

Version 3.4.3
-------------

Adds correct dependencies to the `setup.py` file.

Version 3.4.2
-------------

Released on January 2, 2013

Adds a convenience function to retrieve the members of a queue by running
client.members("QU123").

Version 3.4.1
-------------

Python3 support!

Version 3.3.11
--------------

- Fix a bug where participants could not be kicked from a Conference


Version 3.3.10
--------------

- Add support for Queue. Fix a bug where the library wouldn't work in Python 2.5


Version 3.3.9
-------------

- Fix an error introduced in 3.3.7 that prevented validation calls from
  succeeding.

Version 3.3.8
-------------

- Use next_page_uri when iterating over a list resource


Version 3.3.7
-------------

- Allow arbitrary keyword arguments on resource creation and listing

Version 3.3.6
-------------

- Remove doc/tmp directory which was preventing installation on certain Windows machines
- Add Travis CI integration
- Update httplib2 dependency

Version 3.3.5
-------------

Released on January 18, 2011

- Fix a bug with the deprecated `TwilioRestClient.request` method
- Fix a bug in filtering SMS messages by DateSent

Version 3.3.4
-------------

Released on December 16, 2011

- Allow both unicode strings and encoded byte strings in request data
- Add support for SMS and Voice application sids to phone number updating
- Fix documentation error relating to phone number purchasing
- Include doc string information for decorated functions

Version 3.3.3
-------------

Released on November 3, 2011

- Support unicode characters when validating requests
- Add support for Great Britain language on the Say verb
- Set Sms Application, Voice Application, and/or a Friendly
  Name when purchasing a number
- Add missing parameters for resource creation and update

Version 3.3.2
-------------

Released on September 29, 2011

- TwiML verbs can now be used as context managers

Version 3.3.1
-------------

Released on September 27, 2011

- Allow phone numbers to be transferred between accounts and subaccounts

Version 3.3.0
-------------

Released on September 21, 2011

- Add support for Twilio Connect. Connect applications and authorized Connect
  applications are now availble via the REST client.
- Fix a problem where date and datetimes weren't coverted to strings when
  querying list resources
