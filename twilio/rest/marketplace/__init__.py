from twilio.rest.marketplace.MarketplaceBase import MarketplaceBase


class Marketplace(MarketplaceBase):
    def available_add_ons(self):
        return self.v1.available_add_ons

    def installed_add_ons(self):
        return self.v1.installed_add_ons
