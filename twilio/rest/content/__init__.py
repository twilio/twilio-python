from warnings import warn

from twilio.rest.content.ContentBase import ContentBase
from twilio.rest.content.v1.content import ContentList
from twilio.rest.content.v1.legacy_content import LegacyContentList


class Content(ContentBase):
    @property
    def contents(self) -> ContentList:
        warn(
            "contents is deprecated. Use v1.contents instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.contents

    @property
    def legacy_contents(self) -> LegacyContentList:
        warn(
            "legacy_contents is deprecated. Use v1.legacy_contents instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.v1.legacy_contents
