# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class PhoneCallList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the PhoneCallList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.phone_call.PhoneCallList
        :rtype: twilio.rest.preview.trusted_comms.phone_call.PhoneCallList
        """
        super(PhoneCallList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Business/PhoneCalls'.format(**self._solution)

    def create(self, from_, to, reason=values.unset, application_sid=values.unset,
               caller_id=values.unset, fallback_method=values.unset,
               fallback_url=values.unset, machine_detection=values.unset,
               machine_detection_silence_timeout=values.unset,
               machine_detection_speech_end_threshold=values.unset,
               machine_detection_speech_threshold=values.unset,
               machine_detection_timeout=values.unset, method=values.unset,
               record=values.unset, recording_channels=values.unset,
               recording_status_callback=values.unset,
               recording_status_callback_event=values.unset,
               recording_status_callback_method=values.unset,
               send_digits=values.unset, sip_auth_password=values.unset,
               sip_auth_username=values.unset, status_callback=values.unset,
               status_callback_event=values.unset,
               status_callback_method=values.unset, timeout=values.unset,
               trim=values.unset, url=values.unset):
        """
        Create a new PhoneCallInstance

        :param unicode from_: Twilio number from which to originate the call
        :param unicode to: The terminating Phone Number
        :param unicode reason: The business reason for this phone call
        :param unicode application_sid: Refers to the Voice API Initiate Call parameter
        :param unicode caller_id: Refers to the Voice API Initiate Call parameter
        :param unicode fallback_method: Refers to the Voice API Initiate Call parameter
        :param unicode fallback_url: Refers to the Voice API Initiate Call parameter
        :param unicode machine_detection: Refers to the Voice API Initiate Call parameter
        :param unicode machine_detection_silence_timeout: Refers to the Voice API Initiate Call parameter
        :param unicode machine_detection_speech_end_threshold: Refers to the Voice API Initiate Call parameter
        :param unicode machine_detection_speech_threshold: Refers to the Voice API Initiate Call parameter
        :param unicode machine_detection_timeout: Refers to the Voice API Initiate Call parameter
        :param unicode method: Refers to the Voice API Initiate Call parameter
        :param bool record: Refers to the Voice API Initiate Call parameter
        :param unicode recording_channels: Refers to the Voice API Initiate Call parameter
        :param unicode recording_status_callback: Refers to the Voice API Initiate Call parameter
        :param unicode recording_status_callback_event: Refers to the Voice API Initiate Call parameter
        :param unicode recording_status_callback_method: Refers to the Voice API Initiate Call parameter
        :param unicode send_digits: Refers to the Voice API Initiate Call parameter
        :param unicode sip_auth_password: Refers to the Voice API Initiate Call parameter
        :param unicode sip_auth_username: Refers to the Voice API Initiate Call parameter
        :param unicode status_callback: Refers to the Voice API Initiate Call parameter
        :param unicode status_callback_event: Refers to the Voice API Initiate Call parameter
        :param unicode status_callback_method: Refers to the Voice API Initiate Call parameter
        :param unicode timeout: Refers to the Voice API Initiate Call parameter
        :param unicode trim: Refers to the Voice API Initiate Call parameter
        :param unicode url: Refers to the Voice API Initiate Call parameter

        :returns: Newly created PhoneCallInstance
        :rtype: twilio.rest.preview.trusted_comms.phone_call.PhoneCallInstance
        """
        data = values.of({
            'From': from_,
            'To': to,
            'Reason': reason,
            'ApplicationSid': application_sid,
            'CallerId': caller_id,
            'FallbackMethod': fallback_method,
            'FallbackUrl': fallback_url,
            'MachineDetection': machine_detection,
            'MachineDetectionSilenceTimeout': machine_detection_silence_timeout,
            'MachineDetectionSpeechEndThreshold': machine_detection_speech_end_threshold,
            'MachineDetectionSpeechThreshold': machine_detection_speech_threshold,
            'MachineDetectionTimeout': machine_detection_timeout,
            'Method': method,
            'Record': record,
            'RecordingChannels': recording_channels,
            'RecordingStatusCallback': recording_status_callback,
            'RecordingStatusCallbackEvent': serialize.map(recording_status_callback_event, lambda e: e),
            'RecordingStatusCallbackMethod': recording_status_callback_method,
            'SendDigits': send_digits,
            'SipAuthPassword': sip_auth_password,
            'SipAuthUsername': sip_auth_username,
            'StatusCallback': status_callback,
            'StatusCallbackEvent': serialize.map(status_callback_event, lambda e: e),
            'StatusCallbackMethod': status_callback_method,
            'Timeout': timeout,
            'Trim': trim,
            'Url': url,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return PhoneCallInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.PhoneCallList>'


class PhoneCallPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the PhoneCallPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.trusted_comms.phone_call.PhoneCallPage
        :rtype: twilio.rest.preview.trusted_comms.phone_call.PhoneCallPage
        """
        super(PhoneCallPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PhoneCallInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.trusted_comms.phone_call.PhoneCallInstance
        :rtype: twilio.rest.preview.trusted_comms.phone_call.PhoneCallInstance
        """
        return PhoneCallInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.PhoneCallPage>'


class PhoneCallInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the PhoneCallInstance

        :returns: twilio.rest.preview.trusted_comms.phone_call.PhoneCallInstance
        :rtype: twilio.rest.preview.trusted_comms.phone_call.PhoneCallInstance
        """
        super(PhoneCallInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'from_': payload.get('from'),
            'to': payload.get('to'),
            'reason': payload.get('reason'),
            'created_at': deserialize.iso8601_datetime(payload.get('created_at')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Current Call.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: Account Sid.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def from_(self):
        """
        :returns: The originating Phone Number
        :rtype: unicode
        """
        return self._properties['from_']

    @property
    def to(self):
        """
        :returns: The terminating Phone Number
        :rtype: unicode
        """
        return self._properties['to']

    @property
    def reason(self):
        """
        :returns: The business reason for this phone call
        :rtype: unicode
        """
        return self._properties['reason']

    @property
    def created_at(self):
        """
        :returns: The date this Current Call was created
        :rtype: datetime
        """
        return self._properties['created_at']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.PhoneCallInstance>'
