from twilio.rest.resources.available_phone_numbers import AvailablePhoneNumbers
from twilio.rest.resources.base import ListResource, InstanceResource
from twilio.rest.resources.util import UNSET_TIMEOUT, transform_params, change_dict_key

TYPES = {"local": "Local", "tollfree": "TollFree", "mobile": "Mobile"}


class IncomingPhoneNumber(InstanceResource):
    pass


class IncomingPhoneNumbers(ListResource):

    def __init__(self, base_uri, auth, timeout=UNSET_TIMEOUT):
        super(IncomingPhoneNumbers, self).__init__(base_uri, auth, timeout)
        self.available_phone_numbers = \
            AvailablePhoneNumbers(base_uri, auth, timeout, self)

    def list(self, type=None, **kwargs):
        """
        :param phone_number: Show phone numbers that match this pattern.
        :param friendly_name: Show phone numbers with this friendly name
        :param type: Filter numbers by type. Available types are
            'local', 'mobile', or 'tollfree'

        You can specify partial numbers and use '*' as a wildcard.
        """

        uri = self.uri
        if type:
            uri = "%s/%s" % (self.uri, TYPES[type])

        params = transform_params(kwargs)
        resp, page = self.request("GET", uri, params=params)

        return [self.load_instance(i) for i in page[self.key]]

    def purchase(self, status_callback_url=None, **kwargs):
        """
        Attempt to purchase the specified number. The only required parameters
        are **either** phone_number or area_code

        :returns: Returns a :class:`PhoneNumber` instance on success,
                  :data:`False` on failure
        :raises: A :exc:`TypeError` if neither phone_number or area_code
        is specified.
        """
        kwargs["StatusCallback"] = kwargs.get("status_callback",
                                              status_callback_url)

        if 'phone_number' not in kwargs and 'area_code' not in kwargs:
            raise TypeError("phone_number or area_code is required")

        number_type = kwargs.pop('type', False)
        uri = self.uri
        if number_type:
            uri = "%s/%s" % (self.uri, TYPES[number_type])

        params = transform_params(kwargs)
        resp, instance = self.request('POST', uri, data=params)

        return self.load_instance(instance)

    def search(self, **kwargs):
        """
        :param type: The type of phone number to search for.
        :param str country: Only show numbers for this country (iso2)
        :param str region: When searching the US, show numbers in this state
        :param str postal_code: Only show numbers in this area code
        :param str rate_center: US only.
        :param tuple near_lat_long: Find close numbers within Distance miles.
        :param integer distance: Search radius for a Near- query in miles.
        :param boolean beta: Whether to include numbers new to the Twilio
            platform.
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
        kwargs_copy = dict(kwargs)
        change_dict_key(kwargs_copy, from_key="status_callback_url",
                        to_key="status_callback")

        if "application_sid" in kwargs_copy:
            for sid_type in ["voice_application_sid", "sms_application_sid"]:
                if sid_type not in kwargs_copy:
                    kwargs_copy[sid_type] = kwargs_copy["application_sid"]
            del kwargs_copy["application_sid"]
        return self.update_instance(sid, kwargs_copy)
