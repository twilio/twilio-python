from twilio.rest.serverless import ServerlessBase
from warnings import warn


class Serverless(ServerlessBase):

    @property
    def services(self):
        warn('services() is deprecated. Use v1.services() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.services
