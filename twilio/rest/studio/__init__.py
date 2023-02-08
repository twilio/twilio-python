from twilio.rest.studio import StudioBase
from warnings import warn


class Studio(StudioBase):

    @property
    def flows(self):
        warn('flows is deprecated. Use v2.flows instead.', DeprecationWarning, stacklevel=2)
        return self.v2.flows

    @property
    def flow_validate(self):
        warn('flow_validate is deprecated. Use v2.flow_validate instead.', DeprecationWarning, stacklevel=2)
        return self.v2.flow_validate
