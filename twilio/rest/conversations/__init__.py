from twilio.rest.conversations import ConversationsBase
from warnings import warn


class Conversations(ConversationsBase):

    @property
    def configuration(self):
        warn('configuration() is deprecated. Use v1.configuration() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.configuration

    @property
    def address_configurations(self):
        warn('address_configurations() is deprecated. Use v1.address_configurations() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.address_configurations

    @property
    def conversations(self):
        warn('conversations() is deprecated. Use v1.conversations() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.conversations

    @property
    def credentials(self):
        warn('credentials() is deprecated. Use v1.credentials() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.credentials

    @property
    def participant_conversations(self):
        warn('participant_conversations() is deprecated. Use v1.participant_conversations() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.participant_conversations

    @property
    def roles(self):
        warn('roles() is deprecated. Use v1.roles() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.roles

    @property
    def services(self):
        warn('services() is deprecated. Use v1.services() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.services

    @property
    def users(self):
        warn('users() is deprecated. Use v1.users() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.users



