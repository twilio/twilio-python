from twilio.rest.routes import RoutesBase
from warnings import warn


class Routes(RoutesBase):

    @property
    def phone_numbers(self):
        warn('phone_numbers is deprecated. Use v2.phone_numbers instead.', DeprecationWarning, stacklevel=2)
        return self.v2.phone_numbers

    @property
    def sip_domains(self):
        warn('sip_domains is deprecated. Use v2.sip_domains instead.', DeprecationWarning, stacklevel=2)
        return self.v2.sip_domains

    @property
    def trunks(self):
        warn('trunks is deprecated. Use v2.trunks instead.', DeprecationWarning, stacklevel=2)
        return self.v2.trunks
