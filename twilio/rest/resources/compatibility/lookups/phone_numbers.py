from twilio.rest.resources.base import NextGenInstanceResource, NextGenListResource
from twilio.rest.resources.util import transform_params


class PhoneNumber(NextGenInstanceResource):
    pass


class PhoneNumbers(NextGenListResource):

    def get(self, number, include_carrier_info=False, country_code=None):
        """Look up a phone number.

        :param str number: The phone number to query.
        :param bool include_carrier_info: Whether to do a carrier lookup on
            the phone number. See twilio.com for the latest pricing.
        :param str country_code: If the number is provided in a local format
        rather than E.164, specify the two-letter code of the country to parse
        the number for.
        """

        params = {}
        if country_code is not None:
            params['country_code'] = country_code

        if include_carrier_info:
            params['type'] = 'carrier'

        params = transform_params(params)
        uri = "%s/%s" % (self.uri, number)
        _, item = self.request("GET", uri, params=params)

        return self.load_instance(item)
