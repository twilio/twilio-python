r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Pricing
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Optional
from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.pricing.v1.messaging import MessagingList
from twilio.rest.pricing.v1.phone_number import PhoneNumberList
from twilio.rest.pricing.v1.voice import VoiceList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Pricing

        :param domain: The Twilio.pricing domain
        """
        super().__init__(domain, "v1")
        self._messaging: Optional[MessagingList] = None
        self._phone_numbers: Optional[PhoneNumberList] = None
        self._voice: Optional[VoiceList] = None
        
    @property
    def messaging(self) -> MessagingList:
        if self._messaging is None:
            self._messaging = MessagingList(self)
        return self._messaging

    @property
    def phone_numbers(self) -> PhoneNumberList:
        if self._phone_numbers is None:
            self._phone_numbers = PhoneNumberList(self)
        return self._phone_numbers

    @property
    def voice(self) -> VoiceList:
        if self._voice is None:
            self._voice = VoiceList(self)
        return self._voice

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Pricing.V1>"
