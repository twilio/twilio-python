from twilio.rest.resources import transform_params
from twilio.rest.lookups.phone_number import (
    PhoneNumber,
    PhoneNumbers as BasePhoneNumbers
)
from twilio.rest.resources.base import GetQuery


class PhoneNumbers(BasePhoneNumbers):

    def get(self, number, include_carrier_info=False, country_code=None):
        params = {}
        if country_code is not None:
            params['country_code'] = country_code

        if include_carrier_info:
            params['type'] = 'carrier'

        uri = '%s/%s' % (self.uri, number)
        return GetQuery(self, uri, self.use_json_extension, params=params)
