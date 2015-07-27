from twilio.exceptions import TwilioException
from twilio.rest.resources.base import InstanceResource, ListResource
from twilio.rest.resources.util import transform_params


TYPES = {"local": "Local", "tollfree": "TollFree", "mobile": "Mobile"}


class AvailablePhoneNumber(InstanceResource):
    def __init__(self, parent, *args, **kwargs):
        # Available Phone Numbers have no sid.
        super(AvailablePhoneNumber, self).__init__(parent.phone_numbers, None)

    def purchase(self, **kwargs):
        return self.parent.purchase(phone_number=self.phone_number,
                                    **kwargs)


class AvailablePhoneNumbers(ListResource):

    def __init__(self, base_uri, auth, timeout, phone_numbers):
        super(AvailablePhoneNumbers, self).__init__(base_uri, auth, timeout)
        self.phone_numbers = phone_numbers

    def get(self, sid):
        raise TwilioException("Individual AvailablePhoneNumbers have no sid")

    def list(self, type="local", country="US", region=None, postal_code=None,
             lata=None, rate_center=None, **kwargs):
        """
        Search for phone numbers
        """
        kwargs["in_region"] = kwargs.get("in_region", region)
        kwargs["in_postal_code"] = kwargs.get("in_postal_code", postal_code)
        kwargs["in_lata"] = kwargs.get("in_lata", lata)
        kwargs["in_rate_center"] = kwargs.get("in_rate_center", rate_center)
        params = transform_params(kwargs)

        uri = "%s/%s/%s" % (self.uri, country, TYPES[type])
        resp, page = self.request("GET", uri, params=params)

        return [self.load_instance(i) for i in page[self.key]]

