"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.microvisor.v1.account_config import AccountConfigList
from twilio.rest.microvisor.v1.account_secret import AccountSecretList
from twilio.rest.microvisor.v1.app import AppList
from twilio.rest.microvisor.v1.device import DeviceList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Microvisor

        :param domain: The Twilio.microvisor domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._account_configs = None
        self._account_secrets = None
        self._apps = None
        self._devices = None
        
    @property
    def account_configs(self) -> AccountConfigList:
        """
        :rtype: twilio.rest.microvisor.v1.account_config.AccountConfigList
        """
        if self._account_configs is None:
            self._account_configs = AccountConfigList(self)
        return self._account_configs

    @property
    def account_secrets(self) -> AccountSecretList:
        """
        :rtype: twilio.rest.microvisor.v1.account_secret.AccountSecretList
        """
        if self._account_secrets is None:
            self._account_secrets = AccountSecretList(self)
        return self._account_secrets

    @property
    def apps(self) -> AppList:
        """
        :rtype: twilio.rest.microvisor.v1.app.AppList
        """
        if self._apps is None:
            self._apps = AppList(self)
        return self._apps

    @property
    def devices(self) -> DeviceList:
        """
        :rtype: twilio.rest.microvisor.v1.device.DeviceList
        """
        if self._devices is None:
            self._devices = DeviceList(self)
        return self._devices

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Microvisor.V1>'
