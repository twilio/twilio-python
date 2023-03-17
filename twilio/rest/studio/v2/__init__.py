r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Studio
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.studio.v2.flow import FlowList
from twilio.rest.studio.v2.flow_validate import FlowValidateList


class V2(Version):
    def __init__(self, domain: Domain):
        """
        Initialize the V2 version of Studio

        :param domain: The Twilio.studio domain
        """
        super().__init__(domain, "v2")
        self._flows = None
        self._flow_validate = None

    @property
    def flows(self) -> FlowList:
        if self._flows is None:
            self._flows = FlowList(self)
        return self._flows

    @property
    def flow_validate(self) -> FlowValidateList:
        if self._flow_validate is None:
            self._flow_validate = FlowValidateList(self)
        return self._flow_validate

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Studio.V2>"
