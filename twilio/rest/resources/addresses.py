from twilio.rest.v2010.account.address.dependent_phone_number import (
    DependentPhoneNumber,
    DependentPhoneNumbers,
)
from twilio.rest.v2010.account.address import (
    Address,
    Addresses as BaseAddresses
)


class Addresses(BaseAddresses):

    def list(self, customer_name=None, friendly_name=None, iso_country=None):
        kwargs = {
            'customer_name': customer_name,
            'friendly_name': friendly_name,
            'iso_country': iso_country,
        }
        return self.get_instances(kwargs)

    def create(self, customer_name, street, city, region, postal_code,
               iso_country, friendly_name=None):
        """Create an :class:`Address`.

        :param str customer_name: Your customer's name
        :param str street: The number and street of your address
        :param str city: The city of you or your customer's address
        :param str region: The region or state
        :param str postal_code: The postal code of your address
        :param str iso_country: The ISO 3166-1 alpha-2 (two-character)
            country code, e.g. 'US' or 'AU'
        :param str friendly_name: A user-defined name for this address
            (optional; up to 64 characters)
        """
        kwargs = {
            'customer_name': customer_name,
            'street': street,
            'city': city,
            'region': region,
            'postal_code': postal_code,
            'iso_country': iso_country,
        }

        if friendly_name is not None:
            kwargs['friendly_name'] = friendly_name

        return self.create_instance(kwargs)
