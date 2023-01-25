from twilio.rest.trunking import TrunkingBase
from warnings import warn


class Trunking(TrunkingBase):

    @property
    def trunks(self):
        warn('trunks() is deprecated. Use v1.trunks() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.trunks
