from twilio.rest.numbers import NumbersBase
from warnings import warn


class Numbers(NumbersBase):

    @property
    def regulatory_compliance(self):
        warn('regulatory_compliance() is deprecated. Use v2.regulatory_compliance() instead.', DeprecationWarning, stacklevel=2)
        return self.v2.regulatory_compliance
