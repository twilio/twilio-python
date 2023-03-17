r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Content
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.content.v1.content import ContentList
from twilio.rest.content.v1.legacy_content import LegacyContentList


class V1(Version):
    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Content

        :param domain: The Twilio.content domain
        """
        super().__init__(domain, "v1")
        self._contents = None
        self._legacy_contents = None

    @property
    def contents(self) -> ContentList:
        if self._contents is None:
            self._contents = ContentList(self)
        return self._contents

    @property
    def legacy_contents(self) -> LegacyContentList:
        if self._legacy_contents is None:
            self._legacy_contents = LegacyContentList(self)
        return self._legacy_contents

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        """
        return "<Twilio.Content.V1>"
