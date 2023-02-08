from twilio.rest.messaging import MessagingBase
from warnings import warn


class Messaging(MessagingBase):

    @property
    def brand_registrations(self):
        warn('brand_registrations is deprecated. Use v1.brand_registrations instead.', DeprecationWarning, stacklevel=2)
        return self.v1.brand_registrations

    @property
    def deactivations(self):
        warn('deactivations is deprecated. Use v1.deactivations instead.', DeprecationWarning, stacklevel=2)
        return self.v1.deactivations

    @property
    def domain_certs(self):
        warn('domain_certs is deprecated. Use v1.domain_certs instead.', DeprecationWarning, stacklevel=2)
        return self.v1.domain_certs

    @property
    def domain_config(self):
        warn('domain_config is deprecated. Use v1.domain_config instead.', DeprecationWarning, stacklevel=2)
        return self.v1.domain_config

    @property
    def external_campaign(self):
        warn('external_campaign is deprecated. Use v1.external_campaign instead.', DeprecationWarning, stacklevel=2)
        return self.v1.external_campaign

    @property
    def services(self):
        warn('services is deprecated. Use v1.services instead.', DeprecationWarning, stacklevel=2)
        return self.v1.services

    @property
    def tollfree_verifications(self):
        warn('tollfree_verifications is deprecated. Use v1.tollfree_verifications instead.', DeprecationWarning, stacklevel=2)
        return self.v1.tollfree_verifications

    @property
    def usecases(self):
        warn('usecases is deprecated. Use v1.usecases instead.', DeprecationWarning, stacklevel=2)
        return self.v1.usecases
