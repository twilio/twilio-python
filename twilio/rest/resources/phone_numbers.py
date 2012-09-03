import re

from twilio import TwilioException
from twilio.rest.resources.util import transform_params
from twilio.rest.resources import InstanceResource, ListResource


class AvailablePhoneNumber(InstanceResource):
    """ An available phone number resource """

    def __init__(self, parent):
        super(AvailablePhoneNumber, self).__init__(parent, "")
        self.name = ""

    def purchase(self, **kwargs):
        return self.parent.purchase(phone_number=self.phone_number,
                                    **kwargs)


class AvailablePhoneNumbers(ListResource):

    name = "AvailablePhoneNumbers"
    key = "available_phone_numbers"
    instance = AvailablePhoneNumber

    types = {"local": "Local", "tollfree": "TollFree"}

    def __init__(self, base_uri, auth, phone_numbers):
        super(AvailablePhoneNumbers, self).__init__(base_uri, auth)
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

        uri = "%s/%s/%s" % (self.uri, country, self.types[type])
        resp, page = self.request("GET", uri, params=params)

        return [self.load_instance(i) for i in page[self.key]]

    def load_instance(self, data):
        instance = self.instance(self.phone_numbers)
        instance.load(data)
        instance.load_subresources()
        return instance


class PhoneNumber(InstanceResource):

    def load(self, entries):
        """ Set the proper Account owner of this phone number """

        # Only check if entries has a uri
        if "account_sid" in entries:
            # Parse the parent's uri to get the scheme and base
            uri = re.sub(r'AC(.*)', entries["account_sid"],
                self.parent.base_uri)

            self.parent = PhoneNumbers(uri, self.parent.auth)
            self.base_uri = self.parent.uri

        super(PhoneNumber, self).load(entries)

    def transfer(self, account_sid):
        """
        Transfer the phone number with sid from the current account to another
        identified by account_sid
        """
        a = self.parent.transfer(self.name, account_sid)
        self.load(a.__dict__)

    def update(self, **kwargs):
        """
        Update this phone number instance.
        """
        a = self.parent.update(self.name, **kwargs)
        self.load(a.__dict__)

    def delete(self):
        """
        Release this phone number from your account. Twilio will no longer
        answer calls to this number, and you will stop being billed the monthly
        phone number fees. The phone number will eventually be recycled and
        potentially given to another customer, so use with care. If you make a
        mistake, contact us... we may be able to give you the number back.
        """
        return self.parent.delete(self.name)


class PhoneNumbers(ListResource):

    name = "IncomingPhoneNumbers"
    key = "incoming_phone_numbers"
    instance = PhoneNumber

    def __init__(self, base_uri, auth):
        super(PhoneNumbers, self).__init__(base_uri, auth)
        self.available_phone_numbers = \
            AvailablePhoneNumbers(base_uri, auth, self)

    def delete(self, sid):
        """
        Release this phone number from your account. Twilio will no longer
        answer calls to this number, and you will stop being billed the
        monthly phone number fees. The phone number will eventually be
        recycled and potentially given to another customer, so use with care.
        If you make a mistake, contact us... we may be able to give you the
        number back.
        """
        return self.delete_instance(sid)

    def list(self, **kwargs):
        """
        :param phone_number: Show phone numbers that match this pattern.
        :param friendly_name: Show phone numbers with this friendly name

        You can specify partial numbers and use '*' as a wildcard.
        """
        return self.get_instances(kwargs)

    def purchase(self, status_callback_url=None, **kwargs):
        """
        Attempt to purchase the specified number. The only required parameters
        are **either** phone_number or area_code

        :returns: Returns a :class:`PhoneNumber` instance on success,
                  :data:`False` on failure
        """
        kwargs["StatusCallback"] = kwargs.get("status_callback",
                                              status_callback_url)

        if 'phone_number' not in kwargs and 'area_code' not in kwargs:
            raise TypeError("phone_number or area_code is required")

        return self.create_instance(kwargs)

    def search(self, **kwargs):
        """
        :param type: The type of phone number to search for.
        :param string country: Either "US" or "CA". Defaults to "US"
        :param string region: When searching the US, show numbers in this state
        :param string postal_code: Only show numbers in this area code
        :param string rate_center: US only.
        :param tuple near_lat_long: Find close numbers within Distance miles.
        :param integer distance: Search radius for a Near- query in miles.
        """
        return self.available_phone_numbers.list(**kwargs)

    def transfer(self, sid, account_sid):
        """
        Transfer the phone number with sid from the current account to another
        identified by account_sid
        """
        return self.update(sid, account_sid=account_sid)

    def update(self, sid, **kwargs):
        """
        Update this phone number instance
        """
        if "application_sid" in kwargs:
            for sid_type in ["voice_application_sid", "sms_application_sid"]:
                if sid_type not in kwargs:
                    kwargs[sid_type] = kwargs["application_sid"]
            del kwargs["application_sid"]
        return self.update_instance(sid, kwargs)
