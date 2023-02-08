from twilio.rest.chat import ChatBase
from warnings import warn


class Chat(ChatBase):

    @property
    def credentials(self):
        warn('credentials is deprecated. Use v2.credentials instead.', DeprecationWarning, stacklevel=2)
        return self.v2.credentials

    @property
    def services(self):
        warn('services is deprecated. Use v2.services instead.', DeprecationWarning, stacklevel=2)
        return self.v2.services

    @property
    def channels(self):
        warn('channels is deprecated. Use v3.channels instead.', DeprecationWarning, stacklevel=2)
        return self.v3.channels
