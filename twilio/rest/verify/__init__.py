from twilio.rest.verify import VerifyBase
from warnings import warn


class Verify(VerifyBase):

    @property
    def forms(self):
        warn('forms is deprecated. Use v2.forms instead.', DeprecationWarning, stacklevel=2)
        return self.v2.forms

    @property
    def safelist(self):
        warn('safelist is deprecated. Use v2.safelist instead.', DeprecationWarning, stacklevel=2)
        return self.v2.safelist

    @property
    def services(self):
        warn('services is deprecated. Use v2.services instead.', DeprecationWarning, stacklevel=2)
        return self.v2.services

    @property
    def verification_attempts(self):
        warn('verification_attempts is deprecated. Use v2.verification_attempts instead.', DeprecationWarning, stacklevel=2)
        return self.v2.verification_attempts

    @property
    def verification_attempts_summary(self):
        warn('verification_attempts_summary is deprecated. Use v2.verification_attempts_summary instead.', DeprecationWarning, stacklevel=2)
        return self.v2.verification_attempts_summary

    @property
    def templates(self):
        warn('templates is deprecated. Use v2.templates instead.', DeprecationWarning, stacklevel=2)
        return self.v2.templates
