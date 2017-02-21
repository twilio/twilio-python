from .. import NextGenInstanceResource, NextGenListResource


class Messaging(object):
    """Holds references to the Messaging pricing resources."""

    name = "Messaging"
    key = "messaging"

    def __init__(self, base_uri, auth, timeout):
        self.uri = "%s/Messaging" % base_uri
        self.countries = MessagingCountries(self.uri, auth, timeout)


class MessagingCountry(NextGenInstanceResource):
    """Pricing information for Twilio Messages in a specific country.

    .. attribute:: country

        The full name of the country.

    .. attribute:: iso_country

        The country's 2-character ISO code.

    .. attribute:: price_unit

        The currency in which prices are measured, in ISO 4127 format
        (e.g. 'usd', 'eur', 'jpy').

    .. attribute:: outbound_sms_prices

        A list of dicts containing pricing information as follows:
            - prefix_list: a list of number prefixes in the requested country
              that have the same pricing
            - friendly_name: a descriptive name for this prefix set
            - call_base_price: the base price per minute for calls to numbers
              matching any of these prefixes
            - call_current_price: the current price per minute (including
              volume discounts, etc.) for your account to make calls to
              numbers matching these prefixes

    .. attribute:: inbound_sms_prices

        A list of dicts containing pricing information for inbound calls:
            - number_type: 'local', 'mobile', 'national', or 'toll_free'
            - call_base_price: the base price per minute to receive a call
              to this number type
            - call_current_price: the current price per minute (including
              volume discounts, etc.) for your account to receive a call
              to this number type
    """
    id_key = "iso_country"


class MessagingCountries(NextGenListResource):
    """A list of countries where Twilio Messages are available.

    The returned list of MessagingCountry objects will not have pricing
    information populated. To get pricing information for a specific country,
    retrieve it with the :meth:`get` method.
    """

    instance = MessagingCountry
    key = "countries"
    name = "Countries"

    def get(self, iso_country):
        """Retrieve pricing information for Twilio Messages in the specified
        country.

        :param iso_country: The two-letter ISO code for the country
        """
        return self.get_instance(iso_country)

    def list(self, **kwargs):
        """Retrieve the list of countries in which Twilio Messages are
        available."""

        return super(MessagingCountries, self).list(**kwargs)
