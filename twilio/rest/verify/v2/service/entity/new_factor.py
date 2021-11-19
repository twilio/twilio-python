# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class NewFactorList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, identity):
        """
        Initialize the NewFactorList

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param identity: Unique external identifier of the Entity

        :returns: twilio.rest.verify.v2.service.entity.new_factor.NewFactorList
        :rtype: twilio.rest.verify.v2.service.entity.new_factor.NewFactorList
        """
        super(NewFactorList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'identity': identity, }
        self._uri = '/Services/{service_sid}/Entities/{identity}/Factors'.format(**self._solution)

    def create(self, friendly_name, factor_type, binding_alg=values.unset,
               binding_public_key=values.unset, config_app_id=values.unset,
               config_notification_platform=values.unset,
               config_notification_token=values.unset,
               config_sdk_version=values.unset, binding_secret=values.unset,
               config_time_step=values.unset, config_skew=values.unset,
               config_code_length=values.unset, config_alg=values.unset):
        """
        Create the NewFactorInstance

        :param unicode friendly_name: The friendly name of this Factor
        :param NewFactorInstance.FactorTypes factor_type: The Type of this Factor
        :param unicode binding_alg: The algorithm used when `factor_type` is `push`
        :param unicode binding_public_key: The public key encoded in Base64
        :param unicode config_app_id: The ID that uniquely identifies your app in the Google or Apple store
        :param NewFactorInstance.NotificationPlatforms config_notification_platform: The transport technology used to generate the Notification Token
        :param unicode config_notification_token: For APN, the device token. For FCM, the registration token
        :param unicode config_sdk_version: The Verify Push SDK version used to configure the factor
        :param unicode binding_secret: The shared secret in Base32
        :param unicode config_time_step: How often, in seconds, are TOTP codes generated
        :param unicode config_skew: The number of past and future time-steps valid at a given time
        :param unicode config_code_length: Number of digits for generated TOTP codes
        :param NewFactorInstance.TotpAlgorithms config_alg: The algorithm used to derive the TOTP codes

        :returns: The created NewFactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.new_factor.NewFactorInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'FactorType': factor_type,
            'Binding.Alg': binding_alg,
            'Binding.PublicKey': binding_public_key,
            'Config.AppId': config_app_id,
            'Config.NotificationPlatform': config_notification_platform,
            'Config.NotificationToken': config_notification_token,
            'Config.SdkVersion': config_sdk_version,
            'Binding.Secret': binding_secret,
            'Config.TimeStep': config_time_step,
            'Config.Skew': config_skew,
            'Config.CodeLength': config_code_length,
            'Config.Alg': config_alg,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return NewFactorInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.NewFactorList>'


class NewFactorPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the NewFactorPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Sid.
        :param identity: Unique external identifier of the Entity

        :returns: twilio.rest.verify.v2.service.entity.new_factor.NewFactorPage
        :rtype: twilio.rest.verify.v2.service.entity.new_factor.NewFactorPage
        """
        super(NewFactorPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of NewFactorInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.entity.new_factor.NewFactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.new_factor.NewFactorInstance
        """
        return NewFactorInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            identity=self._solution['identity'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.NewFactorPage>'


class NewFactorInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class FactorStatuses(object):
        UNVERIFIED = "unverified"
        VERIFIED = "verified"

    class FactorTypes(object):
        PUSH = "push"
        TOTP = "totp"

    class NotificationPlatforms(object):
        APN = "apn"
        FCM = "fcm"
        NONE = "none"

    class TotpAlgorithms(object):
        SHA1 = "sha1"
        SHA256 = "sha256"
        SHA512 = "sha512"

    def __init__(self, version, payload, service_sid, identity):
        """
        Initialize the NewFactorInstance

        :returns: twilio.rest.verify.v2.service.entity.new_factor.NewFactorInstance
        :rtype: twilio.rest.verify.v2.service.entity.new_factor.NewFactorInstance
        """
        super(NewFactorInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'entity_sid': payload.get('entity_sid'),
            'identity': payload.get('identity'),
            'binding': payload.get('binding'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'friendly_name': payload.get('friendly_name'),
            'status': payload.get('status'),
            'factor_type': payload.get('factor_type'),
            'config': payload.get('config'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'identity': identity, }

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Factor.
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
    def service_sid(self):
        """
        :returns: Service Sid.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def entity_sid(self):
        """
        :returns: Entity Sid.
        :rtype: unicode
        """
        return self._properties['entity_sid']

    @property
    def identity(self):
        """
        :returns: Unique external identifier of the Entity
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def binding(self):
        """
        :returns: Unique external identifier of the Entity
        :rtype: dict
        """
        return self._properties['binding']

    @property
    def date_created(self):
        """
        :returns: The date this Factor was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Factor was updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description of this resource.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def status(self):
        """
        :returns: The Status of this Factor
        :rtype: NewFactorInstance.FactorStatuses
        """
        return self._properties['status']

    @property
    def factor_type(self):
        """
        :returns: The Type of this Factor
        :rtype: NewFactorInstance.FactorTypes
        """
        return self._properties['factor_type']

    @property
    def config(self):
        """
        :returns: Binding for a `factor_type`.
        :rtype: dict
        """
        return self._properties['config']

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
        return '<Twilio.Verify.V2.NewFactorInstance>'
