from twilio.rest.resources import transform_params
from twilio.rest.lookups.phone_number import (
    PhoneNumber,
    PhoneNumbers as BasePhoneNumbers
)


class PhoneNumbers(BasePhoneNumbers):

    def get(self, number, include_carrier_info=False, country_code=None):
        params = {}
        if country_code is not None:
            params['country_code'] = country_code

        if include_carrier_info:
            params['type'] = 'carrier'

        params = transform_params(params)
        uri = '%s/%s' % (self.uri, number)
        _, item = self.request('GET', uri, params=params)

        return self.load_instance(item)
