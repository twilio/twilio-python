from twilio.rest.pricing import PricingBase
from warnings import warn


class Pricing(PricingBase):

    @property
    def messaging(self):
        warn('messaging() is deprecated. Use v1.messaging() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.messaging

    @property
    def phone_numbers(self):
        warn('phone_numbers() is deprecated. Use v1.phone_numbers() instead.', DeprecationWarning, stacklevel=2)
        return self.v1.phone_numbers

    @property
    def voice(self):
        warn('voice() is deprecated. Use v2.voice() instead.', DeprecationWarning, stacklevel=2)
        return self.v2.voice

    @property
    def countries(self):
        warn('countries() is deprecated. Use v2.countries() instead.', DeprecationWarning, stacklevel=2)
        return self.v2.countries

    @property
    def numbers(self):
        warn('numbers() is deprecated. Use v2.numbers() instead.', DeprecationWarning, stacklevel=2)
        return self.v2.numbers
