.. module:: twilio.rest.resources

=============================
:mod:`twilio.rest.resources`
=============================

.. autoclass:: ListResource
   :members: count, get, iter

.. autoclass:: InstanceResource

Accounts
>>>>>>>>>

.. autoclass:: Accounts
   :members:
   :exclude-members: instance

.. autoclass:: Account
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this account.

   .. attribute:: date_created

      The date that this account was created, in GMT in RFC 2822 format

   .. attribute:: date_updated

      The date that this account was last updated, in GMT in RFC 2822 format.

   .. attribute:: friendly_name

      A human readable description of this account, up to 64 characters long. By default the FriendlyName is your email address.

   .. attribute:: status

      The status of this account. Usually active, but can be suspended if you've been bad, or closed if you've been horrible.

   .. attribute:: auth_token

      The authorization token for this account. This token should be kept a secret, so no sharing.


Applications
>>>>>>>>>>>>>>>

.. autoclass:: Applications
   :members:
   :exclude-members: instance

.. autoclass:: Application
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this application.

   .. attribute:: date_created

      The date that this application was created, in GMT in RFC 2822 format

   .. attribute:: date_updated

      The date that this application was last updated, in GMT in RFC 2822 format.

   .. attribute:: friendly_name

      A human readable description of this application, up to 64 characters long. By default the FriendlyName is your email address.

   .. attribute:: status

      The status of this account. Usually active, but can be suspended if you've been bad, or closed if you've been horrible.

   .. attribute:: api_version

      Requests to this application will start a new TwiML session with this API version.

   .. attribute:: voice_url

      URL Twilio will request when a phone number assigned to this application receives a call.

   .. attribute:: voice_method

      The HTTP method Twilio will use when requesting the above Url. Either GET or POST.

   .. attribute:: voice_fallback_url

      The URL that Twilio will request if an error occurs retrieving or executing the TwiML requested by Url.

   .. attribute:: voice_fallback_method

      The HTTP method Twilio will use when requesting the VoiceFallbackUrl. Either GET or POST.

   .. attribute:: status_callback

      The URL that Twilio will request to pass status parameters (such as call ended) to your application.

   .. attribute:: status_callback_method

      The HTTP method Twilio will use to make requests to the StatusCallback URL. Either GET or POST.

   .. attribute:: voice_caller_id_lookup

      Look up the caller's caller-ID name from the CNAM database (additional charges apply). Either true or false.

   .. attribute:: sms_url

      The URL Twilio will request when a phone number assigned to this application receives an incoming SMS message.

   .. attribute:: sms_method

      The HTTP method Twilio will use when making requests to the SmsUrl. Either GET or POST.

   .. attribute:: sms_fallback_url

      The URL that Twilio will request if an error occurs retrieving or executing the TwiML from SmsUrl.

   .. attribute:: sms_fallback_method

      The HTTP method Twilio will use when requesting the above URL. Either GET or POST.

   .. attribute:: sms_status_callback

      Twilio will make a POST request to this URL to pass status parameters (such as sent or failed) to your application if you specify this application's Sid as the ApplicationSid on an outgoing SMS request.

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com
      

Calls
>>>>>>

.. autoclass:: twilio.rest.resources.Calls
   :members:
   :exclude-members: instance
   :inherited-members:

.. autoclass:: twilio.rest.resources.Call
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this resource.

   .. attribute:: parent_call_sid

      A 34 character string that uniquely identifies the call that created this leg.

   .. attribute:: date_created

      The date that this resource was created, given as GMT in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given as GMT in RFC 2822 format.

   .. attribute:: account_sid

      The unique id of the Account responsible for creating this call.

   .. attribute:: to

      The phone number that received this call. e.g., +16175551212 (E.164 format)

   .. attribute:: from_

      The phone number that made this call. e.g., +16175551212 (E.164 format)

   .. attribute:: phone_number_sid

      If the call was inbound, this is the Sid of the IncomingPhoneNumber that received the call. If the call was outbound, it is the Sid of the OutgoingCallerId from which the call was placed.

   .. attribute:: status

      A string representing the status of the call. May be :data:`QUEUED`, :data:`RINGING`, :data:`IN-PROGRESS`, :data:`COMPLETED`, :data:`FAILED`, :data:`BUSY` or :data:`NO_ANSWER`.

   .. attribute:: start_time

      The start time of the call, given as GMT in RFC 2822 format. Empty if the call has not yet been dialed.

   .. attribute:: end_time

      The end time of the call, given as GMT in RFC 2822 format. Empty if the call did not complete successfully.

   .. attribute:: duration

      The length of the call in seconds. This value is empty for busy, failed, unanswered or ongoing calls.

   .. attribute:: price

      The charge for this call in USD. Populated after the call is completed. May not be immediately available.

   .. attribute:: direction

      A string describing the direction of the call. inbound for inbound calls, outbound-api for calls initiated via the REST API or outbound-dial for calls initiated by a <Dial> verb.

   .. attribute:: answered_by

      If this call was initiated with answering machine detection, either human or machine. Empty otherwise.

   .. attribute:: forwarded_from

      If this call was an incoming call forwarded from another number, the forwarding phone number (depends on carrier supporting forwarding). Empty otherwise.

   .. attribute:: caller_name

      If this call was an incoming call from a phone number with Caller ID Lookup enabled, the caller's name. Empty otherwise.

