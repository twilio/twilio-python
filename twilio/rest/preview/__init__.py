from twilio.rest.preview import PreviewBase
from warnings import warn


class Preview(PreviewBase):

    @property
    def fleets(self):
        warn('fleets is deprecated. Use deployed_devices.fleets instead.', DeprecationWarning, stacklevel=2)
        return self.deployed_devices.fleets

    @property
    def authorization_documents(self):
        warn('authorization_documents is deprecated. Use hosted_numbers.authorization_documents instead.', DeprecationWarning, stacklevel=2)
        return self.hosted_numbers.authorization_documents

    @property
    def hosted_number_orders(self):
        warn('hosted_number_orders is deprecated. Use hosted_numbers.hosted_number_orders instead.', DeprecationWarning, stacklevel=2)
        return self.hosted_numbers.hosted_number_orders

    @property
    def available_add_ons(self):
        warn('available_add_ons is deprecated. Use marketplace.available_add_ons instead.', DeprecationWarning, stacklevel=2)
        return self.marketplace.available_add_ons

    @property
    def installed_add_ons(self):
        warn('installed_add_ons is deprecated. Use marketplace.installed_add_ons instead.', DeprecationWarning, stacklevel=2)
        return self.marketplace.installed_add_ons

    @property
    def services(self):
        warn('services is deprecated. Use sync.services instead.', DeprecationWarning, stacklevel=2)
        return self.sync.services

    @property
    def assistants(self):
        warn('assistants is deprecated. Use understand.assistants instead.', DeprecationWarning, stacklevel=2)
        return self.understand.assistants

    @property
    def commands(self):
        warn('commands is deprecated. Use wireless.commands instead.', DeprecationWarning, stacklevel=2)
        return self.wireless.commands

    @property
    def rate_plans(self):
        warn('rate_plans is deprecated. Use wireless.rate_plans instead.', DeprecationWarning, stacklevel=2)
        return self.wireless.rate_plans

    @property
    def sims(self):
        warn('sims is deprecated. Use wireless.sims instead.', DeprecationWarning, stacklevel=2)
        return self.wireless.sims
