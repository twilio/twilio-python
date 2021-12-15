twilio-python Changelog
=======================

Here you can see the full list of changes between each twilio-python release.

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