Caller Ids
>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.CallerIds
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.CallerId
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this resource.

   .. attribute:: date_created

      The date that this resource was created, given in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given in RFC 2822 format.

   .. attribute:: friendly_name

      A human readable descriptive text for this resource, up to 64 characters long. By default, the FriendlyName is a nicely formatted version of the phone number.

   .. attribute:: account_sid

      The unique id of the Account responsible for this Caller Id.

   .. attribute:: phone_number

      The incoming phone number. Formatted with a '+' and country code e.g., +16175551212 (E.164 format).

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com.

Conferences
>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.Conferences
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.Conference
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this conference.

   .. attribute:: friendly_name

      A user provided string that identifies this conference room.

   .. attribute:: status

      A string representing the status of the conference. May be init, in-progress, or completed.

   .. attribute:: date_created

      The date that this conference was created, given as GMT in RFC 2822 format.

   .. attribute:: date_updated

      The date that this conference was last updated, given as GMT in RFC 2822 format.

   .. attribute:: account_sid

      The unique id of the Account responsible for creating this conference.

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com.

   .. attribute:: participants

      The :class:`Participants` resource, listing people currently in this conference


Connect Apps
>>>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.ConnectApps
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.ConnectApp
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this resource.

   .. attribute:: date_created

      The date that this resource was created, given as GMT in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given as GMT in RFC 2822 format.

   .. attribute:: account_sid

      The unique id of the Account responsible for creating this call.

   .. attribute:: permissions

      The list of permissions that your ConnectApp requests.

   .. attribute:: friendly_name

      A human readable name for this resource.

   .. attribute:: description

      A more detailed human readable description of this resource.

   .. attribute:: company_name

      The company name set for this Connect App.

   .. attribute:: homepage_url

      The public URL where users can obtain more information about this Connect App.

   .. attribute:: authorize_redirect_url
     
      The URL the user's browser will redirect to after Twilio authenticates the 
      user and obtains authorization for this Connect App.

   .. attribute:: deauthorize_callback_url

      The URL to which Twilio will send a request when a user de-authorizes this 
      Connect App.

   .. attribute:: deauthorize_callback_method

      The HTTP method to be used when making a request to the deauthorize
      callback url.

   .. attribute:: uri 

      The URI for this resource, relative to https://api.twilio.com.


Notifications
>>>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.Notifications
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.Notification
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this resource.

   .. attribute:: date_created

      The date that this resource was created, given in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given in RFC 2822 format.

   .. attribute:: account_sid

      The unique id of the Account responsible for this notification.

   .. attribute:: call_sid

      CallSid is the unique id of the call during which the notification was generated. Empty if the notification was generated by the REST API without regard to a specific phone call.

   .. attribute:: api_version

      The version of the Twilio in use when this notification was generated.

   .. attribute:: log

      An integer log level corresponding to the type of notification: 0 is ERROR, 1 is WARNING.

   .. attribute:: error_code

      A unique error code for the error condition. You can lookup errors, with possible causes and solutions, in our Error Dictionary.

   .. attribute:: more_info

      A URL for more information about the error condition. The URL is a page in our Error Dictionary.

   .. attribute:: message_text

      The text of the notification.

   .. attribute:: message_date

      The date the notification was actually generated, given in RFC 2822 format. Due to buffering, this may be slightly different than the DateCreated date.

   .. attribute:: request_url

      The URL of the resource that generated the notification. If the notification was generated during a phone call: This is the URL of the resource on YOUR SERVER that caused the notification. If the notification was generated by your use of the REST API: This is the URL of the REST resource you were attempting to request on Twilio's servers.

   .. attribute:: request_method

      The HTTP method in use for the request that generated the notification. If the notification was generated during a phone call: The HTTP Method use to request the resource on your server. If the notification was generated by your use of the REST API: This is the HTTP method used in your request to the REST resource on Twilio's servers.

   .. attribute:: request_variables

      The Twilio-generated HTTP GET or POST variables sent to your server. Alternatively, if the notification was generated by the REST API, this field will include any HTTP POST or PUT variables you sent to the REST API.

   .. attribute:: response_headers

      The HTTP headers returned by your server.

   .. attribute:: response_body

      The HTTP body returned by your server.

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com

