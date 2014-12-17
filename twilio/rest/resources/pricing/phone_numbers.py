from .. import InstanceResource, ListResource


class PhoneNumbers(object):
    """Holds references to the Number pricing resources."""

    name = "Number"
    key = "Number"

    def __init__(self, base_uri, auth, timeout):
        self.uri = "%s/PhoneNumbers" % base_uri
        self.countries = PhoneNumberCountries(self.uri, auth, timeout)


class PhoneNumberCountry(InstanceResource):
    """Pricing information for Twilio Phone Numbers in a specific country.

    .. attribute:: country

        The full name of the country.

    .. attribute:: iso_country

        The country's 2-character ISO code.

    .. attribute:: price_unit

        The currency in which prices are measured, in ISO 4127 format
        (e.g. 'usd', 'eur', 'jpy').

    .. attribute:: phone_number_prices

        A list of dicts containing pricing information as follows:
            - type: "local", "mobile", "national", or "toll_free"
            - base_price: the base price per month for this Twilio number type
            - current_price: the current price per month (including discounts)
            for this Twilio number type
    """

    id_key = "iso_country"


class PhoneNumberCountries(ListResource):

    instance = PhoneNumberCountry
    key = "countries"
    name = "Countries"

    def get(self, iso_country):
        """Retrieve pricing information for Twilio Number in the specified
        country.

        :param iso_country: The two-letter ISO code for the country
        """
        return self.get_instance(iso_country)

    def list(self):
        """Retrieve the list of countries in which Twilio Number is available."""

        resp, page = self.request("GET", self.uri)

        return [self.load_instance(i) for i in page[self.key]]
