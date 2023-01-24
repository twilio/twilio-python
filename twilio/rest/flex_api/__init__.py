from twilio.rest.flex_api import FlexApiBase
from warnings import warn


class FlexApi(FlexApiBase):

    @property
    def assessments(self):
        warn('assessments() is deprecated. Use v1.assessments() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.assessments

    @property
    def channel(self):
        warn('channel() is deprecated. Use v1.channel() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.channel

    @property
    def configuration(self):
        warn('configuration() is deprecated. Use v1.configuration() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.configuration

    @property
    def flex_flow(self):
        warn('flex_flow() is deprecated. Use v1.flex_flow() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.flex_flow

    @property
    def good_data(self):
        warn('good_data() is deprecated. Use v1.good_data() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.good_data

    @property
    def interaction(self):
        warn('interaction() is deprecated. Use v1.interaction() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.interaction

    @property
    def user_roles(self):
        warn('user_roles() is deprecated. Use v1.user_roles() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.user_roles

    @property
    def web_channel(self):
        warn('web_channel() is deprecated. Use v1.web_channel() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.web_channel

    @property
    def web_channels(self):
        warn('web_channels() is deprecated. Use v2.web_channels() instead.', DeprecationWarning, stacklevel=2)
        return self.v2.web_channels

