from twilio.rest.lookups import LookupsBase
from warnings import warn


class Lookups(LookupsBase):

    @property
    def phone_numbers(self):
        warn('phone_numbers() is deprecated. Use v1.phone_numbers() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.phone_numbers
