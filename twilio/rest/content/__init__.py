from twilio.rest.content import ContentBase
from warnings import warn


class Content(ContentBase):

    @property
    def contents(self):
        warn('contents() is deprecated. Use v1.contents() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.contents