Participants
>>>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.Participants
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.Participant
   :members:

   .. attribute:: call_sid

      A 34 character string that uniquely identifies the call that is connected to this conference

   .. attribute:: conference_sid

      A 34 character string that identifies the conference this participant is in

   .. attribute:: date_created

      The date that this resource was created, given in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given in RFC 2822 format.

   .. attribute:: account_sid

      The unique id of the Account that created this conference

   .. attribute:: muted

      true if this participant is currently muted. false otherwise.

   .. attribute:: start_conference_on_enter

      Was the startConferenceOnEnter attribute set on this participant (true or false)?

   .. attribute:: end_conference_on_exit

      Was the endConferenceOnExit attribute set on this participant (true or false)?

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com.


Phone Numbers
>>>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.PhoneNumbers
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.PhoneNumber
   :members:

.. autoclass:: twilio.rest.resources.AvailablePhoneNumber
   :members:


Queues
>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.Queues
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.Queue
   :members:


Queue Members
>>>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.Members
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.Member
   :members:

Recordings
>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.Recordings
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.Recording
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this resource.

   .. attribute:: date_created

      The date that this resource was created, given in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given in RFC 2822 format.

   .. attribute:: account_sid

      The unique id of the Account responsible for this recording.

   .. attribute:: call_sid

      The call during which the recording was made.

   .. attribute:: duration

      The length of the recording, in seconds.

   .. attribute:: api_version

      The version of the API in use during the recording.

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com

   .. attribute:: subresource_uris

      The list of subresources under this account

   .. attribute:: formats

      A dictionary of the audio formats available for this recording

      .. code-block:: python

          {
              "wav": "http://www.dailywav.com/0112/noFateButWhatWeMake.wav",
              "mp3": "https://api.twilio.com/cowbell.mp3",
          }

Sandbox
>>>>>>>>

.. autoclass:: twilio.rest.resources.Sandboxes
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.Sandbox
   :members:

   .. attribute:: pin

      An 8 digit number that gives access to this sandbox.

   .. attribute:: account_sid

      The unique id of the Account connected to this sandbox.

   .. attribute:: phone_number

      The phone number of the sandbox.  Formatted with a '+' and country code e.g., +16175551212 (E.164 format).

   .. attribute:: voice_url

      The URL Twilio will request when the sandbox number is called.

   .. attribute:: voice_method

      The HTTP method to use when requesting the above URL. Either GET or POST.

   .. attribute:: sms_url

      The URL Twilio will request when receiving an incoming SMS message to the sandbox number.

   .. attribute:: sms_method

      The HTTP method to use when requesting the sms URL. Either GET or POST.

   .. attribute:: date_created

      The date that this resource was created, given in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given in RFC 2822 format.

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com


Short Codes
>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.ShortCodes
   :members:

.. autoclass:: twilio.rest.resources.ShortCode
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this resource.

   .. attribute:: date_created

      The date that this resource was created, given in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given in RFC 2822 format.

   .. attribute:: friendly_name

      A human readable descriptive text for this resource, up to 64 characters long. By default, the :attr:`friendly_name` is just the short code.

   .. attribute:: account_sid

      The unique id of the Account that owns this short code.

   .. attribute:: short_code

      The short code. e.g., 894546.

   .. attribute:: api_version

      SMSs to this short code will start a new TwiML session with this API version.

   .. attribute:: sms_url

      The URL Twilio will request when receiving an incoming SMS message to this short code.

   .. attribute:: sms_method

      The HTTP method Twilio will use when making requests to the :attr:`sms_url`. Either GET or POST.

   .. attribute:: sms_fallback_url

      The URL that Twilio will request if an error occurs retrieving or executing the TwiML from :attr:`sms_url`.

   .. attribute:: sms_fallback_method

      The HTTP method Twilio will use when requesting the above URL. Either GET or POST.

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com.


SMS Messages
>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.SmsMessages
   :members:

.. autoclass:: twilio.rest.resources.SmsMessage
   :members:

Transcriptions
>>>>>>>>>>>>>>>

.. autoclass:: twilio.rest.resources.Transcriptions
   :members:
   :exclude-members: instance

.. autoclass:: twilio.rest.resources.Transcription
   :members:

   .. attribute:: sid

      A 34 character string that uniquely identifies this resource.

   .. attribute:: date_created

      The date that this resource was created, given in RFC 2822 format.

   .. attribute:: date_updated

      The date that this resource was last updated, given in RFC 2822 format.

   .. attribute:: account_sid

      The unique id of the Account responsible for this transcription.

   .. attribute:: status

      A string representing the status of the transcription: in-progress, completed or failed.

   .. attribute:: recording_sid

      The unique id of the Recording this Transcription was made of.

   .. attribute:: duration

      The duration of the transcribed audio, in seconds.

   .. attribute:: transcription_text

      The text content of the transcription.

   .. attribute:: price

      The charge for this transcript in USD. Populated after the transcript is completed. Note, this value may not be immediately available.

   .. attribute:: uri

      The URI for this resource, relative to https://api.twilio.com


