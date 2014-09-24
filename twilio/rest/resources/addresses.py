from twilio.exceptions import TwilioException
from twilio.rest.resources import InstanceResource, ListResource


class DependentPhoneNumber(InstanceResource):
    pass


class DependentPhoneNumbers(ListResource):
    name = "DependentPhoneNumbers"
    key = "dependent_phone_numbers"
    instance = DependentPhoneNumber


class Address(InstanceResource):
    """An Address resource. See [url].

    .. attribute:: friendly_name

        A human-readable description of this address. Maximum 64 characters.

    .. attribute:: customer_name

        Your or your customer's name or business name.

    .. attribute:: street

        The number and street address where you or your customer are located.

    .. attribute:: city

        The city in which you or your customer are located.

    .. attribute:: region

        The state or region in which you or your customer are located.

    .. attribute:: postal_code

        The postal code in which you or your customer are located.

    .. attribute:: iso_country

        The ISO country code of your or your customer's address.
    """
    subresources = [DependentPhoneNumbers]

    def update(self, **kwargs):
        """Update this phone number instance.

        Parameters are as described in :meth:`Addresses.create`, with
        the exception that `iso_country` cannot be updated on an existing
        Address (create a new one instead).
        """
        return self.parent.update(self.sid, kwargs)


class Addresses(ListResource):
    name = "Addresses"
    key = "addresses"
    instance = Address

    def list(self, customer_name=None, friendly_name=None, iso_country=None):
        kwargs = {
            'customer_name': customer_name,
            'friendly_name': friendly_name,
            'iso_country': iso_country,
        }
        return self.get_instances(kwargs)

    def create(self, customer_name, street, city, region, postal_code,
               iso_country, friendly_name=None):
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

    def update(self, sid, **kwargs):
        """Update an :class:`Address` with the given parameters.

        Parameters are described above in :meth:`create`, with
        the exception that `iso_country` cannot be updated on
        an existing Address (create a new one instead).
        """
        if 'iso_country' in kwargs:
            raise TwilioException("Cannot update iso_country on an existing Address")

        return self.update_instance(sid, kwargs)
